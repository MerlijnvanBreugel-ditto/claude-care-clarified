# S2 — Implications for ditto

**Prepared:** 2026-06-10 · **Branch:** `claude/market-research-synthesis-ltz3lu`
**Reads:** `S1` (framework & direction) through the product/strategy lens of the prior round (`reused/13-synthesis-final.md`, `reused/14-moat-and-platform-strategy.md`). Source files in brackets `[Mx]`.

> Purpose: turn the market view into a discussable set of where-to-play / what-to-watch / what-to-avoid calls for the team. Opinionated by design; every call is gated on evidence, not assumed.

---

## 1. The five things we now know with high confidence

1. **The "comprehension gap" is real and admitted from inside the system.** ~70M Germans have an ePA but ~3.6% use it; NL PGO uptake is low and MedMij itself now lists "more understandable" as a 2026 goal `[M3,M4]`. ditto's core thesis — the bottleneck is *understanding/using* health data, not *accessing* it — is corroborated by the flagship national systems' own failure to drive use.
2. **The category is validated and contested — but the leaders are locked out of the EU.** Five US giants launched record-ingesting health assistants in one quarter; ChatGPT Health is GDPR/MDR-blocked from the EU/UK/CH `[M4]`. Demand is proven; the EU door is held open by regulation — for now.
3. **ditto has a near-mirror direct competitor: Kin.** Kin Health (meetkin.com) records visits → plain-English summaries with action items → role-tiered "care circle," raised a $9M seed (Maveron, May 2026), and its roadmap (a longitudinal "health graph") *is* ditto's roadmap `[M5]`. ditto is not first.
4. **Patient summaries are being commoditised from two directions.** Clinician scribes wrap after-visit summaries into their envelope (Dragon Copilot lands in NL early 2026; Epic Emmie explains labs in MyChart), and Big Tech assistants subsume "explain my lab" `[M4,M8]`. The standalone "AI explains a document" feature is the most exposed.
5. **Retention is a category property, and an episodic summary is structurally a churner.** ~71% of health-app users gone in 90 days; the appointment summary is the symptom-tracker failure mode at the visit level `[M6,M7]`. A great summary wins the first moment; it does not, alone, produce a companion's retention curve.

## 2. Where ditto can win — the defensible position

The differentiators that **survive commoditisation** are not features; they are structural `[M4,M5,M8]`:

- **EU-native trust & regulation.** GDPR-native consent, EU/NL data residency, AI Act/MDR posture, and a non-referral business model. This is precisely what blocks ChatGPT Health and what Kin's US, free-forever, *referral-monetised* model cannot cleanly replicate in Europe `[M4,M5]`. Trust is the moat the incumbents structurally cannot copy fast.
- **The caregiver as a first-class co-user.** The entire "caregiver comprehension" cell of the market map is empty — *none* of the 2026 Big Tech assistants model the loved one `[M4]`. This is ditto's least-contested wedge and is legally enabled (EHDS digital representatives; NL DigiD Machtigen; DE ePA representatives) `[M3]`.
- **Cross-provider, longitudinal synthesis in the EU's multi-portal reality.** Not a single after-visit note (scribes' output) but understanding that follows the patient across providers over time `[M4,M8]`.
- **Grounded & cited, in patient language.** Borrow OpenEvidence's architecture (licensed evidence + inline citations + refuse-when-unsure) for a register OpenEvidence deliberately does not serve — the patient and their family `[M6]`.
- **Condition-agnostic for serious illness.** The only real companions (Outcomes4Me/Mika, Jasper, Belong) are oncology-locked; cross-condition serious illness is uncovered `[M4]`.

**One-line position:** *the EU-anchored, GDPR-native, caregiver-inclusive, grounded-and-cited patient-comprehension layer* — the part neither the US scribes nor the US consumer-AI giants are positioned to own in the Netherlands.

## 3. The retention problem ditto must solve (the make-or-break)

From the consumer-health teardown, the appointment summary must become a **recurring, anticipatory, compounding daily question**, or it inherits the 90-day churn curve `[M7]`. The transferable test — apply to every "Living Health Companion" feature:

1. **Daily-relevant question** the user already re-asks (not just our push notification).
2. **Changing answer** day to day (static dashboards fail).
3. **Effort ≤ reward, felt today** — passive/auto-capture (EHR/summaries/wearables), not manual logging.
4. **Compounding personal data** — each day visibly improves tomorrow's answer (the moat, reflected back).
5. **Life-stage / salience hook** — post-diagnosis, medication change, pregnancy, chronic onset.
6. **Social / reassurance loop** — caregiver/partner sharing (ditto's natural strength).
7. **Identity, not illness** — frame around agency, not a sick identity.

The cycle-tracker pattern translated to clinical care: *"given your last appointment and what's changed since, here's what to watch / do / ask today"* — refreshed daily, smarter with every visit `[M7]`. Note the EU constraint: passive capture and partner-sharing are harder under GDPR, so build the compounding loop on data the user has already consented to share — which is also ditto's moat.

## 4. What to watch (the encroachment radar)

| Threat | Why it matters | Trigger to act |
|---|---|---|
| **Kin** `[M5]` | Near-mirror product + roadmap, well-funded for a US push | EU launch; any EU data-residency / multilingual move |
| **Dragon Copilot (NL, early 2026)** `[M8]` | Scribe with after-visit summaries landing in ditto's home market | NL hospital deployments bundling patient summaries |
| **Epic "Emmie"** `[M4,M8]` | Plain-language explanations inside the portal patients already have | Cross-provider + caregiver features; EU hospital rollout |
| **Big Tech health AI (ChatGPT Health et al.)** `[M4]` | Owns the Q&A/aggregation layer; validated demand | EU localisation / GDPR-compliant EU launch |
| **Hedy AI** `[M5]` | Most EU-credible patient-side rival (30+ languages, GDPR docs, real-time translation) | Caregiver role tiers; NL traction |
| **Oncology companions going cross-condition** `[M4]` | MDR/DiGA base + expansion engine (Belong playbook) | Outcomes4Me/Mika launching non-oncology |

## 5. Business model & go-to-market read

- **Pure D2C subscription is the hardest-funded, hardest-retained path** `[M1,M2]`. The market's survivable model is **B2B2C** — couple the patient experience to a distribution + reimbursement partner.
- **EU rails:** Germany's **DiGA** is the clearest patient-facing reimbursement on-ramp (and a credibility anchor), though small in absolute terms; NL has no DiGA-equivalent app formulary but reimburses digital care on par with in-person `[M1]`. NL B2B2C counterparties: **zorgverzekeraars, hospital groups, GP cooperatives, pharma** `[M2]`.
- **Avoid the medical-device trap.** Babylon and Woebot show diagnosis/triage/therapy claims invite an AI Act + MDR high-risk burden that can kill the product. Position as **information / comprehension / preparation / companion**, not diagnosis `[M6]`.

## 6. The honest risks (hypotheses, not wins)

- **Time-bound EU moat (~18–36 months).** GDPR/MDR blocks US giants *today*; they will localise. The window to build EU trust + data integrations + caregiver habit is open now `[M4]`.
- **Big Tech / OS bundling.** If Apple/Google bundle a serious-illness, caregiver-inclusive companion into the OS health app, the standalone thesis weakens `[M4]`.
- **Adoption-gap cuts both ways.** The low PGO/ePA uptake that is ditto's opportunity is also a market-education burden ditto inherits `[M3]`.
- **Daily engagement, monetisation, and network effects are unproven** for this product `[reused/13]`. Retention (Section 3) is the existential question.
- **Integration cost is real and per-country** (MedMij certification in NL, ePA/gematik in DE) `[M3]`.

## 7. The strategic question to hold

> Are we building a daily, caregiver-inclusive, EU-trust **comprehension companion** that happens to start with summaries — or an excellent summary tool that the scribes and Big Tech will absorb?

Every roadmap decision should be tested against: does it (a) deepen the **daily, compounding, anticipatory** loop (Section 3), and (b) lean on a moat the US incumbents **structurally cannot copy** in the EU (trust, caregiver, cross-provider, reimbursement) (Section 2)? The market has validated the destination and is racing toward it from both sides; ditto's edge is the EU-native, trust-first, caregiver-inclusive path — earned one validated loop at a time.
