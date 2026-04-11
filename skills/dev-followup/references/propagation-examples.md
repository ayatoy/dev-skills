# Propagation Examples

Use these examples when deciding whether follow-up changes should update downstream artifacts.

## Update The Spec

- The follow-up changed a visible workflow, acceptance criterion, API, CLI, schema, or invariant.
- Example: a delete flow now requires confirmation and soft-delete retention.

## Update The Walkthrough

- The important reading order changed enough that the old path is misleading.
- Example: the fix moved the semantic center from a route handler into a shared service.

## Update The Recap

- The follow-up materially changed current status, unresolved risk, or the handoff story.
- Example: a post-merge bug fix removed the main blocker that the recap still calls out.

## Do Not Propagate

- The change is implementation-only and preserves the same requirement boundary.
- The old reading path still makes sense.
- The recap remains accurate without further edits.
