# Phase 1: Scope & Research Prompts

Use this reference when the user has a broad topic, early question, preliminary sources, or a partially scoped research direction that needs sharper boundaries before external Deep Research prompts are generated.

## Phase 1 navigation

| Step | What happens | Output |
|---|---|---|
| 1. Orient | Summarize what the user already provided and identify missing dimensions | Known-context summary |
| 2. Scope | Use structured elicitation or conversational scoping to fill the six dimensions | Complete scope inputs |
| 3. Shape | Translate vague topics into answerable research questions and select the right research lens | Draft research plan |
| 4. Seed | Identify, verify, or propose seed sources that should anchor the research pass | Seed list |
| 5. Approve | Ask the user to approve or revise the research plan | Approved research plan |
| 6. Prompt | Generate tailored Deep Research prompts for the user to run outside this chat | Customized prompt(s) + next-step handoff |

Use these steps sequentially, but do not force unnecessary interaction. If the user already provides enough context for a step, summarize it and move forward.

## Goal

Turn an underspecified topic into an approved research plan and tailored external Deep Research prompts with:

- 1–3 focused research questions, or up to 5 for a thorough scan with distinct subtopics
- clear audience and decision context
- usable scope boundaries
- evidence preferences
- domain-specific citation seeds
- known exclusions and risks
- customized Deep Research prompts the user can run outside this chat

Phase 1 should make the later research easier to verify and ensure external Deep Research tasks answer the user's actual questions. This avoids having research runs wander into the wrong domain or return reports that are misaligned with the user's context. A vague prompt can produce a plausible report; a scoped prompt produces a report that can be checked, corrected, and synthesized.

## Inputs

Start from whatever the user has already provided:

- topic or broad question
- audience or deliverable context
- source files, bibliographies, spreadsheets, reports, or notes
- known authors, papers, frameworks, or organizations
- preferred geography, population, time period, or evidence type
- constraints from a partner, funder, team, or project

Do not re-ask for information the user already gave unless clarifications are needed. Start by summarizing what is known, then collect only the missing dimensions that matter.

Use this pattern before asking for more information. Render only the rows you can actually fill from the user's input — drop any dimension you'd otherwise mark `[unclear]`, `[not specified]`, or `[none yet]`. Empty rows feel like noise and obscure what's actually anchored. Surface what's still missing as a short inline list under the table instead.

```markdown
Here's what I have so far, so I don't loop on things you've already said:

| Dimension | Captured |
|---|---|
| [dimension you can populate] | [captured value, paraphrased from the user's input] |
| [next populated dimension] | [captured value] |

Still missing or unclear: [comma-separated dimensions you can't populate from the user's current input — or omit this line if everything's anchored].
```

Candidate dimensions to consider (include only the ones you have signal on): Topic area, Audience & purpose, Research type / lens, Depth, Emphasis, De-emphasis / exclusions, Population / setting, Geography & time, Seed sources.

If the user’s request clearly enters Phase 1, do not ask them to choose a phase. If the entry point is genuinely ambiguous, use `structured-question interface` to confirm where they are starting, recommending extra scoping whenever the initial request is missing any of the dimensions specified here. If specific dimensions are missing, skip confirming the entry point and present the user with the existing clear dimensions collected from their initial request, and ask for the missing dimensions using the format below.

## Scoping dimensions

Collect enough information to fill these six dimensions.

| Dimension | What to capture | Why it matters |
|---|---|---|
| Core questions | The specific questions the evidence scan should answer, scoped to an appropriate level of breadth and depth | Prevents topic drift and overbroad research |
| Audience & purpose | Who will use the output and what decision it informs | Shapes depth, tone, implications, and source standards |
| Depth | Light = quick directional or exploratory orientation (when users don't know much about the topic or the topic is broad by design); Standard = solid evidence scan for most internal-facing deliverables; Thorough = deeper scan for high-stakes, nuanced, contested, or strategically important questions | Sets expectations for breadth, source requirements, and verification effort |
| Evidence preferences | Academic literature, policy reports, practitioner evidence, grey literature, or mixed sources | Guides source targeting in the Deep Research prompts |
| Scope boundaries | Date range, geography, populations, sectors, outcomes, exclusions | Keeps research prompts precise and later verification tractable |
| Seed sources | Key papers, authors, frameworks, organizations, terms, or known source files | Improves recall and reduces missed literatures |

## How to gather scope

### Highly preferred: structured elicitation

If the `visualize` MCP is available in the Claude session, use `show_widget` with the `elicitation` module to gather the six dimensions at once. Pre-fill fields the user has already answered.

Before the first widget call, read the elicitation schema with `tool schema reader` using `modules: ["elicitation"]`. Only use the fallback below if you absolutely cannot use this tool.

The structured form should collect:

1. Core research question — show a draft for the user to edit or confirm.
2. Audience and decision — who the research is for and what it will inform.
3. Depth — Light, Standard, or Thorough. Render with a one-line distinction at point of decision and a recommendation so the user can pick or defer rather than answer from cold:
   - **Light** — quick directional scan when the topic is broad or the user is exploring early.
   - **Standard** — solid evidence scan for most internal-facing deliverables. **Recommended default unless there's a reason to pick otherwise.**
   - **Thorough** — deeper scan for high-stakes, nuanced, contested, or strategically important questions.

   Form copy should state the recommendation explicitly: "Recommended: Standard for most internal work — pick Light for quick orientation or Thorough for high-stakes / contested questions."
4. Source types — multi-select. Allow combinations of:
   - peer-reviewed academic
   - policy / government reports
   - practitioner case studies / program evaluations *(applied work from organizations running the intervention — e.g., a Mathematica program eval, an MDRC working paper, an organization's internal study)*
   - grey literature *(non-peer-reviewed but credible work — think tank reports, white papers, conference papers, dissertations, organization research not in journals)*

   Define the less-familiar terms inline in the form copy; users who don't know them can't pick informedly.
4b. Study designs to prioritize — multi-select, optional. The user may not care; default all on. Surfacing the axis here keeps the DR prompt's evidence-priorities block from being the first place the user encounters it:
   - experimental (RCTs and similar)
   - quasi-experimental (regression discontinuity, difference-in-differences, matched comparisons)
   - observational / correlational
   - qualitative
   - theoretical / conceptual
   - meta-analyses and systematic reviews

   Source type (academic / policy / practitioner / grey) and study design are orthogonal axes — a peer-reviewed paper can be RCT or observational, a practitioner report can describe quasi-experimental work — so keep the two questions separate.
5. Scope boundaries — render dimension by dimension, not as one textarea:
   - Date range — text input with default ("2014-present" or whatever fits the topic).
   - Geography — text input with default ("U.S." unless the topic clearly implies otherwise).
   - Population / setting — multi-select pills pre-filled with plausible options for the topic (e.g., for an education topic: K-12 / community college / 4-year college / adult learners). User deletes the ones that don't apply rather than editing a text default.
   - Outcomes of interest — multi-select pills pre-filled based on the topic (e.g., for persistence work: enrollment / retention / completion / earnings / belonging). User keeps the relevant ones.
   - Exclusions — multi-select pills pre-filled with commonly excluded populations, methods, or outcomes for the topic. User keeps the relevant exclusions.
6. Seed papers, authors, frameworks, organizations, or source files — optional upload or pasted citations / names. Use web search to pull live source information if pasted or referenced without full citation.

Use sensible defaults when the user has not specified them. State the defaults in the form copy so the user can edit rather than answer from scratch. For multi-select pickers (Population, Outcomes, Exclusions, Source types, Study designs), propose plausible options based on the topic so the user prunes rather than types from scratch.

### Fallback: conversational scoping

If the structured form is unavailable, gather the same dimensions through a short conversation. Do not turn the process into a long questionnaire. Keep questions sharp, concise, and focused on gathering needed information.

Use `structured-question interface` to collect missing dimension blocks.

Prefer question blocks that help the user choose between meaningful research lenses:

```markdown
“Best practices” can mean a few different evidence products. Which is closest?

1. Effectiveness lens — what does evidence say works?
2. Design lens — what principles should guide the intervention, tool, message, or service?
3. Landscape lens — what has been tried, by whom, for which populations, and with what results?
4. Implementation lens — what makes adoption, delivery, or scale easier or harder?
```

Use concrete follow-ups when dimensions are missing:

- "Who is this research for and what decision will it inform: partner-facing memo or deliverable, internal design decisions or activities, grant / funder audience or concept note/proposal, or something else?"
- "Which population or setting should anchor the scan?"
- "Which outcomes, behaviors, interventions, or programs are in scope, and which should be excluded?"
- "Should we prioritize peer-reviewed evidence, applied policy / government reports, practitioner case studies, grey literature, or a mix?"
- "Default scope is U.S.-focused, recent evidence from roughly the last 10 years, plus seminal earlier work. Should I change that?"
- "Are there seed papers, authors, frameworks, organizations, or internal memos I should make sure the research pass covers?"

Avoid asking the user to choose a phase or restate the whole project when the available context already implies the path.

## Common scoping patterns

Use these patterns to standardize common Phase 1 situations.

### User asks for “best practices” or "interventions" or "designs"

Treat these as underspecified. Ask whether they want an effectiveness, design, landscape, or implementation lens. If more than one lens is needed, convert each into a separate research question only when it would produce a meaningfully different research prompt.

### User asks for a “landscape scan”

Clarify whether they want:

- a map of existing actors, programs, tools, or interventions;
- evidence on what works;
- design principles or practical implementation guidance; or
- all of the above.

A landscape scan often needs broader source types, including policy / government, practitioner, and grey literature.

### User asks for an “evidence scan” or “literature review”

Prioritize source quality and claim traceability. Ask about evidence hierarchy, date range, geography, population, and outcomes. Keep the final research questions narrow enough to verify later. Specifically ask whether to prioritize field research, experimental studies, meta-analyses and systematic reviews or whether non-experimental and laboratory observational or correlational studies should also be included.

### User has a motivating problem but no research question

Translate the problem into one or more answerable questions. For example:

- Problem: "Users screen eligible but do not complete the next step."
- Possible question: "What explains drop-off between eligibility screening and benefit receipt, and what interventions reduce that gap?"

### User has strong domain context

Use their context instead of overwriting it. Summarize what is already known, name the remaining gaps, and ask only for missing boundaries or seeds.

## Seed-source handling

Seed sources are not general background reading. They are recall anchors for the external research prompts.

Good seeds sit at the intersection of:

1. the user's topic, population, intervention, setting, or outcome; and
2. the relevant research or practice domain.

For example, for "chatbots for healthcare," a useful seed might come from behavioral nudges using chatbots directly with patients or providers or reputable health organization pilots of a chatbot design. General behavioral science papers that rely on theoretical behavioral principles or outline broad behavioral insights are too broad unless the user explicitly wants theory background.

### Seed quality rules

- Prefer 3–5 strong seeds over a long, noisy list.
- Do not include general behavioral-science canons as seeds unless they are directly relevant to the question or the user requests their inclusion.
- Separate verified seeds from seeds suggested from memory. In cases where users provide no seeds or direction, conduct a quick web search to select suggested seed.
- Mark any seed not yet verified through uploaded files or web/source lookup as `[unverified]`.
- If the user has no seeds, propose potential seeds based on web search. If the user rejects inclusion of the seeds, suggest that the research prompt should ask the research tool to identify seminal and recent sources.

## Handling uploaded or provided source files

If the user provides bibliographies, spreadsheets, reading lists, research notes, or source corpora, triage them before proposing seeds.

1. Identify the user’s core question and scope.
2. Review the provided corpus for topical relevance.
3. Filter out sources that are only broadly adjacent.
4. Group relevant sources by theme, population, intervention, or evidence type.
5. Present candidate seeds for user confirmation.

Do not surface general adjacent material as seeds just because it appears in the corpus.

If the corpus is large, do not try to summarize everything in Phase 1. The goal is to identify the subset that should shape the research prompts.

## Draft the research plan

After scoping, produce a concise research plan. Make the plan specific enough that the Deep Research prompts can be generated without asking the user for the same information again.

Confirm the research plan with a compact summary table. The table is the approval ask, not a slimmed-down plan; save the full plan as a file or artifact (or hold it in chat below the table) so the user can dig in if they want.

```markdown
## Proposed research plan

| Dimension | Proposed | Edit? |
|---|---|---|
| Purpose & audience | [one-phrase summary] | |
| Research lens | [Effectiveness / Design / Landscape / Implementation / Mixed] | |
| Research questions | [N questions, one short label each] | |
| Depth | [Light / Standard / Thorough] | |
| Date range | [date range] | |
| Geography | [geography] | |
| Population / setting | [population] | |
| Benefits / intervention / program scope | [scope] | |
| Outcomes | [outcomes] | |
| Source types | [academic / policy / practitioner / grey — list selected] | |
| Study designs | [experimental / quasi / observational / qualitative / theoretical / meta — list prioritized, or "all"] | |
| Exclusions | [exclusions] | |
| Seed sources | [N seeds, M `[unverified]`] | |
| Known risks or gaps | [one short risk; expand on request] | |

Full plan saved to [link / artifact]. Open it for the full research-question text, full seed citations, and risk callouts.
```

Use 1–5 research questions, depending on how many separate and meaningfully distinct topics are uncovered through scoping. For thorough scans, prioritize more research questions that are better defined and more targeted. One question is usually better when the topic is narrow. Use multiple questions when the user's evidence need contains meaningfully distinct subquestions that should become separate research prompts, or when users want distinct lenses or types of evidence covered in the scan in depth.

## Ask for approval

Ask the user to approve or revise the research plan before generating Phase 1's final output: the customized Deep Research prompts.

Use concise language:

```markdown
Does this plan look right, or should we adjust anything before I generate the Deep Research prompts?
```

For targeted changes, show a compact diff instead of reprinting the entire plan.

## Generate the Deep Research prompts

After the user approves the research plan, generate one tailored Deep Research prompt per research question. Each prompt should be specific enough to run in a separate new chat or external research tool.

Read `references/prompt-templates.md` now. Use that file as the source of truth for full reusable prompt templates, especially when the user asks only for a prompt template without going through the full Phase 1 scoping workflow.

Before generating final prompts, check `references/quality-rubric.md` for Phase 1 quality gates. The research plan should be specific enough that the external research tool can answer the intended question without drifting into adjacent domains.

When generating prompts from Phase 1:

- Pull scoping-dimension values directly from the approved research plan. The Phase 1 scope is the source of truth for prompt variables.
- If a required variable is missing, ask the user for that specific gap rather than improvising.
- Generate one prompt per meaningfully distinct research question.
- Do not use in-chat WebSearch as a substitute for this research step. If a quick web search would suffice, the `SKILL.md` off-ramp should have caught it.

The structure below is the required Phase 1 prompt skeleton to populate from the approved research plan.

Use this structure for each prompt:

```markdown
# Deep Research Prompt [N]: [short title]

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

### Prompt generation rules

- Generate one prompt per research question.
- If the scan is light and has one question, generate one prompt only.
- If the scan is standard, usually generate 1–3 prompts.
- If the scan is thorough, generate up to 5 prompts only when each prompt covers a distinct subtopic, lens, population, or evidence type.
- Do not include generic seed sources unless they are directly relevant to the scoped question.
- Preserve the user's terminology where useful, but sharpen vague phrases like "best practices" into answerable research questions.
- Include scope boundaries and exclusions in every prompt so separate research chats do not drift.

## End of Phase 1

Phase 1 is complete when the user has approved the research plan and received the customized Deep Research prompt(s).

The approved plan should include:

- research question(s)
- audience and purpose
- scope boundaries
- source targets
- seed list, if any

The final output should include:

- the approved research plan summary
- one customized Deep Research prompt per research question
- instructions for the user to run each prompt externally and return with the completed research reports

## Finalize Phase 1

Use a standard phase wrap-up so the user understands what happened, can copy the next-step materials, and knows exactly how to re-enter the skill later.

Read `references/output-formats.md` before finalizing Phase 1 if you need the standard Phase 1 wrap-up structure.

### Wrap-up style

Render the wrap-up in-chat with readable formatting. Compactness > completeness — the user has the conversation. Use clear section headers, short bullets, and one instruction per line. Do not bury the final prompts above the fold; repeat them at the bottom so the user can copy them without scrolling back through the conversation.

Render the DR prompts using the lightest available format:

- **`interactive elicitation tool` available (any environment with an interactive preview tool) — preferred.** Render the prompts as a tabbed-preview widget: one tab per prompt, with a copy-to-clipboard button on each tab. Call `tool schema reader` first to read the schema before the first widget call.
- **Claude artifacts / preview tabs available — fallback.** Create one Markdown artifact per prompt with a clear title, such as `deep-research-prompt-1-[short-title].md`, `deep-research-prompt-2-[short-title].md`.
- **Otherwise — required final fallback.** Output each prompt inline in its own fenced Markdown block with a clear heading.

### Required wrap-up structure

Always include:

```markdown
## Phase 1 complete

[One-line summary — e.g., "Scoped a thorough rural-vs-urban higher-ed evidence scan; 3 Deep Research prompts generated."]

### Outputs
- Approved research plan: [link / artifact]
- Deep Research prompts: [tabbed widget, N artifacts, or N fenced blocks per the rendering rule above]

### Next from you
- Run each prompt in a separate chat (Claude Research / ChatGPT Deep Research / Gemini Deep Research). Don't continue chatting after the report is generated — export and move on.
- Export each report as `.docx` or markdown, not PDF.
- Re-invoke this skill when the reports are back: "verify these Deep Research reports", "fact-check these outputs", or "build a citation ledger from these reports".
```

If the user has been away from the conversation or the original request was thin, optionally prepend a one-line "What we started with" quote of the original request. Otherwise skip it — the user has the conversation.

### Handoff guidance

Explain why these next-step instructions matter, but keep it brief:

- `.docx` or markdown is preferred because PDF exports can break extraction of numeric values such as percentages, effect sizes, dollar figures, or sample sizes.
- Separate chats prevent each follow-up from re-reading the full Deep Research report and researched sources, which can compound token usage quickly.
- Any chat can resume the workflow. The skill should pick up at Phase 2 when the user returns with completed research reports.

Next step: return to `SKILL.md` when the user comes back with completed research reports and proceed to Phase 2: Claim Extraction + Verification Prep.

