# Output Formats

Use this reference as the source of truth for standardized evidence-scan outputs.

## Contents

1. Approved Research Plan
2. Deep Research Prompt Block
3. Phase 1 Wrap-up
4. Artifact Inventory
5. Citation Ledger
6. Verification Packet
7. Phase 2 Wrap-up
8. Corrections Applied Changelog
9. Corrected Source Reports / Notes
10. Full Evidence Report
11. Executive Summary
12. Phase 3 Wrap-up

## Document 1: Approved Research Plan

Purpose: capture the scoped research direction before Deep Research prompts are generated.

When produced: Phase 1.

Template:

```markdown
## Proposed research plan

### Purpose and audience
[Who this is for and what decision / deliverable it supports]

### Research lens
[Effectiveness, design, landscape, implementation, mixed, or other]

### Research questions
1. [Question 1]
2. [Question 2, if needed]
3. [Question 3, if needed]
4. [Question 4, if needed for a thorough scan]
5. [Question 5, if needed for a thorough scan]

### Depth
[Light, Standard, or Thorough]

### Scope boundaries
- Date range:
- Geography:
- Population / setting:
- Benefits / intervention / program scope:
- Outcomes:
- Included evidence:
- Exclusions:

### Source targets
- Peer-reviewed academic evidence:
- Policy / government reports:
- Practitioner or program evaluations:
- Grey literature:

### Seed sources
- [Seed 1]
- [Seed 2]
- [Seed 3]

### Known risks or gaps
- [Risk, ambiguity, missing source type, or evidence limitation]
```

## Document 2: Deep Research Prompt Block

Purpose: copy-ready external research prompt generated from the approved research plan.

When produced: Phase 1.

Template: use `references/prompt-templates.md` as the source of truth. Phase 1 may include a compact prompt skeleton, but this file should preserve the final display structure.

Display rules:

- Provide one prompt per meaningfully distinct research question, up to 5 prompts for thorough scans.
- Place each prompt in its own artifact or fenced Markdown block.
- Repeat prompts at the bottom of the Phase 1 wrap-up so the user does not need to scroll back.

## Document 3: Phase 1 Wrap-up

Purpose: close Phase 1 and hand the user copy-ready research prompts.

Template:

```markdown
## Phase 1 complete: Scoping + Deep Research Prompt Generation

### What we started with
[User's topic area or initial request]

### What we did
- Scoped the research question(s)
- Clarified audience, purpose, depth, evidence preferences, and boundaries
- Confirmed or proposed seed sources
- Generated tailored Deep Research prompt(s)

### What you now have
- Approved research plan
- Domain-specific seed list
- Customized Deep Research prompt(s)

### Deep Research prompt files / copy blocks
[Provide one artifact or one fenced Markdown block per prompt]

### Next from you
Run each prompt in its own new Claude conversation with Research mode enabled, or in ChatGPT Deep Research or Gemini Deep Research.

Export each completed report as `.docx` or markdown, not PDF.

Use a separate chat for each Deep Research run. Do not continue chatting in the Deep Research chat after the report is generated; export or copy the report and move on.

When you have the reports, invoke this skill again in any chat with language like:

- "verify these Deep Research reports"
- "fact-check these research outputs"
- "build a citation ledger from these reports"
```

## Document 4: Artifact Inventory

Purpose: summarize research reports and source materials received at the start of Phase 2.

Template:

```markdown
## Phase 2 artifact inventory

### Research outputs received
- R1: [title / filename / source]
- R2: [title / filename / source]
- R3: [title / filename / source]
- R4: [title / filename / source, if applicable]
- R5: [title / filename / source, if applicable]

### Source materials received
- [source file, bibliography, reference list, or none]

### Synthesis goal
[What the user wants to do with the verified evidence, if known]

### Potential issues
- [missing source links, PDF extraction risk, incomplete report, unclear scope, etc.]
```

## Document 5: Citation Ledger

Purpose: structured workbook for claim extraction, verification, correction tracking, and final audit trail.

When produced:

- Initial ledger: Phase 2
- Finalized ledger: Phase 3

Preferred filename patterns:

```text
[Topic] — Citation Ledger.xlsx
[Topic] — Citation Ledger (Final).xlsx
```

Preferred format: `.xlsx` with five tabs. `.xlsx` is the primary format for verification and archival use. Use `scripts/create_ledger.py` to generate the initial workbook when possible.

If `.xlsx` cannot be created, provide a Markdown fallback and tell the user it should be converted to `.xlsx` before verification or archiving. Markdown is only a fallback when file generation is unavailable.

### Tab structure

| Tab | Purpose |
|---|---|
| README | Scope, date, verification tool, codes legend, links to tabs, and Coverage QA summary |
| Claims | One row per extracted material claim, unified across reports |
| References | Full reference list from each report bibliography |
| Cross-Report Inconsistencies | Numeric, entity, framing, or internal conflicts across reports / sources |
| Corrections Applied | Populated in Phase 3 when corrections are applied |

### README tab contents

Include:

- Topic
- Date
- Verification tool planned or used
- Verification codes legend
- Links / references to other tabs
- Coverage QA summary

Coverage QA summary columns:

| Column | Description |
|---|---|
| Report | R1 / R2 / R3 / R4 / R5 |
| Section | Section heading |
| Pages | Page range, if available |
| Claims extracted | Count |
| Stakes breakdown | #H / #M / #L |

### Claims tab columns

| Column | Description |
|---|---|
| Report | R1 / R2 / R3 / R4 / R5 |
| Claim ID | Example: R1-C01 |
| Section | Report section / heading where the claim appears |
| Claim | The factual / statistical / recommendation claim, verbatim or lightly paraphrased |
| Source Cited | Short cite, such as Author, Year |
| Full Citation | Full citation so the verifier can find the source |
| Evidence Type | RCT / meta-analysis / quasi-experimental / observational / qualitative / policy report / practitioner report / synthesis / uncited |
| Stakes | H / M / L |
| Verified | Blank initially; later filled with [C] / [P] / [U] / [X] |
| Verification Notes | Blank initially; filled for non-[C] rows |
| Correction | Blank initially; filled for [P] and [X] rows |
| Claude QA | Blank initially; filled after corrections are applied |

### References tab columns

| Column | Description |
|---|---|
| Report | R1 / R2 / R3 / R4 / R5 |
| Reference ID | Example: R1-REF01 |
| Full Citation | Full citation from report bibliography |
| Referenced in claims | Claim IDs that cite this reference |

### Cross-Report Inconsistencies tab columns

Use long format: one row per inconsistency-report pairing.

| Column | Description |
|---|---|
| Inconsistency ID | X01, X02, etc. Repeats across rows of the same inconsistency |
| Source scope | cross-report / within-source |
| Report | R1 / R2 / R3 / R4 / R5 |
| Claim text | The claim or value as stated in this row’s report |
| Affected Claim IDs | The claim IDs contributing to this row |
| Type | Numeric conflict / entity disambiguation / framing disagreement / internal numeric variance |
| Resolution | Blank initially; filled after verification when possible |

### Corrections Applied tab columns

| Column | Description |
|---|---|
| Claim ID | R1-C## |
| Verified code | [P] / [X] |
| Original text | Claim as originally extracted |
| Corrected text | Corrected version |
| Reason | Why the correction was needed |
| Claude QA | ✓ or ✗ with note |

### Stakes key

| Code | Meaning |
|---|---|
| H | Drives a recommendation or would change advice if wrong |
| M | Supports an argument but is not the sole basis for advice |
| L | Contextual, descriptive, or well-established |

### Verification codes

| Code | Meaning |
|---|---|
| [C] Confirmed | Source exists and supports the claim as stated |
| [P] Partially confirmed | Source exists but characterization is slightly off; Correction explains |
| [U] Unconfirmed | Source or claim cannot be verified |
| [X] Corrected | Claim is inaccurate; correction belongs in Correction column |

## Document 6: Verification Packet

Purpose: help the user run external verification.

When produced: Phase 2.

Contents:

- Citation Ledger file or fallback table
- Verification prompt
- “Pay particular attention” block
- Handoff instructions
- Follow-up language if the verifier returns narrative instead of an updated workbook

Use `references/prompt-templates.md` for the source-of-truth verification prompt.

Verification output requirements:

- The primary output is an updated Citation Ledger `.xlsx`.
- Narrative-only verification is incomplete unless the verifier cannot produce files.
- The updated `.xlsx` should include Verified filled for every row, Verification Notes filled for every non-[C] row, and Correction filled for every [P] and [X] row.
- If the verifier runs out of capacity, a partial `.xlsx` with completed rows and a note listing unverified row ranges is preferable to narrative-only verification.

## Document 7: Phase 2 Wrap-up

Purpose: close Phase 2 and hand the user the verification-ready materials.

Template:

```markdown
## Phase 2 complete: Claim Extraction + Verification Prep

### What we started with
[Completed Deep Research reports / cited drafts / source materials]

### What we did
- Inventoried the research outputs
- Checked extraction quality
- Extracted material claims
- Built the initial Citation Ledger
- Flagged cross-report inconsistencies and extraction issues
- Generated verification prompt(s) / instructions

### What you now have
- Initial Citation Ledger: [file, artifact, or table]
- Verification prompt / instructions
- Rows requiring special attention: [summary]

### Verification prompt files / copy blocks
[Provide one artifact or one fenced Markdown block with the final verification prompt]

### Next from you
Use the verification prompt with Perplexity or another source-checking workflow. For academic sources, use Perplexity Deep Research with the Academic connector enabled when available.

Upload the Citation Ledger and request an updated `.xlsx` ledger with Verified, Verification Notes, and Correction filled in.

If the tool only returns narrative, reply:

"Please also produce the updated Citation Ledger `.xlsx` with Verified, Verification Notes, and Correction filled for every non-[C] row. A narrative-only response is incomplete unless you cannot produce files."

When you have the verified ledger, verification notes, or corrected table, return in any chat with language like:

- "apply these verification corrections"
- "synthesize this verified research"
- "use this verified citation ledger to create the evidence report"
```

## Document 8: Corrections Applied Changelog

Purpose: transparent record of corrections made before final synthesis.

When produced: Phase 3, when corrections exist.

Filename:

```text
[Topic] — Corrections Applied.md
```

Template:

```markdown
# Corrections Applied: [Topic]

| Claim ID | Verified code | Original text | Corrected text | Reason |
|---|---|---|---|---|
| [R1-C01] | [P] | [original] | [correction] | [verification note] |
```

## Document 9: Corrected Source Reports / Notes

Purpose: corrected source material for final synthesis and optional NotebookLM upload. Usually produce up to 5 corrected research reports, matching the Phase 1 prompt limit.

When produced: Phase 3, when original report text is available and corrections are needed.

Filename pattern:

```text
[Topic] — R1 (Corrected).md
[Topic] — R2 (Corrected).md
[Topic] — R3 (Corrected).md
[Topic] — R4 (Corrected).md
[Topic] — R5 (Corrected).md
```

Rules:

- Preserve [C] claims verbatim.
- Replace [P] and [X] claims with corrected wording.
- Preserve [U] claims only when needed, visibly flagged as unverified.
- Do not overwrite original reports.
- If there are more than 5 reports, batch them or ask which 5 are highest priority before creating corrected versions.

## Document 10: Full Evidence Report

Purpose: comprehensive, intentionally overinclusive research output optimized for grounded synthesis and optional NotebookLM upload. This is the evidence binder.

When produced: Phase 3.

Filename:

```text
[Topic] — Evidence Report.md
```

Template:

```markdown
# Evidence Report: [Research Question]

**Prepared:** [Date]
**Scope:** [Brief scope description]
**Tools used:** [Claude Research / ChatGPT Deep Research / Gemini Deep Research / verification tools]
**Citation seeds used:** [List seed papers, or "None"]
**Structure note:** [If preserved: "Structure preserved from corrected research reports." If reshaped: "Reshaped into N themes to surface cross-cutting patterns; original structure noted per section."]

---

## Executive Overview

[3–5 sentence summary of what the evidence says overall]

---

## Theme 1: [Theme Name]

### Summary

[2–3 sentence overview of what the evidence shows for this theme]

### Key Findings

**Finding 1.1: [Concise finding statement]**

- **Evidence strength:** [High | Moderate | Low | Very Low] (GRADE; flag adjacent-domain extrapolation or `[mixed evidence]` as needed)
- **Source(s):** [Inline citation(s)]
- **Detail:** [Methodology, sample size, effect size, context, population, setting]
- **Direct quote:** "[Relevant quote from source if available]"
- **Limitations:** [Boundary conditions, caveats, generalizability]
- **Practical implication:** [What this means for the user's context]

**Finding 1.2: [Next finding]**

[Same structure]

### Theme Summary

[What the evidence collectively says about this theme. Note contradictions explicitly.]

---

## Theme 2: [Theme Name]

[Same structure as Theme 1]

---

## Evidence Gaps

- [Gap 1: what remains unknown and why it matters]
- [Gap 2]

## Methodological Notes

- [Patterns in study quality, common limitations, biases across the literature]

## Complete Reference List

[Full citations for every source referenced, alphabetized]
```

Rules:

- Organize by theme, not by source.
- Include more detail than seems necessary for a normal memo; this report doubles as an evidence binder.
- Cite every factual claim.
- Flag any inference with `[INFERENCE]`.
- Do not smooth over contradictions.
- Include direct quotes where available.
- If the corrected reports were already themed and that structure is preserved, say so in the Structure note.
- If the report was reshaped into new themes, explain why.

## Document 11: Executive Summary

Purpose: human-readable briefing for sharing with colleagues, leadership, funders, partners, or project teams. Keep it concise, scannable, and action-oriented.

When produced: Phase 3.

Filename:

```text
[Topic] — Executive Summary.md
```

Template:

```markdown
# [Research Question]: Evidence Summary

**Prepared for:** [Audience]
**Date:** [Date]
**Methodology:** AI-assisted evidence scan using [tools]. Claims verified via [verification method]. Full Evidence Report and Citation Ledger available on request.

---

## Key Findings

**1. [Finding headline]** *(Evidence: [High | Moderate | Low | Very Low])*  
[2–3 sentence summary with inline citation]

**2. [Finding headline]** *(Evidence: [High | Moderate | Low | Very Low])*  
[2–3 sentence summary with inline citation]

**3. [Finding headline]** *(Evidence: [High | Moderate | Low | Very Low])*  
[2–3 sentence summary with inline citation]

[Up to 5 key findings]

---

## Evidence Landscape

### [Theme 1]

[1 paragraph summarizing what the evidence says]

### [Theme 2]

[1 paragraph]

---

## Gaps & Limitations

[What the evidence does not answer well. What would need further investigation.]

---

## Practical Implications

[What this means for the user's specific project, decision, or context. Actionable takeaways.]

---

## Methodology Note

This evidence scan extracted [N] claims from [N] research reports, verified via [Perplexity / independent Claude chat / other method], applied corrections surgically, and synthesized into the full Evidence Report. [X] cross-report inconsistencies resolved; [Y] claims corrected.
```

Rules:

- Keep to 2–4 pages.
- Lead with findings, not methodology.
- Include evidence strength rating on every key finding.
- Write for someone who has 10 minutes, not 2 hours.
- End with “so what”: practical implications should be specific and actionable, not generic.
- Preserve nuance without turning the summary into the full evidence binder.

## Document 12: Phase 3 Wrap-up

Purpose: close the workflow and orient the user to final outputs.

Template:

```markdown
## Phase 3 complete: Synthesize Verified Evidence

### What we started with
[Verified ledger / verifier output / correction notes / corrected reports]

### What we did
- Normalized verified results into the Citation Ledger structure
- Applied corrections without overwriting originals
- Produced corrected source reports / notes where needed
- Ran Claude QA on corrected rows
- Synthesized verified evidence into final outputs

### What you now have
- Final Citation Ledger: [file or fallback]
- Evidence Report: [file or copy block]
- Executive Summary: [file or copy block]
- Corrections Applied changelog: [file or not needed]
- Corrected source reports / notes: [files, up to 5 reports, or not needed]

### Optional next steps
Upload the Evidence Report, Executive Summary, final Citation Ledger, and corrected source reports to NotebookLM or an equivalent grounded synthesis tool if you want audio overviews, mind maps, or follow-up synthesis queries. Run follow-up synthesis queries one at a time rather than all at once.

Use the Executive Summary for stakeholders who need a concise briefing.

Use the Evidence Report and Citation Ledger for anyone who needs to inspect the evidence base.
```

