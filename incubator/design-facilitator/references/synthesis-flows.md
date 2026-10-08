# Synthesis & Consolidation Flows

**Source:** Design Part 2 deck (full); Menu of Design Activities slide 15.

This reference owns the **synthesize / consolidate** route. Read this when the user has raw ideation output and wants help narrowing it.

## Two consolidation moments — they are different

Per Part 2 deck slides 20–23, consolidation happens **twice** in the design phase, and the goals are different:

1. **First consolidation — Fanning In.** Take ~100–400 raw ideas, cluster them, dedupe, surface gaps. Output: ~20–50 unique ideas with a category structure. Don't try to pick winners yet.
2. **Second consolidation — Synthesize.** Take ~20–50 organized ideas, narrow to 4–10 elaborated ideas worth prototyping. This is where prioritization criteria come in.

If the user is mid-flow, the skill must figure out which consolidation moment they're in before recommending a flow. **Ask if ambiguous.**

## Three principles for selecting the best ideas

From Part 2 deck slide 13:

1. **Revisit diagnosis** — refresh the team's memory of the behavioral problem and target user before any prioritization. Ideas that were "obvious winners" during ideation often look different against the diagnosis.
2. **Use multiple criteria** — single-criterion picking (e.g., "most exciting") under-weights feasibility, equity, partner-fit. Force the team to apply 2–4 criteria.
3. **Make the trade-offs visible** — when you eliminate an idea, name what's getting traded away. Otherwise the team sleepwalks into a constrained shortlist.

## The five consolidation activities

### Categories — first consolidation, organize without prioritizing

→ See [activities/categories.md](activities/categories.md) for the full activity reference.

Use this as the **default first move** for any consolidation, unless the idea count is small (<30).

### Dot Voting — first or second consolidation, prioritize without justifying

→ See [activities/dot-voting.md](activities/dot-voting.md).

Use after Categories. Use when partners are involved (lower cognitive load than Weighted Metrics). Use as a quick gut-check before committing to a more rigorous flow.

### Weighted Metrics — second consolidation, prioritize WITH justification

The defensible version of Dot Voting. Each idea is scored against 3–5 criteria, criteria are weighted, total scores rank the ideas.

**Typical criteria** (Part 2 deck slide 42):
- Behavioral impact (will it move the target behavior?)
- Feasibility (can the partner implement it?)
- Equity (does it close or widen disparities?)
- Cost / effort
- Novelty / differentiation

**Process:**
1. Team agrees on 3–5 criteria (don't go above 5 — it dilutes signal).
2. Team agrees on weights (1–3 scale per criterion). Make trade-offs explicit.
3. Each idea gets scored on each criterion (1–5 scale).
4. Sum the weighted scores. Rank.
5. Discuss surprises — high scorers the team feels meh about, low scorers the team feels strongly about. The numbers are a *signal*, not a *verdict*.

**Common pitfall:** treating Weighted Metrics output as final. The training (Slide 13) is explicit — make the trade-offs visible, don't sleepwalk.

### MoSCoW — partner-engaged second consolidation, classify by must/should/could/won't

For aligning with partners on what's in scope. Each idea goes into one of:
- **M**ust have (without it, the design fails)
- **S**hould have (high value, not strictly required)
- **C**ould have (nice-to-have)
- **W**on't have (not this round)

Use when partners need to have a stake in the prioritization. Skip if internal-only.

**Common pitfall:** everything ends up in Must or Should because nobody wants to put their idea in Could. The facilitator has to push for honest classification.

### Down-to-Earth — late filter, kill ideas that won't survive contact with reality

A feasibility filter applied near the end of consolidation. For each shortlisted idea, ask:
- Can the partner actually implement it?
- Does it require resources the team doesn't have?
- Does it require behaviors the user is unlikely to do?
- Does it conflict with constraints (regulatory, legal, brand)?

Use this **after** Weighted Metrics or MoSCoW, as a sanity pass before committing the shortlist to Elaboration.

## Recommended flow combinations

| Stage | Partner involvement | Recommended flow |
|---|---|---|
| First consolidation | Internal only | Categories → Dot Voting |
| First consolidation | Partner-engaged | Categories → Dot Voting (partners do dots) |
| Second consolidation | Internal only | Weighted Metrics → Down-to-Earth |
| Second consolidation | Partner-engaged, criteria-aligned | Weighted Metrics (joint) → Down-to-Earth |
| Second consolidation | Partner-engaged, scope-aligned | MoSCoW (joint) → Down-to-Earth |
| Mixed engagement | Some partners, not all | Internal Weighted Metrics first → MoSCoW with partners on the shortlist |

## When the user dumps raw output and asks for help

Standard response shape:

1. Confirm the consolidation moment (first vs second).
2. Ask the load-bearing questions: how many ideas? what stage? partner involvement? criteria already chosen or open?
3. Recommend the flow (one of the rows in the table above).
4. Offer to **execute the flow** on the dumped output — cluster, score, return a structured shortlist as markdown or an .xlsx.
5. Flag what's lost in the consolidation (e.g., "Idea #43 ranked low but felt important — flag for later?").

## Output handoff

The shortlist (4–10 elaborated ideas) feeds **Elaboration** (one person per idea), then **Assumption Listing**, then **Prototyping**.

## Status

**Skeleton complete; example outputs and weighted-metrics scoring sheet pending Box-folder source assets.**
