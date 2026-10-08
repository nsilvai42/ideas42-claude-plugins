# Validation and refinement (Phase 4–5 mechanics)

The loop where voice.md actually gets good. Until the user has approved 3 sample outputs in 3 different message types, the skill is not done.

## Table of contents
- Phase 4 setup — picking the 3 message types
- Phase 4 generation — rendering the outputs
- Phase 5 — the per-output diagnostic
- Edit clustering — going from diagnostics to voice.md changes
- Re-rendering and the next round
- Definition of done
- Failure modes and recovery

## Phase 4 setup — picking the 3 message types

After v1 voice.md is drafted, ask the user to pick 3 message types. Use `AskUserQuestion` with `multiSelect: true`. Pull the menu from `message-types.md`. The exact menu in the question depends on the user's Phase 1 "primary use" answer:

- **Long-form primary** — show: blog post intro, newsletter section, LinkedIn post, internal memo, podcast show notes
- **Short-form primary** — show: email reply, Slack message, SMS, group text, quick announcement
- **Marketing primary** — show: landing page hero, product email, social post, sales follow-up, case study opener
- **Internal comms primary** — show: team update, project status, FAQ answer, all-hands intro, Slack announcement
- **Mixed** — show: email, Slack message, Substack/Medium opener, LinkedIn post, internal memo, SMS (six items; user picks up to 3 via multiSelect)

If the user picks fewer than 3 in the multi-select, fill the remaining slot(s) from the matching primary-use defaults — do not ask twice.

If they pick more than 3, take the first 3 listed (or ask which 3 to start with).

## Format-diversity check

After the user has picked 3 message types, classify each as **short** (<5 sentences typical), **medium** (5–15), or **long** (>15) using the lengths in `message-types.md`. If all 3 fall in the same bucket, surface this once before generating:

> "All 3 picks are short-form. Voice.md often passes a same-shape validation but breaks on a different length. Want to swap one for a [medium/long]?"

If the user says no — e.g., their primary use is genuinely narrow (Slack-only, all-LinkedIn) — proceed and note in the v1 voice.md that the profile is shape-tuned to that bucket. If they swap, re-run the check on the new selection, then proceed.

## Phase 4 generation — rendering the outputs

For each chosen message type, you need a **topic** to write about. **Default: ask the user.** Run a single short prompt: "Quick — give me a one-line topic for each of the 3 outputs (a real thing you'd plausibly write about). Or say 'pick something' and I'll choose."

Fallback ladder if asking isn't viable (user delegated, or already said "just figure it out"):

1. **Reuse a topic from earlier in the conversation** — a project, decision, or subject the user named in Phase 1 or 2.
2. **Pick a generic plausible topic** — last resort. Generic topics risk contaminating the per-output diagnostic with topic-noise rather than voice-noise (the user reads "this doesn't sound like me" when really they mean "I'd never write about this"). If you go here, pick topics that fit the user's apparent surface area (their role, brand, recurring subjects from samples) and flag the choice when rendering: "I picked these topics — say if any feel off-distribution and we'll swap."

Generate each output applying v1 voice.md as if it were the live system prompt. Do not editorialize — render clean copy as if shipping.

Render all 3 in a single message with clear separators:

```
**Output 1 — Email reply**
[Topic: "Following up on the Q3 planning meeting"]
[Output text]

---

**Output 2 — Slack message**
[Topic: "Heads-up on the timeline shift"]
[Output text]

---

**Output 3 — Blog post intro**
[Topic: "Why we changed our hiring process"]
[Output text]
```

Then proceed to Phase 5 diagnostics.

## Phase 5 — the per-output diagnostic

For each of the 3 outputs, ask **one structured `AskUserQuestion`** with multiple questions inside. The questions vary by what's most likely off, but a strong default set is:

```
Question 1: How does Output [N]'s overall feel land?
- Sounds like me / our brand
- Close but off in [specific way]
- Doesn't sound like me at all

Question 2: What's most off about this output? (multiSelect: true)
- Too formal
- Too casual
- Wrong rhythm — too uniform
- Wrong rhythm — too choppy
- Wrong word choice — there are specific words I'd never use
- Missing a specific habit of mine (name it in Question 3)
- Wrong structure (length, opener, closer)
- Wrong tone for this channel
- Nothing — this one's good

Question 3: Specific words, phrases, or habits I'm missing or getting wrong? (free-text via "Other") — examples: "you missed my em-dashes," "you used 'impact' as a verb," "the closer should ask the reader a question on Substack pieces."
```

If the user picks "Sounds like me" + "Nothing — this one's good" on Question 1+2, mark the output as approved and move on.

If they flag specific issues, capture them verbatim and proceed to clustering. **Do not edit voice.md mid-diagnostic** — finish all 3 outputs, then cluster.

You may need to adapt the question set:
- If the v1 was visibly off (a whole register wrong), skip the granular question and ask one big "what's the main thing?" question
- If the user already approved 1 or 2 outputs, only diagnose the failing one(s)

## Edit clustering — going from diagnostics to voice.md changes

After all 3 diagnostics, you'll have a pile of feedback. Cluster it into **2–4 concrete voice.md edits**. Don't propose more than 4 changes per round — bigger changes create regression risk on the outputs that were already passing.

Clustering moves:

- **Multiple outputs flagged "too formal"** → change the rhythm or add a "default to contractions" rule
- **Same banned word offender flagged twice** → add to the banned vocabulary list explicitly
- **"Missing my em-dashes" + "wrong rhythm"** → may both point to the same idiosyncrasy section update
- **"Wrong opener" on the blog post but not the email** → channel-specific note in structural defaults, not a global rule

Show the user the proposed diff in a compact form:

```
Proposed voice.md edits (round 2):

1. Add to "Banned vocabulary": "delve," "dive into," "in this post"
2. Add to "Top 5 rules" (replacing #4): "Open every blog post with a counterintuitive claim, not a topic announcement."
3. Add to "Idiosyncrasies": "Em-dashes used as breath marks, often paired."

Apply these and re-render?
```

Use `AskUserQuestion` with options like "Apply all," "Apply some — let me say which," "Don't apply — let me explain."

If they want partial edits, take their picks and apply only those.

## Re-rendering and the next round

After applying edits, **re-render all 3 outputs from scratch** with the same topics and message types. Don't surgically patch the previous outputs — that's not what voice.md will do in production.

Then run the diagnostic again. If any output the user previously approved now fails, that's a regression — flag it, ask whether to revert the edit or keep it and accept this trade-off.

Track the round number ("Round 2 outputs" / "Round 3 outputs") so the user can see progress.

## Definition of done

The skill is done when:
- All 3 outputs receive an explicit "Sounds like me / our brand" or "this one's good" from the user
- No flagged issues remain
- No regressions from previous rounds

"Good enough" is not done. The user has to actually approve each output.

## Failure modes and recovery

**3 rounds in, still failing on the same output.**
Root cause is almost always sample insufficiency in that register. Go back to Phase 2: "We're stuck on [Slack messages]. Can you send me 2–3 more real Slack messages from the last week so I can recalibrate?"

**The user keeps saying 'I don't know what's wrong, it just doesn't sound like me.'**
Don't keep asking the same diagnostic. Instead, render a deliberately bad version (default LLM voice with no profile) and ask the user to flag what's off about *that*. The contrast surfaces patterns the user couldn't articulate against the closer-to-right v1.

**Outputs are individually fine but the voice feels different across the 3.**
Check if you're applying voice.md consistently. Reread voice.md and check if there are contradictory rules. If the user has different voices per channel and voice.md is collapsing them, split voice.md into a primary section and a per-channel notes section.

**The user wants to keep refining past round 4.**
At round 4+, the marginal quality is usually flat and you're chasing noise. Tell the user explicitly: "We've made 3 rounds of edits. The remaining differences are likely things voice.md can't fully constrain — Claude will get them right ~70% of the time and miss sometimes. Want to ship this version and iterate later, or keep going?"

**The user says 'just write all 3 yourself first and I'll edit those.'**
This is fine as a Phase 5 fallback — sometimes editing is faster than diagnostic questions. Render the 3 outputs, get inline edits back, then reverse-engineer voice.md changes from what they edited. Show the proposed voice.md diff before applying.
