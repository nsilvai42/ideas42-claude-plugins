# Prompt — Build a data prep inventory

**Use in:** any chat (the data prep is content-only, like extraction).

**Inputs:**
- The raw data file (if you have it)
- The cleaned data file (`clean.csv`)
- Any cleaning script / notebook / prompt used to produce the clean file

**Output expected:** a `data_prep_inventory.xlsx` populated with every field that involved transformation, with `audit_needed` flagged.

---

## Prompt

```
You are inventorying the data-prep step of a data-analysis bundle for an independent verification pass.

INPUTS:
- raw data file: <filename>
- cleaned data file: clean.csv
- cleaning rule / script / prompt: <filename or "not available">

TASK:
For every column in the cleaned file, identify how it was derived from the raw file.

For each column, output one row with:

| Column | What goes in it |
|---|---|
| field_name | Column name in clean.csv |
| raw_source | Column name(s) in raw file (mark UNKNOWN if you cannot map) |
| transformation | One of: identity / type-coercion / value-recoding / open-ended-parse / multi-select-explode / verbal-to-numeric / theme-tagging / aggregation / other |
| transformation_rule | Verbatim rule from the cleaning script or prompt; "AI inference" if no explicit rule |
| ai_judgment_required | Yes if the transformation required non-trivial AI judgment (open-ended → number, verbal → code, theme tagging, parsing of comma-containing labels) |
| audit_needed | Yes if ai_judgment_required = Yes, OR if this field is used by any H-stakes claim in the ledger |
| notes | Any caveat the operator should know |

Then for each `audit_needed = Yes` field, propose:
- a stratified sample of 30 raw→clean pairs (10 from low-end of cleaned distribution, 10 from mid-range, 10 from high-end OR NaN, depending on field type)
- a 1-paragraph description of what would constitute a "Pass" for that field's audit

CONSTRAINTS:
- Do not propose audits for fields that are identity or type-coercion only.
- Mark UNKNOWN where mapping cannot be determined; do not invent transformations.
- If `clean.csv` has columns not present in the raw file with no rule on how they were derived, flag those columns explicitly.

Return the inventory as a markdown table or CSV.
```

## Notes for the operator

- Fields most likely to need audits: open-ended numeric, multi-select with comma-containing labels, verbal→categorical, free-text→theme.
- A failed audit on a field used by an H-stakes claim is a do-not-publish gate.
