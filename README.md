# ideas42 Claude Plugins

A Claude plugin marketplace of **ideas42-specific** plugins — the skills that encode ideas42 brand, voice, methodology, and workspace conventions, which you can't get anywhere else. Generic craft skills (data, design, research, connector automation, deliverables) are **not** re-hosted here: they come from Anthropic's Cowork skill bundle and community packs, and mirroring them would just add drift and maintenance with no ideas42 value. See [What's not here](#whats-not-here-and-why).

Most plugins serve multiple stages of the IDEAS methodology (Identification, Diagnosis, Engineer, Assess, Scale & Sustain). Stage-specific methodology plugins (behavioral-diagnosis, intervention-design, experimental-design, scale-sustain) are planned — see [RECOMMENDATIONS.md](RECOMMENDATIONS.md).

## Install (individuals)

In Claude Code or Cowork:

```
/plugin marketplace add nsilvai42/ideas42-claude-plugins
/plugin install brand-systems@ideas42-claude-plugins
```

These plugins are meant to be **customized on install** — in Cowork, run the plugin customizer after installing to swap in your own tools, channels, and workspace values.

## Distribute org-wide (Team/Enterprise admins)

Admins can add this repo as an organization plugin marketplace and choose which plugins members see, install themselves, or get auto-installed: [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).

## Plugins (5)

| Plugin | What makes it ideas42's | Skills |
|--------|-------------------------|--------|
| **brand-systems** | Partner brand guidelines — pure ideas42 IP | ideas42, SBNC, Bottom Line, Calbright, Year Up brand guidelines |
| **ideas42-comms** | Writing in the ideas42 voice | i42-copy-editor, internal-communications, learning-coach |
| **quantitative-analysis** | Data outputs styled with the ideas42 brand (Figtree, ideas42 palette, brand config) | data-cleaning, describe-sample, quick-csv-summary, verify-data-analysis, visualize |
| **claude-ops** | Workspace operations tuned to how ideas42 works | project-setup, file-organizer, memory-import, memory-consolidation, schedule, setup-cowork, create-plugin, skill-lookup, review-console, review-council |
| **qualitative-research** | Behaviorally-informed fieldwork (seed for the IDEAS-stage roadmap) | journey-mapping (user-testing, interview-guide, qualitative-synthesis planned) |

## What's not here (and why)

Five earlier plugins — `deliverables`, `research-evidence`, `web-dev`, `connector-automation`, `notion-workflows` (28 skills) — were **verbatim copies** of skills from Anthropic's Cowork bundle and community packs (e.g., [awesome-claude-skills](https://github.com/) for artifacts-builder, canvas-design, theme-factory, image-enhancer, and the figma/miro/notion automation skills). They carried **no ideas42-specific content**, so they've been moved to [`archived-plugins/`](archived-plugins/) and de-listed from the marketplace — preserved (nothing deleted), just no longer distributed as ideas42 plugins.

To get that functionality, install the originals directly (so you inherit their updates), then customize on install:

| Need | Get it from |
|------|-------------|
| Deliverables, artifacts, docs, themes, creative assets | Anthropic Cowork bundle (`artifact-production`, `document-production`) + community packs |
| Research, synthesis, deep research, concept maps | Anthropic Cowork bundle / community research packs |
| Figma web-dev, design-system rules, UI review | [Figma](https://github.com/figma/mcp-server-guide) + Anthropic `design` plugin |
| Figma/Miro/Notion automation, MCP building | [awesome-claude-skills](https://github.com/) and vendor repos below |
| Notion capture / meeting / spec workflows | Anthropic Cowork bundle (`notion-workflows`) |

## Third-party plugins (not mirrored here)

Maintained by their vendors — install from the in-app plugin directory or their official repos so you get updates:

| Plugin | Author | Official source |
|--------|--------|-----------------|
| productivity, enterprise-search, data, marketing, engineering, design, product-management, pdf-viewer, cowork-plugin-management | Anthropic | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| slack-by-salesforce | Salesforce | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (`partner-built/slack`) |
| figma | Figma | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) |
| miro | Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) (`claude-plugins/miro`) |
| airtable | Airtable | [airtable/skills](https://github.com/airtable/skills) |
| desktop-commander | Desktop Commander | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) |
| learn-with-coursera | Coursera | [coursera/skills](https://github.com/coursera/skills) |

## Conventions

- **Only host what's ideas42's.** A skill belongs here if it encodes ideas42 brand, voice, methodology, or workspace conventions. If it's a generic craft skill, point to the upstream instead of copying it.
- Stage-specific methodology (b-mapping, testing protocols) goes in a stage plugin; reusable ideas42 craft goes in a craft plugin.
- Bump the plugin version and the marketplace version with every change so installed copies refresh.
- Plugins are customized on install — keep org/personal specifics as `~~`-prefixed placeholders where possible so the Cowork customizer can fill them.
- Plugins that require connectors note it in their description; users authenticate on first use.
