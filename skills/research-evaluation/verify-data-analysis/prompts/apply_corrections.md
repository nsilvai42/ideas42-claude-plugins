# Prompt — Apply human-approved corrections to a report / dashboard

**Use in:** a chat with read/write access to the original outputs. Save corrected copies with `(Corrected)` suffix; never overwrite.

**Inputs:**
- The verified ledger with `human_approved = Yes` and `final_action = Revise output` on the rows to apply
- The original Word report
- The original dashboard HTML (and embedded JSON / data)
- The original analysis.json
- Any chart caption files

**Output:** corrected versions of all linked outputs, plus a populated `Corrections Applied` tab in the ledger.

---

## Prompt

```
You are applying human-approved corrections to data-analysis outputs. The verified ledger is the source of truth for what to change. The original outputs are the targets — never source.

INPUTS:
- verified_claim_ledger.xlsx (with human_approved and final_action filled)
- original outputs:
  - <report filename>.docx
  - <dashboard filename>.html
  - analysis.json
  - <any chart caption files>

TASK:

For every row where human_approved = Yes AND final_action = Revise output:

1. Read the claim's `location` field. Locate the exact passage in the corresponding output.

2. Apply the correction:
   - Error: replace original_value with verifier_value or recommended_fix.
   - Drift: refresh the value.
   - Method disagreement: replace with the human-approved denominator-clarified wording.
   - Directional only: soften language to directional per the recommended_fix.
   - Unable: per the human note, either refresh or visibly flag as unverified.

3. Look for the same value or wording in OTHER outputs — exec summary, chart captions, KPI cards, embedded JSON, methods notes, appendix tables. Update all of them. The claim's `outputs` field and the cross-output-inconsistencies tab help locate parallels.

4. Update analysis.json values where the corrected number is canonical (e.g., the corrected money-source counts replace the buggy parser output).

5. Add a "Verification note" to the Methods section of the report (and the corresponding Sample & Methods area of the dashboard) explaining that high-stakes and human-review-flagged claims were independently checked against clean.csv and analysis.json.

6. Save corrected outputs alongside the originals:
   - <report> (Corrected).docx
   - <dashboard> (Corrected).html
   - analysis_corrected.json

7. For every applied row, populate the "Corrections Applied" tab of the ledger:
   | claim_id | status | original_text | corrected_text | outputs_changed | reason | applied_by | applied_date |

CONSTRAINTS:
- NEVER overwrite the originals. Save copies with "(Corrected)" suffix.
- Apply corrections surgically. Touch only the prose, table cells, or data values the ledger specifies.
- Do not introduce new numerical claims. Every value must trace to clean.csv, analysis_corrected.json, or the verified ledger.
- Do not silently rewrite recommendations. If a correction changes a finding's strength, ensure the changelog and exec summary reflect it.
- Maintain cross-output consistency. The same statistic appearing in multiple places must end up with the same value.

Return:
- The corrected files
- The populated Corrections Applied tab
- A short summary listing every claim_id revised, by output
```

## Notes for the operator

- After this step, the Corrections Applied tab effectively contains the changelog content. The changelog template formats it for human consumption.
- Final QA scans only the revised claims, so the better Corrections Applied is populated, the faster QA goes.
