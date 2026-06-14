# F8 — The Operational Front Door

> Field brief for the Market Deep Dive. Layer informed: **Operational** (feeds C3). Anchor: **Doctolib**.
> Written 2026-06-09 by Mewtwo. Source-graded inline: **[P]** primary · **[S]** reputable secondary · **[V]** vendor self-report. Figures flagged «unverified» where unconfirmed. Prefer 2024–2026.
> Web access: available. All non-obvious claims carry a URL in the citation list.

## The one-line answer

The operational front door is a **provider-side SaaS / distribution game that is already won in every EU geography that matters**, monetized almost entirely by *providers*, not patients. The winners (Doctolib, DocPlanner, national apps) are now climbing *up* into the intelligence layer from a position of distribution strength. For a 16-person patient-side player, building the front door is not realistic. The strategic question is not "own vs integrate" — it is "integrate, and make sure the integration is not commoditized by the front door owning intelligence first."

---

## (a) One-screen field map

The "front door" is not one market. It is five operational jobs, each with its own winner, payer, and moat shape.

| Sub-layer | Job | EU/NL winner(s) | Who pays | Moat shape | Relevance to Ditto |
|---|---|---|---|---|---|
| **Patient↔provider scheduling** | Book/manage appointments | **Doctolib** (FR/DE/IT), DocPlanner (PL/ES/IT/DE via Jameda), Doctena (DACH/Benelux) | Provider SaaS | Two-sided network + practice lock-in | The anchor. Front-door incumbent. |
| **Referral routing (B2B rail)** | GP → specialist/hospital handoff | **ZorgDomein** (NL, 91% of GPs) | Provider/system SaaS | Institutional integration + de-facto standard | NL-specific; near-monopoly rail Ditto must ride, cannot replace. |
| **Telehealth / on-demand care** | See a doctor now, get a script | Kry/Livi (Nordics/UK/FR), Qare→HealthHero (FR) | Public payer (~90%) + SaaS | Payer contracts + clinician supply | Capital-heavy, payer-gated, low-margin. Not a Ditto game. |
| **Professional messaging** | Clinician-to-clinician secure chat | **Siilo → now "Doctolib Connect"** (550k EU members) | Free to clinicians; enterprise upsell | Clinician network density | Already absorbed by the front-door incumbent. |
| **Second opinion** | Sanity-check a serious diagnosis | Included Health (US, employer), Medexo (DE, insurer) | Employer / insurer (rarely patient) | Expert network + payer contracts | Closest to Ditto's severe-disease moment, but B2B2C payer model. |
| **National front doors** | Government-issued "one app" | NHS App (UK, ~40M), MijnGezondheid.net / PGOs (NL) | Taxpayer / system | Mandate + identity + record access | The structural threat: states are building the free front door. |

**The pattern that runs through the whole field:** every durable winner monetizes the *provider* or the *system*, never the patient directly. And the two strongest commercial winners (Doctolib, DocPlanner) are, as of 2025–2026, both spending their network advantage to climb *into* AI/intelligence — exactly the layer Ditto calls its core. [S][S]

---

## (b) Player teardowns — 7 lenses

### ANCHOR: Doctolib

The reference case for "how you take the operational front door." Studied deepest.

| Lens | Finding | Grade |
|---|---|---|
| **1. Job & moment** | Started single-job: let a patient book a doctor's appointment online, 24/7, without calling. Trigger = "I need an appointment." Expanded to the practice's whole admin spine (calendar, records, telehealth, billing, messaging). | [S] |
| **2. Sticky mechanic** | Not the patient app — the **practice operating system**. Once a practice runs its calendar, patient management, billing-to-Social-Security, and now AI scribe through Doctolib, ripping it out means re-coordinating the entire front office. The patient side is a free funnel that feeds the paid provider side. | [S] |
| **3. Frequency engine** | Provider: daily (it *is* the front desk). Patient: episodic (you book when sick), but **80M patient accounts** create a persistent logged-in identity the platform can re-activate. Frequency lives on the provider side; the patient side is reach, not habit. | [S][V] |
| **4. Monetization** | **99% of ARR is provider subscriptions.** Flat SaaS, ~€139/mo base + modules (Médecin ~€135, telehealth €79, card reader €29) — a full stack can reach ~€4.5k/yr per practice. **2024 ARR €348M (+22.5% YoY)**, loss narrowed to €53.8M (from €87.1M), profitability targeted "in months" as of Apr-2025. €115M R&D (≈⅓ of revenue) into AI. **"Patients don't pay, and Doctolib does not monetize its data."** | [S][P-ish via Sifted] |
| **5. Defensibility / moat** | Textbook two-sided network + deep practice integration. Won **geography by geography** (FR 2013 → DE 2016 → IT 2021), reaching supply-side critical mass locally before rivals could. To displace it you must move *both* sides at once in a single country. **The moat is a distribution/network moat, and in its core geographies it is effectively closed to a new entrant.** | [S] |
| **6. Outcome & graveyard lesson** | Not a graveyard — a winner. €5.8B valuation, IPO-track. Lesson for Ditto is the *inverse* of a graveyard: this is what "owning the front door" looks like at maturity, and it took 12 years + ~€516M-class capital + a country-by-country supply war to build. | [S] |
| **7. EU-applicability** | It *is* the EU benchmark. But note: even Doctolib is **not pan-EU** — 80% of ARR is still France, 17% Germany, <3% Italy. The front door is won **per country**, not continentally. NL is not a Doctolib stronghold. | [S] |

**The Doctolib question Ditto actually cares about — is it climbing into the intelligence layer?**
Yes, unambiguously, and on two fronts:
- **Provider-side intelligence (2025):** an all-in-one practice suite with three AI assistants — a 24/7 telephone assistant, and a **consultation assistant that transcribes the visit in real time and produces structured summaries/notes**. [S] That is conversation-to-summary inside the clinical workflow — adjacent to Ditto's wedge, but sold to the *doctor*.
- **Patient-side intelligence (early 2026):** **"Doctolib Parents,"** a multi-LLM medical assistant for parents of 0–4-year-olds, answering health questions on validated French medical knowledge, EU-hosted, with pediatric/midwife societies as partners. No diagnosis/no prescribing, "personalized responses based on the patient's profile." [S]

**Read for Ditto:** the front-door incumbent is using its distribution to launch a *patient-facing health-question assistant* — the most direct possible encroachment on "understanding → advising." It is starting narrow (a life-moment segment, parents) and credentialed (medical societies). This is the v2 thesis happening *in reverse*: the operational player is reaching up into intelligence, rather than an intelligence player reaching down into operations. Whoever owns the front door gets the first, cheapest shot at the intelligence layer because they already hold the patient relationship and the data exhaust. That is the core threat this brief surfaces.

---

### DocPlanner Group (the pan-EU consolidator)

| Lens | Finding | Grade |
|---|---|---|
| 1. Job & moment | Same job as Doctolib (booking) but built as a **multi-country roll-up**: 13 countries, owns Jameda (DE, ~20k doctors / 8M patients/mo at acquisition), strong in PL/ES/IT/BR/MX. | [S] |
| 2. Sticky mechanic | Practice management SaaS + a public-facing doctor marketplace/reviews directory (SEO-driven patient acquisition). | [S] |
| 3. Frequency engine | Provider daily; patient episodic. ~100M monthly users / 210k+ active paying doctors «vendor/aggregator-sourced, unverified». | [V] |
| 4. Monetization | Provider SaaS. Reached profitability (reported Feb-2026), prepping IPO. | [S] |
| 5. Moat | Network + acquisition-led geographic coverage. | [S] |
| 6. Outcome | Winner, IPO-track. | [S] |
| 7. EU-applicability | The clearest signal for Ditto: DocPlanner is **explicitly repositioning as an "AI-driven clinical workflow / medical-data" company to justify a premium IPO valuation**, expanding an AI Assistant across five countries. [S] | [S] |

**Read:** the *second* front-door winner is making the identical climb into AI/data. Two independent incumbents converging on "front door → intelligence" is a pattern, not a one-off. The front door is being used as the on-ramp to the exact territory Ditto wants to defend.

---

### ZorgDomein (the NL referral rail) — the most NL-relevant case

| Lens | Finding | Grade |
|---|---|---|
| 1. Job & moment | The GP→specialist/hospital **referral** moment — the B2B handoff, not consumer booking. | [S] |
| 2. Sticky mechanic | Embedded in GP information systems as the *standard* referral workflow; also diagnostic requests + consultations. | [S] |
| 3. Frequency engine | Provider daily-operational; invisible to patients. | [S] |
| 4. Monetization | SaaS to the system/providers (PE-backed: Levine Leichtman, Rabo). Exact pricing «unverified». | [S]/[V] |
| 5. Moat | **91% of all Dutch GPs** route referrals through it — a de-facto national standard + institutional integration. Replacing it is a system-level decision, not a competitive one. | [S] |
| 6. Outcome | Quiet near-monopoly on the NL referral rail. | [S] |
| 7. EU-applicability | NL-specific by construction. **This is the rail Ditto's severe-disease patients are *already* travelling on at the diagnosis moment.** Ditto cannot replace it; the question is whether Ditto can *plug into* the referral event (the most decision-dense moment in the journey). | [S] |

**Read:** ZorgDomein owns the single most important *moment* in Ditto's severe-disease beachhead — the referral into specialist/oncology care. It is a partner/integration target, never a build target.

---

### Zocdoc (US) — the cautionary monetization tale

| Lens | Finding | Grade |
|---|---|---|
| 1. Job & moment | Consumer find-and-book in the US insurance maze. | [S] |
| 2. Sticky mechanic | Insurance-aware search + last-minute cancellation fill. | [S] |
| 3. Frequency engine | Episodic patient; ~6M monthly bookings. | [S] |
| 4. Monetization | **Switched from flat $3k/yr subscription to $300/yr + ~$35–$100+ per booking** — and the switch exposed the model's flaw: high-demand urban specialists win cheaply, low-demand/rural providers churn ("inequitable value capture"). ~$200M revenue 2024 (+~20%) «aggregator-estimated». | [S]/[V] |
| 5. Moat | Two-sided network, but **weaker than Doctolib's** — US fragmentation + per-booking friction caused provider churn. | [S] |
| 6. Outcome & graveyard lesson | Survived but stalled relative to ambition. **Lesson: the per-transaction model breaks trust on the supply side and concentrates value in already-popular providers.** A booking marketplace is only as strong as its weakest-monetizing geography. | [S] |
| 7. EU-applicability | Low — EU public-payer systems don't have the US insurance-matching pain Zocdoc monetizes. | [S] |

---

### Kry / Livi (EU telehealth)

| Lens | Finding | Grade |
|---|---|---|
| 1. Job & moment | "See a doctor now" online; scripts, lab tests. | [S] |
| 2. Sticky mechanic | Clinician supply + payer integration (NHS, Swedish regions). | [S] |
| 3. Frequency engine | Episodic acute. | [S] |
| 4. Monetization | Consultation fees, **~90% from public payers**; plus clinic SaaS and pharmacy/lab referral fees. ~$215M revenue (2022) «Sacra, dated». | [S] |
| 5. Moat | Payer contracts + clinician network — but capital-intensive and politically exposed. | [S] |
| 6. Outcome & graveyard lesson | **Two rounds of layoffs in 2022, exited Germany**, then reached profitability across markets (credits AI for cost-out). **Lesson: payer-funded telehealth is a thin-margin operations business that nearly broke a $2B-valued, €516M-funded company.** | [S] |
| 7. EU-applicability | High relevance, low attractiveness for Ditto — it is the opposite of asset-light patient software. | [S] |

---

### Doctena / Jameda (DACH booking)

| Lens | Finding | Grade |
|---|---|---|
| 1–3 | DACH/Benelux booking; provider-daily, patient-episodic. Doctena: 10k+ doctors, 1.5M visits/mo «vendor, ~2021». Jameda: ~20k doctors, 8M patients/mo at 2022 acquisition. | [V]/[S] |
| 4. Monetization | Provider SaaS + (Jameda historically) a reviews/visibility model. | [S] |
| 5. Moat | Regional network — **but consolidating**: Jameda absorbed by DocPlanner (2022). | [S] |
| 6. Outcome | Roll-up targets, not independent winners. | [S] |
| 7. EU-applicability | Confirms the field is consolidating into 2–3 pan-EU SaaS owners. | [S] |

---

### Siilo → "Doctolib Connect" (professional messaging)

| Lens | Finding | Grade |
|---|---|---|
| 1. Job & moment | Secure GDPR-compliant clinician-to-clinician messaging on complex cases. | [S] |
| 2. Sticky mechanic | Network density among verified clinicians; >550k members, >1B messages. | [V] |
| 3. Frequency engine | Daily for engaged clinical teams. | [V] |
| 4. Monetization | Free to individuals, enterprise/department upsell to hospitals + associations. | [V] |
| 5. Moat | Clinician network — strong, but **acquired by Doctolib (Mar-2023), now "Doctolib Siilo / Doctolib Connect."** | [S] |
| 6. Outcome & graveyard lesson | **The professional-messaging layer got absorbed by the front-door incumbent.** Lesson: standalone messaging is a feature/acquihire, not a standalone business — and the buyer was, again, the front door. | [S] |
| 7. EU-applicability | EU-native (Amsterdam-built). But it's a *clinician* network — wrong side for a patient-first player. | [S] |

*Klara (US, acquired by ModMed) and Spruce are the patient↔provider messaging analogues: both are practice-software features, not independent businesses, and both monetize the provider.* [S]

---

### Second opinion: Included Health (US) · Medexo (DE)

| Lens | Included Health (Grand Rounds) | Medexo (DE) | Grade |
|---|---|---|---|
| 1. Job & moment | "Is this serious diagnosis right?" — the exact severe-disease moment Ditto cares about. | Same, document-based. | [S] |
| 2. Sticky mechanic | Curated expert network; **changed diagnosis/treatment in 66% of cases** (vendor). | In-house case mgmt + external expert reviews records. | [V]/[S] |
| 3. Frequency engine | Episodic, high-stakes. | Episodic. | [S] |
| 4. Monetization | **Employer-paid benefit, free to the member** — 6M+ covered lives. | **Insurer-paid** (30+ statutory/private insurer relationships). | [S] |
| 5. Moat | Expert network + employer benefit-channel distribution. | Insurer contracts + Germany's statutory **Zweitmeinungsverfahren** (legally mandated free second opinion for specified surgeries: hysterectomy, tonsillectomy, knee/shoulder, spinal, diabetic-foot amputation). | [S]/[P G-BA] |
| 6. Outcome | Scaled via the US employer-benefits channel (no EU equivalent). | Sustainable but small, riding a regulatory mandate. | [S] |
| 7. EU-applicability | **Low — the US employer-pays-for-health-benefits channel does not exist in NL.** EU second opinion is **insurer/system-funded and partly legally mandated**, not consumer-paid. | [S] |

**Read:** second opinion is the operational job *closest* to Ditto's emotional moment (a scary diagnosis, "is this right?"), but it monetizes via employer/insurer, and in the EU it is partly a regulated, insurer-funded process. A patient-pays second-opinion product has no proven EU monetization.

---

### National front doors: NHS App (UK) · MijnGezondheid.net / PGOs (NL)

| Lens | NHS App | NL: MijnGezondheid.net + PGOs (MedMij) | Grade |
|---|---|---|---|
| 1. Job & moment | Government "one app for the NHS." | GP-record portal (MGn) + personal health environments (PGOs: Quli, Ivido) under the MedMij standard. | [S] |
| 2. Sticky mechanic | Prescriptions + record + appointments in one place, free, identity-backed. | Aggregated record across GP/hospital/pharmacy/mental health; user can add own data. | [S] |
| 3. Frequency engine | **67.8M repeat prescriptions/yr; GP record viewed ~20M times/mo** — genuine habitual use at national scale. | Low adoption; fragmented; users must actively choose and connect a PGO. | [S]/[S] |
| 4. Monetization | **Taxpayer-funded; free to patient.** | System-funded; free to patient. | [S] |
| 5. Moat | **State mandate + national identity + record access** — pledged to be a "full front door to the NHS by 2028," default patient comms channel by 2029, single patient record, AI triage. | MedMij standard + (planned) consolidation from ~10 PGOs to **3** via government procurement. | [S]/[S] |
| 6. Outcome | The single biggest structural force: **the state is building the free front door**, and adding AI triage and record-understanding on top. | NL version is weaker/fragmented but heading toward consolidation + a standardised data-exchange rail. | [S] |
| 7. EU-applicability | Direct. In NL, the government PGO consolidation + MedMij is the equivalent dynamic Ditto must position against/onto. | Direct and immediate for Ditto's home market. | [S] |

**Read:** in both the UK and NL, the *operational* front door is trending toward a **free, state-backed** product that also wants the record and is bolting on AI triage. A commercial patient-side player cannot out-distribute a national app on the operational job, and the operational job is being given away for free. The defensible position is *not* the operational layer — it is the intelligence/understanding the national app does poorly.

---

## (c) White space for Ditto — plain verdict

The brief was asked four specific questions. Direct answers:

### Q1 — How did Doctolib actually win, and is the moat replicable or closed?
**Mechanic:** provider-side two-sided network + deep practice-OS lock-in, won **one country at a time** by reaching supply-side critical mass locally before rivals (FR→DE→IT). Patient accounts are a free funnel, not the moat. **Verdict: in its core geographies the moat is effectively closed.** It took 12 years, ~€500M-class capital, ~€115M/yr R&D, and a country-by-country supply war. A new entrant cannot replicate it — *but* note Doctolib is **not strong in NL**, so "the NL booking front door" is not as locked as France's. That is a real-but-unattractive opening (see Q4).

### Q2 — Does the operational monetization model survive the patient-side filter?
**No, not as a patient-pays model.** Every durable winner monetizes the **provider or the system**: Doctolib/DocPlanner/ZorgDomein (provider SaaS), Kry (public payer), Included Health (employer), Medexo (insurer), NHS App/PGOs (taxpayer). **"Patients don't pay" is not a Doctolib quirk — it is the law of this layer.** For Ditto to monetize the operational front door it would have to become a **provider/system SaaS company**, i.e. flip from patient-first to B2B SaaS — a different company than the one v2 describes. This is the hard-filter failure: the operational layer's proven monetization is structurally incompatible with a patient-first stance, *unless* Ditto explicitly adds a provider/payer-paid B2B line (which is a strategy choice, not a free extension).

### Q3 — THE KEY QUESTION: does owning the front door genuinely feed the intelligence layer, or are they two businesses?
**They are two businesses, and the stacking is real but runs the *opposite* direction from the v2 hope.**

The v2 thesis is "own the front door → the data + scheduling feed intelligence." The evidence says the dependency is real but asymmetric:
- **Direction that works:** front door → intelligence. The front door holds the patient relationship, the scheduling event, and the data exhaust, so it is the *cheapest place from which to launch* an intelligence product. This is exactly why **Doctolib launched "Doctolib Parents"** and **DocPlanner is repositioning as an AI/medical-data company.** The front door feeds intelligence — *for whoever owns the front door.*
- **Direction that does NOT work:** intelligence → front door. Being good at understanding a diagnosis does not get you the provider network, the practice OS, or the referral rail. Those are won with feet-on-the-street sales and capital, not patient love. The intelligence layer does not "unlock" the operational layer.

So the two layers **stack only in one direction**, and the front door is the *upstream* asset. The v2 framing ("if you are the front door, you also hold extra data and you can schedule, which feeds everything above") is **mechanically correct but strategically inverted for Ditto** — because Ditto is not, and realistically cannot become, the front door. The players who *are* the front door will feed *their own* intelligence layers from it. **Plain verdict: the front door feeds intelligence, but Ditto is not positioned to be the front door, so this synergy mostly accrues to incumbents and is a threat to Ditto more than an opportunity.**

What genuinely feeds Ditto's intelligence layer is **data access** (the record), not scheduling. Scheduling is a thin operational event with little semantic content. The record is the fuel. And data access in NL is heading toward a *standardised, free rail* (MedMij/PGO consolidation, EHDS) — meaning Ditto can likely *get* the fuel without owning a front door. That decouples "intelligence" from "front door" further.

### Q4 — Can a ~16-person patient-side player OWN any operational front-door function in NL/EU?
**No. Integrate, don't build. This is direct.**

| Function | Own? | Why |
|---|---|---|
| Scheduling | No | Requires winning the provider supply war Doctolib/DocPlanner already fought; thin data value anyway. |
| Referral rail | No | ZorgDomein = 91% of NL GPs; a system-standard, not a competitive market. |
| Telehealth | No | Capital-heavy, payer-gated, thin-margin (Kry nearly died building it). |
| Pro messaging | No | Already absorbed by Doctolib; clinician-side, wrong audience. |
| Second opinion | **Maybe — as a service layer, not infra** | Closest to Ditto's moment; but EU monetization is insurer/system, not patient. A patient-facing "is this right / help me get a second opinion" *intelligence* feature is plausible; owning the second-opinion *operations* is not. |
| Data access | **Integrate via standards** | Don't build a PGO; ride MedMij/EHDS. Owning data *understanding* ≠ owning data *plumbing*. |

**The one nuance worth flagging to Merlijn:** because Doctolib is weak in NL, the "NL booking/front-door" seat is genuinely less occupied than France's. But taking it would mean becoming a provider-SaaS company — abandoning the patient-first identity, not extending it. That is a fork for Merlijn/Nick, not a research conclusion.

### Bottom line for the synthesis (C3)
- The operational front door is a **provider/system SaaS distribution moat, already won per-country, monetized by providers — never patients.**
- It **does** feed intelligence, but **upstream-to-downstream**, which benefits the incumbents who own the door. Ditto is downstream.
- Therefore the front door is, for Ditto, primarily a **threat vector and an integration surface**, not a business to own. The defensible position is the **intelligence the front doors do badly** (understanding → advising → agency on a serious diagnosis), fed by **standardised data access** rather than owned scheduling.
- **Recommendation: integrate, don't build.** Treat ZorgDomein (referral moment), MedMij/EHDS (data fuel), and the national apps (distribution) as rails to ride. Reserve the "own" verb for the intelligence layer. If a provider/payer-paid B2B line is ever wanted for monetization, that is a deliberate identity choice to put to the board, not a natural extension of the patient product.

---

## (d) Graded citations

**Doctolib**
- [S] Sifted — Doctolib 2024 results, €348M ARR, losses, geo split: https://sifted.eu/articles/doctolib-results-2024
- [S] Contrary Research — Doctolib business breakdown, pricing, network mechanic, product evolution: https://research.contrary.com/company/doctolib
- [S] heise online — Doctolib practice software with three AI assistants (telephone, consultation scribe): https://www.heise.de/en/news/Doctolib-launches-practice-software-with-AI-support-11039664.html
- [S] Banque Populaire / Le Moniteur des Pharmacies — "Doctolib Parents" patient AI assistant, early 2026, parents 0–4, multi-LLM, EU-hosted: https://www.banquepopulaire.fr/professionnels/conseils/doctolib-assistant-ia-patients/ · https://www.lemoniteurdespharmacies.fr/business/numerique/e-sante/doctolib-va-lancer-un-assistant-medical-fonde-sur-lia
- [S] Frontiers Health — corroborates €348M ARR / profitability framing: https://www.frontiers.health/stories/facts/doctolib-shares-financial-results-hitting-eu348m-arr-eyes-profitability

**DocPlanner / Jameda / Doctena**
- [S] Bloomberg — DocPlanner CEO on AI/medical-data fueling growth pre-IPO (Jan-2026): https://www.bloomberg.com/news/articles/2026-01-26/docplanner-ceo-sees-medical-data-ai-fueling-growth-before-ipo
- [S] ainvest — DocPlanner AI pivot pre-IPO, AI Assistant in 5 countries: https://www.ainvest.com/news/docplanner-ai-pivot-rewrite-healthcare-story-ipo-2601/
- [S] Sifted — DocPlanner acquires Jameda (Germany entry): https://sifted.eu/articles/docplanner-acquires-jameda-germany
- [S] Tech.eu — DocPlanner/Jameda acquisition, ~20k doctors / 8M patients/mo: https://tech.eu/2021/11/23/healthcare-booking-and-management-platform-and-docplanner-snaps-up-hubert-burda-media-property-jameda/
- [V] CB Insights — competitor set (DocPlanner, Doctena, Jameda, Keldoc, Qare, Vezeeta): https://www.cbinsights.com/research/doctolib-competitors-docplanner-doctena-jameda-keldoc-qare-vezeeta-clickdoc/

**ZorgDomein**
- [S] ZorgDomein patient support — what it is / referral function: https://patienten-support.zorgdomein.com/hc/nl/articles/10985640987538-What-is-ZorgDomein
- [S] Rabo Investments / Levine Leichtman — 91% of NL GPs, PE ownership: https://raboinvestments.com/portfolio/zorgdomein/ · https://www.llcp.com/portfolio/zorgdomein/

**Zocdoc**
- [S] Summit Health Advisors — Zocdoc model evolution, network effects, inequitable value capture: https://www.summithealth.io/insights/how-zocdoc-evolved-its-business-model-to-unlock-exponential-growth-with-network-effects
- [V] Daffodil / business-model write-ups — $300/yr + ~$35/booking, ~6M monthly bookings, ~$200M 2024 rev: https://insights.daffodilsw.com/blog/how-zocdoc-works-business-model-and-revenue-streams

**Kry / Livi**
- [S] Sifted — Kry layoffs, exit from Germany, then profitability via AI: https://sifted.eu/articles/kry-layoffs-digital-health-news · https://sifted.eu/articles/kry-profitable-in-all-markets-we-wouldnt-have-managed-it-as-quickly-without-ai-news
- [S] Sacra — Kry revenue (~$215M, 2022), revenue mix (~90% public payers), funding €516M: https://sacra.com/c/kry/

**Qare**
- [S] MobiHealthNews — HealthHero acquires Qare: https://www.mobihealthnews.com/news/emea/uk-based-healthhero-acquires-french-telehealth-provider-qare

**Siilo / Klara / Spruce (pro + patient messaging)**
- [S] Silicon Canals — Siilo rebrands as Doctolib Siilo post-acquisition: https://siliconcanals.com/siilo-rebrands-as-doctolib-siilo/
- [V] Siilo / EQT Ventures — 550k members, 1B+ messages, free-to-clinician + enterprise: https://medium.com/eqtventures/our-investment-in-siilo-elegantly-revolutionizing-healthcare-from-the-bottom-up-d23c35bf8ad9
- [S] Klara — acquired by ModMed, practice patient-engagement software: https://www.klara.com/blog/modmed-acquires-maker-of-the-klara-practice-patient-collaboration-platform

**Second opinion**
- [S] Included Health — Grand Rounds second-opinion origin, 66% change rate, employer-paid, 6M+ lives: https://includedhealth.com/blog/tech/our-product-journey/
- [S] Fierce Healthcare — Included Health virtual specialty clinic (cancer focus): https://www.fiercehealthcare.com/health-tech/included-health-launches-virtual-specialty-care-clinic-initial-focus-cancer-weight-loss
- [S] VMS Hannover — Medexo, insurer-funded, 30+ insurer relationships, document-based: https://vms-hannover.com/en/medexo/
- [P] gesund.bund.de (G-BA) — statutory Zweitmeinungsverfahren: free second opinion, covered procedures: https://gesund.bund.de/en/second-opinion

**National front doors**
- [S] NHS England — record NHS App usage, ~40M registered, 67.8M repeat prescriptions, ~20M record views/mo: https://www.england.nhs.uk/2025/12/record-numbers-using-nhs-app-to-manage-health/
- [S] HTN / Full Fact — NHS App "full front door by 2028" roadmap, single patient record, AI triage: https://htn.co.uk/2025/05/01/nhs-app-roadmap-outlines-health-records-appointments-prescriptions-integrated-services-and-messaging-plans/ · https://fullfact.org/government-tracker/nhs-app-improvements/
- [S] med-techinsights — NHS App default patient comms channel by 2029: https://med-techinsights.com/2025/10/27/nhs-app-to-be-defualt-patient-communication-channel-by-2029/
- [S] MedMij / Patiëntenfederatie — MedMij standard, PGO definition (Quli, Ivido), MGn = GP-record portal: https://medmij.nl/en/home/ · https://www.patientenfederatie.nl/over-de-zorg/pgo

**Unverified / needs confirmation**
- Doctolib patient-account total (80M) and provider count (~400k) are [S]/[V] aggregator/press figures, not audited. «treat as directional»
- DocPlanner "100M monthly users / 210k+ active doctors" is [V] aggregator-sourced. «unverified»
- Kry revenue (~$215M) is 2022-dated; no confirmed 2024/25 figure found. «stale»
- Doctena/Jameda volume figures are vendor/acquisition-era. «dated»
