---
name: dev-followup
description: Update an existing ExecPlan-led workstream after narrow post-implementation changes and keep the plan and any justified downstream docs aligned with the current code and validation state. Use only when the user explicitly invokes `$dev-followup` or `dev-orchestrate` explicitly delegates to this skill for a same-workstream narrow follow-up that already has a relevant ExecPlan. Do not trigger this skill for new planning, broad greenfield work, or generic implementation changes without an existing plan.
---

# dev-followup

Keep one existing workstream aligned with reality after a narrow follow-up change.

This skill assumes a relevant ExecPlan already exists under `$PWD/docs/plans/`.

## Inputs

- An explicit ExecPlan path
- A narrow follow-up request tied to an existing planned feature
- A dirty working tree that clearly belongs to an existing workstream
- Optional related artifacts under `$PWD/docs/specs/`, `$PWD/docs/walkthroughs/`, or `$PWD/docs/recaps/`

If no valid target plan exists, stop and hand off to `dev-plan`.

## Output Contract

- Update exactly one primary ExecPlan in place
- Update related spec, walkthrough, or recap artifacts only when the propagation rules justify it
- Keep the plan readable as the current source of truth, not an append-only log

Follow `references/markdown-artifact-rules.md` for any saved markdown edits.

## Primary Target Selection

Choose exactly one active plan in this order:

1. the explicit plan path from the user
2. the active plan selected by an upstream workflow
3. the newest relevant ExecPlan that matches the changed files, feature name, or nearby artifacts

Ask one concise question only when selecting the wrong plan would materially corrupt documentation.

## Workflow

1. Resolve the primary plan target.
2. Inspect the current diff, the plan's living sections, and any commands or outputs actually produced during the follow-up.
3. Rewrite stale plan statements so they match the new implementation and validation state.
4. Append only net-new evidence another engineer would need.
5. Decide whether the spec, walkthrough, or recap also needs an update.

## Plan Update Rules

Keep these sections aligned with the current state:

- `Progress`: update milestones, partial completion, and next steps
- `Surprises & Discoveries`: capture genuine new observations with brief evidence
- `Decision Log`: record meaningful follow-up decisions and why they won
- `Outcomes & Retrospective`: rewrite stale outcome summaries instead of stacking contradictions
- `Concrete Steps`: refresh only if the practical execution recipe changed
- `Validation and Acceptance`: record only commands that were actually rerun and what they showed

## Propagation Rules

- Update the spec when the follow-up changes visible behavior, requirements, contracts, or invariants.
- Update or regenerate the walkthrough when the recommended reading path materially changed or the user asked for a refreshed one.
- Update the recap when current status, unresolved risks, or the handoff story changed enough that the old recap is misleading.

See `references/propagation-examples.md` for representative cases.

## Guardrails

- Never invent commands, results, or observations.
- Do not treat every tiny edit as a spec change.
- Do not rewrite unrelated sections just because the file is open.
- If the follow-up grows into a broad scope reset, hand off to `dev-plan` or `dev-orchestrate`.

## Quality Bar

- Another engineer should be able to read the updated plan and understand the follow-up without reopening the full session.
- Downstream artifact updates should be selective and justified.
