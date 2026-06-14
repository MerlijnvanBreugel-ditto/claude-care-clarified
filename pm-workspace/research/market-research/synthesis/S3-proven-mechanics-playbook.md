# S3 — The Proven-Mechanics Playbook (adopt-as-is vs innovate-with-ditto)

**Prepared:** 2026-06-14 · **Branch:** `claude/market-research-synthesis-ltz3lu`
**The lens (Mark Pincus):** *take a **proven** mechanic and make it **better**.* Don't reinvent what already works; adopt the proven engagement plumbing to best-in-class standard, and spend ditto's innovation budget only where its edges make a mechanism genuinely better.
**Inputs:** the catalogue [`M16`](../findings/M16-solution-catalogue.md) (152 products, 16 categories) + the mechanisms [`M17`](../findings/M17-table-stakes-mechanisms.md) (10 table-stakes) + the market-research corpus (M1–M15) + ditto's roadmap thesis ([`reused/13`](../reused/13-synthesis-final.md), [`reused/14`](../reused/14-moat-and-platform-strategy.md)).

---

## 1. The thesis in one page

The consumer-health market has already proven what makes a product retain, and it is **structural, not cosmetic** `[M7]`: winners stack a *daily-relevant, anticipatory question with a changing answer*, fed by *passive capture* and a *compounding personal-data moat* (Flo ~60% MAU >1yr; Oura >80% yr-1 renewal; Whoop >50% daily at 18mo). ~71% of health apps are abandoned within 90 days because they invert effort-vs-reward `[M7,M16]`.

So the move for ditto is not to invent new mechanics — it is to **adopt the proven ones and concentrate invention where its edges win:**

> **Adopt-as-is the engagement plumbing** (mechanisms 2, 3, 4, 6, 10 — passive capture, streaks, caregiver sharing, felt reward, voice). Match best-in-class (Duolingo, Strava, Finch, Oura) and move on. **Innovate the intelligence layer** (1, 5, 7, 8, 9 — daily anticipatory answer, compounding data, contextual nudges, grounded-and-cited answers, human-in-the-loop) — where ditto's LLM + smart synthesis + EU clinical-grounding + curated partnerships make a *better* mechanism, and where the moat actually lives `[M17]`.

**The single highest-leverage bet is #1 × #5 × #8 fused:** a daily, forward-looking, *cited* answer — *"given your last visit and what's changed, here's what to watch / ask today"* — personalized to the patient's own record, getting smarter every appointment. No incumbent owns patient-grade, grounded, cited, EU-available, personalized answers; OpenEvidence is clinician-only, Google's health citations skew to YouTube `[M11,M17]`. This *is* the "Living Health Companion" daily loop, expressed as proven mechanics.

---

## 2. The adopt/innovate map — mechanism → proof → market-research → ditto roadmap

| # | Mechanism | Proven by (exemplars) | Verdict | Evidence `[file]` | Maps to ditto feature / roadmap |
|---|---|---|---|---|---|
| 1 | Daily anticipatory **changing answer** | Flo, Clue, Oura | **INNOVATE** | `M7,M10,M17` | **Daily check-in** (habit engine) `[reused/13 §4.1]` |
| 2 | Passive / zero-effort **capture** | Oura, Whoop, Apple Health | Adopt | `M10,M17` | Summaries = consented passive capture; **care graph** ingest `[reused/14 D2/D4]` |
| 3 | **Streaks** / gamified identity | Duolingo, Finch | Adopt | `M10,M16,M17` | Daily check-in retention layer (agency-framed) |
| 4 | Social / **caregiver sharing** | Strava, CaringBridge, Flo | Adopt | `M7,M16,M17` | **The circle** (growth engine) `[reused/13 §4.2]` |
| 5 | Compounding **personal-data moat** | Oura, Whoop, Natural Cycles, Function | **INNOVATE** | `M7,M12,M17` | **Care graph** / longitudinal record `[reused/14 D2/D4]` |
| 6 | Variable + immediate **felt reward** | Calm, Headspace, Finch | Adopt | `M7,M17` | Reassurance/clarity in the summary & check-in |
| 7 | Proactive, well-timed **nudges** | Medisafe (OR 2.34), Oura | **INNOVATE** | `M6,M17` | Contextual reminders in daily loop (refills, "ask this next visit") |
| 8 | **Grounded & cited** answers (refuse-when-unsure) | OpenEvidence, Perplexity Health | **INNOVATE** | `M2,M6,M11,M17` | The companion's Q&A, grounded in the patient's record |
| 9 | **Human-in-the-loop** / reimbursed scaffold | K Health, Maven, Natural Cycles | **INNOVATE** | `M6,M15,M17` | Born in the clinical encounter; **B2B2C / DiGA** moat `[reused/14 D1/D3/D5]` |
| 10 | Conversational / **voice** interface | ChatGPT/Perplexity voice, ElliQ | Adopt* | `M11,M17` | Voice I/O for accessibility (*innovate on *what it says*) |

**Read:** five mechanisms map straight onto ditto's existing **"build = one loop"** roadmap (daily check-in, the circle, the reframed summary) `[reused/13]`; the innovate mechanisms (1,5,7,8,9) are precisely the intelligence layer that turns that loop into a moat `[reused/14]`.

---

## 3. ditto's four edges → the mechanics each unlocks

ditto's stated edges map cleanly onto the *innovate* column — confirming where to spend invention:

- **LLM intelligence** → #1 (manufacture the changing daily answer), #5 (reflect the data moat back), #8 (grounded answers).
- **Smart synthesis** → #1, #5, #7 (the *right* nudge from your summary + meds + upcoming appointments), #8.
- **Voice navigation/processing** → #10 (low-friction, accessible I/O) — adopt the interface, pair it with #8 so the spoken answer is *trustworthy*.
- **Curated-resource partnerships** → #8 (cite EU clinical guidelines/sources), #9 (provider/patient-org/payer embedding → the reimbursed scaffold).

The two edges ditto *doesn't* lean on (raw consumer network virality, wearable hardware) are exactly the *adopt-as-is* plumbing — borrow, don't build.

---

## 4. Prioritized shortlist — adopt now / innovate now / watch

**Adopt now (cheap, proven, execution not invention):**
- **Consented caregiver sharing** of summaries/plans (#4) — the circle; build on NL DigiD Machtigen / DE ePA proxy rails `[reused/13 §4.2]`. GDPR-grade, no-repeat updates, "here's how to help."
- **Gentle, agency-framed streaks** (#3) — "you've stayed on top of your health N weeks," with a Duolingo-style "freeze" to defuse loss-aversion backfire; never "sick-person" framing.
- **Reassurance/clarity as the felt reward** (#6) — "your results are normal — here's what they mean."
- **Voice I/O** (#10) — accessibility for older/low-literacy/low-dexterity users.
- **Passive capture via the summary itself** (#2) — zero-logging, already-consented clinical data.

**Innovate now (the moat — concentrate here):**
- **The fused daily cited answer (#1 × #5 × #8)** — the core bet: a daily, forward-looking, cited, record-personalized "what to watch / ask today," getting smarter every visit. Directly = the daily check-in habit engine `[reused/13 §4.1]`.
- **Contextual nudges (#7)** — LLM-timed to refills, follow-ups, "ask this next appointment" — not scheduled alarms (the #1 backfire).

**Watch / sequence later (heavier, earned after the loop is proven):**
- **Human-in-the-loop / reimbursed scaffold (#9)** — DiGA module + B2B2C distribution + eventual full-stack `[reused/14 D1/D3/D5]`. The retention scaffold and the durable economics, but gated on engagement proof (`reused/13 §6`).

---

## 5. "Proven → better": five worked moves

The Pincus move, made concrete — each takes a *proven* mechanic from the catalogue and applies a ditto edge:

| Proven mechanic (who) | ditto's "better" version | Edge | Mech |
|---|---|---|---|
| Cycle prediction → daily reason to open (Flo) | "Given your last visit + what's changed, here's what to watch/ask today" | LLM synthesis | #1 |
| Medication reminder, OR 2.34 (Medisafe) | Contextual nudge: "your repeat script runs out Friday — flag a refill?" | Smart synthesis | #7 |
| Streaks (Duolingo) | Agency-framed health-ownership streak, caregiver-visible, gentle | — (adopt) | #3 |
| Cited clinical answers for doctors (OpenEvidence) | Patient-language, EU-grounded, refuse-when-unsure, on *your* record | LLM + partnerships | #8 |
| Family updates on WhatsApp (status quo) | Consented, no-repeat circle + "how to help," on proxy rails | — (adopt) | #4 |

---

## 6. How this connects to the rest of the corpus

- **Why these mechanics matter now:** demand is overwhelming (40M ChatGPT health Q's/day) but unmet, and access is solved while comprehension isn't `[S1, M2, M3]`.
- **Why the moat is trust + caregiver + grounding, not features:** the competitive map and Kin teardown `[M4, M5, S2]`.
- **Why retention is the existential question:** the 90-day churn curve and the cycle/meditation/tracker teardown `[M7, M10, M15]`.
- **Why "innovate the intelligence layer" is defensible:** grounded-and-cited is clinician-only today; patient-grade EU-available is white space `[M11]`; and the moat stack underneath is B2B2C + data + regulatory `[reused/14]`.

---

## 7. Open dependency — Linear roadmap cross-check

This playbook maps mechanisms onto ditto's roadmap **as documented in the repo** (`reused/13` "build = one loop"; `reused/14` moat stack). A live cross-check against **ditto's Linear projects/initiatives was not possible this round** — the Linear MCP reads were blocked by an approval gate. **To finalize the roadmap mapping, approve Linear access** (read-only `list_projects` / `list_initiatives` / `list_issues`) and I'll reconcile each mechanism against the actual planned issues/milestones and flag any gaps or conflicts.

---

## 8. One-line takeaway

**Adopt the proven engagement plumbing (passive capture, streaks, caregiver sharing, felt reward, voice) to best-in-class standard; spend invention on the intelligence layer (the daily, cited, record-personalized answer + contextual nudges + the clinical scaffold) — which is both ditto's roadmap loop and its moat.**

*Cross-references: catalogue [`M16`](../findings/M16-solution-catalogue.md) · mechanisms [`M17`](../findings/M17-table-stakes-mechanisms.md) · market framework [`S1`](S1-market-framework-and-direction.md) · implications [`S2`](S2-implications-for-ditto.md) · ditto thesis [`reused/13`](../reused/13-synthesis-final.md) & moat stack [`reused/14`](../reused/14-moat-and-platform-strategy.md).*
