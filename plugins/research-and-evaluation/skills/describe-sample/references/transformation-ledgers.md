# Transformation ledgers

Whenever a transformation involves subjective judgment — collapsing categories, binning continuous variables, recoding "Other" responses, merging duplicate sources — produce a ledger row before applying. Subjective transformations always require user approval; mechanical ones (e.g., trimming whitespace, parsing standard ISO dates) do not.

## What counts as subjective vs. mechanical

| Mechanical (apply silently, log briefly) | Subjective (propose, show examples, require approval) |
|---|---|
| Stripping whitespace | Collapsing "Black or African American" + "African" into "Black" |
| Lowercasing for join keys | Mapping "self-employed (consultant)" → "Self-employed" |
| Parsing ISO dates | Choosing 5 vs 10 income brackets |
| Coercing dtypes (int → float for math) | Binning age into "young / mid / older" labels |
| Removing UTF-BOM characters | Choosing primary source between Qualtrics and Prolific copies |
| Renaming columns to snake_case | Recoding "Prefer not to say" as NaN vs. own category |
| Computing derived counts (e.g., `funding_n_selected`) | Defining what counts as "caregiver" when there are 3 yes-variants |

If unsure, treat as subjective.

## Ledger structure

A single CSV (`04_Transformation-Ledger.csv`) lives in the output folder. One row per transformation.

| Column | Description |
|---|---|
| `id` | Sequential integer |
| `timestamp` | ISO datetime when applied |
| `column_in` | Source column name(s) — pipe-separated if multiple |
| `column_out` | Resulting column name (suffixed `_recoded`, `_binned`, `_clean`, etc.) |
| `decision_type` | `collapse`, `bin`, `recode`, `parse`, `source_pick`, `impute`, `derive` |
| `decision` | One-line description of the rule |
| `rationale` | Why this rule (best practice, user-requested, etc.) |
| `examples_shown` | The 3 example rows used to ask for approval (JSON) |
| `affected_rows` | n affected by the transformation |
| `user_approved` | `yes` / `no` / `auto` |
| `notes` | Any caveats or edge-case handling |

## Approval flow (subjective transformations)

For every subjective transformation, before applying:

1. **Generate the rule.** Examples:
   - "Collapse 9 race categories into {White, Black, Asian, Mixed, Other, Prefer not to say}"
   - "Bin age into {18-24, 25-34, 35-44, 45-54, 55-64, 65+}"
   - "Treat sentinel value 999 in `years_experience` as NaN"

2. **Pull 3 random illustrative examples** from rows where the rule applies. Show the user `original_value → proposed_value`, three pairs.

3. **Surface via elicitation form** with options: Approve / Adjust / Skip transformation. If "Adjust", let the user type the desired rule.

4. **Log the decision** in the ledger with `user_approved` set accordingly.

5. **Apply** if approved.

## Example ledger entry (formatted as it would appear in the CSV)

```
id: 7
timestamp: 2026-05-23T15:34:21
column_in: employment_raw
column_out: employment_recoded
decision_type: collapse
decision: "Collapse 'Other' write-ins into existing canonical categories where possible; create 'Not in labor force' bucket for retired/disabled/homemaker/stay-at-home"
rationale: "26 'Other' responses inspected; 23 fit a new NILF bucket; baker → FT; 1 self-employed write-in folded back"
examples_shown: [{"in":"baker (full-time work)","out":"Working full-time"},{"in":"retired teacher","out":"Not in labor force"},{"in":"self employed contractor","out":"Self-employed"}]
affected_rows: 26
user_approved: yes
notes: "Reviewed full ledger of 26 'Other' rows; 0 ambiguous"
```

## When NOT to ledger

- Anything in the **mechanical** list above (still apply, but no need for a ledger row — just include in the end-of-process summary as "standard data hygiene applied: trim whitespace, parse dates, etc.")
- Filtering/dropping at the row level (those go in the retention waterfall, not the ledger)
- Statistical computations (mean, median, etc. are not "transformations")

## Re-running the skill

If the skill is re-run on the same dataset, look for an existing ledger in any prior dated subfolder. Offer to re-apply previously approved decisions to save the user time — but still show what's being applied and let them adjust.
