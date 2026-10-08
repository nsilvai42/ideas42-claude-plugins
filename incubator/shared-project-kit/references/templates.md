# Kit Templates

## Table of Contents

1. Custom instructions (paste into the project field)
2. `project_overview.md`
3. `status.md`
4. `directory.md`
5. Filling rules

Self-contained copies of the four kit templates (canonical pattern: the SBNC kit and `Project Management/SHARED_PROJECT_KIT_SETUP.md`). Replace every bracketed prompt with confirmed content or a `[VERIFY]` placeholder.

## 1. Custom instructions (paste into the project field)

```
<project>
[Project or engagement name]
[One-paragraph description of the work]
Team: [names and roles]
</project>

<role>
[ideas42's role — e.g., behavioral design and evaluation partner]
[The partner's role and decision rights]
</role>

<tone>
Use the [brand skill name] skill for deliverables when it is enabled and relevant. If the skill is unavailable, say so outside the deliverable and instruct the user to reach out to [owner].
</tone>

<always>
- Be honest about the certainty of your claims, name material assumptions, and distinguish between evidence, interpretation, inference, and recommendation.
- Where user statements conflict with project knowledge, identify the discrepancy and recommend specific updated language before relying on it.
- When guidance is vague and materially changes your output, ask clarifying questions using an interactive visual survey (use visualize first, ask_user_input as fallback) instead of relying on assumptions.
- Prioritize web search to verify claims that change over time; rely on model knowledge only for durable concepts.
</always>

<never>
Overstate effects, imply causation from correlational or directional evidence, or remove material caveats when summarizing results. [Add project-specific hard guardrails — PII rules, claims to never make, external-review requirements.]
</never>

<source_hierarchy>
Use sources in this order:
1. User's current request and direct factual corrections.
2. Project knowledge (see project_knowledge).
3. Tool calls to the live sources of record linked in directory.md.
4. Current official, reputable primary external sources for time-sensitive claims.
5. Model knowledge for durable general concepts.
</source_hierarchy>

<project_knowledge>
Files:
- project_overview.md — goals, phases, people, durable decisions. Read for project context or historical framing.
- status.md — current focus, next steps, recent decisions, open questions. Read for anything about current work.
- [Work plan] and [Meeting notes] — Drive-synced into project Files and kept live; read them there by default (no connector call needed).
- directory.md — external links and tool IDs. Read before connector calls; use an ID only to reach a source that is not Drive-synced into Files.
How to use:
- status.md wins on current project state when files conflict.
- If context is missing, stale, or contradictory, identify the exact information that may need updating and suggest replacement language.
- Remind users to update project context after finishing substantial chunks of work or deliverables.
</project_knowledge>
```

## 2. `project_overview.md`

```
**What this file contains:** Static reference for [engagement] — what the program and project are, our workstreams, where files and systems live, and stakeholders. Facts here should rarely change. For current state, read status.md.
**Use it when:** You need context about the project beyond current active work.
**Last updated:** [date] by [owner]

## Project Summary
[Two or three paragraphs: who the partner is, what the project does, why it matters]

## Project Goals
[The outcomes that define success]

## Project Phases
[Phase — dates — status — key outputs, one subsection per phase]

## People
### ideas42
[Name (role, decision rights)]
### Partner
[Name (role, decision rights, working preferences worth knowing)]
### Vendors and Others
[Name (what they own)]
```

## 3. `status.md`

```
**What this file contains:** The live state of [engagement] — where we are by workstream, immediate next steps, recent decisions, and open questions. When this file conflicts with any other, this one is right unless otherwise noted.
**Use it when:** Answering any question about current or active work.
**Last updated:** [date] by [owner]
**Refresh trigger:** Weekly, after [standing meeting]

## Active flags
[Sensitivity, credential, or time-sensitive items needing action — e.g., "credentials found in [file]; rotate and remove before sharing." Note the flag and the action, never the sensitive value itself. Remove once resolved.]

## Where We Are (overwrite each update)
[One bullet per workstream: state, owner, near-term direction]

## Near-Term Steps
[Action — owner — timing]

## Recent Decisions
[Date — decision — rationale]

## Open Questions
[Question — owner — what would resolve it]

## Changelog (one line per update, newest first)
[Date: what changed]
```

## 4. `directory.md`

```
**What this file contains:** Tool-call directory for [engagement] — the minimal IDs Claude needs to find live artifacts via connectors.
**Use it when:** You need an ID for a connector call to locate the live source of record.
**Last updated:** [date] by [owner]
**Refresh trigger:** whenever a canonical artifact is created or an ID changes

**Note:** [Work plan] and [Meeting notes doc] are Drive-synced into the shared project's Files (live); read them from Files by default and use the IDs below only as a fallback.

## Systems
| System | Item | ID |
|---|---|---|
| Google Drive | [Root folder] | [ID] |
| Google Drive | [Meeting Notes doc] ↳ *Drive-synced into project Files — read there by default* | [ID] |
| Asana | [Project] | [GID] |

## Boards and Pages
| System | Item | ID |
|---|---|---|
| Miro | [Board] | [ID] |
| Notion | [Page] | [link] |

## Key Files (Google Drive)
| Doc | Type | ID |
|---|---|---|
| [Work plan] ↳ *Drive-synced into project Files — read there by default* | Sheet | [ID] |
| [Canonical deliverable] | Doc | [ID] |
```

## 5. Filling rules

- Name each output file after the project where useful (e.g., `sbnc_directory.md`) but keep the four-part anatomy exactly.
- Drop template sections that genuinely do not apply (e.g., no vendors); never leave a bracketed prompt in a delivered file — fill it or mark it `[VERIFY]`.
- Keep the header block ("What this file contains / Use it when / Last updated / Refresh trigger") on all three knowledge files — it is how future chats route.
- Surface any PII, credential, or time-sensitive issue found while gathering in `status.md` → **Active flags**, recording the flag and the action needed, never the value.
- If the kit will be shared beyond the project team, offer to redact connector IDs.
