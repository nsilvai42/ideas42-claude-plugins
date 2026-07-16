# Enterprise Boundary Gate

Use this whenever the **destination** is a Team or Enterprise (employer-governed) Claude
workspace — most importantly for the personal → enterprise migration in
`source-claude-personal.md`. This runs **before** the merge and review steps.

This is not the same as `privacy-review.md`. That step protects the user from exposing
sensitive excerpts *to you* during review. This gate decides whether a piece of context
should cross into an employer-controlled space **at all**. The two stack: boundary gate
first (what may cross), then privacy review (how to handle what crosses).

## The default: work- and project-specific only

The default is **opt-in by work relevance**, not opt-out by sensitivity. Bring over only
context that is about the user's work or specific projects. Everything else stays in the
personal account. When an item is ambiguous, leave it out and surface it as a single
question rather than importing it.

Tell the user this plainly before extraction, because it is the whole point of the
careful flow:

> We'll carry over only your work and project context. Anything personal stays in your
> personal account — once context is in a Team or Enterprise workspace, you can't
> selectively pull it back out, and on Enterprise an admin can see it.

## Carry over (work / project relevant)

- Role, team, and professional context tied to this job
- Projects, clients, workstreams, and their decisions, constraints, and deliverables
- Work tools, frameworks, methods, and internal terminology
- Communication and formatting preferences for work output
- Work writing voice / styles

## Leave behind (default-deny)

Drop these even if they look harmless — do not import, do not echo their specifics:

- Personal life, family, health, finances, relationships
- Side projects, job searching, or anything about other/previous employers
- Hobbies and personal interests unrelated to the role
- Third parties' personal details (names, contact info, private circumstances)
- Anything the user is unsure they want their employer to see

## Admin-visibility notice (state before import)

The destination is not private to the user. Surface the relevant point so they can make
an informed call — verify specifics against current Anthropic docs rather than asserting:

- **Enterprise:** the organization's Primary Owner can access full content of chats,
  projects, and uploaded files (via data export, audit logs, and the Compliance API),
  and org data-retention rules may apply to anything imported.
- **Team:** admins see usage **metadata** only, not message content — but the workspace
  is still org-managed and governed by org settings.
- Either way: content imported here may fall under different data-handling and training
  defaults than the personal account. Treat the move as one-directional and permanent.

## How to run the gate

1. After extraction (`source-claude-personal.md`), sort every collected item into
   **carry over**, **leave behind**, or **ask**.
2. Drop the leave-behind set silently except for a count (e.g., "set aside 6 personal
   items"). Do not restate their content.
3. For the **ask** set, batch a short yes/no checklist using the granularity rules in
   `review-ux.md` — one decision per item, default to *leave behind*.
4. Pass only the carry-over set forward to the high-level synthesis gate, merge, and
   review steps in the main working sequence.
5. In the final orientation, report how many items were intentionally left in the
   personal account so the user knows nothing personal silently crossed over.
