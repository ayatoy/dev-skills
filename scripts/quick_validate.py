#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SHARED_RULES = REPO_ROOT / "shared" / "markdown-artifact-rules.md"


def iter_skill_dirs(target: Path) -> list[Path]:
    if (target / "SKILL.md").exists():
        return [target]

    if target == REPO_ROOT:
        skills_root = REPO_ROOT / "skills"
    else:
        skills_root = target

    return sorted(
        path
        for path in skills_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").exists()
    )


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing frontmatter start"]

    try:
        _, frontmatter, _ = text.split("---", 2)
    except ValueError:
        return {}, ["malformed frontmatter"]

    data: dict[str, str] = {}
    for raw_line in frontmatter.strip().splitlines():
        if ":" not in raw_line:
            errors.append(f"invalid frontmatter line: {raw_line}")
            continue
        key, value = raw_line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')

    extra_keys = sorted(set(data) - {"name", "description"})
    if extra_keys:
        errors.append(f"unexpected frontmatter keys: {', '.join(extra_keys)}")

    return data, errors


def validate_openai_yaml(skill_dir: Path, errors: list[str]) -> None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.exists():
        errors.append("missing agents/openai.yaml")
        return

    text = path.read_text(encoding="utf-8")
    display_name = re.search(r'display_name:\s*"([^"]+)"', text)
    short_description = re.search(r'short_description:\s*"([^"]+)"', text)
    default_prompt = re.search(r'default_prompt:\s*"([^"]+)"', text)

    if not display_name:
        errors.append("missing interface.display_name")
    elif display_name.group(1) == skill_dir.name:
        errors.append("display_name should be human-facing, not the raw skill slug")

    if not short_description:
        errors.append("missing interface.short_description")

    if not default_prompt:
        errors.append("missing interface.default_prompt")


def validate_shared_rules(skill_dir: Path, errors: list[str]) -> None:
    local_copy = skill_dir / "references" / "markdown-artifact-rules.md"
    if not local_copy.exists():
        errors.append("missing references/markdown-artifact-rules.md")
        return

    if local_copy.read_text(encoding="utf-8") != SHARED_RULES.read_text(encoding="utf-8"):
        errors.append("references/markdown-artifact-rules.md is out of sync with shared/markdown-artifact-rules.md")


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    frontmatter, frontmatter_errors = parse_frontmatter(skill_md)
    errors.extend(frontmatter_errors)

    if frontmatter.get("name") != skill_dir.name:
        errors.append("frontmatter name must match the skill directory name")

    description = frontmatter.get("description", "")
    if not description:
        errors.append("missing frontmatter description")
    elif not re.search(r"\bUse (?:when|only when|primarily when)\b", description):
        errors.append("description must include explicit trigger guidance such as 'Use when', 'Use only when', or 'Use primarily when'")

    skill_text = skill_md.read_text(encoding="utf-8")
    if "$HOME/.agents/skills/" in skill_text:
        errors.append("skill should not hardcode $HOME/.agents/skills paths")

    validate_openai_yaml(skill_dir, errors)
    validate_shared_rules(skill_dir, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", nargs="?", default=str(REPO_ROOT))
    args = parser.parse_args()

    target = Path(args.target).resolve()
    skill_dirs = iter_skill_dirs(target)
    if not skill_dirs:
        print(f"no skill directories found under {target}", file=sys.stderr)
        return 1

    failures = 0
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failures += 1
            print(f"{skill_dir.relative_to(REPO_ROOT)}")
            for error in errors:
                print(f"  - {error}")

    if failures:
        return 1

    print(f"validated {len(skill_dirs)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
