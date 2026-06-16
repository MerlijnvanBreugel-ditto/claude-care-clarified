# Prototype B — Voice-First "ditto today" Daily/Weekly Note · Feature Spec

**Status:** rough spec for prototyping · **Prepared:** 2026-06-16 · **Branch:** `claude/market-research-synthesis-ltz3lu`
**Companion docs:** [research.md](research.md) · [overview & comparison](../00-overview-and-comparison.md) · mechanics [`M17`](../../research/market-research/findings/M17-table-stakes-mechanisms.md) · retention [`M7`](../../research/market-research/reused/) / [`M10`](../../research/market-research/findings/M10-consumer-app-deepdives.md) · mental-health regs [`M14`](../../research/market-research/findings/M14-ai-mental-health-therapy.md)

> Rough feature spec + the full list of open questions before prototyping. ASCII wireframes stand in for visual mockups (deferred this round).

---

## 1. One-liner, job-to-be-done & who

**One-liner:** *Open ditto, and just talk. It listens calmly, transcribes subtly, and structures what you say into simple cards — symptoms, meds, mood, actions, things to tell your family — then asks what you'd like to do with it. Effortless capture at zero energy.*

**Primary JTBD** (`reused/13`, `08b`): the daily lived work of being ill that's carried alone — "get what's in my head out," log how I feel / symptoms / meds, remember things, decide whether to tell my family — **without filling in forms when I have no energy.**

**Who:** the patient (often fatigued, low-energy, possibly older/low-dexterity); caregiver can carry it on bad days (`reused/13 §4`).

**Why ditto / the wedge:** this is the **daily check-in (habit engine)** of the Living Health Companion — the part that builds frequency, the data moat, and the caregiver feed (`reused/13`). The differentiator is **effortless voice capture + *live* fact-extraction into pills** — genuine white space (no journaling app ships live entity pills, `research §2`) — done **calmly**, input-first, *not* as an AI therapist (the lane that collects lawsuits/regulatory exits, `research §1`, `M14`).

---

## 2. The experience

Four surfaces: **home card (+ nudge)** → **ramble full-view (live transcript + live pills)** → **"here's what we understood" + decide** → **timeline card.**

**(a) Home — "ditto today" card with a last-entry nudge**
```
┌──────────────  ditto today  ──────────────┐
│  What's on your mind?                       │
│  Anything you want to jot down — how you    │
│  feel, symptoms, something not to forget.   │
│                                             │
│            (  ●  tap to start  )            │  ← one action: tap → talk
│                                             │
│  ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ │
│  yesterday · you mentioned the oncologist   │  ← gentle hint (skippable, never required)
│  visit — how are you feeling about it?      │
└─────────────────────────────────────────────┘
```

**(b) Ramble full-view — interface abstracted away; top = subtle live transcript (fades in mid-screen, scrolls up), bottom = live pills accreting quietly**
```
┌─────────────────────────────────────────────┐
│        …took my anti-nausea pill this        │  ▲ transcript scrolls up,
│        morning and the headache came back     │  │ fades in from the middle,
│        around noon, a bit worried about       │  │ no controls, no chrome
│        tomorrow's scan …                       │  ▼
│                                               │
│   (calm — just keep talking)                  │
│ ───────────────────────────────────────────── │
│  💊 Medication taken · anti-nausea            │  ← live pills (white, icon-only
│  🩹 Symptom · headache · ~noon                 │     category; peripheral, never
│  🧠 Mood · worried · scan tomorrow             │     interrupting, no sound/haptic)
│                                               │
│                  ●  stop                       │
└─────────────────────────────────────────────┘
```

**(c) Say "stop" → calm "here's what we understood" + you decide**
```
┌────────  here's what we understood  ────────┐
│  💊 Anti-nausea taken (this morning)     ✏︎  │  ← confirm/edit here (not mid-ramble)
│  🩹 Headache · around noon               ✏︎  │
│  🧠 Feeling worried about tomorrow's scan ✏︎ │
│                                              │
│  Everything's saved privately. What next?    │
│   [ Register it ]                            │
│   [ Tell my family how I'm doing ]           │
│   [ See how my symptoms are trending ]       │
│   [ Adjust / discard ]                       │
└──────────────────────────────────────────────┘
```

**(d) Becomes a "today's notes" card in the timeline (expandable; later → trends)**
```
┌──────────────  your timeline  ──────────────┐
│  Today · 3 things noted          [expand ▾]  │
│  Yesterday · oncologist reflection           │
│  Mon · 2 symptoms, meds on track             │
└───────────────────────────────────────────────┘
```

---

## 3. Core features

**v0 (prototype — what we test):**
1. **Home card + last-entry nudge** — one action (tap → talk); a gentle, skippable hint seeded from the last entry / appointment.
2. **Ramble capture with subtle live STT** — top-half transcript fades in mid-screen and scrolls up; no chrome; tolerates pauses/trailing-off.
3. **Live fact-extraction pills** — bottom-half, minimal (white/light-grey, **category by colored icon only**), accreting quietly; never interrupt the speaker (`research §2`).
4. **"Stop" → understood-summary → decide** — confirm/edit pills *here*; choose: register · tell family · see trend · adjust/discard.
5. **Medication/symptom safety confirm** — meds/symptoms confirmed at the summary before any "register it" (drug-name STT errors are safety events, `research §2`).
6. **Timeline card** — the entry lands as an expandable "today's notes" card.

**Later:** symptom trends & correlations; caregiver-circle auto-updates; "health Wrapped" periodic narrative; passive/wearable inputs; multi-language beyond NL/EN; deeper reflection.

---

## 4. Mechanics used (proven → better)

| Mechanic (`M17`/`S3`) | Adopt vs innovate | How it shows up |
|---|---|---|
| #10 Voice interface | **Adopt** (best-in-class STT) | The capture channel; ~3× faster, fewer errors, best for older users (`research §3`) |
| #2 Passive / low-effort capture | Adopt | Ramble = near-zero-effort; one action |
| #1 Anticipatory changing answer | Innovate | Live pills + a daily-varying calm summary = felt progress |
| #5 Compounding data moat | Innovate | The accreting timeline; each entry makes tomorrow's nudge smarter |
| #7 Contextual nudges | Innovate | Last-entry/event-anchored hint (not a scheduled nag) |
| #4 Caregiver sharing | Adopt (later) | "Tell my family how I'm doing" |
| **Live speech→fact-extraction pills** | **Innovate (signature)** | White space — no journaling app ships this (`research §2`) |

**Positioning (critical):** input-first (AudioPen/Granola lane), *not* conversational AI-therapist (Sonia/Rosebud lane). Intelligence lives in **extraction + summary + trend**, never in probing back-and-forth (`research §1`, `M14`).

---

## 5. Context & data model

- **Capture:** audio → live STT → live entity extraction → typed "pills" (category, value, time, confidence, source span).
- **STT lexicon bias** seeded from the user's own appointment record (meds/conditions) to fight drug-name errors — *an edge ditto uniquely has* (`research §2`).
- **Entry object:** date, raw transcript (retention policy TBD), extracted pills, user decisions (registered? shared?), links into symptom history.
- **Privacy posture (copy Granola):** on-device transcription where feasible, **delete audio after transcription**, visible recording state, bounded tap-start/say-stop — no always-listening (`research §4`).

---

## 6. Grounding, safety & regulatory

- **Not therapy, not diagnosis.** The summary is *"here's what we understood,"* never a verdict. Stay input-first; no conversational probing. This keeps ditto out of the AI-therapist blast radius (Woebot shutdown, Ash UK exit, APA advisory, EU AI Act, `M14`).
- **Crisis routing** — if distress/self-harm signals appear, route to humans/emergency resources (do not "handle" it conversationally).
- **Medication/symptom confirmation** before registering (STT safety).
- **GDPR/EU** — explicit consent, EU residency, AI disclosure, audio-delete; emotion content handled carefully (AI Act emotion-recognition limits, `M14`).

---

## 7. Success signals (prototype test)

- **Effort/feel:** can a low-energy user complete an entry in <1 min, one action? Self-reported effort; completion rate incl. on "bad days."
- **The "calm not creepy" read:** do live pills reassure ("it's listening, it understands") without distracting? (Qual + do they look at the pills mid-ramble?)
- **Capture quality:** extraction precision/recall vs human; med/symptom confirmation accuracy.
- **Retention (the existential test, `reused/13 §5`):** D7/D30 repeat-entry rate for seriously-ill users — does the daily habit hold where logging apps churn (~70%/100d)?
- **Next-action uptake:** % who register / share / view trend.

## 8. Scope & non-goals

**In:** voice ramble, subtle live STT, live extraction pills, stop→understood→decide, timeline card, med/symptom safety confirm. **Out (v0):** trends/correlations, auto caregiver updates, always-listening/ambient, conversational steering/therapy, non-NL/EN, diagnosis/therapy claims, gamified streaks.

---

## 9. Open questions to answer before prototyping

**Product / scope**
- [ ] Daily *and* weekly, or start daily-only? Is there a "weekly reflection" variant?
- [ ] Is v0 capture-only, or does "see how my symptoms are trending" ship in v0 (it's the reward that may drive retention)?
- [ ] Relationship to Prototype A's saved actions / home — one timeline or two surfaces?

**UX / interaction (the signature risk)**
- [ ] **Does live extraction help or distract?** (The key unstudied UX question, `research §2`.) Test: live pills vs pills-only-at-summary.
- [ ] Transcript treatment — how subtle is "subtle"? Fade/scroll params; show full text or fade most away?
- [ ] Pill design — confirm white/light-grey + colored-icon-only; tap → bottom sheet vs inline edit; when (only at summary)?
- [ ] How does it handle silence, long pauses, "I don't know what to say," and rambling that's mostly emotional with no extractable facts?
- [ ] "Stop" — voice command, button, or both? Auto-stop on long silence?

**Voice / STT**
- [ ] STT provider with strong **NL + EN medical** accuracy + low latency; on-device vs cloud (privacy trade-off).
- [ ] Lexicon-biasing from the user's record — feasible in v0? Fallback when meds aren't known yet.
- [ ] Confidence display + the confirm-before-register flow for meds/symptoms.

**Content & categories**
- [ ] What are the v0 **pill categories** (medication, symptom, mood, action, family-update, …)? Fixed taxonomy or open?
- [ ] What detail does a pill hold (value, time, severity, free-text)? What's in the bottom sheet?

**Privacy / consent / regulatory**
- [ ] Audio retention: delete-after-transcription (Granola model) vs keep? Transcript retention?
- [ ] Crisis-detection + human-routing policy and copy.
- [ ] Confirm input-first framing keeps us clear of MDR/AI-Act high-risk; formal regulatory read.
- [ ] Caregiver sharing consent model (later, but design now).

**Engineering / feasibility**
- [ ] Real-time STT + streaming entity extraction architecture; latency budget so pills feel live but calm.
- [ ] EU hosting; cost per minute of streaming STT+LLM.

**GTM / positioning**
- [ ] Position as "jot down your day," explicitly *not* "AI journal/therapist" (`research §implications`).
- [ ] B2B2C channel (clinic/payer/patient-org) vs direct.

**Metrics**
- [ ] Primary success metric — repeat-entry retention? completion-at-low-energy? extraction quality?
- [ ] How we measure "calm not creepy" and distraction.

---

*Sources & full landscape detail (voice intelligent-vs-input verdict, live-extraction precedent, effortless-capture evidence, product-leader principles, mistakes to avoid): [research.md](research.md).*
