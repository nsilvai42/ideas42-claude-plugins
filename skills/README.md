# Skills (source of truth)

These are the individual ideas42 skills, grouped by theme. **This folder is the source of truth** — edit skills here, not in `plugins/`.

Skills reach more surfaces than plugins: they work in Claude Code, Cowork, **claude.ai web chat**, the API/Agent SDK, and Slack. Plugins (the marketplace) only reach the Claude Code family (CLI + Cowork). So share the individual skill for broad, low-friction reach; offer the plugin for people who want one-click install and versioned updates.

## Themes

| Theme | Skills | Shipped in plugin |
|-------|--------|-------------------|
| `brand/` | bottom-line-brand, calbright-brand, ideas42-brand, sbnc-brand, year-up-brand | `brand-systems` |
| `communications/` | i42-copy-editor, internal-communications, learning-coach | `ideas42-comms` |
| `data-analysis/` | data-cleaning, describe-sample, quick-csv-summary, verify-data-analysis, visualize | `quantitative-analysis` |
| `workspace-ops/` | project-setup, file-organizer, memory-import, memory-consolidation, schedule, setup-cowork, create-plugin, skill-lookup, review-console, review-council | `claude-ops` |
| `qualitative-research/` | journey-mapping | `qualitative-research` |

## Sharing an individual skill

Each `skills/<theme>/<skill>/` directory is a complete, self-contained skill (SKILL.md plus any references/scripts/assets). To share one:

- **claude.ai web chat / Cowork:** upload or enable it via the Skills / capabilities UI.
- **Claude Code (a repo):** copy the skill directory into that repo's `.claude/skills/`.

## Keeping plugins in sync

The marketplace plugins under `../plugins/` are wrappers: each plugin's `skills/` subdirectory is **generated** from a theme folder here. After editing any skill, regenerate the wrappers:

```bash
bash scripts/sync-skills-to-plugins.sh
```

Never edit `plugins/<plugin>/skills/` directly — the next sync overwrites it. The mapping (theme → plugin) lives at the top of that script.
