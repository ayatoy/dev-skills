---
name: dev-recap
description: Summarize the current session or workstream into one detailed handoff note under $PWD/docs/recaps and include evidence-based repeated-work and skill-opportunity analysis. Use only when the user explicitly invokes `$dev-recap` or `dev-orchestrate` explicitly delegates to this skill for a handoff recap, session summary, or repeated-work analysis after work has already happened. Do not trigger this skill during active ideation or normal implementation requests.
---

# dev-recap

Create or update one detailed recap note under `$PWD/docs/recaps/`.

## Inputs

- The current session history as the primary source
- Optional constraints such as audience, language, filename hint, or whether recommendations should be conservative

Use local repository evidence only to confirm concrete details such as files, commands, diffs, and artifacts mentioned in the session.

## Output Contract

- Create or update exactly one recap note under `$PWD/docs/recaps/`
- Capture enough detail that another strong engineer can continue the work without reopening the full transcript
- Include a `Repeated work patterns` section
- Include an `Agent skill opportunities` section

Follow `references/markdown-artifact-rules.md` for saved-note formatting and path handling.

## Reuse Rules

Prefer updating the existing recap when the current run is clearly a continuation of the same session or workstream.

See `references/reuse-rules.md` for the reuse heuristic.

## Workflow

1. Determine the scope of the recap.
2. Decide whether to reuse an existing recap or create a new one.
3. Reconstruct the session chronology from conversation history.
4. Confirm concrete repository details only where they materially affect the handoff.
5. Write or update one coherent recap note.
6. Add repeated-work analysis.
7. Add conservative skill-opportunity analysis.

## What To Capture

- user goals, constraints, and direction changes
- key decisions and why they were made
- commands, edits, validations, and artifacts that materially changed the work
- blockers, failures, dead ends, and resolutions
- current status, risks, and unfinished work

## Guardrails

- Do not omit major reversals, failures, or unresolved issues.
- Do not invent transcript details that are not in session history or confirmed locally.
- Do not create duplicate recap notes for the same ongoing work without a clear reason.
- Recommend fewer, stronger skill candidates instead of a long speculative list.

## Quality Bar

- Another engineer should be able to resume the work from the recap alone.
- The repeated-work analysis should be evidence-based, not generic process advice.
- Skill recommendations should clear a real reuse bar, not just describe normal engineering behavior.
