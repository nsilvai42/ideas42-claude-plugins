# Human Review Queue Template

A filtered, sorted view of the claim ledger containing every row that requires human judgment. Should be self-contained — the reviewer should not need to bounce back to the master ledger.

## Filtering rule

`status != "Replicated"` OR `(stakes = "H" AND human_review_needed = Yes)`.

## Sort rule

Sort by `stakes` (H first, then M, then L), then by `status` (Error → Method disagreement → Unable → Drift → Directional only → Replicated-but-flagged).

## Columns (subset of the master ledger)

| Column | Why it's here |
|---|---|
| claim_id | Reference back to master |
| stakes | Drives reviewer priority |
| status | Tells the reviewer what kind of decision is needed |
| location | Where in the outputs the claim sits |
| claim_text | The claim verbatim |
| original_value | What the output currently says |
| verifier_value | What the verifier computed |
| difference | The delta |
| verification_notes | Why the status applies |
| recommended_fix | Proposed revision wording or value |
| **human_approved** | **Reviewer fills: Yes / No / TBD** |
| **human_notes** | **Reviewer fills: any wording or denominator choices** |
| **final_action** | **Reviewer fills: Approve / Revise output / Add caveat / Exclude claim / No action** |

## Review instructions sheet (Tab 2)

A one-pager that travels with the queue. Should include:

1. **Purpose**: "Use this workbook as the single human decision surface."
2. **Steps**:
   - Step 1: Start with rows where status is Error, Drift, or Method disagreement.
   - Step 2: Read `recommended_fix`. If acceptable, set `human_approved = Yes`.
   - Step 3: Use `human_notes` for any wording or denominator choices.
   - Step 4: Once all non-Replicated rows are decided, send back to whoever is applying corrections.
3. **Status options**: TBD (needs decision) / Yes (approved) / No (reject recommendation) / Not needed (replicated).
4. **Final action options**: No action / Approve / Revise output / Add caveat / Exclude claim.
5. **Recommended QA gate**: Do not publish if any High-stakes row has status Error/Unable/Method-disagreement and human_approved is not Yes.

## Suggested batch decisions

Most engagements will have most rows fitting one of these batches. Approve at the batch level if appropriate, override individually where needed.

| Batch | Default disposition |
|---|---|
| Replicated fixed-choice / numeric rows | Approve as-is |
| Replicated open-text / theme rows | Approve as directional |
| Drift rows | Approve refresh |
| Error rows | Approve recommended fix |
| Method disagreement rows | Approve recommended denominator clarification |
| Unable rows | Decide row-by-row (refresh / flag / exclude) |
