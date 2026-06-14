# Linear Project Templates

In Linear, projects represent a body of work with a clear goal and end state. Every project — whether it's a new feature, an AI quality improvement, or an infrastructure migration — needs to answer the same fundamental questions: **why are we doing this, what are we building, and how will we know it worked?**

The template below is universal. At the bottom, category-specific guidance helps you tailor sections to the type of work.

---

## Universal Project Template

```markdown
## Category
<!-- Pick one: Product Feature | Product Improvement | AI Improvement | Infrastructure -->

## Context & Problem
<!-- What situation, insight, or trigger led to this project? What problem are we solving or what opportunity are we pursuing? Who or what is affected? If there's prior research or an idea spec, link it here. -->

## Goal
<!-- What outcome are we targeting? Frame as a result, not a deliverable. Bad: "Build X." Good: "Enable Y so that Z." -->

## What We're Building
<!-- Describe what changes once this ships. For user-facing work: what will the user see and experience? For technical work: what will be different about the system? A developer should understand the "what" and "why" without a separate call. -->

## Why This Matters
<!-- How does this project contribute to our goals? What's the expected impact on Monthly Active Users, retention, product quality, or system reliability? Be specific about which lever this pulls and for which segment or system. If this is an improvement to something that already works: why is it worth investing more here? -->

## Substantiation
<!-- What evidence supports this? Use at least one: -->
<!-- - User data: interviews, feedback, observed behavior, support tickets -->
<!-- - Analytics: Mixpanel data, funnel analysis, cohort behavior -->
<!-- - Market research: competitor patterns, benchmarks, trends -->
<!-- - Technical evidence: error rates, latency data, incident history -->
<!-- - Grounded reasoning: clear logic chain with stated assumptions -->

## Success Criteria

<!-- What does success look like, and how will we measure it? -->

| Metric | Current baseline | Target | How we track | Evaluate by |
|--------|-----------------|--------|--------------|-------------|
|        |                 |        |              |             |

## Scope

**In scope (smallest version that delivers value and lets us learn):**
-

**Intentionally deferred (and why):**
-

<!-- If this can be phased: Phase 1 = X, Phase 2 = Y. Each phase must deliver standalone value. -->

## Effort & Complexity

| Dimension | Notes |
|-----------|-------|
| Engineering | |
| Design | |
| AI / data | |

## Dependencies
<!-- What could block this? Other projects, teams, external partners, legal/privacy, data sources, migrations. -->
-

## Risks & Open Questions
<!-- What could go wrong? What assumptions are untested? What needs to be resolved before or during build? -->
-
```

---

## Category-Specific Guidance

Each category emphasizes different aspects of the template. Use this to calibrate how much depth each section needs.

### Product Feature
New user-facing functionality that doesn't exist today.

| Section | Emphasis |
|---------|----------|
| Context & Problem | User problem with evidence. Who experiences it, how painful, how frequent? |
| Goal | User outcome. What changes in their experience? |
| What We're Building | Describe from the user's perspective — what they see and do |
| Why This Matters | Impact on Monthly Active Users: does this drive acquisition, activation, engagement, or referral? |
| Substantiation | User research, feedback, or analytics strongly preferred over intuition alone |
| Scope | MVP thinking — what's the smallest version that delivers core value and collects data? |
| Effort | Flag design complexity and any new UI patterns needed |

### Product Improvement
Enhancing something that already exists and already works.

| Section | Emphasis |
|---------|----------|
| Context & Problem | What's underperforming or frustrating? Show the gap between current and desired state |
| Goal | Measurable improvement — "from X to Y" |
| What We're Building | What changes vs. what stays the same |
| Why This Matters | Why is it worth investing more here? What's the ceiling if we don't improve this? |
| Substantiation | Analytics and user feedback are key — show the current performance data |
| Success Criteria | Baseline is critical. You can't claim improvement without knowing where you started |
| Effort | Usually lower design/engineering effort — flag if migration or breaking changes are involved |

### AI Improvement
Model quality, summary accuracy, prompt engineering, AI pipeline changes.

| Section | Emphasis |
|---------|----------|
| Context & Problem | What's wrong or suboptimal about current AI output? Specific examples help |
| Goal | Quality outcome — "summaries correctly capture X in Y% of cases" |
| What We're Building | Model changes, prompt changes, pipeline changes, evaluation changes |
| Why This Matters | Direct link to product quality and user trust. How does this affect user-perceived value? |
| Substantiation | Example outputs, error analysis, user complaints about summary quality |
| Success Criteria | Eval metrics with clear methodology — how do we score quality before and after? |
| Risks | Content policy issues (Azure OpenAI), edge cases in medical language, regression risk |

### Infrastructure
Security, performance, technical debt, compliance, DevOps.

| Section | Emphasis |
|---------|----------|
| Context & Problem | What's the technical risk or constraint? What happens if we do nothing? |
| Goal | System outcome — "zero manual intervention for X," "p99 latency under Y ms" |
| What We're Building | Technical approach — enough detail for a senior engineer to review and challenge |
| Why This Matters | Does this unblock product work? Reduce incident risk? Meet compliance requirements? |
| Substantiation | Incident history, error rates, latency data, compliance requirements |
| Success Criteria | Concrete acceptance criteria — measurable system states, not vague "improved reliability" |
| Risks | Rollback plan. Is this reversible? What breaks if the migration fails mid-way? |
