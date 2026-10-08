# Dot Voting

**Phase:** Consolidation (Part 2 — Fan In + Synthesize)
**Status flag (canonical):** **OPTIONAL** per Menu slide 42. Part 2 slide 25 names Categories + Weighted Metrics as the two consolidation essentials, NOT Categories + Dot Voting.
**Why this skill keeps it in v1 pilot scope anyway:** Dot Voting is the canonical lightweight prioritization tool used in the Sprint sequence (Menu slide 23 — _"Affinity Map + Dot Voting"_ for both Fan In and Synthesize) and is the partner-friendly consolidation tool. The yesterday-2026-05-07 v1-scope decision intentionally substituted Dot Voting for Weighted Metrics on the consolidation side because partners can run Dot Voting cold; Weighted Metrics requires criteria-design prep partners typically skip. Flag mismatch with Menu's "OPTIONAL" labeling for downstream readers.

**Source — training narrative:** Design Part 2 deck slides 36–39 (intro + variants); slide 51 (live practice instruction text); slide 56 (debrief).
**Source — canonical activity card:** Menu of Design Activities slide 42.
**Source assets (ideas42 internal):** Starter Deck; Input Sheet Template (digital); Input Sheet Template (in-person, _"though best to use butcher paper if possible"_ per Menu). All linked from the activity card on Menu slide 42. Pending pull into `04_Assets/design-activities/`.
**Design Guide point person:** Katy Davis (same as Categories).
**Function (per Menu):** Prioritize via inclusion (filtering on 1–4 factors).
**Effort (per Menu):** 1 hour prep; 45 min – 1.5 hour group session. 2+ people. Fine for remote; **fantastic for co-design.**

## Purpose

A lightweight prioritization activity. Each participant gets a fixed number of "dots" to spend on the ideas they like best. Aggregate counts surface group preference fast.

## When to use it

- **After Categories**, when the team is ready to prioritize but the criteria are still implicit / vibes-based.
- **With partners** — Menu slide 42 calls Dot Voting _"fantastic for co-design or difficult group decisions"_ because _"it levels power imbalances."_
- **In Sprint-paced projects** — Menu slide 23 pairs it with Affinity Map at both Fan In (Step 2) and Synthesize (Step 4) of the Sprint sequence.
- **As a quick gut-check** before committing to Weighted Metrics for Typical / Deep Dive sequences.

Menu slide 42 is precise about scale: _"Dot Voting narrows from a moderate set of ideas (max ~40) to a smaller final set."_ If you're starting with >40, run Categories first to dedupe; if you're starting with <10, the activity is overkill — discuss directly.

## How it differs from neighbors

- vs **Weighted Metrics**: Dot Voting captures preference; Weighted Metrics captures justified preference. If you need defensibility ("why these 10?"), use Weighted Metrics. If you need speed and partner alignment, use Dot Voting.
- vs **MoSCoW**: MoSCoW forces classification into 4 categories. Dot Voting is continuous.
- vs **Down-to-Earth**: Down-to-Earth is a feasibility filter applied late. Dot Voting is preference-based and applied earlier.

## Default approach

Menu slide 42 specifies **1–4 voting parameters** ("filtering via inclusion"). Each parameter can be a different color of dot. The training specifies dot allocation as a tunable knob — fewer dots = more concentration, more dots = more breadth. Conventional rule of thumb (not in source decks but consistent with the practice): each participant gets ~10–15% of the total idea count as dots per parameter. So 30 ideas → 3–5 dots per person per parameter.

**Variants from the training:**
- **Multi-parameter dots** (Menu slide 42) — different parameters / colors mean different criteria (e.g., green = "high impact"; red = "feasible"; blue = "exciting"). Up to 4 per the canonical activity definition.
- **Flag-for-later dots / "Bike Rack"** — Part 2 slide 38 explicitly: _"Flag extra zany ideas to return to later in the process – put them in the 'Bike Rack'."_ This is a separate marker — not a vote, but a "preserve, don't kill" signal. Critical for not losing high-variance ideas.
- **Virtual + in-person hybrid** — Part 2 slide 37 speaker notes describe a real example: _"Some mix of virtual (internal) and in person (external partners) would work best."_ Internal team dots virtually; partners dot during the in-person session.

## Prep checklist

- [ ] Categorized + shortlisted idea list already exists (Dot Voting after Categories is the canonical sequence; ideal scale is ≤40 ideas per Menu slide 42).
- [ ] Decide voting parameters (1–4 per Menu) — e.g., impact, feasibility, alignment with diagnosis, partner appetite. Write them down before the session.
- [ ] Decide dot allocation per parameter (rule of thumb: ~10–15% of idea count).
- [ ] Decide whether to use a separate **Bike Rack** marker for flag-for-later ideas (Part 2 slide 38). Recommended: yes.
- [ ] Pick the tool: virtual board with sticker emojis (Miro/FigJam — Part 2 slide 37 mentions Miro specifically as a recent ideas42 example) or in-person physical stickers / butcher paper.
- [ ] If running with partners: brief them on the dot rules in advance, not in the session. Pull the Starter Deck once `04_Assets/design-activities/dot-voting-Starter-Deck.pptx` is available.
- [ ] Block 45 min – 1.5 hours per Menu.

## In-session timing (~1 hour)

- 5 min: framing + voting parameters + dot rules + Bike Rack rule
- 5 min: silent re-read of the idea list (so people don't just vote on what they remember from Categories)
- 15–25 min: voting (silent, simultaneous if possible — see "anchoring" pitfall below)
- 5 min: tally — count votes per idea per parameter
- 15–25 min: discuss top vote-getters, low vote-getters, surprises, and Bike Rack flags

## Prompt templates

The 10-min training-practice version (Part 2 slide 51), verbatim:

> **Dot Voting (10 min):**
> _In our breakout rooms, we will visit the design training input sheet to:_
> _- select voting parameters (as a group), and_
> _- cast votes (individually)._

The full design-phase version, parameterized:

> **Dot Voting — for {design-challenge}**
> _We have ~{idea-count} ideas after Categories. Today we'll prioritize by voting on these {parameter-count} parameters:_
> _- {parameter-1} (color: {color-1}) — {short-definition}_
> _- {parameter-2} (color: {color-2}) — {short-definition}_
> _- (up to 4 parameters)_
>
> _You each get **{N} dots per parameter** to spend on whichever ideas you think rate highest on that parameter. Spend them however you want — concentrate on one idea or spread across many._
>
> _Separately, you have **2 'Bike Rack' flags** — for any zany or risky idea you want to preserve regardless of votes. The Bike Rack ideas don't count as votes; they're "don't kill this yet."_
>
> _Vote silently and simultaneously — don't watch each other vote. We'll discuss after the count._

Multi-parameter scoring sheet (for capture, not for in-session display):

```
Idea          | Impact (●) | Feasible (●) | Excite (●) | Bike Rack (★) | Total dots
{idea-1}      |   3        |   1          |   2        |   0           | 6
{idea-2}      |   1        |   4          |   0        |   1           | 5 + ★
...
```

**Verbatim Starter Deck language pending** — once `04_Assets/design-activities/dot-voting-Starter-Deck.pptx` is pulled, replace the parameterized version above with the deck's actual prompt copy.

## Common pitfalls

- Voting before re-reading. People vote on the loudest-named ideas, not the best ones.
- Letting voting be public — early votes anchor later ones. Use silent / simultaneous voting.
- Skipping the Bike Rack — many good ideas get killed at this stage that would have been resurrectable. Use the flag-for-later marker (Part 2 slide 38).
- Treating Dot Voting output as final. It's a *signal*, not a *decision*. The team should look at the top cluster + the surprising votes + the Bike Rack.
- Using Dot Voting at the wrong scale. >40 ideas is too many (per Menu slide 42); <10 is too few (just discuss). If you're outside this range, the team should pick a different consolidation activity.

## Debrief questions (training-standard, Part 2 slide 56)

- How did it go?
- What came up in your break-out room discussion?
- How might you adapt this activity to a future project?

Project-specific debrief additions:

- Which top vote-getter is the team genuinely excited about vs. obligated to keep?
- Which low vote-getter ended up Bike-Racked — and why?
- Do the top votes cluster in one Category, or spread across many? What does that mean for the next round?

## Output handoff

The voted list typically feeds:

1. **Weighted Metrics** next, if you're on a Typical / Deep Dive sequence and want defensible second-consolidation. The team narrows from voted top ~15 to top 4–10 with explicit criteria.
2. **Directly to Elaboration / Build** in Sprint sequences (Menu slide 23) — Sprint pairs Dot Voting with Affinity Map and goes straight from there to Charrette.
3. **Bike Rack list** — preserve, don't lose. Often resurfaces in Round Out or in the Polish phase.

## Status

**Body content populated from training decks (Design Part 2 slides 36–39, 51, 56) and Menu slide 42.** Verbatim training-practice prompt language pulled. Multi-parameter scoring sheet and Bike Rack mechanism documented. **Drift flag retained** between the Menu's "OPTIONAL" classification and yesterday's v1-pilot-scope decision — see top of file. Still pending: the canonical Dot Voting Starter Deck and both Input Sheet Templates (digital + in-person) — all linked from Menu slide 42; Niko to pull from Box into `04_Assets/design-activities/dot-voting-Starter-Deck.pptx` and `dot-voting-Input-Sheet-{digital,in-person}.xlsx`. Once present, update the "Prompt templates" section with verbatim deck copy.
