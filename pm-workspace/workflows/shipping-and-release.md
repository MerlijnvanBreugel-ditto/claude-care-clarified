# Workflow: Shipping & Release

> Prepares a feature for release by ensuring learning readiness, drafting activation content, and connecting to the learning loop. Run when a feature enters QA or is approaching release.

## When to Use

- A feature is entering QA and heading toward release
- When Merlijn says "prepare the release for X" or similar
- Before any app store submission

## Input

- Jira epic key (e.g., DPMA-1903) or feature name
- Target release date (if known)

## Steps

### 1. Classify and Prepare

Pull the epic from Jira and classify:

- **Explore**: New capability that didn't exist before
- **Exploit**: Doubling down on proven mechanics
- **Polish**: UX improvements, bug fixes

Check the epic for a success hypothesis. If missing:
- Draft one using the [hypothesis template](../how-we-run-product/discovery/hypothesis-template.md)
- Get Merlijn's sign-off before proceeding

Generate the pre-release readiness checklist and add it to the Jira epic description (or as a comment).

### 2. Draft Activation Content

Based on the tier classification, prepare content for each applicable channel:

**All tiers:**
- App store release notes (EN + NL) using the [template](../how-we-run-product/shipping-and-release/)
- In-app notification center content

**Explore only:**
- LinkedIn post draft (benefit-first, professional tone)
- Push notification copy

**Explore + Exploit:**
- Instagram post draft (user-friendly, visual)

**Exploit (email):**
- Queue for next email batch (note in Customer.io backlog)

Post all drafts in #releases-mobile Slack channel for review.

### 3. Verify Readiness

Before deploy, run through the gates:

**Learning ready?**
- [ ] Success hypothesis defined
- [ ] Mixpanel tracking verified in staging
- [ ] Week 1 + Week 2 checks scheduled with dates and owners

**Activation ready?**
- [ ] Release notes approved
- [ ] Social content approved
- [ ] In-app notification content ready

If any gate is not met → flag to Merlijn, do not proceed.

### 4. Ship and Verify

On deploy day:
- Verify Mixpanel tracking in production (not staging)
- Publish release notes to app stores
- Send communications per matrix
- Post in #releases-mobile with summary
- Add to Friday demo queue

### 5. Connect to Learning Loop

- Add the feature to the next product strategy meeting's Release Evaluation table (see [prepare-product-strategy-session](./prepare-product-strategy-session.md) workflow)
- Ensure Week 1 health check is on the calendar
- Ensure Week 2 impact check is on the calendar
- After Week 2: log learning in the Learning Log, update verdict in strategy meeting page

### 6. Feedback

Offer feedback prompt (as defined in CLAUDE.md).

## Quality Gates

- [ ] Feature tier is classified before any content is drafted
- [ ] Success hypothesis exists before release
- [ ] Tracking is verified in production, not just staging
- [ ] Release notes are in benefit language, not feature language
- [ ] Social content is tailored per channel (LinkedIn ≠ Instagram)
- [ ] Feature appears in next product strategy meeting evaluation table
- [ ] Week 1 + Week 2 checks are scheduled with specific dates
