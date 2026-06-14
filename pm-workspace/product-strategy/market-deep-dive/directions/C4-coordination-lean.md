# C4 — Care Coordination as a Lean-In (not the spine)

**Market Deep Dive · Part II · drafted 2026-06-09**

v2's words: "There is a real market here if you do it extremely well, and we should experiment, but it should not be the spine." This chapter shows why that read is correct, and exactly how light the lean-in should be. Shared framing (covered in Part III, one line): money is B2B everywhere, the recurring understood-conversation moment is Ditto's rare asset, and coordination is a lean, not a spine.

## 1. The rule this field obeys

Coordination is a *company* only when bolted to an institutional cost the buyer already owns. Untethered from such a cost, it resolves into a feature. The proof:

| Player | What it tried | Tether to an owned cost | Outcome / lesson |
|---|---|---|---|
| **Wellthy** | Employer-paid caregiving concierge | Employer attrition + absenteeism (HBS: turnover -1–7%, absenteeism -10–50%, ~126% ROI) [S] | ~$56M rev. Works because HR buys an outcome. The human coach, not the app, is what's bought. |
| **Thyme Care** | Value-based oncology navigation | Payer total-cost-of-care (PMPM + shared savings; EmblemHealth) [S] | $178M raised, $480M val. The moat is being trusted with financial risk. |
| **Memora Health** | Standalone "intelligent care navigation" | None durable; B2B SaaS to institutions | Absorbed all-stock into Commure infra, Dec 2024. Coordination → feature of a clinical-ops platform. |
| **Jasper Health** | Cancer navigation chasing CMS codes | Codes, not contracts (no held risk) | Cut ~half of ~48 staff, May 2024. Chasing reimbursement without holding risk is fragile. |

The throughline: where coordination earns money, an *institution buys an outcome* (lower attrition, lower total cost of care). A family buying a nicer message thread does not monetize. That is the rule that governs the entire field.

## 2. Why it does not transplant to NL/EU

The two monetized models are US-benefits-market and US-payer-risk artifacts. Neither rail exists here.

| US ingredient | NL/EU reality | Monetization rail? |
|---|---|---|
| Employers carry health-spend, buy benefits via brokers (PEPM seats) | Universal coverage (Zvw/Wlz); employers don't carry the cost, so the "buy a benefit to manage our cost" reflex is weak | Statutory **zorgverlof** (leave) + paid human **mantelzorgmakelaar** (often via supplementary Zvw) + a *non-paid* "mantelzorgvriendelijk" badge. No PEPM SaaS rail. |
| Risk-bearing payer who keeps avoided cost (MA, EOM; MEOS $70→$110 PMPM) | No NL entity holds oncology total-cost risk; no standing navigation PMPM code | None. Closest cousin **Santeon** is hospitals improving their *own* outcomes (real: ~30% fewer breast-cancer inpatient stays) — clinical value, no third-party enabler revenue line. |
| Neutral EHR-adjacent family portal | **Caren** is tethered to Nedap's Ons EHR, free-to-family; OZOverbindzorg is municipality/insurer-funded non-profit; Familienet is €99/mo to facilities | Low-ticket B2B to care orgs, or public budgets. Not a patient-owned platform. |

The pain is equal or larger here (≈1 in 4 NL workers are caregivers), but the *buying motion* doesn't transfer. Entering the NL professional layer head-on means fighting Nedap's distribution and free-to-family economics.

## 3. White space for Ditto

The one coordination asset every competitor lacks is Ditto's input: the **understood medical conversation**. Caren, Lotsa, OZO and the rest coordinate around an empty calendar or a message thread; Ditto can coordinate around what the doctor actually said and what happens next. That is the natural place to seed sharing inside the oncology beachhead, where a care circle already exists and is anxious for exactly this.

The lightest viable loop, as a growth/retention feature (not a revenue line):

| Element | Spec |
|---|---|
| **Loop** | "Share this summary + next steps with my care circle." Patient taps share; circle member receives the patient-friendly summary and the action list. |
| **Why it works** | The understood conversation is the payload nobody else has; the severe-disease circle is motivated to receive it. This is Ditto's natural virality wedge. |
| **Measure** | Circle invites sent, summaries opened by circle, patient re-engagement after a share. |
| **Explicitly not** | A shared calendar/task manager, a professional portal, or anything sold as a coordination product. Do not rebuild Caren. |

## 4. Verdict

**Experiment lightly. Do not lean in as a market. Do not skip the feature.** Against the 4 core questions:

| Question | Read |
|---|---|
| **What does it solve?** | Real: keeping the severe-disease circle informed off the understood conversation. Worth shipping as a loop. |
| **Who for?** | The oncology beachhead patient and their care circle — the same users, no new segment. |
| **Moat?** | The understood conversation is the moat; the *coordination layer itself* is not. Lean on the asset, not the layer. |
| **Monetize?** | **No NL rail today.** Treat as growth/retention, not revenue. A standalone-market thesis is currently unfunded. |

**Open factual question (would move the verdict):** would a Dutch insurer or the regulator ever create a *billable line* for navigating a severe-disease patient — the NL analog of CMS PIN/EOM that ianacare is chasing via GUIDE? If yes, coordination could become a market here. Worth a direct check with **Zilveren Kruis / VGZ** innovation desks. Until that line exists, hold the standalone-market thesis as unfunded and ship only the lightest loop.
