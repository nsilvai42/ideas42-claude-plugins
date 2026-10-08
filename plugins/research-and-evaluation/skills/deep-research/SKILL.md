---
name: deep-research
description: >-
  Produces structured, source-backed evidence scans and research syntheses with scoping, Deep Research prompts, claim extraction, citation ledgers, verification prep, evidence reports, and executive summaries. Use for literature reviews, evidence scans, landscape scans, policy scans, research briefs, source-backed summaries, citation checks, fact-checks, or synthesis across multiple research outputs. Phase 1 when the user has a topic or research question; Phase 2 when they have completed reports, cited drafts, or sources to verify; Phase 3 when they have verified results, corrections, or a citation ledger to synthesize. Do not use for quick factual lookups, single-source summaries, general writing, code review, identity checks, math, consumer/product/travel research, or formal PRISMA-style reviews.
---

# AI-Assisted Evidence Scan

Create a structured, source-backed evidence package through three handoff-based phases: **Scope & Research Prompts → Claim Extraction & Verification Prep → Synthesize Verified Evidence**.

Final package:

- Synthesized Evidence Report
- Synthesized Executive Summary
- Verified Citation Ledger

Phases 1, 2, and 3 are independent entry points. Route based on what the user already has in hand.

## Workflow map

Use the lightest route that still protects evidence quality. Phase boundaries are based on user-side handoffs, not internal model steps.

| Phase                                   | Use when...                                                                                                                        | Output                                                                                                   | User-side next step                                                          |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1. Scope & Research Prompts             | User has a topic, broad question, initial evidence need, preliminary sources, or partially scoped research direction               | Approved research plan + copy-ready Deep Research prompts                                                | Run the prompts externally and return with completed reports                 |
| 2. Claim Extraction & Verification Prep | User has completed Deep Research reports, cited drafts, source-backed research outputs, or source materials that need verification | Extracted material claims + initial Citation Ledger + verification prompts / instructions                | Run external verification and return with verified ledger / correction notes |
| 3. Synthesize Verified Evidence         | User has verified results, a verified Citation Ledger, correction notes, or verifier output to apply                             | Corrected source notes / reports if needed + Synthesized Evidence Report + Synthesized Executive Summary + updated Verified Citation Ledger if needed | Use or share final outputs                                                   |

## Scale check / off-ramps

Before starting the pipeline, check whether the request needs a verified multi-source synthesis. When in doubt, recommend the full or compact workflow including scoping and verification.

Answer directly or use ordinary tools when the user wants:

- a quick factual lookup
- a single-source or one-paper summary
- a narrow claim check that does not need a ledger
- code review, identity checks, or arithmetic / math verification
- consumer/product/travel research
- general writing or editing

If the user wants a lightweight evidence answer, offer a brief source-backed response instead of forcing the full pipeline. Use the full workflow when the output needs structured scoping, multiple sources, verification, or a reusable evidence package.

For formal PRISMA-style systematic reviews, meta-analyses, or publication-grade literature reviews, explain that this skill can support scoping and synthesis but is not a replacement for a specialized review workflow or tool. Suggest a specialized review workflow or tool such as Elicit when appropriate.

## Phase routing

Infer the starting phase from the user’s request and files. Ask using the `AskUserQuestion` tool only when the starting point or available artifacts are ambiguous.

| User has...                                                                                                         | Start at                                                  | Ask before proceeding?                          |
| ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------- |
| Only a broad topic or question, or a poorly scoped set of research questions                                        | Phase 1: Scope & Research Prompts                         | Yes, gather missing scope                       |
| Topic plus seeds, sources, audience, or angles but missing scope dimensions                                         | Phase 1: Scope & Research Prompts, accelerated            | Ask only for missing dimensions                 |
| Approved research plan but no customized Deep Research prompts yet                                                  | Phase 1: Scope & Research Prompts, prompt generation step | Usually no                                      |
| Completed research reports, Deep Research outputs, cited drafts, or source-backed outputs that require verification | Phase 2: Claim Extraction & Verification Prep             | Only if files are unclear                       |
| Verified results, a verified Citation Ledger, correction notes, or verifier output for material claims in source research reports | Phase 3: Synthesize Verified Evidence                     | Usually no                                      |
| Quick factual question, one source, or formal academic systematic review / meta-analysis                            | Off-ramp                                                  | No, answer directly or route to better workflow |

Do not re-scope when the user enters at Phase 2 or Phase 3 unless the purpose is unclear, the scope is poorly defined or missing dimensions, the files are unusable, the artifacts lack enough information for the requested output, or the user explicitly asks to revisit scope.

When the user's opening message is ambiguous about which phase they are entering — for example, mixed cues about both having a topic AND having uploaded reports, or a generic "help me with research" without a clear artifact handoff — confirm phase explicitly via `AskUserQuestion` *before* asking any scoping or format question. Use language such as: "Confirm phase before scope: do you want Deep Research prompts (Phase 1), verification of existing research outputs (Phase 2), or synthesis of verified material (Phase 3)?" Do not let format / depth / audience questions on turn 2 substitute for the phase-routing check on turn 1.

Phase 1 is a handoff point. Generate copy-ready Deep Research prompts for the user to run externally, then stop. Phase 2 begins when the user returns with completed research outputs or source-backed drafts. Phase 3 begins when the user returns with verified results, a verified ledger, correction notes, or verifier output. Phase 3 applies corrections before synthesis when corrections have not already been applied.

## Detailed instructions

Read only the file needed for the current phase or user request:

- Phase 1 scoping and research prompts: `references/phase-1-scope.md`
- Phase 2 claim extraction and verification prep: `references/phase-2-verify-prep.md`
- Phase 3 synthesis: `references/phase-3-synthesize.md`
- Applying verifier corrections: `references/correction-workflow.md`
- Prompt templates: `references/prompt-templates.md`
- Output templates: `references/output-formats.md`
- Quality checks: `references/quality-rubric.md`
- Examples for calibration: `references/examples.md`
- Claim extraction agent: `agents/claim-extractor.md`
- Quality audit agent: `agents/quality-auditor.md`
- Evaluation cases: `evals/evals.json`
- Ledger creation: `scripts/create_ledger.py`
- Ledger validation: `scripts/validate_ledger.py`
- Cross-report inconsistency candidates: `scripts/find_cross_report_inconsistencies.py`
- Apply ledger corrections to a source report: `scripts/apply_corrections.py`

Use `references/prompt-templates.md` when the user asks only for a reusable Deep Research prompt template or when Phase 1 needs to generate final customized prompts.

Use `references/quality-rubric.md` before completing any phase. Use `references/examples.md` only when an example would help calibrate scope, claim extraction, verification codes, evidence strength, or wrap-up style.

Use `scripts/create_ledger.py` in Phase 2 when the environment supports running Python and producing downloadable `.xlsx` files. If the script cannot be run, preserve the same ledger schema in a Markdown table or copy block and tell the user it should be converted to `.xlsx` before external verification.

Use `scripts/validate_ledger.py` when a Citation Ledger is created, returned from verification, or finalized. Run it with the validation stage that matches the workflow point: `initial`, `verified`, or `final`.


## Agent usage

Use agents only where context isolation improves reliability. If the environment does not support subagents, perform the same checks inline and continue the workflow — the agent files are also valid prompt templates for inline use.

**Phase 2 extraction:** When the user provides multiple substantial reports or cited drafts, spawn one extraction subagent per report using `agents/claim-extractor.md`. Give each subagent only one report, the report ID, and the extraction scope. Collect the structured outputs, resolve duplicate or overlapping claims in the main thread, then create the Citation Ledger with `scripts/create_ledger.py` when possible.

*Subagent capacity caveat:* per-report subagents commonly fail with "Prompt is too long" on real Deep Research reports because the source artifact alone consumes most of the subagent context budget. The failure is about the report length, not the spawn prompt. When a subagent spawn fails this way, do not retry with a shorter spawn prompt — switch to the chunked inline fallback below. For ≥4 substantial reports, plan on the chunked inline path from the start and write extraction JSON to disk between sections so the main thread is not holding N×report-length simultaneously.

*Inline fallback (no subagents, or after a subagent capacity failure):* read `agents/claim-extractor.md` and follow it as a prompt-to-self for each report, one report at a time. For long reports, follow the `<chunked_extraction>` block in that file — extract section-by-section, write the per-section JSON to disk between sections, and merge in the main thread once all sections are done. Produce the same JSON output schema. The claim_extractor schema is already aligned to the canonical Citation Ledger schema, so the JSON feeds straight into `scripts/create_ledger.py` without translation.

**Phase 2 and Phase 3 quality checks:** Before handing off Phase 2 or finalizing Phase 3, use `agents/quality-auditor.md` when subagents are available. Give the auditor the phase, the artifact being checked, and `references/quality-rubric.md`. Fix blocking issues before wrap-up. Do not use a synthesis subagent for Phase 3; final synthesis should stay in the main thread so all verified claims, contradictions, and limitations remain visible together.

*Inline fallback (no subagents):* read `agents/quality-auditor.md` and `references/quality-rubric.md` and produce the same Pass / Revise-before-handoff audit inline before the wrap-up. Document the audit result in the run summary or a `quality-audit.md` file alongside the deliverables. The producer-self-grading risk is real but partially mitigated when the audit is a separate explicit step against the rubric, even in the same context.

## Core principles

- Preserve evidence quality over speed. The workflow exists to prevent plausible but unsupported synthesis.
- Keep the user oriented. Tell them which phase they are in, what artifact you are producing, and what they need to do next.
- Use the fewest steps that are sufficient for the user’s goal. Do not force the full pipeline when a lighter route is enough.
- Separate research generation from verification. Treat generated research outputs as drafts to check, not as final evidence.
- Make uncertainty visible. Flag weak, conflicting, outdated, missing, or adjacent evidence instead of smoothing it away.
- Keep material claims traceable. Material factual claims in source reports should connect to a source, citation, verification status, and correction note when needed.
- Verification catches subtle errors, not just fabricated sources. Watch especially for misattributions, composite statistics, overstated effects, generous framing, and claims that blend multiple sources.
- Use the verified Citation Ledger as the source of truth for final synthesis.

## Standard phase wrap-up

End each phase with a clear handoff so the user understands what happened, can access the next-step materials, and knows how to re-enter the workflow.

Each wrap-up should include:

- a one-line summary of what was done
- output links or artifacts
- what the user should do next outside this chat, if anything
- re-invocation language for returning to the workflow

Compactness > completeness. Skip "What we started with" verbatim quotes and exhaustive enumerations of what was done unless the user is far from context — they have the conversation.

When a phase produces copy-ready prompts, files, or outputs, render them at the bottom of the message using the lightest available format:

- **`mcp__visualize__show_widget` available — preferred.** Render copy-ready items as a tabbed-preview widget (one tab per item, copy-to-clipboard button on each tab) when there are 2+ items; single artifact otherwise. Call `mcp__visualize__read_me` first.
- **Claude artifacts / preview tabs available — fallback.** Create one Markdown artifact per copy-ready item.
- **Otherwise — required final fallback.** Output each item in its own fenced Markdown block.

When a phase produces a file, attach or link the file clearly. If a file cannot be produced in the current environment, provide a copyable fallback and state what file format the user should convert it into.

## Phase summaries

### Phase 1: Scope & Research Prompts

Use this phase when the user has a broad topic, early question, preliminary sources, or partially scoped research direction that still needs sharper boundaries before external research. Clarify the decision context, audience, depth, evidence preferences, scope boundaries, literature boundaries, and seed sources. Produce an approved research plan and customized Deep Research prompt(s) the user can run outside this chat.

Read `references/phase-1-scope.md` for the full procedure and `references/prompt-templates.md` when generating the final prompts.

### Phase 2: Claim Extraction & Verification Prep

Use this phase when the user provides completed Deep Research reports, cited drafts, source-backed research outputs, or source materials that need verification. Inventory the artifacts, run an extraction sanity check, extract material claims, map them to sources and evidence details, build the initial Citation Ledger, flag cross-report inconsistencies, and generate verification prompts / instructions for external source checking. For multiple substantial reports, use `agents/claim-extractor.md` to extract each report independently before merging in the main thread.

Read `references/phase-2-verify-prep.md` for the full procedure, `references/output-formats.md` for ledger and verification packet templates, `agents/claim-extractor.md` when extracting multiple reports with subagents, and `scripts/create_ledger.py` when generating the `.xlsx` Citation Ledger. Run `scripts/validate_ledger.py --stage initial` when an `.xlsx` ledger is created and before handing it off for external verification. Run `scripts/find_cross_report_inconsistencies.py` against the initial ledger to surface candidate cross-report conflicts mechanically before triaging them into the Cross-Report Inconsistencies tab. Use `agents/quality-auditor.md` before Phase 2 wrap-up when subagents are available.

### Phase 3: Synthesize Verified Evidence

Use this phase when the user provides verified results, a verified Citation Ledger, correction notes, or verifier output. First apply corrections to the ledger and source research notes / reports when needed, without overwriting originals. Then create the final evidence package from verified and corrected claims only: corrected source notes / reports if needed, Synthesized Evidence Report, Synthesized Executive Summary, and an updated Verified Citation Ledger if needed. Preserve citations, limitations, strength-of-evidence judgments, verification notes, contradictions, and practical implications.

Read `references/phase-3-synthesize.md` for the full procedure, `references/correction-workflow.md` when applying verifier corrections, and `references/output-formats.md` for report templates. Run `scripts/validate_ledger.py --stage verified` after normalizing verifier output and `scripts/validate_ledger.py --stage final` before final synthesis when an `.xlsx` ledger is available. Use `scripts/apply_corrections.py` to mechanically apply the two-pass corrected-source-report workflow (inline targeted substitution + per-document Corrections appendix for any unanchored flags) when source report text is available; this is the documented default for ≥3 reports. Use `agents/quality-auditor.md` before final wrap-up when subagents are available.

