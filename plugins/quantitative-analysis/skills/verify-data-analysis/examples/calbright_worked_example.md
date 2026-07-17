# Worked example — Calbright Affordability Pilot

This is the worked example that the `/verify-analysis` skill is built from. It is intentionally concise and contains no respondent-level PII or confidential raw data — only the structural details of the verification flow and the issue classes that surfaced.

## Inputs

- `clean.csv` — N = 310, fielded April 30 – May 8, 2026, post-screener
- `analysis.json` — intermediate analytical output produced by the original analyst
- Findings Report (.docx)
- Findings Dashboard (.html)
- A research-questions document used to brief the original analysis

## What the verification produced

| Output | Purpose |
|---|---|
| `calbright_affordability_claim_ledger.xlsx` (235 rows) | Initial extraction of every material claim across the report, dashboard, exec summary, and analysis.json |
| `verified_claim_ledger.xlsx` (126 rows recomputed) | Numerical recomputation against clean.csv for all H-stakes + originally human-flagged claims |
| `verified_claim_ledger_with_suggested_approvals.xlsx` | Adds `recommended_fix`, `human_approved`, `final_action` columns + suggested batch decisions |
| `human_review_queue.xlsx` (67 rows) | Filtered, sorted decision surface for the human reviewer |
| 11 approved revisions (CL-003, CL-005, CL-020, CL-073, CL-101, CL-113, CL-139, CL-146, CL-161, CL-217, CL-233) | The Error / Drift / Method-disagreement claims the reviewer approved for revision |
| `Findings Report (Corrected).docx` | Surgically corrected report |
| `Findings Dashboard (Corrected).html` | Surgically corrected dashboard |
| `Calbright_Affordability_Corrections_Changelog.docx` | Per-claim record |
| `Calbright_Affordability_Remaining_Limitations.docx` | Verified-vs-untested note |

## Verification statistics

- 235 material claims extracted across all outputs.
- 126 priority claims verified (all H-stakes + all original human-review flags).
- 115 replicated, 1 drift, 5 error, 5 method disagreement, 0 unable.
- 11 claims approved for output revision after human review.

## Issue classes found

Each Calbright issue maps to a class in the skill's broader failure-mode taxonomy. The mapping is the point of the worked example — it lets you predict the issue classes likely to show up in a *future* AI-generated analysis, even before you start the verification pass.

| Calbright issue | Skill taxonomy class | Why it matters |
|---|---|---|
| **CL-003 — "14-minute survey, May 2026"** described the survey using a target length and an over-broad month; actual fielding was Apr 30 – May 8, 2026 and median completion was ~17 minutes | **Survey timing / duration mismatch** | Methods-section claims often round or summarize fielding details. Verifying against StartDate / EndDate / Duration is cheap and catches this. |
| **CL-005 — Recruitment described as full screen.** Final self-report includes 12 BA/grad, 34 ≥$75k, 60 outside strict working/job-seeking categories | **Screener vs. self-report mismatch** | "Pre-screened to X" is rarely a strict cut. Verifying the screener language against self-reported categorical fields is essential for honest sample descriptions. |
| **CL-020 — "66% under $50k"** | **Denominator ambiguity** | The exact value depends on whether the denominator is full N (64.2%) or known-income respondents (65.2%). Neither is 66%. A different denominator was probably picked unintentionally. |
| **CL-073 — Community college (4.75) grouped with university online (4.94) under a single "~4.94" claim** | **Computation-mismatch / table-to-prose drift** | Prose summaries of multi-row tables often quietly group or round. Re-derive from the source table, not the prose. |
| **CL-101 — "A quarter of respondents guessed under $500"** | **Denominator + boundary ambiguity** | <$500 = 18.3%; ≤$500 = 28.2%; p25 = $500. Three defensible numbers, none of which is exactly "a quarter under $500." Verify against the exact comparison the claim implies. |
| **CL-113 — "79% top-3"** | **Stale or invented value** | Direct recomputation: 75.8% (235/310). The 79% didn't replicate at any plausible denominator. Likely a transcription or rounding error compounded into prose. |
| **CL-139 — "Financial aid 52%"** | **Multi-select parsing bug** | Option label "Financial aid (Pell Grant, state grant, etc.)" contains three commas. Naive `.split(',')` created three spurious labels and under-counted financial aid from 178 → 51 (52%). Robust value: 57.4%. |
| **CL-146 — "Employer assistance, family/partner each ~13–18%"** | **Vague-range summary** | Same multi-select parsing issue, plus a deliberately vague range that doesn't match either value. Robust values: family/partner 20.3%, employer assistance 19.0%. |
| **CL-161 — "Employer value ~85%, clear cost ~78%, financial aid ~76%"** | **Confidence-factor / unverified-denominator inflation** | Three numbers in the right shape but none replicate at any plausible denominator. Robust values 68.7 / 66.8 / 65.5. This is a class of error to watch for: numbers that *feel* right because they're the highest items, but check at the wrong scale. |
| **CL-217 — "PAYG working 82.4% / unemployed 79.6%"** | **Stale subgroup values** | Robust recompute: 81.2 / 79.4. Small drift, likely from a subgroup table computed early in the analysis and not refreshed after a filter step. |
| **CL-233 — "PAYG leads on every metric"** | **Overbroad summary language** | PAYG leads enrollment, fairness, and ranking — but on "best for motivation," Progress-Based Refund narrowly wins (114 vs 113). "Every metric" is overclaim. Common in exec-summary headline cards. |

## What the skill carries forward

The seven failure-mode classes in `SKILL.md` are the same classes above with names normalized for reuse:

1. Survey timing / duration mismatch
2. Screener vs. self-report mismatch
3. Denominator ambiguity (incl. boundary issues — CL-101)
4. Stale subgroup values
5. Multi-select parsing bug (including comma-in-label edge cases)
6. Confidence-factor / unverified-denominator inflation (a.k.a. computation-mismatch with a plausible shape)
7. Overbroad summary language

Two patterns from Calbright that surfaced *too rarely* to be top-of-taxonomy but are worth watching:

- **Table-to-prose drift** (CL-073): a multi-row table summarized in one number that doesn't appear in the table.
- **Vague-range summary** (CL-146): "respondents ranged from X to Y" where neither bound matches.

## How the workflow handled each class

| Class | Audit type | Verification status assigned |
|---|---|---|
| Survey timing / duration | Numerical against StartDate/EndDate/Duration | Method disagreement |
| Screener vs. self-report | Numerical against demographics columns | Method disagreement |
| Denominator ambiguity | Numerical with multiple denominators tried | Method disagreement (or Error, if neither denom matches) |
| Stale subgroup values | Numerical recompute | Drift |
| Multi-select parsing bug | Multi-select parsing audit (separate prompt) | Error (data-prep failure) |
| Confidence-factor inflation | Numerical recompute with denominator stress test | Error |
| Overbroad summary language | Interpretive overclaim audit (human judgment) | Error |
| Table-to-prose drift | Numerical recompute against the source table | Error |
| Vague-range summary | Numerical recompute | Error |

## Lessons

Three things this worked example confirmed that shaped the skill:

1. **A single multi-select parsing bug propagated into a dozen downstream claims.** Once the parser was fixed, money-source counts AND confidence-factor counts both needed updating (the latter shared the same parser). Data-prep audits prevent this; downstream-claim-only verification doesn't.

2. **Overbroad summary language is the most decision-relevant class.** A number being slightly wrong rarely changes a recommendation. A claim of "PAYG leads every metric" being qualified to "leads on enrollment, fairness, ranking; near-tie on motivation" *does*, because it opens the door to Progress-Based Refund for a sub-segment. Save reviewer attention for exec-summary and recommendation-section language.

3. **The ledger as decision surface saved cycles.** Once `recommended_fix` and `human_approved` columns lived in the same workbook as the verification output, the reviewer could approve batch dispositions and override individual rows in the same place. The skill is built around keeping these columns together rather than scattering them across separate docs.
