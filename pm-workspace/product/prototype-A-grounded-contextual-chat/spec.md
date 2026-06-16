# Prototype A — Grounded, Context-Aware Chat that "Turns into Interface" · Feature Spec

**Status:** rough spec for prototyping · **Prepared:** 2026-06-16 · **Branch:** `claude/market-research-synthesis-ltz3lu`
**Companion docs:** [research.md](research.md) · [overview & comparison](../00-overview-and-comparison.md) · mechanics [`M17`](../../research/market-research/findings/M17-table-stakes-mechanisms.md) · landscape [`M11`](../../research/market-research/findings/M11-ai-frontdoor-deepdive.md) · playbook [`S3`](../../research/market-research/synthesis/S3-proven-mechanics-playbook.md)

> This is a **rough feature spec + the full list of open questions to answer before prototyping** — not an engineering doc. ASCII wireframes stand in for visual mockups (deferred this round).

---

## 1. One-liner, job-to-be-done & who

**One-liner:** *Ask anything about your own care and get a calm, plain-language, **cited** answer that you can act on — follow-ups arrive as **savable task pills** with smart due-dates, and every claim links to a trusted source. It explains; it never diagnoses or advises.*

**Primary JTBD** (newly-diagnosed patient + their caregiver, `reused/13`):
- "What did the doctor actually say / what does this word mean?" (comprehension)
- "What was I supposed to do, and by when?" (action recall + scheduling)
- "Is this normal / should I be worried?" → *clarify and route to clinician*, never verdict.

**Who:** the patient and, on consented proxy rails, a caregiver co-user. Beachhead = oncology / serious-illness newly-diagnosed (`reused/13`).

**Why ditto / the wedge:** no engine today is *patient-facing + grounded + cited + aware of the patient's **own record** + EU-available + no-advice* (`research §1`). OpenEvidence/Glass are clinician-only; ChatGPT Health is record-aware but **EU-excluded**; Perplexity/Comet are EU-available + cited but only **web-context**, not *your record*. Grounding answers in the patient's **own appointment history** is the defensible move.

---

## 2. The experience

A chat where the *answer is often a component, not a paragraph.* Three core surfaces: **the chat**, **the action pill → detail panel**, and **the home screen of saved items**.

**(a) Chat with rendered components**
```
┌─────────────────────────────────────────────┐
│  ditto                                   ⋯    │
│                                               │
│  You: what did the oncologist say I need to   │
│       do after last week's visit?             │
│                                               │
│  ditto: Based on your visit on 9 Jun, three   │
│  follow-ups were mentioned:                    │
│   ┌───────────────────────────────────────┐  │
│   │ 🩸 Blood test            due in ~1 wk ▸ │  │  ← action pill (tap → panel)
│   ├───────────────────────────────────────┤  │
│   │ 💊 Start anti-nausea meds       today ▸ │  │
│   ├───────────────────────────────────────┤  │
│   │ 📅 Book follow-up consult     ~3 wks  ▸ │  │
│   └───────────────────────────────────────┘  │
│   “Two of these had timing your doctor gave;   │
│    tap any to check or save it.”               │
│                                               │
│   ┌──────────────── source ───────────────┐   │
│   │ 📄 Chemo side-effects — Thuisarts.nl ▸ │   │  ← cited resource card (tap → read more)
│   └───────────────────────────────────────┘   │
│                                               │
│  [ Ask about your care…              🎤  ➤ ]  │
└─────────────────────────────────────────────┘
```

**(b) Tap a pill → detail panel (with provenance + editable date + Save)**
```
┌──────────────  Blood test  ──────────────┐
│ Type: Lab test                            │
│ Due:  ~16 Jun  (1 week)            [edit] │  ← computed draft, editable
│                                            │
│ Why: mentioned at your visit on 9 Jun     │
│  “…get your blood taken in about two       │  ← source snippet (auditable)
│    weeks.”                                 │
│                                            │
│ This is a reminder, not medical advice.    │
│                                            │
│ [ Save to home ]   [ Snooze ]   [ Dismiss ]│
└────────────────────────────────────────────┘
```

**(c) Home screen — saved actions live here**
```
┌──────────────  Your care — today  ──────────────┐
│  ▸ 🩸 Blood test                   due in 1 week │
│  ▸ 💊 Anti-nausea meds                     today │
│  ▸ 📅 Follow-up consult            due in 3 weeks │
│  ─────────────────────────────────────────────── │
│  Saved from your chat · tap to view or share ⤴   │  ← shareable to caregiver circle
└───────────────────────────────────────────────────┘
```

**Flow:** ask → ditto answers grounded in *your record + trusted sources* → actions render as pills, claims render as cited cards → tap a pill to verify/edit the smart due-date and **Save to home** → saved items can be **shared to the caregiver circle**.

---

## 3. Core features

**v0 (prototype — what we test):**
1. **Contextual Q&A over the patient's own record** — answers "what did my doctor say / what were my actions / what does X mean?" grounded in the user's appointment summaries + a curated trusted-source set.
2. **Generative-UI rendering** — follow-up actions render as **tappable task pills**; tap → **detail panel** → **Save to home**. (Adopt a proven stack — AI-SDK-style tool-call→component — `research §2`.)
3. **Intelligent due-date extraction** — relative dates ("in two weeks") resolved against the **known appointment timestamp**, surfaced as an **editable draft with the source snippet** (`research §3`).
4. **Cited resource cards** — every non-trivial claim links to a clickable, verifiable card from **clinician-grade EU sources** (e.g. Thuisarts.nl, Apotheek.nl, guidelines).
5. **Refuse-when-unsure / no-advice** behaviour with escalation cues ("ask your care team").

**Later (not in prototype):** caregiver-circle sharing of saved items; cross-provider record ingestion (EHDS/PGO/ePA); voice input; symptom-trend links from Prototype B; proactive (un-asked) nudges; multi-language beyond NL/EN.

---

## 4. Mechanics used (proven → better)

| Mechanic (`M17`/`S3`) | Adopt vs innovate | How it shows up |
|---|---|---|
| #8 Grounded & cited (refuse-when-unsure) | **Innovate** | Core: cited answers in patient language over *your* record — the white space |
| #1 Daily anticipatory answer | Innovate | "what did my doctor say / what's next" from episodic visit data |
| #7 Contextual nudges | Innovate (later) | Due-date-aware reminders ("blood test due Friday") |
| #5 Compounding data moat | Innovate | Each saved item + visit enriches future context |
| #10 Voice | Adopt (later) | Voice input as an add-on; not the v0 differentiator |
| Generative UI (action pills, resource cards) | **Innovate (application)** | Proven tech, near-absent in patient health (`research §2`) — *the signature surface* |

**The hero is the task pill, not the chat** — a structured, dated, saveable, patient-owned action object. Chat-with-citations is becoming table-stakes; scribes (Abridge, Nabla) stop at prose (`research §3`).

---

## 5. Context & data model

The product is only as good as the context it grounds in. v0 must know:
- **Appointments & their timestamps** (the anchor for relative due-dates) + the **visit summary text** (ditto's existing asset).
- **Medications, problems, prior actions** mentioned across visits.
- **Trusted-source corpus** — a curated, clinician-authored EU set (NL-first), each citable as a resource card.
- Later: contacts/circle, uploads, cross-provider records (EHDS/PGO).

**Grounding rule:** answers draw on (1) the patient's own record and (2) the curated source set — *not* the open web (avoids the YouTube-skewed-citation failure, `research §4`). Every extracted action carries a **source snippet** for auditability.

---

## 6. Grounding, safety & regulatory

- **Explain, don't advise** — clarify/translate/organize; never diagnose, triage, or recommend treatment. This is also the **cheapest regulatory lane**: it keeps the product in EU AI Act *limited-risk transparency* territory rather than *high-risk* MDAI/SaMD (which bites for new SaMD from **Aug 2026**) (`research §4`, [`M13`](../../research/market-research/findings/M13-partnerships-eu-scribes-eu-block.md)).
- **Refuse-when-unsure** — ~5–13% of unguarded LLM patient answers are unsafe (`M11`); calibrate against over- *and* under-refusal; escalate to "ask your care team."
- **Never fabricate a date** — degrade to a question when confidence is low (the Columbia/JAMA finding, `research §3`).
- **Transparency** — always disclosed as AI; **EU data residency + GDPR consent**; citations only from vetted clinician-grade EU sources.

---

## 7. Success signals (prototype test)

- **Comprehension:** users report they understood their care better (self-report + task-based comprehension check).
- **Action capture:** % of surfaced actions **saved**; % with a **correct** auto-extracted due-date (vs human-verified).
- **Trust:** % of answers where the user opens a cited source; qualitative trust rating.
- **Safety:** zero unsafe answers in an adversarial eval set; refusal calibration (false-refusal rate).
- **The "intelligent vs gimmicky" read:** do users *use* the pills (save/edit), or ignore them and read the text? (Pill-interaction rate.)

## 8. Scope & non-goals

**In:** contextual cited Q&A over the patient's own record; action pills + due-dates + save-to-home; resource cards; no-advice/refuse. **Out (v0):** diagnosis/triage, proactive nudges, caregiver sharing, cross-provider ingestion, voice, non-NL/EN, any medical-device claim.

---

## 9. Open questions to answer before prototyping

**Product / scope**
- [ ] Is v0 strictly Q&A-over-your-record, or also "explain general medical terms"? (Scope of grounding corpus.)
- [ ] Single beachhead condition (oncology) or condition-agnostic from the start?
- [ ] Is "Save to home" the right primitive, or should saved actions push to the device calendar / reminders?

**UX / interaction**
- [ ] When does an answer become a **component** vs stay text? (Rule for when to render pills/cards — avoid over-rendering, `research §2`.)
- [ ] Pill anatomy: what's the minimum on the pill vs in the detail panel? Which actions (Save / Snooze / Dismiss / Done / Share)?
- [ ] Where do saved items live — a home "Your care" list, the timeline, or both? Relationship to Prototype B's timeline?
- [ ] Resource card: inline expand vs full-screen reader? How many citations per answer before it's clutter?

**Content & grounding**
- [ ] Which **trusted EU sources** form the v0 corpus (Thuisarts.nl, Apotheek.nl, Federa/guidelines…)? Licensing?
- [ ] How is "no advice" operationalised in the system prompt + eval — where exactly is the explain/advise line drawn?
- [ ] Refusal policy: what triggers "ask your care team"? How do we measure over/under-refusal?

**Data & context (A-specific)**
- [ ] What does v0 actually have access to — only ditto's own appointment summaries, or also uploads/labs? In what structured form?
- [ ] How is the appointment **timestamp anchor** stored and surfaced for relative-date resolution?
- [ ] How do we represent a "saved action" object (fields: type, due-date, source snippet, status, shareable)?

**Due-date / action extraction**
- [ ] Acceptable accuracy bar for auto-dates, and the confirm/edit UX when confidence is low?
- [ ] Do we always show the **source snippet**, and how do we handle multiple/conflicting dates?

**Privacy / consent / regulatory**
- [ ] EU data residency + GDPR consent model for grounding over health data; what's stored vs ephemeral?
- [ ] Confirm "explain-not-advise" keeps us in limited-risk (not MDAI/SaMD) — get a formal regulatory read.
- [ ] AI-disclosure + escalation copy.

**Engineering / feasibility**
- [ ] Build on an AI-SDK-style generative-UI stack? Streaming + error/fallback-to-text states (`research §2`).
- [ ] STT/LLM provider, EU hosting, latency budget for streamed components.

**GTM / positioning**
- [ ] Lead message: "understand & act on *your* care," not "ask about hypertension" (`research §implications`).
- [ ] B2B2C channel (clinic/payer/patient-org) vs direct — who funds it?

**Metrics**
- [ ] Define the prototype's primary success metric (comprehension lift? action-save rate? trust?).
- [ ] Define the eval set for safety (adversarial patient questions) and date-extraction accuracy.

---

*Sources & full competitive/landscape detail: [research.md](research.md).*
