# B-Mapping Lite (Behavioral Mapping Lite)

**Phase:** Build (Part 3 — Prototyping & User Testing).
**Status:** Essential. Part 3 slide 35: _"All three are considered essential"_ (Charrette + B-Mapping Lite + User Testing Guides).

**Source — training narrative:** Design Part 3 deck slides 39–40 (intro + activity-card metadata).
**Source — canonical activity card:** Menu of Design Activities slide 49.
**Source assets (ideas42 internal):** **BMapping Instructions & Checklist; Blank Swing Sheet; Quick Checklist with Bins.** (These three named assets are linked from the activity card on Menu slide 49 — pending pull into `04_Assets/design-activities/`.) These are the canonical materials, NOT a Starter Deck — B-Mapping Lite uses checklists and a swing sheet rather than a slide-driven session.
**Design Guide point person:** Doug Palmer (also User Testing Guides).
**Function (per Menu):** _"A breakneck version of behavioral mapping to avoid recreating bottlenecks."_
**Effort (per Menu):** 30 min prep; 10 min intro + 45 min per idea. 1–5 people. Remote: Great. Co-design: **Risky** (one of the few activities flagged as risky for co-design — partners may not have B-mapping fluency).

## Purpose

A lightweight version of full Behavioral Mapping. Trace the user's behavioral journey through the design — what they do, what they think, what they feel, where the friction is, where the design intervenes. Surfaces gaps in the design that the team didn't see when they were focused on the artifact.

## When to use it

- **Right after Design Charrette**, paired. The Charrette gives you the sketch; B-Mapping Lite gives you the journey through the sketch.
- **Before user testing**, so the testing protocol can target the predicted friction points.
- When the team is overconfident in a design — B-Mapping Lite often surfaces failure modes nobody flagged in the Charrette.

## How it differs from neighbors

- vs **Design Charrette**: Charrette = the artifact. B-Mapping Lite = the user's path through it.
- vs **full Behavioral Mapping**: full B-Mapping is a multi-day deep mapping done in the Diagnose phase. The "Lite" version is a 30–60 min design-phase activity that's narrower and faster.
- vs **Assumption Listing**: B-Mapping Lite reveals assumptions implicitly through the journey trace; Assumption Listing makes them explicit.

## Prep checklist

- [ ] Have a Charrette sketch / synthesized design package (per Part 3 slide 58) to map against. B-Mapping Lite is downstream of Charrette in the canonical sequence.
- [ ] Define the persona / user segment whose journey you're mapping. The Diagnose-phase persona work feeds in here.
- [ ] **Pull the BMapping Instructions & Checklist** from Box once `04_Assets/design-activities/b-mapping-lite-Instructions-and-Checklist.docx` is available — this is the canonical step-by-step the activity is built around (NOT a slide deck).
- [ ] **Pull the Blank Swing Sheet** (`b-mapping-lite-Blank-Swing-Sheet.xlsx`) — the working artifact where the journey is captured.
- [ ] **Pull the Quick Checklist with Bins** (`b-mapping-lite-Quick-Checklist-with-Bins.docx`) — the bin-by-bin behavioral-bottleneck check.
- [ ] Block 30 min prep + ~10 min intro + 45 min per idea (so for 3 ideas, ~2.5 hours session). Per Menu slide 49.
- [ ] Decide which idea(s) to map. With time pressure, map only the most-confident design first; if it survives the lite map without major revisions, you can skip the others or batch them.
- [ ] Decide whether to map multiple personas — recommended: most-engaged AND least-engaged user (bouncers tell you more than completers).

## In-session timing (per idea, ~45 min — Menu canonical)

- 5 min: framing + persona reminder + load the Swing Sheet for this idea
- 5 min: lay out journey stages along the Swing Sheet (typical stages: aware → consider → try → complete → return / fail → re-engage)
- 25 min: per stage, walk the bins from the Quick Checklist with Bins — what does the user **do**, **think**, **feel**, **encounter**, **miss**? Where does the design intervene? (The bins ARE the canonical question set per Menu — don't free-style; use the checklist.)
- 5 min: highlight friction points and intervention points; flag anything that needs assumption-listing or user-testing
- 5 min: capture, hand off

## Prompt templates

Note: **B-Mapping Lite is checklist-driven, not deck-driven.** The canonical materials are documents (Instructions & Checklist, Swing Sheet, Quick Checklist with Bins). Until those Box-source documents are pulled, these prompt templates are conservative reconstructions; defer to the canonical docs once available.

Framing prompt (parameterized, conservative until canonical doc arrives):

> **B-Mapping Lite — for {design-name}**
> _We're going to walk a hypothetical user — {persona-name}, {persona-1-line-description} — through {design-name} stage by stage. At each stage, we'll fill in the Swing Sheet bins — what {persona-name} **does, thinks, feels, encounters, misses** — and flag any friction or intervention points._
> _The point isn't to predict perfectly. It's to surface assumptions about the user that the Charrette didn't make explicit, so we can test them in user testing._

Per-stage prompt (one pass per stage on the Swing Sheet):

> _**Stage: {stage-name}** — e.g., "User becomes aware of the program"_
> _- What does {persona-name} **do** at this stage?_
> _- What do they **think**?_
> _- What do they **feel**?_
> _- What do they **encounter** in their environment?_
> _- What do they **miss** / fail to notice?_
> _- Where does the design intervene? Is the intervention timed right?_
> _- Friction flag: anything in this stage that creates a new barrier?_

Bin-check prompt (run after the stage walk, against the Quick Checklist with Bins):

> _Now check this stage against the bottleneck bins: {bottleneck-bin-list}. For each, ask: did our design accidentally re-create this bottleneck, or address it?_

**Verbatim canonical-doc language pending** — once `04_Assets/design-activities/b-mapping-lite-Instructions-and-Checklist.docx` is pulled, replace the parameterized templates with the verbatim instruction copy. The Quick Checklist with Bins specifically supplies the canonical question set for the bin-check prompt; without it, the bin list above is incomplete.

## Common pitfalls

- Mapping the journey *the team wishes* the user had, not the journey they're likely to actually have. Push for realism — what does a tired, distracted, half-trusting user do? Part 3 slide 39 speaker notes: _"Your design will likely change the way people interact with something. That change is really important to understand."_
- Skipping the "think" and "feel" rows. They're where most behavioral insight lives, but they're harder to fill in than "do." Don't let the team skip them — they're explicitly in the bin set.
- Mapping only one persona. If your design serves multiple user types, map the most-engaged AND the least-engaged.
- Running it as co-design with partners who don't have B-mapping fluency. Menu slide 49 flags **co-design as risky** for this activity — partners can join later for friction-point review, but the bin-check pass should be ideas42-internal.
- Treating the map as a deliverable. It's a tool for finding the **friction list and assumption list**. The output is those lists, not the map itself.
- Skipping the bin check against the Quick Checklist. Without it, the activity becomes generic journey-mapping — losing the "behavioral mapping" half of its name.

## Debrief questions (training-standard, Part 3 slide 63)

- How did it go?
- What came up in your break-out room discussion?
- Would you feel comfortable using this activity on a project?

Project-specific debrief additions:

- Where in the journey is friction highest? Does the design address it?
- Where does the user lack information they'd need?
- Where is the design's intervention point too late?
- Which "feel" entries indicate emotional friction that no UX tweak fixes?
- Which bottleneck bins did the design re-create? Is that fixable in revision, or do we need to test it before deciding?

## Output handoff

The friction points + intervention gaps feed:

1. **Assumption Listing** (Simple Instructions Step 5) — assumptions about user state at each friction point.
2. **User Testing Guides strategy** — the testing protocol targets the predicted friction points.
3. **Design revision** — back to Charrette / Elaboration if the journey reveals the design itself is mis-targeted.

## Status

**Body content populated from training decks (Design Part 3 slides 39–40, 63) and Menu slide 49.** Verbatim Menu metadata (effort, team size, co-design risk flag, named asset list) pulled. **B-Mapping Lite is the most asset-dependent of the 6 — its prompt templates are conservative reconstructions until the three canonical Box-source documents are pulled.** Niko to pull from Box: `b-mapping-lite-Instructions-and-Checklist.docx`, `b-mapping-lite-Blank-Swing-Sheet.xlsx`, `b-mapping-lite-Quick-Checklist-with-Bins.docx`. Once present, replace the parameterized prompts with the verbatim Instructions copy and replace the bin-check placeholder with the actual bin list from the Quick Checklist.
