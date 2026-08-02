# Prompt Templates

Use this reference as the source of truth for reusable evidence-scan prompts. Replace bracketed text with project specifics. When a phase has already collected the needed variables, populate them directly instead of asking again.

## Contents

1. Phase 1: Deep Research Prompt Template
2. Evidence Quality Appendix
3. Phase 2: Verification Prompt Template
4. Phase 3: Synthesis Queries
5. Narrative Synthesis Template

## Phase 1: Deep Research Prompt Template

Use this template after the Phase 1 research plan is approved. Generate one customized prompt per meaningfully distinct research question, up to 5 prompts for thorough scans.

If the user asks only for a reusable prompt template and does not want scoping, provide this template with bracketed placeholders.

```markdown
# Deep Research Prompt: [Short title]

<role>
You are a senior research analyst conducting evidence synthesis for [audience / project context]. Your work is read by decision-makers who need calibrated evidence assessment, not advocacy. Frame findings through a practical, applied lens unless the topic clearly requires another orientation.
</role>

<research_question>
[Specific research question]
</research_question>

<context>
[2–4 sentences on the project, audience, decision context, and why this matters]
</context>

<scope>
- Date range: [date range]
- Geography: [geography]
- Population / setting: [population or setting]
- Benefits / intervention / program scope: [scope]
- Outcomes: [outcomes]
- Exclusions: [exclusions]
</scope>

<evidence_priorities>
Prioritize: [peer-reviewed empirical studies, meta-analyses, systematic reviews, policy / government reports, practitioner evaluations, grey literature, or mix]

When evidence types differ, distinguish:
- experimental, quasi-experimental, observational, qualitative, and theoretical evidence
- field evidence vs. lab evidence
- direct evidence vs. adjacent-domain extrapolation
- research findings vs. practitioner recommendations
</evidence_priorities>

<evidence_strength_rubric>
Apply the GRADE framework to every major finding. Use these four levels:

**High:** Further research is very unlikely to change confidence in the estimate. Typically multiple high-quality RCTs, well-conducted meta-analyses, or systematic reviews with consistent findings across populations.

**Moderate:** Further research is likely to have an important impact and may change the estimate. RCTs with limitations (inconsistent results, methodological flaws, indirectness, or imprecision) OR exceptionally strong observational evidence.

**Low:** Further research is very likely to change the estimate. Observational studies without exceptional strengths, or RCTs with serious limitations.

**Very Low:** Any estimate is highly uncertain. Case reports, expert opinion, theoretical reasoning, or studies with major methodological flaws.

If a finding draws on adjacent-domain evidence (extrapolation from a different population, setting, or intervention), label it as "Very Low — adjacent-domain extrapolation" rather than the strength of the underlying study.

When sources conflict, assign the GRADE label that reflects the overall body of evidence and add a separate `[mixed evidence]` flag. Surface the contradiction explicitly rather than averaging it away.
</evidence_strength_rubric>

<seed_sources>
[Include 3–5 strong domain-specific seeds when available. For seeds marked [unverified], verify author, year, title, and existence before relying on them. If no seeds are available, identify seminal and recent sources.]
</seed_sources>

<anti_hallucination_rules>
These rules apply to ALL sources, not just seeds:

- Never fabricate citations, statistics, sample sizes, effect sizes, dates, or DOIs.
- If you cannot verify a specific number, write "approximately" or "reported as" with a citation rather than a fabricated precise figure.
- If a source's existence is uncertain, flag it with "[verify before use]" rather than presenting it as confirmed.
- For any claim where confidence is below ~95%, hedge explicitly: "Research suggests..." or "Available studies indicate..." rather than stating it as fact.
- Distinguish what authors *claim* from what their *evidence* actually supports.
- Flag any finding based on a single study with "[single-study evidence]".
</anti_hallucination_rules>

<output_requirements>
Go straight to findings. Keep background brief unless necessary to interpret the evidence.

Structure the report as:

1. **Key findings** — 3–5 findings, each with specific citations and a GRADE label (High / Moderate / Low / Very Low). Include the adjacent-domain flag where applicable.

2. **Evidence landscape** — organized by theme. For each theme, list source details, study design (RCT, quasi-experimental, observational, qualitative, theoretical), population, sample size where reported, and GRADE strength.

3. **Gaps and limitations** — what the evidence does not resolve, including contradictory findings, weak-evidence pockets, and methodological gaps.

4. **Practical implications** — what this means for [specific audience / decision].

5. **Practical recommendations** — ranked by evidence strength AND relevance to [specific audience / decision]. Distinguish *well-supported recommendations* from *promising but under-evidenced recommendations*.

6. **Reference list** — full citations in [APA 7 / Chicago / Vancouver — pick one] format with DOI or stable URL where available.

For each major claim:
- cite the source precisely
- include statistics, effect sizes, sample sizes, or study design details where available
- flag claims based on a single study
- never present adjacent-domain evidence as direct evidence
- flag uncertainty explicitly using the hedging language above

Output as markdown or `.docx`, not PDF.
</output_requirements>

<self_verification>
Before finalizing, verify:

1. Every finding has a GRADE label and a precise citation.
2. No claim exceeds the strength of its underlying evidence.
3. Single-study claims are flagged.
4. Adjacent-domain extrapolations are flagged.
5. Recommendation rankings reflect the evidence-strength labels in section 1.
6. The exclusions in <scope> have not been violated.
7. No statistics, dates, or DOIs have been fabricated — when uncertain, hedge or remove.

If any check fails, revise before producing the final output.
</self_verification>
```

## Evidence Quality Appendix

Append this block when stronger quality control is needed.

```markdown
## Additional evidence quality requirements

- Flag any claims where evidence is limited to a single study or extrapolated from adjacent domains.
- Provide an explicit GRADE evidence strength rating (High / Moderate / Low / Very Low) for each major claim.
- Note practitioner-oriented recommendations separately from research findings.
- When you are less certain about a claim, say so explicitly.
- Distinguish causal / experimental findings from correlational evidence.
- Prefer field research over laboratory studies when both exist.
- Identify methodological limitations, sample-size concerns, and generalizability boundaries.
```

## Phase 2: Verification Prompt Template

Use this template after generating the initial Citation Ledger. Before giving the prompt to the user, scan the actual ledger and populate the `<focus_areas>` block with specific high-suspicion rows (cross-report inconsistencies, weak primary sources, suspiciously round numbers, possible composites, uncited load-bearing claims, citation-claim domain mismatches, etc.).

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

Follow-up text if the verifier returns narrative only:

```text
Please also produce the updated Citation Ledger `.xlsx` with Verified, Verification Notes, and Correction filled for every non-[C] row. A narrative-only response is incomplete unless you cannot produce files.
```

## Phase 3: Synthesis Queries

Use these internally in Phase 3 or provide them to the user for NotebookLM / equivalent grounded synthesis tools if requested. If using these in NotebookLM or another grounded synthesis tool, run them one at a time rather than all at once.

### Query 1 — Convergence

```text
What findings appear consistently across multiple reports? Identify the 3–5 most robust conclusions with source citations and evidence strength.
```

### Query 2 — Contradictions

```text
Where do these sources disagree or present contradictory evidence? What explains the contradictions, such as different populations, methods, geographies, outcomes, or contexts?
```

### Query 3 — Practical implications

```text
Based on all the verified evidence, what are the strongest practical recommendations for [project / decision]? Rank them by evidence quality and implementation relevance.
```

### Query 4 — Gaps

```text
What critical evidence gaps remain that this scan could not resolve? Which gaps matter most for [project / decision]?
```

### Query 5 — Evidence quality

```text
For each major finding, assign a GRADE evidence-strength rating (High, Moderate, Low, or Very Low) and explain why. Consider methods, sample sizes, directness, consistency, and source quality. Flag adjacent-domain extrapolations as Very Low. Surface contradictory evidence with a `[mixed evidence]` flag rather than averaging it away.
```

## Narrative Synthesis Template

Use internally when writing the Executive Summary.

```markdown
Synthesize the verified research into a coherent evidence base for [project / decision].

Inputs:
- Corrected research reports / notes, up to 5 reports
- Final Citation Ledger
- Corrections Applied changelog
- Approved research plan

Structure:
1. Context — what question we answered and why it matters
2. Key findings — the 3–5 most important conclusions, each with evidence strength
3. Evidence landscape — organized by theme, not by source
4. Gaps and limitations — what we still do not know
5. Practical implications — what this means for [specific decisions]
6. Reference list

Rules:
- Only include findings from verified and corrected material.
- Flag any inference or extrapolation with [INFERENCE].
- When combining findings, preserve citations and note source basis.
- Do not smooth over contradictions — present them explicitly.
- Rate evidence strength for each key finding.
```

