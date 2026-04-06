# Workflow: Functional Scoping

> Transforms a product idea or feature request into a complete, delivery-ready specification with epics and Jira tickets.

## When to Use

- New feature needs scoping before development
- Existing feature request needs proper specification
- Strategic initiative needs to be broken into deliverables

## Input

Merlijn provides one of:
- A rough feature idea (verbal or written)
- A user research insight that implies a feature
- A strategic priority that needs to be made concrete
- A reference to an existing backlog item

## Steps

### 1. Problem Clarification
Before anything else, nail the problem.

Ask Merlijn (if not already clear):
- What specific user problem does this solve?
- How do users currently deal with this?
- How painful is this (1-5)?
- What evidence do we have that this is real?

Output: 2-3 sentence problem statement. No fluff.

### 2. Impact Assessment
Evaluate before investing in detailed scoping.

- **User impact**: How many users? How often? How painful?
- **Strategic alignment**: Does this serve our north star metric?
- **Differentiation**: Is this a gimmick or truly differentiating?
- **Effort estimate**: T-shirt size (S/M/L/XL) — gut feel is fine here

Output: Quick impact verdict — proceed, park, or kill. With reasoning.

If verdict is "park" or "kill", stop here. Add to backlog with rationale if parking.

### 3. Functional Specification

Write the spec. Keep it tight.

**Template:**

```markdown
# [Feature Name]

## Problem
[2-3 sentences. What's broken or missing? For whom?]

## Solution
[What are we building? Describe the user experience, not the implementation.]

## Scope
**In scope:**
- [Concrete deliverable 1]
- [Concrete deliverable 2]

**Out of scope (and why):**
- [Thing we're NOT doing — reason]

## User Flow
[Step-by-step: what the user does and sees. Keep it linear. Branch only where truly needed.]

## Edge Cases & Risks
[What could go wrong? What's the weird scenario? What assumption might be wrong?]

## Success Criteria
- [Measurable outcome 1]
- [Measurable outcome 2]

## Experimentation
[How do we validate this works? What's the cheapest test? What do we measure?]

## Phasing
[If this is too big for one sprint: Phase 1 = X, Phase 2 = Y. Each phase must deliver standalone value.]
```

### 4. Multi-Perspective Review
Trigger the multi-perspective review (defined in CLAUDE.md).

Review from: User, Mobile Dev, CPO/Strategy, Growth, Business, Privacy/GDPR.

Flag any 🔴 blockers. Resolve or explicitly accept risks before proceeding.

### 5. Epic & Ticket Breakdown

Break the spec into Jira-ready structure:

**Epic**: One epic per feature or phase.
- Title: Clear, action-oriented
- Description: Link to spec, summary of scope

**Tickets**: One ticket per independently deliverable unit of work.
- Title: Verb + noun (e.g., "Implement share button on summary screen")
- Description: What to build, acceptance criteria, edge cases relevant to this ticket
- Dependencies: List if any
- Estimate: Story points or T-shirt size

Rules:
- A ticket should be completable in 1-3 days
- If a ticket needs a call to clarify, the spec is insufficient — fix the spec
- Don't create tickets for things that are out of scope

**Next step:** Once the epic is created, run [Feature Measurement](./feature-measurement.md) (`/measure-feature`) to generate tracking and metrics tickets before build starts.

### 6. Documentation

- Save spec to `/specs/[feature-name].md`
- Update `/registry/registry.json`
- If approved by Merlijn: push to Confluence and create Jira tickets via MCP
- Archive previous versions if updating an existing spec

### 7. Feedback

Offer feedback prompt (as defined in CLAUDE.md).

## Quality Gates

This workflow is NOT complete unless:
- [ ] Problem is validated (evidence cited or gap acknowledged)
- [ ] Impact assessment says "proceed"
- [ ] Spec passes multi-perspective review with no unresolved 🔴
- [ ] Tickets are independently deliverable
- [ ] A developer could start working without asking questions
- [ ] Total spec is readable in under 2 minutes
