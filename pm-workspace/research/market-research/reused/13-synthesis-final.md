# 13 — Final Synthesis (Master Document)

**Project:** Life-Changing Healthcare Moments — ditto.care
**Date:** 2026-05-31
**Status:** Refined after red-team (file 12). This is the document to read if you read only one.

> **How to read this:** the *vision* is intentionally bold; the *build* is intentionally narrow and evidence-gated. Everything labelled **Hypothesis** is something the red-team wounded and that must be tested before scaling — not assumed.

---

## 1. The opportunity in one page

People hit by a life-changing diagnosis — cancer, dementia/Parkinson's/ALS, MS/autoimmune, stroke/cardiac — face the **same five problems regardless of disease**: they don't understand or remember what's happening, no one can see the whole picture over time, the people who love them are locked out and overwhelmed, the daily work of symptoms/meds/mood is unsupported, and the emotional load is carried alone. These are not disease-specific and they are not "the patient's job" — they are the **universal operating system of being seriously ill**, and most of them are **daily**, not appointment-bound.

In Europe this touches an outer-bound **~34–38M people living with these conditions (~44–76M including loved ones)**, with a serviceable **~4–5M newly-diagnosed/year** as the highest-intent entry point. The enabling shifts are here now: **LLMs** make plain-language comprehension cheap; **EHDS** (in force 26 Mar 2025; patient summaries EU-wide by 2029) forces patients' data to them but **won't explain it**; and **caregiving** (~80% of EU long-term care, informal) is at a breaking point with its behavior already living, ungoverned, on WhatsApp.

ditto today owns the thinnest, most episodic slice — the appointment summary. The opportunity is to use it as a wedge into the **daily, multi-player territory nobody owns.**

---

## 2. What we know with high confidence (the validated core — survived the red-team)

1. **Comprehension failure is universal and severe.** 40–80% of medical information is forgotten immediately; ~half of the rest is wrong ([Kessels 2003](https://journals.sagepub.com/doi/10.1177/014107680309600504), *verified*). Amplified by **47.6% of EU adults having limited health literacy** ([HLS19](https://m-pohl.net/HLS19), *verified*).
2. **No one owns the longitudinal, cross-provider overview.** ~50M multimorbid Europeans; the family is the silent integration layer; EHDS will populate the record but not interpret it.
3. **The loved-one is the missing user.** ~80% of EU long-term care is informal; caregivers are locked out, untrained, and unsupported — the "hidden patient."
4. **The frequency problem is real** (pending confirmation against ditto's own data, §6): an episodic, single-player, externally-triggered summary cannot build a habit, a data moat, or network effects.
5. **The direction of the flip is right:** change the unit from *appointment → day*, and from *patient → patient-and-circle.*

## 3. The category & the flip (the vision)

**Category to define and own — "The Living Health Companion: a care OS for patients and the people who love them."**

> **Before:** healthcare happens *to you* in episodes you don't understand, can't remember, can't oversee, and carry alone — stitched across WhatsApp, a notes-app symptom list, pill alarms, Dr. Google, a binder of letters, and a portal you can't read.
> **After:** you and your circle have one calm daily companion that helps you understand and manage your illness day to day, lets the people who love you actually help, and turns each clinical encounter into one you walk into prepared and walk out understanding.

**The appointment summary is not the product — it is the proof-of-trust artifact and the periodic crystallization of the daily relationship.** (Red-team D1/B2: the summary is *not* defensible on its own and is a fast-follow target for AI scribes; the defensibility is the daily multi-player relationship.)

## 4. The narrowed build (ruthlessly sequenced — red-team E1)

Vision = the OS. **Build = one loop:**

**Layer onto the existing summary, in this order:**
1. **Daily check-in (the habit engine):** a low-effort, *adaptive-cadence*, opt-in symptom/mood/med log. Anchored on the **painkiller** job — "is this normal, what did my team say to watch for?" — surfacing patterns and prompting questions, **without** a triage verdict (stays non-device; red-team D1). Must gracefully go quiet on bad days and let the **caregiver carry it when the patient can't** (red-team C2).
2. **The circle (the growth engine — *Hypothesis*):** permissioned, no-repeat updates + "here's how to help," built on existing national proxy rails (DE ePA ≤5 representatives; NL DigiD Machtigen). Privacy-by-design, patient-as-owner, revocable — a **P0**, not v2 (red-team D3).
3. **The summary, reframed:** now grounded in a month of real daily data and shareable to the circle in one tap — the crystallization, not the core.

**Explicitly deferred:** true clinical triage (until a deliberate CE-marked/DiGA module is justified), full cross-provider record aggregation, lifestyle/peer-community layers, and multi-journey expansion.

## 5. The honest risk register (hypotheses to test, not wins to assume)

| # | Risk / hypothesis | Red-team verdict | Why it could kill the bet |
|---|---|---|---|
| **1** | **Monetization / who pays** | **Unresolved — biggest risk** | EU patient-pay is hard; charging the seriously ill is fraught; loved-one-payer unproven; DiGA needs the device status we're avoiding early. |
| 2 | **Network effects compound** | Wounded (aspirational) | CaringBridge/WhatsApp already exist and didn't become category-defining; the circle may be a feature, not a company. |
| 3 | **Daily engagement from the sick** | Wounded | Fatigue/depression/"I want to forget I'm sick" fight a daily habit; peak-need moments are when people least open an app. |
| 4 | **Non-device version still valuable** | Tension | The most valuable job is the regulated one; the de-risked version may be a vitamin. |
| 5 | **Beachhead choice** | Uncertain | Cancer = biggest but crowded + heavy; MS/autoimmune = cleaner but smaller. |
| 6 | **The frequency problem's true size** | Unmeasured | Based on the founder's account, not yet ditto's own retention data. |

## 6. What to do next (evidence-gated, cheapest-first)

**Step 0 (this week, near-free): measure the actual problem.** Pull ditto's own Mixpanel/Granola/usage data to quantify the real frequency/retention of the summary product and what users already ask for. *This was out of scope for the external round and is the highest-ROI next move* (red-team E3).

**Step 1 (weeks, concierge): two parallel 30-person cohorts** — newly-diagnosed cancer+caregiver vs MS/young-autoimmune — running a wizard-of-oz daily check-in + manual circle updates. **Primary metrics:** D30 daily-check-in retention (target ≥40% checking in ≥4 days/wk), average circle size seeded per patient, and **whether any invited loved one starts their own circle** (the network seed — the single most important signal). Pick the beachhead from data.

**Step 2 (in parallel): two pre-build research spikes** — (a) **monetization**: price-probe patient/family subscription vs loved-one-as-payer vs B2B2C/insurer/DiGA; (b) **regulatory**: get a formal read that the non-device "watch-for" design stays outside MDR.

**Gate:** do not scale until engagement (≥1 cohort), a credible payer, and the non-device design are all validated.

## 7. The question to hold above all

> *Are we building a daily companion that happens to make summaries — or a summary tool pretending to be daily?*

Every roadmap decision is tested against whether it increases **daily, multi-player** engagement. The vision is the operating system for living with serious illness; the discipline is to earn it one validated loop at a time.

---

### Appendix — confidence summary
- **High / verified:** Kessels recall, HLS19 health literacy, EHDS dates & scope, Eurocarers informal-care share, EU multimorbidity, the five universal clusters.
- **Directional (US-flagged):** Basch survival, discharge-comprehension %, caregiver-mortality magnitudes, transportation burden.
- **Low / unresolved:** monetization, network-effect compounding, daily-engagement retention, dementia incidence, AMI-survivor pool, exact TAM.
