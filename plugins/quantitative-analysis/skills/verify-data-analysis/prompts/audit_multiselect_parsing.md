# Prompt — Audit multi-select parsing (with comma-in-label edge cases)

**Use in:** a chat with the raw data + clean data + survey instrument.

**Inputs:**
- Raw multi-select column (typically a comma-joined string of option labels)
- Clean version (either still a comma-joined string, or exploded into indicator columns)
- The list of valid option labels from the survey instrument

**Output:** a parsing-audit workbook with per-option counts under naive vs. robust parsing, plus the corrected counts.

---

## Prompt

```
You are auditing a multi-select parsing step. The common failure mode is option labels with embedded commas — naive split-by-comma over-counts and creates spurious labels.

INPUTS:
- raw multi-select column: <name>
- known valid option labels (verbatim from survey instrument):
  - <label 1>
  - <label 2>
  - ...

TASK:

1. Identify which option labels contain commas. These are the at-risk labels.

2. For each at-risk label, compute:
   - count_naive: rows where the raw value contains any of the comma-separated tokens of this label (this is what a naive parser does, and it will over-count)
   - count_robust: rows where the raw value contains the full label as a substring (using known-option string matching)
   - spurious_labels: the comma-tokens of this label that a naive parser would create as separate labels (e.g., "Financial aid (Pell Grant", "state grant", "etc.)")

3. For each non-at-risk label, compute count_robust the same way and confirm count_naive == count_robust.

4. Output a comparison table:
   | option_label | has_comma | count_naive | count_robust | spurious_labels_under_naive | parser_used_in_clean | parser_used_in_analysis.json | parser_used_in_dashboard_data | recommended_value |

5. Cross-check: for each option, what value does the downstream analysis (analysis.json, dashboard embedded data, report text) report? Flag any output that uses the naive count instead of the robust count.

6. Document the correction: which counts need to be replaced, and where.

CONSTRAINTS:
- Use string matching, not regex with comma as separator. Robust = `option in raw_value`.
- Do not assume the analyst used a robust parser. Always compute both.
- If the raw column has been pre-exploded into indicator columns, audit the indicator columns against the option labels and flag any indicators that don't map cleanly to a known label.

Return the comparison table.
```

## Notes for the operator

- The Calbright worked example had exactly this bug: "Financial aid (Pell Grant, state grant, etc.)" was split into three spurious labels by the naive parser, under-counting financial aid from 178 → 51 (52%).
- Any multi-select with parenthesized parenthetical examples is at risk.
- The fix is at the parser level, not the value level — every downstream claim that references the field must be re-derived.
