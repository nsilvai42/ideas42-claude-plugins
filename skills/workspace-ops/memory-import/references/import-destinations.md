# Import Destinations in Claude

Help the user decide where each confirmed item belongs.

## Claude Memory

Best for durable context that should help across conversations:

- role and professional context
- stable working style
- response preferences
- recurring tools and methods
- broad communication preferences
- durable standards or pet peeves

Keep Memory concise. Prefer short statements over long autobiographical paragraphs.

## Claude Projects

Best for bounded context:

- project briefs
- client or partner context
- active workstreams
- source documents
- project-specific terminology
- decisions, constraints, milestones, and deliverables

If a project setup skill is available, recommend it for building a full Claude Project after migration context is extracted.

## Both

Many migrations should split context:

- Memory: "how to work with me"
- Projects: "what this specific work is about"

## Do not import

Leave out:

- raw transcripts
- stale assumptions
- third-party personal details
- sensitive content the user has not explicitly chosen to keep
- anything the user has not reviewed

## Claude built-in memory import

If available, Claude's built-in memory import flow is useful for a quick first pass. The current flow is typically under **Settings > Capabilities > Memory > Start import**, or from an import card on the home screen. The user pastes exported memory/context text into Claude and can review memory edits afterward.

Do not claim Claude can directly pull data from another provider. The built-in flow relies on the user exporting or copying text from the previous assistant.

## Team / Enterprise destinations (employer-governed)

When importing into a Team or Enterprise workspace, a few things differ from a personal
account. Verify specifics against current Anthropic docs rather than asserting them:

- **Memory and Projects may be admin-configured.** An org may set, restrict, or manage
  Memory and Project behavior. The user may have less individual control than in a
  personal account.
- **Retention may be enforced.** Enterprise admins can set custom data-retention periods;
  imported chats, projects, and artifacts can be deleted when retention expires. Don't
  treat the workspace as permanent personal storage.
- **Visibility and training defaults differ.** On Enterprise, the Primary Owner can read
  full content (exports, audit logs, Compliance API); on Team, admins see metadata only.
  Data-handling and training defaults may differ from the personal account. Surface this
  before import — see `enterprise-boundary.md`.
- **A native account migration may exist.** For a personal → Enterprise move, an
  admin-initiated domain claim can merge the personal account wholesale. Prefer it for a
  full migration; use this skill's flow for a curated, work-only subset. See
  `source-claude-personal.md`.
