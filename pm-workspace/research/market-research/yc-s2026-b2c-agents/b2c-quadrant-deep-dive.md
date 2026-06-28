# B2C Quadrant Deep Dive — YC Spring 2026 (P2026)

Researched 2026-06-19. Five companies the source map placed in "B2C Autonomous Agents." Identity confirmed against primary YC sources for all five. Sources in `sources.md`.

## What the quadrant actually contains

The map's label oversells on both axes. Reality, after verification:

| Company | Truly B2C / patient-facing? | Truly autonomous? | What it really is |
|---|---|---|---|
| **Juno** | ✅ Yes | Semi (patient-initiated, proactive patterns) | B2C AI companion for chronic illness |
| **Clara** | ✅ Yes | ❌ Clinician approves every decision | B2C "AI primary care doctor" |
| **Framewise Health** | ⚠️ Patient is recipient; **sold B2B** | ❌ Clinician reviews each video | EHR→patient-education video engine |
| **Lumius** | ❌ Mis-plotted | ❌ | B2B 3D-ultrasound **hardware** |
| **Adialante** | ❌ Mis-plotted | ❌ | B2B portable-MRI **hardware** |

So only **two** are real B2C patient-facing products (Juno, Clara), one is a B2B tool whose *output* reaches patients (Framewise), and two are medical-imaging hardware that do not belong in this quadrant at all. None is fully autonomous: the moment a product prescribes, orders, or pushes clinical content, a human clinician is kept in the loop, which is a regulatory necessity, not a product gap.

---

## 1. Juno — the one that matters

**`junocompanion.com` · YC slug `juno-chat` · UK-founded · 2 employees · founded 2025**

AI personal health assistant for "the 1B+ people living with chronic illness." The patient talks to "Juno" daily, by voice or text, about symptoms, sleep, meds, and mood. Juno tracks patterns automatically, gives personalised guidance, and turns months of data into a **PDF the patient brings to appointments**. Built on Oxford/UCL research plus 1,000+ patient interviews. Conditions skew to the hard-to-diagnose and under-served: fibromyalgia, long COVID, POTS, ME/CFS, EDS, endometriosis, PCOS, lupus, MS.

- **Founders:** Marshall Gould (CEO, MSc Genomic Medicine, Oxford; lives with ME/CFS) and Isaac Tolley (CTO, Molecular Biology UCL; previously built NHS chatbots). Lived experience + NHS chatbot history is a credible founder-market fit.
- **Traction (FACT, sourced):** 125,000+ patients globally, ~$85K MRR, 9,000+ five-star App Store reviews, launched ~Oct 2025. That is real consumer pull inside ~6 months.
- **Model:** B2C subscription up front (exact pricing not public), with a stated B2B layer: the engagement data becomes "an AI-native patient-engagement platform for pharma, hospitals, medical devices, private clinics." Acquire patients direct, monetise the data/engagement to industry.
- **Geography:** "Global," UK-rooted. No public GDPR/EU data-handling statement found (thin, given the age).

**Relevance to Ditto — the closest analogue on the map.**
- *Same destination:* convert clinical reality into a patient-friendly artifact, then build a care-intelligence layer monetised via pharma/providers. That is Ditto's own long-term thesis, validated by an independent team with traction.
- *Opposite path in:* Juno is **B2C-acquired** (consumer app, direct download); Ditto is **B2B-acquired** (clinic/partner distribution). Same revenue pool, different front door.
- *Different wedge:* Juno = longitudinal daily companion across many chronic conditions; Ditto = the specific consultation made understandable, then care-circle coordination on severe paths (oncology primary).
- **Read: validation + a watch-item, not a today-threat.** It proves patients will pay for AI-structured longitudinal health data and that the data→pharma model works. It is not in Ditto's EU B2B oncology lane now, but a funded B2C player with 125K users and a working pharma-data wedge is the kind of company that can drift toward Ditto's space. Worth tracking quarterly. Note the direct overlap with Ditto's own **Prototype B (voice daily note)** concept — Juno is essentially a live, scaled version of that bet.

## 2. Clara — AI primary care doctor (US)

**`askclara.com` · YC slug `clara-2` · San Francisco · 9 employees · $12M pre-seed (oversubscribed; YC + A.Capital, Liquid 2, SV Angel)**

"AI primary care doctor." Pulls a patient's full history from 150,000+ hospitals/labs/pharmacies, reads labs against the patient's goals, and drafts refills, orders, and care plans, but **every clinical decision is approved by Clara's licensed physicians** (50-state licensed, HIPAA). Optional wearable + longevity-lab bundles. Founders are the ex-Circle Medical team (George Favvas, ex-CEO Circle Medical ~$100M rev; Caitlin Swift; ex-Hims/GoodRx CMO Brendan Levy) — a genuinely heavyweight, proven team, which is why the $12M pre-seed is the largest disclosed raise in this set.

**Relevance to Ditto — low direct threat, high validation.**
- Clara *delivers* AI-assisted primary care (diagnose/treat/prescribe) in the US; Ditto *explains* a clinical conversation and coordinates care in the EU. Different geography (no GDPR collision), different wedge (care delivery vs. comprehension), different buyer (B2C membership vs. B2B-monetised).
- A $12M raise behind a proven team confirms strong investor appetite for "AI ingests your full medical record and acts on it," which is adjacent to Ditto's PHR/record-aggregation ambitions.
- **Watch-item:** if Clara expands from primary care into severe/chronic care *coordination* and a patient's care circle, it converges on Ditto, but that is a future US scenario, not a current EU competitor.

## 3. Framewise Health — patient-education video, sold B2B (US)

**`framewisehealth.com` · YC slug `framewise-health` · San Francisco · 2 employees · ~$500K (unverified; consistent with YC standard deal)**

AI generates personalised patient-education **videos** from EHR data (FHIR-native: Epic, Oracle/Cerner, Athena, eClinicalWorks), a clinician reviews each, then it ships via **SMS link before discharge** in 75+ languages, no app or login. It also tracks comprehension by topic to flag patients who need follow-up. Founders Tane Kim (ex-Brown BS/MD) and David Cui (CTO). HIPAA + SOC 2; no named customers public.

**Relevance to Ditto — same JTBD, different everything else; strong validation, low threat.**
- *Same core job as Ditto:* make clinical information patient-understandable, EHR-adjacent, B2B-monetised. Their "comprehension as a tracked data asset" mirrors Ditto's care-intelligence instinct.
- *Differs:* video vs. summary; the discharge moment vs. longitudinal; US vs. EU; no care circle. The patient is a passive video recipient, not a conversational user.
- **Read: the strongest pure validation of Ditto's thesis on the map** — an independent YC team betting that "translate clinical data into patient-friendly output, monetise B2B" is fundable. Not a competitor in Ditto's lane (US-only, discharge wedge, 2-person seed).

## 4. Lumius — mis-categorised (B2B hardware)

**`lumius-imaging.com` · YC slug `lumius` · San Francisco · 4 employees · Duke BME founders (Tri Vu, Luca Menozzi, Chenhang Li)**

Real-time **3D ultrasound** imaging hardware with AI guidance (auto-detects vessels/nerves), starting with vascular access (central lines), where first-attempt failure runs ~50%. Sold to hospitals/clinics. **Not patient-facing, not an agent.** No product, user, geography, or business-model overlap with Ditto. **Recommendation: drop from Ditto's competitive map.**

## 5. Adialante — mis-categorised (B2B hardware)

**`ycombinator.com/companies/adialante` · Minneapolis · 4 employees · >$3M (incl. $1.18M NSF SBIR Phase II); $12.75M in LOIs, pre-FDA**

A redesigned **portable, low-cost MRI scanner** for cancer screening, sold to medical sites on a flat per-scan fee (hardware-as-a-service). Founders Efraín Torres and Parker Jenkins (biomedical engineers, U Minnesota breakthrough). **Not patient-facing, not an agent.** The only thread to Ditto is the oncology journey: Adialante at *detection*, Ditto downstream at *comprehension/coordination*. Conceivable far-future partner, never a competitor. If anything it reinforces Ditto's "integrate, don't own the rails" thesis — diagnostic hardware is a separate stack.

---

## Verdict for Ditto

1. **The market keeps confirming Ditto's core thesis.** Three independent YC P2026 teams (Juno, Framewise, and arguably Clara) are all betting that turning clinical reality into patient-understandable output, monetised through industry/providers rather than the patient's wallet, is a fundable business. That is Ditto's bet. Nobody is doing it in Ditto's exact shape (EU, B2B-distributed, conversation-to-summary, care circle, oncology-first).

2. **The autonomy axis is theatre, for now.** Every patient-acting product here keeps a clinician in the loop. "Autonomous patient agent" is a positioning label, not a shipped reality in regulated care. Ditto should not feel behind on autonomy, and should be skeptical of competitors who claim it.

3. **Juno is the single company to track.** It is the live, scaled version of Ditto's Prototype B (voice daily note), on the B2C path Ditto chose not to take, with traction that proves the consumer pull. Quarterly watch: does it move from chronic-illness-broad toward severe paths, and does its pharma-data layer mature into the model Ditto is also reaching for?

4. **Two of five were noise.** Lumius and Adialante are hardware mis-plotted into the B2C quadrant. A reminder that secondary positioning maps need verification before they enter our competitive view, exactly the failure mode that produces phantom competitors.

5. **Geography is Ditto's current moat and its risk.** Four of five are US-centric with no GDPR posture. That insulates Ditto in the EU today and is precisely the gap a US winner (Clara, Juno) would have to cross to threaten it. The EU/GDPR-native build is a defensible wedge worth naming explicitly in strategy.
