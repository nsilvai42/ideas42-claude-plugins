# Gathering and Interview Guide

How to collect project context with minimum burden on the user. Gather first, interview second, and never ask for what you already found. Render every structured question round per `intake-forms.md` (widget → AskUserQuestion → inline); this file owns the content, that file owns the shape.

## Gathering source order

Collect from whatever is available, asking permission before each new system. All access is read-only.

1. **Existing context files** — any CLAUDE.md, project-overview, status, kit, or memory files in the connected folder or uploads. If the project follows the ideas42 six-folder system, start in `01_Context/`.
2. **Asana** (or the team's task tracker) — project brief, milestones, owners, due dates.
3. **Google Drive** — the project folder: proposal, work plan, meeting-notes doc, canonical deliverables. Record file IDs as you go.
4. **Meeting notes and Slack** — recent decisions, open questions, stakeholder names.
5. **Miro / Notion** — boards and pages that count as live sources of record.

While gathering: log anything unconfirmed as a `[VERIFY]` candidate for the interview; if content looks like PII (student data, survey responses, personal contact details), stop and flag it rather than reading further; if you find credentials (API keys, passwords, tokens, Okta/SSO logins), flag their existence to the user and never reproduce or copy the value.

## Keeping the user oriented

Open every working message with a one-line orientation ("Step 3 of 6 — a few questions I couldn't answer from your files"). While gathering, narrate lightly at system granularity ("checked your Asana project and the Drive folder"), never file-by-file. Never expose internal step names, reference files, or template language — the user hears project language only.

## The announce-then-ask pattern

Open the interview with a short summary: "Here's what I found: …" (3–5 bullets, plain language, no internal jargon). Then: "Correct anything that's wrong, and I have a few questions I couldn't answer from the files." This makes the flow feel assisted rather than interrogative. Announce inferences before any form renders (see `intake-forms.md` — pills cannot pre-fill), and track what you announced so contradictions in the form return get surfaced, not silently overridden.

## Question bank

Ask only the items gathering could not answer. Batch into at most two rounds, rendered as Form B per `intake-forms.md`.

**Round 1 — identity and shape**
1. Project summary in two sentences, and the goal that defines success.
2. ideas42's role vs. the partner's role and decision rights.
3. Team members and roles; partner and funder names.
4. Current phase, active workstreams, and near-term steps.

**Round 2 — sources, guardrails, and upkeep**
5. The canonical work plan: which document, where it lives.
6. The running meeting-notes doc, if one exists.
7. Live systems and IDs not already captured: Drive folders, Asana project, Miro boards, Notion pages.
8. Hard guardrails: PII rules, claims to never make, review requirements before anything external.
9. Tone and brand: which brand skill applies (ideas42-brand, a partner brand skill), plus any voice rules.
10. The freshness owner — the named person who refreshes `status.md` weekly (and the meeting the refresh follows).

**The Drive-sync decision (always ask, in Round 2 or right after):**
Which one or two major canonical documents should be Drive-synced into project Files? Default recommendation: the work plan and the meeting-notes doc. State both caveats when asking: synced files are processed as text only (comments and suggestions are not read), and Claude's access mirrors each member's Google permissions — every project member needs Drive access to the synced files. Everything else stays a directory pointer, and synced files keep their directory ID as a fallback.

## Handling thin context

If there is little to gather and the user's answers are sparse: generate anyway with `[VERIFY]` placeholders, say plainly which sections are placeholders, and recommend the kit be treated as a draft until the freshness owner completes them. Never pad thin context with invented detail.
