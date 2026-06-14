# Hypothesis Template

Use this template when an idea moves toward a [Go/No-Go gate](../product-strategy/how-we-make-decisions.md#gono-go-gate). Every Explore bet requires a hypothesis before it can be approved for delivery.

> *"Most hypotheses fail because they describe WHAT will happen but not WHY. Without the mechanism, you can't debug failure."*
> — **Shreyas Doshi**

---

## Template

```
## [Feature Name]

### Segment
Who benefits most?

### Hypothesis
We believe that [feature] will cause [specific user behavior change],
which will result in [measurable outcome] for [segment].

### Mechanism
Users will [do X differently] because [reason tied to their current pain].

This is the most important part. Without the "because," you can't tell whether
a failure was caused by a bad solution or a bad assumption about user behavior.

### Metrics

| Metric | Baseline | Target | Kill Threshold |
|---|---|---|---|
| Behavior change (Week 1) | [X]% | [Y]% | <[Z]% |
| Outcome metric (Week 2) | [X] | [Y] | <[Z] |
| MAU contribution | [X] | [Y] | <[Z] |

### Kill Criteria
If [leading indicator] doesn't reach [threshold] by [date], we will [action].

### If We're Wrong
We'll know because [specific observable signal].

### Evidence Summary
What did discovery reveal? Link to research, interviews, analytics.

### Four Risks

| Risk type | Assessment | Mitigation |
|---|---|---|
| **Value** (will users want it?) | | |
| **Usability** (can users figure it out?) | | |
| **Feasibility** (can we build it?) | | |
| **Viability** (does it work for the business?) | | |
```

## How this connects

1. Idea enters IDEA Board using the [Idea Template](./idea-template.md)
2. Idea enters Discovery — research, prototyping, user testing
3. Before Go/No-Go: write this hypothesis
4. Go/No-Go gate reviews hypothesis + evidence
5. After launch: [Week 1/2 evaluation](../shipping-and-release/) tests whether the hypothesis held
6. Results logged in Learning Log

---

*A hypothesis without a mechanism is just a wish.*
