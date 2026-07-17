#!/usr/bin/env python3
"""Adaptive sample-description chart builder.

Reads config + column_classification + dataset, decides what charts to render
based on detected variable families, and emits brand-styled PNGs into <out>/charts/.

Designed for matplotlib + Figtree font (loaded from brand JSON's font_file_dir).

Usage:
    python build_charts.py --config /abs/path/to/config.json
"""

import argparse
import json
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter

# ---------------------------------------------------------------------------
# Brand loading
# ---------------------------------------------------------------------------

def load_brand(brand_path: str) -> dict:
    with open(brand_path) as f:
        return json.load(f)


def color_of(brand: dict, role: str) -> str:
    palette_key = brand["semantic"].get(role, role)
    return brand["palette"].get(palette_key, palette_key)


def apply_brand_theme(brand: dict):
    font_dir = brand.get("fonts", {}).get("font_file_dir")
    if font_dir and os.path.isdir(font_dir):
        for fname in os.listdir(font_dir):
            if fname.endswith(".ttf"):
                font_manager.fontManager.addfont(os.path.join(font_dir, fname))
    primary_font = brand["fonts"]["primary"]
    mpl.rcParams.update({
        "font.family": primary_font,
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlecolor": color_of(brand, "title"),
        "axes.titlepad": 14,
        "axes.labelcolor": color_of(brand, "body_text"),
        "axes.edgecolor": color_of(brand, "footer_text"),
        "axes.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": color_of(brand, "grid_lines"),
        "grid.linewidth": 0.7,
        "grid.alpha": 0.8,
        "xtick.color": color_of(brand, "body_text"),
        "ytick.color": color_of(brand, "body_text"),
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",
        "text.parse_math": False,  # never let $ be math-mode
    })


# ---------------------------------------------------------------------------
# Chart helpers
# ---------------------------------------------------------------------------

def pct_fmt(v, _):
    return f"{int(v)}%"


def attribution(fig, brand, n, study_name="study", date_range="", note=""):
    base = f"Source: {study_name}"
    if date_range:
        base += f", {date_range}"
    base += f" · n = {n}"
    if note:
        base += f" · {note}"
    fig.text(0.99, 0.005, base, ha="right", va="bottom",
             fontsize=8, color=color_of(brand, "footer_text"), style="italic")


def small_n_caveat(ax, brand, n_total, small_n_threshold):
    if n_total < small_n_threshold:
        ax.text(0.5, -0.18, f"Small-sample caveat (n = {n_total}): estimates may be noisy.",
                transform=ax.transAxes, ha="center",
                fontsize=8, color=color_of(brand, "warning"), style="italic")


# ---------------------------------------------------------------------------
# Chart factories
# ---------------------------------------------------------------------------

def chart_continuous(df, col, out_path, brand, title=None, n_total=None,
                     small_n_threshold=100, study_name="study"):
    s = pd.to_numeric(df[col], errors="coerce").dropna()
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.hist(s, bins=min(30, max(10, int(np.sqrt(len(s))))),
            color=color_of(brand, "chart_bar_primary"),
            edgecolor="white", linewidth=1.2)
    ax.axvline(s.mean(), color=color_of(brand, "highlight"), linestyle="--",
               linewidth=2, label=f"Mean = {s.mean():.1f}")
    ax.axvline(s.median(), color=color_of(brand, "warning"), linestyle=":",
               linewidth=2, label=f"Median = {s.median():.1f}")
    ax.set_xlabel(col.replace("_", " ").title())
    ax.set_ylabel("Respondents")
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title(title or f"{col.replace('_', ' ').title()} distribution", pad=12)
    small_n_caveat(ax, brand, n_total or len(df), small_n_threshold)
    attribution(fig, brand, n_total or len(df), study_name)
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def chart_categorical_bar(df, col, out_path, brand, title=None, n_total=None,
                          top_k=12, highlight_value=None, small_n_threshold=100,
                          study_name="study"):
    n_total = n_total or len(df)
    s = df[col]
    vc = s.value_counts().head(top_k)
    other_n = s.value_counts().iloc[top_k:].sum()
    labels = list(vc.index.astype(str))
    vals = list(vc.values)
    if other_n > 0 and s.nunique() > top_k:
        labels.append(f"Other {s.nunique() - top_k} categories")
        vals.append(other_n)
    pcts = [v / n_total * 100 for v in vals]
    colors = []
    for lab in labels:
        if highlight_value and lab == str(highlight_value):
            colors.append(color_of(brand, "highlight"))
        elif lab.startswith("Other"):
            colors.append(color_of(brand, "grid_lines"))
        else:
            colors.append(color_of(brand, "chart_bar_primary"))
    fig, ax = plt.subplots(figsize=(11, max(5, len(labels) * 0.42)))
    y = np.arange(len(labels))
    ax.barh(y, pcts, color=colors, edgecolor="white", linewidth=1)
    ax.invert_yaxis()
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.xaxis.set_major_formatter(FuncFormatter(pct_fmt))
    ax.set_xlabel("Share of sample")
    ax.set_xlim(0, max(pcts) + 8)
    for i, (p, v) in enumerate(zip(pcts, vals)):
        ax.text(p + 0.4, i, f"{p:.1f}%  (n={v})", va="center",
                fontsize=9, color=color_of(brand, "body_text"))
    ax.set_title(title or f"{col.replace('_', ' ').title()} distribution", pad=12)
    small_n_caveat(ax, brand, n_total, small_n_threshold)
    attribution(fig, brand, n_total, study_name)
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def chart_donut_or_bar(df, col, out_path, brand, title=None, n_total=None,
                       study_name="study"):
    n_total = n_total or len(df)
    vc = df[col].value_counts()
    fig, ax = plt.subplots(figsize=(7, 6))
    if len(vc) <= 4:
        colors = [color_of(brand, "chart_bar_primary"),
                  color_of(brand, "chart_bar_accent"),
                  color_of(brand, "warning"),
                  color_of(brand, "grid_lines")][:len(vc)]
        ax.pie(vc.values, labels=None, colors=colors,
               wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2),
               startangle=90, counterclock=False,
               autopct=lambda p: f"{p:.0f}%" if p > 3 else "",
               pctdistance=0.78,
               textprops=dict(fontsize=11, color="white", fontweight="bold"))
        ax.text(0, 0, f"n = {vc.sum()}", ha="center", va="center",
                fontsize=12, color=color_of(brand, "title"), fontweight="bold")
        legend_labels = [f"{lab} — {v} ({v/vc.sum()*100:.1f}%)"
                         for lab, v in vc.items()]
        ax.legend([f for f in legend_labels], loc="lower center",
                  bbox_to_anchor=(0.5, -0.05), ncol=1, frameon=False, fontsize=10)
    else:
        return chart_categorical_bar(df, col, out_path, brand, title=title,
                                     n_total=n_total, study_name=study_name)
    ax.set_title(title or col.replace("_", " ").title())
    attribution(fig, brand, n_total, study_name)
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Family grouping
# ---------------------------------------------------------------------------

DEMO_FAMILIES = {
    "Geography":       ["state", "country", "zip", "region"],
    "Age":             ["age"],
    "Sex":             ["sex", "gender"],
    "Income":          ["income"],
    "Education":       ["education", "edu_level"],
    "Employment":      ["employment", "work_status"],
    "Ethnicity":       ["ethnicity", "race"],
    "Origin":          ["nationality", "language"],
    "Behavioral":      ["caregiver", "prior_", "goals", "interest", "experience"],
}


def group_by_family(cols):
    """Word-boundary match — "Language" should not match "age" substring."""
    import re
    families = {fam: [] for fam in DEMO_FAMILIES}
    families["Other"] = []
    for c in cols:
        cl = c.lower()
        placed = False
        for fam, patterns in DEMO_FAMILIES.items():
            for p in patterns:
                # Match as a word or as a prefix (e.g., "prior_") — never as a mid-word substring
                if re.search(rf"(^|_){re.escape(p)}(_|$)", cl) or (p.endswith("_") and cl.startswith(p)):
                    families[fam].append(c)
                    placed = True
                    break
            if placed:
                break
        if not placed:
            families["Other"].append(c)
    return {k: v for k, v in families.items() if v}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)
    brand = load_brand(cfg["brand_path"])
    apply_brand_theme(brand)

    df = pd.read_csv(cfg["input_dataset"], low_memory=False)
    out_dir = os.path.join(cfg["output_dir"], "charts")
    os.makedirs(out_dir, exist_ok=True)

    n_total = len(df)
    small_n = cfg.get("small_n_threshold", 100)
    large_n = cfg.get("large_n_threshold", 5000)
    study_name = cfg.get("study_name", "study")

    # Pull classification
    cls_path = os.path.join(cfg["output_dir"], "column_classification.json")
    with open(cls_path) as f:
        classification = json.load(f)

    # Demographic + behavioral columns only
    demo_cols = [c for c, v in classification.items()
                 if v["role"] in ("demographic", "behavioral")
                 and v["type"] not in ("text_free", "structural", "id")]

    families = group_by_family(demo_cols)
    chart_index = 1
    chart_files = []

    for family, cols in families.items():
        for col in cols:
            kind = classification[col]["type"]
            out_path = os.path.join(out_dir, f"{chart_index:02d}_Chart_{family}_{col}.png")
            try:
                if kind == "numeric_continuous":
                    chart_continuous(df, col, out_path, brand,
                                     title=f"{family} — {col.replace('_', ' ').title()} distribution",
                                     n_total=n_total, small_n_threshold=small_n,
                                     study_name=study_name)
                elif kind == "boolean" or (kind == "categorical_nominal" and df[col].nunique() <= 4):
                    chart_donut_or_bar(df, col, out_path, brand,
                                       title=f"{family} — {col.replace('_', ' ').title()}",
                                       n_total=n_total, study_name=study_name)
                else:
                    highlight = None
                    if family == "Geography" and "California" in df[col].astype(str).unique():
                        highlight = "California"
                    chart_categorical_bar(df, col, out_path, brand,
                                          title=f"{family} — {col.replace('_', ' ').title()}",
                                          n_total=n_total, highlight_value=highlight,
                                          small_n_threshold=small_n,
                                          study_name=study_name)
                chart_files.append(out_path)
                chart_index += 1
            except Exception as e:
                print(f"WARN: failed to render {col}: {e}", file=sys.stderr)

    print(json.dumps({
        "status": "ok",
        "charts_rendered": len(chart_files),
        "out_dir": out_dir,
        "files": [os.path.basename(p) for p in chart_files],
        "timestamp": datetime.utcnow().isoformat(),
    }, indent=2))


if __name__ == "__main__":
    main()
