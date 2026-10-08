# Extraction rules

How to read samples in Phase 3 and produce a v1 voice.md that captures real patterns instead of generic adjectives.

## Table of contents
- The reading pass
- What to extract (six categories)
- Anti-patterns: what to NOT extract
- When the samples disagree
- Calibrating confidence
- Translating extracted patterns into voice.md sections

## The reading pass

Read all samples once for gestalt, then read each sample again with extraction in mind. Take notes per sample (you'll cross-reference at the end). Don't draft voice.md until all samples are read — first impressions tend to over-weight whichever sample you read last.

Cross-reference: a pattern is real if it shows up in **at least 2 samples**. A pattern in only one sample might be a one-off; flag it as "tentative" and validate in Phase 4.

## What to extract (six categories)

### 1. Behavioral rules — patterns of *what they do*

Look for:
- Where do they put the main point? (First sentence? Buried? After scene-setting?)
- How do they open? (Greetings? In medias res? Question? Statement of fact?)
- How do they close? (Summary? Next-step? Question? Specific signoff?)
- Do they use contractions consistently? Selectively?
- Do they hedge? With what phrases?
- Do they ask questions of the reader? Rhetorical, real, or both?

Translate into rules: "Leads with the conclusion in the first sentence." "Opens with a fact, never a greeting, in internal emails." "Asks a real question to the reader at the end of long-form pieces."

### 2. Vocabulary

**Preferred (positive signal):**
- Words that appear unusually often across samples
- Phrases that appear in multiple samples (signature phrases)
- Specific concrete nouns the user reaches for over abstract ones (e.g., "team," "ship," "revenue" instead of "stakeholders," "deliver," "value creation")

**Banned (negative signal):**
- LLM-default words the samples *never* use, despite many opportunities
- Industry jargon the user actively avoids
- Words the user once used in an old voice they're trying to escape (ask if relevant)

Common LLM-default words to test against samples — if absent across all of them, ban: leverage, unlock, delve, navigate, robust, seamless, comprehensive, elevate, empower, harness, transform; passionate, authentic, thoughtful, meaningful, vibrant, innovative, dynamic (adjective-defaults); in today's fast-paced world, in the realm of, it's important to note that, in conclusion, furthermore, moreover, ultimately.

Don't ban a word the samples use even once — it's in the user's vocabulary even if it sounds AI-default.

Banned items can be a bare word ("leverage"), a phrase ("in today's fast-paced world"), or a *grammatical form* — e.g., a word the user freely uses as a noun but never as a verb. When you spot one, write the ban as the form to avoid: "to impact / impacted / impacting (verb forms only — noun is fine)" rather than "impact." Same pattern works for "interface," "leverage" when used as both noun and verb, etc. Default to the narrowest ban that captures the pattern.

### 3. Sentence rhythm

Measure (you don't need precise stats — eyeball is fine):
- **Average sentence length** — count words in 10–20 sentences across samples. Most people fall in 12–22 words.
- **Variance** — do they mix 4-word sentences with 30-word ones, or are they uniform? High variance = "burstiness" — a strong human-voice signal.
- **Paragraph length** — 1 sentence? 3? 5? Mixed?
- **One-sentence paragraphs** — frequency. Some writers never use them; others use them constantly for emphasis.

### 4. Structural defaults

- **Opener patterns** — how do the samples start? Pick the most common 1–2 patterns.
- **Closer patterns** — how do they end? Specific signoff phrases?
- **Lists** — when do they bullet vs prose? At what threshold (3 items, 5)?
- **Headers** — do they use them? At what length?
- **Transitions** — "and," "but," "so" mid-sentence? "However," "additionally"? Or none?

### 5. Idiosyncrasies

The signal-richest section. Pull anything that feels distinctive:
- Punctuation: em-dashes, en-dashes, semicolons, ellipses, exclamation use, question-mark use
- Capitalization: lowercase 'i,' lowercase headlines, ALL CAPS for emphasis
- Formatting: bold use, italic use, single-line breaks for emphasis, parenthetical asides
- Speech tics: "honestly," "tbh," "look," "right?," "anyway" — and note when these are stance-triggered rather than universal (e.g., "look"/"honestly" only when pushing back). Stance-scoped tics get a `(when: <trigger>)` annotation in the voice.md, not a `(channel: ...)` one.
- Specific recurring phrasings: "two things," "the real question is," "here's the thing"
- Syntactic shortcuts: dropping "that" in dependent clauses ("I think we should ship it"), dropping articles ("good point — moving on"), fragments as sentences for tempo, comma splices, dropped subjects in continuation sentences
- Avoidances: never starts a sentence with "I"; never uses "very"; never uses Oxford comma (or always)

If you can't articulate why a sample sounds like *that person*, it's probably an idiosyncrasy you haven't named yet. Read again and pin it down.

### 6. What it doesn't sound like

For every "sounds like" you write, ask: what's the antonym that would *break* the voice? Add it to "doesn't sound like."

Examples:
- Sounds like a peer thinking out loud → doesn't sound like a consultant performing expertise
- Sounds like specific examples → doesn't sound like vague generalities
- Sounds like direct asks → doesn't sound like hedged "perhaps consider"

## Anti-patterns: what to NOT extract

- **Adjectives without a behavioral rule attached.** "Friendly" alone is useless. "Friendly = uses the reader's name early, asks how they are without it being formulaic" is fine.
- **Aspirations the samples don't support.** If samples are corporate but the user says they want "punchy and direct," note it as a directional shift but draft voice.md from samples.
- **Patterns from a single sample, especially the most recent one.** Cross-reference rule.
- **Patterns that are channel-specific masquerading as voice.** Slack-only patterns shouldn't show up as universal rules. Note the channel scope.
- **Demographic stereotypes.** "Sounds millennial / Gen-Z / corporate / startup" is lazy and usually inaccurate. Describe the actual pattern instead.

## When the samples disagree

Two cases.

**Case A: register disagreement is real.** Slack is sharp; blog is corporate. The user has two voices. Either:
- Capture the dominant voice they want and note the other as "this voice doesn't apply to [channel]"
- Capture both as paired profiles ("casual mode" and "long-form mode") with explicit triggers

Default to the first unless the user explicitly wants both.

**Case B: one sample is off.** The user grabbed something that wasn't really their voice (ghostwritten, written under deadline, pre-current-style). Ask before excluding: "This [sample] reads differently from the others — was this a typical piece of yours, or an outlier?" If outlier, drop it.

## Calibrating confidence

For each rule you draft into voice.md, ask: would the user agree this describes them? If you're unsure, mark it tentative in your notes (you don't need to mark it tentative *in the voice.md itself* — the Phase 4–5 validation will surface tentatives that miss).

If 3+ rules in your draft are tentative, you don't have enough sample diversity. Go back to Phase 2 and ask for more.

## Translating extracted patterns into voice.md sections

| Extracted | Goes in voice.md section |
|---|---|
| Behavioral rules (Cat 1) | Top 5 rules, Structural defaults |
| Preferred + banned vocab (Cat 2) | Vocabulary |
| Length / variance / paragraph stats (Cat 3) | Sentence rhythm |
| Opener / closer / list / header patterns (Cat 4) | Structural defaults |
| Punctuation / cap / format quirks (Cat 5) | Idiosyncrasies |
| Antonyms of "sounds like" entries (Cat 6) | Sounds like / doesn't sound like |

Top 5 rules should be the **highest-leverage** rules — the ones whose violation most damages the voice. Pick in this priority order, top-down, until 5 slots are filled:

1. **Signature moves** — patterns that uniquely identify *this* writer/brand. The reader recognizes the voice from these alone (em-dashes paired as breath marks, counterintuitive opener, specific signoff).
2. **Strong avoidances** — bans whose violation breaks the voice (banned verb forms, banned LLM-defaults the samples never use).
3. **Rhythm and structure defaults** — variance, opener style, paragraph default — only if signature/avoidance slots aren't already taking 5.
4. **Generic style points** (contractions, plain language) — only if no slot 1–3 candidates remain.

If you find yourself reaching tier 4 to fill 5 slots, you've under-extracted at tier 1 — re-read the samples for what makes them *uniquely* sound like this voice. Lower-cost patterns that don't make the Top 5 still go into the more specific sections (Vocabulary, Sentence rhythm, Structural defaults, Idiosyncrasies).

**Dual placement of signature patterns.** A Tier-1 signature move that's also a Cat-4 (structural default) or Cat-5 (idiosyncrasy) appears in *both* Top 5 and its native section: a terse one-liner in Top 5, the elaborated form in Idiosyncrasies or Structural defaults. The two serve different reads — Top 5 is a checklist, the native section is the reference — so the same pattern earns its place in both. Don't dual-place lower-tier patterns: non-signature quirks live in their native section only.

## Examples to generate

For Phase 3 v1, generate 2–3 example before/after pairs. Pick contexts that match what the user said in Phase 1's "primary use" question. Make the "before" examples genuinely bland (LLM-default), not strawmen — the contrast lands harder when the before is plausibly what an unconfigured Claude would write.

Don't reuse exact sentences from the user's samples in the examples. Paraphrase or invent. Otherwise voice.md becomes a memorization exercise rather than a pattern guide.
