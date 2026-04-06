# Design: Shipping, Release & Activation Process

> Date: 2026-02-19
> Status: Approved
> Problem: Features ship but don't get systematically activated or evaluated. Learning loops are slow, and users don't always discover new capabilities.

## Goals

1. **Faster learning loops** — ship and know within days whether it's working
2. **Higher feature activation** — users discover and use what we build

## Key Decisions

### Explore / Exploit / Polish Classification

Every feature gets classified before release. A feature area (like Care Circle) can contain both Explore and Exploit work:

- **Explore**: New capability that didn't exist before (e.g., profile page with FAQ)
- **Exploit**: Doubling down on proven mechanics (e.g., extending sharing with personal messages)
- **Polish**: UX improvements, bug fixes, performance

This classification drives the communication plan and learning cadence.

### Communication Matrix

| Channel | Explore | Exploit | Polish |
|---|---|---|---|
| App store notes | Yes | Yes | Yes |
| In-app notification center | Yes | Yes | Yes |
| Push notification | Yes | — | — |
| Email (Customer.io) | Yes (dedicated) | Batched | — |
| LinkedIn | Yes | — | — |
| Instagram | Yes | Yes | — |
| Internal Slack | Yes | Yes | Yes |
| Friday demo | Yes | Yes | — |

**Rationale:**
- LinkedIn = professional/investor/partner audience → new capabilities only
- Instagram = user community → anything that makes Ditto better
- Email = personal → Explore gets dedicated email, Exploit gets bundled digest (cadence TBD with Customer.io)
- Friday demo = team alignment → Explore and Exploit, not polish

### Pre-Release Readiness Gates

Release is blocked until both learning readiness and activation readiness are confirmed:

**Learning ready:**
- Success hypothesis defined (behavior change, metric, threshold)
- Mixpanel tracking implemented and verified in staging
- Week 1 + Week 2 checks scheduled

**Activation ready:**
- Feature tier classified (Explore / Exploit / Polish)
- Communication plan filled per matrix
- Release notes drafted (EN + NL)
- In-app notification content ready
- Social content prepared (per matrix)

**Deploy:**
- Code complete, reviewed, merged, QA sign-off
- Deployed to production
- Tracking verified in production

### Workflow (Brookflow-operated)

**Step 1: Classify and prepare** (when feature enters QA)
- Pull epic from Jira, classify tier
- Check for success hypothesis — draft one if missing
- Generate pre-release readiness checklist in Jira epic

**Step 2: Draft activation content** (before deploy)
- App store release notes (EN + NL)
- In-app notification content
- Social content per matrix (LinkedIn for Explore, Insta for Explore+Exploit)
- Post drafts in Slack for review

**Step 3: Ship and verify** (deploy day)
- Verify Mixpanel tracking in production
- Publish release notes and communications per matrix
- Post in #releases-mobile
- Add to Friday demo queue

**Step 4: Connect to learning loop**
- Schedule Week 1 + Week 2 checks
- Add feature to next product strategy meeting's Release Evaluation table
- After Week 2: log learning, update verdict

## Implementation

1. Update `pm-workspace/how-we-run-product/shipping-and-release/README.md` with new matrix, readiness gates, and internal rituals
2. Create `pm-workspace/workflows/shipping-and-release.md` with the Brookflow workflow
3. Connect to the `prepare-product-strategy-session` workflow (shipped features auto-populate evaluation table)

## What This Does NOT Cover

- Build and QC process (see Ways of Working on Confluence)
- Growth experimentation / A/B testing (see Niek's Statsig page)
- Content creation guidelines (separate page, coming soon)
- Customer.io email cadence (TBD once tool is set up)
