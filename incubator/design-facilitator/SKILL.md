---
name: design-facilitator
description: Plan, facilitate, and synthesize ideas42's internal Design phase activities — DDD(TS) ideation, consolidation, prototyping, and user testing. Use when an ideas42 team member needs to (1) pick an activity sequence (Sprint / Typical / Deep Dive) for an upcoming design phase, (2) prep or run a specific named activity (Change the Context, Forced Fitting, Trade, Creative Matrix, Telephone, Categories, Dot Voting, Weighted Metrics, MoSCoW, Down-to-Earth, Design Charrette, B-Mapping Lite, User Testing Guides, Elaboration, Assumption Listing), (3) consolidate raw ideation output into a shortlist, or (4) generate a customized Activity Kit / Starter Deck. Trigger phrases include "design phase," "design session," "design sprint," "ideation," "consolidation," "fan out," "fan in," "DDD(TS)," "Equity Premortem revisit," or any of the named activities above. Do NOT trigger for UI/visual design, system design, or graphic design — this is for ideas42's behavioral-design facilitation methodology only.
---

# Design Facilitator (ideas42)

This skill helps an ideas42 facilitator plan, run, and consolidate the team's Design phase — the part of DDD(TS) where the team takes a defined behavioral problem and moves through ideation → consolidation → prototyping → user testing toward a final design package.

It assumes the reader is an ideas42 employee who has been through Parts 1–3 of the design training but wants a working partner to plan a sequence, prep a session, or synthesize messy output. It does NOT teach design from scratch — for that, point users to the recorded trainings and the Menu of Design Activities.

## Step 1 — Classify the request

Before anything else, decide which of three moments-of-use the user is in. The downstream behavior is materially different for each.

| Cue | Moment | Route to |
|---|---|---|
| "I have a project starting in N weeks" / "What activities should we run?" / mentions timeline + partners | **Plan the sequence** | [references/sequences.md](references/sequences.md) |
| "I'm running {activity} on {date}" / "How do I prep for {activity}?" / mid-session questions | **Facilitate a single activity** | [references/activities/](references/activities/) |
| "Here are our 200 ideas, help us narrow down" / paste of raw ideation output / "what's our shortlist?" | **Synthesize / consolidate** | [references/synthesis-flows.md](references/synthesis-flows.md) |

If unclear, ask one short question. Don't guess.

A user can be in multiple moments across one conversation (plan → facilitate → synthesize). When the moment shifts, re-read the relevant reference. Don't try to hold all three flows in working memory at once.

## Step 2 — Read the routed reference, then act

Each route's reference file owns the actual workflow. SKILL.md keeps only the routing gate plus cross-cutting conventions.

**Plan the sequence** → [references/sequences.md](references/sequences.md). Asks for timeline, partner involvement, design challenge, prior phase outputs (Equity Premortem, Diagnose deliverables). Returns a sequence (Sprint / Typical / Deep Dive or custom), an activity-by-activity rationale, a calendar with prep buffers, and a flag for any activity that needs partner-side prep.

**Facilitate a single activity** → [references/activities/{activity-slug}.md](references/activities/). Each activity file covers: purpose, when to use it, how it differs from neighbors, prep checklist, in-session timing, prompt templates customized to the user's design challenge, common pitfalls, debrief questions.

**Synthesize / consolidate** → [references/synthesis-flows.md](references/synthesis-flows.md). Five named flows (Categories, Dot Voting, Weighted Metrics, MoSCoW, Down-to-Earth). Each has its own input shape and output shape. The skill picks the right flow based on the user's stage (first vs second consolidation) and constraints, or asks if ambiguous.

## Step 3 — Activity Kit / Starter Deck production (when requested)

When the user wants a customized Starter Deck for an activity (e.g., "make me the Change the Context deck for our EITC project"), produce a `.pptx`:

1. Load the activity's source template from `04_Assets/design-activities/{slug}-Starter-Deck.pptx`. Each per-activity reference file documents the canonical asset name(s) — see the "Source assets" line at the top of `references/activities/{slug}.md`. As of 2026-05-08 these Box-source assets are pending pull; check `04_Assets/design-activities/` first.
2. Customize the design-challenge slide, prompt slides, and team-roster slide with project context. Use the verbatim "Prompt templates" section in the activity's reference file as the source of truth for prompt copy.
3. Apply ideas42 brand via the `anthropic-skills:ideas42-brand` skill — call it before final write.
4. Save as `.pptx` to the user's outputs / selected folder.

If the Starter Deck source isn't available yet (most activities, as of 2026-05-08), fall back to outputting the kit content as structured markdown built from the activity's reference file (Purpose / Prep checklist / Prompt templates / Debrief questions). Tell the user the brand-styled deck is a v2 capability gated on the Box asset pull. Don't fabricate a deck against a missing template.

## Step 4 — 10-step DDD(TS) process awareness

If the user mentions stages outside the four moments above (early user input, elaborate, list assumptions, polish), see [references/10-step-process.md](references/10-step-process.md). Some steps (Elaboration, Assumption Listing) have facilitation activities of their own; others (early user input, polish) are project-management steps where this skill points the user to the right ideas42 resource (Concept Cards, Mitra Salasel + Elise for graphic design, Fiverr for illustration).

## Conventions

- Always assume the team has already finished the **Diagnose** phase — this skill is for the Design phase only.
- Always remind the team to **revisit the Equity Premortem at Step 0**. The Simple Instructions doc makes this explicit, and skipping it is a known failure mode.
- For ideation outputs, expect 100–400 raw ideas before consolidation, ending around 20–50 unique ideas after the second consolidation. Use these counts to sanity-check user inputs.
- Default partner-engagement assumption: partners are at least somewhat involved. If the user says partners are uninvolved or unavailable, swap out activities that depend on them (e.g., Telephone with partners → internal-only Forced Fitting).
- "Essential" activities flagged in the trainings: Change the Context (ideation), Categories + Dot Voting (consolidation), Design Charrette + B-Mapping Lite + User Testing Guides (build). When in doubt, recommend an essential.
- When producing decks, always call `anthropic-skills:ideas42-brand` for color/typography/logo guidance. Don't free-style brand.

## Anti-patterns

- Don't recommend Telephone (or any partner-dependent activity) without confirming partner availability — it's a wasted activity slot.
- Don't skip the Equity Premortem revisit — reset the team's awareness of pitfalls before ideating.
- Don't conflate first consolidation (fanning in / clustering) with second consolidation (synthesizing into ~20-50 final ideas) — they serve different goals and the trainings flag this.
- Don't recommend more than ~5 activities for a Sprint sequence — capacity is the constraint, not idea count.
- Don't try to hold all three moments-of-use (plan / facilitate / synthesize) in working memory across a long chat. Re-read the routed reference each time the moment shifts.
- Don't trigger on "UI design," "graphic design," "system design," "logo design," or any non-behavioral design context.
