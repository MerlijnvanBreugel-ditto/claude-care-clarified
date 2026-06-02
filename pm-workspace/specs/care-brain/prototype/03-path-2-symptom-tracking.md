# 03 · Path 2 — Symptom Tracking via Voice

**Prereq**: `01-core-architecture.md`. Schemas in `05-data-schemas.md`.

**Purpose**: Implement a daily-active engagement surface. Patients check in via voice in 30 seconds. Symptoms get structured, logged to a time series, visualized, and pattern-detected. Results flow into the next appointment's prep briefing automatically.

---

## User story

Jan (74, multi-condition patient) sits at his kitchen table with coffee. He taps the voice button on Ditto. "My knee was stiff again when I got out of bed. Worse than yesterday. Vertigo was better though, not much dizzy today." He taps send. Thirty seconds total.

A week later, Jan opens the Symptoms tab. A simple chart shows his knee stiffness trending up over 10 days, his vertigo trending down. Three vertical dashed lines mark days his medication was adjusted. He brings this chart to his cardiologist. She adjusts his beta-blocker dose in five seconds.

---

## End-to-end flow

```
1. POST /voice-inputs
   Body: { patient_id, audio_url or transcript_text, duration_s? }

2. API stores the VoiceInput, emits `voice_input.received`

3. symptom_extractor_worker runs:
   - Extracts typed Symptom entities against a finite symptom ontology
   - Severity scored on defined scale per symptom type
   - Low confidence → confirmation card (review loop)
   - Writes Symptom entities with timestamp, severity, qualifiers, source_event_id

4. `symptom.logged` events emitted per extracted symptom

5. wiki_render_worker updates:
   - entities/conditions/{related_condition}.md (if symptom is linked)
   - symptoms/timeline.md
   - log.md

6. symptom_visualization_worker (on demand, triggered by API call):
   - Queries graph: last N days of symptoms by type
   - Produces a structured chart spec (JSON)
   - Returns to API for client rendering

7. symptom_pattern_worker (scheduled, weekly per patient):
   - Reads the last 30-90 days of symptom data + timeline events (meds, appointments)
   - Detects: trends (rising/falling), correlations with events, clustering
   - Emits `pattern.detected` events for surface-able patterns
   - Writes findings to a patterns section in the wiki

8. Before a scheduled appointment, prep_worker (existing) reads symptom patterns
   and includes them in the appointment brief
```

---

## Pipelines required

### Existing (reused)

- **voice_input.received event** (already in direction-c)
- **prep_worker** (reused — we only add a pattern-fetching hook)

### New pipelines (Path 2)

**`symptom_extractor_worker`**
- **Trigger**: `voice_input.received`
- **Input**: voice transcript, patient's recent symptoms, patient's conditions
- **Context mode**: fact + filter (fetch last 30 days of symptoms, relevant conditions)
- **Processor**: LLM-based (Haiku for extraction speed + cost; Sonnet only if Haiku struggles). Prompt structured around the symptom ontology (see Schemas §Symptom).
- **Output**: one or more `Symptom` entities with `(type, severity, qualifiers[], body_region?, source_excerpt, timestamp)`
- **Side effects**: `graph_write`; emits `symptom.logged` per extracted symptom; emits `review.required` for low-confidence extractions
- **Eval criteria**: given 20 annotated voice transcripts, extracts the right symptom types with correct severity bin 85%+ of the time. Zero cases of silent wrong log (below-confidence threshold always surfaces for confirmation).
- **Discipline**:
  - Only emit symptoms whose type is in the defined ontology
  - Confidence scoring per extraction; below threshold → flag for confirmation, do not silently log
  - Never infer symptoms not mentioned in the transcript

**`symptom_visualization_worker`**
- **Trigger**: API call (`GET /patients/{id}/symptoms/timeline`) — not an event-driven worker
- **Input**: symptom entities from the graph for the given patient, time range, and (optional) symptom type filter
- **Context mode**: fact (pure DB query)
- **Processor**: deterministic. No LLM. Bins data into time buckets (daily, weekly), computes trend lines, overlays event markers (medication changes, appointments).
- **Output**: a structured JSON chart spec — not an image. Client renders. (Example format below.)
- **Side effects**: none (read-only)
- **Eval criteria**: given known symptom data, returns correct bucket counts + correct event overlays. Deterministic; unit-testable.

**`symptom_pattern_worker`**
- **Trigger**: scheduled (e.g., weekly per patient). Also on-demand via API endpoint.
- **Input**: symptom history (30–90 days), timeline events (medications, appointments), patient conditions
- **Context mode**: fact + filter (read the wiki timeline and concept pages)
- **Processor**: hybrid. Deterministic trend detection (e.g., linear regression over severity) + LLM composition of a patient-facing pattern description that's grounded and non-diagnostic.
- **Output**: `Pattern` entities written to the graph and a `patterns/recent.md` wiki page
- **Side effects**: `graph_write`, `wiki_write`, `pattern.detected` events for high-salience patterns
- **Eval criteria**: given a curated dataset with known patterns (e.g., worsening fatigue after a specific medication change), detects the pattern 80%+ of the time. Does NOT hallucinate patterns in noise — false positive rate <10% on a random-noise dataset.
- **Discipline**:
  - Never make a diagnosis
  - Always ground each pattern in the source data (list the specific check-ins that show the trend)
  - If a pattern could be alarming (symptoms escalating rapidly), include a "worth raising with your doctor" framing — never imperative medical advice

---

## API endpoints

### `POST /voice-inputs`
- Input: `{ patient_id, audio_url? or transcript_text, duration_s?, captured_at? }`
- If `audio_url` provided, transcribe first (speech-to-text out of scope for prototype; accept `transcript_text` as primary input).
- Emits `voice_input.received` and returns the voice input ID immediately (processing async).

### `GET /patients/{patient_id}/symptoms/timeline`
- Query params: `symptoms=fatigue,pain` (optional filter), `from=YYYY-MM-DD`, `to=YYYY-MM-DD`, `bucket=day|week`
- Returns: chart spec (see format below)

### `GET /patients/{patient_id}/symptoms/patterns`
- Query params: `window=30d|90d` (default 30d)
- Returns: list of detected patterns with grounding

### `POST /patients/{patient_id}/symptoms/patterns/refresh`
- Triggers `symptom_pattern_worker` on-demand
- Returns: updated patterns

### `POST /voice-inputs/{id}/confirm` and `POST /voice-inputs/{id}/reject`
- Used when `symptom_extractor_worker` flagged an extraction for review

---

## Chart spec format (example)

```json
{
  "patient_id": "...",
  "window": {"from": "2026-03-15", "to": "2026-04-15"},
  "bucket": "day",
  "series": [
    {
      "symptom_type": "knee_stiffness",
      "unit_scale": "0-10",
      "data_points": [
        {"date": "2026-04-04", "severity": 6, "source_voice_input_ids": ["..."]},
        {"date": "2026-04-05", "severity": 7, "source_voice_input_ids": ["..."]},
        ...
      ]
    },
    {
      "symptom_type": "vertigo",
      "unit_scale": "0-10",
      "data_points": [...]
    }
  ],
  "event_overlays": [
    {
      "date": "2026-04-03",
      "kind": "medication_change",
      "label": "Started oxaliplatin",
      "source_event_id": "..."
    }
  ],
  "notable_patterns": [
    "knee_stiffness trending upward since 2026-04-03"
  ]
}
```

Client renders this as a line chart with event markers. The prototype's demo frontend can use any chart library.

---

## Quick-tap scale (alternative input)

For patients who find voice too much (cognitive decline, low-energy days, dementia), a numeric quick-tap scale is allowed as a second input modality:

- `POST /patients/{id}/symptoms/quick-tap`
- Body: `{ symptom_type, severity (0-10), timestamp? }`
- Creates a `Symptom` entity directly (no extraction needed, `source: quick_tap`)

The symptom ontology is the same. The extraction step is skipped; the review loop is skipped (direct structured input).

---

## Wiki integration

Three wiki pages are maintained by Path 2:

- **`symptoms/timeline.md`** — chronological list of symptom check-ins with frontmatter metadata. Used by other pipelines (prep_worker, condition pages) for context.
- **`symptoms/patterns.md`** — current detected patterns, grounded in specific data points.
- **Entity pages for conditions** — when a symptom is linked to a condition (e.g., vertigo → diabetes), the condition's entity page references recent symptom trends.

See `05-data-schemas.md` for the page frontmatter schema.

---

## Eval suite

Location: `/evals/symptom_tracking/`

Minimum test cases:

1. **Clean extraction**: "My knee was stiff, maybe 6 out of 10." → `{type: knee_stiffness, severity: 6, confidence: high}`
2. **Multi-symptom**: "Knee is worse, vertigo better." → two Symptom entities with inferred relative severities
3. **Ambiguous**: "Feeling off today." → low-confidence; review flagged; no silent log
4. **Out-of-ontology**: "My aura was weird today." → logged as `type: other, notes: "aura weird"`; flagged for ontology review
5. **Negation**: "No nausea today." → optional: log as `{type: nausea, severity: 0}` or skip entirely (agent decides; document the choice)
6. **Qualifier-rich**: "Pain in my left hip, only when I stand up." → `{type: pain, body_region: left_hip, qualifiers: [positional]}`
7. **Trend detection**: 14 days of rising fatigue scores → `symptom_pattern_worker` detects upward trend
8. **False-positive resistance**: 14 days of random-noise fatigue scores → no pattern detected
9. **Event correlation**: rising knee stiffness starting 2 days after a medication change → pattern detected with correlation note

---

## Success criteria for Path 2

- [ ] `POST /voice-inputs` accepts transcripts and triggers extraction
- [ ] `symptom_extractor_worker` passes eval thresholds (85%+ correct type + severity bin; 0 silent wrong logs)
- [ ] `GET /symptoms/timeline` returns a valid chart spec for a seeded patient
- [ ] `symptom_pattern_worker` runs on a fixture with known patterns and detects them
- [ ] Quick-tap scale endpoint works as an alternative input
- [ ] Symptoms flow into `prep_worker` output (verifiable via a second path: run prep for a test appointment; confirm recent symptoms are cited)
- [ ] Demo frontend has a minimal chart view that renders the chart spec

---

## What you choose

- Exact symptom ontology (start with the ~15 listed in schemas; expand as test cases demand)
- Severity scale: numeric 0–10 suggested, but qualitative 5-point is acceptable if the agent prefers; the data contract just requires `severity` be comparable across entries of the same type
- Visualization library on the demo frontend
- Whether to ship a mobile-style voice-recording UI (not required; a text input + "voice input" tag is enough)
- Pattern detection technique (linear regression, moving average, changepoint detection — pick what works; explain in repo README)

---

## What you do NOT have latitude on

- The symptom ontology is **versioned and finite**. New types require schema change, not runtime extension by the LLM.
- Confidence scoring is **required**. Low-confidence extractions go to review. Silent wrong logging is the #1 failure mode to prevent.
- `symptom_pattern_worker` outputs are **always grounded** in specific check-ins — no generic pattern claims.
- Patterns are **never** phrased as medical advice. "Worth raising with your doctor" is the strongest framing allowed.
- The chart spec is **not an image**. Always return structured data; let the client render.

---

## Out of scope for Path 2

- Speech-to-text (accept transcript text as input; real STT integration is production work)
- Wearable data ingestion (heart rate, CGM, etc.)
- Real-time alerts ("your symptoms escalated, call your doctor") — only surfaces passively in the app
- Multi-patient aggregation for research
- Export to clinical systems (EHR, etc.)
