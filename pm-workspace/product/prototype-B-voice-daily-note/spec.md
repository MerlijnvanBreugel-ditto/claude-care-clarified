# Prototype B — "Jot down your day" · Voice Daily Note · Feature Spec

**Status:** spec for prototyping — key decisions locked 2026-06-17 · **Prepared:** 2026-06-16 · **Updated:** 2026-06-17
**Companion docs:** [research.md](research.md) (see **§7 streaming entity extraction** for the build pattern) · [overview & comparison](../00-overview-and-comparison.md) · mechanics [`M17`](../../research/market-research/findings/M17-table-stakes-mechanisms.md) · mental-health regs [`M14`](../../research/market-research/findings/M14-ai-mental-health-therapy.md) · STT [`Resonate`](../../specs/resonate-custom-model/dutch-medical-training-data.md)

> Tagline (locked): **"Jot down your day."** Not an AI journal, not a therapist — effortless voice capture with live, structured understanding underneath.

---

## 1. One-liner, JTBD & who

**One-liner:** Open ditto and just talk. It listens calmly, streams what you say, and structures it into simple cards — meds, symptoms, mood, treatment, side effects, concerns, questions for your doctor — then saves it. Effortless capture at zero energy.

**Primary JTBD** (`reused/13`, `08b`): the daily lived work of being ill, carried alone — "get what's in my head out," log how I feel / symptoms / meds, remember what to ask the doctor — **without filling in forms when I have no energy.**

**Who:** the patient (often fatigued, low-energy, oncology/chronic); caregiver can carry it on bad days.

**Why ditto / the wedge:** this is the **daily check-in (habit engine)** of the Living Health Companion — frequency, the data moat, and (later) the caregiver feed. The differentiator is **effortless voice capture + *live* fact-extraction into pills** — genuine white space (no journaling app ships live entity pills, `research §2`) — done **calmly** and input-first, *not* as an AI therapist (the lane that collects lawsuits and regulatory exits, `research §1`, `M14`).

---

## 2. The experience

Four surfaces: **home card (+ nudge)** → **live ramble (top-half feed: transcript + pills)** → **"here's what we understood" sheet** → **timeline card (+ 7-day look-back).**

**(a) Home — "ditto today" card with a last-entry nudge**
```
┌──────────────  ditto today  ──────────────┐
│  Jot down your day.                         │
│  How you feel, symptoms, something not to   │
│  forget — just talk.                        │
│                                             │
│            (  ●  tap to start  )            │  ← one action: tap → talk
│  ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ │
│  yesterday · you mentioned the oncologist   │  ← gentle hint (skippable, never required)
│  visit — how are you feeling about it?      │
└─────────────────────────────────────────────┘
```

**(b) Live ramble — top half is the live feed: transcript scrolls upward under a light gradient, pills surface as compact visual chips. Bottom half stays empty/calm. Reference feel: Claude voice (words dimmed until final).**
```
┌─────────────────────────────────────────────┐
│  ░░ …took my anti-nausea pill this ░░         │  ▲ transcript scrolls up,
│     morning and the headache came             │  │ light gradient fade at the top,
│     back around noon, a bit worried           │  │ words dimmed until finalized,
│     about tomorrow's scan▌                     │  ▼ then solid (Claude pattern)
│                                               │
│   💊 anti-nausea    🩹 headache    🫀 worried  │  ← live pills: ICON + short label only,
│                                               │     pop quietly as facts finalize,
│      ·  ·  ·   (just keep talking)            │     no sound / no haptic / no interrupt
│                                               │
│                  ●  stop                       │  ← tap to stop (always visible)
└─────────────────────────────────────────────┘
```
- **Top half only.** All live activity (transcript + pills) lives in the top half; keep the bottom calm and empty. Pills are *visual-first*: a category icon + a 1–2 word label (💊 + drug name; 🫀/heart if mood is fear/scared). Nothing more on this screen.
- **Pills commit only from finalized transcript** (never volatile partials) → no flicker, no duplicates (`research §7`). Extraction may trail the voice by ~1 s — that's calm, not laggy.
- **Silence / rambling is fine.** Long pauses, trailing off, or emotional rambling with no extractable facts is expected and OK — no pills is a valid state.

**(b·i) Stuck? — after ~5 s of silence, a gentle centered prompt (label TBD, e.g. "Not sure what to say?" / "Need a nudge?")**
```
┌─────────────────────────────────────────────┐
│                                               │
│            Not sure what to say?               │  ← appears centered after ~5s silence,
│              ( tap for a nudge )               │     soft; ignore it and keep talking = it fades
│                                               │
│   ── on tap, reveals gentle chips: ──          │
│   ▸ How did you feel today?                    │
│   ▸ Did you take any medications?              │
│   ▸ Any symptoms?                              │
│                       ●  stop                  │
└─────────────────────────────────────────────┘
```

**(b·ii) Crisis state — independent risk module, not the extraction prompt (`research §7`)**
```
┌─────────────────────────────────────────────┐
│                                               │
│         It looks like you could use help.      │  ← centered, calm, no clinical claim
│              You don't have to do this alone.  │
│                                               │
│            [  📞  Reach us  ]                   │  ← one tap → call (NL: 113 / 112)
│                                               │
│              ( or keep talking )               │
└─────────────────────────────────────────────┘
```
Triggers on signals of self-harm/suicidal ideation, extreme pain, or possible medical emergency (e.g. heart-attack language). Tap-to-call is the whole point — prominence + correct routing, not just showing a number (`research §7`, MHACSAF).

**(c) "Stop" → "here's what we understood" sheet — saved by default; adjust or reject, not confirm**
```
┌────────  here's what we understood  ────────┐
│  💊 Medication · Anti-nausea            ▾ ✏︎ │  ← tap ▾ to expand: full value +
│  🩹 Symptom · Headache · ~noon          ▾ ✏︎ │     the direct quote from the audio
│  🫀 Mood · Worried about tomorrow's scan ▾  │     ("…the headache came back around noon")
│  ❓ Question for doctor · ask about scan ▾  │
│                                              │
│  Saved privately. Adjust anything?           │  ← no mandatory confirm step; default = saved
│   [ Tell my family how I'm doing ] (later)   │
│   [ See how this week's going ]              │
│   [ Adjust / reject a card ]                 │
└──────────────────────────────────────────────┘
```
- **No forced confirmation.** Pills are saved by default; the user can **adjust or reject** any pill, but isn't made to tick through them. (Reverses the earlier "confirm-before-register" plan — confirmation friction kills the zero-energy spell; correction stays available, not mandatory.)
- **Expandable detail:** each pill expands to its full value plus the **direct quote** it was extracted from (provenance = trust).

**(d) Timeline card + 7-day look-back**
```
┌──────────────  your timeline  ──────────────┐
│  Today · 4 things noted          [expand ▾]  │
│  This week · headaches on 3 of 4 days,       │  ← 7-day look-back (from the 2nd entry on)
│  meds on track                               │
│  Yesterday · oncologist reflection           │
└───────────────────────────────────────────────┘
```

---

## 3. Core features (v0 — what we test)

1. **Home card + last-entry nudge** — one action (tap → talk); a gentle, skippable hint seeded from the last entry / appointment.
2. **Live ramble, top-half feed** — Resonate streams the transcript (dimmed→solid), scrolling up under a light gradient; minimal, just enough to see it's working. Tolerates pauses and trailing off.
3. **Live fact-extraction pills** — compact, icon-first chips that pop only from finalized text; never interrupt the speaker (no sound/haptic). **The signature feature** (`research §2`, §7).
4. **"Stuck?" assist** — after ~5 s silence, a soft centered prompt → suggestion chips (how did you feel / meds / symptoms) + stop. Skippable.
5. **Crisis routing** — independent risk module → centered "Reach us" with tap-to-call (113/112).
6. **"Here's what we understood" sheet** — saved by default; expandable pills with the source quote; adjust/reject available, not required.
7. **Timeline card + 7-day look-back** — entry lands as an expandable "today's notes" card; from the **2nd entry onward**, a simple pass over the previous 7 days surfaces light patterns (skipped on the 1st entry — a one-shot "you logged once last week" read is worse than nothing).

**Later (not v0):** symptom trends/correlations in time-relation to **Prototype A** (for now A and B are independent); caregiver-circle auto-updates ("tell my family"); "health Wrapped" narrative; passive/wearable inputs; languages beyond NL/EN; weekly-reflection variant.

---

## 4. Categories (pills)

| Category | Icon | Live label example | Notes |
|---|---|---|---|
| **Medication** | 💊 | "anti-nausea" | drug name front and centre |
| **Symptom** | 🩹 | "headache · ~noon" | value + rough time |
| **Mood** | 🫀 / heart | "worried" | heart shown when mood is fear/scared |
| **Treatment** | (tbd) | "chemo round 2" | procedures, therapy, sessions |
| **Side effect** | (tbd) | "tingling hands" | distinct from symptom — tied to a treatment/med |
| **Concern** | (tbd) | "scan tomorrow" | worries the user voices |
| **Open question for doctor** | ❓ | "ask about dose" | things to raise at the next appointment |

Open vs fixed taxonomy and the final icon set are a design task; the set above is the v0 taxonomy.

---

## 5. Context & data model

- **Capture:** audio → **Resonate** streaming STT → streaming entity extraction (Gemini 3.5 Flash, structured output) → typed pills (category, value, time, confidence, **source quote span**).
- **STT:** Resonate is ditto's own Dutch-medical model — it already carries the clinical/Dutch vocabulary, so a **separate lexicon-biasing layer is not needed for v0.** Streaming, NL + EN.
- **Extraction pattern (`research §7`):** show partial transcript dimmed→solid; fire extraction on each **finalized utterance**; stream structured pills; dedup on a stable key (category + normalized value); commit pills only from finalized text. Round-trip target <1 s after an utterance finalizes; cost is pennies per ramble (context-cache the transcript prefix).
- **Entry object:** date, transcript, extracted pills, user adjustments/rejections, links into symptom history.
- **Audio:** **deleted after transcription** (Granola model). Visible recording state, bounded tap-start / tap-stop — no always-listening.

---

## 6. Grounding, safety & regulatory

- **Not therapy, not diagnosis.** The sheet is *"here's what we understood,"* never a verdict. Input-first, no conversational probing — keeps ditto out of the AI-therapist blast radius (`M14`).
- **Crisis routing** — a **dedicated risk-detection module, independent of the extraction model**, biased toward safety (tolerate false positives). On signal → centered, calm "Reach us" with one-tap call to **113 Zelfmoordpreventie** (self-harm) / **112** (medical emergency). Never handle a crisis conversationally (`research §7`).
- **Medication/symptom accuracy** — pills are editable; low-confidence extractions surface tentatively. Resonate's medical training is the first line of defence against drug-name errors.
- **GDPR/EU** — explicit consent, EU residency (Gemini on Google Cloud EU), AI disclosure, audio-delete. Emotion content handled carefully (AI Act limits, `M14`).
- **MDR:** out of scope for the prototype — revisit before any clinical claim or decision-support behaviour.
- **Caregiver sharing:** designed-for, built **later** — consent model deferred.

---

## 7. Success signals (prototype test)

**Primary metrics (locked):**
1. **Repeat entry** — does a user come back and log again? (the existential test for a daily-capture habit)
2. **Notes viewed again** — do users return to read their own entries, and how soon/often? (proof the capture has lasting value, not write-only)
3. **Retention after N entries** — does the habit hold once someone has logged a handful of times? (where logging apps churn ~70%/100d, `research §3`)
4. **Engagement, broadly** — session frequency, entries per active user, completion of started rambles.

**Secondary (qual + instrumented):** effort/feel (can a low-energy user finish in <1 min, one action?); the **"calm not creepy"** read (do live pills reassure without distracting?); extraction precision/recall vs human; next-action uptake (view week / adjust / later: share).

---

## 8. Scope & non-goals

**In (v0):** daily voice ramble, top-half live transcript + live pills, "stuck?" assist, crisis routing, "understood" sheet (saved-by-default, adjustable, with source quotes), timeline card + 7-day look-back from the 2nd entry, audio-delete.

**Out (v0):** weekly-reflection variant; trends/correlations and any time-relation to Prototype A (A and B independent for now); auto caregiver updates; always-listening/ambient; conversational steering/therapy; mandatory pill confirmation; non-NL/EN; diagnosis/therapy claims; gamified streaks; MDR-class behaviour.

---

## 9. Decisions locked (2026-06-17) & remaining opens

**Locked this round:**
- Daily only, no weekly variant; don't assume daily use.
- 7-day look-back after saving, **starting from the 2nd entry** (skip the 1st).
- A ↔ B time-relation view: **later**; independent for now.
- Live extraction shown, **top half, scrolls up, light gradient, minimal** (Claude-style dimmed→solid). Build-design direction approved.
- ~5 s silence → centered "stuck?" prompt → chips (feel / meds / symptoms) + stop. (Rename the prompt — "sparring partner" is a placeholder.)
- STT = **Resonate streaming**; no separate lexicon bias needed for v0.
- Pills: **no mandatory confirmation**; adjustable/rejectable. Categories above approved (+ treatment, side effect, concern, open-question).
- Live pill = icon + short label; heart for scared/fear mood. Sheet pill = title + expandable value + **direct audio quote**.
- Audio **deleted**. Crisis detection + human routing **in v0**. MDR + caregiver sharing **later**.
- Streaming extraction: **the "facts as you speak" pattern is real and buildable** — hybrid of partial-object streaming + commit-on-finalized (`research §7`). **Agreed.**

**Remaining opens (design / eng):**
- [ ] Final label for the "stuck?" prompt; exact silence threshold (5 s start point) and fade behaviour.
- [ ] Icon set for treatment / side-effect / concern; open vs fixed taxonomy.
- [ ] Gradient + scroll params; how much transcript stays visible vs fades.
- [ ] Risk-module thresholds and the precise NL crisis copy/routing (113 vs 112 branching).
- [ ] Partial-object streaming vs debounced re-extraction for v0 (start with commit-on-finalized; layer partial-object streaming if the "magical" feel needs it — `research §7`).
- [ ] EU hosting + cost per ramble at scale (expected pennies; confirm with context caching).

---

*Sources & full landscape (voice intelligent-vs-input verdict, live-extraction precedent, effortless-capture evidence, **streaming-extraction architecture §7**, crisis-routing best practice): [research.md](research.md).*
