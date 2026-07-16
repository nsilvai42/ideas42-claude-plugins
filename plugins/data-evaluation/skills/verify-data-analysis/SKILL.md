---
name: verify-data-analysis
description: Verify AI-generated reports, dashboards, charts, and recommendations by recomputing claims from source data and logging corrections.
---

# /verify-data-analysis — Verify AI-generated data-analysis outputs

## TL;DR

You have an analysis bundle (Word report, dashboard, charts, exec summary) that an AI tool produced from raw data. Before it gets shared, you want confidence that the numbers replicate from the source, the recommendations are supported, and the wording isn't overclaiming. This skill walks you through a lightweight, structured verification: extract every material claim into a ledger, recompute the high-stakes ones deterministically (Python against `clean.csv` / `analysis.json` / raw data), route discrepancies through a human review queue, apply approved corrections, and ship a corrections changelog plus a remaining-limitations note.

The skill is built on five rules learned from a worked example:

1. **Do not use the same model that produced the original analysis as the sole verifier.** Use a different chat session, a different model, or — ideally — deterministic Python against the source data.
2. **Treat the report and dashboard as targets to be checked, never as the source of truth.** The source of truth is `clean.csv` (and behind it, the raw data + the survey/source instrument).
3. **Verify numerically when you can; route to humans when you can't.** Open-text theme counts, denominator choices, and interpretive claims all need human judgment.
4. **Prioritize high-stakes and human-review-flagged claims.** Don't try to re-verify everything.
5. **Make the ledger the decision surface.** Status columns, recommended fixes, human-approval columns, and a final_action column live in the same workbook. The verification output is also the decision tracker.

---

## When to use

- Right before publishing an AI-generated findings report, dashboard, or recommendations deck.
- When someone (a colleague, a partner, a funder) is going to act on the numbers.
- When the analysis touches open-ended fields, multi-select items with parsing edge cases, theme coding, or non-trivial subgroup cuts.
- When the analysis bundle includes multiple linked outputs (report + dashboard + exec summary + charts) and you need them to agree.

## When NOT to use

- For exploratory analysis that won't drive a decision.
- For analyses where you already control the codebase end-to-end and have unit tests.
- For pure descriptive lookups (e.g., "how many sign-ups last week") — use a data-validation workflow instead.
- For evidence-scan / citation verification — use the deep-research skill instead.

---

## Required inputs

- **Source data**: `clean.csv` (or whatever the analyst used as their working dataset after cleaning).
- **At least one analysis output**: the Word report, the dashboard HTML, the chart files, or the deck. More than one is better — cross-output inconsistency is one of the most common findings.
- **The analyst's intermediate artifact, if it exists**: `analysis.json`, the SQL/Python notebook, or the codebook for any qualitative coding.

## Optional inputs (improve the verification)

- The raw data file the analyst started from (so you can audit data prep, not just the final analysis).
- The survey instrument / data dictionary.
- The original analysis prompt or research-question document (lets you do the analytical-completeness audit, not just the numerical audit).
- A list of known points of concern from the analyst or stakeholders (use these as the initial "Human review flag" rows).

---

## Core workflow

Six phases. The first three are about building the ledger; phases 4–6 are about acting on it.

### Phase 0 — Scope and intake

Inventory what you have. Pick which audits you can run.

Five audit types — most engagements run a subset, not all five:

| Audit | Question it answers | Default trigger |
|---|---|---|
| **Numerical verification** | Does this number replicate from `clean.csv`? | Always run on high-stakes claims. |
| **Data-prep audit** | Did the AI's transformation of raw → `clean.csv` produce correct values? | Run when any field involved AI judgment (open-ended → number, verbal → code, multi-select with parsing). |
| **Analytical completeness audit** | Are there research questions the analysis didn't actually answer? | Run when a research-question doc exists. |
| **Interpretive overclaim audit** | Does the prose state more than the data supports? | Run on executive summary, key takeaways, and recommendations. |
| **Correction QA** | After we revise, do the new outputs actually contain the corrections? | Always run after applying corrections. |

Output of Phase 0: a short scope memo naming which audits apply and which artifacts feed each audit.

### Phase 1 — Claim extraction

Read each analysis output. Extract every **material numerical or interpretive claim** that could drive a decision. Atomic claims, stable IDs, location pointers.

A "material claim" is anything load-bearing for a recommendation, executive summary, key takeaway, or top-line headline. Background prose and decorative numbers don't need extraction.

Six claim types to watch for:

| Type | Example |
|---|---|
| **Descriptive** | "N = 310"; "82% likely to enroll" |
| **Derived** | "PAYG mean rank 1.48"; "Optimal Price Point = $800" |
| **Comparative** | "PAYG vs Subscription: +17 percentage points" |
| **Inferential** | "California respondents notably less enthusiastic" |
| **Methodological** | "$575 − $58 − $57 = $460 (net price equalization)" |
| **Interpretive** | "Investment framing dominates over subscription framing" |

The first four are numerically verifiable. Methodological claims usually check arithmetically. Interpretive claims need the overclaim audit, not numerical recomputation.

Output of Phase 1: an initial `claim_ledger.xlsx` with one row per material claim, populated for ID, output, location, claim text, claim type, stakes (H/M/L), source columns, computation rule, original_value. Verified, verifier_value, status, recommended_fix, and human columns are blank.

### Phase 2 — Deterministic recomputation

For every H-stakes numerical claim, write Python that re-derives the value from `clean.csv` (or raw data, for data-prep audit). Record `verifier_value`, `difference`, and `status`.

This is the phase that gives you confidence. **The verifier must be deterministic code, not another LLM chat that ingests the report.** An LLM verifier shares the original model's blind spots and can reanchor on the very numbers you're trying to check.

Six verification statuses:

| Code | Meaning | What to do |
|---|---|---|
| **Replicated** | verifier value matches the claim (within rounding). | Approve as-is. |
| **Drift** | Same intent, small numerical difference (rounding, stale recompute). | Note in the changelog, refresh the value. |
| **Error** | Verifier value differs substantively from the claim. | Route to human review. Almost always a fix. |
| **Unable** | Verifier could not reproduce (missing data, ambiguous method). | Route to human review. Often a method clarification, sometimes a re-run. |
| **Method disagreement** | Both numbers defensible; the analysis chose one method, the verifier chose another (e.g., denominator over full N vs. over known-respondents). | Route to human review. Usually a wording fix, not a value fix. |
| **Directional only** | Open-text theme counts, qualitative tallies, regex-coded categories — verifier can replicate the count but cannot independently validate the regex. | Approve as directional. Do not allow stronger language than "respondents whose response matched the [theme] keywords." |

Output of Phase 2: ledger with `verifier_value`, `difference`, and `status` filled for every priority claim.

### Phase 3 — Human review queue

Filter the ledger to rows that are not "Replicated". Sort by stakes descending. This is the **human review queue**: it should contain every claim that needs a human decision.

For each row, populate:
- `recommended_fix` — the proposed revision wording or value.
- `human_approved` (Yes / No / TBD).
- `human_notes` — any deviation from the recommended fix.
- `final_action` (Approve / Revise output / Add caveat / Exclude claim / No action).

Critical: the reviewer should be **someone other than the analyst who produced the original output**, ideally someone with subject-matter judgment but not someone who has anchored on the existing prose.

Output of Phase 3: a `human_review_queue.xlsx` view (same schema as the ledger, filtered + sorted) plus a one-page review instructions sheet.

### Phase 4 — Apply corrections

Once `human_approved = Yes` and `final_action = Revise output` is set on each row, apply the corrections surgically:

- For every `Error`/`Drift` row: replace the claim wording or value with the `recommended_fix`, preserving surrounding prose.
- For every `Method disagreement` row: reword to add denominator clarity or boundary specificity per the human note.
- For every `Directional only` row marked for revision: soften language to directional (e.g., "% of respondents whose response matched [theme] keywords").
- For every `Unable` row: either replace with a refreshed value, or visibly flag as unverified.
- Replicated rows are untouched.

**Apply across every linked output.** A corrected number on slide 5 of the deck must also be corrected in the dashboard, the report, the executive summary, the chart caption, the appendix, the `analysis.json`, and the methods section. The corrections changelog is the cross-output index.

**Never overwrite the original outputs.** Save as `<filename> (Corrected).<ext>` alongside the originals.

### Phase 5 — Corrections changelog + remaining limitations note

- **Changelog**: one entry per revised claim with ID, status, location, original issue, fix applied, output locations changed. Use the changelog template.
- **Remaining limitations note**: distinguishes what was verified (data, claims) from what remains untested (real-money behavior, brand effects, unaudited qualitative themes, etc.). Use the limitations template.

### Phase 6 — Final narrow QA

Re-scan only the non-replicated rows after corrections are applied. For each, confirm:
1. The corrected output contains the new wording or value.
2. The original wording or value is gone (no orphan instances in chart captions, dashboard tooltips, etc.).
3. Cross-output consistency holds (dashboard and report agree).

Final QA should be tight — minutes, not hours. If anything fails, loop back to Phase 4.

---

## Verification statuses (reference)

| Status | Numerical match | Action |
|---|---|---|
| Replicated | Yes | None |
| Drift | Close but not exact | Refresh value, note in changelog |
| Error | Substantively wrong | Fix value, document |
| Unable | Cannot recompute | Human judgment: refresh or flag |
| Method disagreement | Both defensible | Clarify denominator / boundary in prose |
| Directional only | N/A (qualitative) | Keep directional; require coding audit before quantifying |

---

## Human-in-the-loop gates

These steps **require human judgment**, not Claude judgment:

1. **Approving any `Error`/`Method disagreement` fix on a high-stakes claim.** The wording or denominator choice can change the recommendation.
2. **Promoting a `Directional only` claim to a precise percentage.** This requires a separate coding audit.
3. **Resolving cross-output inconsistencies.** If the dashboard says 82% and the report says 81.9% — which one is the official number?
4. **Accepting an `Unable` row without re-running the analysis.** A flagged-but-unfixed claim should be a deliberate decision, not a default.
5. **Sign-off on the corrected outputs before publication.** A human reads the corrected report end-to-end.

---

## Do-not-publish gates

Do not ship the corrected outputs while any of these are true:

- Any **High-stakes** row has status `Error` or `Unable` and `human_approved` is not `Yes`.
- Any **Method disagreement** on a recommendation-driving claim is unreviewed.
- Any cross-output numerical inconsistency on a high-stakes claim is unresolved.
- The **data-prep audit** failed for any field used in a high-stakes claim, and the remediation is not documented.
- An **interpretive claim** in the executive summary is not supported by a numerical claim in the body.
- The corrections changelog is incomplete (i.e., the ledger lists revised rows that aren't in the changelog).

---

## Output artifacts

A complete verification run produces:

```
verification/
├── claim_ledger.xlsx                           # the master, all claims
├── data_prep_inventory.xlsx                    # per-field transformation log (if data-prep audit run)
├── human_review_queue.xlsx                     # filtered view of non-replicated rows
├── parsing_audits/
│   ├── cost_parsing_audit.xlsx                 # for open-ended numeric inputs
│   ├── multiselect_parsing_audit.xlsx          # for comma-in-label edge cases
│   └── theme_coding_audit.md                   # if qualitative coding was audited
├── corrections_changelog.docx                  # per-claim record of revisions
├── remaining_limitations.docx                  # what was verified vs untested
├── final_verification_memo.md                  # one-page summary for stakeholders
├── <report> (Corrected).docx                   # surgically corrected outputs
└── <dashboard> (Corrected).html
```

---

## Common failure modes

The Calbright worked example surfaced seven distinct issue classes. Watch for these:

1. **Survey timing / duration mismatch.** Stated length vs. observed median completion time often differ; "May" may obscure a 7-day field window.
2. **Screener vs. self-report mismatch.** Recruitment screens to criteria, but final self-reported demographics include respondents outside those criteria.
3. **Denominator ambiguity.** Same numerator, different denominator — "% of N", "% of known income", "% of respondents who answered" can all be defensible but produce different numbers.
4. **Stale subgroup values.** A subgroup table that was computed early and never refreshed when the dataset filtered down.
5. **Multi-select parsing bug.** Option labels with embedded commas break naive comma-split parsers and over- or under-count.
6. **Confidence-factor / unverified-denominator inflation.** A number that looks right because it has the right shape (e.g., 85%) but doesn't replicate at any plausible denominator.
7. **Overbroad summary language.** "PAYG leads every metric" when in fact one metric is a near-tie. Common in executive-summary headline cards.

The taxonomy above is also useful as a *checklist for the claim-extraction phase* — when you see one of these patterns in the original output, flag the row as `human_review_needed = Yes` even if the number replicates, because the framing might still need work.

---

## Rules for correcting final outputs

- **Never overwrite the original.** Save corrected versions with `(Corrected)` suffix.
- **Apply corrections surgically.** Touch only the prose, table cells, or data values that the ledger specifies. Don't rewrite unaffected sections.
- **Update all linked outputs together.** Report, dashboard, exec summary, chart captions, embedded JSON, appendix tables, methods notes. The changelog is the cross-output index.
- **Add a "Verification note" to the methods section** explaining that high-stakes and human-flagged claims were independently checked against the source data.
- **Keep open-text theme counts directional** unless a separate coding audit was completed and documented.
- **Do not introduce new numerical claims** that aren't in the verified ledger, `analysis.json`, or `clean.csv`. Verification is for checking, not extending.
- **No silent rewriting of recommendations.** If a correction changes a finding's strength, surface the change in the changelog and the executive summary.

---

## Tool guidance

Three tool types, each for a different job:

### Deterministic Python (the bulk of the work)

Use for: numerical recomputation, data-prep audits, multi-select parsing audits, cross-output consistency checks, final QA scans.

Why: same input → same output, every time. The verifier cannot be reanchored by the prose it's checking.

Pattern: read `clean.csv` with pandas, compute the same statistic the original claim implies, compare to `original_value`, record `verifier_value` and `difference`.

### LLM (a small slice of the work)

Use for: claim extraction from prose (the LLM is good at finding "load-bearing" numerical claims in long reports); proposing wording for `recommended_fix` once a discrepancy is identified; drafting changelog entries from the ledger.

**Critical:** do not use the same chat session, project, or model that generated the original analysis. Use a fresh session with no memory; ideally a different model for the extraction pass.

### Human (the irreducible judgment work)

Use for: approving fixes on high-stakes claims; deciding denominator/boundary choices; promoting directional themes; resolving cross-output inconsistencies; signing off on corrected outputs.

The ledger's `human_approved` and `human_notes` columns are the durable record of these decisions.

---

## Quick-start

If you've never run this before:

1. Drop the analysis bundle and `clean.csv` in a folder.
2. Open `prompts/extract_claims.md`. Run it in a fresh chat against your outputs to produce the initial claim ledger.
3. Open `prompts/verify_high_stakes_claims.md`. Hand it the ledger and `clean.csv` to populate `verifier_value` and `status`.
4. Filter to non-Replicated rows → that's your human review queue.
5. Review, approve, decide.
6. Use `prompts/apply_corrections.md` to revise the outputs surgically.
7. Use `prompts/final_qa.md` to confirm.
8. Ship.

Templates and prompts live in `templates/` and `prompts/`. The Calbright worked example is in `examples/calbright_worked_example.md`.
