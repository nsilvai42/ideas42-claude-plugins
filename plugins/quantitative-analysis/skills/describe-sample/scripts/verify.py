#!/usr/bin/env python3
"""Spot-check pass for the sample-description bundle.

Re-computes a list of headline numbers from the raw dataset and compares against
expected values supplied by the SKILL.md orchestrator (which extracted them
from the rendered deliverables). Writes a PASS/FAIL report to 10_Verification.md.

Usage:
    python verify.py --config /abs/path/to/config.json --claims /abs/path/to/claims.json

claims.json schema (an array of claim dicts):
[
  {"name": "California n", "expr": "(df['05_4A'] == 'California').sum()", "expected": 54},
  {"name": "Sample n",     "expr": "len(df)",                              "expected": 314},
  ...
]
"""

import argparse
import json
import os
import sys
import pandas as pd  # noqa: F401  (used in eval'd exprs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--claims", required=True)
    args = ap.parse_args()

    cfg = json.load(open(args.config))
    claims = json.load(open(args.claims))

    df = pd.read_csv(cfg["input_dataset"], low_memory=False)  # noqa: F841

    lines = ["# Verification report", "",
             f"- Dataset: `{cfg['input_dataset']}`",
             f"- Rows: {len(df)}",
             f"- Claims checked: {len(claims)}",
             ""]
    n_pass = 0
    n_fail = 0
    for c in claims:
        name = c["name"]
        expr = c["expr"]
        expected = c["expected"]
        try:
            obs = eval(expr, {"df": df, "pd": pd})
        except Exception as e:
            lines.append(f"- ❌ **{name}**: error evaluating `{expr}` — {e}")
            n_fail += 1
            continue
        passed = (obs == expected) or (
            isinstance(obs, float) and isinstance(expected, float)
            and abs(obs - expected) < 0.01)
        status = "✅" if passed else "❌"
        lines.append(f"- {status} **{name}**: observed `{obs}` | expected `{expected}`")
        if passed:
            n_pass += 1
        else:
            n_fail += 1
    lines.append("")
    lines.append(f"**Summary: {n_pass} passed / {n_fail} failed.**")

    out_path = os.path.join(cfg["output_dir"], "10_Verification.md")
    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(json.dumps({"status": "ok", "pass": n_pass, "fail": n_fail, "file": out_path}, indent=2))
    if n_fail > 0:
        sys.exit(3)


if __name__ == "__main__":
    main()
