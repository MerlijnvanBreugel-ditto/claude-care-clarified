---
description: Turn raw input (email, transcript, screenshot context) into a structured Linear issue. Defaults to Product team, flags duplicates, asks before creating when unclear.
argument-hint: [raw input — paste anything: bug report, email thread, voice memo, screenshot caption]
---

You are running the **Create Linear Issue** workflow as Mewtwo.

## Your task

Turn the raw input below into a well-structured Linear issue, following `pm-workspace/workflows/create-issue.md` exactly.

## Workflow summary (read the full file before acting)

1. **Load the workflow file** at `pm-workspace/workflows/create-issue.md` — it contains the templates and rules.
2. **Classify** the input: bug / feature / spec iteration / ops task / spike.
3. **Pick the team** — default Product. Override only when the input clearly belongs to Operations, Partnerships, or Marketing. If genuinely ambiguous → ask Merlijn.
4. **Pick the assignee** — default Merlijn. Override if the input names someone ("put it on Hester's name"). For bugs that need triage, default to Merlijn.
5. **Check for duplicates** (mandatory, blocking) — use `mcp__linear-server__list_issues` with title keywords + project filter. If a likely duplicate exists, **STOP and flag it** before creating. Wait for Merlijn's call.
6. **Ask before creating** if the input contradicts itself, a critical field is missing AND not inferrable (which user, which device, which appointment), or two voices conflict. Don't ask for things that can be filled with "TBC".
7. **Apply privacy hygiene** — redact phone numbers and personal addresses unless operationally required (flyer ship-to is fine; user phone in a bug ticket is not).
8. **Draft using the matching template** from the workflow file (bug / feature / ops / spec iteration).
9. **Create the issue** via `mcp__linear-server__save_issue` with team, title, description, assignee, labels (`Bug` for bugs), and `relatedTo` for any linked tickets.
10. **Report back** with the URL, a 1-sentence summary of judgment calls, and the standard feedback prompt:

```
Feedback? (optional)
1. Yes, let me share
2. Not now / later
3. Not needed — you were perfect
```

## Quality bar

A dev or ops person should be able to act on the ticket without messaging Merlijn for clarification. Lead with the call (Direction / Action), supporting context goes below.

## Raw input

$ARGUMENTS
