# Quality Rubric

Use this reference as a phase-gate checklist before completing major outputs. The goal is to prevent plausible but unsupported research products.

## Contents

1. Phase 1 quality gates
2. Phase 2 quality gates
3. Phase 3 quality gates
4. Evidence strength rubric
5. Do-not-proceed gates

## Phase 1 quality gates

Before generating Deep Research prompts, confirm:

- The audience and purpose are known or explicitly defaulted.
- The research lens is clear: effectiveness, design, landscape, implementation, mixed, or other.
- The research question(s) are answerable and not just broad topic labels.
- Depth is set: Light, Standard, or Thorough.
- Scope boundaries are defined or defaulted:
  - date range
  - geography
  - population / setting
  - intervention / program / benefit scope
  - outcomes
  - exclusions
- Evidence preferences are specified or defaulted.
- Seed sources are confirmed, proposed, or explicitly absent.
- The final prompt(s) include scope boundaries and exclusions.
- The user has approved the research plan before final prompts are generated, unless they explicitly requested a reusable template only.

Do not generate final Deep Research prompts if the prompt would send the research tool into a vague domain without audience, scope, or evidence priorities.

## Phase 2 quality gates

Before handing off verification materials, confirm:

- Reports and source materials are inventoried.
- Extraction quality was checked.
- Broken PDF / table extraction risks were flagged.
- Material claims were extracted from each report, up to 5 reports unless the work is batched.
- Claim IDs are unique.
- Each claim includes:
  - Report
  - Claim ID
  - Section
  - Claim
  - Source Cited, when available
  - Full Citation, when available
  - Evidence Type
  - Stakes
- Stakes are H / M / L.
- Initial `Verified`, `Verification Notes`, `Correction`, and `Claude QA` fields are blank.
- References are mapped to claim IDs where possible.
- Cross-report inconsistencies were checked and logged.
- Claims were checked for subtle verification risks: misattribution, composite statistics, overstated framing, source blending, and overgeneralization beyond the cited source.
- The verification prompt includes a “Pay particular attention” block at the top.
- The verification prompt states that the primary output is an updated Citation Ledger `.xlsx`, and that narrative-only verification is incomplete unless files cannot be produced.
- If an `.xlsx` ledger was created, `scripts/validate_ledger.py --stage initial` was run or the same checks were applied manually.
- The user receives clear instructions for how to return with verified results.

Do not call evidence verified in Phase 2. Phase 2 prepares verification; it does not complete it.

## Phase 3 quality gates

Before final synthesis, confirm:

- Verification results are normalized into the ledger structure.
- If an `.xlsx` verified ledger is available, `scripts/validate_ledger.py --stage verified` was run or the same checks were applied manually.
- [P] and [X] rows have correction text.
- [U] rows are visibly flagged or excluded from final claims.
- Corrections Applied changelog exists when corrections exist.
- Corrected reports / notes were created when original report text was available, up to 5 reports unless the work is batched.
- Original files were not overwritten.
- Claude QA was run on corrected rows.
- If an `.xlsx` final ledger is available, `scripts/validate_ledger.py --stage final` was run or the same checks were applied manually.
- No unresolved correction mismatch remains.
- Final synthesis uses verified and corrected material only.
- Every factual claim in the Evidence Report and Executive Summary has a citation.
- Contradictions and limitations are preserved.
- Inferences are marked with `[INFERENCE]`.
- Practical implications are specific to the user’s context.
- If there are multiple research questions, synthesis first addresses each question, then surfaces cross-question mechanisms, contradictions, evidence gaps, and practical implications.
- If the evidence base is thin, limitations are stated clearly and the output recommends broadening scope, adding better seeds, narrowing claims, or re-running research.

Do not synthesize a polished final report from unverified or uncorrected claims unless the user explicitly asks for an exploratory draft and the limitations are prominently labeled.

## Evidence strength rubric

Use the GRADE framework. GRADE is the de facto standard for evidence-strength rating across systematic reviewers, the WHO, Cochrane, and most policy bodies. Apply it consistently.

| Label | Use when... |
|---|---|
| High | Further research is very unlikely to change confidence in the estimate. Multiple high-quality RCTs, well-conducted meta-analyses, or systematic reviews with consistent findings across populations. |
| Moderate | Further research is likely to have an important impact and may change the estimate. RCTs with limitations (inconsistent results, methodological flaws, indirectness, or imprecision) OR exceptionally strong observational evidence. |
| Low | Further research is very likely to change the estimate. Observational studies without exceptional strengths, or RCTs with serious limitations. |
| Very Low | Any estimate is highly uncertain. Case reports, expert opinion, theoretical reasoning, or studies with major methodological flaws. |

**Adjacent-domain extrapolation:** If a finding draws on evidence from a different population, setting, or intervention than the research question, label it `Very Low — adjacent-domain extrapolation` regardless of the underlying study's quality. Adjacent-domain evidence is never elevated above Very Low.

**Mixed / contradictory evidence:** GRADE strength is not a label for direction. When sources conflict, assign the strength label that reflects the overall body of evidence and add a separate `[mixed evidence]` flag. Surface the contradiction explicitly in the synthesis rather than averaging it away.

When uncertain between labels, choose the more cautious label and explain why.

## Do-not-proceed gates

Pause or warn the user before continuing when:

- Phase 1 lacks enough scope to generate useful prompts.
- Research reports have no citations or unusable citations. Flag the limitation, extract claims anyway, and warn that many claims may verify as [U].
- Extraction appears broken because numeric values are missing.
- Phase 2 ledger lacks required columns or unique Claim IDs.
- [P] or [X] rows lack correction text before synthesis.
- Claude QA contains unresolved failures.
- Major cross-report inconsistencies remain unresolved and central to the research question.
- More than 30% of material claims are [U] or [X].
- Evidence base is too thin for the requested synthesis. Recommend broadening scope, adding better seeds, narrowing the claims, or re-running research.
- `scripts/validate_ledger.py` fails for the relevant stage and the issue is not explicitly documented as unresolved.
- The user asks for a formal systematic review or meta-analysis beyond this skill’s scope.

When a gate blocks progress, offer the smallest next step: clarify scope, re-export files, run targeted verification, narrow the synthesis, or re-run research.

