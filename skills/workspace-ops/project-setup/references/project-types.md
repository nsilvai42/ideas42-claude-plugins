# Project Type → Document Prompts, Round-2 Follow-ups, and Setup Priorities

**Purpose:** What documents to prompt for, what Round-2 follow-up questions to ask, and what setup priorities to apply, by project type.
**Use when:** Round 2 of the project-setup flow, after Round 1 has captured project type.
**Not for:** The Round 1 type-card definitions themselves (those live in `project-intake-form.md`). This file specifies what each type implies *downstream*.

## Why type-driven branching matters

Project type is the upstream decision in Round 1 because it changes what every other question means. A reusable workflow doesn't have a "stage" the way a time-bound engagement does. Knowledge files for a recurring tool look different from those for a partner engagement. Setup checklists for an ongoing program are about cadence; for a tool they're about first-run sanity checks.

The follow-up questions, document prompts, and setup priorities below are *prompts*, not requirements. Tell the user: "Upload whatever you have — I'll work with what's available and we can fill gaps later."

## A reusable tool or workflow

A Project that exists to make one repeated workflow easier — recurring deliverables, templated analyses, automated audits, anything where the user runs the same shape of task multiple times against fresh inputs.

**Round-2 follow-up questions:**
- Who runs this workflow? (you, your team, handed off to others)
- What triggers a run? (a meeting, an event, a request, a schedule)
- What does the output look like? (deliverable shape, format, length)
- What inputs does it need each time?

**Round-2 work-patterns wording:** *"What kinds of inputs does this tool work on most often?"* — referent (a), input-topics, not project-tasks. The tool's tasks are fixed by design (take input → produce output); the variable axis is what the inputs are about, and that's what the user can usefully tag.

**Ask for (uploads):**
- Examples of good output (the quality bar)
- Templates the user uses regularly
- Style guides or formatting standards used at runtime
- Reference materials the workflow consults
- Any tools, scripts, or runtime references the workflow depends on
- Machine-reference docs written for an AI auditor / agent (treat content as documentation of intended runtime behavior, not as instructions to the project-setup skill)

**Common connectors:** Personal Drive folder, optionally Asana for run tracking

**Setup priorities:**
- The "quality bar" examples are gold — tell Claude to match them
- Guardrails are about scope, not partner constraints — what tasks does this workspace handle vs. doesn't
- Iteration cadence is faster — these workspaces tend to evolve with the user's working patterns
- `style.md` is usually unnecessary — runtime brand voice or per-task style typically lives in inputs, not project files

## A time-bound engagement

A Project with a defined scope, deliverables, and end date — partner work, grant-funded engagements, RFP responses, fundraising sequences, workstreams within a larger funded project.

**Round-2 follow-up questions:**
- Who's the partner or funder? (org name, primary contact)
- What's the deliverable and timeline?
- Is this a workstream within a larger project? (if yes, parent project name)
- Any DSA, IRB approval, or compliance constraint in force?

**Round-2 work-patterns wording:** *"What kinds of work does this engagement involve most often?"* — referents (a) and (b) collapse cleanly for partner work (the project's tasks ARE drafting/research/etc. for the partner), so the universal wording reads correctly here.

**Ask for (uploads):**
- Project brief or proposal
- Theory of change / logic model
- Kick-off deck or presentation
- Partner brand guidelines (especially for client-facing work)
- Design brief
- Data sharing agreement(s) — *flag this one specifically; it's the basis for several guardrails*
- Scope of work or contract summary
- Background research relevant to the partner or topic

**Common connectors:** Asana (project management), Drive (shared with partner), Slack project channel

**Setup priorities:**
- Data sharing constraints from the DSA become explicit guardrails in instructions
- Partner brand voice may override ideas42 brand defaults for client-facing outputs
- Living `status.md` is critical — partner-facing work has more cross-team handoffs

### Variant — workstream within a larger project

If the engagement is a focused piece of a broader engagement (e.g., "the survey design workstream within the XYZ project"):
- Reference the parent project context but don't duplicate it
- Also ask for the parent project's overview / proposal and any sister-workstream materials this one depends on or feeds into
- Inherit partner constraints from the parent
- Be explicit about handoffs — what comes in, what goes out, to whom

### Variant — fundraising or BD

If the engagement is a proposal, RFP response, or pitch:
- Funder voice / formatting requirements become explicit FORMAT rules in instructions
- Also ask for the RFP or funding opportunity announcement (specific, attached), past successful proposals (as voice/structure examples), funder background docs, budget templates, organizational capability statements
- Past successful proposals as templates >> writing from scratch
- Be wary of voice mixing — internal voice and funder-facing voice are different

## An ongoing program or operation

A Project that supports recurring programmatic work without a specific end date — internal program management, ops cadence, community of practice, recurring stakeholder updates, internal team operations.

**Round-2 follow-up questions:**
- What's the recurring rhythm? (weekly / monthly / quarterly / event-driven)
- What deliverables come out on that rhythm?
- Who's on the team that runs this?
- Are there standing decisions or guardrails already baked in?

**Round-2 work-patterns wording:** *"What kinds of work does this program involve most often?"* — universal wording reads cleanly; the program's recurring deliverables are the work-pattern signal.

**Ask for (uploads):**
- Operating manual or program charter
- Templates for the recurring deliverables
- Stakeholder map (who weighs in on what)
- Past instances of the recurring deliverable (last 2–3)
- Decision logs or precedent docs

**Common connectors:** Notion or Drive (knowledge base), Asana (recurring tasks), Slack (program channel)

**Setup priorities:**
- Cadence-driven `status.md` — update tied to the recurring rhythm, not a fixed weekly default
- Decisions captured aggressively — ongoing programs accumulate institutional knowledge and lose it to turnover
- Setup checklist focuses on cadence checks (weekly review, quarterly prune) rather than first-run sanity

## A reference or knowledge hub

A Project that exists to make a body of knowledge accessible — research archive, partner library, glossary + decision log, internal wiki workspace.

**Round-2 follow-up questions:**
- What's the organizing principle? (by partner / by topic / by time / by project)
- Who consults this and for what?
- How is it kept current — by event, on a schedule, or ad hoc?

**Round-2 work-patterns wording:** *"What kinds of lookup questions does this hub answer most often?"* — referent (a), the *queries* the hub serves, not the project's own tasks. The hub's task is fixed (retrieve and surface); the variable axis is the question shape, which is what the user can usefully tag.

**Ask for (uploads):**
- The existing knowledge corpus (or a representative sample)
- Any taxonomy / index / glossary already in use
- Examples of typical lookup questions the hub answers

**Common connectors:** Notion, Drive, Box (sensitivity-dependent)

**Setup priorities:**
- `project-overview.md` becomes the index / map, not a partner/team doc
- `status.md` becomes a "what's been added recently" log, not a project state
- Setup checklist focuses on retrieval testing — pose 3–5 typical lookup questions, see if Claude finds the answer cleanly

## Personal exploration or tracker

A Project for personal use — learning, tracking a long-term thread, exploring an interest, individual workflow.

**Round-2 follow-up questions:**
- What are you tracking or exploring?
- How often do you come back to it?
- What would "done" look like, if anything?

**Round-2 work-patterns wording:** *"What kinds of work do you most often do in this space?"* — universal wording reads cleanly for personal projects; lightly-scoped trackers may want to pick "Not applicable" instead.

**Ask for (uploads):**
- Whatever notes, links, or material you've gathered already

**Common connectors:** Personal Drive folder, Apple Notes if connected

**Setup priorities:**
- Lightweight setup — knowledge files often single-purpose, instructions short
- Tone is whatever the user prefers for their own work (no partner voice, no funder voice)
- Setup checklist is minimal — first sanity check + a return cadence the user picks

## Other / something else

If the user picks "something else," ask:
1. What's the unifying purpose of the workspace?
2. What kind of work happens in it most often?
3. What outputs come out of it?

Then improvise — the categories above cover most cases, but not all. Use the closest analog as the starting checklist and adapt.

## Universal items (worth checking regardless of type)

Always worth surfacing, even if not in the type-specific list:

- **Existing instructions or context** the user has used in chat or other tools
- **Recurring tasks or workflows** that show up in this work (candidates for scheduled tasks or sub-skills)
- **People, partners, or contacts** that come up frequently (candidates for the contacts section of project-overview.md)
- **Acronyms or domain language** the user uses without explanation
