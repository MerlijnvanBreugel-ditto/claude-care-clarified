# C6 — The JTBD-Forward Map

> Part II of the Market Deep Dive. The other direction. C1-C5 reason *backwards* from the vision (the layers). This chapter reasons *forwards* from jobs people already do badly. v2 names five. We run each: who solves it best today, how, who pays, whether it needs intelligence or just operations, and whether there is a real wedge for Ditto.
>
> Shared framing (one line, Part III owns it): money is B2B everywhere; the recurring *understood-conversation* moment is Ditto's rare asset; integrate-not-own the operational and data layers; the patient is who you serve, rarely who pays.

## 1. The master table — one row per job

| Job (how often) | Who owns it today | How they win | Monetization | Intelligence or operations? | Wedge for Ditto? | Verdict |
|---|---|---|---|---|---|---|
| **Landing & booking appointments** (episodic) | Doctolib (FR/DE/IT), DocPlanner, **ZorgDomein** (NL referral, 91% of GPs) — F8 | Provider-side two-sided network + practice-OS lock-in, won country-by-country. Patient app is a free funnel. | Provider SaaS; **patients never pay** (F8: "the law of this layer") | **Operations.** Scheduling is a thin event with little semantic content. | **No.** The NL moat is closed (ZorgDomein) or owning it means becoming a provider-SaaS company. The synergy runs front-door→intelligence, and Ditto is downstream. | **Integrate** (ride ZorgDomein at the referral moment); never build |
| **Finding your own data** (rare) | PHR/data layer: b.well (US), national rails **MedMij/ePA/EHDS** — F3/F4 | Become the *pipe*, not the vault. Owning the record is a graveyard (Google Health, HealthVault, Vivy, NL PGOs at ~207k users). Value moved to infra below and AI above. | B2B infra (payers, AI platforms); **the consumer record pays zero** | **Neither owns the value** — the record is inert until intelligence reasons over it. | **No wedge in the record itself.** The wedge is *reasoning over* it. The PHR is the multiplier, not the product. | **Integrate via MedMij** today; design EEHRxF-aware for EHDS ~2029. The multiplier, not the destination |
| **Looking things up online** (frequent, low-stakes) | Consumer medical search: ChatGPT Health, Ada, Healthily, Doctolib Parents — F6/F8 | Generic Q&A / symptom triage. Commoditizing fast (ChatGPT Health launched Jan 2026 on b.well). Pure symptom-checkers don't retain (episodic) and pivoted B2B. | Mostly weak; consumer-AI assistants pivoted away from D2C (K Health, Ada, Healthily) | **Intelligence — but commoditized.** Anyone can wrap a frontier model. | **Thin as generic Q&A. Real if grounded in YOUR record.** Ditto's edge is answering "what does *this* mean for *me*" against the understood conversation + record, not generic search. | **Build, but only the grounded version**; skip generic Q&A — that fight is lost |
| **Making sense of literature / the diagnosis** (episodic-but-recurring, high-stakes) | **Comprehension / intelligence — Ditto's core.** OpenEvidence et al. serve the *clinician*; the *patient* side is wide open (Gravitate Health is a non-commercial EU pilot). | Plain-language understanding of what the doctor/letter/scan actually means. This is rung 0-1 of the ladder, CE-light, where Ditto already lives. | B2B (provider/payer/pharma); the comprehension job is EU-validated (Gravitate) but un-commercialized patient-side | **Pure intelligence.** The one rung with no incumbent owning the patient side. | **Yes — the real wedge.** It is what Ditto is, it builds directly on the recurring moment, and big tech/EHRs are worst at it (F3). | **Build — this is the spine.** Own rungs 0-1; route around the Class IIa line with a human for rung 2 (F6) |
| **Updating your loved ones** (event-driven, can be weekly in oncology) | Social / coordination — **WhatsApp is the default** (2B users); CaringBridge/Kanker.nl (charity, can't charge); peer-communities monetize data — F7/F5 | The job is real and durable (CaringBridge: 300k/day) but nobody pays for it. Frequency comes from the *event*, not gamification. | Nobody pays for the social layer directly; it monetizes via what it *produces* (retention, B2B2C) | **Operations/social** on its own; becomes intelligence-backed only when the circle reacts to *understanding*. | **Ownable only as the social surface of an understood care-graph.** As messaging it is a worse WhatsApp and dies. Coupled to comprehension, it is the one thing no one owns. | **Build the lean-in loop** ("circle reacts to the summary"); never the spine, never the till |

## 2. The pattern across the jobs

Two of the five jobs are **operations** (booking, finding data). They are won country-by-country with capital and a provider supply war, monetized off the provider/system, and Ditto sits downstream. **Integrate, never own.** They map to C3 (operational front door) and C2 (PHR-as-multiplier) — and the F8/F3 evidence confirms v2's "integrate, not own" call, with one sharpening: the front-door→intelligence synergy runs *toward the incumbent*, so the door is more threat than opportunity for Ditto.

One job is **commoditized intelligence** (looking things up). Generic Q&A is a lost fight; the only defensible slice is the version grounded in the user's own understood record. That is not a separate product, it is a feature of the spine.

One job is **pure, un-incumbented intelligence** (making sense of the diagnosis/literature). This is C1 (climb the intelligence ladder), rung 0-1, and it is the only job where Ditto already wins and no one owns the patient side.

One job is a **lean** (updating loved ones). Demand is proven, willingness-to-pay is zero, and it is ownable only as the social surface of the care-graph. Maps to C5 (social, lean-in) and C4 (coordination, lean-in) — both correctly classified as leans, now evidence-backed.

| Job | Type | Layer it belongs to (C1-C5) | Call |
|---|---|---|---|
| Booking appointments | Operations | C3 operational front door | Integrate |
| Finding your data | Operations | C2 PHR-as-multiplier | Integrate |
| Looking things up online | Intelligence (commoditized) | C1 intelligence ladder (feature of) | Build grounded only |
| Making sense of literature | Intelligence (open) | C1 intelligence ladder (rung 0-1) | **Build — spine** |
| Updating loved ones | Social/coordination (lean) | C5 social / C4 coordination | Lean-in feature |

## 3. Forward-vs-backward reconciliation

**Where the two lenses AGREE.** The JTBD-forward axis lands on the same place as the vision-backward axis: the **understood conversation is the wedge for the highest-value job** (making sense of the diagnosis). Both lenses independently demote operations and data-ownership to "integrate," both classify social and coordination as leans, and both insist the patient is served but rarely pays. The forwards walk did not contradict the backwards walk — it confirmed it from the demand side, which is the stronger validation because it started from real struggle rather than a chosen vision.

**Where the JTBD lens ADDS something the vision missed.**
- **A near-term shippable job the vision under-weighted: "looking things up, grounded in my record."** The vision treats intelligence as a ladder to climb later; the JTBD lens shows that the *frequent, low-stakes* version of intelligence ("what does this mean for me") is shippable now, sits at rung 0-1, and is the bridge that turns the episodic comprehension moment into a recurring habit. It is the cheapest way to add frequency without crossing the device line.
- **The frequency answer the vision hand-waved.** v2 worries the summary is a weekly-at-most moment. The JTBD map locates the frequency: the loved-ones job (event-driven, many people checking in lightly) and the grounded-lookup job (a question after every appointment, every letter, every scan) are where recurring use lives — not in the summary itself.
- **A direction-of-synergy correction.** The vision hoped owning the front door would feed intelligence. The forward lens (F8) shows that synergy runs the *opposite* way and accrues to incumbents. The vision should stop treating the front door as an opportunity to climb toward and treat it purely as an integration surface and a threat to watch.

## 4. Verdict — the jobs to attack next, in priority order

1. **Making sense of the diagnosis / literature (the spine).** Highest-value, only job with no patient-side incumbent, and it is literally what Ditto is. Builds directly on the recurring understood-conversation moment. Everything else hangs off it. Own rungs 0-1; use a human for the individualized rung-2 step to stay below the Class IIa line.

2. **Looking things up, grounded in your record (the frequency bridge).** Attack only the grounded version, never generic Q&A. Frequency-fit is high (a question after every appointment), monetization-fit rides the spine's B2B model, and it converts the episodic comprehension moment into a habit. This is the cheapest, fastest add and the one the vision under-weighted.

3. **Updating your loved ones (the lean-in growth loop).** Event-driven frequency that Ditto does not have to manufacture, and the one social surface no incumbent owns — *if* the circle reacts to shared *understanding*, not chat. Build it as an activation/retention loop feeding the B2B-paid spine; drive circle size as a first-class metric. Never the spine, never the revenue line.

Booking and finding-data are integrations, not jobs to attack — ride ZorgDomein and MedMij. Generic online lookup is a fight already lost to ChatGPT; do not enter it.
