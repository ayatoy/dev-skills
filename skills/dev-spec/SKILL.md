---
name: dev-spec
description: Draft a decision-ready specification under $PWD/docs/specs from an investigation report or free-form request plus supporting context. Use only when the user explicitly invokes `$dev-spec` or `dev-orchestrate` explicitly delegates to this skill to produce a feature, product, or technical specification before implementation. Do not trigger this skill for step-by-step implementation planning or generic coding requests unless specification work is explicitly requested.
---

# Specification Drafter

Create one decision-ready specification under `$PWD/docs/specs/`.

## Inputs

- An investigation report, pasted markdown, or a file path
- Or a free-form request plus supporting context such as docs, issues, notes, code paths, or requirement memos
- Optional constraints such as audience, spec type, language, goals, non-goals, deadlines, or forbidden approaches

## Output Contract

- Save exactly one main specification under `$PWD/docs/specs/`
- Keep the document traceable: major requirements, decisions, assumptions, and open questions should point back to source material
- Treat the result as a draft unless the user explicitly asks for a final spec
- Reuse an existing same-workstream spec only when the current run clearly continues that artifact or the user explicitly asks for an update

Follow `references/markdown-artifact-rules.md` for saved-spec formatting and path handling.

## Workflow

1. Normalize the input into source material, goal, scope, constraints, audience, and open questions.
2. Extract facts, constraints, and unknowns from the source material.
3. Read local repository context only when the source material is incomplete or ambiguous.
4. Draft a concise spec that separates confirmed facts, proposed decisions, assumptions, and open questions.
5. Save the result under `$PWD/docs/specs/`.

Create new specs from `references/TEMPLATE.md`.

## Drafting Checklist

- identify the problem and audience
- separate goals from non-goals
- derive concrete requirements from available evidence
- define observable acceptance criteria
- call out constraints, tradeoffs, assumptions, and open questions

## Guardrails

- Do not implement code as part of this skill.
- Do not invent requirements or acceptance criteria without labeling them as assumptions or proposals.
- Prefer explicit gaps over false precision.

## Quality Bar

- Another engineer or product manager should be able to challenge each major requirement by tracing it back to evidence.
- The scope should stay decision-oriented instead of turning into an implementation plan.
