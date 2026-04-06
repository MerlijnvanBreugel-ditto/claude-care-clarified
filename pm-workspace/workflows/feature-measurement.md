# Workflow: Feature Measurement

> Given a refined epic, generates measurement work items so nothing ships without proper tracking.

## When to Use

- After functional scoping produces an epic (output of [Functional Scoping](./functional-scoping.md))
- Before build starts
- Any feature evaluated at Week 1/2 (see [Experimentation & Learning](../how-we-run-product/experimentation-and-learning/))

## Input

Jira epic key (e.g., `DPMA-1964`) or spec file path (e.g., `pm-workspace/specs/care-circle-v2.md`).

## Output

3 Jira stories under the epic, created **sequentially** with validation between each:

| # | Story | Owner | When | Content |
|---|---|---|---|---|
| 1 | **Define Business Metrics** | PM (Merlijn) | Before build | Hypotheses, metrics, baselines, targets, kill thresholds |
| 2 | **Define Tracking Plan** | Growth (Niek) | After Story 1 validated | Events, properties, dashboard spec |
| 3 | **Implement Tracking** | Engineering | During build, blocks release | Instrument + verify events |

Each story is created only after Merlijn validates the previous one (he may edit directly in Jira/Confluence). Story 3 must be Done before release ([anti-pattern fix](../how-we-run-product/shipping-and-release/#anti-patterns)).

## Steps

### 1. Load Epic Context

Find all existing documentation — don't rely solely on Jira:
- Confluence pages linked from epic or parent
- Spec files in `pm-workspace/specs/`
- [Tracking approach](../context/tracking-approach.md) for reusable events
- [Ditto Metrics Framework](https://docs.google.com/spreadsheets/d/19st40l2ZYNNaF5TZ8MXZlssCjmiaJ7cLhYmT36k73ac/edit?gid=1484002407#gid=1484002407) for L1/L2 metric mapping
- [Care Circle tracking sheet](https://docs.google.com/spreadsheets/d/19st40l2ZYNNaF5TZ8MXZlssCjmiaJ7cLhYmT36k73ac/edit?gid=1641519238#gid=1641519238) for existing event names and properties

If documentation is insufficient, **ask Merlijn** before proceeding.

Extract: problem statement, user segment, success criteria, feature classification (Explore/Exploit/Polish).

| Classification | Depth | Required |
|---|---|---|
| **Explore** | Full | Hypothesis + mechanism, behavior + outcome metrics, kill thresholds + criteria |
| **Exploit** | Standard | Behavior + outcome metrics, targets |
| **Polish** | Light | Health metrics only (crash rate, task completion, latency) |

### 2. Generate Business Metrics

Use [Hypothesis Template](../how-we-run-product/discovery/hypothesis-template.md). Tables, not prose.

**Explore:** Hypothesis → Mechanism → Metrics table (with kill thresholds) → Kill criteria.
**Exploit:** Metrics table only, no kill thresholds.
**Polish:** Health metrics only.

Query Mixpanel MCP for baselines. Flag gaps as `[NEW — no baseline]`.

### 3. Generate Tracking Plan

**Before creating any events, validate against the [tracking sheet](https://docs.google.com/spreadsheets/d/19st40l2ZYNNaF5TZ8MXZlssCjmiaJ7cLhYmT36k73ac/edit?gid=1641519238#gid=1641519238):**
- [ ] Fetch existing events and properties
- [ ] Extend existing events with new properties (prefer over creating new ones)
- [ ] Document what's already tracked and needs no changes
- [ ] Only create new events when no existing event covers the trigger

**Naming convention — match the tracking sheet exactly:**
- Events: Title Case with feature prefix and dash separator
  - `Care Circle - Follow Request Sent`, `Invite Sent`, `Summary Created`
- Properties: `snake_case`
  - `request_age_hours`, `invite_channel`, `following_count_before`

**Output structure — use [tracking plan template](../specs/measurement-templates/02-define-tracking-plan.md):**
1. Existing Events to Extend (+ new properties)
2. Already Tracked (no changes needed)
3. New Business Events (genuinely new only)
4. Granular UI Events (existing `button_tapped` / `screen_viewed` patterns)
5. Dashboard spec (chart → type → question it answers)

### 4. Create Ticket 1: Business Metrics

Present Step 2 output (business metrics) to Merlijn. Ask:
1. Metrics capture what matters? Anything missing?
2. Baselines and targets realistic?
3. Hypotheses sharp enough?

Once approved, create the Jira ticket:
- **Title:** Short, action-oriented (e.g., "Define Business Metrics")
- **Description:** Jump straight into content. No preamble.
- **Acceptance criteria:** Native markdown checkboxes (`- [ ]`).
- Story, assigned to Merlijn.

**⏸️ STOP. Wait for Merlijn to validate.** He will likely edit directly in Confluence/Jira. When he signals ready, reload the ticket to pick up his changes before proceeding.

### 5. Generate Tracking Plan (using validated business metrics)

Re-read Ticket 1 from Jira/Confluence to incorporate Merlijn's edits. Then execute Step 3 (Generate Tracking Plan), ensuring events and properties align with the validated business metrics.

Present the tracking plan to Merlijn. Ask:
1. Events cover all the metrics we defined?
2. Properties capture the right context?
3. Anything engineering will push back on?

Once approved, create the Jira ticket:
- Story, assigned to Niek (Growth).
- Event catalog + dashboard spec.

**⏸️ STOP. Wait for Merlijn to validate.** Same as above — he may edit directly. When ready, reload before proceeding.

### 6. Create Ticket 3: Implement Tracking

Re-read Ticket 2 from Jira/Confluence to incorporate Merlijn's edits. Then create the implementation ticket:
- Story, assigned to Engineering.
- Blocked by Ticket 2. **Blocks release.**
- Links to Ticket 2 as source of truth — don't duplicate event catalog.
- Acceptance criteria: each event verified in Mixpanel debug view.

### 7. Update Registry

Update `pm-workspace/registry/registry.json`.

### 8. Feedback

Offer feedback prompt (as defined in CLAUDE.md).

## Quality Gates

- [ ] Feature classification determined
- [ ] Metrics match classification depth
- [ ] Baselines are real numbers or flagged as new
- [ ] Ticket 1 (Business Metrics) approved by Merlijn before creating Ticket 2
- [ ] Ticket 1 edits reloaded before generating tracking plan
- [ ] Tracking plan validated against tracking sheet — no duplicate events, naming matches
- [ ] Ticket 2 (Tracking Plan) approved by Merlijn before creating Ticket 3
- [ ] Ticket 2 edits reloaded before creating implementation ticket
- [ ] Concrete event names engineering can implement directly
- [ ] All acceptance criteria use `- [ ]` checkboxes
- [ ] Ticket 3 blocks release

## How This Connects

```
[Idea] → Refinement → Functional Scoping → FEATURE MEASUREMENT → Build → Ship → Learn
                                                    │
                                          ┌─────────┼─────────┐
                                          │         │         │
                                    Business    Tracking   Implement
                                    Metrics     Plan       Tracking
```

- **Upstream:** [Functional Scoping](./functional-scoping.md)
- **Downstream:** [Shipping & Release](../how-we-run-product/shipping-and-release/)
- **Evaluation:** [Experimentation & Learning](../how-we-run-product/experimentation-and-learning/)
