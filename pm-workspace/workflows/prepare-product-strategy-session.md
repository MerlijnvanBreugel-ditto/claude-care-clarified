# Workflow: Prepare Product Strategy Session

> Prepares the weekly product strategy meeting by creating a pre-populated Confluence page, pulling live data from Jira, and prompting each participant for input.

## When to Use

- Every week before the Thursday product strategy meeting
- When Merlijn says "prepare the strategy session" or similar

## Participants

| Person | Role | Prep responsibility |
|---|---|---|
| Merlijn | Product & Strategy | Strategic context, user support patterns, Go/No-Go updates |
| Niek | Growth & Metrics | North Star progress, key metrics, analytics surprises |
| Ilayda | Design & Research | Top 2-3 user research findings, usability signals |
| Iman | Dev & Delivery | Technical risks, capacity flags, feasibility concerns |
| Yury | CTO & Architecture | Architecture considerations, tech debt signals, cross-team deps |

## Steps

### 1. Create Meeting Page

Duplicate or create a new Confluence page under the Product Strategy space (`DG`).

- **Title format**: `YYMMDD - Product Strat` (e.g., `260226 - Product Strat`)
- **Parent page**: Product Strategy Cadence section
- **Reference template**: [260219 - Product Strat](https://dittocare.atlassian.net/wiki/spaces/DG/pages/820740103/260219+-+Product+Strat)

### 2. Pull Release Data from Jira

Query Jira for recent and in-progress epics in the DPMA project:

```
# Recently shipped (for evaluation subsections)
project = DPMA AND issuetype = Epic AND status = Done AND resolved >= -14d ORDER BY resolved DESC

# In progress (for roadmap table)
project = DPMA AND issuetype = Epic AND status = "In Progress" ORDER BY updated DESC
```

Populate:
- **Section 1 (Release Evaluation)**: Create a subsection per shipped epic (see template structure below)
- **Section 4 (Roadmap - In Flight)**: All in-progress epics with owner and status

### 3. Carry Forward Unresolved Items

Check the **previous week's** meeting page for:
- Features with verdict "Need data" or "Iterate" that haven't been resolved → carry into this week's evaluation
- Open decisions/actions not yet completed → carry into Decisions & Actions table
- Impediments still unresolved → carry forward

### 4. Pre-fill Signal Prompts

For Niek's section, pull the latest North Star metric value if available from Mixpanel or the last meeting page. Leave as placeholder if not accessible.

### 5. Publish and Notify

- Push the completed page to Confluence
- Share the page URL with the team
- Optionally send a Slack message: "Product Strat prep is live — please fill in your section before Thursday: [link]"

### 6. Post-Meeting: Capture Decisions

After the meeting, ensure:
- All shipped features have a verdict (no blanks)
- Decisions & Actions table is filled with owners and due dates
- "Iterate" items are added to the Jira backlog or [Idea Board](https://dittocare.atlassian.net/jira/polaris/projects/BIGB/ideas/view/5417433)
- Key learnings are captured (even if just 1-2 bullets)
- Update `/registry/registry.json` with the new meeting page

### 7. Feedback

Offer feedback prompt (as defined in CLAUDE.md).

## Template Structure

The meeting page follows five sections:

### Section 1: Release Evaluation (centerpiece)

Each shipped feature gets its own subsection with:

```markdown
### [Feature Name] — [DPMA-XXXX](link) | vX.X.X

**Signal**
- *Usage & feedback:* [User feedback, support tickets, qualitative signal]
- *Analytics:* [Mixpanel data, screenshots/graphs welcome]

**Open questions**
- [Questions that determine: kick off next phase, shape next phase, or kill]

**Verdict:** Working | Iterate | Rethink | Need more data

**Next action:** [What happens now]
```

For complex features (e.g., Activation Fix), add a callout linking to a dedicated evaluation page rather than cramming everything into the meeting template.

### Section 2: Fresh Signals

Role-specific prep sections, max 3 bullets per person. Filled before the meeting.

### Section 3: New Ideas to Triage

Link to the [Idea Board](https://dittocare.atlassian.net/jira/polaris/projects/BIGB/ideas/view/5417433). Table for ideas surfaced that week.

### Section 4: Roadmap & Delivery

In-flight epics (6-week view) and impediments.

### Section 5: Decisions & Actions

Captured during meeting with owner + due date.

## Quality Gates

- [ ] Every shipped feature has its own subsection with Jira link
- [ ] Signal section has structured prompts (usage/feedback + analytics)
- [ ] Complex features link to dedicated evaluation pages
- [ ] In-flight epics are current (no stale items from >2 months ago)
- [ ] Previous week's unresolved items are carried forward
- [ ] Each participant has a clearly labeled section for prep
- [ ] Idea Board link is present in section 3
- [ ] Page is published at least 24h before the meeting
