---
date: 2026-03-17
context: MCO-95 Website 2.0 epic refinement
---

## What went wrong

When creating Jira tickets via `createJiraIssue`, the `description` string parameter doesn't properly interpret newlines for markdown rendering. The result is a wall of text with literal `\n` characters and unrendered `##` headers.

## Why

The `createJiraIssue` tool's `description` parameter is a plain string — it doesn't go through the same markdown-to-ADF conversion as the `editJiraIssue` tool's `fields.description` when `contentFormat: "markdown"` is set.

## Rule

**Always use `editJiraIssue` with `contentFormat: "markdown"` and `fields: {"description": "..."}` for any ticket with structured markdown content.** Either:
1. Create the ticket with a minimal description, then immediately edit it with the full markdown content, OR
2. Create the ticket, then batch-edit all descriptions afterward

Option 2 is more efficient when creating many tickets at once.
