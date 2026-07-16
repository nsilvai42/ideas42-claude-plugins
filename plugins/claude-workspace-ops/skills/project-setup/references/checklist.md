# Internal Checklist — items to fill before delivering the setup package

**Purpose:** The full list of items the skill needs to fill in to produce a good Project setup, plus where to look for each.
**Use when:** Round 2 of the project-setup flow. Read this once at session start; track each item as filled / empty in working memory.
**Not for:** A user-facing form. The user only ever sees items still empty after Round 2 (and even then, grouped into a tight form, not a long survey).

## Sources, in priority order

For every checklist item, try the highest-priority source first. Do not ask the user a question that any of these sources can answer.

1. **The user's first message** — often carries project name, type, purpose, even tone preference
2. **Uploaded files the user authorized in Round 1's context-method selection** — read with the file tool
3. **Connected tools the user authorized in Round 1's context-method selection** — prefer `enterprise-search:search` if installed (one query across all connectors); otherwise call individual connector tools
4. **Prior chat context** — anything from earlier turns

If two sources disagree (the proposal says one team, Asana shows another), surface the conflict in the Step 3 review table — don't pick silently.

## Connector allowlist for project context

Filter the visible connector list before listing connectors as a context-method option in Round 1 or pulling from them in Round 2. The point is to focus on sources that actually carry project context, and to avoid embarrassing the user with a 15-connector dump that includes dev tools, design tools, etc. Real-world failure that drove this rule: a claude.ai test run rendered every connected MCP — Slack, Gmail, Calendar, Drive, Notion, Asana, Canva, Figma, Miro, Cloudflare, Supabase, Netlify, Apple Notes, NotebookLM, Fireflies — as one comma-separated line. Unscannable.

### Show (org-context sources)

These are the connectors `enterprise-search:search` treats as common context sources, plus standard project trackers:

- **Slack** — chat platform
- **Gmail** — email
- **Google Drive** — cloud storage
- **Box** — sensitive / final docs
- **Asana** — project tracking
- **Notion** — knowledge base
- **Google Calendar** — meetings, events
- **Salesforce** — CRM
- **Confluence** — wikis, documentation
- **Linear** — issue tracking
- **Jira** — issue tracking

Add to this list as new org-context connectors come online. Principle: would Claude actually pull project context — briefs, decision memos, kickoff decks, partner email, status updates — from this source?

### Suppress (not org-context)

Don't list these in Round 1's connector option. They're useful tools, just not project-context sources for setup.

- **Cloudflare, Supabase, Netlify** — dev / infra
- **Figma, Canva, Miro** — design / whiteboard
- **NotebookLM, Fireflies** — AI tools (Fireflies is meeting-adjacent but the meeting context is usually duplicated in Calendar + Slack, where it's already searchable)
- **Zoom** — meetings

If you're unsure whether a new connector is org-context or not, ask: would I expect to find a project brief, decision memo, kickoff deck, partner email, or status update in this tool? If yes, allowlist; if no, suppress.

### Cap inline display

When listing the filtered allowlist in Round 1's inline-prose template (or in any in-chat reference to available connectors), cap at 8 displayed; if more, append "+N more". This keeps the first impression scannable.

## Items the skill needs to fill

### Project metadata (3 items)

| Item | Field type | Pre-fill from |
|---|---|---|
| Type — reusable tool or workflow / time-bound engagement / ongoing program or operation / reference or knowledge hub / personal exploration or tracker / other | single select; **captured in Round 1**, drives downstream branching | Asana project name; proposal or RFP title; uploaded contract; user's first message |
| Stage — just starting or setting up / actively in progress / in review or wrap-up / recurring or always-on / other | single select; type-agnostic; **captured in Round 1** | Asana milestones; proposal timeline; deliverable status |
| Sensitivity / compliance — vulnerable population / IRB / DSA / partner confidentiality / non-public data / none | multi-select | Brief content; uploaded DSA or IRB approval; partner name |

### Inputs to the instructions block (6 items)

These map directly to the `<role>` / `<context>` / `<guidelines_do>` / `<guidelines_do_not>` / `<format>` / `<when_unsure>` XML-tagged sections of the assembled instructions block. See `references/instruction-template.md`.

| Item | What it produces | Pre-fill from |
|---|---|---|
| Role — what is Claude in this project, who's the audience | `<role>` sentence | User's role + team; project type; audience cues in brief |
| Context — what the project is for, who's involved, what's at stake | `<context>` (2–3 sentences) | Project brief; proposal; kickoff deck |
| DO behaviors with intent (3–5) | `<guidelines_do>` | Style guides; partner deliverable patterns; user's stated needs |
| DO NOT behaviors with intent (3–5) | `<guidelines_do_not>` | Real incidents named in chat or files; partner constraints; user's stated frustrations |
| Format / tone — tone, structure, length defaults | `<format>` line | Brand guidelines; partner voice samples; deliverable types in brief |
| When unsure — escalation rule | `<when_unsure>` line | Sensitivity level (high-stakes → "ask first" default); user preference |

Every DO and DO NOT bullet must carry a "because." Intent is what makes them generalize at edge cases.

### Inputs to the knowledge files (8 items)

These map to `project-overview.md` and `status.md`. Templates in `references/standard-files.md`.

| Item | Goes in | Pre-fill from |
|---|---|---|
| Project name + 1-line summary | overview | Asana project; proposal; brief title |
| Team and partner roles | overview | Asana members; meeting notes; brief |
| Goal / success criteria | overview | Proposal; kickoff deck; theory of change if uploaded |
| Workstreams | overview | Asana sections; proposal scope; deliverable list |
| Key terms and acronyms | overview | Recurring jargon across uploads (any term used 3+ times without expansion is a candidate) |
| Connected resources (links) | overview | The connector list itself — Asana / Drive / Slack / Notion URLs |
| Current phase + recent decisions | status | Recent Asana activity; meeting notes; first-message context |
| Update cadence | status header; default `after major decisions` | User preference |

### Audience and work patterns (2 items, shape FORMAT)

These don't have a dedicated output slot but they sharpen the FORMAT line and the project-overview audience section.

| Item | Field type | Pre-fill from |
|---|---|---|
| Primary users / audience — internal team / partner / funder / external / personal | multi-select | Partner field on Asana; recipient pattern in deliverables |
| Common work patterns — drafting / research / data analysis / PM / brainstorming / decks / review / stakeholder comms | multi-select; pick 2–4 | Deliverable types in brief; Asana task verbs; meeting notes |

If the user picks 5+ work patterns, ask in chat to narrow to top 3 — instructions optimized for everything optimize for nothing.

## Filling rule of thumb

Before adding any item to the user-facing question list, run through:

1. Did the user reference it in their first message?
2. Is it in an uploaded file? (Read the file before asking.)
3. Is it accessible via a connector? (Search before asking — narrow queries with the Round 1 purpose textarea as a scope token; if it's empty, confirm scope on the first-pass results before deepening.)
4. Did the user mention it in an earlier chat turn?

Only after all four return nothing does the item go to Round 2's project-specific question form.

## When the user picked only "Ask me questions in chat" in Round 1 Q4

This is the new shape of the old "sparse path" — instead of being inferred from sparseness, it's now an explicit user choice. When the user picked only chat (no connectors, no uploads), Round 2 leans on a leaner set of questions targeted at filling the highest-leverage gaps:

1. **What's this project for?** (one or two sentences — covers role + context, may already be in the Round 1 purpose textarea)
2. **What kind of work happens here most?** (multi-select: drafting / data analysis / research / brainstorming / PM / something else — covers FORMAT inputs)
3. **What tone or style?** (single select: ideas42 brand / partner / casual / formal / depends — covers FORMAT)

Then deliver the package with `[fill in: …]` placeholders for everything else, and tell the user explicitly: "Come back after 3–5 chats and we'll fill in the DO / DO-NOT rules using what's actually happened in your real chats."

If Round 1 Q4 returns empty (no method selected), default to chat-questions automatically — never gather silently.

## When you've filled enough to draft

You don't need every item filled before showing the user a draft. Minimum bar to enter the Step 3 review table without it feeling like a long survey:

- All 3 project metadata items have either a value or a confident inference (note: Type and Stage are captured directly in Round 1)
- ROLE and CONTEXT have draft sentences
- Project name + summary + at least one of (team / goal / workstreams) is filled
- Update cadence has a default

Below that bar, items stay in Round 2 as gap-fill questions. Above the bar, items skip to the Step 3 review table — *unless* the item is high-stakes (next section).

## High-stakes inferences need confirmation

Most checklist items follow the standard split: filled values go to the Step 3 review table, empty items go to Round 2's project-specific question form. But three items get an extra check — they're high-stakes enough that a wrong silent inference can corrupt the project's instructions for every chat going forward:

1. **Sensitivity / compliance** — wrongly inferring "no special sensitivity" when there's a DSA in force, or vice versa, sets the wrong default for what Claude can repeat in deliverables.
2. **Audience** — getting "internal team" vs. "partner / client" wrong rewrites the entire tone of every output.
3. **DO-NOT rules** — guessing at guardrails the user didn't explicitly state risks both false guardrails (annoying) and silent omissions (dangerous).

For these three, **even if you have a confident guess from a source, surface it as a Round 2 question** with the inference pre-announced — don't let it ride silently to the Step 3 review table. The form gives the user a deliberate moment to confirm; a row note in the table is too easy to skim past. Examples:

- *"I'd guess your Sensitivity is 'partner confidentiality' and 'DSA constraints in force' based on the brief and the draft DSA — confirm or adjust:"* → Round 2 form, with the announced inference held in working memory so Step 3 review can flag any mismatch.
- *"From the brief, your audience looks like external partner and funder. Is that the primary set, or am I missing one?"* → Round 2 follow-up.

A second pattern worth flagging here: **default vs. illustrative example**. When a partner / org / framework name shows up in uploaded material, surface it explicitly as a Step 3 review row note: *"Bottom Line shows up in your uploads — is that the default org for this auditor, or just an example?"* Silently encoding an example as the default is a real, costly misalignment (the deliverable ships with a baked-in assumption the user never confirmed).

For everything else (Type, Stage, Project name, Team, Goal, Workstreams, Update cadence) — if you have a value, send it to the Step 3 review table. The user can correct it there.
