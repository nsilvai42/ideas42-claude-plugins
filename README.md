# ideas42 Claude Plugins

A Claude plugin marketplace for ideas42 team members. Contains 26 plugins: 4 custom ideas42 plugins (brand-systems, claude-workspace-ops, claude-admin-utilities, cowork-plugin-management) plus mirrored copies of public directory plugins, snapshotted 2026-07-16.

## Install (individuals)

In Claude Code or Cowork:

```
/plugin marketplace add nsilvai42/ideas42-claude-plugins
/plugin install brand-systems@ideas42-claude-plugins
```

## Distribute org-wide (Team/Enterprise admins)

Admins can add this repo as an organization plugin marketplace and choose which plugins members see, install themselves, or get auto-installed: [Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).

## Notes

- **brand-systems** is the flagship custom plugin: ideas42, SBNC, Bottom Line, Calbright, and Year Up brand skills.
- Mirrored third-party plugins (figma, miro, slack-by-salesforce, airtable, learn-with-coursera, desktop-commander, etc.) are frozen snapshots — they do not receive vendor updates here. For the latest versions, install them from the public Claude plugin directory instead.
- Plugins that bundle MCP connectors (`.mcp.json`) require each user to authenticate those connectors on first use.
- Third-party plugin content remains the property of its respective vendors and is mirrored here for internal ideas42 convenience.
