# C3 — The Operational Front Door

> Part II synthesis chapter. Source: brief F8 (anchor: Doctolib), v2 vision (Nick's "front door" layer).
> Shared framing (one line, Part III owns it): money in this space is B2B everywhere; the recurring understood-conversation moment is Ditto's rare asset; reserve the verb "own" for the intelligence layer.

The front door is the operational stack patients touch to *act*: scheduling, prescriptions, professional messaging, second opinion, data access. v2 borrows Nick's hope that owning it pays for the intelligence above it: "if you are the front door, you also hold extra data and you can schedule, which feeds everything above." This chapter tests that.

## 1. How the front door is won, and whether it is closed

Doctolib is the mechanic in pure form. It is not a patient app, it is a **practice operating system**: once a clinic runs its calendar, patient management, billing-to-Social-Security, and AI scribe through Doctolib, ripping it out means re-coordinating the entire front office. The patient side (80M accounts) is a free funnel into the paid provider side.

| Ingredient | What it is | Why a new entrant can't copy it cheaply |
|---|---|---|
| Two-sided network | Patients go where doctors are; doctors go where patients are | Must move *both* sides at once, in one country |
| Practice-OS lock-in | Calendar + records + billing + scribe in one spine | Switching cost is operational, not just contractual |
| Country-by-country supply war | FR 2013 → DE 2016 → IT 2021, local critical mass first | 12 years, ~€500M capital, ~€115M/yr R&D |

**Moat status: closed in the core geographies (FR/DE/IT), open in NL.** Doctolib is ~80% France, 17% Germany, <3% Italy. The front door is won *per country*, never continentally. NL is not a Doctolib stronghold, which is the one live fork (section 4).

## 2. The monetization-fit problem

Every durable winner in this layer monetizes the supply side. There is no exception in the field.

| Player | Who pays | Patient pays? |
|---|---|---|
| Doctolib / DocPlanner / ZorgDomein | Provider SaaS | No |
| Kry / Livi (telehealth) | Public payer (~90%) | No |
| Included Health (US) | Employer | No |
| Medexo (DE) | Insurer | No |
| NHS App / NL PGOs | Taxpayer / system | No |

"Patients don't pay" is not a Doctolib quirk, it is the law of the layer. For a patient-first player, this means the operational front door has no patient-pays business model. To monetize it, Ditto would have to add a **provider/payer-paid B2B SaaS line** — a different company than the one v2 describes, not a free extension of the patient product.

## 3. THE KEY QUESTION: does owning the front door feed the intelligence layer?

**They are two businesses, and the synergy is real but runs the opposite direction from the v2 hope.**

- **Front door → intelligence works.** Whoever holds the patient relationship, the scheduling event, and the data exhaust has the cheapest launchpad for an intelligence product. This is why **Doctolib launched "Doctolib Parents"** (a patient-facing health-question assistant, starting with parents of 0–4s) and **DocPlanner is repositioning as an AI/medical-data company** pre-IPO. Two independent incumbents climbing the same ladder is a pattern, not a one-off.
- **Intelligence → front door does not work.** Being excellent at explaining a diagnosis does not hand you the provider network, the practice OS, or the referral rail. Those are won with feet-on-the-street sales and capital, not patient trust.

So the layers stack in **one direction only**, and the front door is the upstream asset. v2's framing is mechanically correct but strategically inverted for Ditto, because Ditto is not, and realistically cannot become, the front door. The synergy accrues to incumbents. For Ditto it is a threat vector first.

Crucially, **scheduling is not what feeds Ditto's intelligence.** A booking event is a thin operational signal with little semantic content. What fuels the intelligence layer is **the record**, and in NL that is heading toward a free, standardised rail (**MedMij / PGO consolidation, EHDS**). Ditto can get the fuel without owning a front door. That decouples intelligence from the front door entirely.

## 4. The NL fork (a board decision, not a recommendation)

Because Doctolib is weak in NL, the NL booking seat is genuinely less locked than France's. That is real white space. But taking it is a strategic identity choice, not a product extension.

| | Take the NL front-door seat | Stay patient-first |
|---|---|---|
| What Ditto becomes | A provider-SaaS company | A patient intelligence company |
| Sold to | Clinics (daily-use practice OS) | Patients (the understood-conversation moment) |
| Monetization | Provider subscriptions (proven) | TBD, patient/payer (unproven for this layer) |
| Cost | A country-by-country supply war Ditto has never fought | Reuse existing distribution and identity |

This is a fork for Nick and Merlijn to decide at the board level, with eyes open about the trade-off. It is not something a 16-person patient-side team should drift into by building "just scheduling."

## 5. White space + verdict

**Own-vs-integrate per function:**

| Function | Verdict | Rationale |
|---|---|---|
| Scheduling | Integrate | Provider supply war already lost to incumbents; thin data value anyway |
| Referral rail | Integrate | ZorgDomein = 91% of NL GPs; a system standard, not a market. But plug into the referral *event* (most decision-dense moment in the journey) |
| Telehealth | Integrate | Capital-heavy, payer-gated, thin-margin; Kry nearly died building it |
| Pro messaging | Integrate / ignore | Already absorbed by Doctolib (Siilo); clinician-side, wrong audience |
| Second opinion | **Maybe — as a patient-facing intelligence feature** | Closest to Ditto's "is this serious diagnosis right?" moment. Own the *understanding* ("help me sanity-check / get a second opinion"), not the *operations* (EU monetization is insurer/system, partly the regulated Zweitmeinungsverfahren) |
| Data access | Integrate via standards | Ride MedMij / EHDS; don't build a PGO. Owning data *understanding* ≠ owning data *plumbing* |

**Verdict against the 4 core questions:**

| Q | Answer for the front door |
|---|---|
| What do we solve? | The operational jobs are real, but incumbents and the state already solve them, mostly for free |
| Who for? | Front-door monetization serves providers/payers, not the patient Ditto serves |
| What's the moat? | A provider-SaaS distribution moat. Closed per-country; Ditto cannot build it. The defensible moat is the intelligence the front doors do *badly* |
| How do we monetize? | Not patient-pays. Only as a deliberate B2B SaaS pivot (section 4) |

**Bottom line:** the front door is for Ditto an **integration surface and a threat vector, not a business to own.** Integrate, don't build. Treat ZorgDomein (referral moment), MedMij/EHDS (data fuel), and the national apps (distribution) as rails to ride. The one thing worth *owning* is the intelligence layer the front doors are themselves now climbing toward.
