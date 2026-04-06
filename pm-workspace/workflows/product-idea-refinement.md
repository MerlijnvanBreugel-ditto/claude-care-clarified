# Workflow: Product Idea Refinement

> Takes raw product ideas and shapes them into well-structured backlog items ready for prioritization and eventual scoping.

## When to Use

- Grooming the product backlog
- Processing new feature requests from users, partners, or team
- Reviewing and upgrading existing backlog items
- Translating user research insights into actionable ideas

## Input

One of:
- A raw idea (from Merlijn, team, user feedback, or Mixpanel insight)
- A batch of backlog items to review and refine
- A strategic theme to generate ideas for

## Steps

### 1. Idea Capture

If not already structured, capture the raw idea:

```markdown
## [Idea Title — verb + outcome]

**Source**: [Where did this come from? User feedback / analytics / team / strategy / partner]
**Raw input**: [The original unfiltered idea or observation]
```

### 2. Problem Validation

Challenge the idea immediately:
- **Is this a real problem?** What evidence do we have?
- **How many users does this affect?** (all / segment / edge case)
- **How often do they encounter it?** (daily / weekly / rarely)
- **What do they do today?** (workaround / nothing / leave)
- **Is this OUR problem to solve?** (or is it better solved elsewhere)

If the problem isn't clear or real → mark as "Needs Research" and specify what research would validate it.

### 3. Strategic Fit

Score against Ditto's priorities:

| Criterion | Score (1-5) | Notes |
|---|---|---|
| Solves user pain | | |
| Moves north star metric | | |
| Enables growth/virality | | |
| Strengthens differentiation | | |
| Partnership value (Menzis, etc.) | | |
| Technical feasibility | | |

**Total**: /30

Gut check: Is this score surprising? If the number says "high" but your gut says "meh" (or vice versa), flag the disconnect and discuss.

### 4. Refinement

Shape the idea into a standard backlog item:

```markdown
# [Idea Title]

**Priority score**: [X/30]
**Status**: [Raw / Needs Research / Refined / Ready for Scoping]

## Problem
[1-2 sentences]

## Proposed Solution
[High-level — what would this look like? Not a spec, just direction.]

## Expected Impact
[What changes for the user? What metric moves?]

## Open Questions
[What do we NOT know yet? What needs validation?]

## Cheapest Validation
[If we're not sure: what's the fastest way to learn? User interview? Fake door? Analytics check?]

## Dependencies
[Does this require other work first? Other teams?]

## Size Estimate
[T-shirt: S / M / L / XL]
```

### 5. Backlog Placement

Recommend where this fits:
- **Now**: High impact, validated, ready for scoping → trigger functional-scoping workflow
- **Next**: High potential, needs minor validation or depends on current work
- **Later**: Interesting but not urgent, or needs more research
- **Kill**: Low impact, poor fit, or solved by other means → explain why

### 6. Batch Mode

When processing multiple ideas:
- Present a summary table with: Idea | Score | Status | Recommendation
- Highlight the top 3 by impact
- Flag any ideas that conflict with or complement each other
- Identify patterns (e.g., "3 of these ideas point to the same underlying problem")

### 7. Documentation

- Save refined ideas to `/specs/ideas/[idea-name].md`
- Update `/registry/registry.json`
- If patterns emerge, note them in `/backlog/backlog.json` as potential strategic insights

### 8. Feedback

Offer feedback prompt (as defined in CLAUDE.md).

## Quality Gates

- [ ] Every idea has a clear problem statement (not a solution masquerading as a problem)
- [ ] Strategic scoring is honest, not inflated
- [ ] Open questions are specific and answerable
- [ ] Cheapest validation is actually cheap (not "let's build an MVP")
- [ ] Recommendations are decisive — no "it depends" without saying what it depends on
