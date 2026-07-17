# ideas42 Claude Plugins

A Claude plugin marketplace of custom plugins built at ideas42, grouped by craft. Most crafts serve multiple stages of the IDEAS methodology (Identification, Diagnosis, Engineer, Assess, Scale & Sustain), so plugins are organized around what you're doing, not which stage you're in. Stage-specific methodology plugins (behavioral-diagnosis, intervention-design, experimental-design, scale-sustain) are planned — see [RECOMMENDATIONS.md](RECOMMENDATIONS.md).

## Install (individuals)

In Claude Code or Cowork:

```
/plugin marketplace add nsilvai42/ideas42-claude-plugins
/plugin install brand-systems@ideas42-claude-plugins
```

## Distribute org-wide (Team/Enterprise admins)

Admins can add this repo as an organization plugin marketplace and choose which plugins members see, install themselves, or get auto-installed: [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).

## Plugins (10)

| Plugin | Craft | Skills |
|--------|-------|--------|
| **brand-systems** | Partner-facing deliverable branding | ideas42, SBNC, Bottom Line, Calbright, Year Up brand guidelines |
| **ideas42-comms** | Writing in the ideas42 voice | i42-copy-editor, internal-communications, learning-coach |
| **research-evidence** | Collecting, synthesizing, compiling information | deep-research, article-extractor, concept-map, research-writer, agent-council |
| **qualitative-research** | Qualitative fieldwork (all stages) | journey-mapping (user-testing, interview-guide, qualitative-synthesis planned) |
| **quantitative-analysis** | Quantitative analysis (all stages) | data-cleaning, describe-sample, quick-csv-summary, verify-data-analysis, visualize |
| **deliverables** | Producing polished outputs | doc-coauthoring, artifacts-builder, web-artifacts-builder, theme-factory, canvas-design, visual-design-foundations, image-enhancer, algorithmic-art, slack-gif-creator |
| **claude-ops** | Claude workspace operations | project-setup, file-organizer, memory-import, memory-consolidation, schedule, setup-cowork, create-plugin, skill-lookup, review-console, review-council |
| **web-dev** | Web development with Figma | figma-code-connect, figma-design-system-rules, figma-implement-design, react-performance, ui-ux-design-review, web-ui-review |
| **connector-automation** | Automating connected tools | figma-automation, miro-automation, notion-automation, mcp-builder |
| **notion-workflows** | Notion-based workflows | knowledge-capture, meeting-intelligence, research-documentation, spec-to-implementation |

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

- One craft per plugin; each skill lives in exactly one plugin.
- Stage-specific methodology (b-mapping, testing protocols) goes in a stage plugin; reusable craft (interviews, data cleaning, deliverables) goes in a craft plugin.
- Bump the plugin version and marketplace version with every change so installed copies refresh.
- Plugins that require connectors note it in their description; users authenticate on first use.
