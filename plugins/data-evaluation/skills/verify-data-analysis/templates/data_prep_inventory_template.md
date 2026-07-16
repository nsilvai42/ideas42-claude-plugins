# Data Prep Inventory Template

Lives alongside the claim ledger. Documents every field where an AI step transformed the raw data, and audits whether the transformation is faithful.

## Tab 1 — Fields touched

| Column | Description |
|---|---|
| field_name | Column name in the cleaned file |
| raw_source | Column name(s) in the raw file |
| transformation | What the AI did (e.g., "open-ended dollar string → numeric"; "multi-select option text → exploded indicator columns"; "verbal estimate → numeric") |
| transformation_rule | The rule or prompt used (verbatim if possible) |
| ai_judgment_required | Yes / No — did the transformation require non-trivial AI judgment? |
| audit_needed | Yes if ai_judgment_required = Yes, OR if field is used in any H-stakes claim |
| audit_method | Stratified sample of raw→clean pairs / full pass / spot check |
| pass_rate | % of audited rows where the transformation is correct |
| pass_threshold | 95% default for H-stakes claims; 90% for M; not gated for L |
| audit_result | Pass / Fail / Not run |
| remediation | Required for Fail; how to fix |

## Tab 2 — Sample audit (per field)

For each `audit_needed = Yes` field, attach 30 stratified raw→clean pairs and a column for the human reviewer to mark correct / incorrect.

| field_name | row_idx | raw_value | cleaned_value | reviewer_assessment | reviewer_note |
|---|---|---|---|---|---|
| 01_1_1C | 12 | "around 1k" | 1000 | Correct | |
| 01_1_1C | 47 | "i don't know" | NaN | Correct | Should remain blank |
| 01_1_1C | 89 | "$5-10" | NaN | Incorrect — should be midpoint ~$7.50 or flagged | Convert to range or exclude |

## Common gotchas

- **Open-ended cost / numeric:** verbal answers ("five hundred", "1k", "around two grand") that need conversion; ranges ("$200–500") that need midpointing or exclusion; "free", "I don't know", "depends" → NaN.
- **Multi-select with comma-containing labels:** naive `.split(',')` breaks. Use known-option string matching.
- **Date fields:** time zones, half-completed timestamps, "Prefer not to say" coded as 1900-01-01 etc.
- **Likert recoding:** when text → numeric, verify 1↔5 vs 5↔1 polarity.
- **Free-text → theme:** these go to the theme-coding audit template, not here.

## Gate

If `audit_result = Fail` for any field used in an H-stakes claim, the H-stakes claim cannot be marked Replicated even if its number recomputes from the (possibly faulty) clean file.
