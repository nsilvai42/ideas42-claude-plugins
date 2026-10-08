#!/usr/bin/env bash
#
# sync-skills-to-plugins.sh
#
# Single source of truth for skills is skills/<theme>/<skill>/.
# The marketplace plugins under plugins/<plugin>/ are shipping wrappers whose
# skills/ subdirectory is GENERATED from the theme folders below — do not edit
# plugins/<plugin>/skills/ by hand; edit skills/<theme>/ and re-run this script.
#
# Each plugin keeps its own hand-maintained files (plugin.json, OVERVIEW.md,
# TEST_PROMPTS.md); only the skills/ subdirectory is regenerated.
#
# Usage:  bash scripts/sync-skills-to-plugins.sh
#
set -euo pipefail
cd "$(dirname "$0")/.."

# theme_folder -> plugin_name  (one line per mapping)
MAP="
brand:brand-systems
communications:ideas42-comms
research-evaluation:research-and-evaluation
behavioral-diagnosis:behavioral-diagnosis
governance:governance
workspace-ops:claude-ops
"

echo "$MAP" | while IFS=: read -r theme plugin; do
  [ -z "$theme" ] && continue
  src="skills/$theme"
  dst="plugins/$plugin/skills"
  if [ ! -d "$src" ]; then echo "!! missing source: $src" >&2; exit 1; fi
  rm -rf "$dst"
  mkdir -p "$dst"
  for sk in "$src"/*/; do
    name=$(basename "$sk")
    cp -R "$src/$name" "$dst/$name"
  done
  echo "synced $src -> $dst ($(ls "$dst" | wc -l | tr -d ' ') skills)"
done

echo "done. plugins/<plugin>/skills regenerated from skills/<theme>."
