# Intake Form Rendering

**Purpose:** How to render the structured question rounds — Form A (Step 1 scope) and Form B (Step 3 interview gaps). Content comes from `interview-guide.md`; this file only specifies render mode and field shape.

## Table of Contents

1. Render mode, in order of preference
2. Pre-fill and announced inferences
3. Form A — scope (Step 1)
4. Form B — interview gaps (Step 3)
5. Inline-prose paths
6. Parsing form returns

## 1. Render mode, in order of preference

The same three-tier fallback applies to both forms. The inline-prose path (typical on claude.ai without the widget MCP) is a first-class render, not a degraded one — it must mirror the form question-for-question. Do not redesign for inline.

1. **Form widget (preferred).** If `mcp__visualize__show_widget` is available, read the elicitation schema first (`mcp__visualize__read_me({ modules: ["elicitation"] })`), then render one form per round.
2. **AskUserQuestion.** One block per logical group; mirror the form's options and inline definitions. At most 4 questions per call; prefer multi-select where choices are not exclusive.
3. **Inline prose.** Numbered questions in chat mirroring the form groups exactly, defaults stated, unfamiliar terms defined inline.

## 2. Pre-fill and announced inferences

- **Pills do not pre-fill.** For inferred values that would have been a pre-press, announce them in chat **before** rendering the form ("From your folder I'd guess Dan owns freshness and the work plan is the Phase 2 sheet — confirm or adjust below"), then let the user actively select. Hold the announced-inference list in working memory: if the form return contradicts an announced inference, surface the conflict — never silently encode the override.
- **Native text inputs do pre-fill.** Textareas and text/date inputs accept initial values — use them aggressively for anything gathered (project name, partner names, work-plan location). An empty field when material exists is a UX miss.

## 3. Form A — scope (Step 1)

Form A adapts to whether sources are already connected.

- **Connected session (folder or connectors visible):** gather what's visible first, then open Form A with a one-line "here's what I can see — confirm or adjust" preamble. Omit Group 2 for anything already visible; pre-fill Group 1 and the freshness owner from what you found (native text inputs pre-fill — see §2). Form A becomes a confirm-and-fill-gaps round, not a cold ask.
- **No-context session (nothing connected):** run Form A cold — no preamble, since there is nothing to show yet.

Groups (include only those not already answered by the read):

- **Group 1 — Project** (`textarea`, pre-fill from the read or the user's message): "Which project or engagement is this kit for?"
- **Group 2 — What exists already** (multi-select pills; **omit when a folder/connectors are visible**): connected folder with context files / an existing kit to check or refresh *(routes to Phase 2)* / live systems I can pull from (Drive, Asana, Miro, Notion) / not much — mostly in my head.
- **Group 3 — Freshness owner** (`text`, optional, pre-fill if the read named an owner): "Who will keep the kit current (weekly status refresh)? Leave blank if undecided."

If Group 2 (or the read) shows "not much," expect the interview to carry the load (see thin-context handling in `interview-guide.md`) — do not re-ask it later. If the read reveals an existing kit, confirm Phase 1 vs. Phase 2 before building.

## 4. Form B — interview gaps (Step 3)

Rendered **after** gathering, immediately after the announce-then-ask summary. Build the form dynamically: include only question-bank items (from `interview-guide.md`) that gathering could not answer, in bank order, at most two rounds. Field shapes:

- Roles, phases, guardrails, tone: multi-select pills with an **Other / type below** escape; pair each pills group with an optional textarea.
- Names, documents, IDs: text inputs or textareas, pre-filled with gathered candidates.
- **Drive-sync decision (always present, last group):** multi-select pills listing the discovered candidate documents (default recommendation pressed into the copy, not the pills: "I recommend the work plan and the meeting-notes doc"). Form copy must carry both caveats verbatim-level clarity: *synced files are read as text only — comments and suggestions aren't seen; Claude mirrors each member's Google permissions — every project member needs Drive access to the synced files.*

Copy above Form B: one line of orientation plus the batching promise — "These are the only questions; everything else came from your files."

## 5. Inline-prose paths

Mirror each form group as a numbered question with its options as bullets. State the same defaults, definitions, and caveats. For Form B in inline mode, still cap at two messages of questions; group by round, not one question per message.

## 6. Parsing form returns

- The elicitation shell drops skipped fields entirely from the return string — handle "key absent" and "key present but empty" the same way (treat as blank, do not re-ask unless the item is load-bearing; load-bearing blanks become `[VERIFY]`).
- No pills pressed on the Drive-sync group = adopt the stated recommendation after one confirmation sentence, not silently.
- If a group returns contradictory picks (e.g., "not much exists" plus "connected folder"), ask one targeted follow-up rather than guessing.
