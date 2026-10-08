# Prompt — Extract material claims

**Use in:** a fresh chat with a different model (or at minimum a different project) from the one that generated the original analysis. Never reuse the analyst's session.

**Inputs to attach:**
- The Word report (or whichever long-form output exists)
- The dashboard HTML or screenshots
- The exec summary if it lives in a separate file
- Any chart captions

**Output expected:** an initial `claim_ledger.xlsx` (or CSV) populated for the master tab columns through `original_value`. Verifier columns left blank.

---

## Prompt

```
You are extracting material claims from a data-analysis bundle for an independent verification pass. You are NOT verifying the claims. You are NOT the analyst who produced the analysis. Treat the outputs as targets to be checked, not as sources of truth.

INPUTS:
- <list each attached output by filename>

TASK:
For every material claim in the attached outputs, produce one row of a claim ledger. A "material claim" is anything load-bearing — i.e., anything that:
- appears in the executive summary or top-line headline
- supports a recommendation
- carries a "Key takeaway" or similar framing
- is referenced in a chart caption or KPI card
- states a percentage, count, median, mean, rank, or other statistic on a topic of interest
- claims a comparison or magnitude ("PAYG leads", "more than 3×")
- characterizes a population, subgroup, or condition

Skip:
- pure styling text, decorative numbers, page-fillers, transition prose
- citation-style references to instrument design ("Phase 1 — Mental Models")

OUTPUT SCHEMA (one row per claim):

| Column | What goes in it |
|---|---|
| claim_id | CL-001, CL-002, ... |
| output | report / dashboard / analysis.json / chart-<name> |
| location | section heading + paragraph, or chart title + caption position |
| claim_text | the claim verbatim (or lightly paraphrased; preserve numbers exactly) |
| claim_type | descriptive / derived / comparative / inferential / methodological / interpretive |
| stakes | H if the claim drives a recommendation or appears in the exec summary; M if it supports an argument; L if it's background |
| source_columns | best guess at which clean.csv columns the claim derives from (mark UNKNOWN if you cannot tell) |
| computation_rule | what pandas/SQL expression would re-derive the value (e.g., "df['col'].value_counts(normalize=True)['Yes'] * 100") |
| original_value | the value as stated in the output |
| human_review_needed | Yes if any of the following: stakes = H AND the computation rule has ambiguity (denominator, parsing, subgroup definition); claim is interpretive; claim involves open-text / theme coding; claim cites a multi-select where option labels contain commas |

CONSTRAINTS:
- Atomic claims. One numerical assertion per row. Split compound claims.
- Do not paraphrase numbers. "82% of respondents" must remain "82%", not "most respondents".
- Do not invent values. If a percentage is implied but not stated, leave original_value blank and note in claim_text that the value is implied.
- Cover every output. A claim that appears in three outputs gets three rows (or one row with multiple location pointers, but flag the duplication for the cross-output consistency check).

Return the ledger as a markdown table or CSV. Stop when the inputs are exhausted — do not extrapolate, do not synthesize.
```

## Notes for the operator

- This pass is content-only; it does not check whether anything is correct.
- Expect 100–250 claims for a typical findings report + dashboard bundle.
- After extraction, the human operator triages the `stakes` and `human_review_needed` columns, then hands off to the verification prompt.
