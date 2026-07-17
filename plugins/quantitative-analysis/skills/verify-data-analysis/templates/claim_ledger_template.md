# Claim Ledger Template

The claim ledger is the central artifact of a verification pass. It's both the verification output and the human decision tracker. Implement as an `.xlsx` workbook with the tabs below.

## Tab 1 — README

Single-page metadata sheet.

| Field | Example |
|---|---|
| Topic | Calbright Affordability Pilot |
| Source data | clean.csv (N=310, fielded Apr 30 – May 8, 2026) |
| Outputs verified | Findings Report.docx, Findings Dashboard.html, analysis.json |
| Verifier | Independent Claude pass against source data; not the model that generated the original analysis |
| Verifier date | 2026-05-19 |
| Status codes | Replicated · Drift · Error · Unable · Method disagreement · Directional only |
| Stakes codes | H = drives a recommendation; M = supports an argument; L = background |
| Verification scope | All high-stakes claims + all human-review-flagged rows |

## Tab 2 — Claims (the master)

One row per material claim.

| Column | Type | Description |
|---|---|---|
| claim_id | string | Stable ID, format `CL-###` |
| output | string | Which file the claim appears in (report / dashboard / analysis.json / chart) |
| location | string | Section heading + page, or chart title + caption |
| claim_text | string | The claim verbatim or lightly paraphrased |
| claim_type | enum | descriptive / derived / comparative / inferential / methodological / interpretive |
| stakes | enum | H / M / L |
| source_columns | string | Which `clean.csv` columns the claim derives from |
| computation_rule | string | The pandas / SQL expression that re-derives the value |
| numerator | int/float | If applicable |
| denominator | int/float | If applicable |
| original_value | string | The value as stated in the output |
| verifier_value | string | Value computed by deterministic Python against source |
| difference | string | verifier_value − original_value (or qualitative diff) |
| status | enum | Replicated / Drift / Error / Unable / Method disagreement / Directional only |
| verification_notes | string | What the verifier checked and why the status applies |
| human_review_needed | bool | Yes if status != Replicated, or stakes = H and verification has ambiguity |
| recommended_fix | string | Proposed revision wording or value (filled by verifier for non-Replicated rows) |
| human_approved | enum | Yes / No / TBD |
| human_notes | string | Reviewer's wording choice or rationale for deviating from recommended_fix |
| final_action | enum | Approve / Revise output / Add caveat / Exclude claim / No action |
| post_correction_qa | enum | ✓ / ✗ / N/A |

## Tab 3 — Cross-Output Inconsistencies

Long-format: one row per (inconsistency × output).

| Column | Description |
|---|---|
| inconsistency_id | X01, X02, etc. Repeats across rows of the same inconsistency. |
| output | Which file this row's value came from |
| claim_id | Linked claim_id in the master ledger |
| value_in_this_output | The number or wording as it appears here |
| type | numeric / wording / framing |
| resolution | Filled after human review |
| reconciled_value | The canonical value chosen |

## Tab 4 — Corrections Applied

Empty in the initial ledger. Populated as Phase 4 progresses.

| Column | Description |
|---|---|
| claim_id | |
| status | Error / Drift / Method disagreement / Directional only |
| original_text | As extracted |
| corrected_text | After revision |
| outputs_changed | Comma-separated list (e.g., "report §3.2; dashboard RQ2 takeaway; exec summary card 3") |
| reason | Short explanation tied to verifier_notes |
| applied_by | Person / agent that made the edit |
| applied_date | |

## Tab 5 — Coverage QA Summary

| Output | Total claims | H | M | L | # Replicated | # Drift | # Error | # Unable | # Method-disagreement | # Directional |
|---|---|---|---|---|---|---|---|---|---|---|
| Report | | | | | | | | | | |
| Dashboard | | | | | | | | | | |
| analysis.json | | | | | | | | | | |
| Charts | | | | | | | | | | |
| **Total** | | | | | | | | | | |

