---
name: dev-brainstorm
description: Run a free-form brainstorming conversation, keep a single canonical inbox brief under $PWD/docs/inbox, and stay in ideation mode until the user explicitly transitions. Use only when the user explicitly invokes `$dev-brainstorm` or an upstream workflow explicitly delegates to this skill for ideation, vague-request shaping, or option comparison. Do not trigger this skill from generic requests for implementation, investigation, review, or recap.
---

# dev-brainstorm

Maintain one canonical inbox note under `$PWD/docs/inbox/` while helping the user think through a problem in open-ended conversation.

The saved note is not a transcript. It is the current best brief for what the user may want to do next.

## Inputs

- Plain text, pasted notes, file paths, directories, screenshots, or session history
- Optional constraints such as language, topic split, or filename hint

If the user provides explicit input, treat it as the primary source. Otherwise use the relevant session history.

## Output Contract

- Create or update exactly one main inbox note under `$PWD/docs/inbox/`
- Keep the note abstract enough to remain useful as upstream input for `dev-investigate` or `dev-orchestrate`
- Distill the conversation continuously instead of logging raw chat
- Prefer updating the active inbox note over creating a competing note for the same thread

Follow `references/markdown-artifact-rules.md` for saved-note formatting and path handling.

## Workflow

1. Resolve the primary input.
2. Create or update the inbox note near the start of the run.
3. Seed the note with the current problem shape, motivations, constraints, options, and open questions.
4. Stay in brainstorming mode and keep refining the note after each meaningful exchange.
5. Tighten the brief only when the user explicitly asks to transition to the next step.

Create new notes from `references/TEMPLATE.md`.

## Brainstorming Mode

- Stay in ideation mode while this skill is active.
- Do not invoke downstream workflow skills or start implementation during the brainstorming run.
- Do not auto-exit because the discussion feels complete.
- When the user gives explicit transition intent, update the note one last time and then allow the next workflow to begin.

See `references/transition-signals.md` for representative transition and non-transition examples.

## Distillation Rules

Keep the note focused on durable signal:

- what the user may want to do
- why it matters
- current framing
- constraints and preferences
- viable directions and tradeoffs
- open questions
- user-provided reference targets when explicitly supplied

Prefer concise synthesis over transcript-like logging.

## Guardrails

- Do not invent requirements that were not stated or strongly implied.
- Distinguish confirmed asks from your own framing.
- Do not narrow the downstream scope prematurely.
- Do not create multiple partial notes for the same active thread unless the user asks for separation.

## Quality Bar

- Another engineer should be able to read the inbox note and understand the likely next problem, why it matters, and what remains uncertain.
- The note should get sharper over time without collapsing exploration too early.
