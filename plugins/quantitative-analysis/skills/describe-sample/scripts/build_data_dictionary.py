#!/usr/bin/env python3
"""Generate a column glossary CSV from the dataset + classification.

Usage:
    python build_data_dictionary.py --config /abs/path/to/config.json
"""

import argparse
import json
import os
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)

    df = pd.read_csv(cfg["input_dataset"], low_memory=False)
    out_dir = cfg["output_dir"]
    with open(os.path.join(out_dir, "column_classification.json")) as f:
        classification = json.load(f)

    # Optional column dictionary path (CSV with: column, question_text or label)
    label_map = {}
    label_csv = cfg.get("column_dictionary_path")
    if label_csv and os.path.exists(label_csv):
        ld = pd.read_csv(label_csv)
        first_col = ld.columns[0]
        text_col = next((c for c in ld.columns[1:]
                         if "text" in c.lower() or "label" in c.lower() or "question" in c.lower()),
                        ld.columns[1] if len(ld.columns) > 1 else None)
        if text_col:
            label_map = dict(zip(ld[first_col], ld[text_col]))

    rows = []
    for c in df.columns:
        s = df[c]
        cls = classification.get(c, {})
        example_vals = s.dropna().astype(str).unique()[:5].tolist()
        rows.append({
            "column": c,
            "label": label_map.get(c, ""),
            "type_inferred": cls.get("type", ""),
            "role_inferred": cls.get("role", ""),
            "n_nonnull": int(s.notna().sum()),
            "n_unique":  int(s.nunique(dropna=True)),
            "example_values": " | ".join(example_vals),
            "derived_from": "",
            "transformation_ledger_ids": "",
            "notes": "",
        })

    out = pd.DataFrame(rows)
    out.to_csv(os.path.join(out_dir, "03_Data-Dictionary.csv"), index=False)
    print(json.dumps({"status": "ok", "rows": len(out)}, indent=2))


if __name__ == "__main__":
    main()
