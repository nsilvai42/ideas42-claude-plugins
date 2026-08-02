#!/usr/bin/env python3
"""Adaptive sample-description profiler.

Reads a cleaned tabular dataset and produces:
  - Numeric profile CSV     (05_Numeric-Profile.csv)
  - Categorical profile CSV (06_Categorical-Profile.csv)
  - Quality metrics CSV     (07_Quality-Metrics.csv) — retention, missingness, cell sizes
  - Column classification   (column_classification.json) — used by downstream scripts

Designed to be invoked by SKILL.md but also runnable standalone:
    python profile_data.py --config /abs/path/to/config.json
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", message="Could not infer format")
warnings.filterwarnings("ignore", category=UserWarning, module="dateutil")

# ---------------------------------------------------------------------------
# Heuristics
# ---------------------------------------------------------------------------

PII_PATTERNS = {
    "email":   r"(^|_)e?mail$",
    "name":    r"(^|_)(first|last|full|recipient_?\w*)?_?name$",
    "phone":   r"(^|_)(phone|mobile|tel|cell)$",
    "ssn":     r"(^|_)(ssn|social_security|tax_id|tin)$",
    "govt_id": r"(^|_)(passport|drivers_license|license_no|ein)$",
    "finance": r"(^|_)(account_number|card_number|bank_account)$",
    "health":  r"(^|_)(mrn|medical_record|diagnosis|icd(_?\d+)?)$",
    "address": r"(^|_)(home_address|street_address|mailing_address)$",
    "geo":     r"(latitude|longitude|^lat$|^lng$|^gps|coordinates)",
    "ip":      r"(ip_?address|device_id|mac_?address)",
    "dob":     r"(^dob$|date_of_birth|birth_date)",
}

DEMOGRAPHIC_PATTERNS = [
    r"^age($|_)", r"^sex$", r"^gender$", r"^race$", r"^ethnicity",
    r"^income", r"^education", r"^employment", r"^state$", r"^country",
    r"^nationality$", r"^language$", r"^marital", r"^household",
    r"^zip", r"^region$", r"^urban_?rural",
]
BEHAVIORAL_PATTERNS = [
    r"caregiver", r"^prior_", r"experience", r"^goals?$",
    r"interest", r"recruitment_?", r"referral",
]
QUALITY_PATTERNS = [
    r"attention_?check", r"recaptcha", r"^consent$", r"^finished$",
    r"^duration", r"^progress$", r"^status$", r"completed", r"^time(_taken)?_sec$",
]
TREATMENT_PATTERNS = [
    r"^treatment$", r"^arm$", r"^condition$", r"^group$",
    r"^variant$", r"^cohort$",
]
OUTCOME_PATTERNS = [
    r"^q\d+", r"_score$", r"_rating$", r"_ord$", r"likelihood", r"fairness", r"_response$",
]


def matches_any(name, patterns):
    name = name.lower()
    return any(re.search(p, name) for p in patterns)


# ---------------------------------------------------------------------------
# Type detection
# ---------------------------------------------------------------------------

def detect_type(series: pd.Series, name: str) -> str:
    name_low = name.lower()
    if "uuid" in name_low or name_low.endswith("_id") or name_low == "id":
        return "id"
    if pd.api.types.is_bool_dtype(series):
        return "boolean"
    if pd.api.types.is_datetime64_any_dtype(series):
        return "temporal"
    if pd.api.types.is_numeric_dtype(series):
        nu = series.nunique(dropna=True)
        rng = series.max() - series.min() if nu > 0 else 0
        if nu <= 10 and (rng <= 10 or name_low.endswith(("_ord", "_rank", "_scale"))):
            return "numeric_ordinal"
        if nu > 20 and rng > 50:
            return "numeric_continuous"
        return "numeric_ordinal" if nu <= 20 else "numeric_continuous"
    # string-ish
    if pd.api.types.is_string_dtype(series) or series.dtype == object:
        non_null = series.dropna().astype(str)
        if len(non_null) == 0:
            return "categorical_nominal"
        # detect date-strings
        try:
            pd.to_datetime(non_null.head(20), errors="raise")
            return "temporal"
        except Exception:
            pass
        nu = non_null.nunique()
        avg_len = non_null.str.len().mean()
        if avg_len > 50:
            return "text_free"
        if nu > 50:
            return "categorical_highcard"
        # check boolean-ish
        lowered = set(non_null.str.lower().unique())
        if lowered.issubset({"yes", "no", "true", "false", "y", "n", "0", "1"}):
            return "boolean"
        return "categorical_nominal"
    return "structural"


def detect_role(name: str) -> str:
    if matches_any(name, [p for p in PII_PATTERNS.values()]):
        return "pii_candidate"
    if matches_any(name, DEMOGRAPHIC_PATTERNS):
        return "demographic"
    if matches_any(name, QUALITY_PATTERNS):
        return "quality_flag"
    if matches_any(name, TREATMENT_PATTERNS):
        return "treatment_arm"
    if matches_any(name, OUTCOME_PATTERNS):
        return "outcome"
    if matches_any(name, BEHAVIORAL_PATTERNS):
        return "behavioral"
    return "metadata"


# ---------------------------------------------------------------------------
# Profile builders
# ---------------------------------------------------------------------------

def numeric_profile(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    rows = []
    n_total = len(df)
    for c in cols:
        s = pd.to_numeric(df[c], errors="coerce")
        n_nn = int(s.notna().sum())
        if n_nn == 0:
            rows.append({"col": c, "n_nonnull": 0, "n_null": n_total, "null_pct": 100.0})
            continue
        row = {
            "col": c,
            "n_nonnull": n_nn,
            "n_null": int(n_total - n_nn),
            "null_pct": round((n_total - n_nn) / n_total * 100, 2),
            "mean": round(float(s.mean()), 4),
            "median": round(float(s.median()), 4),
            "sd": round(float(s.std()), 4) if n_nn > 1 else None,
            "min": round(float(s.min()), 4),
            "p1": round(float(s.quantile(0.01)), 4),
            "p5": round(float(s.quantile(0.05)), 4),
            "p25": round(float(s.quantile(0.25)), 4),
            "p75": round(float(s.quantile(0.75)), 4),
            "p95": round(float(s.quantile(0.95)), 4),
            "p99": round(float(s.quantile(0.99)), 4),
            "max": round(float(s.max()), 4),
            "skew": round(float(s.skew()), 4) if n_nn > 2 else None,
            "n_zero": int((s == 0).sum()),
            "n_negative": int((s < 0).sum()),
        }
        rows.append(row)
    return pd.DataFrame(rows)


def categorical_profile(df: pd.DataFrame, cols: list, top_k: int = 15) -> pd.DataFrame:
    rows = []
    n_total = len(df)
    for c in cols:
        s = df[c]
        n_nn = int(s.notna().sum())
        vc = s.value_counts(dropna=False).head(top_k)
        for rank, (val, count) in enumerate(vc.items(), start=1):
            rows.append({
                "col": c,
                "rank": rank,
                "value": str(val),
                "n": int(count),
                "pct_of_total": round(int(count) / n_total * 100, 2),
                "pct_of_nonnull": round(int(count) / n_nn * 100, 2) if n_nn and not pd.isna(val) else None,
            })
    return pd.DataFrame(rows)


def retention_waterfall(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """Heuristic waterfall using common gate columns; user can override in config."""
    n_total = len(df)
    gates = []
    gates.append(("Analytic (input)", n_total))
    if "Finished" in df.columns:
        gates.append(("Finished == True", int(df["Finished"].astype(bool).sum())))
    if "Attention_Check" in df.columns:
        gates.append(("Passed attention check", int((df["Attention_Check"] == 1).sum())))
    if "Q_RecaptchaScore" in df.columns:
        gates.append(("reCAPTCHA >= 0.5", int((pd.to_numeric(df["Q_RecaptchaScore"], errors="coerce") >= 0.5).sum())))
    if "consent" in df.columns or "Consent" in df.columns:
        col = "consent" if "consent" in df.columns else "Consent"
        gates.append((f"{col} == Yes",
                      int(df[col].astype(str).str.lower().isin({"yes", "true", "1"}).sum())))
    if not gates:
        gates = [("Analytic (input)", n_total)]
    return pd.DataFrame([{"gate": g, "n": n} for g, n in gates])


def missingness_patterns(df: pd.DataFrame) -> pd.DataFrame:
    """Per-column nulls + flag of high co-missingness pairs."""
    null_pct = df.isna().mean() * 100
    rows = [{"col": c, "null_pct": round(p, 2), "flag":
            "unusable" if p > 50 else "sensitivity" if p > 20 else "ok"}
            for c, p in null_pct.items()]
    return pd.DataFrame(rows)


def cell_size_diagnostics(df: pd.DataFrame, key_demos: list, min_cell: int = 10) -> pd.DataFrame:
    """For pairs of key demographics, surface any thin cells."""
    rows = []
    if len(key_demos) < 2:
        return pd.DataFrame(columns=["dim_a", "dim_b", "value_a", "value_b", "n", "flagged"])
    for i in range(len(key_demos)):
        for j in range(i + 1, len(key_demos)):
            a, b = key_demos[i], key_demos[j]
            if a not in df.columns or b not in df.columns:
                continue
            ct = pd.crosstab(df[a].astype(str), df[b].astype(str))
            for va in ct.index:
                for vb in ct.columns:
                    n = int(ct.loc[va, vb])
                    rows.append({
                        "dim_a": a, "value_a": str(va),
                        "dim_b": b, "value_b": str(vb),
                        "n": n,
                        "flagged": "yes" if n < min_cell else "",
                    })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, help="Path to run config.json")
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)

    input_path = cfg["input_dataset"]
    out_dir = cfg["output_dir"]
    os.makedirs(out_dir, exist_ok=True)

    df = pd.read_csv(input_path, low_memory=False)
    n_total = len(df)

    # Auto-classify if not provided
    classification = {}
    for c in df.columns:
        classification[c] = {
            "type":  detect_type(df[c], c),
            "role":  detect_role(c),
            "n_nonnull": int(df[c].notna().sum()),
            "n_unique":  int(df[c].nunique(dropna=True)),
        }

    # Allow config overrides
    user_cols = cfg.get("columns", {})
    for role, col_list in user_cols.items():
        for c in (col_list or []):
            if c in classification:
                classification[c]["role"] = role

    with open(os.path.join(out_dir, "column_classification.json"), "w") as f:
        json.dump(classification, f, indent=2)

    # Numeric profile
    num_cols = [c for c, v in classification.items()
                if v["type"] in ("numeric_continuous", "numeric_ordinal")
                and v["role"] not in ("pii_candidate", "outcome")]
    num_df = numeric_profile(df, num_cols)
    num_df.to_csv(os.path.join(out_dir, "05_Numeric-Profile.csv"), index=False)

    # Categorical profile
    cat_cols = [c for c, v in classification.items()
                if v["type"] in ("categorical_nominal", "categorical_highcard", "boolean")
                and v["role"] not in ("pii_candidate", "outcome")]
    cat_df = categorical_profile(df, cat_cols)
    cat_df.to_csv(os.path.join(out_dir, "06_Categorical-Profile.csv"), index=False)

    # Quality metrics stacked (waterfall + missingness + cell sizes)
    quality_frames = []
    wf = retention_waterfall(df, cfg)
    wf.insert(0, "metric", "retention_waterfall")
    quality_frames.append(wf.rename(columns={"gate": "label"}))
    miss = missingness_patterns(df)
    miss.insert(0, "metric", "missingness")
    miss = miss.rename(columns={"col": "label", "null_pct": "n"})
    quality_frames.append(miss[["metric", "label", "n", "flag"]])
    csd = cell_size_diagnostics(df, cfg.get("key_demographics", []),
                                 cfg.get("min_cell_size", 10))
    if len(csd):
        csd.insert(0, "metric", "cell_size_diagnostic")
        csd["label"] = csd["dim_a"] + "=" + csd["value_a"] + " × " + csd["dim_b"] + "=" + csd["value_b"]
        quality_frames.append(csd[["metric", "label", "n", "flagged"]].rename(columns={"flagged": "flag"}))
    qual = pd.concat(quality_frames, ignore_index=True)
    qual.to_csv(os.path.join(out_dir, "07_Quality-Metrics.csv"), index=False)

    # Summary stdout
    pii_cols = [c for c, v in classification.items() if v["role"] == "pii_candidate"]
    print(json.dumps({
        "status": "ok",
        "rows": n_total,
        "cols": len(df.columns),
        "pii_detected": pii_cols,
        "files_written": [
            "05_Numeric-Profile.csv",
            "06_Categorical-Profile.csv",
            "07_Quality-Metrics.csv",
            "column_classification.json",
        ],
        "timestamp": datetime.utcnow().isoformat(),
    }, indent=2))

    if pii_cols:
        print(f"\nWARNING: PII-candidate columns detected: {pii_cols}", file=sys.stderr)
        print("Halt and request authorization before proceeding.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
