---
name: dev-review
description: Review code changes or existing code areas in two passes, save one review note under $PWD/docs/reviews, and deduplicate against prior same-target reviews. Use only when the user explicitly invokes `$dev-review` or `dev-orchestrate` explicitly delegates to this skill for a findings-first change review or code review. Do not trigger this skill when the goal is only to build a reading path, draft a spec, or continue implementation without an explicit review phase.
---

# Review

Review a target in two passes:

1. a strict first pass for discrete actionable issues
2. a broader second pass for intent, security, regression, testing, operations, and AI-readability checks

## Modes

- `change-review`: diffs, commits, commit ranges, branches, or pull requests
- `code-review`: existing features, files, directories, modules, entry points, stack traces, or failing tests

If the user does not name a mode, infer it from the target. If both are present, start with `change-review`.

## Inputs

- A diff, commit, branch comparison, pull request, file, directory, feature name, stack trace, failing test, or bug report
- Optional context such as PR description, intended behavior, issue link, focus areas, or language

## Output Contract

- Save exactly one main review note under `$PWD/docs/reviews/`
- State the exact mode and target near the top
- Use the newest same-target review artifact as the deduplication baseline
- Keep findings first, and emit only net-new findings or material status changes

Follow `references/markdown-artifact-rules.md` for saved-review formatting and path handling.

## References

- `references/official_review_principles.md`: strict first pass for `change-review`
- `references/code_review_principles.md`: strict first pass for `code-review`
- `references/second_pass_checklist.md`: broader second-pass checks
- `references/output_examples.md`: concise clean-result and delta-only examples

## Workflow

1. Resolve the exact mode and review target.
2. Inspect the latest same-target review artifact first when one exists.
3. Gather only the context needed to review the target well.
4. Run Pass 1 using the rubric for the selected mode.
5. Run Pass 2 using the second-pass checklist.
6. Deduplicate within the current review and then against the prior review series.
7. Save one concise review note.

## Scope Rules

- For `change-review`, focus on issues introduced by the reviewed change.
- For `code-review`, focus on concrete problems visible in the current code and nearby evidence.
- Keep confirmed bugs separate from risks or missing-context questions.

## Guardrails

- Do not stop after the first valid issue.
- Do not inflate severity.
- Do not repeat unchanged older findings as if they were new.
- Do not spend tokens summarizing every file.

## Quality Bar

- Findings should be discrete, actionable, and tied to the smallest useful location.
- Clean repeat reviews should explicitly say there are no new actionable findings instead of restating the old series.
