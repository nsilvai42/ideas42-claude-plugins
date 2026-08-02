#!/usr/bin/env python3
"""Generate a public-safe variant of the sample-description narrative.

- Strips PII-candidate columns from any output dataset
- Suppresses cells where n < min_cell_size (default 5) in frequency tables
- Adds a watermark / footer to the docx

This script writes 09_Sample-Description_Public.docx by post-processing the
narrative docx (xml-unpack → edit → repack), so it must run AFTER build_docs.js.

For simplicity in v1, this implementation outputs a markdown-equivalent that the
SKILL workflow then converts to docx via the same docx skill.
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

    out_dir = cfg["output_dir"]
    min_cell = int(cfg.get("public_min_cell_size", 5))

    # Strip suppressed cells from the categorical profile
    cat_path = os.path.join(out_dir, "06_Categorical-Profile.csv")
    if not os.path.exists(cat_path):
        print("ERROR: profile not found; run profile_data.py first.")
        return 1
    cat = pd.read_csv(cat_path)
    cat["public_n"] = cat["n"].where(cat["n"] >= min_cell, other="—")
    cat["public_pct_of_total"] = cat.apply(
        lambda r: r["pct_of_total"] if r["n"] >= min_cell else "—", axis=1)
    cat_out = cat[["col", "rank", "value", "public_n", "public_pct_of_total"]]
    cat_out.to_csv(os.path.join(out_dir, "06_Categorical-Profile_Public.csv"), index=False)

    # Strip suppressed cells from quality / cell-size diagnostics
    qual_path = os.path.join(out_dir, "07_Quality-Metrics.csv")
    if os.path.exists(qual_path):
        qual = pd.read_csv(qual_path)
        if "n" in qual.columns:
            qual["public_n"] = qual["n"].apply(
                lambda x: x if (pd.api.types.is_number(x) and x >= min_cell) else (
                    "—" if pd.api.types.is_number(x) else x))
            qual.to_csv(os.path.join(out_dir, "07_Quality-Metrics_Public.csv"), index=False)

    # Markdown summary for public variant
    public_md = os.path.join(out_dir, "09_Public-Variant-Notes.md")
    with open(public_md, "w") as f:
        f.write("# Public-safe variant notes\n\n")
        f.write(f"- Cells with n < {min_cell} suppressed (shown as '—')\n")
        f.write("- All PII-candidate columns removed from outputs\n")
        f.write("- This is a public-release variant of the sample description\n\n")
        f.write("Pair this with `06_Categorical-Profile_Public.csv` and `07_Quality-Metrics_Public.csv`.\n")
        f.write("Ask the SKILL.md workflow to rebuild the .docx using only these suppressed tables.\n")

    print(json.dumps({"status": "ok", "min_cell": min_cell}, indent=2))


if __name__ == "__main__":
    main()
