---
name: file-organizer
description: Analyze messy folders, find duplicates, propose safe organization plans, and create logged file cleanup or restructuring workflows.
---

# File Organizer

Maintain clean, logical file structures by understanding context, finding patterns, and automating organization tasks.

## When to Use

- Downloads folder is chaotic
- Files scattered across system
- Duplicate files taking space
- Folder structure needs improvement
- Starting new project structure
- Preparing for archiving

## Core Workflow

### 1. Understand Scope

Ask clarifying questions:
- Which directory? (Downloads, Documents, home folder)
- Main problem? (can't find files, duplicates, no structure)
- Files to avoid? (active projects, sensitive data)
- Organization level? (conservative vs. aggressive)

### 2. Analyze Current State

```bash
# Overview
ls -la [target_dir]

# File types and sizes
find [target_dir] -type f -exec file {} \; | head -20

# Largest files
du -sh [target_dir]/* | sort -rh | head -20

# File type counts
find [target_dir] -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn
```

Summarize findings:
- Total files/folders, size distribution
- File type breakdown, date ranges
- Organization issues

### 3. Identify Patterns

**By Type**: Documents (PDF, DOCX), Images (JPG, PNG), Videos (MP4), Archives (ZIP), Code, Spreadsheets, Presentations

**By Purpose**: Work vs Personal, Active vs Archive, Project-specific, Reference, Temporary

**By Date**: Current year/month, Previous years, Archive candidates (>6 months old)

### 4. Find Duplicates

```bash
# Exact duplicates by hash
find [dir] -type f -exec md5 {} \; | sort | uniq -d

# Same name
find [dir] -type f -printf '%f\n' | sort | uniq -d

# Similar size
find [dir] -type f -printf '%s %p\n' | sort -n
```

For duplicates, show:
- All paths, sizes, dates
- Recommendation (keep newest/best-named)
- **Always confirm before deleting**

### 5. Propose Organization Plan

Present clear plan before changes:

```markdown
# Organization Plan for [Directory]

## Current State
- X files, Y folders, [Size] total
- File types: [breakdown]
- Issues: [problems]

## Proposed Structure
[Show tree diagram]

## Changes
1. Create folders: [list]
2. Move files:
   - X PDFs → Work/Documents/
   - Y images → Personal/Photos/
3. Rename: [patterns]
4. Delete: [duplicates/trash]

## Needs Your Decision
[Unsure files]

Ready? (yes/no/modify)
```

### 6. Execute Organization

After approval:

```bash
# Create structure
mkdir -p "path/to/folders"

# Move with logging
mv "old/path/file" "new/path/file"

# Rename consistently
# Format: "YYYY-MM-DD - Description.ext"
```

**Rules**:
- Always confirm deletions
- Log moves for undo
- Preserve modification dates
- Handle conflicts gracefully
- Stop and ask on unexpected situations

### 7. Provide Summary

```markdown
# Organization Complete ✨

## Changes
- Created [X] folders
- Organized [Y] files
- Freed [Z] GB
- Archived [W] old files

## New Structure
[Tree diagram]

## Maintenance Tips
- Weekly: Sort new downloads
- Monthly: Archive completed projects
- Quarterly: Check duplicates
- Yearly: Archive old files

## Quick Commands
[Custom commands for their setup]
```

## Common Tasks

**Downloads Cleanup**: "Organize Downloads - move docs to Documents, images to Pictures, archive files >3 months old"

**Project Organization**: "Review Projects folder, separate active from archived projects"

**Duplicate Removal**: "Find duplicates in Documents, help decide which to keep"

**Desktop Cleanup**: "Desktop is covered in files, organize into Documents properly"

**Photo Organization**: "Organize photos by date (year/month) based on when taken"

**Work/Personal Separation**: "Separate work from personal files in Documents"

## Best Practices

**Folder Naming**:
- Clear, descriptive names
- Avoid spaces (use hyphens/underscores)
- Be specific: "client-proposals" not "docs"
- Use prefixes for ordering: "01-current", "02-archive"

**File Naming**:
- Include dates: "2024-10-17-meeting-notes.md"
- Be descriptive: "q3-financial-report.xlsx"
- Avoid version numbers (use version control)
- Remove artifacts: "doc-final-v2 (1).pdf" → "document.pdf"

**When to Archive**:
- Not touched in 6+ months
- Completed work needing reference
- Old versions after migration
- Hesitant to delete (archive first)

## Pro Tips

1. Start small with one folder (Downloads)
2. Run weekly cleanup on Downloads
3. Use "YYYY-MM-DD - Description" format
4. Archive aggressively vs deleting
5. Keep Active separate from Archive
6. Let Claude handle cognitive load
