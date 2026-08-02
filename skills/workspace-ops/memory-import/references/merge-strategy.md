# Merge Strategy

How to slot extracted context into existing Claude context before review. The default for memory-import is to merge first and review only what bounces — not to ask the user about every item.

## Inventory step

Before any merge, list what Claude already has access to:

- **Claude Memory** — durable facts, working preferences, role context. Carries across conversations.
- **Project context** — bounded workstream details inside a specific Claude Project.
- **Project-level memory file** — if the working directory has one (e.g., `MEMORY.md`, `CLAUDE.md`), include its entries in the inventory.

If existing Memory isn't directly visible, ask the user to paste or summarize it. Don't merge blind.

## Compatibility detection

An incoming item is **compatible** with an existing item when:

- They cover the same topic, and
- The incoming item adds detail without contradicting the existing one, or
- The incoming item is a more recent version of a fact whose old value isn't load-bearing.

Compatible items merge automatically — no user touch required.

## Conflict detection

An incoming item is a **conflict** when it contradicts something already in Claude's context. Examples:

- Source says "prefers concise responses"; existing memory says "prefers comprehensive."
- Source says role is X; existing memory says role is Y.

Subtle disagreements default to keeping existing — don't escalate noise. Only flag clear contradictions.

Conflicts go into the bounced set for user review.

## No existing match

Items with no counterpart in existing context aren't conflicts; they're net-new additions. Default is "add as new" with a one-tap confirm. Sensitive or low-confidence items still require explicit review (see source-confidence rules below).

## Source-confidence rules

When the source labeled items by confidence (see `extraction-prompts.md`):

- `saved memory`, `custom instructions`, `saved/personalized context`, `Gem/project context` → auto-confirm. Do not escalate.
- `inferred from examples`, `uncertain` → escalate to the bounced-set review.

## Superseded record format

When an auto-merge updates an existing record, leave a one-line note on the prior version inline:

```
- [original record content]  (superseded 2026-05-08 by import from ChatGPT)
```

Don't create a separate audit log file. The inline note is enough to make the change traceable.

## Output to user

After the merge runs, report counts:

- N items auto-merged (compatible)
- M items added as new (no existing match, low-risk)
- K items in the bounced set requiring review

Then hand the bounced set to the review surface (`review-ux.md`).
