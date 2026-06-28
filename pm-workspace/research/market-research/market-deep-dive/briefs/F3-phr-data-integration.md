# F3 — Patient-Owned Health Records (PHR/PGO) & Data Integration

> Market Deep Dive · Part I · Field brief. Created 2026-06-09 by Mewtwo.
> Informs v2's **"PHR as multiplier, not destination"** thesis (direction C2). Monetization is a hard filter.
> Source grades inline: **[P]** primary · **[S]** reputable secondary · **[V]** vendor self-report. Unverified figures flagged «unverified».
> Web-researched 2026-06-09. Where a figure could not be triangulated to a primary source, it is flagged.

## (a) One-screen field map

**The game in one line:** owning the record is a graveyard; *piping* the record (B2B infra) is a business; *reasoning over* the record (AI layer) is the new frontier that just opened. The consumer-facing "vault" almost always dies. The value moved underneath it (integration plumbing) and on top of it (intelligence).

**The historical PHR-failure pattern (consistent across two decades).** Every standalone consumer PHR that tried to be the destination failed for the same four reasons, in combination:

| Failure mechanism | What it looked like | Players it killed |
|---|---|---|
| **Data without insight** | A tidy "online scrapbook" of records. No reason to act. | Google Health 1.0, HealthVault |
| **No frequency / no reason to return** | You file your data once, then never open it again. Healthy people don't think about health. | All of them |
| **No actionable jobs** | Couldn't book, refill, or message a doctor — the basics users actually wanted. | Google Health 1.0 (admitted by Google) |
| **Integration cost & gatekeeping** | Providers, labs, PBMs hoarded data as a business asset and would not feed a third party for free. | Dossia, HealthVault |

**What is structurally different in 2025–2026 (this is the live question).**

| Shift | Evidence | Does it change the verdict? |
|---|---|---|
| **Regulatory force-feeds the data** | US 21st Century Cures Act bans information blocking, mandates free FHIR R4 patient-access APIs [P]. Germany ePA flipped to **opt-out** Jan 2025: <1% → ~70M accounts in weeks [S]. NL MedMij gives every citizen a free PGO by law via DigiD [P]. | Yes for *supply*. Integration cost (failure #4) is collapsing. But ePA's own data shows accounts ≠ active use — the *frequency* problem (#2) is untouched. |
| **An AI layer can finally turn data into insight** | Jan 2026: **OpenAI launched ChatGPT Health**, connecting medical records — built on **b.well** as the data layer [P]. Perplexity Health, Samsung, Google all routing through b.well in early 2026 [S]. | Yes for *value*. This directly attacks failure #1 (data without insight). This is the single most important development for Ditto's thesis. |
| **Big Tech still can't make the destination work** | Feb 2026: Apple **shelved** its "Project Mulberry" AI health coach; new lead judged it not good enough vs Oura/Whoop, cited FDA risk [S]. | Tempering signal. Even the AI layer is hard to make sticky and trustworthy. The record alone is not enough; the AI on top is necessary but not sufficient. |

**The three-tier structure of who wins:**

| Tier | Role | Who pays | Verdict |
|---|---|---|---|
| **Consumer PHR / vault** | Patient-facing "own your data" | Almost nobody | **Graveyard.** Free utility at best; never a standalone business. |
| **Aggregation infra ("plumbing")** | B2B API: retrieve, normalize, dedupe, deliver FHIR | Payers, health systems, AI platforms, digital health | **Real business.** $40–50M rounds, becoming the standard layer. |
| **Intelligence on top of the record** | AI that reasons over the longitudinal record | TBD (consumer subs, enterprise) | **Frontier, just opening.** ChatGPT Health is the proof shot. |

## (b) Player teardowns (7-lens)

### CONSUMER PHR — the destination layer (where value does NOT accrue)

#### Apple Health / Health Records
| Lens | Finding |
|---|---|
| **1. Job & moment** | "See all my medical records in one place on my iPhone." Launched 2018 with 12 US health systems via FHIR [S]. Aggregates allergies, conditions, labs, meds, immunizations into a timeline. |
| **2. Sticky mechanic** | None for the records feature itself. Stickiness in the *Health app* comes from the **watch/sensor loop** (steps, sleep, heart rate), not from clinical records. The records sit there. |
| **3. Frequency engine** | Sensor data = daily. **Records = episodic, near-zero return visits.** This is the whole problem in miniature: the part that retains is the wearable, not the record. |
| **4. Monetization** | Records are **free, never monetized**. Apple's monetization is hardware + the (reduced) "Quartz" premium tier planned 2026 [S]. Tellingly, Apple **shelved Project Mulberry**, the AI coach that would have monetized the record, in Feb 2026 [S]. |
| **5. Moat** | Device install base + FHIR partnerships. Strong as a platform, weak as a record business. |
| **6. Outcome & lesson** | Reached huge scale (every iPhone) but the *record* never became the reason anyone uses it. **Lesson: even infinite distribution doesn't make a passive record sticky or monetizable.** |
| **7. EU-applicability** | Available UK + Canada since 2020 [S]; no confirmed broad EU/NL clinical-records rollout. EU integration runs through national frameworks (MedMij, ePA), not Apple. Low direct relevance to Ditto's EU market. |

#### Google Health Connect (note: NOT the dead Google Health 1.0)
| Lens | Finding |
|---|---|
| **1. Job & moment** | An on-device **API/repository** so Android apps share health data with each other. Added FHIR medical-records support March 2025 [S]. It is plumbing, not a destination app. |
| **2. Sticky mechanic** | Indirect: it is infrastructure baked into Android 14+. 500+ apps integrated by May 2024 [V/S]. |
| **3. Frequency engine** | N/A — frequency lives in the apps on top (Peloton, etc.), not in Health Connect. |
| **4. Monetization** | Not directly monetized. Strategic: keeps health data flowing inside Android. |
| **5. Moat** | OS-level integration. Very durable as a pipe. |
| **6. Outcome & lesson** | Google learned from Google Health 1.0: **don't build the destination, build the pipe and bake it into the OS.** |
| **7. EU-applicability** | Global. But again, an enabler, not a market Ditto competes for. |

#### Withings (the one consumer model that monetizes — because it's not a PHR)
| Lens | Finding |
|---|---|
| **1. Job & moment** | Track body metrics with beautiful devices (scales, watches, BeamO). The record is a *byproduct* of the device, not the product. |
| **2. Sticky mechanic** | The **device-data loop**: you weigh in, the app shows a trend. Hardware in your bathroom manufactures the return visit. |
| **3. Frequency engine** | Daily/weekly via physical devices. This is the frequency a pure PHR never had. |
| **4. Monetization** | **~70% hardware** revenue (late 2024) [S]; **Withings+ subscription** ≈€9.99/mo or €99/yr, attach rate up ~40% YoY «unverified» [S]; **B2B Withings Health Solutions** scaled ~10%→~20% of revenue 2021→2025, fastest-growing [S]. |
| **5. Moat** | Hardware design + recurring-revenue flywheel + RPM/payer channel. |
| **6. Outcome & lesson** | Healthy, growing. **Lesson: the record monetizes only when wrapped around a daily device or a B2B reimbursement channel — never as the record itself.** |
| **7. EU-applicability** | French company, strong EU fit. But Ditto is not a hardware company; the transferable lesson is "frequency needs a non-record hook." |

### AGGREGATION INFRASTRUCTURE — the layer that DOES capture value

#### b.well Connected Health (the standout — the layer under the AI wave)
| Lens | Finding |
|---|---|
| **1. Job & moment** | Unify fragmented patient data into one clean, AI-ready FHIR layer that any partner can build on. 60,000+ live consumer-mediated data connections [V]. |
| **2. Sticky mechanic** | **It became the data layer for the 2026 AI health launches.** OpenAI selected b.well to power **ChatGPT Health** (Jan 2026) [P]; reportedly also Perplexity Health, Google, Samsung — "five platform partnerships in five months" [S]. Once you are the pipe under ChatGPT, you are load-bearing. |
| **3. Frequency engine** | Inherits frequency from the apps on top. Doesn't need its own. |
| **4. Monetization** | **B2B/B2B2C.** Pays = payers (commercial/Medicare/Medicaid), health systems, retail pharmacy, AI platforms. Raised **$40M Series C** Feb 2024, ~$133.5M total [S]. Specific pricing/revenue **not disclosed** «unverified». |
| **5. Moat** | Data normalization completeness + becoming the *standard*. "Applications get acquired or commoditized; infrastructure gets buried in the foundation and stays" [S]. |
| **6. Outcome & lesson** | Quietly winning. **Lesson: the company that pipes the record to the AI layer captures the durable value — not the AI app, not the consumer vault.** |
| **7. EU-applicability** | US-centric (TEFCA-adjacent). In the EU this role is filled by national frameworks (MedMij/ePA) + EHDS nodes — see F4. The *pattern* transfers; the company doesn't. |

#### Particle Health / Health Gorilla / 1up Health (the US plumbing pack)
| Lens | Finding |
|---|---|
| **1. Job & moment** | Developer APIs to retrieve and normalize clinical records at scale. Particle: 270M+ records [V]. Health Gorilla: TEFCA-designated QHIN [S]. 1up: clinical+claims for health plans [V]. |
| **2. Sticky mechanic** | Integration lock-in: once a digital-health app builds on your API, switching is painful. |
| **3. Frequency engine** | N/A (infra). |
| **4. Monetization** | **Usage-based / enterprise API fees**, paid by digital health, payers, providers, labs. Particle raised ~$49M (Series B) [S]. |
| **5. Moat** | Network designations (QHIN/TEFCA), data breadth — **but dangerously dependent on upstream gatekeepers.** |
| **6. Outcome & lesson** | **Critical cautionary tale: Particle v. Epic.** In 2024 Epic **cut off Particle's data access** alleging misuse; Particle sued for antitrust (Sherman Act); a network of oncology practices reported 2,800+ patients' care harmed by the blockage [S]; judge let the case proceed [S]. **Lesson: if your business is reselling someone else's data access, the data owner can throttle you. The "plumbing" moat is real but rented.** |
| **7. EU-applicability** | US health-information-exchange specific. EU equivalent risk: dependence on national nodes and provider EHRs. The dependency lesson is the transferable part. |

#### Fasten Health (the open-source / consumer wildcard)
| Lens | Finding |
|---|---|
| **1. Job & moment** | Open-source, **self-hosted** personal/family medical-record aggregator; connects to thousands of providers via SMART-on-FHIR [V]. For privacy-maximalist families. |
| **2. Sticky mechanic** | Ownership + family multi-user. Thin; it's a tool, not a habit. |
| **3. Frequency engine** | Near-zero — same PHR frequency problem, now self-hosted. |
| **4. Monetization** | **Essentially none** (open source). Proves the point: when you strip away enterprise buyers, the consumer PHR has no revenue model at all. |
| **5. Moat** | Community / open source. Not a commercial moat. |
| **6. Outcome & lesson** | Niche by design. **Lesson: the consumer-owned record, in its purest form, is a free utility — confirming value does not accrue here.** |
| **7. EU-applicability** | Self-hosting fits GDPR/privacy-sensitive EU users, but it's a hobbyist segment, not a market. |

### EU / NL — the framework-driven reality Ditto actually lives in

#### Germany ePA (the 2025 opt-out national rollout — the big one)
| Lens | Finding |
|---|---|
| **1. Job & moment** | National electronic patient record for all 73M statutory-insured Germans. Opt-out, not opt-in. |
| **2. Sticky mechanic** | **The default itself.** No persuasion — you have one unless you object (6-week window). |
| **3. Frequency engine** | Provider mandate from Oct 2025 forces clinical touchpoints. But **active patient use lags badly**: 70M accounts created, yet logging in / uploading / sharing "remains far less widespread" [S]. |
| **4. Monetization** | State infrastructure — **not a commercial product.** This is the point: the national record is a public good, not a business. You cannot out-compete it; you build *value on top of it.* |
| **5. Moat** | Statutory. Unassailable as the record of record. |
| **6. Outcome & lesson** | Adoption crisis solved (1.5% → near-universal) **by flipping the default**. **Lesson: defaults beat persuasion for the record; but a record people don't open is still inert. The unsolved problem is the reason to return — exactly the layer an AI assistant could own.** |
| **7. EU-applicability** | This *is* the EU reality. ePA (DE), MedMij (NL), EHDS (bloc-wide) mean the **record is being commoditized by the state**. Ditto must treat the record as a free input, not a product. |

#### MedMij / Quli / Ivido (the NL PGO framework)
| Lens | Finding |
|---|---|
| **1. Job & moment** | MedMij = the NL **trust framework/standard** (via DigiD+BSN) for secure data exchange. PGOs (Quli, Ivido, Drimpy, Zodos) are the consumer apps that pull a **free** copy of your records [P]. |
| **2. Sticky mechanic** | Weak. PGOs are certified plumbing endpoints; little to make you return. |
| **3. Frequency engine** | Low. **~207,000 PGO users in Q1 2024** [S] — tiny vs the IZA goal that every citizen who wants one has a well-filled PGO by end-2025 [S]. The gap *is* the failure pattern repeating in NL. |
| **4. Monetization** | PGOs are **free to citizens** (publicly subsidized framework). No consumer revenue model. Same verdict as everywhere: the record doesn't pay. |
| **5. Moat** | MedMij the framework has a regulatory moat; individual PGOs have none and are interchangeable. |
| **6. Outcome & lesson** | A government-backed PGO framework with full standards and free access still gets ~207k users. **Lesson: even with regulation removing the integration cost, demand for a bare record is anemic. Confirms data-without-insight fails even when the data is handed to you for free.** |
| **7. EU-applicability** | Directly Ditto's home market. The MedMij rails are the *integration path* Ditto should ride; being "just another PGO" is the trap to avoid. |

### THE GRAVEYARD — why each died (do not repeat)

| Player | What it was | Why it died | The transferable lesson |
|---|---|---|---|
| **Google Health 1.0** [S] | Web PHR / data aggregator, 2008–2012 | Only tech-savvy adopters; an "online scrapbook"; **no booking, refill, or messaging** — the jobs users actually wanted. Couldn't translate niche use into daily routine. | Data aggregation with no actionable job = no adoption. |
| **Microsoft HealthVault** [S] | PHR vault, 2007–2019 | **No mobile app**, browser-bound; ignored wearable/dynamic data; weak provider/EHR adoption of its data standard (CCD); no insights, no social. | A static, web-only record missed the frequency device data could have provided. |
| **Vivy (Germany)** [S] | Insurer-backed (Allianz) eHealth record, 2017–~2023 | **Killed by the state**: after Mar 2022 it could no longer act as the eHealth record for statutory funds once Germany's official ePA arrived; pivoted, then wound down. | If your product is "the record," a national record can legislate you out of existence. |
| **Dossia (US)** [S] | Employer-consortium PHR (Walmart, Intel, BP…), ~2006–2016 | **Providers/labs/PBMs refused to share data** or wanted to charge for it; **employees distrusted employer involvement** in their health; spent millions, never reached scale. | Data gatekeepers + a distrusted sponsor kill a record before it starts. |

## (c) White space for Ditto — ruling on the "multiplier, not destination" thesis

**Verdict: the evidence strongly SUPPORTS the thesis. Owning the record is not a business; integrating it to multiply intelligence is the entire game in 2026.**

The case, plainly:

1. **The destination is a graveyard, repeatedly and recently.** Google Health, HealthVault, Vivy, Dossia — and even Apple's records feature never became sticky, with Apple *shelving* its AI coach in Feb 2026. NL's MedMij/PGOs and Germany's ePA show that **even when the state removes the integration cost and hands you a free, well-filled record, demand for the bare record is anemic** (207k PGO users in NL; 70M ePA accounts but minimal active use). The four-part failure pattern — data without insight, no frequency, no actionable job, gatekept integration — is consistent across two decades and two continents.

2. **Value provably accrues to two places, neither of which is the consumer vault:** the **infra/API layer** (b.well, Particle, Health Gorilla, 1up — real revenue, real rounds) and, newly, the **intelligence layer on top** (ChatGPT Health, Jan 2026). The clinching datapoint: **OpenAI did not build a record — it connected one (via b.well) so the AI could reason over the patient's full picture.** That is v2's thesis, executed by the most-watched company in AI, in the same quarter.

3. **Does owning data monetize at all? No — not the consumer-owned record.** Withings only monetizes because the record rides a daily device + a B2B reimbursement channel. Pure consumer PHRs monetize at zero (Fasten = open source; PGOs = free; HealthVault = dead). Value accrues to whoever *pipes* the data (B2B infra) or whoever *reasons over* it (AI). Ditto must be the latter.

**So what is the white space for Ditto?**

| Where Ditto should play | Why it's open / defensible |
|---|---|
| **Integrate the record as fuel for the intelligence layer** | Treat ePA/MedMij/EHDS as free inputs. The assistant with the full longitudinal picture gives radically better summaries, advice, and prep. This is the "multiplier" working exactly as v2 hypothesized. |
| **The frequency the record never had** | Ditto already has the recurring *moment* the PHR graveyard lacked: the medical conversation, repeated (weekly in oncology). The record makes each of those moments smarter; the moment gives the record a reason to be opened. They compound. |
| **EU integration via national rails, not Apple/Google** | In Ditto's market the record is a state-commoditized public good. Ditto should ride MedMij (DigiD) and position for EHDS (see F4) as the integration path — and explicitly *not* try to be "another PGO." |

**The two warnings the evidence forces:**

- **Rented moat (Particle v. Epic).** If integration is via a gatekeeper who can throttle you, the data access is rented, not owned. In the EU the gatekeepers are national nodes and provider systems; the regulatory tailwind (Cures-equivalent, EHDS) mitigates but doesn't eliminate this. **Flag for Merlijn: who can turn off Ditto's data tap, and what is the fallback?**
- **The record alone — even with AI on top — is necessary but not sufficient.** Apple shelving Mulberry, and ePA's 70M-accounts-but-inert reality, both warn that bolting an AI on a record does not automatically create trust, value, or a return visit. Ditto's advantage is that it starts from an *already-frequent, already-trusted moment* (the conversation), and adds the record to deepen it — not the reverse. That sequencing is the whole bet.

**Net:** integrate, don't own. The PHR is the multiplier that makes Ditto's intelligence layer sharper and the loved-one/coordination leans richer. It is not, and should never be pitched as, the destination. **Thesis upheld.**

## (d) Graded citations

| # | Claim supported | Source | Grade |
|---|---|---|---|
| 1 | Apple Health Records launched 2018, 12 hospitals, FHIR | Healthcare IT News — apple-launch-health-records-app-hl7s-fhir-specifications-12-hospitals | S |
| 2 | Apple Health Records UK/Canada availability (2020) | Apple Newsroom / MobiHealthNews — apple-health-records-goes-international | S/P |
| 3 | Apple Project Mulberry AI coach shelved Feb 2026; "Quartz" tier reduced | digitalhealthnews.com; fitt insider; gadgethacks | S |
| 4 | Google Health 1.0 shut 2012; "online scrapbook", no booking/refill/messaging | Computerworld; MobiHealthNews "10 reasons"; InformationWeek | S |
| 5 | Microsoft HealthVault shut 2019; no mobile app, weak CCD adoption, no dynamic data | HIT Consultant; thefresh.co.uk; adaptiveproduct.com | S |
| 6 | Vivy lost statutory-record status Mar 2022 after ePA; wound down | versicherungsbote.de; meine-krankenkasse.de | S |
| 7 | Dossia: employer consortium, providers/labs hoarded data, employee distrust, shut 2016 | mikecritelli.com; InformationWeek; FierceHealthcare | S |
| 8 | Google Health Connect: on-device API, FHIR records Mar 2025, 500+ apps May 2024 | Wikipedia (Health Connect); Android Developers Blog; ASO World | S/V |
| 9 | Withings ~70% hardware; Withings+ €9.99/mo; B2B 10%→20% of revenue | businessmodelcanvastemplate.com; canvasbusinessmodel.com («unverified» figures) | V/S |
| 10 | b.well $40M Series C Feb 2024, ~$133.5M total; 60,000+ connections | FierceHealthcare; PitchBook; PRNewswire (b.well) | S/V |
| 11 | OpenAI selected b.well to power ChatGPT Health, Jan 2026 | PRNewswire / OpenAI / CNBC / FierceHealthcare | P |
| 12 | b.well as data layer for Perplexity, Google, Samsung ("5 partnerships in 5 months"); infra-captures-value framing | onhealthcare.tech | S |
| 13 | Particle 270M+ records, founded 2018, ~$49M funding | CB Insights; PitchBook; Particle Health | V/S |
| 14 | Health Gorilla = TEFCA-designated QHIN | Health Gorilla; CB Insights | V/S |
| 15 | Particle v. Epic: Epic cut off access spring 2024; antitrust suit; 2,800+ oncology patients harmed; motion-to-dismiss denied | Healthcare Dive; FierceHealthcare; STAT; MedCity News | S |
| 16 | Fasten Health: open-source self-hosted PHR, SMART-on-FHIR, family multi-user | blog.fastenhealth.com; GitHub fastenhealth/fasten-onprem | V |
| 17 | Germany ePA opt-out: <1% (2023) → ~70M accounts in weeks; 73M eligible; Jan/Apr/Oct 2025 timeline; accounts ≠ active use; "defaults beat persuasion" | Joep Lange Institute; iamexpat.de; AOK; Bundesregierung | S/P |
| 18 | MedMij = NL trust framework via DigiD/BSN; PGOs free; ~207k users Q1 2024; IZA end-2025 goal | medmij.nl; ICT&health; eudatasharing.eu | P/S |
| 19 | US 21st Century Cures Act: info-blocking ban, free FHIR R4 patient-access API, 2024 enforcement | HealthIT.gov (ONC); CMS; Federal Register | P |
| 20 | PHR/health-app monetization: subscription fatigue, payer/enterprise models win, user≠buyer | interexy.com; appscrip.com; dogtownmedia.com | S |

> **Verification gaps (be honest):** Withings subscription attach-rate and revenue mix (#9) come from secondary business-model write-ups, not Withings filings — treat as directional. b.well's actual pricing/revenue (#10, #12) is undisclosed; the "5 partnerships in 5 months" claim is a single secondary source — verify before quoting in the deck. Apple Mulberry status (#3) is reporting, not an Apple statement.
