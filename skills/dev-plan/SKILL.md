---
name: dev-plan
description: Create, update, and execute ExecPlans for complex work in this repository using references/PLANS.md as the governing method. Use only when the user explicitly invokes `$dev-plan` or `dev-orchestrate` explicitly delegates to this skill to create, update, or execute an ExecPlan. Do not trigger this skill from generic requests for specifications, reviews, or direct implementation unless plan-driven execution is explicitly requested.
---

# ExecPlans

Create or execute an ExecPlan that follows `references/PLANS.md`.

## Inputs

`dev-plan` supports three main input shapes:

1. a free-form implementation request that needs planning first
2. an upstream design or investigation document that should be turned into an ExecPlan
3. an existing ExecPlan under `$PWD/docs/plans/` that should be resumed and executed

When the input is ambiguous, prefer treating non-plan markdown as source material for plan creation instead of executing it directly.

## Output Contract

- Create or update exactly one ExecPlan under `$PWD/docs/plans/`
- Keep the plan as a living document while work progresses
- When executing a plan, continue updating the same plan file instead of creating a second plan

Follow `references/markdown-artifact-rules.md` for saved-plan formatting and path handling.

## Core Rules

1. Read `references/PLANS.md` first and follow it closely.
2. Do not jump into implementation from a free-form request or upstream note before producing or updating the plan.
3. Keep all required living sections current while execution proceeds.

## Plan File Management

- Create new plan files under `$PWD/docs/plans/`
- When the input is source material, create or update the target plan there
- When the input is an existing ExecPlan, keep working in that same file

## Execution Authorization

Execute an ExecPlan only when one of these is true:

- the user says `Execute the plan`
- the user directly provides an existing dev-plan-generated ExecPlan file path or pasted plan content

Do not treat vague approval such as `OK` or `go ahead` as authorization to start coding.

## Guardrails

- Do not invent requirements that the source material does not support.
- Do not let the plan drift away from the actual implementation state.
- Do not create a second competing plan for the same active workstream unless the user explicitly wants that reset.

## Quality Bar

- A novice should be able to execute the plan using the plan file plus the current repo.
- The plan should explain purpose, observable outcomes, concrete steps, and validation clearly enough to resume from any stopping point.
