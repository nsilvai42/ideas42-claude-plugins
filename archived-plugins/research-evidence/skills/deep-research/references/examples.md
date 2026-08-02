# Examples

Use this reference when examples would help choose the right workflow behavior or calibrate output quality. Keep examples short and practical.

## Contents

1. Scoping vague asks
2. Good vs weak seed sources
3. Claim extraction examples
4. Verification code examples
5. Evidence strength examples
6. Phase wrap-up examples
7. Subtle verification risks
8. Weak or missing citations
9. Multiple research questions and up to 5 reports

## 1. Scoping vague asks

### “Best practices”

Input:

```text
I need best practices for chatbots that help students access public benefits.
```

Better Phase 1 move:

```markdown
“Best practices” could mean a few different evidence products. Which is closest?

1. Effectiveness lens — what does evidence say works when chatbots or conversational tools support benefits access?
2. Design lens — what principles should guide a student-facing benefits chatbot?
3. Landscape lens — what has been tried, by whom, for which students and benefits, and with what results?
4. Implementation lens — what makes adoption, trust, delivery, or scale easier or harder?
```

### Motivating problem but no research question

Input:

```text
Students screen eligible for SNAP but don’t complete the next step.
```

Possible research question:

```markdown
What explains drop-off between eligibility screening and benefit receipt among postsecondary students, and what interventions reduce that gap?
```

## 2. Good vs weak seed sources

Good seed:

```markdown
A study or evaluation directly related to the population, behavior, intervention, setting, or outcome in the research question.
```

Weak seed:

```markdown
A general behavioral science book, generic “nudges” paper, or broad theory source that does not directly connect to the question.
```

Rule: use 3–5 strong seeds. Do not stuff the prompt with generic canons unless the user explicitly wants theory background. If no seeds are available, ask the research tool to identify seminal and recent sources rather than inventing seeds.

## 3. Claim extraction examples

Source sentence:

```text
Text-message reminders increased FAFSA renewal among low-income students in a randomized trial.
```

Good claim row:

| Claim | Evidence Type | Stakes |
|---|---|---|
| Text-message reminders increased FAFSA renewal among low-income students in a randomized trial. | RCT | H |

Why: the claim is specific, evidence-bearing, and could affect recommendations.

Source sentence:

```text
Many students struggle with forms.
```

Possible claim row:

| Claim | Evidence Type | Stakes |
|---|---|---|
| The report claims many students struggle with forms, but does not cite a specific source or statistic. | Synthesis / uncited | M |

Why: uncited framing can shape interpretation and should be trackable.

## 4. Verification code examples

| Code | Example |
|---|---|
| [C] | The cited paper exists and reports the same finding, population, and effect direction. |
| [P] | The source supports the general finding, but the report overstates the population or effect size. |
| [U] | The source cannot be found, the citation is incomplete, or the source does not contain enough information to verify the claim. |
| [X] | The claim says the intervention increased uptake, but the cited source found no statistically significant effect. |

## 5. Evidence strength examples (GRADE)

| Label | Example |
|---|---|
| High | Multiple high-quality RCTs, well-conducted meta-analyses, or systematic reviews with consistent findings across the relevant population directly support the claim. |
| Moderate | RCTs with limitations (inconsistent results, methodological flaws, indirectness, or imprecision) OR exceptionally strong observational evidence supports the claim. |
| Low | Observational studies without exceptional strengths, or RCTs with serious limitations, support the claim. Direction is plausible but estimate is uncertain. |
| Very Low | Case reports, expert opinion, theoretical reasoning, single small study, or studies with major methodological flaws. Also assigned when the only evidence is adjacent-domain extrapolation (different population, setting, or intervention). |

When sources conflict, assign the GRADE level that fits the overall body of evidence and add a separate `[mixed evidence]` flag rather than averaging contradictions away.

## 6. Phase wrap-up examples

### Phase 1 wrap-up excerpt

```markdown
## Phase 1 complete: Scoping + Deep Research Prompt Generation

### What you now have
- Approved research plan
- Domain-specific seed list
- 2 customized Deep Research prompts

### Next from you
Run each prompt in its own new research chat. Export each completed report as `.docx` or markdown, not PDF. Then return with the reports and say: “verify these Deep Research reports.”
```

### Phase 2 wrap-up excerpt

```markdown
## Phase 2 complete: Claim Extraction + Verification Prep

### What you now have
- Initial Citation Ledger: [file]
- Verification prompt: [copy block]
- Rows requiring special attention: 6 cross-report numeric conflicts, 3 uncited synthesis claims

### Next from you
Upload the ledger to Perplexity or another source-checking workflow. For academic sources, use Perplexity Deep Research with the Academic connector enabled when available. Ask for the updated `.xlsx` ledger with Verified, Verification Notes, and Correction filled in. Narrative-only verification is incomplete unless the verifier cannot produce files.
```

### Phase 3 wrap-up excerpt

```markdown
## Phase 3 complete: Synthesize Verified Evidence

### What you now have
- Final Citation Ledger
- Evidence Report
- Executive Summary
- Corrections Applied changelog

### Optional next steps
Use the Executive Summary for stakeholders. Upload the Evidence Report and ledger to NotebookLM if you want audio overviews, mind maps, or follow-up synthesis questions. Run follow-up synthesis queries one at a time.
```


## 7. Subtle verification risks

| Risk | Example |
|---|---|
| Misattribution | The claim cites Study A, but the finding actually appears in Study B. |
| Composite statistic | The report combines numbers from multiple sources but cites only one. |
| Overstated framing | The source says “associated with,” but the report says “caused.” |
| Source blending | A sentence combines findings from several sources without clarifying which source supports which part. |
| Overgeneralization | A study of adult SNAP applicants is presented as evidence about college students. |

## 8. Weak or missing citations

If a report has weak citations, do not discard it automatically. Extract material claims, mark missing citations clearly, and warn that many rows may verify as [U].

Example ledger row:

| Claim | Source Cited | Evidence Type | Stakes | Verification risk |
|---|---|---|---|---|
| The report claims chatbot reminders reduce application abandonment, but no source is cited. | Missing | Uncited synthesis | H | Likely [U] unless a source is found during verification |

## 9. Multiple research questions and up to 5 reports

For thorough scans, Phase 1 may generate up to 5 Deep Research prompts, which can produce up to 5 research reports.

Good Phase 3 synthesis pattern:

```markdown
1. Synthesize within each research question first.
2. Then synthesize across questions for shared mechanisms, contradictions, evidence gaps, and practical implications.
3. If more than 5 reports are provided, batch them or ask which 5 are highest priority.
```

Example:

```markdown
Research Question 1: What interventions reduce benefits-application drop-off?
Research Question 2: What chatbot design principles improve trust and completion?
Research Question 3: What implementation barriers affect adoption by colleges?

Cross-question synthesis: reminders may improve completion, but trust and implementation capacity shape whether reminders work in practice.
```

