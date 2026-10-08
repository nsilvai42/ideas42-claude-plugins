---
name: anti-ai-writing
description: Audit and rewrite text to remove AI-tell writing patterns so drafts read like a person wrote them. Use when the user asks to humanize a draft, remove AI-isms, "de-AI" text, audit writing against AI tells, or whenever drafting in the user's voice or on their behalf. Applies to written output only, not conversational replies.
---

# Anti-AI Writing Style

This skill removes the patterns that make writing read as AI-generated. Apply it with judgment — clean, natural writing wins over rule-following. The goal is never to disguise sloppy work; it is to stop statistically average phrasing from flattening a real voice.

## When to apply

- The user asks to humanize, audit, or "de-AI" a draft.
- You are drafting in the user's name or voice (pair with their voice.md if one exists).
- A draft is going to an external audience (clients, funders, the public).

## Workflow

1. **Draft or read normally first.** Don't write defensively; over-correcting produces forced, choppy text.
2. **Audit against the hard bans below.** Flag each violation rather than silently rewriting if the user asked for an audit.
3. **Rewrite flagged sentences.** Delete the pattern, keep the claim. Prefer the shortest honest version.
4. **Final read-aloud test.** If the user wouldn't say the sentence out loud to a colleague, rewrite it again.

## Hard bans

**Negative parallelism in any disguise.** "It's not X, it's Y." / "Not X. Y." / "Less X, more Y." / "X is dead. Y is the future." Delete the rejected half and state the claim directly.

**AI-tell vocabulary.** delve, leverage, seamless, robust, unlock, harness, tapestry, game-changer, transformative, streamline, elevate, empower, pivotal, crucial, showcase, underscore, foster, garner, intricate, vibrant, landscape (abstract), testament, paradigm, cutting-edge, revolutionize, holistic, synergy, groundbreaking, unparalleled, meticulous.

**Bloated verbs and copula avoidance.** "serves as," "stands as," "boasts," "represents a," "features" (for "has"). Use is, has, uses.

**Dead openers and transitions.** "In today's...", "It is important to note," "Furthermore," "Moreover," "That said," "Additionally" at sentence start.

**Significance inflation.** "...highlighting the importance of," "...reflecting broader trends," "stands as a testament to," "plays a vital role in," "marking a pivotal moment." Cut the trailing -ing analysis clause; keep the fact.

**The rule of three.** "Speed, efficiency, and innovation." One strong item beats three padded ones. Vary list lengths.

**False ranges.** "From X to Y" where no real scale exists. Name the items plainly instead.

**Formula endings.** No "Challenges and Future Prospects," no summary of what the reader just read, no "In conclusion."

## Pacing and formatting

- Short paragraphs. Vary sentence length — AI writes like a metronome; real writing is uneven.
- Bold sparingly. Don't bullet-point what should be prose. Headers like salt, not structure-by-default.
- Use digits for numbers. Limit em dashes to one or two per piece.
- Active voice. First and second person are fine. Starting with "And" or "But" is fine.

## Specificity

Replace vague claims with concrete ones. "The tool improves workflow" becomes "The tool removes 4 approval emails from the invoice process." Numbers, names, dates, and examples are the cheapest credibility there is.

## Anti-overfitting

Don't force every sentence to be punchy and don't ban yourself into blandness. Hedge when genuinely uncertain ("maybe," "sometimes") — AI never hedges; humans do. The test for every line: would the user actually write this?

## The audit prompt

When the user says "audit this against the anti-AI writing style," list each violation with the ban it breaks and a suggested rewrite, then offer a clean full rewrite.

## Full field guide

For the complete, example-rich catalog of AI writing signs (Wikipedia's "Signs of AI writing" field guide — significance inflation, weasel attributions, elegant variation, title case, boldface overuse, and more), read `references/signs-of-ai-writing.md`. Consult it when auditing long or high-stakes documents.
