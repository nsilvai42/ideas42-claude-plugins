# Message types — channel menu and per-channel format constraints

The menu Phase 4 picks from. Each entry has format constraints so the validator generates *shape-appropriate* outputs (a Slack message shouldn't have headers; a blog post shouldn't be 30 words).

## Table of contents
- The full menu
- Format constraints per type
- Picking 3 for validation
- When to add a custom type

## The full menu

Group by primary use to make the AskUserQuestion options easier to choose from.

### Short-form / messaging
- Email reply (existing thread)
- Email — cold or first-touch
- Slack message — to a channel
- Slack DM
- SMS / text message
- Group text
- Comment / reply on a post (LinkedIn, etc.)

### Long-form / publishing
- Blog post intro (first 2–3 paragraphs)
- Newsletter section (one segment of a larger newsletter)
- LinkedIn post (300–600 chars)
- Twitter/X thread opener
- Substack / Medium essay opener
- Op-ed lede
- Podcast show notes

### Internal communications
- Team status update
- Project announcement
- All-hands intro / kickoff
- FAQ answer
- Internal memo (1-page)
- Meeting recap

### Marketing / external
- Landing page hero copy
- Product email (announcement, drip)
- Sales follow-up email
- Case study opener
- Social ad copy
- Press release lede

### Operational
- Customer support reply
- Onboarding email
- Receipt / confirmation message (where voice still matters)

## Format constraints per type

When generating, apply the appropriate constraints. These are *format* constraints, not voice constraints — voice.md still drives the words.

| Type | Length | Format notes |
|---|---|---|
| Email reply | 50–200 words | Greet appropriately or skip if thread context allows; signoff appropriate to relationship |
| Email — cold | 60–150 words | Subject line + body; opener that earns the read |
| Slack channel msg | 1–4 sentences | No greeting, often no signoff; emoji optional |
| Slack DM | 1–3 sentences | Casual; replies often partial sentences |
| SMS | <160 chars | One sentence, often two; abbreviations OK if voice supports |
| Group text | 1–3 short sentences | Casual; reactions/emoji common |
| LinkedIn post | 300–600 chars | Hook in first line; line breaks for skim; 3–6 short paragraphs |
| Twitter/X thread opener | <280 chars | Standalone hook; sets up the thread |
| Blog intro | 80–200 words | Lede first; sets stakes/promise; 2–3 paragraphs |
| Newsletter section | 100–250 words | Section header + body; one main idea |
| Substack / Medium essay opener | 200–400 words | 4–6 paragraphs; opener that earns the click; optional pull-quote or scene-setting beat; pacing closer to magazine essay than blog post |
| Op-ed lede | 100–150 words | Strong claim or scene; argument-loaded opening |
| Podcast show notes | 100–200 words | Episode summary + 3–5 bullet highlights; guest credit |
| Team status update | 100–250 words | 3P (Progress, Plans, Problems) or similar structure if user uses it; bullets fine |
| Project announcement | 80–200 words | Lead with the news; what / why / what's next |
| All-hands intro | 100–250 words | Sets tone for meeting; warmer than memo |
| FAQ answer | 50–150 words | Question restated, then concise answer; no preamble |
| Internal memo | 250–500 words | Headed sections OK; clear structure |
| Meeting recap | 100–200 words | Decisions made, action items, open questions |
| Landing page hero | <40 words headline + <80 word subhead | Promise + clarification; no fluff |
| Product email | 80–200 words | Subject line; one CTA; benefits over features |
| Sales follow-up | 50–150 words | Specific reference to prior conversation; clear next step |
| Case study opener | 100–200 words | Customer + problem + outcome teased |
| Social ad copy | <150 chars body | Hook + one CTA |
| Press release lede | 50–100 words | Who/what/when/where in first sentence |
| Customer support reply | 60–200 words | Acknowledge → answer → next step; warmer than corporate-default |
| Onboarding email | 100–250 words | Welcome + first action + what's next |

## Picking 3 for validation

Aim for **format diversity**, not just topic diversity. Three outputs that are all 100–200-word emails won't stress voice.md the way an email + Slack message + blog intro will.

Default heuristics:
- One short (Slack, SMS, or short email)
- One medium (email, FAQ, LinkedIn post)
- One long (blog intro, memo, newsletter section)

If the user's primary use is narrow (e.g., they only ever write Slack messages), it's fine to validate 3 Slack messages with different topics or registers — but tell them voice.md will be Slack-tuned and may need adjustment if they apply it to long-form later.

## When to add a custom type

If the user names a channel that's not in the menu (e.g., "speeches I give at conferences," "lyrics," "court filings"), add it as the third validation type and treat their samples as the format reference. Document the custom type in voice.md so the same channel gets consistent treatment in future use.
