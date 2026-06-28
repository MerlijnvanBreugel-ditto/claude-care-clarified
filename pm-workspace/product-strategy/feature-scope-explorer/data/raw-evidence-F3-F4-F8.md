# Raw evidence — F3 (PHR), F4 (EHDS), F8 (operational front door)
_Extracted 2026-06-25 from market-deep-dive briefs. Raw material for features.json._

## Access to all medical data / PHR (F3)
- **Players**: Apple Health/Health Records (every iPhone; record free, never monetized; record itself is a sideline — stickiness is the watch/sensor loop; 12 US systems via FHIR, no broad EU/NL rollout); b.well Connected Health (60k+ live connections, $40M Series C Feb 2024 / ~$133.5M total; CORE — the data layer under ChatGPT Health); Particle Health (270M+ records, ~$49M Series B; developer API); Health Gorilla (TEFCA QHIN); 1up Health (clinical+claims for health plans); Fasten Health (open-source, self-hosted, SMART-on-FHIR, zero revenue); Google Health Connect (500+ apps, FHIR records Mar 2025; on-device pipe).
- **Popularity**: Aggregation becoming standard infra ($40-50M rounds). Consumer record mature in reach (every iPhone) but barely used.
- **Retention**: The record does NOT retain — "records = episodic, near-zero return visits." Stickiness comes from sensors/devices, not clinical records.
- **Reimbursement**: No.
- **Who pays**: Consumer vault = almost nobody. Infra layer = payers, systems, retail pharmacy, AI platforms (b.well); usage-based/enterprise API fees (Particle/Gorilla/1up). Apple = hardware + premium, never the record.
- **Takeaway**: Owning the record is a graveyard; integrate it as fuel. Value accrues to the pipe and the AI on top, never the vault.

## Self-updating health profile (F3)
- Not a named distinct feature. Closest: aggregation infra (b.well, Particle) keeps a normalized FHIR record current; Germany ePA Oct 2025 provider mandate forces clinical touchpoints; Withings shows device-data loop auto-updating body metrics daily (sensor, not clinical).
- **Retention**: Withings device loop is the one auto-updating profile that drives daily/weekly return ("hardware in your bathroom manufactures the return visit"). Passive clinical record does NOT (ePA: 70M accounts, minimal active use).
- **Who pays**: Withings €9.99/mo / €99/yr + hardware.
- **Takeaway**: A self-updating profile drives frequency only when tied to a daily device or recurring moment; auto-freshness of clinical data alone is inert.

## EHDS integration (F4)
- **Players/initiatives**: MyHealth@EU (live today — patient summaries + ePrescriptions, 15 member states; primary-use rail, state-provided); HealthData@EU + national HDABs (secondary use; HDABs designated by 26 Mar 2027, live ~2029); HDAB-NL (Health-RI/VWS/ICTU/CBS/RIVM, €9.5M, pilots 2025-26, obligations ~Mar 2029); xShare "Yellow Button" (Horizon Europe, one-click EEHRxF share; pilot, public good); Gravitate Health G-Lens (IMI2 Oslo+Pfizer, literacy-adapted e-leaflets; concluded ~Oct 2025; non-commercial). Off-mission secondary-use incumbents: IQVIA, TriNetX (300M+ patients), Datavant, Owkin, Aridhia. Finland precedent: Findata + Kanta.
- **Popularity**: Reg EU 2025/327 in force 26 Mar 2025; primary-use live ~Mar 2029 (Group 1), images/labs ~2031. "EU-project-stage, not startup-stage."
- **Reimbursement/who pays**: Primary — state-funded, no consumer monetization. Secondary — pharma/research pay HDABs (cost-recovery, Art. 42). Penalties €10M/2% to €20M/4% global turnover.
- **Takeaway**: 2029+ architecture signal, not a 2026 opportunity. "Launching partner" is positioning language. Design EEHRxF-aware; do MedMij now; embed xShare later. Don't be a consent broker (commoditizing).

## Patient-initiated data sharing (F3, F4)
- **Players**: xShare "Yellow Button" (closest EU "bring your verified record anywhere"; pilot); MedMij + NL PGOs (Quli, Ivido, Drimpy, Zodos, Patients Know Best — citizen pulls free copy via DigiD+BSN; ~207k PGO users Q1 2024); b.well/Particle (consumer-mediated connections); Fasten Health (self-hosted family sharing).
- **Popularity**: Weak consumer pull (NL PGOs ~207k vs IZA goal of every citizen by end-2025). xShare not yet production.
- **Retention**: Poor — sharing primitive alone gives no reason to return; PGOs "not loved."
- **Who pays**: No working consumer monetization; PGOs free/subsidized; xShare grant-funded to embed.
- **Takeaway**: The consent/sharing rung is commoditizing into a public button apps embed. Embed it; don't be it.

## Always-current medication overview (F3)
- Not a standalone product. Meds are one record category Apple Health aggregates; ePrescriptions live on MyHealth@EU; Gravitate Health covers leaflet comprehension not a live list.
- **Takeaway**: Treated as a sub-element of the aggregated record/ePrescription rails. The data is a free input; value is in reasoning over it.

## Messaging professional systems (F8)
- **Players**: Siilo → "Doctolib Connect/Siilo" (550k+ EU members, 1B+ messages; clinician-to-clinician; free to clinicians + enterprise upsell; CORE but acquired by Doctolib Mar 2023); Klara (US, patient↔provider, acquired by ModMed; a practice-software feature); Spruce (US).
- **Retention**: Daily for engaged clinical teams (clinician side).
- **Who pays**: Free to clinicians; enterprise upsell to hospitals (provider/system pays).
- **Takeaway**: Standalone messaging is a feature/acquihire, not a business — and the buyer was the front-door incumbent. Clinician-side anyway.

## Scheduling & appointments (F8)
- **Players**: Doctolib (80M patient accounts, ~400k providers «unverified»; 2024 ARR €348M +22.5%, 99% from provider subs ~€139/mo base / ~€4.5k/yr full stack; €5.8B valuation; weak in NL); DocPlanner Group (13 countries, owns Jameda DE, ~100M monthly users / 210k+ paying doctors «unverified»; profitable Feb 2026, IPO-prep); Doctena (DACH/Benelux, 10k+ doctors, 1.5M visits/mo; roll-up target); Zocdoc (US, ~6M monthly bookings, ~$200M rev; per-booking model caused provider churn — cautionary).
- **Popularity**: Front door "already won in every EU geography that matters" — won per-country, not continentally.
- **Retention**: Provider daily (it's the front desk); patient episodic ("you book when sick"). Frequency on provider side; patient side is reach not habit.
- **Who pays**: Provider subscriptions ~100%. "Patients don't pay" is the law of this layer.
- **Takeaway**: A 16-person patient-side player cannot win the provider supply war; scheduling is thin semantic data. Integrate, don't build. Threat: Doctolib climbing into patient AI ("Doctolib Parents," early 2026).

## Referral management (F8)
- **Players**: ZorgDomein (NL) — **91% of all Dutch GPs** route referrals through it; PE-backed; near-monopoly national rail; also diagnostic requests + consultations.
- **Retention**: Provider daily-operational; invisible to patients.
- **Who pays**: SaaS to system/providers.
- **Takeaway**: Owns the single most decision-dense moment in Ditto's severe-disease beachhead (referral into specialist/oncology). Partner/integration target, never a build target.

## Planning second opinions (F8)
- **Players**: Included Health (Grand Rounds, US) — 6M+ covered lives; changed diagnosis/treatment in 66% of cases (vendor); employer-paid, free to member; Medexo (DE) — 30+ insurer relationships; insurer-paid, document-based; small.
- **Reimbursement**: **Yes in Germany** — statutory Zweitmeinungsverfahren (G-BA): legally mandated free second opinion for specified surgeries.
- **Who pays**: Employer (US) or insurer/system (EU). Rarely the patient. No proven EU patient-pays model.
- **Takeaway**: Closest to Ditto's emotional moment ("is this serious diagnosis right?"), but EU monetization is insurer/system + partly regulated. A patient-facing intelligence feature is plausible; owning second-opinion operations is not.

## Medication ordering & refills (F8)
- Not a standalone market in F8. Adjacent: named in F3 as one of the "actionable jobs" dead PHRs lacked (Google Health 1.0 had "no booking, refill, or messaging"). NHS App handles 67.8M repeat prescriptions/yr. Kry/Livi do scripts + pharmacy/lab referral fees.
- **Takeaway**: Flagged as a must-have actionable job that vaults lacked, but no commercial teardown here. Underexplored.

## Candidate missing features (from F3/F4/F8)
| Capability | Who does it | Size / stickiness | Why Ditto might need it |
|---|---|---|---|
| **In-visit AI scribe (provider-side)** | Doctolib consultation assistant (2025); DocPlanner AI Assistant (5 countries) | Both front-door winners climbing in; Doctolib ~€115M/yr AI R&D | Adjacent to Ditto's exact wedge but sold to the doctor — incumbent encroaching from provider side. A threat to defend. |
| **Patient-facing medical Q&A by life-moment** | "Doctolib Parents" (early 2026, parents 0-4, multi-LLM, EU-hosted, society-credentialed); Apple's shelved Project Mulberry | Doctolib using 80M-account distribution for the most direct understanding→advising encroachment | Front-door incumbent launching the exact intelligence product Ditto calls core, narrow + credentialed. |
| **Device / sensor data loop (passive daily)** | Withings (~70% hardware rev, €9.99/mo, B2B 10%→20%); Apple Watch | The one consumer model that monetizes and retains daily/weekly | F3 lesson: the record gets frequency only wrapped around a recurring hook. Proven alternative frequency engine. |
| **AI triage** | NHS App (AI triage pledged, full front door by 2028) | National scale (~40M registered, ~20M record views/mo) | States bolting AI triage onto free front doors — the free state app moving into intelligence. |
| **Literacy-adapted medicine info / e-leaflets** | Gravitate Health G-Lens (EU-funded, FHIR ePI) | EU funding Ditto's exact comprehension value prop (leaflets only) | Validates the comprehension job AND warns the concept is non-defensible; edge must be breadth + quality. |

**Cross-cutting**: every durable winner across F3/F4/F8 monetizes the provider, payer, employer, insurer, or state — never the patient directly.
