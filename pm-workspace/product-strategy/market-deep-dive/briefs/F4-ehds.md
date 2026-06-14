# F4 — EHDS & the patient-data economy: who is positioning to exploit it

> Market Deep Dive, Part I brief. Field F4. Researched 2026-06-09 by Mewtwo (web-enabled).
> Informs v2 layer: **PHR-as-multiplier**. Companion to the EHDS timeline in `../../market-trend-analysis/`, which this brief deliberately does not repeat.
> Sourcing: web verified. Grades inline — [P] primary (regulator/company/law), [S] reputable secondary, [V] vendor self-report. Unverifiable figures flagged «unverified».

## The one-line answer

EHDS is **two different economies wearing one name.** The money and the positioning are almost entirely in the **B2B secondary-use track** (pooled data sold to pharma/research via national access bodies), which the incumbents — IQVIA, TriNetX, Datavant, Owkin, Aridhia — are already building for and which does not touch Ditto's user. The **primary-use track** (a patient moving their own verified record between providers) is the one that would multiply Ditto's intelligence layer, but it is **EU-project-stage, not startup-stage, and gated to ~2029**. No one is yet winning the consumer-facing "bring your verified record anywhere" broker role. That is the white space — and the trap. **Near-term verdict: 2029+ architecture signal, not a 2026 opportunity. Do not chase "launching partner."**

---

## (a) Field map — two tracks, one regulation

EHDS Regulation **(EU) 2025/327**, published 5 March 2025, in force **26 March 2025**. [P] [health.ec.europa.eu](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en) It splits cleanly into two tracks that share almost no value chain.

| | **Primary use** (the patient's track) | **Secondary use** (the industry's track) |
|---|---|---|
| **What** | A patient accesses and shares their own record across providers/borders. | Pooled, pseudonymised data accessed by researchers, pharma, policymakers, innovators. |
| **Rails** | MyHealth@EU (operational today for patient summaries + ePrescriptions). [P] | HealthData@EU + national **Health Data Access Bodies (HDABs)**. [P] |
| **Who pays** | No one pays the patient; cost sits with member states / providers. | **Data users pay access fees** to HDABs/data holders (cost-recovery, SME discounts). [P] Art. 42. |
| **Live date** | Group 1 (patient summaries, ePrescriptions) **~March 2029**; Group 2 (images, labs, discharge letters) **~March 2031**. [P] | Most categories **~March 2029**; remainder **~2031**. HDABs designated by **26 March 2027**. [P] |
| **Where Ditto could sit** | Consumer-facing app that ingests a verified record (multiplier for intelligence). | Nowhere obvious — Ditto is not a data holder at meaningful scale, and selling user data contradicts its trust position. |

**Value chain (secondary use, where the money is):**
`Data holders (hospitals/labs)` → `HDAB (permit + pseudonymise + provision, charges fee)` → `Secure Processing Environment / TRE (compute stays inside)` → `Data user (pharma/research, pays)`. Vendors are colonising the **TRE/SPE** and **connectivity/tokenisation** rungs.

**Value chain (primary use, where Ditto would sit):**
`Provider EHR (EEHRxF format)` → `MyHealth@EU / national node` → `Patient-facing app (PGO in NL)` → `the patient shares onward`. Today in NL this rung is **MedMij-certified PGOs**; the EU-wide consumer-sharing primitive is the **xShare "Yellow Button,"** still a pilot.

---

## (b) Player & initiative teardowns

Lens key: **1** what + EHDS angle · **2** value-chain seat · **3** monetisation (who pays) · **4** moat · **5** maturity/traction · **6** EU/NL applicability + timeline.

### Secondary-use / real-world-data players (B2B — the money)

**IQVIA** — [V]/[S]
1. The category incumbent: RWD assets, analytics, consulting; positions HDAB access as *one more source* feeding its pipeline.
2. Data aggregator + analytics, top of the value stack (sells evidence, not raw data).
3. Pharma pays, richly. EHDS lowers IQVIA's input cost; does not threaten its sell-side.
4. Moat = scale, pharma relationships, regulatory-grade methods. Deep.
5. Mature, multi-billion. Buyers pick *neutral* intermediaries like Datavant *because* IQVIA competes with its own data products. [S] [datavant.com](https://www.datavant.com/blog/the-next-generation-of-data-connectivity-for-healthcare)
6. Fully EU-active. EHDS is a tailwind, not a disruptor. Irrelevant to Ditto except as proof of where value pools (industry, not patient).

**TriNetX** — [V]/[S]
1. Federated RWD network: query patient-level data without moving it. Natural fit for EHDS's "compute-to-data" design.
2. Infra + data aggregator (federated).
3. Pharma/CRO subscriptions + study fees; providers contribute data for analytics access.
4. Moat = network of contributing health systems (300M+ patients, 200+ HCOs, 20+ countries, Sept 2025 self-report «unverified»). [V] [trinetx.com](https://trinetx.com/data/)
5. Mature, broad EU footprint.
6. Its federated model is the architectural template EHDS secondary use is copying. No consumer surface. Not a Ditto path.

**Datavant** — [S]
1. **Neutral connectivity/tokenisation layer** — links datasets without exposing them or competing with data products. The "Switzerland" play.
2. **Consent/linkage infrastructure** — the most interesting seat for Ditto to *understand* (not occupy).
3. Data users pay; Datavant monetises the *plumbing*, not the data.
4. Moat = neutrality + tokenisation network effects. Buyers at Oracle/IQVIA choose it *because* it doesn't compete. [S]
5. Actively building EU/GDPR capability: Promptly Health partnership (Iberia → UK/Sweden, Apr 2024), Trace Data acquisition for GDPR governance, 100+ UK staff. [V] [datavant.com](https://www.datavant.com/press-release/promptly-health-datavant-announce-partnership-advance-european-health-data-accessibility)
6. EU-relevant, B2B only. **Lesson for Ditto:** the durable seat is *neutral connection*, not data ownership. But it's a B2B plumbing business, not a consumer one.

**Owkin** — [V]/[S]
1. Federated learning across hospitals for oncology drug discovery; data stays local, models travel. Privacy-preserving by design — EHDS-shaped.
2. Data aggregator + AI/model layer, co-development.
3. Pharma R&D deals dominate (Sanofi ~$270M cited; ~60–70% of revenue «unverified»); plus SaaS + tiered data-access fees. Revenue ~$300M 2024 «unverified, vendor/secondary». [S]/[V] [dealroom.co](https://app.dealroom.co/companies/owkin)
4. Moat = federated node network + oncology model IP + pharma lock-in.
5. Well-funded, oncology-deep — Ditto's exact disease beachhead, but the *opposite* end of the value chain (pharma R&D, not patient comprehension).
6. EU-native (Paris). Confirms oncology data has real buyers — none of whom are patients.

**Aridhia** — [V]
1. Digital Research Environment = a **Secure Processing Environment / TRE**, the exact compute box EHDS Art. mandates for secondary use. Explicitly markets EHDS-readiness for data holders. [V] [aridhia.com](https://www.aridhia.com/blog/ehds-patient-consent-and-the-expectations-on-secure-processing-environment-providers/)
2. Infrastructure (SPE/TRE).
3. Data holders / HDABs / research institutions license the environment.
4. Moat = certified secure environments + NHS/Great Ormond Street references. Moderate, defensible on compliance.
5. Operating, EU/UK research traction.
6. Directly EHDS-positioned — but selling *to HDABs and data holders*, a procurement game a 16-person consumer app cannot and should not enter.

*Lynx.MD* — searched; no material EU/EHDS footprint surfaced. Treat as US-focused TRE/data-collaboration vendor, **not** an EU positioning signal. «unverified — flag if it resurfaces».

**Read-through:** every secondary-use player monetises the **same buyer (pharma/research)** and sits on infra/aggregation rungs. None has a consumer surface. EHDS is a *tailwind* for all of them and changes none of their business models. This track is **closed to Ditto** and contradicts its trust position.

### Consent / infrastructure / EU projects (primary use — the patient's track)

**HealthData@EU pilot + the HDABs** — [P]
1. The pilot (Oct 2022–Dec 2024) built and tested the secondary-use cross-border infra; MVP deployed in **France, Denmark, Finland**. [P] [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC12420900/) HDABs are the national permit authorities, designated by **26 March 2027**, live ~2029. [P]
2. Public infrastructure + governance (the toll booth of secondary use).
3. Cost-recovery fees from data users; SME discounts. [P]
4. Moat = statutory monopoly. They *are* the gate.
5. Pilot complete; build-out 2025–2028.
6. Core EU plumbing. Ditto is neither a builder nor a customer here.

**HDAB-NL (Netherlands)** — [P]
1. National programme to stand up the Dutch HDAB. Health-RI with VWS, ICTU, CBS, RIVM. Pilots 2025–2026; obligations bite ~March 2029. [P] [health-ri.nl](https://www.health-ri.nl/en/projects-collaborations/hdab-nl)
2. National secondary-use node.
3. €9.5M budget, VWS + EU co-funded. [P] Data users will pay access fees.
4. Statutory.
5. In build.
6. **NL-specific and relevant for context only** — it governs *secondary* use. Ditto's interest is *primary* use, a different track.

**MedMij + the NL PGO ecosystem (Quli, Ivido, Patients Know Best, etc.)** — [P]/[S]
1. **MedMij** = the NL trust framework for secure patient-data exchange between certified PGOs (personal health environments) and providers. Quli/Ivido are MedMij-certified PGOs. This is the **NL primary-use rail that predates EHDS** and will plug into it.
2. **Consent/exchange standard (MedMij) + consumer-facing apps (the PGOs).** This is the rung Ditto would touch.
3. **No working consumer monetisation.** PGOs are subsidised/policy-pushed, not paid-for. The IZA target — every citizen who wants one has a "well-stocked" PGO by end-2025 — is a *policy aspiration*, and adoption has been chronically weak. [S] [medmij.nl](https://medmij.nl/en/faq/), [volgjezorg.nl](https://www.volgjezorg.nl/en/faq/about-personal-portal-pgo-portals-medmij)
4. Moat = certification + national mandate (for the framework, not for any one PGO).
5. **The PGO graveyard signal:** despite years of subsidy and a national mandate, Dutch PGO adoption is low and the apps are not loved. This is the single most important datapoint for Ditto. The rail exists; *consumers don't show up for the rail itself.*
6. **Most directly relevant to Ditto of anything in F4.** A MedMij connection is the concrete, available-today way to ingest a verified NL record. The lesson: **the record is a feature inside a loved product, never the product.** PGOs died proving the opposite.

**xShare "Yellow Button"** — [P]/[S]
1. Horizon Europe project building a one-click primitive for a patient to **download or generate a secure, time-limited link to share their record in EEHRxF**. Explicitly targets EHDS *primary-use* categories (patient summaries, ePrescriptions). [P] [xshare-project.eu](https://xshare-project.eu/the-xshare-button/)
2. **Consumer-facing consent/sharing primitive** — the closest thing in Europe to "bring your verified record anywhere."
3. No monetisation model — it's grant-funded infrastructure meant to be *embedded* by apps.
4. No moat (it's a public good by design, with open calls for early adopters in 2025–2026).
5. **Pilot stage.** Not production.
6. **The direct answer to Merlijn's white-space question:** the consumer EHDS-sharing primitive is being built as a *public button apps embed*, not as a startup's proprietary moat. If this becomes the standard, "consent broker" is **commoditised infrastructure, not a defensible business.** Ditto should plan to *embed* it, not *be* it.

**Gravitate Health (G-Lens)** — [P]/[S]
1. IMI2 public-private project (Nov 2020–Oct 2025, Univ. Oslo + Pfizer co-lead) building the **G-Lens**: personalised, literacy-adapted display of approved medicine information (e-leaflets) via the FHIR-based EU ePI standard. [P] [ihi.europa.eu](https://www.ihi.europa.eu/projects-results/project-factsheets/gravitate-health)
2. Consumer-facing *comprehension* layer on top of medicines data.
3. No direct monetisation (research project).
4. Standards-based, no proprietary moat.
5. Concluded ~Oct 2025; output is standards + reference implementation.
6. **Adjacent and instructive:** the EU is *itself* funding the "make medical info understandable to patients" layer — Ditto's exact value proposition, but narrow (medicine leaflets only) and non-commercial. Confirms the comprehension job is real and validated at EU level; also a reminder Ditto's edge is breadth + product quality, not the concept.

### The working precedent — Finland: Findata + Kanta

The closest real-world model of what EHDS does in practice. Worth covering well because **Finland is what NL/EHDS will look like ~2029.**

| Lens | Findata (secondary use) | Kanta (primary use) |
|---|---|---|
| **1. What** | National secondary-use **permit authority** since 2019, under the Act on Secondary Use of Health and Social Data. Grants permits to combine data across controllers. [P] [findata.fi](https://findata.fi/en/) | National EHR/PHR backbone; "secondary use of Kanta data" now flows through Findata. [P] [kanta.fi](https://www.kanta.fi/en/secondary-use-of-kanta-data) |
| **2. Seat** | The HDAB blueprint — exactly the role each member state must stand up by 2027. | National primary-use rail (the Kanta PHR = what a national PGO looks like at maturity). |
| **3. Who pays** | Data users (research, pharma, e.g. RWE provider Quantify) pay permit + provisioning fees. [S] [quantifyresearch.com](https://quantifyresearch.com/2025/03/26/quantify-leads-with-most-findata-permits-issued-in-2024-for-an-rwe-provider/) | State-funded. |
| **4. Maturity** | 2024: 316 applications, 340 decisions, 114 positive permits. [S]/[P] Processing 2–4 months per permit. | Mature; Finland is live on MyHealth@EU. |
| **5. The friction (the warning)** | Centralisation made it **slow and costly**. 2021 surveys: 79% of medical-doctor respondents found the permit process *more complex* than before, 55% saw project delays, 64% higher costs. [S] [ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11443657/) A 2024–25 legal reform is trying to de-bottleneck it. [S] | — |
| **6. Read-through** | EHDS secondary use will be **slow, permit-gated, and built for institutional buyers** — not a fast or consumer-shaped opportunity. | Even the best national primary-use rail is *plumbing the state provides*; the loved product still has to be built on top. |

**Bottom line on Finland:** the most advanced version of EHDS, after **5+ years**, is a slow B2B permit shop plus a state PHR backbone. It is not a consumer gold rush. It is the most concrete evidence that EHDS value accrues to **institutions and infra**, on a **multi-year** clock.

---

## (c) White space for Ditto — the plain verdict

**Q1 — Is anyone positioning as a consumer-facing EHDS consent broker / "bring your verified record anywhere" player?**
**Essentially no — and the way it's being built suggests no one *can* own it.** The action is overwhelmingly B2B infra and secondary-use data (IQVIA, TriNetX, Datavant, Owkin, Aridhia, the HDABs). The one consumer-facing primitive — xShare's Yellow Button — is being built as a **public good apps embed**, not a proprietary moat, and the NL PGO ecosystem (Quli, Ivido) already proves that *a record-portability app, on its own, is something consumers will not show up for.* So "consent broker" is not an empty white space waiting to be claimed; it's a **commoditising rung**. Owning the rung is not the prize. Owning the *product the rung feeds* is.

**Q2 — What does being an "EHDS launching partner" concretely require? Realistic for ~16 people?**
Two very different asks, depending on track:

| | Primary-use participation (what Ditto would want) | Secondary-use / data-holder play (what Ditto should avoid) |
|---|---|---|
| **Technical** | Implement **EEHRxF** ingestion; in NL, **MedMij certification** to connect to providers. Embed a sharing primitive (xShare-style). | Register/describe datasets, build/contract a **Secure Processing Environment**, EEHRxF, annual dataset upkeep. [P] [twobirds biotalk](https://biotalk.twobirds.com/post/102k70n) |
| **Legal/cert** | MedMij framework compliance; GDPR; consent UX. | Data-holder obligations, HDAB liaison, audited provisioning. |
| **Penalty exposure** | Standard GDPR. | EHDS fines up to **€10M / 2%** (minor) to **€20M / 4%** (severe) of global turnover. [P] [skadden.com](https://www.skadden.com/insights/publications/2025/06/the-european-health-data-space) |
| **Realistic for 16 people?** | **The primary-use side, yes — but not before ~2029, and only via MedMij today.** | **No.** This is a procurement/compliance business for data holders and infra vendors. Out of scope and off-mission. |

The honest read: "EHDS launching partner" is **mostly a positioning phrase**, not a concrete program with a partner slot to claim in 2026. The real, available action today is a **MedMij integration** to ingest NL records — which Ditto can do without invoking EHDS at all.

**Q3 — Where does the money accrue, on what timeline? 2026 opportunity, 2029+ signal, or distraction?**

| Track | Who captures value | Timeline | Ditto fit |
|---|---|---|---|
| Secondary-use data/infra | Pharma-facing incumbents + HDABs (fees) | Building now, mature ~2029+ | Off-mission. Skip. |
| Primary-use rails (MyHealth@EU, MedMij) | The state provides them; value sits in apps on top | NL today (MedMij); EU-wide ~2029/2031 | The relevant rung — but the rail is not the product |
| Consumer comprehension/agency *on top of* a portable record | **Open. This is Ditto's lane.** | Multiplies as records become portable, ~2029 | **Yes — but the moat is the intelligence, not the data** |

**Verdict: EHDS is a 2029+ architecture signal, not a 2026 opportunity, and "launching partner" is close to a distraction.** Treat EHDS exactly as v2 frames it — a **regulatory tailwind that makes records portable, turning Ditto's intelligence layer into a multiplier** — not a destination to build toward. Concretely:

- **Now (2026):** if record-ingestion matters for the intelligence layer, do the **MedMij integration** for NL. That is real, available, and does not require waiting for EHDS or claiming any "partner" status.
- **Architecture (design for, don't build yet):** keep the data model EEHRxF-aware so Ditto can embed the xShare-style sharing primitive when it lands, and ingest cross-provider records when MyHealth@EU primary use goes live ~2029. Cheap insurance, not a roadmap line.
- **Do not:** position as an EHDS consent broker (commoditising), pursue data-holder/secondary-use monetisation (off-mission, penalty-heavy, pharma-buyer), or let "EHDS" slow down adding intelligence to the data users already give Ditto. **The trade-off Merlijn named resolves cleanly toward intelligence-first.**

**The one strategic nuance worth Merlijn's attention:** Gravitate Health and xShare show the EU is *publicly funding* both the "make health info understandable" layer and the "share your record" button — Ditto's two core moves, as non-commercial public goods. That is validation that the jobs are real, **and** a warning that the concepts are not defensible. Ditto's moat has to be **product quality, breadth across the care journey, and the trust relationship — not the record, not the rail, and not consent-brokering.**

---

## (d) Graded citations

| # | Source | Grade | Used for |
|---|---|---|---|
| 1 | EU Commission — EHDS Regulation page | [P] | In-force date, primary/secondary split, 2029/2031 timeline |
| 2 | Skadden — EHDS guide (Jun 2025) | [S] | Data-holder obligations, fines €10M/2%–€20M/4% |
| 3 | Bird & Bird (biotalk) — Health Data Holders' obligations | [S] | Data-holder technical/legal obligations |
| 4 | EU Commission — EHDS Art. 42 Fees | [P] | Who pays secondary-use fees, cost-recovery, SME discount |
| 5 | DLA Piper — secondary use under EHDS | [S] | Fee/cost-recovery detail |
| 6 | Findata (findata.fi) | [P] | Findata role, mandate, 2024 permit volumes |
| 7 | Kanta.fi — secondary use of Kanta data | [P] | Kanta primary/secondary integration |
| 8 | NCBI PMC 11443657 — EU health regs reduce registry research | [S] | Finland friction stats (79%/55%/64%, delays) |
| 9 | Quantify Research | [S]/[V] | Findata permit volumes; data-user pays |
| 10 | HealthData@EU pilot (PMC 12420900) | [P] | Pilot dates, FR/DK/FI MVP, infra learnings |
| 11 | Health-RI — HDAB-NL | [P] | NL HDAB programme, €9.5M, 2025–26 pilots, 2029 |
| 12 | MedMij (medmij.nl) + Volgjezorg | [P]/[S] | NL PGO/MedMij framework, IZA end-2025 target |
| 13 | xShare project (xshare-project.eu) | [P]/[S] | Yellow Button, EEHRxF sharing, primary-use, pilot status |
| 14 | IHI Europe — Gravitate Health factsheet | [P] | G-Lens, dates, Oslo/Pfizer, ePI standard |
| 15 | TriNetX (trinetx.com/data) | [V] | Federated network scale «unverified» |
| 16 | Datavant press + blog | [S]/[V] | Neutral intermediary, EU expansion, Promptly/Trace Data |
| 17 | Aridhia blog | [V] | SPE/TRE EHDS-readiness positioning |
| 18 | Dealroom — Owkin | [S]/[V] | Owkin model, revenue «unverified» |
| 19 | MyHealth@EU (EU Commission) | [P] | Primary-use cross-border services, 15 MS connected |

**Verification flags:** TriNetX/Owkin figures are vendor/secondary self-reports — directional only. "Launching partner" has no formal EU definition surfaced — treated as positioning language. Lynx.MD has no confirmed EU/EHDS footprint. Finland friction survey is 2021 (pre-reform); the 2024–25 reform's effect is not yet measurable.
