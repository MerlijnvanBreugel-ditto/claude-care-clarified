# Prototype A — Grounded, Context-Aware Medical Chat that "Turns into Interface"

**Prepared for:** ditto.care (EU/NL patient-facing health-tech) · **Author:** Product + market research analyst
**Date / access date:** 2026-06-16 · **Scope:** deep research against Prototype A
**The prototype:** a patient chat that is (1) **grounded** in trusted medical sources + the patient's **own record**, clarifies but gives no medical advice; (2) **context-aware** (appointments, uploads, history — "what did the doctor say?", "what were my follow-ups?"); (3) **renders interactive UI, not text** — follow-ups as tappable task **pills** → detail panel → **Save** to home; citations as clickable **resource cards**; and **intelligent due-date extraction** ("blood test in two weeks", said last week → "due in ~1 week").

> **Sourcing.** Inline `[Source, year](url)`. Tiers: **T1** = peer-reviewed / official company / regulator · **T2** = reputable press · **T3** = blog / vendor / SEO (FLAGGED). Confidence: high / med / low. **US→EU FLAG** marks US-origin facts that may not transfer to NL/EU. Reuses the ditto corpus (`M11`, `M16`, `M17`, `S3`) for already-vetted facts; net-new facts are freshly cited. Access date for all live URLs: **2026-06-16**.

---

## Key takeaways

- **White-space verdict (high confidence):** the four-corner intersection — **patient-facing + grounded-and-cited + context-aware to the user's own record + EU-available + no-advice** — is still **unoccupied**. The best *cited* engine (OpenEvidence) is clinician-only; the best *patient + record-aware* engine (ChatGPT Health) is **excluded from the EEA/UK/CH** `[M11]` [[OpenAI, 2026](https://openai.com/index/introducing-chatgpt-health/), T1]. Prototype A is pointed exactly at that gap.
- **Generative-UI verdict (med-high):** "chat that renders interactive components" is now a **proven, productionized pattern** (Vercel AI SDK generative UI, Claude Artifacts, ChatGPT Canvas) — but **almost nobody applies it to patient health**, and that is Prototype A's most differentiated surface. The mechanic feels *intelligent* when components are the *answer* (a tappable task is the follow-up); it feels *gimmicky* when UI is decoration on top of text.
- **The single most novel element is the task "pill" + due-date extraction**, not the chat. Chat-with-citations is becoming table-stakes (M17 #8); turning unstructured visit text into **dated, saveable, actionable items** is the part incumbents under-serve — scribes (Abridge, Nabla) generate plain-language summaries but stop short of structured, patient-owned, dated task objects.
- **Due-date / action extraction is feasible but safety-fragile.** LLMs extract dates/scores from clinical text with *high* accuracy on clean single-field tasks [[PMC, 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10888985/), T1] but **degrade badly on messy, real-world notes** — a Columbia/JAMA Network Open study found GPT-4 could **not reliably** reproduce a simple string-search extraction across 54,569 ED records [[ScienceDaily/Columbia, 2024](https://www.sciencedaily.com/releases/2024/08/240819130535.htm), T1]. Treat extracted dates as **drafts the patient confirms**, never silent truth.
- **Safety is the product, not a guardrail.** ~**5–13% of unguarded LLM answers to patient questions are "unsafe"** (npj Digital Medicine 2026) `[M11]`, and Google AI Overviews' health citations skewed to **YouTube (~4.4%) over peer-reviewed journals (~0.48%)** `[M11]` [T3]. Refuse-when-unsure, clinician-grade sources, and "no advice" framing are differentiators, not compliance overhead.
- **EU regulatory posture is a design input from day one.** A patient chatbot that "clarifies/explains" may sit in **limited-risk transparency** territory, but the moment it nudges clinical decisions it risks **high-risk MDAI** classification; SaMD on the EU market must meet high-risk AI requirements from **Aug 2026** [[Tandem Health, 2026](https://tandemhealth.ai/resources/knowledge/eu-ai-act-explained-what-healthcare-organisations-need-to-know), T2; [MedDeviceGuide, 2026](https://meddeviceguide.com/blog/eu-ai-act-medical-devices-compliance-guide), T2]. The "no medical advice + grounded + cited" stance is also the *cheapest regulatory lane*.
- **Borrow the mechanics, not the model:** Granola/Notion extract owners+deadlines from natural language; Cleo/Monzo render plain-language cards over complex personal data. The transferable pattern is **structured, confirmable action objects surfaced as cards** — proven outside health, near-absent inside it.

---

## 1. Patient-facing grounded-and-cited answer engines — the competitive deep-dive

The corpus established the headline: *grounded + cited* leaders are clinician-only or EU-absent `[M11, M17]`. This pass profiles each against Prototype A's five tests — **grounded? cited? context-aware to the user's own record? EU-available? safe-by-design (refuse-when-unsure)?**

| Engine | Grounded | Cited | Context-aware to *your record* | EU-available | Safe-by-design / no-advice |
|---|---|---|---|---|---|
| **OpenEvidence** | **Yes** (NEJM/JAMA/NCCN-licensed) | **Yes** (primary lit) | No | Limited (US guidelines) | High (clinician-gated) — **but clinician-only, NPI-verified** `[M11]` |
| **Perplexity Health / Comet** | Partial (web + premium sources) | **Yes** | Partial (EHR/wearables via b.well, US) | **Comet now global** incl. EU [[Wikipedia/Comet, 2026](https://en.wikipedia.org/wiki/Comet_(browser)), T2; T3] | Med — "when to seek care" guidance, but general-consumer |
| **ChatGPT Health** | Yes (grounding-aware, 260+ MDs) | Partial | **Yes** (portals via b.well, Apple Health, labs) [[Medical Economics, 2026](https://www.medicaleconomics.com/view/openai-launches-chatgpt-health-directly-linking-patient-portals-to-the-ai-chatbot), T2] | **No — excluded from EEA/UK/CH** `[M11]` | Med — sandboxed, "inform not replace doctor", but "makes things up" critique persists [[Harvard/TagTeam, 2026](https://tagteam.harvard.edu/hub_feeds/3382/feed_items/17173992), T2] |
| **Google AI Overviews / AI Mode** | Partial (web) | Partial (weak quality) | No | Lagging (DSA/DMA); **pulled from some medical queries Jan 2026** `[M11]` | Low — YouTube-skewed citations `[M11]` |
| **Glass Health** | **Yes** (literature + guidelines, inline cites) | **Yes** | No (clinician CDS) — *can* generate patient-facing education/discharge text [[Glass Health, 2026](https://glass.health/features), T3] | Unclear / US-first | High (clinician DDx tool) |
| **Consensus** | **Yes** (peer-reviewed papers) | **Yes** | No | Yes (web) | Med — research engine, not clinical |
| **Ada Health (DE 🇪🇺)** | Yes (curated medical KB) | Partial | Partial (session intake) | **Yes (EU-built)** `[M16]` | High — most clinically validated symptom checker |
| **K Health (US)** | Yes (clinical data) | Partial | Partial (intake → clinician) | No (US) | Med — AI intake *into* a care transaction `[M16]` |
| **Docus** | Yes (AI + doctor network) | Partial | Partial | Partial | Med — AI answer + human 2nd opinion `[M16]` |
| **Buoy (US)** | Yes (triage KB) | No | Partial (session) | No | Med — episodic triage `[M16]` |

**Net-new this pass:**
- **Comet went global (incl. EU) in 2026** — a shift from M11's "partial/unclear" EU status. Its "Assistant" reads what you're looking at and explains it [[Beginners in AI, 2026](https://beginnersinai.org/whats-new-perplexity-2026/), T3; [Wikipedia, 2026](https://en.wikipedia.org/wiki/Comet_(browser)), T2]. This makes Perplexity the **closest EU-available, cited, context-aware** competitor — but its "context" is the open web / current page, **not the patient's longitudinal medical record**. That distinction is Prototype A's wedge.
- **ChatGPT Health's context-awareness, examined honestly:** it is genuinely record-aware (labs, visit summaries, meds via b.well; visit-prep; plain-language lab readouts) and **sandboxed** with its own memory store [[Medical Economics, 2026](https://www.medicaleconomics.com/view/openai-launches-chatgpt-health-directly-linking-patient-portals-to-the-ai-chatbot), T2; [Fierce, 2026](https://www.fiercehealthcare.com/ai-and-machine-learning/openai-launches-chatgpt-health-connect-data-health-apps-medical-records), T2]. But (a) it is **EEA/UK/CH-excluded**, (b) b.well is a **US provider network**, and (c) critics note it still **"makes things up"** [[Harvard, 2026](https://tagteam.harvard.edu/hub_feeds/3382/feed_items/17173992), T2]. So even the strongest record-aware engine is *both* unavailable to ditto's users *and* unproven on patient-grade safety.
- **Glass Health** is worth watching: it explicitly can generate **patient-facing education, discharge instructions, and plain-language explanations**, evidence-grounded with inline citations [[Glass Health, 2026](https://glass.health/features), T3]. It is the clinician engine most likely to "go patient" — a future competitor, not a current one.

**White-space verdict (restated, high confidence):** no single engine occupies *patient + grounded + cited + record-context-aware + EU-available + no-advice*. OpenEvidence/Glass are clinician-only; ChatGPT Health is EU-excluded and US-record-bound; Perplexity/Comet are EU-available and cited but **web-context, not record-context**; Ada is EU and safe but **triage, not a grounded answer engine over your own visit history**. ditto's defensible move is **grounding answers in the patient's own appointment record** — a context no open-web engine has `[M16, S3]`.

---

## 2. Generative UI — chat that renders interactive components

This is the corpus's thinnest area and Prototype A's most differentiated surface, so it gets net-new depth.

**The pattern is now production-grade.** The **Vercel AI SDK** ships first-class *generative UI*: model tool-calls map to React components, streamed server-side, so the model returns **interactive components instead of text** [[Vercel, 2024](https://vercel.com/blog/ai-sdk-3-generative-ui), T1; [AI SDK docs, 2026](https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces), T1]. Production guidance already covers **tool-call previews, partial/streaming UI updates, retries, and inline source citations while generating** [[prompt-kit, 2026](https://www.prompt-kit.com/vercel-ai-sdk), T3] — exactly the surfaces Prototype A needs (task pills + resource cards mid-stream).

**Claude Artifacts / ChatGPT Canvas** prove the *adjacent-panel* UX at consumer scale: substantial output (apps, docs, components) renders in a **live side panel** you can edit and iterate on without leaving chat; Artifacts now support **persistent storage, MCP integrations, and "Live Artifacts" that refresh with current data** [[Albato, 2026](https://albato.com/blog/publications/how-to-use-claude-artifacts-guide), T3; [QWE, 2026](https://www.qwe.edu.pl/tutorial/claude-artifacts-interactive-content-tutorial/), T3]. Canvas specializes in **targeted edits** (select text → revise just that) [[XsOne, 2026](https://xsoneconsultants.com/blog/chatgpt-canvas-vs-claude-artifacts/), T3]. The shared lesson: **chat for intent, panel for the durable artifact** — which maps directly onto Prototype A's "tap pill → detail panel → Save to home."

| Example | Pattern | What's good | Transferable to Prototype A |
|---|---|---|---|
| Vercel AI SDK generative UI | Tool-call → streamed React component | Components *are* the answer; streaming + citations native | The literal build pattern for task pills & resource cards |
| Claude Artifacts | Chat + live side panel, persistent, MCP-connected | Durable, editable, iterable artifact beside the chat | "Detail panel" + "Save to home" UX |
| ChatGPT Canvas | Inline targeted-edit pane | Surgical edits, no full regeneration | Editing a task's due date / details in place |
| Cleo / Monzo (fintech) | Plain-language cards over personal data + nudges | Warm persona makes complex data legible `[M16]` | Tone + card-feed over medical complexity |
| Granola / Notion AI | Action items rendered as owner+deadline rows | Commitments become structured, trackable objects | The task-pill mechanic itself |

**UX patterns that make it feel *intelligent* vs *gimmicky*:**
- **Intelligent:** the component *is* the answer the user wanted (a tappable, dated follow-up); it is **actionable** (Save, snooze, mark done); it **streams in** so the answer feels live; and it carries its **provenance** (the cited resource card behind the claim).
- **Gimmicky / pitfalls:** UI as decoration over text the user must still read; **components that don't persist** (a pill you can't save is worse than a sentence); **over-rendering** every reply into widgets (cognitive load); and rendering an interactive control that implies an action the system can't actually take (false affordance). Production write-ups stress **error states** (`input-available` / `output-error`) and graceful fallback to text when a tool fails [[AI SDK docs, 2026](https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces), T1].

**Verdict:** generative UI is **safe to adopt as the rendering layer** (proven, documented, low invention risk) and is **near-absent in patient health** — so the *application* is the innovation, not the technology.

---

## 3. Intelligent action & due-date extraction from medical text

**How tools do it today.** AI scribes capture the consult and emit a patient-facing recap: **Abridge** produces a *Patient Visit Summary* with plan + instructions at an **8th-grade reading level**, drawing on EHR context and a "predicted problems" section [[Abridge support, 2026](https://support.abridge.com/hc/en-us/articles/30235136497811-View-a-Patient-Visit-Summary), T2; [DeepCura, 2026](https://www.deepcura.com/resources/abridge-ai-review), T3]. **Nabla** auto-generates **patient instructions / post-visit recap** and runs a **context-aware agent that drafts a patient summary before the visit** [[Nabla, 2026](https://help.nabla.com/en/articles/769346), T2; [Fierce, 2026](https://www.fiercehealthcare.com/ai-and-machine-learning/ai-scribes-generate-better-documentation-more-patient-context-study), T2]. **Crucially, these stop at prose** — they produce a *readable summary*, not a set of **structured, dated, saveable task objects the patient owns**. That gap is Prototype A's core innovation.

**The extraction itself — feasibility and accuracy.** On **clean, single-field** tasks, LLMs do well: GPT-4 extracted **cognitive-exam dates and scores with high accuracy**, beating Llama-2 [[PMC, 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10888985/), T1]. But on **messy, longitudinal notes** the picture is worse:
- Columbia/JAMA Network Open: across **54,569 ED records**, GPT-4 **could not reliably reproduce** even a simple string-search extraction; the authors conclude AI **"can not yet reliably read and extract"** clinical-note information [[ScienceDaily/Columbia, 2024](https://www.sciencedaily.com/releases/2024/08/240819130535.htm), T1, high]. **US→EU FLAG:** English ED notes; transfer to Dutch/EU records is unvalidated.
- Temporal extraction is the hard part: under naive prompting, LLMs **pull non-relevant meds/procedures and mis-handle irregular time expressions** ("in two weeks", "next month"); **reasoning/"thinking" modes and ontology-grounded systems** (e.g. CLINES, which extracts explicit dates from local context and falls back to admission/discharge metadata when vague) materially cut false positives [[medRxiv CLINES, 2025](https://www.medrxiv.org/content/10.64898/2025.12.01.25341355v1.full.pdf), T1; [arXiv ChemoTimelines, 2025](https://arxiv.org/pdf/2512.04518), T1].

**Implication for "blood test in two weeks, said last week → due in ~1 week":** relative-date resolution requires a **reliable anchor** (the appointment date, which ditto *has*) plus reasoning. It is feasible — but **safety-fragile**. Design rules: (1) anchor every relative date to a known event timestamp; (2) surface the **computed date as a draft the patient confirms/edits**, never silently; (3) show the **source snippet** ("from your visit on 9 Jun: 'blood test in two weeks'") so the extraction is auditable; (4) **degrade to text** ("a follow-up was mentioned — when is it due?") rather than fabricate a date when confidence is low. This mirrors the refuse-when-unsure discipline of M17 #8.

---

## 4. Success cases + mistakes to avoid

**What has worked:**
- **Cited, trusted answers create durable demand** — OpenEvidence reached **>40% of US physicians at a ~$12B valuation** purely on grounded, cited clinical answers `[M11]`. The appetite for *verifiable* answers is proven; the unmet half is *patient-grade, EU, record-aware*.
- **Structured action extraction is a loved feature in adjacent tools** — Granola flags "I'll send that by Friday" as a task with **owner + deadline**; Notion AI ties action items to projects [[Granola, 2026](https://www.granola.ai/blog/meeting-action-items-ai-extraction), T3; [Notion, 2026](https://www.notion.com/compare-against/notion-vs-granola), T3].
- **Adjacent panel + persistence** (Artifacts) and **plain-language card feeds** (Cleo/Monzo) are validated consumer UX `[M16]`.

**Failure modes to avoid:**
- **Hallucinated citations / weak sources** — Google AI Overviews' health citations skewed to **YouTube (~4.4%) vs journals (~0.48%)**, only ~34% from sources with clinical oversight `[M11]` [T3]; Google **pulled AI Overviews from some medical queries (Jan 2026)** under misinformation scrutiny `[M11]`. Cite **clinician-authored EU sources** (Thuisarts.nl, Apotheek.nl, guidelines) and make every cite a clickable, verifiable resource card.
- **Unsafe / over-confident answers** — **5–13% of unguarded LLM patient answers were "unsafe"** (npj 2026) `[M11]`. Mitigate with no-advice framing + refuse-when-unsure + escalation cues.
- **Over- vs under-refusal** — refusing everything kills utility; answering everything is a safety event. Calibrate per the "clarify, don't advise" boundary.
- **Fabricated due dates** — see §3; the Columbia finding is the cautionary headline.
- **Regulatory trap** — drifting from "explain" to "recommend" can flip the product into **high-risk MDAI / SaMD** under the EU AI Act + MDR (high-risk requirements bite for new SaMD from **Aug 2026**) [[MedDeviceGuide, 2026](https://meddeviceguide.com/blog/eu-ai-act-medical-devices-compliance-guide), T2; [Tandem Health, 2026](https://tandemhealth.ai/resources/knowledge/eu-ai-act-explained-what-healthcare-organisations-need-to-know), T2]. Patients must be **clearly told they're talking to AI** (transparency duty). Babylon's ad-funnel + diagnostic-chatbot model is the business cautionary tale `[M16]`.

---

## 5. Adjacent / non-health transferable patterns

- **Cleo / Monzo — conversational coach over your own complex data.** A **witty/warm persona** renders plain-language cards + nudges over financial complexity `[M16, S3]`. Borrow: the persona-led, card-based plain-language read of the patient's medical complexity. Avoid: persona that over-promises or jokes about high-stakes content.
- **Granola / Reflect / Notion — task extraction from natural language.** Identify commitments and render them as **owner + deadline objects**, integrable downstream (Zapier → Notion) [[Granola, 2026](https://www.granola.ai/blog/meeting-action-items-ai-extraction), T3; [Atomic Object, 2026](https://spin.atomicobject.com/zapier-action-items/), T3]. Borrow: the **confirmable structured-task object** as the unit, not prose. Avoid: silent extraction with no review — fine for "email Bob", unacceptable for "blood test".
- **Claude Artifacts / Canvas — chat + durable, editable artifact.** Borrow: tap → detail panel → Save/edit; persistence so a saved task survives the conversation. Avoid: over-rendering; ensure graceful text fallback.
- **Spotify Wrapped / Duolingo streaks** (from `M16/M17`) — periodic personal-data narrative + gentle habit scaffold; adopt the *frame*, reward = clarity/agency not points.

---

## Implications for the Prototype A spec

1. **Adopt the rendering tech, innovate the application.** Build the task-pill / resource-card layer on a proven generative-UI stack (AI SDK-style tool-call → component, streaming, error states). The novelty is *health context*, not the framework — don't over-invest invention here.
2. **Make the white space the moat: ground in the patient's OWN record.** Perplexity/Comet are EU-available and cited but only **web/page-context-aware**; ditto's edge is answering over the user's **longitudinal appointment record** — a context no open-web engine has. Lead with "what did *my* doctor say?" not "what is hypertension?".
3. **Treat the task pill as the hero, not the chat.** The differentiated, near-absent-in-health element is the **structured, dated, saveable action object**. Spec it as a first-class object (source snippet, computed due date, status, save-to-home), borrowing Granola's owner+deadline rigor.
4. **Anchor + confirm every extracted date — never silent.** Resolve relative dates ("in two weeks") against the known appointment timestamp; surface the result as an **editable draft with its source snippet**; degrade to a question when confidence is low (Columbia/JAMA finding).
5. **Safety as differentiator: cite clinician-grade EU sources + refuse-when-unsure.** Every citation is a clickable, verifiable resource card from clinician-authored EU sources (Thuisarts.nl, Apotheek.nl, guidelines) — explicitly *not* the YouTube-skewed open web. Bake the 5–13%-unsafe finding into eval gates.
6. **Hold the "explain, not advise" line — it's also the cheap regulatory lane.** Keep the product in **limited-risk transparency** territory: clarify/explain, no diagnosis or recommendation, always disclose it's AI. This avoids high-risk MDAI/SaMD obligations biting from Aug 2026 — design the boundary now.
7. **Borrow the persona + card feed from Cleo/Monzo, the panel from Artifacts.** Warm, plain-language coach tone; chat for intent, panel for the durable artifact; persistence so saved tasks/cards outlive the conversation.
8. **Avoid:** over-rendering every reply into widgets; false-affordance controls; hallucinated/weak citations; fabricated dates; and any drift from "explain" to "recommend."

---

## Sources

### T1 — peer-reviewed / official company / regulator
- OpenAI — *Introducing ChatGPT Health* (2026): https://openai.com/index/introducing-chatgpt-health/
- Vercel — *Introducing AI SDK 3.0 with Generative UI* (2024): https://vercel.com/blog/ai-sdk-3-generative-ui
- Vercel AI SDK docs — *Generative User Interfaces* (2026): https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces
- PMC — *Evaluating LLMs in Extracting Cognitive Exam Dates and Scores* (2024): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10888985/
- ScienceDaily / Columbia (JAMA Network Open) — *Generative AI can not yet reliably read/extract from clinical notes* (2024): https://www.sciencedaily.com/releases/2024/08/240819130535.htm
- medRxiv — *CLINES: Clinical LLM Information Extraction & Structuring Agent* (2025): https://www.medrxiv.org/content/10.64898/2025.12.01.25341355v1.full.pdf
- arXiv — *UW-BioNLP at ChemoTimelines 2025: chemotherapy timeline extraction* (2025): https://arxiv.org/pdf/2512.04518
- *Carried from corpus `[M11]`:* npj Digital Medicine 2026 (5–13% unsafe); JAMA Network Open 2024 (Goh, GPT-4 ~92%); OpenEvidence $12B/Series D.

### T2 — reputable press
- Medical Economics — *OpenAI launches ChatGPT Health, linking patient portals* (2026): https://www.medicaleconomics.com/view/openai-launches-chatgpt-health-directly-linking-patient-portals-to-the-ai-chatbot
- FierceHealthcare — *OpenAI launches ChatGPT Health* (2026): https://www.fiercehealthcare.com/ai-and-machine-learning/openai-launches-chatgpt-health-connect-data-health-apps-medical-records
- FierceHealthcare — *AI scribe quality jumps with more patient context* (2026): https://www.fiercehealthcare.com/ai-and-machine-learning/ai-scribes-generate-better-documentation-more-patient-context-study
- Harvard / TagTeam — *ChatGPT Health connects records to an AI that makes things up* (2026): https://tagteam.harvard.edu/hub_feeds/3382/feed_items/17173992
- Abridge Support — *View a Patient Visit Summary* (2026): https://support.abridge.com/hc/en-us/articles/30235136497811-View-a-Patient-Visit-Summary
- Nabla — *Patient instructions* (2026): https://help.nabla.com/en/articles/769346
- Wikipedia — *Comet (browser)* (2026): https://en.wikipedia.org/wiki/Comet_(browser)
- Tandem Health — *EU AI Act explained for healthcare* (2026): https://tandemhealth.ai/resources/knowledge/eu-ai-act-explained-what-healthcare-organisations-need-to-know
- MedDeviceGuide — *EU AI Act for Medical Devices compliance guide* (2026): https://meddeviceguide.com/blog/eu-ai-act-medical-devices-compliance-guide

### T3 — blog / vendor / SEO (FLAGGED — use with caution)
- prompt-kit — *Vercel AI SDK UI components* (2026): https://www.prompt-kit.com/vercel-ai-sdk
- Albato — *How to use Claude Artifacts* (2026): https://albato.com/blog/publications/how-to-use-claude-artifacts-guide
- QWE — *Claude Artifacts interactive content* (2026): https://www.qwe.edu.pl/tutorial/claude-artifacts-interactive-content-tutorial/
- XsOne — *ChatGPT Canvas vs Claude Artifacts* (2026): https://xsoneconsultants.com/blog/chatgpt-canvas-vs-claude-artifacts/
- Glass Health — *Features* (2026): https://glass.health/features
- Beginners in AI — *What's New in Perplexity 2026 (Comet)* (2026): https://beginnersinai.org/whats-new-perplexity-2026/
- Granola — *Meeting action items: how AI extracts commitments* (2026): https://www.granola.ai/blog/meeting-action-items-ai-extraction
- Notion — *Notion vs Granola* (2026): https://www.notion.com/compare-against/notion-vs-granola
- Atomic Object — *Track action items from Granola via Zapier* (2026): https://spin.atomicobject.com/zapier-action-items/
- DeepCura — *Abridge AI Review* (2026): https://www.deepcura.com/resources/abridge-ai-review
- *Carried from corpus `[M11, M16]`:* BrightEdge/ALM AI Overview citation-quality stats (YouTube ~4.4% vs journals ~0.48%).

*Access date for all live URLs: 2026-06-16. US→EU flags apply to ChatGPT Health/b.well (US records), the Columbia ED-notes study (English notes), K Health/Buoy (US-only), and cognitive-exam extraction (English clinical text). EU-anchored comparables: Ada (DE), Nabla (FR), Thuisarts.nl/Apotheek.nl (NL) grounding sources, and the EU AI Act/MDR regime.*
