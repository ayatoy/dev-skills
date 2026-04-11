#!/usr/bin/env python3

from pathlib import Path
import shutil
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SHARED_RULES = REPO_ROOT / "shared" / "markdown-artifact-rules.md"


def iter_skill_dirs() -> list[Path]:
    return sorted(
        path
        for path in (REPO_ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").exists()
    )


def sync_markdown_rules() -> int:
    if not SHARED_RULES.exists():
        print(f"missing shared rules: {SHARED_RULES}", file=sys.stderr)
        return 1

    for skill_dir in iter_skill_dirs():
        destination = skill_dir / "references" / "markdown-artifact-rules.md"
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SHARED_RULES, destination)
        print(destination.relative_to(REPO_ROOT))

    return 0


if __name__ == "__main__":
    raise SystemExit(sync_markdown_rules())
