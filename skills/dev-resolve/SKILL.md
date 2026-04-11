---
name: dev-resolve
description: Append best-effort inferred answers to open questions in documents or free-form text while clearly labeling confidence and basis. Use only when the user explicitly invokes `$dev-resolve` or `dev-orchestrate` explicitly delegates to this skill to resolve documented open questions. Do not trigger this skill from generic investigation, planning, or implementation requests unless the open-question resolution phase is explicitly requested.
---

# Resolve Open Questions

Take a document or request that contains open questions and append the strongest defensible answers you can infer.

## Inputs

- A local file path, pasted text, or a mixed request with unresolved questions
- Optional constraints such as preserving exact structure, editing in place, answering only some questions, or language

## Output Contract

- Keep the original question text intact
- Append an answer directly below or immediately after each target question when possible
- Label each answer as inference, include confidence, and give a short basis when it is not obvious
- Leave the question open when the evidence is too weak for a responsible answer

Follow `references/markdown-artifact-rules.md` when editing saved markdown artifacts.

## Default Edit Rules

- If the user gives a writable local file, edit it in place unless asked otherwise.
- If in-place editing is risky or ambiguous, create a sibling file with `-inferred` before the extension.
- If the input is pasted text, return the revised text unless the user asks to save it.

## Workflow

1. Identify the real question targets.
2. Group duplicates so the same issue is answered once.
3. Gather evidence from the surrounding text, the local repository, and external sources when needed.
4. Infer the single best answer that remains defensible from the evidence.
5. Append the answer with confidence and basis.

## Inference Rules

- Prefer one best answer over a menu of possibilities unless the evidence is genuinely split.
- Distinguish facts from inference explicitly.
- Use concrete assumptions instead of vague hedging.
- Keep the answer short and decision-useful.

See `references/annotation-examples.md` for lightweight annotation patterns.

## Guardrails

- Do not replace the original question with an answer.
- Do not present guesses as verified facts.
- Do not broaden the document into a redesign or implementation plan unless the user asks for that.

## Quality Bar

- Each appended answer should help the reader move forward.
- Confidence should match the evidence strength.
- The final result should read like a careful augmentation, not a rewrite.
