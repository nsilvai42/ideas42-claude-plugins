# voice.md template — output structure

This is the canonical structure of the file the skill produces. Use it as the scaffolding for the v1 draft in Phase 3 and refine in Phase 5.

## Table of contents
- Design principles for the file itself
- Section list (in order)
- Per-section field shapes
- Length budget
- The starter template (copy-paste)

## Design principles for the file itself

The voice.md is being read by an LLM at inference time. It competes with the user's actual prompt for attention. So:

- **Keep it under 600 words.** Past that, the model starts averaging across rules instead of applying them.
- **Lead with the strongest behavioral rules.** First section sets defaults; later sections refine.
- **Concrete over abstract.** "Never say 'unlock' or 'leverage'" beats "use plain language."
- **Pair every rule with a do/don't example** when the rule is non-obvious.
- **Cut anything you can't enforce.** "Be authentic" is unenforceable; cut it. "Use contractions in everything except formal external letters" is enforceable; keep it.
- **Reflect what's true, not what the user aspires to.** Aspirations go in a clearly-labeled "directional notes" section if at all.

## Section list (in order)

1. **Identity line** — one sentence. "Voice profile for [Name / Brand]. Captured [date]. Use when writing [primary use]."
2. **Voice in one sentence** — distilled descriptor, 15–25 words, behavioral not adjectival.
3. **Top 5 behavioral rules** — highest-leverage rules. Fill in priority order: signature moves > strong avoidances > rhythm/structure defaults > generic style points. Numbered list, each rule one sentence. See `extraction-rules.md` for the full rubric.
4. **Sounds like / doesn't sound like** — two columns or two lists. 4–6 entries each.
5. **Vocabulary** — preferred words/phrases (5–10) and banned words/phrases (5–10). Banned list usually includes LLM-default words the samples never use.
6. **Sentence rhythm** — average length, variance pattern, paragraph defaults.
7. **Structural defaults** — opener habits, closer habits, list/header use, signature-style if relevant.
8. **Idiosyncrasies** — punctuation tells, capitalization quirks, formatting habits.
9. **Examples** — 2–3 short before/after pairs. Generic input → output in voice.
9b. **Per-channel notes** (optional) — only when Phase 1 returned multi-channel/mixed AND ≥2 extracted patterns are channel-scoped. Holds patterns that don't apply globally.
10. **What to do when the topic doesn't fit the voice** — the escape hatch (technical writing, legal, formal external — when to *intentionally* break voice).
11. **How to use this file** — the footer (paste into Project / system prompt / context).

Sections 1–8 are the rules. Section 9 is the few-shot calibration. Sections 10–11 are operational. Cut any section that has nothing to say — empty sections waste tokens.

## Per-section field shapes

### Identity line
> Voice profile for [Name]. Captured 2026-05-07. Use when writing emails, Slack messages, blog posts.

### Voice in one sentence
Make it behavioral. Bad: *"Direct, warm, and human."* Good: *"Leads with the point, mixes one-sentence paragraphs with longer ones, never uses corporate filler."*

### Top 5 behavioral rules
Numbered, each one sentence, each enforceable. Examples:
1. Lead with the conclusion or the action; never bury it past the second sentence.
2. Use contractions everywhere except external formal correspondence.
3. Mix one-sentence paragraphs with three-sentence ones — variance is the point.
4. Cut every adjective that doesn't earn its place.
5. End with the next step or a question, not a summary.

### Sounds like / doesn't sound like
Use parallel construction so the contrast lands. Each entry is a short phrase, not a full sentence.

```
Sounds like:                          Doesn't sound like:
- A peer thinking out loud            - A consultant performing expertise
- Specific examples over abstractions - Vague generalities
- Em-dashes used as breath marks      - Stuffy semicolons
- Direct asks                         - Hedged "perhaps consider"
```

### Vocabulary
Two lists: preferred, banned. Banned should include the LLM-default words your samples didn't use. Common defaults to consider for the banned list: leverage, unlock, delve, navigate, robust, seamless, comprehensive; passionate, authentic, thoughtful, meaningful, vibrant, innovative, dynamic (adjective-defaults); in today's fast-paced world, it's important to note that, in conclusion.

Preferred list = words/phrases the user actually reaches for repeatedly. Don't pad — 5–10 each is enough.

Banned entries can be a bare word ("leverage"), a phrase ("in today's fast-paced world"), or a *grammatical form* of a word the user uses freely in another form. Write the form to avoid: `to impact (verb forms only — noun is fine)`, `to interface (verb only)`. Same approach for "leverage" if used as a noun but not a verb, etc.

### Sentence rhythm
- Avg sentence length: ~X words (state the actual number)
- Variance: high / medium / low (high = lots of mixing; low = uniform)
- Paragraph default: ~Y sentences (state the number)
- One-sentence paragraphs: rare / occasional / frequent

### Structural defaults
- Openers: how do they typically start? ("Plain factual statement, never 'I hope this finds you well'", "Question to the reader", "Short scene-setting clause")
- Closers: how do they sign off? Specific signoff phrases if recurring.
- Lists/headers: how often, when? Bullets only for >3 items? Headers only for >500 words?

If a default differs by channel, use sub-entries instead of one flat line:
- `Closers — default: <pattern>`
- `Closers — Substack: question to the reader`
- `Closers — email: "—Sam", never "Best,"`

Same shape works for openers when long-form opens differ from short-form. Don't split a field by channel unless the samples actually disagree — flat is cheaper.

### Idiosyncrasies
The hardest section to fake — and the most valuable. Pull from samples. When a quirk only applies to certain channels, annotate the scope inline with `(channel: <scope>)`. When a quirk only applies in certain stances or registers (pushing back, excited, frustrated, pitch-mode), annotate with `(when: <trigger>)`. The two annotations are parallel; use whichever fits, or both. Examples:
- Em-dashes — used as breath marks, often in pairs
- Lowercase 'i' (channel: Slack/SMS only)
- "Look" / "honestly" as soft openers (when: pushing back)
- Single-line paragraph breaks for emphasis
- Uses parentheticals (often)
- One-sentence paragraphs frequent (channel: long-form only)
- "tbh" / "ngl" in casual; never in formal
- Drops the "that" — "I think we should ship it" not "I think that we should ship it"
- Avoids exclamation marks except in genuine excitement

### Examples
2–3 short before/after pairs. Pick contexts the user actually writes in.

```
Example 1 — Slack message
Generic: "Hi team, I wanted to share an update on the project. We've made some progress and I think it's going well overall. Let me know if you have any questions."
In voice: "Quick update — shipped the redesign yesterday. Two open bugs, neither blocking. Anything you want me to surface?"

Example 2 — Blog opener
Generic: "Today, I want to discuss the importance of focus in the modern workplace."
In voice: "Most productivity advice misses the point. The problem isn't that you're distracted — it's that you're working on the wrong thing."
```

### Escape hatch
One paragraph. "When [context], break voice and use [conventional pattern] instead." Examples: legal letters, formal grant applications, technical API docs.

### How to use
Three bullet points covering Project / system prompt / per-conversation context. Plus the line about re-running every 6–12 months.

## Length budget

| Section | Target words |
|---|---|
| Identity line | 15 |
| Voice in one sentence | 15–25 |
| Top 5 rules | 60–90 |
| Sounds like / doesn't sound like | 50–80 |
| Vocabulary | 30–60 |
| Sentence rhythm | 30–50 |
| Structural defaults | 50–80 |
| Idiosyncrasies | 50–100 |
| Examples | 80–150 |
| Per-channel notes (optional) | 30–80 |
| Escape hatch | 30–50 |
| How to use | 30–50 |
| **Total** | **~440–770 words** |

If a section is shorter, fine — don't pad. If much longer, you're probably writing aspirationally; cut.

## Starter template (copy-paste skeleton)

```markdown
# Voice profile — [Name / Brand]
Captured [YYYY-MM-DD]. Use when writing [primary use].

## Voice in one sentence
[Behavioral descriptor.]

## Top 5 rules
1. [Rule]
2. [Rule]
3. [Rule]
4. [Rule]
5. [Rule]

## Sounds like / doesn't sound like
**Sounds like:**
- [Phrase]
- [Phrase]
- [Phrase]
- [Phrase]

**Doesn't sound like:**
- [Phrase]
- [Phrase]
- [Phrase]
- [Phrase]

## Vocabulary
**Preferred:** [word], [word], [word], [phrase], [phrase]
**Banned:** [word], [word], [word], [phrase], [phrase]

## Sentence rhythm
- Avg length: ~[N] words
- Variance: [high/medium/low]
- Paragraphs: ~[N] sentences default; [rare/occasional/frequent] one-sentence breaks

## Structural defaults
- Openers: [pattern]
- Closers: [pattern]
- Lists/headers: [when]

## Idiosyncrasies
- [Quirk]
- [Quirk]
- [Quirk]

## Examples

**[Context 1]**
*Generic:* [bland version]
*In voice:* [voice version]

**[Context 2]**
*Generic:* [bland version]
*In voice:* [voice version]

## Per-channel notes (optional — include only if voice differs across channels)
- [Channel]: [pattern]
- [Channel]: [pattern]

## Escape hatch
[When and how to break voice intentionally.]

## How to use
- Paste into a Claude Project's custom instructions
- Or paste at the top of a system prompt
- Or upload as context whenever you want voice to apply
- Re-run voice-setup every 6–12 months or when outputs feel off
```
