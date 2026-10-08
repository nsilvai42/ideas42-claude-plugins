---
name: voice-setup
description: Captures a person's or brand's writing voice as a portable voice.md. Walks the user through collecting writing samples, extracts behavioral rules and stylistic patterns, then iteratively refines the profile by rendering 3 sample outputs in different message types (email, Slack, blog post, etc.) and using structured per-output diagnostics until the user is happy. Use when the user asks to capture their voice, define a brand voice, train Claude to write like them, build a style profile, clone their writing style, or create a voice guide for an LLM.
---

# voice-setup

Build a portable `voice.md` that makes Claude (or any LLM) write in a specific person's or brand's voice. The deliverable is a single markdown file the user can paste into a Claude Project, system prompt, or another tool.

## When to use this skill
Trigger when the user asks to:
- Capture, define, set up, or create a writing voice or style profile
- Make Claude (or another LLM) sound like them or sound like their brand
- Clone a writing style from samples
- Build a brand voice charter, style guide, or voice document
- Stop AI outputs from sounding generic / "AI default voice"

## Core principle
Behavioral rules beat adjective soup. A voice doc that says "friendly and professional" produces nothing. A voice doc that says "lead with the insight, never bury it; never use 'leverage' or 'unlock'; mix one-sentence paragraphs with three-sentence ones" produces something useful. This skill exists to translate samples into rules of that second kind.

The signal that captures voice lives in patterns across samples — sentence-length variance, vocabulary tells, sentence-opener habits, punctuation quirks, structural defaults — not in what the user *thinks* their voice is. Treat user-stated voice ("I'm direct and warm") as a hypothesis to validate against samples, not as authoritative input.

## The five-phase flow

Copy this checklist into your response when starting a run:

- [ ] Phase 1 — Scope: person or brand? What contexts will they write in?
- [ ] Phase 2 — Collect: walk the user through what to upload; coach until floor is met
- [ ] Phase 3 — Extract: read samples; draft v1 voice.md
- [ ] Phase 4 — Validate: render 3 outputs in different message types the user picks
- [ ] Phase 5 — Refine: per-output diagnostic via AskUserQuestion → cluster into edits → re-render → repeat until user signs off on all 3

Do not skip phases. Do not produce a voice.md without sample evidence. Do not call the skill done until the user explicitly approves all 3 validation outputs.

---

## Phase 1 — Scope

Use `AskUserQuestion` for two questions:

1. **Subject:** Person or brand?
   - *Person* — an individual's voice (yours or someone else's, with permission)
   - *Brand* — an organization, product, or publication's voice
   - *Both / hybrid* — e.g., "my voice when writing as my company's founder" — handle as person-primary, but read brand style guide if available

2. **Primary use:** Where will this voice be used most?
   - Free-text or pick from: long-form (blog, newsletter, essays), short-form (Slack, email, SMS), public-facing marketing, internal comms, mixed

The two answers shape Phase 2 prompts and Phase 4 message-type defaults. Save the answers; carry them forward.

If the user says "just figure it out" — default to **person** with **mixed** primary use, and tell them you're doing so.

---

## Phase 2 — Collect

The user uploads samples. Your job is to coach them to the right *count* and *register diversity* — not just whatever they grab first.

**Floor: 3 samples. Recommended: 5–7 spanning different registers.**

For full collection guidance per subject type, see `references/sample-collection.md`. The short version:

- **Person:** ask for samples across emotional registers — casual / explanatory / excited / frustrated / persuasive. Slack messages, emails (with PII redacted), blog posts, journal entries, LinkedIn posts, Substack drafts all count. Mix lengths.
- **Brand:** ask for the existing style guide (if any), 2–3 published pieces in the brand's strongest channel, plus 1 piece outside that channel (e.g., if they're known for blog posts, ask for a sales email or a LinkedIn post too). Mention any "this is a great example of our voice" reference posts the brand team uses internally.

After uploads, do a **redaction check**: if you see PII, sensitive personal content, or confidential brand material, flag it and ask whether to proceed or wait for redaction. Do not echo PII back in the voice.md.

If the user uploads only 1–2 samples or all from the same register, name the gap explicitly and ask for one more. Do not start Phase 3 below the floor. Sample insufficiency is the most common cause of bad voice docs.

When the floor is met, summarize what you have ("4 samples: 2 emails, 1 blog intro, 1 Slack thread") and ask permission to proceed.

---

## Phase 3 — Extract

Read all samples carefully and draft v1 of `voice.md`. The structure is fixed; see `references/voice-md-template.md` for the section list and field shapes.

Extraction rules — what patterns to pull from samples — are in `references/extraction-rules.md`. The short version:

- **Behavioral rules**, not adjectives. ("Never opens with 'I' on emails" beats "humble.")
- **Vocabulary tells**: words and phrases that appear repeatedly *and* feel idiosyncratic. Also the obvious bans (LLM-default words the samples never use: "leverage," "unlock," "delve," "navigate the landscape," "in today's fast-paced world," etc.).
- **Sentence rhythm**: average length, variance (short-long mixing), one-sentence-paragraph frequency.
- **Structural defaults**: how they open, how they close, how they handle lists, whether they use headers.
- **Idiosyncrasies**: em-dashes? Lowercase i? Specific punctuation habits? Recurring metaphors?
- **What it doesn't sound like**: the antipatterns that would break the voice if Claude defaulted to them.

When v1 is drafted, render it for the user to skim. Don't ask for line-by-line feedback yet — that comes in Phase 5 against actual outputs. Just confirm it looks roughly right and proceed.

---

## Phase 4 — Validate

Pick 3 message types — **different applications/channels**, e.g., email, Slack message, blog post intro, LinkedIn post, SMS, internal memo, FAQ answer, podcast show notes. The full menu and per-type format constraints are in `references/message-types.md`.

Use `AskUserQuestion` (multiSelect: true, max 3) to let the user pick. If they pick fewer than 3, fill the remaining slots from defaults that fit their Phase 1 "primary use" answer.

For each chosen message type, generate **a realistic short sample** using v1 voice.md, with a topic that's plausible for the user (ask if you don't know). Render the 3 outputs together so the user can compare across contexts.

Do not editorialize the outputs ("I tried to capture…"). Render them clean, the way the voice.md should produce them in the wild.

---

## Phase 5 — Refine (the loop)

This is where voice.md actually gets good. The mechanics are in `references/validation-and-refinement.md`. The shape:

For each of the 3 outputs, run a **per-output diagnostic** via `AskUserQuestion`. Ask the user what's off, with structured options like:
- *Too formal / too casual / about right*
- *Wrong rhythm — too uniform / too choppy / about right*
- *Wrong word choice — list specific offenders*
- *Missing my [habit] — e.g., em-dashes, specific opener, signature signoff*
- *Wrong structure — too long / too short / wrong opener*
- *Other* (free-text)

Cluster the answers across all 3 outputs into 2–4 concrete voice.md edits. Show the user the proposed diff (rule additions, vocabulary list updates, sounds-like / doesn't-sound-like additions). Get approval. Apply.

**Re-render all 3 outputs** with the updated voice.md and run the diagnostic again. Repeat until the user approves all 3.

**Definition of done:** the user explicitly says all 3 outputs sound like them / their brand. Not "good enough" — they have to actually approve. If after 3 refinement rounds the user still isn't happy, the most common cause is sample insufficiency — go back to Phase 2 and collect more, especially in the register that's failing.

---

## Final delivery

Save the final `voice.md` to `/Users/nikolassilva/Claude Cowork/c_Skill Creation/` (or the user's selected workspace folder) so they can open and copy it. Provide a `computer://` link.

Append a short **how to use this** footer to voice.md itself:
- Paste into a Claude Project's custom instructions, OR
- Paste at the top of a system prompt, OR
- Upload as context whenever you want voice to apply

Mention: voice degrades if the user's writing changes substantially (new role, new audience, new platform). Recommend re-running this skill every 6–12 months or when the user feels outputs starting to drift.

---

## What NOT to do

- Don't generate voice.md without samples. "Make me a voice doc that sounds like a friendly tech founder" is not a valid input — push back and ask for samples.
- Don't fill voice.md with adjectives. "Authentic, bold, human" is filler; cut it.
- Don't echo PII or confidential content from samples into voice.md.
- Don't skip the 3-output validation. Voice docs that look right in the abstract often break when applied; the validation is the test.
- Don't claim done before the user approves all 3 outputs.
- Don't keep editing voice.md mid-validation round. Render → diagnose → cluster → edit → re-render. One round per cycle.

## Reference files
- `references/sample-collection.md` — what to ask for, person vs brand, register diversity, redaction
- `references/voice-md-template.md` — output structure
- `references/extraction-rules.md` — what to pull from samples
- `references/validation-and-refinement.md` — Phase 4–5 mechanics, diagnostic question banks, edit-clustering protocol
- `references/message-types.md` — channel menu and per-channel format constraints
