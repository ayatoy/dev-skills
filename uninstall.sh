#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
skills_root="$repo_root/skills"
dest_root="${1:-$HOME/.agents/skills}"

if [ -z "$dest_root" ] || [ "$dest_root" = "/" ]; then
  echo "Refusing to uninstall from an unsafe destination: $dest_root" >&2
  exit 1
fi

shopt -s nullglob
skill_mds=("$skills_root"/*/SKILL.md)
shopt -u nullglob

if [ "${#skill_mds[@]}" -eq 0 ]; then
  echo "No skills found under $skills_root." >&2
  exit 1
fi

removed=0

for skill_md in "${skill_mds[@]}"; do
  skill_dir="$(dirname "$skill_md")"
  skill_name="$(basename "$skill_dir")"
  target_dir="$dest_root/$skill_name"

  if [ ! -e "$target_dir" ]; then
    echo "Skipping $skill_name (not installed)"
    continue
  fi

  echo "Removing $skill_name"
  rm -rf -- "$target_dir"
  removed=$((removed + 1))
done

echo "Removed $removed skill(s) from $dest_root"
