# ideas42 Claude Plugins

A Claude plugin marketplace of custom plugins built at ideas42.

## Install (individuals)

In Claude Code or Cowork:

```
/plugin marketplace add nsilvai42/ideas42-claude-plugins
/plugin install brand-systems@ideas42-claude-plugins
```

## Distribute org-wide (Team/Enterprise admins)

Admins can add this repo as an organization plugin marketplace and choose which plugins members see, install themselves, or get auto-installed: [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).

## Plugins in this marketplace (11)

| Plugin | What it does |
|--------|--------------|
| **brand-systems** | ideas42, SBNC, Bottom Line, Calbright, and Year Up brand skills — apply client brand guidelines to any deliverable. |
| **artifact-production** | Algorithmic art, canvas design, artifact building, themes, image enhancement. |
| **claude-admin-utilities** | Plugin creation, memory consolidation, scheduling, Cowork setup, skill lookup. |
| **claude-workspace-ops** | File organizing, project setup, memory import, review consoles/councils. |
| **communications-learning** | Internal communications and learning-coach skills. |
| **connector-automation** | Figma, Miro, and Notion automation workflows plus MCP building. |
| **data-evaluation** | Data cleaning, sample description, CSV profiling, analysis verification, visualization. |
| **document-production** | Word, Excel, PowerPoint, PDF production with doc co-authoring and themes. |
| **figma-web-dev** | Figma-to-code, design-system rules, React performance, UI/UX reviews. |
| **notion-workflows** | Notion knowledge capture, meeting intelligence, research documentation, spec-to-implementation. |
| **research-evidence** | Deep research, agent councils, article extraction, concept and journey mapping, research writing. |

## Third-party plugins (not mirrored here)

These were previously mirrored but are maintained by their vendors — install them from the in-app plugin directory or their official repos so you get updates:

| Plugin | Author | Official source |
|--------|--------|-----------------|
| productivity, enterprise-search, data, marketing, engineering, design, product-management, pdf-viewer, cowork-plugin-management | Anthropic | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| slack-by-salesforce | Salesforce | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (`partner-built/slack`) |
| figma | Figma | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) |
| miro | Miro | [miroapp/miro-ai](https://github.com/miroapp/miro-ai) (`claude-plugins/miro`) |
| airtable | Airtable | [airtable/skills](https://github.com/airtable/skills) |
| desktop-commander | Desktop Commander | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) |
| learn-with-coursera | Coursera | [coursera/skills](https://github.com/coursera/skills) |

Anthropic's broader curated directory (including partner plugins) is at [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official); admins can add `anthropics/knowledge-work-plugins` as a second organization marketplace to distribute the Anthropic plugins alongside this one.

## Notes

- Plugins that bundle MCP connectors (`.mcp.json`) require each user to authenticate those connectors on first use.
- Snapshot date for plugin contents: 2026-07-16.
