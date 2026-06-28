# The Monetization Filter, Applied (Part III)

> v2 makes monetization a hard filter: a beloved thing nobody pays for is excluded. This applies it across the eight fields and names the motions that survive for Ditto. Created 2026-06-09.

## Who pays in each field, and whether it survives

| Field | Who actually pays | Survives the filter as Ditto's revenue? | Note |
|---|---|---|---|
| F1 Symptom / ePRO tracking | Hospital (institutional ePRO), pharma (RWD/PSP), occasionally reimbursement (CANKADO DiGA) | As B2B/RWD, yes. As patient-pay, no. | Tracking is the hook; the alert-to-clinician value is what an institution buys. |
| F2 Journaling / narrative | Almost no one (CaringBridge runs on donations; consumer apps charge a thin subscription) | No as a revenue line. Yes as a stickiness engine. | The best illness-journal in the world cannot charge the patient. |
| F3 PHR / data integration | Infra buyers pay the pipes (b.well); the owned record pays zero | No (owning) / not Ditto's lane (piping) | Value accrues to reasoning over the record, monetised via the intelligence layer. |
| F4 EHDS | Pharma/research buy secondary-use data via national bodies | Off-mission and not near-term | Patient track is a 2029+ rail, not revenue. |
| F5 Care coordination | US employers (Wellthy) and risk-bearing payers (Thyme Care) | Not in NL/EU today (no such buyer) | Becomes a company only bolted to an institutional cost; Ditto holds none. |
| F6 Proactive assistants / coaches | Employers, payers, pharma (DiGA where reimbursed) | As B2B, yes. As consumer subscription, no (every D2C player pivoted to B2B). | Pharma-sponsored oncology programs are the most reachable EU patron. |
| F7 Social / community | Pharma and payers buy the data/RWE the community produces | Not directly. Yes indirectly (B2B2C / RWD on what it produces). | Monetise what the social layer produces, never the social layer itself. |
| F8 Operational front door | Providers (Doctolib), payers (Kry), the state (NHS App) | Not for a patient-side player | Patients-don't-pay is the law of this layer, not a Doctolib quirk. |

The filter is unanimous: **no field monetises on patient payment.** The money is institutional everywhere.

## The motions that survive, for Ditto

Ranked by reachability for a ~16-person EU company, lead with one:

| Motion | Mechanism | Near-term? | Trust / identity cost | Verdict |
|---|---|---|---|---|
| **Home-market B2B licensing** (hospital / insurer, per-pathway or annual) | Sell the value the served patient creates: comprehension, fewer crisis contacts, channel/portal replacement, no-show reduction. Rides the Dutch B2B channels, the diga.nl scheme, and the IZA transformation funds already mapped in the threat analysis. | Yes | Low (clean fit with patient-first) | **Lead with this.** |
| **Pharma-sponsored oncology programs / RWD** | Pharma funds adherence + patient-support + consented real-world data. Validated patrons (Novartis, Sciensus). | Yes | High (risks making the patient the product, against Ditto's trust wedge) | **A deliberate fork for Merlijn.** Acceptable only with consent-first design and a hard line on data use. |
| **Reimbursement (DiGA-style, RCT-gated)** | Clinical trial then a reimbursed tariff. | 2–3 yr | Low, but base-rate-risky (no live oncology-companion DiGA; Mika failed) | A gated go/no-go bet, not a near-term spine. |
| **Direct patient / caregiver subscription** | Premium tier. | Yes | Low | **Topper only.** Low-frequency health does not sustain consumer payment; never the spine. |
| **Employer caregiving benefit (B2B2B)** | Employer pays per seat. | No in NL | n/a | The model does not transplant to the Dutch benefits market. Park it. |

## What the filter kills (say it plainly)

- Journaling as a revenue line.
- Social / community as a revenue line.
- The personal health record as a product (owning it pays zero).
- Care coordination as a standalone market in NL/EU.
- Owning any operational front-door function on patient payment.

These are not failures. Four of the five are valuable as **multipliers or leans** that make the spine stickier and give a B2B buyer more value to pay for. They simply cannot carry the invoice.

## The instruction this yields

Design every layer so an institution can see the value the patient is getting. Lead with home-market B2B licensing. Hold pharma-RWD as a consent-gated fork. Treat patient-pay as a topper and reimbursement as a deliberate, dated bet. The patient is served; the institution pays.
