# Prototype B — Voice-First "ditto today" Daily/Weekly Note · Research

**Prepared for:** ditto.care — EU/NL patient-facing health-tech
**Author:** Product + market research analyst
**Date / access date:** 2026-06-16
**Scope:** Research the prototype against the voice/AI-native journaling, ambient-capture, and effortless-logging landscape. **Reuses** ditto corpus M10, M14, M15, M16, M17 (under `research/market-research/findings/`); adds net-new depth via web research (2025–2026).

> **Sourcing.** Inline `[Source, year](url)`. **T1** = peer-reviewed / analyst / company-verified · **T2** = reputable press · **T3** = blog / vendor / app-store self-report (FLAGGED). Confidence: high/med/low. 🇺🇸→🇪🇺 flags US-sample data whose EU transfer is uncertain. `[corpus]` = carried from ditto's vetted M-series; not re-researched. *unconfirmed* where unsourced.

---

## Key takeaways

- **VERDICT — voice: intelligent vs input-only.** The market splits into two camps and the prototype straddles them. **Input-only/transcription tools** (Wispr Flow, Superwhisper, AudioPen, Otter, Granola, Limitless/Bee) are winning commercially right now — Wispr Flow is at ~$10M ARR, ~40% MoM growth, in talks at a ~$2B valuation ([TechCrunch, 2025](https://techcrunch.com/2025/11/20/as-its-voice-dectation-app-takes-off-wispr-secures-25m-from-notable-capital/); [GetLatka, 2025](https://getlatka.com/companies/wisprflow.ai); T2/T3, med). **Intelligent tools** (Rosebud, Mindsera, Sonia, Ebb, Wysa) *steer, reflect and connect dots* but carry the safety/regulatory load (M14). **Prototype B's defensible position is "effortless input on the surface, intelligence underneath"** — the same conclusion M17 reached for mechanism #10: adopt-as-is on the voice *interface*, innovate on *what it understands and reflects back*.
- **The single most important design decision is to make the ramble feel like input, not therapy.** The "abstract the interface away, just ramble" framing is exactly the **AudioPen/Granola** pattern (you talk, the machine structures) — and it sidesteps the AI-therapist liability that killed Woebot and forced Ash out of the UK (M14). Keep the steering implicit (extraction, summary), not a conversational "AI therapist" that probes.
- **Live fact-extraction "pills" as you speak is genuinely novel for journaling but technically proven elsewhere.** Real-time NER over streaming audio is mature in call-center/agent-assist contexts ([AssemblyAI, 2026](https://www.assemblyai.com/blog/real-time-entity-extraction-from-audio); T3). No consumer journaling app ships live entity pills today — this is real white space — but the **distraction risk is the core UX hazard**: extraction must stay in peripheral vision, never interrupt the speaker.
- **Effortless capture at zero energy is ditto's whole thesis and the literature is unambiguous:** the manual-logging effort-tax drives ~43% pooled dropout in disease-app trials and ~70% abandonment within 100 days ([JMIR, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/); [JMIR, 2024](https://www.jmir.org/2024/1/e56897); T1, high) [corpus M15/M17]. Voice is the strongest known antidote: ~3× faster than typing, ~20% fewer errors, with the **largest gain among older adults** ([arXiv 2111.03756, 2021](https://arxiv.org/pdf/2111.03756); T1, med) [corpus M17].
- **Health-term STT accuracy is a real, recently-narrowed risk.** Best-in-class medical STT now hits ~93% real-world accuracy / ~7% WER, ~4% on medical keywords ([Speechmatics, 2025](https://www.speechmatics.com/company/articles-and-news/speechmatics-sets-record-in-medical-speech-to-text-with-93-percent-accuracy); T2 vendor, med) — but drug names and evolving terms remain the failure point, and **errors on a medication name are a safety event, not a typo** (M17 #10).
- **The 2025–26 mechanism shift is "ambient/passive capture + retroactive structuring."** Limitless and Bee (both acquired — Meta and Amazon respectively, late 2025) proved demand for always-on capture but hit a privacy wall ([UMEVO, 2026](https://www.umevo.ai/blogs/ume-all-posts/limitless-pendant-vs-bee-ai-which-always-on-wearable-recorder-is-best); T3). The durable, less-creepy pattern is **user-initiated capture, AI-structured after** (Granola, AudioPen) — which is exactly Prototype B's "tap start → ramble → 'here's what we understood'."
- **Product-leader read (Lenny's/Eyal/calm-tech):** the prototype's instincts are right — minimize the *action* (Eyal: friction kills the trigger→action loop), give an *immediate variable reward* (the live pills + calm summary = felt progress), and respect *calm-technology* principles (information in the periphery). The biggest avoidable mistakes are **over-prompting, nagging notifications, surveillance-creep, and gamification that reinforces a "sick" identity** (M17 #3, #7).

---

## 1. Intelligent vs input-only — the core classification

The founder's question — *is the voice assistant intelligent or just faster input?* — is the axis the whole market sorts on. The distinction: **input-only** captures and cleans your words (transcription + light formatting); **intelligent** *steers* the session (prompts, probes), *structures* meaning (extraction, themes), or *reflects* (connects dots, surfaces patterns over time). Most products do some of each; what matters is the **dominant mode**.

| Product | Category | Dominant mode | What it actually does | Health-safety load |
|---|---|---|---|---|
| **Wispr Flow** 🇺🇸 | Voice dictation | **Input-only** | Speech → polished text in any app; infers context from screen; ~$10M ARR, ~$2B-talks ([TechCrunch, 2025](https://techcrunch.com/2025/11/20/as-its-voice-dectation-app-takes-off-wispr-secures-25m-from-notable-capital/), T2) | None — pure I/O |
| **Superwhisper** 🇺🇸 | Voice dictation | **Input-only** | On-device + cloud STT, custom "modes," AI formatting, 100+ languages ([superwhisper.com](https://superwhisper.com/), T3) | None |
| **AudioPen** 🇮🇳/global | Voice note → text | **Input-only (+ light structure)** | Rewrites *rambling* voice into polished structured text; cuts filler ([audiopen.ai](https://www.audiopen.ai/), T3) | None — closest UX analog to the ramble |
| **Otter** 🇺🇸 | Meeting transcription | **Input-only (+ summary)** | Live transcript + post-hoc summary/action items | Low |
| **Granola** 🇺🇸 | Meeting notes | **Input-only (+ structuring)** | You write skeleton notes; AI fills detail from transcript; no bot, on-device audio, deletes audio after ([docs.granola.ai, 2025](https://docs.granola.ai/help-center/taking-notes/transcription), T3) | Low — privacy-forward model |
| **Limitless / Bee** 🇺🇸 | Ambient wearable | **Input-only (ambient)** | Always-on capture → retroactive summaries; both acquired (Meta/Amazon late 2025) ([UMEVO, 2026](https://www.umevo.ai/blogs/ume-all-posts/limitless-pendant-vs-bee-ai-which-always-on-wearable-recorder-is-best), T3) | **High — surveillance/consent** |
| **Reflectly** 🇩🇰 | Mood journaling | **Lightly intelligent** | Structured CBT/positive-psych prompts; surface mood tracking ([reflection.app, 2026](https://www.reflection.app/best-journaling-apps-compared/mindsera-vs-reflectly), T3) | Low |
| **Daylio / How We Feel** | Mood logging | **Input-only (one-tap)** | Near-zero-effort tap logging [corpus M10] | Low |
| **Stoic** 🇩🇪 | Journaling + ritual | **Lightly intelligent** | Guided AM/PM prompts + AI pattern insights [corpus M10] | Low |
| **Rosebud** 🇺🇸 | AI journaling | **Intelligent (reflect/steer)** | Chat-based; *learns from entries*, gives personalized prompts ("smallest step to reduce overwhelm"), mood patterns, weekly insights, "Wrapped" ([rosebud.app, 2025](https://www.rosebud.app/blog/best-journaling-app-2025-review), T3) | Med — reflective, not clinical |
| **Mindsera** 🇪🇺 | AI journaling | **Intelligent (steer/reframe)** | Detects cognitive biases, applies *mental models* (inversion, first-principles), evaluates decision quality ([reflection.app, 2026](https://www.reflection.app/blog/ai-journaling-apps-compared), T3) | Med |
| **Youper** 🇺🇸 | AI emotional health | **Intelligent (CBT)** | AI mood chat + CBT; RCT-evidenced [corpus M14] | Med-high |
| **Wysa** 🇮🇳/🇬🇧 | AI MH companion | **Intelligent (CBT+escalation)** | CBT chat + human escalation; FDA Breakthrough; NHS [corpus M14] | High |
| **Sonia** 🇺🇸 | AI voice therapy | **Highly intelligent (steer)** | Full CBT session as a *finite state machine* traversed by an LLM (mood check → agenda → restructuring); "brings up things you said sessions ago" ([Product Hunt](https://www.producthunt.com/products/sonia-ai-therapy); [App Store](https://apps.apple.com/us/app/sonia-ai-wellbeing-coach/id6472111765), T3) | **High — therapy claim** |
| **Ebb (Headspace)** 🇺🇸 | AI companion (voice) | **Intelligent (reflect, guard-railed)** | Motivational-interviewing, voice mode + memory; explicitly *"not a therapist"*; 7M+ messages [corpus M10/M14] | Med — deliberately bounded |
| **Clare&Me** 🇩🇪 | AI voice MH (EU) | **Intelligent** | Voice + text companion; building a clinical LLM [corpus M14] | High |

**Where Prototype B sits:** the *ramble → live pills → calm "here's what we understood" summary* is **input-first with a structuring layer** — the AudioPen/Granola mode, not the Sonia/Rosebud conversational-steering mode. That is the right call. The intelligent products that *steer conversationally* (Sonia "conducts CBT sessions," Rosebud chats back) are precisely the ones carrying lawsuit/regulatory exposure (M14: Woebot shutdown, Ash UK exit, APA advisory, EU AI Act transparency + MDR). Prototype B's intelligence should live in **extraction and reflection (pills, trends, summary), not in a probing back-and-forth.** This keeps it on the right side of the M14 line: *support and comprehension between human care, not a substitute for it.*

---

## 2. Live transcription + live fact-extraction UX

**Live transcription** (top half, fading in, scrolling up) is now table-stakes and well-solved: Granola, Otter, Wispr and Superwhisper all stream transcript with sub-second perceptible delay, the key satisfaction requirement ([Gladia, 2025](https://www.gladia.io/blog/real-time-transcription-powered-by-whisper-asr); T3). Granola's privacy posture is the model to copy — **on-device audio, transcribe, then delete the audio**, no stored recording ([docs.granola.ai, 2025](https://docs.granola.ai/help-center/taking-notes/transcription); T3) — directly relevant under GDPR.

**Live fact-extraction "pills" as you speak is the novel bet.** Technically, real-time Named Entity Recognition over streaming audio is mature in agent-assist/call-center contexts — pulling structured entities (names, meds, dates) from live speech "without waiting for the conversation to end" ([AssemblyAI, 2026](https://www.assemblyai.com/blog/real-time-entity-extraction-from-audio); [Google Agent Assist](https://docs.cloud.google.com/agent-assist/docs/entity-extract); T3). **But no consumer journaling app surfaces live entity pills to the user mid-speech** — that is genuine white space and the prototype's most differentiated feature.

The **failure mode is distraction.** The UX research literature is thin on this specific pattern (the searches surfaced technical NER, not cognitive-load studies — *unconfirmed* on hard numbers), but the principle from calm-technology and the prototype's own instinct converge: **extraction belongs in the periphery, never the focus.** Design implications:
- Pills should **accrete quietly on the bottom half** (white/light-grey, category only by a small colored icon, as specced) so a glance confirms "it's listening and understanding" without pulling attention from the ramble.
- **Never animate a pill in a way that competes with the scrolling transcript** above it; no sounds, no haptics mid-ramble.
- **Defer correction.** Tapping a pill → bottom sheet is correct, but invite edits at the *summary* stage ("here's what we understood"), not mid-flow — interrupting to fix a misheard drug name breaks the zero-energy spell.
- **Show confidence implicitly.** A misheard medication is a safety event (§below). Low-confidence extractions should be visibly tentative (e.g., lighter, "did you mean…?" only at summary), never silently registered.

**STT accuracy / latency / privacy for health terms.** Best-in-class medical STT reached **~93% real-world accuracy, ~7% WER, ~4% medical-keyword error rate** in 2025, with German + Nordic medical models rolling out — relevant for EU/NL ([Speechmatics, 2025](https://www.speechmatics.com/company/articles-and-news/speechmatics-sets-record-in-medical-speech-to-text-with-93-percent-accuracy); [Speechmatics Nordic/German](https://www.speechmatics.com/company/articles-and-news/speechmatics-sets-new-standard-for-real-time-medical-transcription-with-german-and-nordic); T2 vendor, med). The persistent failure point is **drug names and fast-evolving clinical vocabulary** — "clinical vocabulary evolves faster than model updates" ([JAMIA Open, 2025](https://academic.oup.com/jamiaopen/article/8/6/ooaf147/8327118); [arXiv United-MedASR, 2024](https://arxiv.org/html/2412.00055v1); T1). Mitigations: a **medication/condition lexicon bias** seeded from the user's own appointment record (ditto already holds this — a real edge), Dutch + English handling, and **always confirm meds/symptoms at the summary stage before any "register it" action.**

---

## 3. Effortless capture at zero energy

This is ditto's thesis and the prototype's reason to exist. The evidence (corpus M15/M17):
- **The effort tax is the killer:** manual disease-app logging shows ~43% pooled dropout ([JMIR, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/); T1, high); ~70% abandon within 100 days, ~71% within 90 ([JMIR, 2024](https://www.jmir.org/2024/1/e56897); [Alchemer, 2022](https://www.alchemer.com/resources/blog/healthcare-apps-mobile-customer-engagement-benchmarks/); T1/T3) [corpus].
- **What beats it:** passive capture (Oura/Whoop, >50–80% retention) or near-zero-effort logging (Daylio one-tap) [corpus M10]. Voice is the most accessible near-zero-effort mode: **~3× faster than typing, ~20% fewer errors, largest gain in older adults** ([arXiv 2111.03756, 2021](https://arxiv.org/pdf/2111.03756); [PMC7783870, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7783870/); T1, med) [corpus M17 #10] — voice is *the* eye-free, hands-free, low-dexterity, low-literacy modality, which matters acutely for sick, fatigued, and older patients.
- **What makes capture stick for low-energy users:** (1) **one action** (tap → talk), no form, no fields; (2) **immediate felt reward** — the live pills are proof the effort "counted," the affective payoff of *being understood* (M17 #6 reframed as reassurance/clarity); (3) **the user decides what happens next** — register, share, view trend, or nothing — preserving agency, which the prototype already does well.

**The risk:** AudioPen proves rambling-to-text works for *able, motivated knowledge workers*. For *sick/fatigued* users the bar is higher — sessions must tolerate long pauses, trailing off, and "I don't know what to say." The home-screen card's **nudge hinting at the last entry** ("yesterday you mentioned the oncologist visit — how are you feeling about it?") is the right scaffold: it lowers the cold-start cost without demanding a structured answer. Keep it a *gentle hint*, not a prompt that must be answered (over-prompting is a documented churn driver, §5).

---

## 4. Mechanisms that emerged in 2025–2026

- **Voice-to-text crossed from utility to platform.** Wispr Flow's trajectory ($30M Series A June 2025 → $25M Series B Nov 2025 → ~$2B talks; ~40% MoM; users write ~72% of characters via Flow after six months) shows voice input is becoming a *default I/O layer*, not a niche ([TechCrunch, 2025](https://techcrunch.com/2025/11/20/as-its-voice-dectation-app-takes-off-wispr-secures-25m-from-notable-capital/); [GetLatka, 2025](https://getlatka.com/companies/wisprflow.ai); T2/T3, med). Implication: voice-first will feel normal to ditto users by launch — the prototype is well-timed.
- **Ambient/always-on capture peaked and hit a wall.** Limitless and Bee proved demand for passive life-logging but **both were acquired and effectively wound down in late 2025** (Meta acquired Limitless Dec 2025 and stopped hardware sales; Amazon acquired Bee Q3 2025) ([UMEVO, 2026](https://www.umevo.ai/blogs/ume-all-posts/limitless-pendant-vs-bee-ai-which-always-on-wearable-recorder-is-best); T3, med). The lesson for ditto: **always-listening is a privacy/consent minefield** (Limitless built a "Consent Mode" to pause for non-consenting voices and still got absorbed). **User-initiated, bounded capture ("tap start … say stop") is the durable, EU-safe pattern** — and is exactly Prototype B's model.
- **"Retroactive structuring" became the dominant note paradigm.** Granola's "you write the skeleton, AI fills detail" and AudioPen's "ramble → polished" both ship the structuring *after* capture, not via mid-conversation steering. Prototype B's "ramble → 'here's what we understood'" is squarely in this 2025 paradigm.
- **AI journaling specialized by *reflection philosophy*.** Rosebud (growth/pattern-reflection), Mindsera (cognitive frameworks), Stoic (philosophy), Reflectly (mood) now differentiate on *how the AI reflects*, and most added a **"Wrapped"-style annual narrative** (Rosebud Wrapped 2025) ([rosebud.app, 2025](https://www.rosebud.app/blog/best-journaling-app-2025-review); T3) — corroborating M16's "Health Wrapped" Adopt recommendation.
- **Mental-health AI tightened, not loosened.** 2025–26 brought the APA advisory, US state bans, Woebot's shutdown, Ash's UK exit, and EU AI Act enforcement (M14). The market moved *away* from autonomous AI-therapist steering — reinforcing the prototype's input-first, non-clinical-claim stance.

---

## 5. What a Lenny's-Newsletter product leader would say

**Make the action trivially small (Nir Eyal, Hook Model).** Eyal's core lesson: in the trigger→action→reward→investment loop, **friction on the *action* is what breaks the habit** — make it as simple as possible ([nirandfar.com](https://www.nirandfar.com/hooked/); [Insight7, 2025](https://insight7.io/4-product-lessons-on-the-hook-model-from-hooked-by-nir-eyal/); T3). Prototype B's "tap card → just talk" is a near-zero-friction action. The **trigger** should become *internal* over time (the card's last-entry nudge is the external scaffold that builds the internal "I jot to ditto" habit). The **variable reward** is the live pills + the personalized summary (varies every day = anticipatory, per M17 #6). The **investment** is the accreting "today's notes" timeline — each entry makes tomorrow's nudge smarter (compounding data, M17 #5).

**Calm/ambient design (Weiser/Brown calm-technology).** The prototype's "abstract the interface away," peripheral pills, and "subtle" everything are textbook calm-tech: **information lives in the periphery and moves to the center only when the user wants it.** Hold that line ruthlessly — the moment extraction demands attention mid-ramble, it stops being calm.

**Onboarding & first-run (retention leaders).** The first session must deliver the "aha" — *I rambled and it understood me* — in under a minute, no setup. Seed the first nudge from the user's existing appointment summary so the very first card already feels personal.

**Mistakes to avoid (the explicit list):**
- **Nagging notifications.** Generic scheduled reminders are the #1 backfire — users mute, then churn (M17 #7). Nudges must be *contextual* (tied to a real event — a visit, a refill) and *skippable*, never daily-alarm guilt.
- **Over-prompting.** Don't turn the ramble into an interrogation. The hint suggests; it never *requires* an answer. Sonia/Rosebud's conversational probing is a different (riskier) product.
- **Surveillance-creep.** No always-listening, no background capture. Bounded "start/stop," visible recording state, audio deleted after transcription (Granola model). Critical under GDPR and for trust with sick users.
- **Gamification that reinforces a "sick" identity.** M17 #3 is explicit: streaks/badges in a health context can entrench "I'm a sick person." Frame any continuity as *agency* ("you've stayed on top of things"), warmth, and relationship — never points, never a broken-streak penalty that punishes a bad health day.
- **Privacy backlash / over-claiming.** Never imply diagnosis or therapy. The summary is "here's what we understood," not "here's what's wrong with you." Keep the AI-disclosure explicit (EU AI Act transparency, M14).

---

## 6. Adjacent fields — transferable mechanics and mistakes

- **Meditation / calm (Calm, Headspace, Ebb).** *Adopt:* the daily-ritual trigger and audio-first calm. *Avoid:* content-only retention — it decays (Calm/Headspace subscriber erosion, M10). The reward must be *personalized and changing*, not a static library. Ebb's voice-mode + memory + explicit "not a therapist" guardrail is the closest health-companion analog to copy.
- **Productivity capture (Granola, AudioPen, Notion).** *Adopt:* retroactive structuring (you talk, AI organizes), privacy-forward audio handling, and the "user owns an editable living document" metaphor (M16 Notion row) — the "today's notes" card *is* this. *Avoid:* feature-bloat that re-introduces the effort tax.
- **Fintech check-ins (Cleo, Monzo).** *Innovate (closest tonal analog, per M16):* a warm, plain-language persona translating complex data (clinical → human) and a calm, plain-language *feed* of what happened. *Avoid:* gimmicky persona that trivializes serious moments — tone must flex down for an oncology day.
- **BeReal-style daily prompt.** *Adopt:* the **single, well-timed, once-a-day prompt** as the habit anchor (M16) — far healthier than infinite re-engagement. *Avoid:* time-pressure/FOMO mechanics; a sick user can't be punished for missing the window.
- **Spotify Wrapped / Strava year-in-review.** *Adopt:* the periodic shareable "your health story" narrative (Rosebud, Stoic and others already ship "Wrapped"; M16 flags it Adopt) — turns the accreting timeline into an emotional, shareable payoff.

---

## 7. Streaming entity extraction — how to build the "facts as you speak" feel (net-new, 2026-06-17)

**The founder's hypothesis — "a streaming LLM that takes words as they come and emits extracted facts as you speak" — is real, proven, and buildable on ditto's stack today.** It is not a research bet; it's an engineering pattern with production precedent. Two architectures exist; the right answer for v0 is a hybrid.

**(a) True partial-object streaming — the "magical" version.** Modern LLM tooling streams *structured* output incrementally: the model emits JSON token-by-token and the client parses the partial object, rendering each fact the instant its fields complete. This is shipping in mainstream libraries:
- **Vercel AI SDK `streamObject`** exposes `partialObjectStream`, and **`Output.array` / `elementStream`** streams array elements *one at a time* — "stream structured objects by complete object rather than by token… solves layout shift" ([AI SDK docs, 2025](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-object); [Vercel — Array Output Mode](https://vercel.com/templates/ai/array-output-mode); T1 official). That is exactly "a pill pops the moment a fact is complete."
- **Instructor** (`create_partial` / `Partial[Model]`) gives "field-level streaming… incremental snapshots of the current state of the response model that are immediately usable… for rendering UI components" — ~3M downloads/mo, supports Gemini/Vertex ([Instructor — partial streaming](https://python.useinstructor.com/concepts/partial/); [Instructor — Vertex AI guide](https://python.useinstructor.com/integrations/vertex/); T1 official/T3).
- **Gemini supports streamed function calling** — "stream partial function call arguments to improve user experience during tool use" — plus structured output / `responseSchema`, context caching, and "thinking" steps ([Gemini 2.5 Flash, Vertex AI docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash); T1).

**(b) Debounced re-extraction — the robust version.** Re-run extraction on the transcript-so-far on a throttle (every utterance, or ~1.5–2 s of new text + a brief pause), diff against current pills, add/update. Simpler, dead-stable, trivially cheap. This is the call-center agent-assist pattern: "for each end-of-turn event, pipe the finalized transcript into the LLM… for suggestions / next-best-action" ([AssemblyAI — agent-assist guide, 2026](https://www.assemblyai.com/blog/how-does-real-time-agent-assist-work-an-implementation-guide); T3).

**The decisive insight is about flicker, not speed.** The hard problem isn't latency — it's pills jittering or duplicating as the STT *revises* earlier words. The production answer: **extract only off finalized/immutable transcript, never off volatile partials.** AssemblyAI's Universal-Streaming "delivers immutable transcripts with ~300 ms P50 latency… so downstream services start processing immediately without waiting for transcript revisions," and explicitly frames immutability as the fix for "the flicker problem" ([AssemblyAI — agent-assist guide, 2026](https://www.assemblyai.com/blog/how-does-real-time-agent-assist-work-an-implementation-guide); [AssemblyAI — real-time entity extraction, 2026](https://www.assemblyai.com/blog/real-time-entity-extraction-from-audio); T3). So: show the live partial transcript (dimmed), but **only commit a pill from a finalized segment.**

**Recommended v0 architecture (hybrid — magical feel, stable output):**
1. **Resonate streams the transcript.** Show partial words live; render not-yet-final words *dimmed*, solid once finalized — the exact pattern Claude voice mode uses ("speech appears as you speak, dimmed until the transcript is finalized," [Claude Code voice, 2025](https://code.claude.com/docs/en/voice-dictation); T2). This alone makes capture feel alive with zero extraction cost.
2. **Fire extraction on each finalized utterance/segment** (end-of-utterance boundary, or ~1.5–2 s of new finalized text). Send the transcript delta + the running pill state to **Gemini 3.5 Flash** with the pill taxonomy as `responseSchema`, streaming the structured output so a pill can surface individually ((a) layered on top of (b)).
3. **Dedup with stable keys** (category + normalized value, e.g. `medication:ondansetron`). Update-in-place, never re-add. Because pills only ever come from *finalized* text, they don't jitter.
4. **Latency budget:** STT ~300 ms word emission; extraction round-trip target <1 s after an utterance finalizes (Flash TTFT + a few tokens; the family generates "~2–3× the token rate of pro-class models," [MindStudio — Gemini 3.5 Flash, 2026](https://www.mindstudio.ai/blog/what-is-gemini-3-5-flash-3); T3). The conversational "disruption threshold" is ~1 s — but pills are *peripheral*, so a ~1 s lag behind the voice is not just acceptable, it reads as calm rather than twitchy.
5. **Cost:** trivial. Gemini 2.5 Flash is ~$2.50 / 1M input, ~$1.25 / 1M output ([DataStudios — Gemini 2025 lineup](https://www.datastudios.org/post/google-gemini-all-models-available-2025-lineup-capabilities-and-context-limits); T3); 3.5 Flash is faster and cheaper. A 2-min ramble re-prompting the growing transcript per utterance is pennies; **context caching** on the stable transcript prefix cuts the repeated-prefix cost further ([Vertex AI docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash); T1).

**Why this is both magical and calm:** words stream dimmed→solid (felt responsiveness, no waiting); pills accrete only on committed facts (no flicker, no dupes); extraction deliberately trails the voice by ~1 s in the periphery (calm, not surveillance-twitchy). The "smart/magical/intelligent" feel comes from (a) partial-object streaming; the "trustworthy/calm" feel comes from (b) committing only finalized facts. Build both layers.

**Crisis detection runs as a separate, independent module — not a branch of the extraction prompt.** The 2025–26 research consensus: reframe crisis detection "from an accuracy-oriented prediction task toward an online, safety-oriented monitoring problem… with dedicated risk-detection modules operating independently of the conversational model," biased toward tolerating false positives to protect safety ([medRxiv — suicide/crisis-risk detection with LLMs, 2026](https://www.medrxiv.org/content/10.64898/2026.01.12.26343914.full.pdf); [Nature Sci Reports — chatbots detecting suicidal ideation, 2025](https://www.nature.com/articles/s41598-025-17242-4); T1). What counts for the hand-off is **tap-to-call quality, not the mere presence of a number**: the validated framework (MHACSAF) scores "tap-to-call functionality, correct routing, interface prominence" ([Frontiers — MH App Crisis Support Assessment Framework, 2026](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1814547/full); T1). For NL, route to **113 Zelfmoordpreventie** (self-harm) and **112** (medical emergency) with a one-tap call, calm copy, no clinical claim. Apps "are not equipped to manage crises alone… refer to external resources" ([PubMed — MH apps & crisis support, 2025](https://pubmed.ncbi.nlm.nih.gov/40836663/); T1) — so ditto's job is fast, gentle routing, never handling it conversationally.

---

## Implications for the Prototype B spec

- **ADOPT — input-first framing.** Position the ramble as *capture you're understood doing*, not a conversation with an AI. This is the AudioPen/Granola lane and it keeps ditto out of the AI-therapist regulatory blast radius (M14). The intelligence is in extraction + summary + trend, not in probing.
- **ADOPT — Granola's privacy model.** On-device transcription where possible, **delete audio after transcription**, visible recording state, explicit "tap stop." Essential for GDPR and for trust with vulnerable users; also the only durable answer to the surveillance-creep that sank Limitless/Bee.
- **INNOVATE — live extraction pills (the differentiator).** No journaling app ships this; it's white space. Keep pills strictly peripheral (white/grey, icon-only category), never interrupting, with edits invited at the summary stage. This is the prototype's signature — invest the UX care here.
- **INNOVATE — medication/symptom safety layer.** Seed STT with a lexicon from the user's own appointment record to fight drug-name errors; **confirm any med/symptom at the summary before "register it."** A misheard medication is a safety event, not a typo (M17 #10; [JAMIA Open, 2025](https://academic.oup.com/jamiaopen/article/8/6/ooaf147/8327118)).
- **INNOVATE — contextual, event-anchored nudges.** The last-entry hint and any reminders must be tied to real context (a visit, a refill — ditto holds this data), gentle and skippable. This is M17 #7's "innovate" — contextual beats scheduled, and it dodges the nagging-notification trap.
- **ADOPT — the "today's notes" timeline as a living, editable document** (Notion metaphor, M16) and add a periodic **"health Wrapped"** narrative — turns accreting entries into compounding data (M17 #5) and an emotional payoff (Rosebud/Spotify pattern).
- **AVOID — conversational AI-therapist steering, health-points gamification, always-listening, and any diagnosis/therapy claim.** Frame continuity as agency and warmth (M17 #3); summary is "here's what we understood," not a verdict.
- **WATCH — voice-to-text is becoming the default I/O layer** (Wispr's trajectory). Build to best-in-class STT/latency standards; the *interface* is fast becoming table-stakes, so ditto's durable edge is the **grounding + reflection over the user's own clinical record**, not the voice channel itself.

---

## Sources

### T1 — peer-reviewed / analyst / company-verified
- [JMIR — Attrition/dropout in app-based chronic-disease interventions (~43%), 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7556375/)
- [JMIR — When and Why Adults Abandon Mental Health Mobile Apps (~70%/100d), 2024](https://www.jmir.org/2024/1/e56897)
- [arXiv 2111.03756 — Voice assistants for older adults' healthcare (voice 3× faster, 20.4% fewer errors), 2021](https://arxiv.org/pdf/2111.03756)
- [PMC7783870 — Voice assistants & consumer-health access, low-income older adults, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7783870/)
- [JAMIA Open — Benchmarking STT robustness in noisy emergency medical dialogues, 2025](https://academic.oup.com/jamiaopen/article/8/6/ooaf147/8327118) · [PMC mirror](https://pmc.ncbi.nlm.nih.gov/articles/PMC12628192/)
- [arXiv — United-MedASR: high-precision medical STT via synthetic data + semantic correction, 2024](https://arxiv.org/html/2412.00055v1)

### T2 — reputable press / company filings
- [TechCrunch — Wispr secures $25M as voice dictation takes off, 2025](https://techcrunch.com/2025/11/20/as-its-voice-dectation-app-takes-off-wispr-secures-25m-from-notable-capital/)
- [PRNewswire — Wispr raises $25M to build voice OS, 2025](https://www.prnewswire.com/news-releases/wispr-raises-25m-to-build-its-voice-operating-system-302621858.html)
- [Speechmatics — record medical STT 93% accuracy, 2025](https://www.speechmatics.com/company/articles-and-news/speechmatics-sets-record-in-medical-speech-to-text-with-93-percent-accuracy)
- [Speechmatics — real-time medical transcription, German + Nordic rollout, 2025](https://www.speechmatics.com/company/articles-and-news/speechmatics-sets-new-standard-for-real-time-medical-transcription-with-german-and-nordic)

### T3 — blog / vendor / app-store self-report (FLAGGED — directional)
- [GetLatka — Wispr Flow revenue $10M ARR, 2025](https://getlatka.com/companies/wisprflow.ai)
- [AudioPen — voice to polished text](https://www.audiopen.ai/) · [App Store](https://apps.apple.com/us/app/audiopen/id6502638001)
- [Superwhisper — AI dictation](https://superwhisper.com/)
- [Granola — how transcription works (docs), 2025](https://docs.granola.ai/help-center/taking-notes/transcription) · [Granola](https://www.granola.ai/)
- [UMEVO — Limitless Pendant vs Bee AI always-on recorder, 2026](https://www.umevo.ai/blogs/ume-all-posts/limitless-pendant-vs-bee-ai-which-always-on-wearable-recorder-is-best)
- [Rosebud — best journaling app 2025 review](https://www.rosebud.app/blog/best-journaling-app-2025-review) · [Rosebud](https://www.rosebud.app/)
- [Reflection.app — AI journaling apps compared: Reflection vs Rosebud vs Mindsera, 2026](https://www.reflection.app/blog/ai-journaling-apps-compared) · [Mindsera vs Reflectly](https://www.reflection.app/best-journaling-apps-compared/mindsera-vs-reflectly)
- [Mindsera — AI journal for mental wellbeing](https://mindsera.com/)
- [Sonia — Product Hunt](https://www.producthunt.com/products/sonia-ai-therapy) · [App Store](https://apps.apple.com/us/app/sonia-ai-wellbeing-coach/id6472111765)
- [AssemblyAI — real-time entity extraction from audio, 2026](https://www.assemblyai.com/blog/real-time-entity-extraction-from-audio)
- [Google Cloud — real-time entity extraction (Agent Assist)](https://docs.cloud.google.com/agent-assist/docs/entity-extract)
- [Gladia — real-time transcription, 2025](https://www.gladia.io/blog/real-time-transcription-powered-by-whisper-asr)
- [Nir Eyal — Hooked](https://www.nirandfar.com/hooked/) · [Insight7 — 4 product lessons from the Hook Model](https://insight7.io/4-product-lessons-on-the-hook-model-from-hooked-by-nir-eyal/)

### Net-new 2026-06-17 — streaming entity extraction & crisis routing
- [AI SDK — `streamObject` / partial object stream (official docs)](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-object) · [Vercel — Array Output Mode](https://vercel.com/templates/ai/array-output-mode)
- [Instructor — partial / field-level streaming](https://python.useinstructor.com/concepts/partial/) · [Instructor — Vertex AI integration](https://python.useinstructor.com/integrations/vertex/)
- [Gemini 2.5 Flash — Vertex AI docs (streamed function calling, structured output, caching)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) · [MindStudio — Gemini 3.5 Flash, 2026](https://www.mindstudio.ai/blog/what-is-gemini-3-5-flash-3) · [DataStudios — Gemini 2025 lineup & pricing](https://www.datastudios.org/post/google-gemini-all-models-available-2025-lineup-capabilities-and-context-limits)
- [AssemblyAI — real-time agent-assist implementation guide (immutable transcripts, ~300ms, flicker fix), 2026](https://www.assemblyai.com/blog/how-does-real-time-agent-assist-work-an-implementation-guide) · [AssemblyAI — real-time entity extraction, 2026](https://www.assemblyai.com/blog/real-time-entity-extraction-from-audio)
- [Claude Code — voice dictation (streaming, dimmed-until-final), 2025](https://code.claude.com/docs/en/voice-dictation)
- [medRxiv — suicide/crisis-risk detection with LLMs in MH chatbots, 2026](https://www.medrxiv.org/content/10.64898/2026.01.12.26343914.full.pdf) · [Nature Scientific Reports — chatbots detecting/managing suicidal ideation, 2025](https://www.nature.com/articles/s41598-025-17242-4) · [Frontiers — MH App Crisis Support Assessment Framework (MHACSAF), 2026](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1814547/full) · [PubMed — MH apps & crisis support, 2025](https://pubmed.ncbi.nlm.nih.gov/40836663/)

### Reused from ditto corpus (not re-researched)
- [M10 — Consumer-App Deep-dives](../../research/market-research/findings/M10-consumer-app-deepdives.md) · [M14 — AI Mental Health & Therapy](../../research/market-research/findings/M14-ai-mental-health-therapy.md) · [M15 — Winners & Losers](../../research/market-research/findings/M15-winners-losers-why.md) · [M16 — Solution Catalogue](../../research/market-research/findings/M16-solution-catalogue.md) · [M17 — Table-Stakes Mechanisms](../../research/market-research/findings/M17-table-stakes-mechanisms.md)

*Access date for all live URLs: 2026-06-16. 🇺🇸→🇪🇺 flags apply to Wispr/Superwhisper/AudioPen/Granola/Limitless/Bee/Rosebud/Mindsera/Sonia (US-or-global, EU transfer of UX patterns likely but commercial/regulatory context differs). Speechmatics German+Nordic medical STT is the most directly EU-relevant accuracy datapoint. Distraction-cost of live extraction pills is unstudied in the literature surveyed — flagged as the key open UX question to prototype-test.*
