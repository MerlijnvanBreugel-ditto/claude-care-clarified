# Two-stage STT→extraction pipeline (not single-model Gemini-on-audio) for the prototype

**Status:** accepted (2026-06-17)

The voice daily note transcribes speech and extracts structured "pills." We considered a **single-model** path — stream audio straight to Gemini (native multimodal) and have it emit transcript + pills + affect in one pass — which is elegant and uniquely captures vocal affect. We rejected it for the prototype and chose a **two-stage** pipeline: **Reson8 streaming STT (WebSocket) → Gemini (3.5-flash minimal-thinking, model-agnostic behind a protocol) for extraction**, built entirely in the iOS repo, calling both services directly (no Ditto AI Core / Docker dependency).

## Why

- **Drug-name safety.** A dedicated STT can be biased to a medical lexicon; a generalist audio-LLM cannot, and a misheard medication is a safety event, not a typo.
- **Independent verification.** With two stages, the transcript is independent ground truth we can later verify pills against (grounding check, backlogged). A single model writing both the fact *and* its "source quote" can hallucinate both together — circular.
- **GDPR + transcript UX.** Two-stage keeps a path to on-device STT (audio never leaves the device) and gives the crisp dim→solid word-by-word transcript the spec relies on; the Live API is conversation-oriented and chunk-granular.

## Consequences

- Two cloud calls and a coordinator instead of one call; the `ExtractionClient` is model-agnostic so the model (and, later, the single-model experiment) is swappable.
- The single-model Gemini-on-audio approach is **not discarded** — it is backlogged as an A/B experiment behind the same `ExtractionClient` seam (it captures vocal affect the two-stage path cannot). See [prototype-spec.md](../../prototype-spec.md) §11 P3 and [technical-research.md](../../technical-research.md) §2–§3.
- Hard SLA: ≤2 s end-of-speech → pill, which forces element-level streaming of the extraction response and makes the *model name* subordinate to the measured latency.
