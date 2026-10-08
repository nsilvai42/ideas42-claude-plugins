# Prompt — Build the human review queue from a verified ledger

**Use in:** any chat. This is a sorting + formatting task, not verification.

**Inputs:** the ledger with `status` and `recommended_fix` filled.

**Output:** a `human_review_queue.xlsx` workbook with a filtered, sorted view of the ledger + a one-page Review Instructions sheet.

---

## Prompt

```
You are building a Human Review Queue from a verified claim ledger.

INPUTS:
- verified claim_ledger.xlsx with status filled

TASK:

1. Filter the master Claims tab to rows where `status != "Replicated"` OR `(stakes = "H" AND human_review_needed = Yes)`. This is the queue.

2. Sort the queue by stakes (H first, then M, L), then by status in this order: Error, Method disagreement, Unable, Drift, Directional only.

3. Output the queue as Tab 1 of a new workbook with these columns:
   claim_id, stakes, status, location, claim_text, original_value, verifier_value, difference, verification_notes, recommended_fix, human_approved, human_notes, final_action

4. Output a Review Instructions sheet as Tab 2 with:
   - Purpose statement: this workbook is the single human decision surface
   - Step-by-step (start with Error/Method-disagreement rows; read recommended_fix; set human_approved = Yes/No/TBD; use human_notes for any wording deviations; set final_action)
   - Status code legend
   - Final-action code legend
   - QA gate: do not publish if any H-stakes row has status Error / Unable / Method-disagreement and human_approved is not Yes

5. Output a Suggested Batch Decisions sheet as Tab 3 with a table the reviewer can use to approve common patterns in bulk:
   - All replicated rows → approve as-is
   - All Drift rows → approve refresh
   - All Error rows → approve recommended fix
   - All Method disagreement rows → approve denominator clarification
   - All Directional only rows → approve as directional
   - Unable rows: decide row-by-row

CONSTRAINTS:
- Do not edit any verification field. Add human columns only.
- Do not pre-fill human_approved. Leave TBD.
- Include EVERY non-replicated row, even if the recommended_fix looks obvious. The reviewer decides.

Return the new workbook.
```

## Notes for the operator

- The Review Instructions tab should travel with the queue so reviewers don't need access to the master ledger.
- Most reviews complete in 30–90 minutes if the queue is well-sorted and the recommended_fix column is good.
