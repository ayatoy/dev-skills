---
name: dev-orchestrate
description: Orchestrate the repository workflow across the local dev-* skills from investigation through review, walkthrough, and recap, and reopen completed workstreams in follow-up mode when later narrow changes arrive. Use primarily when the user explicitly invokes `$dev-orchestrate` or clearly asks for the full multi-phase dev workflow to be run, resumed from workflow artifacts, or continued as a same-workstream follow-up. Do not trigger this skill for single-phase requests that only need one downstream skill.
---

# dev-orchestrate

Run a full repository workstream from the right starting phase through a clean finish.

Keep the main thread as the orchestrator. Resolve the execution mode before dispatching any phase work.

## Inputs

- A free-form request
- An existing workflow artifact under `$PWD/docs/`
- A dirty workspace that may reflect a paused or manually advanced workstream
- Optional constraints such as execution mode, language, stop phase, resume phase, or timebox

When the user provides a markdown artifact, pass that artifact through as the primary input to the next phase instead of rewriting it into a short summary.

## Execution Modes

Support these modes:

- `auto`: use subagents when available, otherwise run locally
- `local`: run every phase in the main thread
- `subagents`: use a separate subagent per phase unless a real limitation forces a local fallback

Interpret natural-language equivalents semantically. If the user hints at a mode but the intent is still ambiguous, ask one short clarification question.

## Default Workflow

1. `dev-investigate`
2. optional `dev-resolve`
3. optional `dev-spec`
4. `dev-plan` to create or update an ExecPlan
5. `dev-plan` again to execute that ExecPlan
6. `dev-review`
7. narrow implementation and rerun review when blocking findings must be fixed now
8. `dev-walkthrough`
9. `dev-recap`

## Follow-up Mode

Use follow-up mode when the workspace already contains a relevant completed or in-flight workstream and the new request is a narrow continuation rather than a fresh project.

In follow-up mode:

1. identify the existing workstream and active ExecPlan
2. run any needed narrow implementation or review loop
3. run `dev-followup` to synchronize the plan
4. refresh walkthrough or recap only when the follow-up propagation rules justify it

## Phase Selection

Use the strongest available evidence in this order:

1. explicit user override
2. workspace state and uncommitted changes
3. provided workflow artifacts
4. free-form request intent

See `references/resume-and-phase-rules.md` for the resume heuristic and optional-phase rules.

## Orchestrator Responsibilities

- decide the current phase and whether the run belongs to the main cycle or follow-up mode
- preserve user changes and route the workflow around them instead of discarding them
- pass the minimum necessary context to each phase
- keep the active ExecPlan path stable once selected
- keep review and fix loops narrow and evidence-driven
- ensure downstream artifact-producing phases follow `references/markdown-artifact-rules.md`

## Review Loop

- Run `dev-review` after implementation.
- Treat correctness, security, data loss, crash, and similarly severe issues as blocking by default.
- Rerun implementation and review only when the fix pass changed in-scope code, tests, or runtime configuration.
- If review is clean, continue directly to `dev-walkthrough`.

## Guardrails

- Do not jump straight into implementation from a free-form request.
- Do not restart from investigation when stronger evidence shows the workflow already progressed further.
- Do not skip `dev-plan` or post-implementation `dev-review`.
- Do not run overlapping write-capable phases in parallel.
- Do not create multiple main walkthrough or recap artifacts for one completed cycle.

## Quality Bar

- The workflow should feel like a conservative pipeline that preserves user work and prior artifacts.
- Optional phases should be skipped deliberately, not forgotten.
- The final summary should clearly state completed phases, skipped phases, created or updated artifacts, and any remaining blockers.
