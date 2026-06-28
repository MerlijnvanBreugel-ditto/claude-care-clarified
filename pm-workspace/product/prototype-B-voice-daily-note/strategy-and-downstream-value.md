# Voice Daily Note — Strategic Rationale & Downstream Value (Macro)

**Date:** 2026-06-18 · **Owner:** Merlijn
**Reads up from:** [prototype-spec.md](prototype-spec.md) · [spec.md](spec.md) · [research.md](research.md) · [technical-research.md](technical-research.md)
**Reads against:** [product-context.md](../../context/product-context.md) (current strategy) · [long-term product vision](../../product-strategy/long-term-product-vision/) · [UI references](ui-references/index.html)

> The micro docs answer *how we build the ramble*. This macro doc answers *why it matters to ditto's course* and *what the accumulating capture can become*. One line: **the daily note is the only daily, non-appointment reason to open ditto — which is exactly the gap Code Red named — and every minute of rambling compounds into a longitudinal record that feeds retention, the care circle, the clinician, and the intelligence spine.**

---

## 1. The macro bet

ditto today turns **episodic** medical conversations into summaries. Summaries retain well but are **appointment-gated** — and Code Red diagnosed *"dependence on appointments as the activation trigger"* as the core vulnerability behind the MAU plateau. The daily note (the "ramble") is the structural fix: a **daily**, low-effort, non-visit reason to open the app. It converts ditto from a thing you use *around a doctor's visit* into a thing you use *while living with an illness*.

The deeper bet: a few minutes of daily voice, captured across a treatment trajectory, is the **richest patient-generated data stream in European consumer health** — and ditto is positioned to own the patient side of it. The pills shown in-session are the tip; the value is the accumulating, structured, *patient-owned* record underneath.

---

## 2. Relevance to ditto's current course

Mapped directly to the live strategy ([product-context.md](../../context/product-context.md), 2026-05-30):

| Strategic goal (current) | How the daily note serves it |
|---|---|
| **North Star: Core MAU** (~2,080 → 5K Jun / 50K year-end) | Summaries fire only around appointments. The ramble is a **daily** open-reason → lifts frequency and the `summary_viewed`-class engagement the North Star rests on. |
| **The Code Red vulnerability: appointment-dependence** | This *is* the "Beyond Appointments" non-visit activation path the team is hunting. It de-risks the single biggest named threat. Pairs with phone-call recording (80% of feature requests) as the capture layer. |
| **M1 retention 40 → 60% (Merlijn's KR, offTrack)** | A daily habit loop is the textbook retention mechanism. The look-back ("what to raise at your next visit") is the recurring, felt reason to come back — the leaky bucket's plug. |
| **Care circle = growth engine** (1.62 → 3.4) | The daily ramble is the **raw material for the caregiver feed**: "tell my family how I'm doing" drafts itself from today's capture. Updates → invites → acceptance → the compounding loop. |
| **Oncology beachhead (B2B)** | Oncology is high-symptom-burden over weeks of cycles — the path where daily capture stacks hardest and where the structured PRO stream carries hard clinical evidence (Basch +5mo OS). The daily note is the B2B-monetizable asset. |
| **Intelligence spine / "digital front door"** | Summaries are sparse, episodic data. Daily capture **densifies the longitudinal, patient-owned record** that powers understanding → advising → agency. It is the input layer the whole spine compounds on. |

**One-sentence fit:** it attacks the retention KR and the appointment-dependence vulnerability *at the same time*, while feeding the care-circle growth loop and the long-term data moat.

---

## 3. The trajectory thesis — why a few minutes a day compounds

A single ramble is a note. The same ramble, repeated across a **treatment trajectory**, is a different asset class. Take the oncology beachhead: chemo runs in cycles over weeks; symptoms, side-effects, mood, and questions accumulate daily.

```
Day 1        →  one note. "Headache, took anti-nausea, worried about the scan."
Week 1       →  a pattern. "Headaches on 3 of 4 days; nausea improving."
Cycle / month→  a health story + a clinician-legible PRO stream + a shareable update + a memory.
Trajectory   →  a longitudinal, patient-owned record no competitor and no EHR holds.
```

**Design principle this implies: capture wide, structure quietly, surface selectively.** The v0 shows seven pill categories, but the right *capture* posture is to extract as much as each ramble safely yields, because the downstream value lives in the accumulated structured record, not the in-session display. The patient sees a calm handful of pills; the record beneath gains many dimensions. *(Privacy/consent and the "show calm, store rich" boundary are a real design line — see §6.)*

---

## 4. Downstream value map — what it could become

The "we don't have an overview of what it could be" gap. Each dimension below is *captured in the same daily ramble*, then fans out to a different beneficiary. v0 surfaces only the first column; the rest is the roadmap the capture unlocks.

| Captured dimension | Downstream artifact it powers | Who it serves | Strategic payoff |
|---|---|---|---|
| **Clinical facts** (meds, symptoms, side-effects, treatment) | Symptom/side-effect **trends**; medication **adherence** signal | Patient + clinician | PRO stream (Basch evidence) → B2B value |
| **Concerns & open questions** | The **look-back** + auto-built "**questions for your doctor**" list | Patient | Solves the forgetting problem (Kessels 40–80%) → the primary weekly value |
| **Mood & emotional state** (stated) | Emotional **offload**; "how they're really doing" read | Patient + care circle | Felt-understood retention; later, gentle affect (deferred — see §6) |
| **Reminders & intentions** | Contextual nudges (meds, refills, appointments, "ask about X") | Patient | Daily-relevant reminders → return trigger, not nagging |
| **Impressions & lived narrative** | The patient's **health story** / "**Wrapped**" arc; qualitative colour for the clinician | Patient + clinician | Emotional payoff + a record the system has never had |
| **Relationships & updates** | **Auto-drafted messages to family & friends**; the **caregiver feed** | Care circle | The growth engine — updates → invites → acceptance |
| **Logistics** (appointments, admin) | Calendar fill; pre-visit prep pack | Patient + clinician | Shorter, better consultations; widens activation |

Read top-to-bottom it's a feature roadmap. Read by the right-hand columns it's the strategy: **the patient gets clarity, the care circle gets connection (growth), the clinician gets a PRO stream (B2B revenue), and ditto gets the longitudinal moat (the spine).** One daily action, four flywheels.

---

## 5. Market positioning

The voice-capture-with-intelligence market splits into lanes; the daily note sits in the one nobody owns ([research.md §1](research.md), [Mobbin UI references](ui-references/index.html)):

| Lane | Who | What they own | Gap for ditto |
|---|---|---|---|
| **Input-only dictation** | Wispr Flow, AudioPen, Superwhisper | Fast voice→clean text | No structure, no health, no sharing |
| **Meeting/transcription** | Otter, Granola | Live transcript + post-hoc structure | Not patient-facing, not clinical |
| **AI journaling / reflection** | Rosebud, Reflectly, Mindsera, Stoic | Reflective prompts, mood arcs | Conversational/therapy lane = regulatory risk; not clinical, not shared |
| **Symptom / PRO tracking** | Bearable, Visible, Guava | Structured symptom logs | Manual effort-tax; not voice; not care-circle |
| **Clinician AI scribes** | Abridge, Nabla, Suki, DAX | Clinician-side note from the visit | Provider-owned, not patient-owned, not daily, not between-visit |

**ditto's white space:** *effortless daily voice capture for the seriously ill, structured into a clinically-legible record that the patient owns and the care circle shares.* No one combines **patient-side + voice + clinical structure + care-circle sharing + grounded in the patient's own record**. The defensible compound is not transcription quality (commoditized) — it is **the longitudinal patient-owned record + the care circle + EU-native trust**, exactly the moat the market briefs already named.

Positioning line to test: **"Not a journal, not a tracker, not a scribe — the daily two minutes that keeps you, your people, and your doctor on the same page."**

---

## 6. What would make this *not* work (honest risks)

- **Live-pills UX is unstudied** — capture must stay calm or it breaks the spell (A/B it; [technical-research §4](technical-research.md)).
- **"Capture wide, store rich" is a privacy line.** Storing more than we show is powerful and sensitive — it needs explicit consent framing, GDPR Art. 9 care, and a clear patient-owns-and-can-delete posture. Get this wrong and the moat becomes a liability.
- **Affect inference is deliberately excluded** for now (telling someone "you sound scared" is intrusive) — the mood dimension stays stated-in-words ([CONTEXT.md](CONTEXT.md)).
- **The clinical/PRO claim needs a care feedback loop.** A daily note alone cannot claim Basch-style survival benefit; the value lands only when the stream reaches a clinician who acts ([research.md §6 / patient-value](research.md)).
- **Adherence needs purpose + gentle reminders**, not streak-guilt — even effortless capture churns without a felt reason to return.

---

## 7. The macro bet, in one paragraph

The daily note is not a journaling feature bolted onto a summary app. It is the move that makes ditto a **daily** companion instead of an **appointment** utility — fixing the exact vulnerability Code Red named — and the capture engine for the longitudinal, patient-owned record that the care circle, the clinician relationship, and the entire intelligence spine compound on. The prototype proves the felt experience; this is the trajectory it is designed to unlock.

*Companion build docs: [prototype-spec.md](prototype-spec.md) (how to build it), [technical-research.md](technical-research.md) (the mechanism evidence), [CONTEXT.md](CONTEXT.md) (terms), [ui-references/](ui-references/index.html) (Mobbin inspiration).*
