# Shipped Features — Last 3 Months

**Window:** 2026-01-17 → 2026-04-17
**Sources:** Jira (DPMA, MCO, DHE — covers Jan 17 to ~Mar 31) + Linear Product team (Apr 1 onwards)

## Headline

The quarter was defined by **Care Circle V2** — a multi-phase overhaul of the consumer app's follower model (invitations, profiles, sharing, emoji reactions) shipped across DPMA 1.8.0 → 1.8.2. In parallel we closed out two foundational features (Doctor Ditto Phase 1 and Appointment Preparation), stood up the **Customer.io** lifecycle stack end-to-end, and activated **Google Demand Gen** as a new paid channel. Post-migration to Linear (Apr 1), the team shipped a **Discover tab MVP**, **calendar auto-sync default**, **LEGO design system**, and onboarding **intent questions** — the first structured input for Life Moments segmentation.

---

## DPMA — Consumer App Releases (from Jira releases page)

12 releases shipped, ~45 product issues resolved. Sorted newest → oldest.

### 1.8.2 — Care Circle V2 polishing (2026-03-28)
- Design-fidelity pass across Loved Ones tab, follower variants, reaction popover, home (DPMA-2293)
- Calendar push from Ditto events to user's external calendar (DPMA-2206, epic DPMA-1009)
- "I don't have an appointment" option in activation sheet
- "How to use Ditto" onboarding card restored with video carousel on home
- Mixpanel: questions-added tracking; Apple Search Ads attribution fix

### 1.8.1 (2026-03-17)
- Loved Ones tab redesign (Following + Share With split) — DPMA-2134
- Redesigned homepage sections + swipeable new-feature card stack
- Onboarding refactored to coordinator architecture; activation now dynamic based on "what are you using Ditto for"
- Instructional onboarding for Care Circle connections
- Orphaned inbox cleanup when CC access revoked; completed follow-request copy fixes

### 1.8.0 — Care Circle V2 core (2026-03-09)
- **Emoji reactions end-to-end** (DPMA-1966): send/revoke, reaction indicators on cards, inbox in-app messages, push deeplink to source event
- **New follower-initiated invitation flow** + "How Ditto works" infographic + receiver-side accept-follow-request (DPMA-1903)
- **Enhanced follower profiles** (DPMA-1963): profile/settings nav, auto-send profile on approval, read-only follower About view
- **Enhanced sharing** (DPMA-1964): personalised message + follower FE support
- iOS DB migration (ownerId → userId)

### 1.7.12 — iOS only (2026-03-04)
- Fix: users unable to request to join a Care Circle (DPMA-2241)

### 1.7.11 (2026-03-01)
- Activation funnel instrumentation: completion event + skip tracking
- Manual appointment date added to Mixpanel

### 1.7.10 (2026-02-19)
- iOS fix: minimised recorder disappearing on Event Detail when opened from home

### 1.7.9 (2026-02-18)
- New onboarding videos + thumbnails
- 3-dots menu restored across all summaries
- Inbox copy corrections

### 1.7.8 (2026-02-10)
- Batch of High+ priority low-hanging UX improvements
- Inbox notification copy refresh

### 1.7.7 — Doctor Ditto + Appt Prep (2026-02-05)
- **Doctor Ditto Phase 1** (DPMA-1537): in-app AI-doctor help
- **Appointment Preparation Phase 2**: pre-appointment questions (DPMA-1599)

### 1.7.5 — Inbox + Activation (2026-01-29)
- **In-app Inbox v1** (DPMA-1503) — foundation for CC V2
- **Activation fix P1**: auto-create manual appointment for new users (DPMA-1621)
- Dynamic cards on home; Android unclickable-after-follow-back fix

### 1.7.4 (2026-01-19)
- **Change profile picture V1** (DPMA-1488)
- Terms & conditions naming fix

### 1.7.2 (2026-01-12)
- **Doctor Ditto Phase 0** groundwork (DPMA-1605)

### Epic themes across releases
| Epic | Key | Touched |
|---|---|---|
| CC V2 — Invitation flow (P1) | DPMA-1903 | 1.8.0, 1.8.1 |
| CC V2 — Enhanced profiles | DPMA-1963 | 1.8.0, 1.8.1 |
| CC V2 — Emoji reactions (P1) | DPMA-1966 | 1.8.0 |
| CC V2 — Enhanced sharing (P1) | DPMA-1964 | 1.8.0 |
| Inbox Q1 (FE) | DPMA-1639 | 1.7.5, 1.8.0 |
| Doctor Ditto / Appt Prep / Profile pic | DPMA-1640 | 1.7.2, 1.7.4, 1.7.7, 1.7.8 |
| External Calendar integration | DPMA-1009 | 1.8.2 |

---

## Linear — Product Team (Apr 1 → Apr 17)

60 issues completed in the first 17 days on Linear. Migration-to-Linear moment, so heavy on platform/design-system work alongside shipped user-facing features.

### Customer.io — Marketing automation (shipped end-to-end)
- iOS + Android SDK integrated via DittoAnalytics layer (DP-16)
- In-app message triggers live (DP-20)
- Frontend + backend event sync, email + push configured (DP-17, 18, 19)
- MailChimp retired; users backfilled (DP-91)
- Event pipeline observability + retry (DP-71)

### Calendar Integration — auto-sync by default
- Calendar push ramped to 100% after positive A/B signal (DP-67)
- Generalisable **Preferences** settings menu (DP-68, 129)
- First-time-use bottom sheet with auto-sync opt-in (DP-101)
- Default flipped: manual appointments now auto-push to calendar (DP-69)

### Discover Tab — new educational hub (MVP)
- Tab shell + coordinator shipped; Profile demoted to header icon (DP-98)
- Full-screen video views + iOS/Android nav (DP-97)
- Content defined in NL + EN (DP-62)

### LEGO — shared component library
- L.E.G.O. (Layout/Elements/Groups/Objects) set up as shared design–dev source of truth (DP-27)
- Appointment card, color styles, variants, shadow effects migrated (DP-56, 89, 85, 96)
- Android UI consistency gaps addressed (DP-63)

### AI Quality — resilience & guardrails
- Automatic AI provider failover (no manual intervention on Azure OpenAI outages) — DP-34
- Google Gemini 3 Flash initialised as fallback provider — DP-59

### Survicate — in-app feedback
- Standard feedback form migrated from Typeform (DP-131)
- Surveys launched: "why didn't you record?" (DP-134), "why haven't you invited anyone?" (DP-135)

### Life Moments — first foundation
- **Intent questions in onboarding** (DP-36) — first structured data on why users sign up; groundwork for segmentation

### Zorginnovatieprijs campaign (in-app)
- Full implementation: home card, bottom sheet with YouTube, inbox notification, auto-expiry, Mixpanel tracking (DP-24, 25)

### Other notable
- Deep linking website → app (DP-28)
- Domain map for backend service boundaries (DP-33)
- Auth0 user IDs stripped from Mixpanel (privacy/GDPR) — DP-22, 127
- Android 16 KB memory page size support (Play Store compliance) — DP-128
- Background recording QA verified across iOS/Android (DP-21)
- QR-triggered recording deep-link tracking (DP-70)
- Pregnancy lead-gen landing page: assets, video, testimonials, NL translations (DP-110, 111, 115)

---

## B2B / Partnerships (DHE project)

Seven partnerships closed or activated in the window:
- **Haaglanden Medisch Centrum** (hospital) — 2026-03-27
- **Harteraad** (cardiovascular patient org) — 2026-03-31
- **Hematon** (blood cancer patient org) — 2026-03-31
- **Autoscriber** (integration) — 2026-03-30
- **Fysio.ai** (integration) — 2026-03-30
- **Innovatie tweedaagse Huisartsopleiding NL** (GP training conference) — 2026-04-08
- **Conference pipeline aligned to Life Moments** (DHE-284) — 2026-04-14

---

## Marketing, Content & Website (MCO)

- **Website 2.0** rebuild in Framer shipped as a wave (Mar 24 → Apr 13): new homepage, Professionals page, Privacy & AI page, NL translations, domain transfer. Parent epic MCO-95 still open in Jira despite work being live.
- **Google Demand Gen campaigns** live (DPMA-2242, 2026-03-30) — new paid channel activated
- **Zorgverhalen 2.0** relaunch (Phases 1 + 4)
- **Trouw article** published (earned media)
- **Health Valley Event 2026** participation
- **Instagram Ground Up** rebuild
- **B2B content workflow** playbook

---

## Counts

| Source | Metric | Count |
|---|---|---|
| Jira DPMA | Releases | 12 |
| Jira DPMA | Issues resolved | ~45 |
| Jira all projects | Epics resolved | 24 |
| Jira all projects | Stories resolved | 76 |
| Linear Product | Completed issues (Apr 1–17) | 60 |

---

## Flags / Caveats

- **Jira page cap risk**: the cross-project search returned exactly 100 issues. Jan 17 → Mar 9 is empty in those results — likely earlier epics paginated out. If used for a public stakeholder update, re-run with tighter date slices.
- **Website 2.0 parent epic** (MCO-95) is still `In Progress` in Jira despite the work being live. Either close it or report the 23 child stories as the shipment.
- **ZeroClaw** and the **Life Moments analytics pipeline** (Linear) did not ship in this window — both are in exploration/planning. The onboarding intent question (DP-36) is the first operational Life Moments foothold.
