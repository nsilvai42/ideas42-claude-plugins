# ideas42 Claude Plugins

A Claude plugin marketplace of **ideas42-specific** plugins: the skills that encode ideas42 brand, voice, methodology, and workspace conventions, which you can't get anywhere else. Generic craft skills (data, design, research, connector automation, deliverables) are **not** re-hosted here; they come from Anthropic's Cowork skill bundle and community packs, and mirroring them would add drift and maintenance with no ideas42 value. See [What's not here](#whats-not-here-and-why).

Since v3.0.0 the plugins follow the **AI Builders Operating Framework**: one plugin per framework domain (Governance, Research and Evaluation, Design, Implementation), plus the two cross-cutting craft libraries (brand, communications) that every domain uses. Each plugin's OVERVIEW names its domain and the IDEAS stage(s) it serves.

## Repository layout

Skills are the source of truth; plugins are generated wrappers around them.

```
skills/<theme>/<skill>/          <- source of truth, grouped by framework domain
plugins/<plugin>/                <- marketplace wrappers (plugin.json, OVERVIEW.md, TEST_PROMPTS.md)
plugins/<plugin>/skills/         <- GENERATED from skills/ by the sync script; do not edit by hand
incubator/<skill>/               <- skills in development, not yet in any plugin
scripts/sync-skills-to-plugins.sh  <- regenerates plugins/*/skills from skills/
archived-plugins/                <- de-listed generic plugins, preserved (see its README)
```

Two ways to consume the same skills, with no double maintenance:

- **Individual skills** (`skills/`): broadest reach (Claude Code, Cowork, claude.ai web chat, API, Slack). See [`skills/README.md`](skills/README.md).
- **Plugins** (`plugins/` via this marketplace): one-click install and versioned updates for the Claude Code family (CLI and Cowork). Not available in claude.ai web chat.

After editing any skill, run `bash scripts/sync-skills-to-plugins.sh` and bump the affected plugin and marketplace versions.

## Install (individuals)

In Claude Code or Cowork:

```
/plugin marketplace add nsilvai42/ideas42-claude-plugins
/plugin install brand-systems@ideas42-claude-plugins
```

These plugins are meant to be **customized on install**: in Cowork, run the plugin customizer after installing to swap in your own tools, channels, and workspace values.

## Distribute org-wide (Team/Enterprise admins)

Admins can add this repo as an organization plugin marketplace and choose which plugins members see, install themselves, or get auto-installed: [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).

## Plugins (6)

| Plugin | Framework domain | IDEAS stage(s) | Skills |
|--------|------------------|----------------|--------|
| **brand-systems** (0.2.0) | Design (cross-cutting craft) | Engineer | bottom-line-brand, calbright-brand, ideas42-brand, sbnc-brand, year-up-brand |
| **ideas42-comms** (0.3.0) | Communications craft (Governance floor for external-facing work) | Engineer | anti-ai-writing, i42-copy-editor, internal-communications, learning-coach |
| **research-and-evaluation** (0.1.0) | Research and Evaluation | Identify, Diagnose, Assess | data-cleaning, deep-research, describe-sample, journey-mapping, quick-csv-summary, verify-data-analysis, visualize |
| **behavioral-diagnosis** (0.1.0) | Implementation and Design (custom diagnostic tools) | Diagnose | comms-auditor |
| **governance** (0.1.0) | Governance (the floor under every domain) | All stages | review-console, review-council, right-size-setup |
| **claude-ops** (0.3.0) | Implementation (workspace operations) | Engineer, Scale | create-plugin, file-organizer, memory-consolidation, memory-import, project-setup, schedule, setup-cowork, skill-lookup |

## How the plugins map to the framework

The AI Builders Operating Framework (July 2026) splits ideas42's AI work into five domains with one owner each: Governance, Research, Evaluation, Design, and Implementation, run as one IDEAS loop (Identify, Diagnose, Engineer, Assess, Scale). The mapping here is deliberately loose where the craft serves every domain:

- **brand-systems** and **ideas42-comms** are craft libraries every domain uses. Brand sits closest to Design; communications sits on the Governance floor because the external-facing-work guidance (disclosure, voice integrity) lives in how we write.
- **research-and-evaluation** covers two domains on purpose: the Research, Evidence, and Learning team owns both, and the skills (evidence scans, data description, verification, journey mapping) serve Identify, Diagnose, and Assess.
- **behavioral-diagnosis** is the first stage-specific methodology plugin from the roadmap, seeded with the comms auditor. B-mapping and the behavioral-concepts canon belong here next.
- **governance** carries the framework's verification backbone ("nothing ships unverified") and responsible-use defaults.
- **claude-ops** is Implementation in the workspace sense: getting Claude set up and kept tidy the ideas42 way.

Skills still in development sit in `incubator/` until they pass the Skill Lab definition of done; see [`incubator/README.md`](incubator/README.md).

## What's not here (and why)

Five earlier plugins (`deliverables`, `research-evidence`, `web-dev`, `connector-automation`, `notion-workflows`, 28 skills) were **verbatim copies** of skills from Anthropic's Cowork bundle and community packs (for example artifacts-builder, canvas-design, theme-factory, image-enhancer, and the figma/miro/notion automation skills). They carried **no ideas42-specific content**, so they were moved to [`archived-plugins/`](archived-plugins/) and de-listed from the marketplace on 2026-08-02. Nothing was deleted. Note that the archived `research-evidence` plugin contains Anthropic's generic `deep-research`; the `deep-research` in this marketplace is ideas42's own evidence-scan workflow and is unrelated.

To get that functionality, install the originals directly (so you inherit their updates), then customize on install:

| Need | Get it from |
|------|-------------|
| Deliverables, artifacts, docs, themes, creative assets | Anthropic Cowork bundle (`artifact-production`, `document-production`) and community packs |
| Research, synthesis, concept maps | Anthropic Cowork bundle and community research packs |
| Figma web-dev, design-system rules, UI review | [Figma](https://github.com/figma/mcp-server-guide) and Anthropic's `design` plugin |
| Figma/Miro/Notion automation, MCP building | [awesome-claude-skills](https://github.com/) and vendor repos below |
| Notion capture, meeting, and spec workflows | Anthropic Cowork bundle (`notion-workflows`) |

## Third-party plugins (not mirrored here)

Maintained by their vendors; install from the in-app plugin directory or their official repos so you get updates:

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
- **One skill, one plugin.** A skill lives in exactly one theme folder; the theme decides the plugin.
- Stage-specific methodology goes in a stage plugin (behavioral-diagnosis today; intervention-design, experimental-design, scale-sustain next); reusable craft goes in a craft plugin. See [RECOMMENDATIONS.md](RECOMMENDATIONS.md).
- Bump the plugin version and the marketplace version with every change so installed copies refresh.
- Plugins are customized on install; keep org or personal specifics as `~~`-prefixed placeholders where possible so the Cowork customizer can fill them.
- Plugins that require connectors note it in their description; users authenticate on first use.

## Changelog

- **3.0.0 (2026-10-08).** Reorganized around the framework domains. `quantitative-analysis` and `qualitative-research` merged into **research-and-evaluation** (reinstall if you had either). New plugins **behavioral-diagnosis** and **governance**. `review-council` and `review-console` moved from claude-ops to governance. Imported four skills that lived outside the marketplace: `deep-research`, `comms-auditor`, `right-size-setup`, `anti-ai-writing`. Added `incubator/` with `voice-setup`, `design-facilitator`, and `shared-project-kit`.
- **2.1.0 (2026-08-02).** Skills-first layout; five generic plugins archived.
