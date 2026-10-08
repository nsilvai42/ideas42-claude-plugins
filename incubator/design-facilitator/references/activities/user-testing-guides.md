# User Testing Guides

**Phase:** Build (Part 3 — Prototyping & User Testing).
**Status:** Essential. Part 3 slide 35: _"All three are considered essential"_ (Charrette + B-Mapping Lite + User Testing Guides).

**Source — training narrative:** Design Part 3 deck slides 41–51 (testing strategy framework, four-tool taxonomy, audience consideration, format/protocols, script examples, where-to-find-it). Slides 49–50 contain the canonical script examples — extracted-text bodies are sparse (image-heavy) but the speaker notes and structural framing are intact.
**Source — canonical activity card:** Menu of Design Activities slide 50.
**Source assets (ideas42 internal):** **User Testing Guide Template + Example; Sample User Testing Guides and Scripts.** (Linked from the activity card on Menu slide 50 — pending pull into `04_Assets/design-activities/`.) Also referenced in Part 3 speaker notes via Google Doc links (slides 44/45/46/47/48/60) — those are the template + example documents in the team's Drive. Don't auto-fetch those URLs; ask Niko to pull them locally.
**Design Guide point person:** Doug Palmer (also B-Mapping Lite).
**Function (per Menu):** _"Make a strategic plan for your internal and external user testing."_
**Effort (per Menu):** 45 min – 2 hours. 1–5 people. Remote: Great. (Co-design fit not specified on Menu slide 50 — but in practice this is internal team work; partners review the guide, they don't co-author it.)

## Purpose

A structured planning activity (not an in-session group activity) where the team writes the actual interview/observation guides used to test prototypes with users. Good user testing is *strategic* — the training opens this section with that sentence — meaning the guide targets specific assumptions the team needs to confirm or kill, not vibes.

## When to use it

- **After prototype is built**, before any user testing recruitment happens.
- **After Assumption Listing**, so the guide knows which assumptions to test.
- For every round of user testing — first-round prototype, revised prototype, etc. The guide gets refined each round.

## How it differs from neighbors

- vs **Assumption Listing**: Assumption Listing produces the *list of what to test*. User Testing Guides produces the *protocol for how to test it*.
- vs running the actual test: the Guide is the script + observation framework. Running the test is downstream.

## What a User Testing Guide includes (per Part 3 slide 41 framework)

The training (slide 41) decomposes user testing into four sub-flows; the Guide template covers the first two and feeds the second two:

| Sub-flow | What | Lives in the Guide? |
|---|---|---|
| Testing Strategy | Plan for testing assumptions that underly success | YES — Sections 1–3 below |
| Format & Protocols | Decide on the right format for the test | YES — Sections 4–5 below |
| Trial Run | Do a trial run to make sure everything is in place | The Guide is the input |
| Implement | Run the tests; update the prototype between sessions | The Guide is the input |

**Guide section structure:**

1. **Testing strategy — where you are** (Part 3 slide 42). First-round? Refinement? Validation? Pilot? Different stages call for different tools.
2. **Testing strategy — which tool** (Part 3 slide 43). The four-tool taxonomy:
   - **Exploratory test** — does the **concept** solve the problem? (Mostly qualitative. Used early.)
   - **Assessment test** — does the **prototype** solve the problem? (Qual and quant.)
   - **Validation test** — **how well** are we solving the problem? (Quantitative; uses benchmarks.)
   - **Pilot test** — **can we implement** the intervention without fail? (Operational; tests staff training, infrastructure.)
   _"Note: these all occur BEFORE your comparative effectiveness test (RCT, diff-in-diff, etc.)."_ — slide 43 verbatim.
3. **Assumption clarification + prioritization** (Part 3 slide 44). The explicit list of assumptions the test targets, ranked by how load-bearing they are.
4. **Audience definition** (Part 3 slide 45). _"If you're user testing a design to encourage an intervention for on-time court appearances, the general public might not be the right audience. Consider the characteristics, the benefits, and drawbacks of your sample."_ — slide 45 speaker notes verbatim.
5. **Format + protocols** (Part 3 slides 46–48). Interview vs observation, structured vs semi-structured, in-person vs remote, solo vs paired. Match format to the question type.
6. **Script** (Part 3 slides 49–50). Actual question wording, in order, with prompts and follow-ups. The training has Script Example slides at 49–50 — these are the `Sample User Testing Guides and Scripts` referenced from Menu slide 50.
7. **Observation framework** — what the team watches for that the user might not say.

## Prep checklist (for *building* the Guide, not running the test)

- [ ] Assumption list ready (output of Assumption Listing)
- [ ] Prototype ready (or specifically planned — sometimes you test with a paper prototype, sometimes a Figma click-through)
- [ ] Sampling/recruitment strategy decided (which users, how many, which prototypes to which people)
- [ ] **Don't forget partner/stakeholder interviews** — Simple Instructions doc flags this. Partners can answer feasibility questions users can't.
- [ ] If time allows: run mock interviews with team members to pressure-test the guide

## Strategy questions to answer first

Before drafting the guide, the training (Slide 42) walks through these:

1. **Where are you?** First-round testing? Refinement round? Final validation?
2. **Which tool?** (Slide 43, see four-tool taxonomy in Section 2 above.) Different testing tools serve different goals — pick deliberately, don't default.
3. **Which assumptions are highest-priority?** (Slide 44) Test the load-bearing ones, not the cosmetic ones.
4. **Who's your audience?** (Slide 45)
5. **Format + protocols** (Slides 46–48) — match the format to the question type.

## Prompt templates

The Guide is a written planning document, not a facilitated session, so "prompt templates" here means **the scaffolding the Guide-author fills in section by section**, plus the **interview-script prompts** the Guide produces as its main output.

### Guide-authoring scaffold (parameterized)

Each section below is a fill-in-the-blank for the Guide-author. Once `04_Assets/design-activities/user-testing-Guide-Template.docx` is pulled, replace this scaffold with the verbatim template structure.

```
USER TESTING GUIDE — {design-name} — {round-number}

Section 1. Where We Are
- Round number: {1 = exploratory / 2 = assessment / 3 = validation / 4 = pilot}
- What previous round told us: {summary or N/A if first round}
- What this round needs to answer: {one-paragraph problem statement}

Section 2. Tool Choice
- Selected tool: {exploratory / assessment / validation / pilot}
- Why this tool: {1–2 sentences tying tool to round}
- Method: {1:1 interview / observation / group test / intercept / diary / other}

Section 3. Assumption List (prioritized)
- Assumption 1 (load-bearing): {if this is wrong, the design fails}
- Assumption 2 (load-bearing): ...
- Assumption 3 (medium): ...
- Assumption 4 (medium): ...
- Assumption 5+ (low — test only if time): ...
(Pull from Assumption Listing output. Don't generate fresh here.)

Section 4. Audience
- Recruitment criteria: {who counts, who doesn't}
- N participants: {number + rationale}
- Sourcing: {how recruited; partner-introduced vs cold}
- DON'T-recruit list: {users who'd give misleading data — e.g., insiders, prior pilots}

Section 5. Format + Protocols
- Setting: {in-person / remote / hybrid}
- Duration per session: {minutes}
- Materials: {prototype version, props, paper backup}
- Recording: {audio / video / notes only — and consent process}
- Solo or paired: {if paired, who and why}
- Trial run scheduled: {date + reviewers}

Section 6. Script
[See Interview Script Skeleton below.]

Section 7. Observation Framework
- Behaviors to watch: {action 1, action 2, ...}
- Non-verbal signals to flag: {confusion, hesitation, abandonment, etc.}
- What we DON'T expect — flag if it happens: {surprise list}
```

### Interview script skeleton (parameterized — Section 6 of the Guide)

```
[Warm-up — 3–5 min]
Q1: Tell me about a recent time when {scenario related to design but BEFORE introducing it}.
   — Establishes rapport; surfaces user's mental model.

[Concept exposure — 2 min]
"I'm going to show you {prototype-name}. Take a minute to look at it. There's no right answer here, and it's not finished — we're still designing it."
[Hand over prototype. Don't pitch. Don't apologize.]

[Comprehension before evaluation — 5 min]
Q2: What do you think this is for?
Q3: Walk me through what you'd do if you encountered this in {realistic context}.
   — Comprehension answers come before evaluation answers.

[Assumption-targeted questions — 10–15 min, one per load-bearing assumption]
Q4: {Question targeting Assumption 1}
Q5: {Question targeting Assumption 2}
...

[Edge-case probe — 5 min]
Q_n: When would this NOT work for you?
Q_n+1: Who is this clearly NOT for?

[Buried-complaint surfacing — 3 min]
Q_final: If you could change one thing about this, what would it be?

[Wrap]
"Anything I didn't ask about that you think I should know?"
```

### Script-writing principles (from Part 3 slides 28, 44–45 + ideas42 standard practice)

- Open with low-stakes warm-up — establish rapport before any prototype is shown.
- Show the prototype neutrally. _"Don't pitch it, don't apologize for it. Just hand it over."_
- Ask comprehension questions ("what do you think this is for?") **before** evaluation questions ("what do you think of it?"). Comprehension errors invalidate the evaluation.
- Watch for what the user *doesn't* notice or *doesn't* try — not just what they react to. (Part 3 slide 28 _"Good user testing is strategic"_ frames this.)
- Close with: _"If you could change one thing about this, what would it be?"_ — surfaces the buried complaint that the user wouldn't volunteer.
- Train interviewers to seek **disconfirmation**, not confirmation. The team wants the user to say nice things; the Guide's job is to push against that bias.

**Verbatim template language pending** — once `04_Assets/design-activities/user-testing-Guide-Template.docx` and `Sample-User-Testing-Guides-and-Scripts.docx` are pulled from Box, replace the parameterized scaffolds with the verbatim template structure.

## Common pitfalls

- Leading questions. "Don't you think this is a great way to..." — useless data.
- Confirmation-seeking. The team wants the user to say nice things. Train interviewers to seek disconfirmation.
- Mixing audience types in one guide. A guide for end-users is structurally different from a guide for program staff. Build separate Guides per audience type.
- Forgetting partners. **Simple Instructions doc explicitly flags partner/stakeholder interviews** as part of the testing strategy — partners can answer feasibility questions end-users can't.
- Skipping the trial run (Part 3 slide 32). The first real interview is always the worst because the script has flaws nobody caught.
- Forgetting the observation framework — what people *do* often contradicts what they *say*. Observation rows are mandatory, not optional.
- Skipping the prioritization step in Section 3. If every assumption is "load-bearing," none are. Force the rank.

## Debrief questions (after testing rounds — training-standard, Part 3 slide 63)

- How did it go?
- What came up in your testing?
- Would you feel comfortable adapting this Guide for the next round?

Project-specific debrief additions:

- Which assumptions got confirmed? Killed? Newly raised?
- Where did users behave unexpectedly?
- Where do partners and end-users disagree?
- What needs another round of testing vs. what's settled?

## Output handoff

The Guide itself feeds:

1. **The actual user testing rounds** — internal first, then external.
2. **The Trial Run** (Part 3 slide 32) — pressure-test the Guide with team members before going live.

The user testing **output** (after running the rounds) feeds:

1. **Revise** (Simple Instructions Step 8) — comb interview/observation notes for design changes + new outstanding questions.
2. **Polish** (Step 9) — UI/copy refinement, with input from Mitra Salasel + Elise per the Simple Instructions doc.
3. **Next round of testing** — the revised prototype gets a new Guide, often with shorter assumption list (only the load-bearing ones that survived).

## Status

**Body content populated from training decks (Design Part 3 slides 41–51, 63) and Menu slide 50.** Training framework verbatim (4 sub-flows, 4-tool taxonomy with the "all occur BEFORE comparative effectiveness test" caveat). Guide-authoring scaffold and Interview Script skeleton parameterized for plug-in use; both are reconstructions until the canonical Box documents are pulled. **The User Testing Guide Template + Example doc and the Sample User Testing Guides and Scripts doc are the most material-rich pending assets** — these are the canonical script examples Part 3 slides 49–50 reference. Niko to pull from Box: `user-testing-Guide-Template.docx` and `Sample-User-Testing-Guides-and-Scripts.docx`. Once present, replace the parameterized scaffolds with verbatim template structure and consolidate the script-writing principles section against the canonical doc.
