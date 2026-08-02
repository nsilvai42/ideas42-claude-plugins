# Prompt — Final narrow QA on corrected outputs

**Use in:** a chat with access to the corrected outputs and the ledger. This is a tight final check on non-replicated claims only.

**Inputs:**
- The verified ledger with Corrections Applied tab populated
- The corrected outputs (Report (Corrected).docx, Dashboard (Corrected).html, analysis_corrected.json)
- The original outputs (for comparison)

**Output:** the ledger's `post_correction_qa` column filled (✓ / ✗ / N/A) for every revised row, plus a short pass/fail memo.

---

## Prompt

```
You are running a final QA pass on corrected data-analysis outputs. Your job is to verify that every approved correction was applied consistently, and that no original incorrect values remain.

INPUTS:
- verified ledger with Corrections Applied tab
- corrected outputs: <list>
- original outputs (read-only, for comparison): <list>

TASK:

For every row in the Corrections Applied tab (i.e., every row that was revised):

1. Confirm the corrected output contains the new wording or value. Pull a short snippet of the corrected text around the change.

2. Confirm the original wording or value is GONE from the corrected output. Run a substring search for original_value and report any matches.

3. Confirm cross-output consistency: every output that should have been updated (per the outputs_changed column) has been updated. Spot-check the same statistic in each output.

4. Fill the ledger's `post_correction_qa` column:
   - ✓ if the correction is correctly applied and no orphan instances remain
   - ✗ with a note if the correction is missing, partial, or inconsistent
   - N/A if the claim was Replicated and not revised

5. Run two cross-cutting checks:

   a. Replicated rows should NOT have changed. Pick 5 random Replicated H-stakes rows and confirm their original_value still appears in the corrected outputs unchanged.

   b. The Methods section should contain a Verification note explaining the verification pass. Confirm.

6. Run a do-not-publish gate check:
   - Any H-stakes Error / Unable rows without human_approved = Yes? Should be 0.
   - Any unreviewed Method-disagreement rows on recommendation-driving claims? Should be 0.
   - Any cross-output inconsistencies on H-stakes claims? Should be 0.
   - Data-prep audit results documented? Should be Yes.
   - Every exec-summary interpretive claim traces to a body-text numerical claim? Should be Yes.
   - Corrections changelog matches Corrections Applied tab? Should be Yes.

Return:
- The ledger with post_correction_qa filled
- A short Pass / Revise-before-publication memo summarizing the gate check
- If any ✗ rows exist, a list of specific fixes needed

CONSTRAINTS:
- Do NOT re-verify Replicated rows numerically. This pass is about correction integrity, not re-verification.
- Do NOT propose new corrections. If you find a new issue not in the ledger, flag it for the next verification cycle but do not act on it here.
- Be tight. This should be minutes, not hours.
```

## Notes for the operator

- Failed final QA loops back to apply_corrections.md. Iterate until clean.
- A common failure: a value was corrected in the report but the same value still appears in a chart caption or KPI card. The Verification Note in the methods section is also a frequent omission.
