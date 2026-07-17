# Prompt — Audit open-ended numeric (cost / hours / salary) parsing

**Use in:** a chat with the raw data file. The audit is a sampling + comparison task.

**Inputs:**
- Raw data file with the free-text column
- Clean data file with the parsed numeric column
- The parsing rule the AI used (if available)

**Output:** a cost-parsing-audit workbook with stratified samples, a column for the human reviewer to mark correct / incorrect, and a pass-rate computation.

---

## Prompt

```
You are auditing an open-ended numeric parsing step.

INPUTS:
- raw column: <name> in <raw filename>
- cleaned column: <name> in clean.csv
- parsing rule (if available): <verbatim or "not available">

TASK:

1. Pull a stratified sample of 30 rows from the cleaned data:
   - 10 from the bottom decile of cleaned values (low-end, possible "free" / "0" / placeholder issues)
   - 10 from the mid-range (the typical bulk; verbal-expression conversions)
   - 10 from the top decile (high-end / outliers; possible currency / units / range issues)

2. Pull a separate sample of all rows where the cleaned value is NaN. If there are more than 20 such rows, sample 20 stratified by raw text length.

3. For each sampled row, output:
   | row_idx | raw_text | cleaned_value | expected_value | (human fills) match | (human fills) miscoding_type | (human fills) reviewer_note |

4. For each `expected_value`, propose what a human reviewer would likely say the value should be — but mark this clearly as "tentative" and leave the `match` column blank for the human to fill.

5. Tag suspicious patterns to draw the reviewer's attention:
   - ranges ("$200-500") → likely flag, depending on parsing rule
   - verbal numbers ("five hundred", "1k", "two grand") → check
   - "I don't know" / "depends" / "varies" → should be NaN
   - "free" / "$0" → should be 0, not NaN
   - "$50,000" or "$1m" outliers → check if respondent meant the units
   - currency symbols or commas → should be stripped, not coded as missing

CONSTRAINTS:
- Do not invent expected values. Mark "tentative" and let the human decide.
- Do not change the raw or cleaned data. This is a sampling pass only.
- Track which rows are sampled so the same rows aren't re-sampled in subsequent passes.

After the human fills `match`, compute:
- pass_rate per stratum
- common miscoding types
- recommendation (Pass / Fail / Re-parse) per the thresholds in the template

Return the sampled audit table.
```

## Notes for the operator

- A failed parsing audit on a field used in any H-stakes claim is a do-not-publish gate.
- The remediation is usually to re-parse with a corrected rule, not to manually edit the clean file row-by-row.
