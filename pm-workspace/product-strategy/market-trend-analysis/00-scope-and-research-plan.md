# Market & Trend Analysis — Scope & Research Plan

> Outside-in only: competitors, market, trends. Created 2026-05-30. Status: Phase 1 running.
> Engines: `deep-research` (fan-out + adversarial verify) · `market-research` skill (sourcing discipline) · foresight methods (applied manually).
> Boundary: Ditto-internal product + company-strategy data are handled by other agents. Merlijn synthesizes all three into one overview.

## Decision frame (set by Merlijn)

| Axis | Setting |
|---|---|
| Mode | **Open broad scan**: map the landscape evenly, let the synthesis surface priorities. |
| Horizon | **Layered**: 12–18mo tactical + 3–5yr strategic. |
| Geography | **EU primary, US secondary** (US as leading signal). NL and UK sit inside the EU focus. |
| Out of scope (Merlijn's calls) | **Capital / M&A** (just raised, low relevance). **Defensibility** is a *strategic conclusion Merlijn draws from this research*, not a research topic. **Tech/product trends** (wearables ladder, generative UX, agentic) are a light, deferred later pass. |

## Priority (reweighted from Merlijn's steer)

| WS | Workstream | Priority | Why |
|---|---|---|---|
| **A** | EU regulation, certification & AI-error incidents | 🔴 HIGH | The rules are both moat and kill-switch. Merlijn wants recent (last month/year) news of clinical/health AI tools criticized or making mistakes, plus AI Act, MDR/CE certification, EHDS, GDPR. |
| **B** | EU reimbursement of health apps | 🔴 HIGH | The business-model trend that matters most post-raise. Which apps are reimbursed, *why*, and *how much*. As purely European as possible. |
| **C** | Competitive landscape | 🔴 HIGH | Sword Health (fast-moving big AI-care player). Whether ambient scribes are moving consumer/patient-side and offering patient summaries. Direct patient-summary competitors. |
| **D** | US demand-side macro trends | 🟡 MED | US as leading signal for EU demand. |
| **E** | Incumbent platforms (quick look) | 🟡 MED | Epic/MyChart, Apple/Google Health, MedMij/PGO, NHS App: are they encroaching on patient summaries? Quick scan only. |
| — | Tech/product trends, Capital/M&A, Defensibility | ⚪ DEFERRED | Per Merlijn: light/later, or his own strategic synthesis. |

## Workstream research questions

**A. EU regulation, certification & AI-error incidents**
- EU AI Act: status (2026), classification of medical/health AI (high-risk), obligations, timelines, conformity assessment; meaning for a patient-facing AI summary app.
- Medical device certification: MDR, CE marking, MDCG software-as-medical-device guidance, Class I vs IIa triggers for health/AI apps; UK MHRA equivalent briefly.
- EHDS: status, what it enables for app developers (data access/portability), key dates.
- GDPR special-category health data: recent developments for health apps.
- **Incident scan**: last ~12 months (especially the last month) where clinical/health AI tools were criticized, errored, caused harm, were recalled, or faced regulatory/press scrutiny. EU emphasis, notable global included.

**B. EU reimbursement of digital health apps**
- Which EU markets reimburse and how: Germany DiGA, France PECAN/early-access, Belgium mHealthBELGIUM, NL, Nordics, others.
- Concrete reimbursed-app examples: name · country · category · what it does · *why* it qualified (evidence bar) · *how much* (€) · date.
- Trend direction: expanding/contracting, evidence bar rising/falling, eligibility of patient-facing (non-DTx) and AI tools.
- Is there a plausible pathway for a Ditto-type care-companion/summary tool?

**C. Competitive landscape**
- **Sword Health**: product scope (AI clinical care + care platform), scale, funding/valuation, geography, recent moves, threat read. Note obvious peers (e.g. Hinge Health).
- **Ambient scribes** (Abridge, Nuance/Microsoft DAX, Nabla, Heidi, Suki, Corti, Tortus): are any moving consumer/patient-side? Which generate patient-facing summaries? Which are purely B2B? Signals of B2C ambition. EU players emphasized.
- **Direct patient-summary competitors**: who turns a visit into a patient-friendly, shareable summary *for the patient*? EU + notable global.

**D. US demand-side macro trends**
- Patient empowerment / e-patient movement, health-literacy crisis, caregiver economy, aging + chronic burden, consumer health-AI adoption ("Dr. ChatGPT"), after-visit-summary demand, family care coordination. Quantify; read across to EU.

**E. Incumbent platforms (quick look)**
- Epic/MyChart, Apple Health, Google Health, NL MedMij/PGO, NHS App: do they already deliver patient-friendly visit summaries / AI health understanding, and are they a threat to Ditto's "front door" ambition?

## Engines → outputs

| Engine | Domains | Output |
|---|---|---|
| Competitor analysis | C, E | Tiered map + disintermediation read per step. |
| Trend analyzer (now) | A, B, D | Source-graded "what is actually happening." |
| Trend predictor (future) | applied over all | S-curve stage + weak signals + base-rate, a 2×2 scenario, and a *trend → implication → threat/opportunity* ledger across both horizons. |

## Execution

1. **Phase 1 (running):** 5 parallel briefs (A–E), source-graded, broad-but-graded (map, don't exhaust).
2. **Checkpoint:** Merlijn picks the 2–3 highest-stakes threats/opportunities.
3. **Phase 2:** targeted deep dives on those.
4. **Phase 3:** foresight synthesis.
5. **Deliverable:** one **Market & Trend Map** that slots beside the product + company-strategy agent outputs for Merlijn's single overview.

## File index
- `00-scope-and-research-plan.md` — this spine
- `brief-A-regulation-certification-incidents.md`
- `brief-B-eu-reimbursement.md`
- `brief-C-competitive-landscape.md`
- `brief-D-us-demand-macro.md`
- `brief-E-incumbent-platforms.md`
