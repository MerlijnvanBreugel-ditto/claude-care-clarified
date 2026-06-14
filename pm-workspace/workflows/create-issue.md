# Workflow: Create Linear Issue

> Turns raw input into a Linear issue that's structured, scoped, deduped, and ready for someone to act on without a follow-up call.

## When to Use

- Merlijn pastes a user message, email, support thread, or screenshot context and says "create an issue"
- A bug needs to land on the engineering board
- An ops task (flyer ship, materials send, partner follow-up) needs tracking
- A spec or iteration needs reformatting from messy notes into a proper ticket

## Input

Anything: WhatsApp transcript, email thread, screenshot + caption, voice memo transcript, half-formed thought. The workflow does the structuring.

## Steps

### 1. Classify the input

Pick the type — it determines template and defaults:

| Type | Signals | Default team | Default labels |
|---|---|---|---|
| **Bug** | "doesn't work", "can't tap", screenshots of broken UI, error messages, device + OS mentioned | Product | `Bug` |
| **Feature / iteration** | "we should…", "iterate on…", design proposal, copy change, flow change | Product | none (release label optional) |
| **Spec iteration** | Messy spec or proposal that needs reformatting (often has multiple authors / overlapping notes) | Product | none |
| **Ops task** | "send X to Y", "follow up with partner", physical items, scheduling | Operations | none |
| **Spike / research** | "investigate", "understand if", "feasibility" | Product | none |

### 2. Pick the team

- **Default:** Product.
- **Override only when clear:** explicit mention of Operations / Partnerships / Marketing, or operational nature (shipping, partner outreach, recruitment).
- If genuinely ambiguous → ask Merlijn before creating.

### 3. Pick the assignee

- **Default:** Merlijn (`merlijn@ditto.care`).
- **Override:** if the input names someone ("put it on Hester's name", "assign to Patryk"), use them.
- If the bug needs reproduction first, default to Merlijn for triage rather than guessing engineering owner.

### 4. Check for duplicates (mandatory)

Before drafting, run `list_issues` with title keywords + project filter (if known).

- **If a likely duplicate exists** → STOP. Flag it: "Found PRO-XXX which looks like the same thing because [reason]. Recommend [merge / link as related / create separate because…]." Wait for Merlijn's call.
- **If related-but-not-duplicate** → note it, link via `relatedTo` when creating.
- **If clean** → proceed.

### 5. Resolve unclear / contradictory input

Before creating, ask Merlijn if any of these are true:

- The input contradicts itself (e.g., one part says "remove the checkbox", another says "default it on")
- A critical field is missing AND not inferrable: which user, which device, which appointment, what version
- Two people gave conflicting directions and it's not clear whose wins
- The team / project / assignee isn't obvious

**Don't ask** for things that can be filled with sensible TBC placeholders (exact iPhone model, app version when "latest" was stated). Note them as "TBC" instead.

### 6. Apply privacy hygiene

- **Redact** user phone numbers and personal addresses from ticket bodies — replace with "User" or move to a private-context section if needed.
- **Keep** addresses when the ticket *is* the shipping action (flyer drops, NDA mailing, etc.).
- **Keep** email addresses when the ticket needs them for follow-through.
- **Anonymize** unless the user is explicitly being credited (super user, named ambassador).

### 7. Draft using the matching template

#### Bug template

```markdown
## Problem
[One paragraph: what the user tried, what happened, what should have happened.]

## Device & version
- **Device:** [model]
- **OS:** [iOS / Android version]
- **App version:** [version or "latest, downloaded YYYY-MM-DD"]
- **Language:** [if relevant]

## Steps to reproduce
1. …
2. …
3. **Expected:** …
4. **Actual:** …

## Reporter (if relevant)
[Name + one line of context — super user, usability tester, partner, etc. Direct line to Merlijn if applicable.]

## Original report (NL/EN)
> [Verbatim quote, redacted of phone/address.]

## Notes
- Hypotheses on root cause if any
- Whether others have reported similar
```

#### Feature / iteration template

```markdown
## Context
[Why now. Background in 2-3 sentences.]

## Direction
[What we're doing and why. Lead with the call, not the discussion.]

## What ships
| | Now | After |
| --- | --- | --- |
| … | … | … |

## Acceptance criteria
- [ ] …
- [ ] …
- [ ] No regression in [metric]

## Open questions
- …

## Related
- [Linked tickets — duplicates flagged, predecessors, follow-ups]
```

#### Ops task template

```markdown
## Action
[What to do, in one sentence. Quantities if relevant.]

## Address / contact
[Only the fields needed to act.]

## Context
[Who this is for and why it matters — super user, partner, ambassador, etc.]

## Original request (if relevant)
> [Verbatim, redacted as needed.]
```

#### Spec iteration template (when reformatting messy proposals)

Same as **feature / iteration**, plus:
- A "Superseded proposal" section preserving prior thinking when direction changed
- Explicit "Direction (X — leading)" header when one author's call wins over another's

### 8. Create the issue

Use `mcp__linear-server__save_issue` with:
- `team`, `title`, `description` (markdown, literal newlines, no escape sequences)
- `assignee` (email or display name)
- `labels` (array; `Bug` for bugs)
- `project` if implied by content
- `relatedTo` for any linked tickets surfaced in step 4

### 9. Report back

Return:
- The issue URL
- A 1-sentence summary of the call you made (team picked, dedup result, any TBCs)
- Any judgment calls Merlijn might want to override

### 10. Offer feedback

```
Feedback? (optional)
1. Yes, let me share
2. Not now / later
3. Not needed — you were perfect
```

## Quality checklist

Before sending the issue:

- [ ] A dev / ops person could act on this without messaging Merlijn
- [ ] The "why" is clear, not just the "what"
- [ ] Phone numbers and home addresses are redacted unless operationally required
- [ ] Duplicates checked and flagged
- [ ] Open questions live in their own section (not mixed into requirements)
- [ ] No filler — every section earned its place

## Common mistakes

| Mistake | Fix |
|---|---|
| Creating before checking duplicates | Always run `list_issues` first |
| Guessing missing critical fields | Ask, or mark as "TBC" with a note to follow up |
| Including phone numbers in bug tickets | Redact — they don't help reproduction |
| Burying the call in a wall of text | Lead with Direction / Action; supporting context goes below |
| Picking a team because the input *mentions* them | Pick the team that *acts* on it |
| Following the letter of conflicting input | If two parts contradict, ask Merlijn whose call wins |
