# Prompt — Verify high-stakes claims with deterministic Python

**Use in:** a chat with the ability to run Python against `clean.csv` (your verification environment). The prompt is for Claude or another LLM, but the actual verification step must execute deterministic code, not narrative reasoning.

**Inputs:**
- The claim ledger from `extract_claims.md`
- `clean.csv`
- `analysis.json` (if available — useful for cross-checking what the original analyst computed)

**Output:** the ledger with `verifier_value`, `difference`, `status`, and `verification_notes` filled for every priority row.

---

## Prompt

```
You are running deterministic verification on a claim ledger against source data. Your job is to recompute every priority claim from clean.csv and record what you got.

INPUTS:
- claim_ledger.xlsx (attached or inline)
- clean.csv (attached)
- analysis.json (attached if available)

PRIORITY ROWS:
- All rows where stakes = H
- All rows where human_review_needed = Yes
- (Skip stakes = L unless explicitly asked)

FOR EACH PRIORITY ROW:

1. Read the `computation_rule`. If it is missing or marked UNKNOWN, propose one based on `claim_text` and `source_columns`. If you cannot propose a defensible rule, set status = Unable.

2. Execute the rule in Python against clean.csv. Use pandas. Record the result as `verifier_value`.

3. Compare to `original_value`. Record the difference.

4. Assign a status:
   - Replicated: verifier_value matches original_value within rounding (≤0.1 percentage points for percentages; exact match for counts; ≤1% for medians/means).
   - Drift: same intent, small numerical difference (rounding, stale recompute).
   - Error: substantively different (e.g., > 1pp on a percentage, or > 5% on a magnitude). Flag the underlying cause: wrong denominator, parsing bug, stale subgroup, computation mismatch.
   - Unable: cannot reproduce — source columns not identifiable, computation rule ambiguous, or subgroup definition unclear.
   - Method disagreement: both your value and the original are defensible but rely on different denominator / boundary / population definition. Note the alternative.
   - Directional only: the claim is qualitative (theme count, regex match). Replicate the count if you can, but do not change the status from Directional only.

5. For non-Replicated rows, propose a `recommended_fix`:
   - For Error: state the corrected value.
   - For Drift: state the refreshed value.
   - For Method disagreement: propose denominator-clarified wording (do not just substitute a number).
   - For Unable: state what additional information would be needed to verify.
   - For Directional only: propose softened language ("respondents whose response matched the [theme] keywords").

6. Fill `verification_notes` with:
   - the rule you executed (verbatim, in a code block)
   - the verifier_value
   - any caveats about denominator, sample restriction, or subgroup definition

WATCH FOR THESE COMMON FAILURE MODES (taxonomy from the calbright worked example):
- Survey timing / duration mismatch: "May" obscuring a multi-week field window; "X-minute survey" reflecting target not observed.
- Screener vs. self-report mismatch: recruitment criteria phrased as if they fully filter the final sample.
- Denominator ambiguity: % of N, % of known-respondents, % of answered — flag the alternatives.
- Stale subgroup values: subgroup table values that don't recompute from current clean.csv.
- Multi-select parsing bug: option labels with embedded commas. Always parse multi-select with known-option string matching, not naive split.
- Confidence-factor inflation: numbers that don't replicate at any plausible denominator.
- Overbroad summary language: "every metric", "all subgroups" — check the qualifier against the data.

CONSTRAINTS:
- Run real Python. Do not narrate computations without executing them.
- Preserve the original_value column verbatim — do not edit the original ledger's input columns.
- Do not assign Replicated to claims you could not actually recompute. Use Unable.
- Do not propose fixes that introduce values not in clean.csv or analysis.json.

Return the updated ledger.
```

## Notes for the operator

- The expensive step is writing the recomputation rule, not the comparison. If `computation_rule` is filled in during extraction (even tentatively), Phase 2 runs much faster.
- Cross-output inconsistencies surface here: if two rows for the same underlying statistic produce different verifier values, log both in the Cross-Output Inconsistencies tab.
- Save the actual Python you ran. The script becomes auditable evidence.
