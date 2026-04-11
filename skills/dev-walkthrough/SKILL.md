---
name: dev-walkthrough
description: Turn code changes or existing code areas into a short prioritized reading path and save one walkthrough note under $PWD/docs/walkthroughs. Use only when the user explicitly invokes `$dev-walkthrough` or `dev-orchestrate` explicitly delegates to this skill to produce a reading path through a diff or code area. Do not trigger this skill when the main goal is correctness review, planning, or direct implementation.
---

# dev-walkthrough

Turn a target into a short, high-signal path for a human reader.

Optimize for the fastest reliable understanding, not for an exhaustive file-by-file explanation.

## Modes

- `review`: staged or unstaged changes, commits, ranges, branches, or pull requests
- `reading`: existing features, modules, directories, entry points, stack traces, or code questions

If the user does not name a mode, infer it from the target. If both are present, start with `review`.

## Inputs

- A diff, commit, branch comparison, pull request, feature name, file, directory, stack trace, or architecture question
- Optional constraints such as role, time budget, focus areas, or risk tolerance

## Output Contract

- Save exactly one main walkthrough note under `$PWD/docs/walkthroughs/`
- Produce a concise guide with `Target`, `Mode`, `Shape`, `Start here`, `Path`, `Watchpoints`, and `Light scan`
- Add `Key concepts` only when it materially reduces confusion
- Add an `Optional diagram` only when a small Mermaid diagram will reduce cognitive load

Follow `references/markdown-artifact-rules.md` for saved-note formatting and path handling.

## Workflow

1. Resolve the target as narrowly as possible.
2. Inspect structure before details.
3. Group files into a few meaningful reading units.
4. Rank those units by leverage for the chosen mode.
5. Turn them into a serial path that minimizes context switching.
6. Read only enough code to justify the path and watchpoints.

See `references/path-format.md` for the preferred step shape and default reading order.

## Prioritization

Raise priority for entry points, core logic, state transitions, persistence, side effects, permissions, error handling, and tests that reveal intent.

Lower priority for generated files, lockfiles, snapshots, broad rename fallout, and docs that merely mirror already-understood code.

## Guardrails

- Do not claim to have completed a review when you are only structuring a reading path.
- Do not produce an exhaustive changelog unless the user asks for it.
- If the target is too large, split the path into phases instead of dumping more detail.

## Quality Bar

- The path should usually fit in 3 to 7 steps.
- Another engineer should be able to follow it and understand why each step appears in that order.
