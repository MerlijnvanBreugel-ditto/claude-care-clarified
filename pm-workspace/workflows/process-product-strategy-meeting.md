# Workflow: Process Product Strategy Meeting

> Post-processes the weekly Thursday product strategy meeting by updating the Confluence page with meeting outcomes and staging follow-up actions for approval.

## When to Use

- After every Thursday product strategy meeting
- When Merlijn says "process the meeting" or shares Granola + Confluence links

## Input

1. **Granola meeting notes link** — the recorded meeting with transcript and AI summary
2. **Confluence strategy page link** — the pre-populated page from the prep workflow

## Steps

### 1. Ingest Sources

Fetch Granola notes (summary + transcript) and current Confluence page. Cross-reference against the meeting's three agenda blocks from [How We Plan](https://dittocare.atlassian.net/wiki/spaces/DG/pages/821985281):

| Block | What to extract |
|---|---|
| **Learning** | Verdict updates, new signal on shipped features, learnings |
| **Roadmap Update** | Priority changes, new ideas discussed, Go/No-Go outcomes |
| **Delivery Excellence** | Release timeline changes, new/resolved impediments |

### 2. Update Confluence Page

Enrich the existing strategy page section by section:

| Section | What to update |
|---|---|
| **1. Release Evaluation** | Fill verdicts, add signal discussed verbally, update next steps. Flag features at Week 2+ that need a [Learning Log entry](https://dittocare.atlassian.net/wiki/spaces/DG/pages/820936731). |
| **2. Fresh Signals** | Complete any sections filled verbally but not written pre-meeting. |
| **3. New Ideas** | Update priority/quick take based on discussion outcome. |
| **4. Roadmap & Delivery** | Update epic statuses, add/remove impediments, adjust timeline. |
| **5. Decisions & Actions** | Update carried items status. Add new actions with owner + due date. |

### 3. Append "Process Elsewhere" Section

Add a staging table at the bottom of the Confluence page. Nothing executes until Merlijn approves.

```markdown
## 6. Process Elsewhere

| # | Action | Type | Target | Process | Status |
|---|---|---|---|---|---|
| 1 | [description] | Jira epic/ticket | DPMA | Needs hypothesis before Go/No-Go | Pending |
| 2 | [description] | BIGB Idea Board | BIGB | Use Idea Template, set roadmap status | Pending |
| 3 | [description] | Learning Log | Confluence | Hypothesis → Result → Why → Next | Pending |
| 4 | [description] | Roadmap update | BIGB | Update Now/Next/Later/Unsure | Pending |
| 5 | [description] | Week 1/2 check | Confluence | Per post-launch evaluation process | Pending |
```

Each row maps to an existing process from [How We Run Product](https://dittocare.atlassian.net/wiki/spaces/DG/pages/821919746). No orphan actions.

**Types and their targets:**

| Type | Where it goes | Template/process to follow |
|---|---|---|
| Jira epic/ticket | DPMA project | Requires hypothesis + success criteria before Go/No-Go |
| BIGB Idea Board | [Idea Board](https://dittocare.atlassian.net/jira/polaris/projects/BIGB/ideas/view/5417433) | Use [Idea Template](https://dittocare.atlassian.net/wiki/spaces/DG/pages/821821477), set status + roadmap |
| Learning Log | Experimentation & Learning page | Hypothesis → Result → Why → Next |
| Roadmap update | BIGB board | Update roadmap status (Now/Next/Later/Unsure) |
| Week 1/2 check | Strategy page or dedicated page | Per [post-launch evaluation](https://dittocare.atlassian.net/wiki/spaces/DG/pages/820936731) |

### 4. Review with Merlijn

Present:
1. Summary of what was updated on the Confluence page
2. The "Process Elsewhere" table with proposed actions
3. Any flags (missing owners, overdue actions, features needing Learning Log)

Discuss: which actions to execute now, defer, or drop.

### 5. Execute Approved Actions

Only after Merlijn approves:
- Create/update Jira tickets (DPMA)
- Add ideas to BIGB board with Idea Template
- Write Learning Log entries
- Update roadmap statuses
- Mark each row as Done in the Process Elsewhere table

### 6. Wrap Up

- Update `pm-workspace/registry/registry.json` with the processed meeting page
- Add observations to `pm-workspace/backlog/backlog.json` if gaps were noticed
- Offer feedback prompt (as defined in CLAUDE.md)

## Quality Gates

- [ ] Every discussed feature has an updated verdict or explicit "no change"
- [ ] All new actions have owner + due date
- [ ] Carried-forward items are marked resolved or still open (no ambiguity)
- [ ] Process Elsewhere table links each action to its target process
- [ ] No action is executed without Merlijn's approval
- [ ] Features past Week 2 without a Learning Log entry are flagged
