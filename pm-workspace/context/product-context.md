# Ditto Care — Product Context

> Last updated: 2026-05-30 (full refresh from Linear, Granola, Slack)
> Status: Living document — update after every major strategic shift
> Prior version: 2026-02-17 (pre-OKR, pre-Code-Red, pre-UK). This refresh corrects metric definitions, team size, tooling, and strategic focus.

## Company

**Ditto Care B.V.** | Rotterdam, Netherlands
Mission: Care. Clarified.
Team: ~16-18 people (grew from ~10) | Stage: pre-Series A | Won a national healthcare innovation award (Mar 2026)

## What We Do

Ditto turns recorded medical conversations into patient-friendly summaries using AI. Patients record their doctor visits, and Ditto produces clear, understandable summaries they can reference and share with the people who care about them. The strategic direction is to evolve from a summary tool into the intelligent care layer for a patient's whole journey, with the care circle (family and caretakers) as the compounding growth loop.

## The Numbers That Matter (state as of late May 2026)

Metric definitions matter here, because the headline "users" figure and the metric the team actually optimizes are different things:

| Metric | Meaning | Latest reading | Target |
|---|---|---|---|
| Registered users (cumulative) | All-time installs/registrations (vanity) | 35,000+ | n/a |
| **Core MAU (North Star)** | Users who view ≥1 summary in a month | **~2,080 (27 May); ATH 2,086 (22 May)** | **5,000 by Jun 30; 50,000 by year-end** |
| M1 retention | Month-1 (next-month) retention of summary-viewers | **~40% next-month (flat vs 40% baseline); ~78% within-month** | 60% |
| D14 activation | Install → summary viewed within 14 days | **~6-8% blended; ~13% organic; ~27-28% register-based (mature)** | 25% |
| Avg care circle size | Members per active patient (measurement contested, see caveats) | **~1.62 (rigorous, 22 May); 1.44 members added** | 3.4 |
| Partner registrations (Q2) | Regs attributed to B2B partners | ~293 regs (≈270 partner installs to date) | 2,000 |
| AI-agent FTE deployed | Internal automation in FTE-equivalents | ~0-1.5 live | 15 by end Q2 |

Core MAU is ~36% behind the Q2 pace. That gap is what triggered the Code Red.

> Figures above are reconciled to the live Porygon (Mixpanel) reads from #insights as of 2026-05-30. Full dated breakdown, definitions, and data caveats: [`data/product-analytics.md`](../data/product-analytics.md). Note: the team's officially-stated OKR-page values can differ from Porygon's raw reads because of metric definitions (especially retention) and known instrumentation gaps (care circle size, attribution). The earlier "M1 ~15%" figure was the follower deep-creation number, not blended next-month retention.

## North Star Metric

**Core MAU**: users who view at least one summary in a given month. "5K is the signal, not the goal." The 50,000 year-end figure is the Series A milestone. Leading indicators: D14 activation (install to first summary viewed) and M1 retention. The underlying product event is `summary_viewed`.

## Code Red (May 2026) — the dominant strategic context

A leadership alarm raised May 21 ("Code-red pt 1: mitigation of MAU gap") over the gap between the current trajectory and the 50K Series A milestone. Diagnosis: growth is linear rather than exponential, D30 retention sits around 30%, and care circle invite acceptance is around 28%, so churn offsets acquisition and MAU plateaus. The product's dependence on appointments as the activation trigger was named as the core vulnerability.

Decisions taken (hub: #core-decisions, created May 13):
- Keep 50K MAU / Series A as the year-end target (re-evaluate with investors at year-end).
- Narrow to high-intensity care paths (oncology primary, cardiology) rather than broad consumer targeting.
- Make the **care circle the growth engine** and fix invitation friction immediately (auto-accept, remove the two-step acceptance).
- Go **B2B-only** on go-to-market; park consumer paid campaigns.
- Refocus B2B on existing partners (Menzis/ZN, AYA, Ikazia, Hartklinieken).

Open fork ("Part 2", still pending): **Narrow** (double down on severe care paths) vs **Wide** (reduce appointment dependency to broaden activation). A larger Q3 strategy exercise (Tobias, Bart, Merlijn) lands ~mid-June.

## Q2 2026 OKRs

New operating system since ~Mar 30 (the team did not run formal OKRs before this). Two objectives, weekly squad readouts, Friday review cadence. All target Jun 30.

| KR | Owner | Status | Note |
|---|---|---|---|
| **O2: Build the growth loop that compounds into 5K MAU by Jun 30** | Niek | atRisk | Monthly MAU plan: Mar 1,381 → Apr 2,058 → May 3,066 → Jun 4,568 |
| O2-KR1: 2,000 partner registrations | Bart Voorn | offTrack | ~293 to date |
| O2-KR2: D14 activation 11% → 25% | Niek | atRisk | ~6-8% blended; ~13% organic; ~27-28% register-based (mature). Media spikes depress the blend |
| O2-KR3: avg care circle size 1.34 → 3.4 | ilayda | atRisk | ~1.62 rigorous (22 May) / 1.44 members added; measurement broken (PRO-290) |
| O2-KR4: M1 retention 40% → 60% | **Merlijn** | offTrack | ~40% next-month (flat vs 40% baseline), ~20pp below target; ~78% within-month. The "leaky bucket"; lower-intent paid traffic dilutes 5-10pp |
| **O1: Build the team, habits & foundation to hyper-scale internationally** | Bart Voorn | — | Foundational objective |
| O1-KR1: all new hires onboarded & operational by Jun 1 | Bart Voorn | atRisk | Brand hire at risk on applicant quality |
| O1-KR2: 15 FTE AI agents deployed across depts | Iman | atRisk | ~1.5 FTE impact assessed; ~0 fully live |
| O1-KR3: 100 UK MAU + 2 B2B partners referring outside NL | Olivier | atRisk | UK launch is the vehicle |
| O1-KR4: 100% of significant initiatives follow Proposal & Evaluation | Niek | onTrack | Linear-native idea intake + AI completeness check + RISCE scoring |

## Strategy & Positioning

Ditto positions as the intelligent layer that makes health understandable and pulls in the people who care, sitting between two rejected extremes: a pure social platform (crowded) and a "doctor in your pocket" diagnostic AI (legal risk, becoming an AI research lab). Layered evolution: summaries (strong retention, low volume) → appointment tracking (more data, more sharing) → care intelligence (compounding care journey). Long-term ambition voiced internally: "the digital front door for care in Europe."

Two active exploration threads worth naming:
- **"Beyond Appointments"**: appointments are episodic and cap activation; the team is hunting non-visit activation paths (e.g. retroactive "how was your checkup?" capture, phone-call recording, which is 80% of feature requests).
- **Phone-call recording**: surfaced as the next major unlock (80% of feature requests, 50% of support tickets).

> Naming note: "Care Brain" is this workspace's internal codename for the care-intelligence strategy. It does **not** appear in Granola or Slack. The team's real vocabulary is "care circle" and "care intelligence layer." Keep Care Brain for internal strategy docs; use the team's language in anything shared.

## Segmentation: Life Moments → severe care paths

"Life Moments" remains the internal segmentation lens (serious diagnosis, sudden chronic disease, expecting/young parents, neurodegenerative). Post-Code-Red, operational focus narrowed to high-intensity care paths:

- **Oncology (primary)**: ~50% of current active users are cancer patients. The clear wedge.
- **Cardiology**: Hartklinieken partner channel.
- **Neurodegenerative** and **sudden severe diagnosis**: secondary focus.
- **Expecting/young parents**: a large pregnancy-postcard acquisition cohort was tested (strong uplift, fast care-circle invites, but a broken appointment-to-recording chain).

Onboarding now captures persona + intent (top intent: appointment summaries, ~63%). Note: "Life Moments" as a phrase did not surface in recent meetings; the live operational language is severe / high-intensity care paths.

## Core Product (shipped state)

- **Medical conversation recording** → AI transcription and summarization (Conversation Explainer v2)
- **Patient-friendly summaries** → plain language, structured, actionable; long-press editing
- **Care Circle** → share summaries with family; the designated growth engine (invite friction being removed)
- **Calendar integration** → shipped ~May 30 (app v1.9.9), pulls appointments from the device calendar to widen the activation funnel; flagship activation bet, on-device bilingual medical-keyword scan via remote config
- **Appointment preparation** → AI follow-up appointment + suggested-question extraction
- **Customer.io lifecycle** → live since Apr 24 (welcome series, appointment-prep, post-summary, profile-completion); the retention backbone
- **Platform**: native iOS + Android

## Key Partnerships (refreshed)

| Partner | Type | Status |
|---|---|---|
| **Menzis** (+ ZN, CZ) | Health insurer | Reimbursement discussions, no signed deal. ~149-153 attributed regs. Benchmark: Hello 24/7 reimbursed at €6-12/mo. |
| **Ikazia** | Hospital (lead B2B) | Most active; go-live slipped Jun 30 → July; QR-code activation a hard requirement; attribution tracking broken. |
| **AYA** (Jong en Kanker) | Oncology network | Progressing: user-research kickoff + ambassador outreach (Tobias). |
| **Hartklinieken** | Cardiology clinics | ~53-61 attributed regs. |
| **UMCG** | Research | Most structurally advanced: non-WMO pediatric asthma feasibility study (children 6-12). Legal flag: Merlijn's dual role (Ditto owner + UMCG employee) is a conflict of interest needing Board notification; DPIA/MDR work underway. |
| **Juvoly** | Transcription vendor | Role changed: clinical partnership stalled ("team implosion"); now a candidate STT provider in the transcription A/B test. |
| **UK pipeline** | Hospitals/charities | No signed partner yet: Macmillan, Leeds Teaching Hospitals NHS, South London & Maudsley. HLTH Europe (Amsterdam, June) is a major BD push. |

## Technical Stack (filled)

- **Mobile**: native iOS (Swift) + Android
- **AI summary**: Conversation Explainer v2, GPT-4.1 primary with Gemini 3.5 Flash fallback/shadow; actively migrating toward Gemini 3.5 Flash on Google Cloud (EU region). New evaluators dropped false-positive rate ~15% → 1-2%; new guardrails in flight after quality incidents (e.g. a summary that inverted a medication stop/continue instruction).
- **Transcription**: Juvoly/Jubilee today; A/B testing Resonate vs Gemini Flash STT.
- **Auth**: migrating Auth0 → Supabase (prod cutover underway).
- **Analytics**: Mixpanel (with Adjust attribution), Customer.io, Survicate; a Mixpanel experimentation engine (feature flags, variant assignment, significance) is being stood up to replace ship-to-100%-and-eyeball.
- **PM tools**: **Linear** is the system of record across 5 teams (Product, Partnerships, Marketing, Operations, Agents). Confluence still hosts the OKR page and some meeting notes. (Jira/Confluence from the old doc are deprecated for product tracking.)
- **Internal AI agents**: a dedicated **Agents team** runs an autonomous B2B-outreach cascade; Linear-native AI triage does idea completeness checks + RISCE scoring; named internal bots include Porygon (Mixpanel analyst), Mr. Mime, Diglett, Cursor.

## Team Structure (filled)

5 Linear teams: Product (PRO), Partnerships (PAR), Marketing (MAR), Operations (OPS), Agents (AGI, created May 22).

| Person | Role |
|---|---|
| **Iman Hashemi** | Co-founder; AI lead; owns the 15-FTE-agents initiative |
| **Tobias Polak** | Co-founder; commercial / legal / strategy; signs external |
| **Merlijn van Breugel** | PM (product + AI); owns retention KR; CE v2, calendar, localization |
| **Niek** | Growth / Product lead; owns the growth-loop objective; runs reviews |
| **Bart Voorn** | Head of Expansion; B2B, partnerships, hiring; owns the foundation objective |
| **Olivier Desloges ("Oli")** | Expansion / UK / B2B |
| **ilayda** | Product / design; care circle owner |
| **Wouter van Wessel** | Growth Engineer (new, ~May 2026); analytics + experiment engine |
| **Jasper Makkinje** | Engineer / analytics / automation (new, ~Apr 2026) |
| **Yury** | Engineering lead (backend/infra); drives the Agents team |
| **Łukasz** | Mobile engineer (was on race-season leave mid-May, still on the team) |
| **Patryk** | Mobile engineer (calendar, appointment prep) |
| **Maciek** | Mobile / QA engineer |
| **Inês Atienza** | Designer |
| **Hester Verhoeven** | Partnerships |

Active hiring: a second mobile dev ("unicorn mobile developer"), a brand lead (final stages), Chief of Staff, AI engineers, B2B support. Recent departures/transitions: Rebecca (content, left pre-April), Joeri (CTO → advisor). Inês/Rebeka leave status was ambiguous as of late May (treat as unconfirmed).

## Known Data Caveats (flag before quoting numbers)

- **Care circle size measurement is broken** (PRO-290) — `follower_count_after` non-numeric since a v1.7.11 payload bug; reconstructed averages (1.44 members added vs 1.62 circle vs the 2.5-2.7 in older daily reports) disagree until fixed.
- **Retention is definition-sensitive** — M0 within-month (~78%) vs M1 next-month (~40%) vs deep creation (~28%) vs follower deep (~15%) are all real and all different. State the definition before quoting.
- **Mixpanel ↔ Adjust attribution is unreliable** — organic vs paid installs cannot be cleanly separated (~52% of May installs are ATT "No User Consent"; UTM source shows `undefined`, flagged "potentially not fixable").
- "35,000+ users" is cumulative, not Core MAU (~2,080). Do not conflate.
- Full Porygon-sourced figures, dated and caveated: [`data/product-analytics.md`](../data/product-analytics.md).

## Product Principles

1. **Patient-first**: every feature serves the patient's understanding.
2. **Simple > Complete**: better to be clear about less than confusing about more.
3. **Share to care**: health is a family matter; the care circle is the loop.
4. **Trust through transparency**: medical data demands absolute trust (and correct AI output).
5. **Validate before building**: cheap experiments before expensive development. Proposal & Evaluation discipline is now an OKR.

---

*This doc is Mewtwo's foundation. Refreshed 2026-05-30 from live Linear/Granola/Slack. Open items to confirm with Merlijn: (1) adopt team "care circle" language vs internal "Care Brain"; (2) UK medical-device registration detail (MHRA Class I vs MDR); (3) Inês/Rebeka leave permanence.*
