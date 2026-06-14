# Care Circle
> Source: DG-Care Circle-020226-220454.pdf
> Last Updated: November 18, 2025 | Status: Released to Production (November 16, 2025)
> Owner: Merlijn van Breugel

## Why We Built Care Circle

**The Vision**: Healthcare is personal, but never solitary. When someone faces a health challenge, their circle of loved ones faces it alongside them. Yet healthcare systems isolate patients behind privacy walls.

**What users showed us**: Before Care Circle existed, 30% of all Ditto summaries were already being shared with family via WhatsApp and Signal. People were building care circles — we just weren't helping them do it effectively.

**The Problem**: Current solutions fail at the interface where care touches others:
- **Epic/MyChart**: Complex proxy access, clinical-only, no mobile design
- **WhatsApp**: Health updates lost between grocery lists, no privacy controls
- **Existing platforms**: Either too clinical (portals) or too social (messaging)

When healthcare journeys become serious, people share with up to 100 people. This isn't oversharing; it's how humans navigate health challenges.

**Business Case — Network Effects & Flywheel**:
- Each patient invitation brings new users into Ditto
- Followers become future patients who need to share their own care
- Natural viral loop: patients → loved ones → future patients
- Transforms Ditto from single-user tool to network platform

**Validated Demand**: Consistent user requests, investors identified as key differentiator, 30% organic sharing proves PMF.

## How It Works

**Core Flow**: Patient generates summaries → shares specific events via invite links → followers receive notifications and view in Ditto app → patient maintains full control with granular privacy.

### v1 Features (November 2025)
- Summary sharing with optional section exclusions
- Invite links via WhatsApp, Signal, email
- Follow requests requiring approval
- Per-event privacy controls, follower removal
- Notifications (requests, acceptances, new shares)
- End-to-end encryption, EU data residency

### v2 Roadmap
- Granular follower groups (different access per relationship)
- Search within Ditto for existing users
- Event engagement (reactions, comments)
- Link management controls and custom expiration
- Auto-share settings for specific individuals

## Forward-Looking Strategy

**Doubling Down on the Interface**: Care Circle = strategic commitment to the interface where care touches others (formal caregivers, practical helpers, emotional support).

Building at the intersection of:
- **Clinical clarity** (what the doctor actually said)
- **Social support** (who needs to know and how to help)
- **Practical coordination** (what happens next and who does what)

**Future: Visualizing Healthcare Journeys** (Polarsteps for healthcare)
- Where you are in your care journey
- What's happening now and what comes next
- How different threads of care connect
- Where others can meaningfully contribute

## Competitive Positioning

| Solution | Strength | Where Ditto Wins |
|---|---|---|
| WhatsApp/Signal | Universal, familiar | Organization, privacy, healthcare context, permanence |
| Epic MyChart | Direct EHR connection | Ease of sharing, multiple recipients, clarity, mobile-first |
| CaringBridge | Trusted platform, social support | AI clarity, granular privacy, clinical data, EU standards |
| Carenzorgt | Deep EHR integration (Nedap), GGZ leader | Consumer-first design, clarity over clinical access, network effects |

**Key Differentiators**:
1. AI-powered clarity (capture, transcribe, explain)
2. Granular per-event privacy controls
3. Mobile-first consumer design
4. End-to-end encryption with EU data residency
5. Built for the interface where care touches others

## Development Process
- **Sep-Oct 2025**: Discovery & Design (3-4 weeks user research, validated 30% sharing behavior)
- **October 2025**: Technical Development (backend, encryption, invite system, iOS + Android)
- **Oct-Nov 2025**: Testing & Refinement (functional, security, performance; team testathon Nov 10)
- **Nov 16, 2025**: Production Release (soft launch, real-time monitoring)
