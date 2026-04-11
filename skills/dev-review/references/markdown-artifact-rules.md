# Markdown Artifact Rules

Use this reference when a skill creates or edits a saved Markdown artifact.

## Core Rules

- Use a UTC filename prefix in `yyyy-MM-dd'T'HH-mm-ss'Z'` format when the skill creates a new artifact.
- If the artifact body includes created or updated timestamps, use the same UTC format there.
- Write the artifact in the user's language unless the user asks otherwise.
- Save normal Markdown content. Do not wrap the whole artifact in an outer fenced code block.

## Links And Paths

- Use repo-local relative Markdown links from the saved artifact to repository files, docs, tests, configs, and directories.
- Prefer link labels that match the repository-relative path the reader expects to open.
- If line precision matters, keep the link target as the file and put the line number in visible text.
- Keep Markdown links renderable. Do not wrap them in backticks or fenced blocks.

## Path Redaction

- Never emit machine-specific absolute filesystem paths such as `/Users/...` in the saved artifact.
- Never emit `file://`, `vscode://`, or similar editor-specific URIs.
- If prose must mention a workspace-rooted path, rewrite it with a `$PWD/...` placeholder.

## Editing Discipline

- Preserve the artifact's local linking style when it already follows these rules.
- Prefer the smallest reasonable diff when editing an existing artifact.
- Keep the artifact previewable in Markdown after the edit.
