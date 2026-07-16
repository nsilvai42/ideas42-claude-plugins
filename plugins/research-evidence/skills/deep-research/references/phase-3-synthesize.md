# Phase 3: Synthesize Verified Evidence

Use this reference when the user returns with verified results, a verified Citation Ledger, correction notes, verifier output, corrected reports, or source-backed notes ready for final synthesis.

## Phase 3 navigation

| Step | What happens | Output |
|---|---|---|
| 1. Intake | Identify verified ledger, correction notes, verifier output, up to 5 corrected or original research reports, and approved research plan | Verified artifact inventory |
| 2. Normalize | Convert verifier output into the Citation Ledger structure when needed | Updated verification fields |
| 3. Apply corrections | Read `references/correction-workflow.md` and apply corrections without overwriting originals | Corrected reports / notes + correction changelog |
| 4. QA | Validate correction application and ledger completeness | QA-passed ledger / notes |
| 5. Synthesize | Read `references/output-formats.md` and create the final evidence package from verified and corrected material only | Evidence Report + Executive Summary + final ledger |
| 6. Handoff | Tell the user how to use, share, or optionally upload outputs to NotebookLM | Phase 3 wrap-up |

Use these steps sequentially, but do not force unnecessary interaction. If the user already provides corrected reports and a finalized ledger, summarize what is available and move directly to synthesis.

## Goal

Turn verified research materials into a final evidence package:

- corrected source research reports / notes, when corrections have not already been applied
- Corrections Applied changelog, when corrections exist
- finalized Citation Ledger
- comprehensive Evidence Report
- concise Executive Summary
- optional NotebookLM handoff guidance

Phase 3 ends when the user has final files ready to use, share, or upload for alternate digest formats.

## Inputs

Start from whatever the user provides:

- verified Citation Ledger `.xlsx`
- pasted verifier narrative or correction table
- Perplexity / fresh Claude verification output
- correction notes
- original or corrected Deep Research reports, usually up to 5 from Phase 1 research prompts
- approved research plan from Phase 1
- initial Citation Ledger from Phase 2

If the user returns with pasted text instead of a ledger, read `references/correction-workflow.md` before proceeding. Normalize the verifier output into the ledger structure wherever possible. If the narrative only covers some rows, tell the user which rows are still unverified and offer to create a targeted follow-up verification prompt for those rows.

If the verifier returned more than requested, such as a pre-filled Corrections Applied tab, preserve the signal and reshape it into the ledger schema. Do not discard useful verification work just because it does not exactly match the requested format.

If the verified ledger covers fewer claims than the Phase 2 ledger (the verifier prioritized or batched), do not silently drop the unverified rows. Note in the synthesis which Phase 2 claims were not in the verified ledger and offer the user the option of a targeted follow-up verification pass for those rows. Do not synthesize from unverified Phase 2 claims as if they were verified.

If original Deep Research reports are not provided, do not produce corrected source reports. Keep correction text in the final ledger and the Corrections Applied changelog only, and note in the wrap-up that corrected source files were not produced because original report text was not available.

If corrections arrived pre-specified, summarize in one line, such as:

```markdown
Proceeding with the [N] corrections you specified.
```

Do not ask “do you want me to go ahead?” when the verification return already specifies corrections. That gate creates friction after the user has completed the external verification step.

## Output-budget pre-flight

Before producing the Phase 3 deliverable set, take stock of the volume. The full deliverable set — corrected source reports, Corrections Applied changelog, final Citation Ledger, Evidence Report, Executive Summary — is heavy in a single context, and the heaviest single output is the corrected source reports. Plan the order before starting prose.

| Input dimension | Threshold | Action if at or above |
|---|---|---|
| Reports | ≥ 4 | Use the targeted-substitution + corrections-appendix default in `references/correction-workflow.md`. Whole-text regeneration of corrected source reports likely will not fit in one context. |
| Total claims | ≥ 200 | Build the ledger and corrected source reports in this chat; consider handing the Evidence Report + Executive Summary off to a fresh chat with the verified ledger and corrected reports as inputs. |
| [P] + [X] flags | ≥ 50 | Run `scripts/apply_corrections.py` if available. The mandatory per-document Corrections appendix becomes a meaningful chunk of output; account for it in budgeting. |
| Cross-report inconsistencies | ≥ 10 | Synthesize convergence and contradictions per research question first, then look across questions, rather than mixing both in one pass. |

Thresholds are heuristics, not hard limits. For a standard 3-report scan with under 200 claims, all deliverables typically fit in a single context. Above 3 reports, plan the split before producing prose.

If splitting across chats, keep Phase 3.1 (corrections + corrected source reports + final ledger) in this chat and hand off Phase 3.2 (Evidence Report + Executive Summary) to a fresh chat with the corrected materials as inputs.

## Correction workflow

If corrections have not already been applied, read `references/correction-workflow.md` and follow it before synthesis.

Correction workflow handles:

- normalizing verified results
- applying [P] and [X] corrections surgically
- preserving [C] claims exactly
- flagging [U] claims as unverified
- producing corrected source reports / notes for up to 5 research reports when source text is available
- creating the Corrections Applied changelog
- updating the Citation Ledger
- running Claude QA on corrected rows
- protecting original files from overwrite

Do not proceed to final synthesis while known correction mismatches remain unresolved.

## Synthesis rules

Use the verified Citation Ledger and corrected source notes / reports as the source of truth.

When synthesizing:

- use verified and corrected claims only
- cite every factual claim
- flag any inference with `[INFERENCE]`
- distinguish direct evidence from adjacent-domain evidence
- distinguish causal, quasi-experimental, observational, qualitative, theoretical, policy, and practitioner evidence
- preserve contradictions and explain likely reasons where possible
- include evidence gaps and limitations
- keep practical implications specific to the user’s context
- when the scan includes multiple research questions, synthesize within each question first, then look across questions for shared mechanisms, contradictions, evidence gaps, and practical implications
- do not introduce unsupported claims during synthesis

If verification finds major problems, such as more than 30% of material claims unconfirmed or corrected, recommend re-running research or narrowing the synthesis rather than presenting a weak evidence base as stable.

If the evidence base is thin, say so clearly. Suggest broadening scope, adding better seed sources, or re-running Deep Research with adjusted prompts rather than overstating weak findings.

## Preserve or reshape structure

If the corrected research reports are already well-organized by theme, preserve that structure and layer in cross-report synthesis.

If cross-cutting patterns justify a new structure, reshape into new themes. When reshaping, state what changed and why in the Evidence Report structure note.

Do not silently re-architect the evidence base.

## Use synthesis prompts internally

Read `references/prompt-templates.md` for cross-source synthesis queries when helpful. Use them internally to surface:

- convergence across reports
- contradictions and explanations
- strongest practical implications
- unresolved evidence gaps
- evidence quality by finding

Do not hand these prompts to the user unless they ask for NotebookLM / alternate digest guidance.

## Output-budget pre-flight

Phase 3 produces a substantial deliverable set: corrected source reports (one per report, up to 5), a Corrections Applied changelog, a finalized Citation Ledger, an Evidence Report, and an Executive Summary. For ≥3 reports, this combined output runs into single-context-overflow risk if corrections are applied by regenerating full corrected text for each report.

Before producing the final package, check the budget:

- **N source reports × full text regeneration + ~90 references × deliverable set** is the worst-case shape. For ≥3 reports it is uncomfortable; for ≥5 reports it is unlikely to fit in one main-thread context.
- **Targeted text-substitution + per-document Corrections appendix** (the default in `references/correction-workflow.md`) is materially cheaper. Inline pass touches only the matched anchors; appendix pass adds a small structured table at the end of each corrected report. This is the recommended path for ≥3 reports.
- **Whole-document regeneration** is the fallback, not the default. Use it only when the report is short, the corrections are dense enough that targeted substitution would touch most prose anyway, or anchor matching is unreliable (for example, OCR drift).
- **Hard rule**: no matter which path is used, every [P] and [X] flag for a given report must end up either inline in the corrected text OR in that report's Corrections appendix. A flag that lives only in the cross-document `Corrections Applied.md` changelog does not count as applied to the source report. The corrected-source-report is a self-contained contract.

If the projected output exceeds comfortable single-context budget even with targeted substitution, split Phase 3 across chats: produce corrected source reports + final ledger first, hand off to a fresh chat for the Evidence Report and Executive Summary using the same final ledger as input.

When `scripts/apply_corrections.py` is available, prefer it for Pass 1 and Pass 2 — it scales mechanically rather than consuming main-thread output tokens.

## Final output package

Read `references/output-formats.md` for the source-of-truth templates before producing final outputs.

Before producing final outputs, check `references/quality-rubric.md` for Phase 3 quality gates. If an `.xlsx` ledger is available, run `scripts/validate_ledger.py --stage final` before final synthesis and fix validation errors unless they are explicitly documented as unresolved.

Produce three primary outputs:

1. `[Topic] — Evidence Report.md`
2. `[Topic] — Citation Ledger (Final).xlsx`
3. `[Topic] — Executive Summary.md`

Also produce, when relevant:

- `[Topic] — Corrections Applied.md`
- `[Topic] — R1 (Corrected).md`, `[Topic] — R2 (Corrected).md`, ... up to `[Topic] — R5 (Corrected).md`, when relevant.

If the environment can create downloadable files, save these as files and present links. If file creation is unavailable, provide copyable Markdown outputs in clearly labeled sections and state the intended filenames.

## Optional NotebookLM handoff

If the user wants alternate digest formats, suggest uploading these materials to NotebookLM or an equivalent grounded synthesis tool:

- Evidence Report
- Executive Summary
- final Citation Ledger
- corrected Deep Research reports / source notes, up to 5 reports
- Corrections Applied changelog, if useful

Possible use cases:

- audio overviews
- mind maps
- follow-up synthesis questions, ideally run one at a time in NotebookLM or another grounded synthesis tool
- stakeholder-specific digests
- slide or briefing preparation

No further skill action is required unless the user asks for a specific adapted output.

## Finalize Phase 3

Use the same standard phase wrap-up style as earlier phases so the user understands what happened, can access final files, and knows optional next steps.

### Wrap-up style

Render the wrap-up in-chat with readable formatting. Use clear section headers, short bullets, and one instruction per line.

If Claude artifacts / preview tabs are available, create one artifact per major Markdown output:

- `evidence-report-[short-title].md`
- `executive-summary-[short-title].md`
- `corrections-applied-[short-title].md`, if relevant

If downloadable files are available, attach or link all final files clearly. If file generation is not available, output each final document in its own labeled copy block and state the intended filename.

### Required wrap-up structure

Always include:

```markdown
## Phase 3 complete: Synthesize Verified Evidence

### What we started with
[Verified ledger / verifier output / correction notes / corrected reports]

### What we did
- Normalized verified results into the Citation Ledger structure
- Applied corrections without overwriting originals
- Produced corrected source reports / notes where needed, up to 5 reports
- Ran Claude QA on corrected rows
- Synthesized verified evidence into final outputs

### What you now have
- Final Citation Ledger: [file or fallback]
- Evidence Report: [file or copy block]
- Executive Summary: [file or copy block]
- Corrections Applied changelog: [file or not needed]
- Corrected source reports / notes: [files, up to 5 reports, or not needed]

### Optional next steps
Upload the Evidence Report, Executive Summary, final Citation Ledger, and corrected source reports to NotebookLM or an equivalent grounded synthesis tool if you want audio overviews, mind maps, or follow-up synthesis queries.

Use the Executive Summary for stakeholders who need a concise briefing.

Use the Evidence Report and Citation Ledger for anyone who needs to inspect the evidence base.
```

### Handoff guidance

Explain what each final file is for, but keep it brief:

- Executive Summary: shareable briefing.
- Evidence Report: detailed evidence binder and NotebookLM-ready source.
- Citation Ledger: verification and audit trail.
- Corrections Applied changelog: transparent record of what changed.
- Corrected reports / notes: self-consistent source material for downstream synthesis.

The workflow is complete unless the user asks for an adapted output, such as slides, an email, a partner memo, a one-page brief, or NotebookLM query set.

