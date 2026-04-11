---
name: dev-investigate
description: Investigate a topic deeply in the current repository and save one evidence-based report under $PWD/docs/investigations. Use only when the user explicitly invokes `$dev-investigate` or `dev-orchestrate` explicitly delegates to this skill for a persisted deep dive, root-cause analysis, comparative study, or background investigation. Do not trigger this skill from generic implementation or specification requests unless the investigation phase is explicitly requested.
---

# Topic Investigation Reporter

Create one detailed research report under `$PWD/docs/investigations/`.

## Inputs

- Topic text, pasted markdown, or a `.md` file path to use as the investigation brief
- Optional constraints such as scope, audience, language, deadline, or required format

When the user provides markdown, treat it as the primary brief instead of paraphrasing it into a shorter surrogate.

## Output Contract

- Save exactly one main report under `$PWD/docs/investigations/`
- Keep the report evidence-based and traceable
- Prefer local repository evidence first, then add external evidence when the repo is insufficient or recency matters
- Reuse or update an existing same-topic report only when the user explicitly asks for that behavior or the current run is clearly a continuation of the same artifact

Follow `references/markdown-artifact-rules.md` for saved-report formatting and path handling.

## Workflow

1. Determine scope from the topic or provided brief.
2. Investigate local repository evidence first.
3. Add external primary sources when local evidence is not enough.
4. Synthesize findings into a structured report with explicit evidence and unknowns.
5. Save the report under `$PWD/docs/investigations/`.

Create new reports from `references/TEMPLATE.md`.

## Local Investigation Checklist

- Search broadly with `rg` for topic terms and nearby synonyms.
- Read relevant code, tests, configs, docs, and notes.
- Expand outward from entry points into callers, dependencies, and adjacent modules when they may change the conclusion.

## External Investigation Checklist

- Use the web only when unstable facts or missing local context require it.
- Prefer primary sources.
- Distinguish facts from inferences.

## Guardrails

- Do not jump into implementation after the investigation is complete.
- Do not hide unresolved gaps behind generic summaries.

## Quality Bar

- Every major claim should point to explicit evidence.
- Unknowns should be called out directly instead of guessed away.
- Another engineer should be able to use the report to decide what to do next.
