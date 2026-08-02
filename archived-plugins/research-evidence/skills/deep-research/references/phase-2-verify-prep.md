# Phase 2: Claim Extraction + Verification Prep

Use this reference when the user returns with completed Deep Research reports, research outputs, cited drafts, source-backed drafts, or source materials that need to be checked before synthesis.

## Phase 2 navigation

| Step           | What happens                                                                         | Output                            |
| -------------- | ------------------------------------------------------------------------------------ | --------------------------------- |
| 1. Intake      | Identify reports, source files, cited drafts, and the user’s synthesis goal          | Artifact inventory                |
| 2. Extract     | Pull material claims, citations, methods, populations, outcomes, and numeric details | Claim list                        |
| 3. Ledger      | Convert extracted claims into a structured Citation Ledger                           | Initial Citation Ledger           |
| 4. QA          | Check extraction quality and cross-report inconsistencies                            | Coverage QA + inconsistency flags |
| 5. Verify prep | Generate verification prompt(s) and instructions for external source checking        | Verification packet               |
| 6. Handoff     | Tell the user how to verify externally and return                                    | Phase 2 wrap-up                   |

Use these steps sequentially, but do not force unnecessary interaction. If the user already provides enough context for a step, summarize it and move forward.

## Goal

Turn completed research outputs into a verification-ready package:

- extracted material claims
- source links and citation details
- initial Citation Ledger
- cross-report inconsistency flags
- verification prompt(s) / instructions for external fact-checking
- clear next-step handoff for the user

Phase 2 ends when the user has the Citation Ledger and verification materials they need to run the verification step outside this chat.

Phase 2 does **not** apply corrections or synthesize final findings. Corrections and final synthesis happen after the user returns with verified results.

## Inputs

Start from whatever the user provides:

- completed Deep Research reports
- ChatGPT / Claude / Gemini research outputs
- source-backed drafts
- exported `.docx`, markdown, or pasted report text
- source files, PDFs, bibliographies, or reference lists
- prior research notes or partially completed ledgers

Prefer `.docx` or markdown. If a report came from a Gemini / Google Docs PDF export and numeric values appear missing or malformed, ask the user to re-export as `.docx` or markdown. PDF exports can break extraction of percentages, effect sizes, dollar figures, sample sizes, or other numeric values.

Never overwrite the user’s original reports or ledgers. Create new files or new copy blocks alongside the originals.

## Intake

Begin by inventorying the available artifacts.

Use this structure:

```markdown
## Phase 2 artifact inventory

### Research outputs received
- R1: [title / filename / source]
- R2: [title / filename / source]
- R3: [title / filename / source]
- R4: [title / filename / source]
- R5: [title / filename / source]

### Source materials received
- [source file, bibliography, reference list, or none]

### Synthesis goal
[What the user wants to do with the verified evidence, if known]

### Potential issues
- [missing source links, PDF extraction risk, incomplete report, unclear scope, etc.]
```

If the reports are unusable, incomplete, or missing core text, ask for the specific missing artifact. Do not restart Phase 1 unless the purpose or scope is unclear enough that claim extraction cannot be done responsibly.

## Extraction sanity check

Before building the ledger, sample 3–5 claims from the reports and check extraction quality.

Watch for failure signs:

- phrases like “increased by percentage points” with no number
- “effects of dollars” with no dollar amount
- blank effect sizes, percentages, dates, or sample sizes
- broken citation text
- repeated OCR artifacts
- tables that lost column labels

If extraction appears broken, ask the user to re-export as `.docx` or markdown. If they cannot, explain that OCR or manual cleanup may be needed before reliable claim extraction.

## Extraction capacity

Real Deep Research reports often exceed comfortable subagent or single-context budgets. Plan for capacity before starting extraction.

**Subagent failure mode is common, not rare.** The recommended Phase 2 architecture spawns one `agents/claim-extractor.md` subagent per report. On real DR-length inputs, these spawns commonly return `Prompt is too long` because the source report alone consumes most of the subagent context budget. The failure is about report length, not the spawn prompt — retrying with a tighter spawn prompt does not help. When this happens, switch to chunked inline extraction (see below); do not silently downgrade to a single inline pass over the whole report, which compounds the same capacity problem in the main thread.

**Chunked inline extraction is the documented fallback.** Run `agents/claim-extractor.md` inline against one report at a time, segmented by the report's own native sections. The agent file's `<chunked_extraction>` block specifies the procedure: 4–8 sections per report, write per-section JSON to disk between sections, use a stable `Claim ID` counter across sections, merge once all sections are done. This keeps working context bounded by section size rather than report size.

**Cost guidance for ≥4 reports.** The inline fallback's main-thread cost scales with N × report-length × full ledger output. For a "thorough" 5-report scan, a single context will not hold both the per-report extraction work and the Phase 3 deliverable set. For ≥4 substantial reports:

- plan on the chunked path from the start (do not attempt subagents-then-fall-back at this scale)
- write per-section and per-report JSON to disk between steps
- treat the merger as a separate main-thread step that ingests the on-disk JSON, not the in-context claim text
- consider splitting Phase 2 and Phase 3 across separate chats (Phase 2 ends with the verification packet; Phase 3 begins fresh after verification returns)

**Do not skip reports to fit capacity.** If the user provided N reports, all N need ledger rows. If chunking + on-disk handoff still cannot fit, ask the user to reduce N or pre-narrow the scope rather than silently dropping reports from extraction.

## Extract material claims

Extract material claims from every report. A material claim is any factual, statistical, methodological, causal, comparative, or recommendation claim that could affect the synthesis, interpretation, or practical advice.

Include:

- factual claims
- statistical claims
- claims about intervention effectiveness
- claims about mechanisms or behavioral explanations
- claims about populations, settings, outcomes, or methods
- recommendation claims
- uncited framing claims that shape interpretation
- summary-table restatements when they add or alter meaning

Do not extract every tiny factual phrase by default. Exhaustive extraction is only needed when the user asks for it, the deliverable is high-stakes, or the reports are short enough that exhaustive extraction is tractable.

Bias toward over-inclusion when unsure. “Material claim” should be interpreted broadly: include claims that shape interpretation, recommendations, evidence strength, or practical implications. Under-extraction is the bigger risk; stakes are for triage, not filtering.

Watch especially for subtle verification risks:

- misattributed findings
- composite statistics
- generous or overstated framing
- claims that cite one source but rely on several
- claims that generalize beyond the cited population, geography, setting, or method

Assign stakes for triage, not filtering:

- **H** — drives a recommendation or would change advice if wrong
- **M** — supports an argument but is not the sole basis for advice
- **L** — contextual, descriptive, or well-established

## Reports with weak or missing citations

If reports have no citations or weak citations, flag that verification will be limited. Extract material claims anyway and mark missing citations clearly; many of these rows may become [U] during verification.

Do not skip the report solely because citations are weak. The ledger should make the limitation visible.

### Missing or partial bibliographies

It is acceptable for the References tab to be empty when the source reports use only inline citations and provide no separate bibliography or reference list. Do not invent bibliography rows. Document the absence in the README tab Notes (for example: "Reports use inline citations only; References tab intentionally empty"). The Claims tab is the source of truth in this case.

When at least some references are recoverable from inline citations, populate the References tab with what can be reconstructed and leave the rest blank rather than fabricating full citations. Mark partial citations with `MISSING_FROM_REPORT` to signal to the verifier that the gap is on the source-report side, not an extraction failure.

## Citation Ledger format

Create an initial Citation Ledger. The `.xlsx` Citation Ledger is the preferred and primary ledger format for verification and archival use. Markdown is only a fallback when file generation is unavailable.

Prefer `.xlsx` when the environment can create downloadable spreadsheets reliably. If `.xlsx` is unavailable, produce a Markdown table with the same columns and tell the user it should be converted to `.xlsx` before external verification.

Recommended file name:

```text
[Topic] — Citation Ledger.xlsx
```

The ledger has five tabs.

| Tab                          | Purpose                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| README                       | Scope, date, verification tool, codes legend, links to tabs, and Coverage QA summary |
| Claims                       | One row per extracted material claim, unified across reports                         |
| References                   | Full reference list from each report bibliography                                    |
| Cross-Report Inconsistencies | Numeric, entity, framing, or internal conflicts across reports / sources             |
| Corrections Applied          | Empty in initial Phase 2 ledger; populated after verification / correction           |

### README tab

Include:

- Topic
- Date
- Verification tool planned or recommended
- Verification codes legend
- Links / references to other tabs
- Coverage QA summary

Coverage QA summary columns:

| Column           | Description              |
| ---------------- | ------------------------ |
| Report           | R1 / R2 / R3             |
| Section          | Section heading          |
| Pages            | Page range, if available |
| Claims extracted | Count                    |
| Stakes breakdown | #H / #M / #L             |

### Claims tab columns

| Column             | Description                                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Report             | R1 / R2 / R3 / R4 / R5                                                                                                             |
| Claim ID           | Example: R1-C01                                                                                                                    |
| Section            | Report section / heading where the claim appears                                                                                   |
| Claim              | The factual / statistical / recommendation claim, verbatim or lightly paraphrased                                                  |
| Source Cited       | Short cite, such as Author, Year                                                                                                   |
| Full Citation      | Full citation so the verifier can find the source                                                                                  |
| Evidence Type      | RCT / meta-analysis / quasi-experimental / observational / qualitative / policy report / practitioner report / synthesis / uncited |
| Stakes             | H / M / L                                                                                                                          |
| Verified           | Empty initially; later filled with [C] / [P] / [U] / [X]                                                                           |
| Verification Notes | Empty initially; filled for non-[C] rows                                                                                           |
| Correction         | Empty initially; filled for [P] and [X] rows                                                                                       |
| Claude QA          | Empty initially; filled after corrections are applied                                                                              |

### References tab columns

| Column               | Description                            |
| -------------------- | -------------------------------------- |
| Report               | R1 / R2 / R3 / R4 / R5                 |
| Reference ID         | Example: R1-REF01                      |
| Full Citation        | Full citation from report bibliography |
| Referenced in claims | Claim IDs that cite this reference     |

### Cross-Report Inconsistencies tab columns

Use long format: one row per inconsistency-report pairing.

| Column             | Description                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Inconsistency ID   | X01, X02, etc. Repeats across rows of the same inconsistency                                |
| Source scope       | cross-report / within-source                                                                |
| Report             | R1 / R2 / R3 / R4 / R5                                                                      |
| Claim text         | The claim or value as stated in this row’s report                                           |
| Affected Claim IDs | The claim IDs contributing to this row                                                      |
| Type               | Numeric conflict / entity disambiguation / framing disagreement / internal numeric variance |
| Resolution         | Empty initially; filled after verification                                                  |

For cross-report conflicts, use one row per report contributing a distinct value. If a report is silent on the datum, do not create a row unless that silence itself matters; note it in Type when helpful.

For within-source ambiguity, use one row when a single claim contains multiple conflicting values, or one row per disagreeing claim when multiple claims in the same report conflict.

### Corrections Applied tab columns

Leave this tab empty in the initial Phase 2 ledger except for headers.

| Column         | Description                         |
| -------------- | ----------------------------------- |
| Claim ID       | R1-C##                              |
| Verified code  | [P] / [X]                           |
| Original text  | Claim as originally extracted       |
| Corrected text | Corrected version                   |
| Reason         | Why the correction was needed       |
| Claude QA      | Empty until corrections are applied |

## Verification codes

External verification should fill these codes:

| Code                    | Meaning                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------- |
| [C] Confirmed           | Source exists and supports the claim as stated                                     |
| [P] Partially confirmed | Source exists but the characterization is slightly off; Correction column explains |
| [U] Unconfirmed         | Source or claim cannot be verified                                                 |
| [X] Corrected           | Claim is inaccurate; correction belongs in Correction column                       |

## Helper scripts

Use `scripts/create_ledger.py` to create the standardized `.xlsx` Citation Ledger when the environment supports running Python and writing downloadable files.

`create_ledger.py` is the executable source of truth for workbook creation. Do not inline or rewrite the script inside this reference file.

### `scripts/create_ledger.py`

Purpose: create a standardized `.xlsx` Citation Ledger from structured claim and reference data.

Inputs:

- `claims.json` — extracted claims
- `references.json` — extracted references
- optional `inconsistencies.json` — detected cross-report or within-source inconsistencies
- `--topic` — evidence scan topic for the README tab
- `--verification-tool` — planned verification tool, defaulting to Perplexity or equivalent source-checking workflow
- `--notes` — optional README notes
- `--output` — output `.xlsx` path

Expected behavior:

- create five tabs: README, Claims, References, Cross-Report Inconsistencies, Corrections Applied
- write required headers exactly as specified in this file
- add README metadata and Coverage QA summary
- freeze header rows
- set readable column widths
- apply basic readability formatting
- leave `Verified`, `Verification Notes`, `Correction`, and `Claude QA` empty in the initial ledger
- validate that every claim has `Report`, `Claim ID`, `Claim`, `Stakes`, and `Evidence Type`
- validate unique Claim IDs
- validate stakes values as H / M / L
- fail with a clear error if required fields are missing or invalid

Example command:

```bash
python scripts/create_ledger.py \
  --topic "Benefits chatbot evidence scan" \
  --claims claims.json \
  --references references.json \
  --inconsistencies inconsistencies.json \
  --output "Benefits chatbot evidence scan — Citation Ledger.xlsx"
```

If the script cannot be run, produce the same ledger structure as a Markdown table or copy block and tell the user it should be converted to `.xlsx` before external verification.

### `scripts/validate_ledger.py`

Use `scripts/validate_ledger.py` when a Citation Ledger is created, returned from verification, or finalized. Run it with the validation stage that matches the workflow point: `initial`, `verified`, or `final`.

Purpose: check a Citation Ledger before handoff or synthesis.

Expected checks:

- required tabs exist
- required columns exist in each tab
- Claim IDs are unique
- every claim has Report, Claim ID, Claim, Evidence Type, and Stakes
- Stakes values are only H / M / L
- `initial` stage: verification fields should remain blank
- `verified` stage: Verified values should be [C] / [P] / [U] / [X], and [P] / [X] rows should have Correction text
- `final` stage: corrected rows should have Correction, Corrections Applied rows, and Claude QA

Example commands:

```bash
python scripts/validate_ledger.py "Benefits chatbot evidence scan — Citation Ledger.xlsx" --stage initial
python scripts/validate_ledger.py "Benefits chatbot evidence scan — Citation Ledger.xlsx" --stage verified
python scripts/validate_ledger.py "Benefits chatbot evidence scan — Citation Ledger (Final).xlsx" --stage final
```

## Cross-report inconsistency check

Before finalizing the ledger, compare numeric, entity, and recommendation claims across reports. The data is already in the ledger after extraction — this step is mechanical filtering plus targeted close-reading on the rows the filter surfaces, not full re-reading of every report.

### Conflict-pattern checklist

Run through this checklist against the extracted ledger. Each pattern points at a specific cell-comparison shape that is mechanically detectable from the Claims tab.

| Pattern | What to check | Detection shape |
|---|---|---|
| Same-source-different-magnitude | Two reports cite the same source but quote different numeric values (effect sizes, percentages, sample sizes, dollar amounts) | Group by `Source Cited`; flag groups where rows from ≥2 reports contain divergent numeric tokens in `Claim` |
| Same-source-different-time-point | Two reports cite the same source but quote different follow-up periods, study endpoints, or measurement years | Group by `Source Cited`; flag groups where rows from ≥2 reports differ on date / time-period tokens in `Claim` or `evidence_detail` |
| Same-source-different-claim-domain | Two reports cite the same source for substantively different claims (one for an effect on outcome A, the other for an effect on outcome B) | Group by `Source Cited`; flag groups where rows from ≥2 reports differ on `claim_type` or where the `Claim` text addresses different outcomes |
| Cross-report citation re-use | Same source / same authors / same year cited by ≥2 reports for distinct claims, even if not numerically conflicting | Group by `Source Cited`; flag any group with rows from ≥2 reports for verifier confirmation that the source supports all uses (mirrors the `Type` enumeration in `references/output-formats.md`) |
| Direction-of-effect inversion | Two reports report effects in opposite directions for the same intervention or population, regardless of source overlap | Group by intervention or population key tokens in `Claim`; flag pairs where `Claim` contains opposite-sign effect language ("increased / decreased", "improved / worsened") |
| Composite-vs-primary divergence | One report treats a primary RCT as the source; another treats a meta-analysis or synthesis citing that RCT as the source. The "same effect" may carry different magnitudes through aggregation | Cross-check `Evidence Type` for rows about the same intervention; flag mismatches where one report's row is `RCT` and another's is `meta-analysis` / `synthesis` |
| Adjacent-domain leak | One report treats adjacent evidence as direct; another distinguishes it explicitly | Look for rows where one report's `Claim` generalizes a population / setting that another report's `Claim` keeps narrowly scoped |
| Internal numeric variance | A single report internally cites different values for the same datum (e.g., 82% / 84% / 85% in different sections of the same report) | Within-report grouping on `Source Cited` + numeric-token divergence across the same report's rows |

### Mechanical filter recipe

If the ledger is in `.xlsx` form, the conflict-pattern checks above can be mechanized on the Claims tab:

1. Group the Claims tab by `Source Cited`.
2. For groups with rows from ≥2 reports, scan for: divergent numeric tokens in `Claim`, divergent dates / time periods in `Claim` or `evidence_detail`, divergent `claim_type` values, divergent `Evidence Type` values, opposite-direction effect language.
3. For each divergence, add one row per contributing report to the Cross-Report Inconsistencies tab using the long-format schema (`Inconsistency ID` repeats; one row per `Inconsistency × Report`; `Source scope` = `cross-report`).
4. For within-source numeric variance, add one row per disagreeing claim with `Source scope` = `within-source` and the same `Inconsistency ID`.

If `scripts/find_cross_report_inconsistencies.py` is available in the bundle, it automates steps 1–2 against the `.xlsx` ledger and emits a candidate list for the human or verifier to triage. Treat its output as suggestions, not final classifications — the script is a filter, not a judgment. If the script is not present, the steps above are tractable to perform by hand on the Claims tab using sort-by-Source-Cited plus row-level scanning for the divergence shapes listed.

### Resolution policy

Add candidate conflicts to the Cross-Report Inconsistencies tab with `Resolution` left blank. Do not try to resolve them in Phase 2 unless the resolution is obvious from the reports themselves. The verifier resolves source-disagreement conflicts during Phase 2 verification; cross-report citation re-use confirmations and adjacent-domain framing calls usually resolve in Phase 3 synthesis.

## Verification handoff

Ask the user how they want to verify the claims.

Use `structured-question interface`:

```markdown
How would you like to verify these claims?

A. Perplexity or equivalent source-checking tool — recommended for web-native search, academic connectors, and source-existence verification. For academic sources, use Deep Research mode with the Academic connector enabled when available.
B. A fresh Claude chat with no memory of this one — backup option, less reliable for source-existence checks.
```

Before delivering the verification prompt, scan the ledger and identify rows that need special attention:

- cross-report inconsistencies
- weak primary sources, such as preprints, theses, uncited synthesis, or low-quality grey literature
- suspiciously clean or round numbers
- composite claims that combine multiple sources or outcomes
- uncited claims that nevertheless shape interpretation

Put a “pay particular attention” block at the very top of the verification prompt so it cannot be missed.

For Perplexity: recommend Deep Research mode with the Academic connector enabled when checking academic sources. Explain that Perplexity is recommended because it is web-native, independent of this chat’s context, and better suited for source-existence checks.

## Verification prompt skeleton

Read `references/prompt-templates.md` before generating the final verification prompt. Use the template there as the source of truth when available. The skeleton below mirrors that template — keep both copies in sync. Before delivery, scan the actual ledger and populate the `<focus_areas>` block with specific high-suspicion rows (cross-report inconsistencies, weak primary sources, suspiciously round numbers, possible composites, uncited load-bearing claims, citation-claim domain mismatches, etc.).

```markdown
<context>
You are an elite Evidence Verification Agent. Your objective is to audit an Evidence Scan Citation Ledger by checking whether every factual claim is supported by its cited source and the relevant literature.
</context>

<focus_areas>
Pay particular attention to these rows:
- [Claim ID]: [cross-report inconsistency, weak source, suspicious number, composite claim, uncited load-bearing claim, or citation-claim domain mismatch]
- [Claim ID]: [reason]
- [Claim ID]: [reason]
</focus_areas>

<inputs>
- Uploaded Citation Ledger: [filename]
- Source reports: [R1, R2, R3, R4, R5, if available]
- Topic / scope: [brief scope]
</inputs>

<task>
For every claim row, fill:
- Verified: [C], [P], [U], or [X]
- Verification Notes: explain what you checked and why the code applies
- Correction: required for [P] and [X] rows

Preserve Claim IDs exactly. Do not collapse multiple claim rows into one narrative answer.
</task>

<verification_codes>
- [C] Confirmed — source exists and supports the claim as stated.
- [P] Partially confirmed — source exists but characterization is slightly off (e.g., overgeneralization, minor stat error). Provide corrected wording.
- [U] Unconfirmed — cannot verify source or claim based on the provided texts.
- [X] Corrected — claim is highly inaccurate or relies on a broken or hallucinated source. Provide corrected wording.
</verification_codes>

<verification_rules>
1. Verify the cited source actually exists in the provided context.
2. Check whether the cited source supports the claim as written.
3. Check whether the claim overgeneralizes beyond the source population, geography, setting, or method (e.g., calling a single RCT a "meta-analysis").
4. Verify that statistics, dates, sample sizes, and effect sizes match the source exactly.
5. For composite claims, check whether they improperly blend multiple sources without support from the primary cited source.
</verification_rules>

<edge_case_handling>
- **Cross-report inconsistencies:** If a row compares conflicting claims between two or more reports (and lacks a primary citation), do not automatically default to [U]. Attempt to synthesize the truth using your search tool or internal knowledge base. If unresolvable, mark [U] and detail the specific contradiction in the Verification Notes.
- **Author synthesis / no citation:** If a claim is explicitly marked "Author synthesis, no citation" or carries no source attribution, default to [U]. The skill treats uncited load-bearing claims as flags. Do not elevate to [C] on the basis of surrounding prose alone — only elevate to [C] if you can find an external source that directly supports the claim.
</edge_case_handling>

<output_format>
The primary output is the updated Citation Ledger `.xlsx` with all columns filled. A narrative-only response is incomplete unless you cannot produce files.

The updated `.xlsx` must include:
- Verified filled for every row
- Verification Notes filled for every non-[C] row
- Correction filled for every [P] and [X] row

If you run out of tool calls or capacity before finishing, return the partial `.xlsx` with completed rows, followed by a bolded note: **UNREVIEWED ROWS: [Start ID] to [End ID]**. Do not substitute a narrative for the workbook.

**Fallback protocol** (only if you cannot natively produce or modify the `.xlsx` file):

1. **Confirmed Claims Log** — a comma-separated list of all Claim IDs you reviewed and verified as [C]. Example: `Confirmed: R1-C02, R1-C04, R2-C07`.
2. **Exception Table** — a markdown table containing ONLY the non-[C] rows, with these exact headers:

   | Claim ID | Verified | Verification Notes | Correction |

If you run out of capacity before finishing the fallback output, return the table for completed rows followed by **UNREVIEWED ROWS: [Start ID] to [End ID]**.
</output_format>
```

Warn the user that some external tools may return narrative instead of the updated workbook. If that happens, they should reply:

```text
Please also produce the updated Citation Ledger `.xlsx` with Verified, Verification Notes, and Correction filled for every non-[C] row. A narrative-only response is incomplete unless you cannot produce files.
```

## Phase 2 outputs

Before handing off Phase 2, check `references/quality-rubric.md` for Phase 2 quality gates.

Produce:

- Citation Ledger `.xlsx`, if possible
- fallback Markdown ledger table, if `.xlsx` is not possible
- verification prompt / instructions
- notes on rows requiring special attention
- phase wrap-up with next steps

If a downloadable `.xlsx` file is created, also provide a short in-chat summary of:

- number of reports processed
- number of claims extracted
- stakes breakdown
- number of cross-report inconsistencies flagged
- any extraction or source-quality warnings

## Finalize Phase 2

Use a standard phase wrap-up so the user understands what happened, can access the next-step materials, and knows exactly how to re-enter the skill later.

### Wrap-up style

Render the wrap-up in-chat with readable formatting. Use clear section headers, short bullets, and one instruction per line. Do not bury the verification prompt above the fold; repeat it at the bottom so the user can copy it without scrolling back through the conversation.

If Claude artifacts / preview tabs are available, create one Markdown artifact for the verification prompt with a clear title, such as:

- `verification-prompt-[short-title].md`

If a downloadable Citation Ledger can be produced, attach or link it clearly. If downloadable files are not available, output the ledger as a Markdown table or copy block and clearly tell the user it should be converted to `.xlsx` before verification.

If artifacts / preview tabs are not available, output the verification prompt inline in its own fenced Markdown block with a clear heading. This fallback is required.

### Required wrap-up structure

Always include:

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
Use the verification prompt with Perplexity or another source-checking workflow.

Upload the Citation Ledger and request an updated ledger with Verified, Verification Notes, and Correction filled in.

If the tool only returns narrative, reply:

"Please also produce the updated Citation Ledger xlsx with Verified, Verification Notes, and Correction filled for every non-[C] row."

When you have the verified ledger, verification notes, or corrected table, return in any chat with language like:

- "apply these verification corrections"
- "synthesize this verified research"
- "use this verified citation ledger to create the evidence report"
```

### Handoff guidance

Explain why these next-step instructions matter, but keep it brief:

- Perplexity or another source-checking workflow is recommended because it is independent of this chat and better suited for source-existence checks. For academic sources, Perplexity Deep Research with Academic connector enabled is preferred when available.
- The updated `.xlsx` ledger is preferred because it preserves row-level verification status, notes, and corrections.
- Narrative-only verification is incomplete unless the verifier cannot produce files. The user may need to ask the verifier to produce the updated ledger after the first response.
- Any chat can resume the workflow. The skill should pick up at Phase 3 when the user returns with verified results.

Next step: return to `SKILL.md` when the user comes back with verified results and proceed to Phase 3: Synthesize Verified Evidence.

