# Technical Architecture: Voice Health Check-in

**Version**: 1.0
**Date**: 2026-02-05
**Status**: Draft
**Author**: Engineering Architecture

---

## Executive Summary

This document defines the technical architecture for Voice Health Check-in, a multi-agent AI system that processes voice input in near real-time to extract structured health data. The architecture prioritizes:

1. **Speed** (<2 second response time)
2. **Accuracy** (90%+ extraction precision)
3. **Safety** (no medical advice, quality control)
4. **Scalability** (handle concurrent users)
5. **Privacy** (data sovereignty, HIPAA-ready)

---

## 1. System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CLIENT (iOS/Android)                               │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Voice     │    │  Real-time  │    │   Chat UI   │    │  Timeline   │  │
│  │   Input     │───▶│ Transcription│───▶│  Display    │    │   View      │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
└────────────────────────────────┬────────────────────────────────────────────┘
                                 │ WebSocket (streaming)
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATION LAYER                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Session Orchestrator                              │   │
│  │  • Manages conversation state                                        │   │
│  │  • Routes to appropriate agents                                      │   │
│  │  • Enforces latency budgets                                          │   │
│  │  • Handles failover                                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────┬────────────────────────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
┌──────────────┐        ┌──────────────┐        ┌──────────────┐
│   SPEECH     │        │   CONTEXT    │        │  RESPONSE    │
│   PIPELINE   │        │   PIPELINE   │        │   PIPELINE   │
│              │        │              │        │              │
│ • ASR Agent  │        │ • Retrieval  │        │ • Generation │
│ • Extraction │        │ • Memory     │        │ • QC Agent   │
│ • Categorize │        │              │        │              │
└──────────────┘        └──────────────┘        └──────────────┘
        │                        │                        │
        └────────────────────────┼────────────────────────┘
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DATA LAYER                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   User      │    │   Health    │    │   Vector    │    │   Event     │  │
│  │   Store     │    │   Records   │    │   Store     │    │   Stream    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Multi-Agent Architecture

The system uses specialized agents that work in parallel and sequence to achieve <2 second response time.

### Agent Network Overview

```
                        ┌───────────────────┐
                        │                   │
   Voice Input ────────▶│  ORCHESTRATOR     │◀──── User Context
                        │                   │
                        └─────────┬─────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
          ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│  SPEECH AGENT   │    │  CONTEXT AGENT  │    │  CHART AGENT    │
│  (Extraction)   │    │  (Memory)       │    │  (Visualization)│
│                 │    │                 │    │                 │
│  • ASR          │    │  • Retrieve     │    │  • Update       │
│  • Parse        │    │    history      │    │    trends       │
│  • Categorize   │    │  • Find         │    │  • Detect       │
│  • Normalize    │    │    patterns     │    │    anomalies    │
│                 │    │  • Build        │    │  • Generate     │
│                 │    │    context      │    │    insights     │
└────────┬────────┘    └────────┬────────┘    └────────┬────────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                │
                                ▼
                   ┌─────────────────────┐
                   │                     │
                   │  RESPONSE AGENT     │
                   │  (Generation)       │
                   │                     │
                   │  • Generate reply   │
                   │  • Pick follow-up   │
                   │  • Check safety     │
                   │                     │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │                     │
                   │  QUALITY CONTROL    │
                   │  AGENT              │
                   │                     │
                   │  • Validate output  │
                   │  • Block medical    │
                   │    advice           │
                   │  • Detect crisis    │
                   │  • Ensure accuracy  │
                   │                     │
                   └──────────┬──────────┘
                              │
                              ▼
                        Response to User
```

---

## 3. Agent Specifications

### 3.1 Speech Agent (Extraction)

**Purpose**: Convert voice to structured health data

**Latency Budget**: 400ms

**Input**: Audio stream (WebM/Opus)

**Output**: Structured extraction JSON

```json
{
  "transcript": "Had a headache this morning, took two ibuprofen around 8am",
  "extractions": {
    "body": [
      {
        "type": "symptom",
        "name": "headache",
        "severity": null,
        "timing": "this morning",
        "location": "head",
        "confidence": 0.95
      }
    ],
    "actions": [
      {
        "type": "medication",
        "name": "ibuprofen",
        "dose": "2 tablets",
        "timing": "8am",
        "confidence": 0.92
      }
    ],
    "mind": [],
    "context": []
  }
}
```

**Implementation**:
- ASR: Whisper Large v3 (or Deepgram Nova-2 for speed)
- Extraction: Claude Haiku with function calling
- Streaming: Process in 2-second chunks for real-time display

**Prompt Strategy**:
```
You are a health data extraction specialist. Extract structured health
information from the patient's speech.

CATEGORIES:
- body: symptoms, vitals, physical sensations
- mind: emotions, mood, cognitive state
- actions: medications, exercise, treatments
- context: sleep, social, environment

RULES:
1. Only extract what is explicitly stated
2. Never infer diagnoses
3. Include confidence scores
4. Normalize medication names to standard forms
5. Convert relative times to absolute when possible

OUTPUT: JSON matching the schema provided.
```

---

### 3.2 Context Agent (Memory & Retrieval)

**Purpose**: Retrieve relevant history and identify patterns

**Latency Budget**: 300ms (parallel with Speech Agent)

**Input**: User ID, current session transcript

**Output**: Context package for response generation

```json
{
  "recent_entries": [
    {"date": "2026-02-03", "summary": "headache, 6/10 severity"},
    {"date": "2026-02-01", "summary": "headache, 4/10 severity"}
  ],
  "patterns": [
    {
      "type": "recurrence",
      "symptom": "headache",
      "frequency": "3x this week",
      "trend": "increasing"
    }
  ],
  "related_medications": ["ibuprofen", "acetaminophen"],
  "open_threads": [
    "Started new medication (metformin) 5 days ago"
  ],
  "suggested_followups": [
    "Ask about headache location compared to Tuesday"
  ]
}
```

**Implementation**:
- Vector store: Pinecone or pgvector
- Embedding model: text-embedding-3-small
- Retrieval: Hybrid (vector + keyword) search
- Pattern detection: Rules engine + LLM analysis

**Prompt Strategy**:
```
You are a health pattern analyst. Given the user's recent health entries,
identify:

1. RECURRENCE: Symptoms appearing multiple times
2. TRENDS: Increasing/decreasing severity patterns
3. CORRELATIONS: Possible connections (new med → new symptom)
4. OPEN THREADS: Unresolved health topics to follow up on

Be conservative. Only flag patterns with 3+ data points.
Never suggest diagnoses or causes.
```

---

### 3.3 Response Agent (Generation)

**Purpose**: Generate empathetic, helpful AI response

**Latency Budget**: 500ms

**Input**: Extractions, context, conversation history

**Output**: Natural language response + structured follow-up

```json
{
  "response": "That sounds frustrating - a headache first thing in the morning. This is the third one this week. Is it in the same spot as Tuesday, behind your eyes?",
  "follow_up_question": {
    "topic": "headache_location",
    "intent": "pattern_confirmation"
  },
  "tone": "empathetic",
  "references_history": true
}
```

**Implementation**:
- Model: Claude Sonnet (for nuance) or Haiku (for speed)
- Streaming: Token-by-token for perceived responsiveness

**Prompt Strategy**:
```
You are a caring health companion. Generate a response that:

1. ACKNOWLEDGES: Show you heard what they said
2. CONNECTS: Reference relevant history if available
3. FOLLOWS UP: Ask ONE thoughtful question (if appropriate)

TONE: Warm, concise, never clinical. Like a thoughtful friend.

CONSTRAINTS:
- Never diagnose ("You might have...")
- Never prescribe ("You should take...")
- Never minimize ("That's not a big deal")
- Keep under 40 words unless user is sharing a lot
- Maximum 1 follow-up question per response

CONTEXT PROVIDED:
- Recent health history
- Detected patterns
- Current extraction
```

---

### 3.4 Chart Agent (Visualization)

**Purpose**: Update visualizations in near real-time

**Latency Budget**: 200ms (async, non-blocking)

**Input**: New extraction data, historical data

**Output**: Updated chart data for client rendering

```json
{
  "charts_updated": [
    {
      "chart_id": "headache_frequency",
      "type": "bar",
      "data": [
        {"date": "Mon", "count": 1},
        {"date": "Tue", "count": 1},
        {"date": "Wed", "count": 0},
        {"date": "Thu", "count": 0},
        {"date": "Fri", "count": 1}
      ]
    },
    {
      "chart_id": "medication_timeline",
      "type": "event",
      "new_event": {"time": "8:00", "label": "Ibuprofen 2x"}
    }
  ],
  "insights": [
    {
      "type": "trend_alert",
      "message": "Headache frequency increased this week",
      "severity": "info"
    }
  ]
}
```

**Implementation**:
- Runs asynchronously after extraction
- Client-side chart library (Chart.js or D3)
- Incremental updates via WebSocket

---

### 3.5 Quality Control Agent

**Purpose**: Ensure safety, accuracy, and compliance

**Latency Budget**: 100ms (inline gate)

**Input**: Response before delivery

**Output**: Approved response or rejection with reason

```json
{
  "approved": true,
  "checks": {
    "no_diagnosis": true,
    "no_medical_advice": true,
    "no_crisis_indicators": true,
    "extraction_plausible": true,
    "tone_appropriate": true
  },
  "modifications": null
}
```

**OR (rejection)**:

```json
{
  "approved": false,
  "checks": {
    "no_diagnosis": false,
    "reason": "Response implies possible migraine diagnosis"
  },
  "suggested_revision": "Remove 'sounds like it could be migraines'"
}
```

**Implementation**:
- Fast classifier for common violations
- LLM review for edge cases
- Hard blocks: diagnosis, prescriptions, minimization
- Soft blocks: Tone issues (flag for review)

**Prompt Strategy**:
```
You are a medical compliance reviewer. Check the response for:

HARD VIOLATIONS (block immediately):
- Diagnosis language ("You have...", "Sounds like...")
- Treatment advice ("You should take...", "Try...")
- Dismissive language ("That's nothing", "Don't worry")
- Crisis indicators unaddressed

SOFT VIOLATIONS (flag for review):
- Overly clinical tone
- Excessive medical terminology
- Response too long (>50 words)

If HARD VIOLATION found: Reject and provide corrected version.
If SOFT VIOLATION found: Flag but approve.
```

---

## 4. Latency Breakdown

Target: **<2000ms** end-to-end

```
┌────────────────────────────────────────────────────────────────┐
│                    LATENCY BUDGET                               │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Audio Upload        ████░░░░░░░░░░░░░░░░░░░░  200ms           │
│                                                                 │
│  ┌──────────────────────────────────────────┐                  │
│  │ PARALLEL EXECUTION                        │                  │
│  │                                           │                  │
│  │  Speech Agent     ████████░░░░░░░░░░░░░░  400ms             │
│  │  Context Agent    ██████░░░░░░░░░░░░░░░░  300ms             │
│  │                                           │                  │
│  └──────────────────────────────────────────┘  (max: 400ms)    │
│                                                                 │
│  Response Agent      ██████████░░░░░░░░░░░░  500ms             │
│                                                                 │
│  QC Agent            ██░░░░░░░░░░░░░░░░░░░░  100ms             │
│                                                                 │
│  Network Return      ████░░░░░░░░░░░░░░░░░░  200ms             │
│                                                                 │
├────────────────────────────────────────────────────────────────┤
│  TOTAL               ████████████████░░░░░░  1400ms (target)   │
│                      ████████████████████░░  1800ms (p95 max)  │
└────────────────────────────────────────────────────────────────┘
```

### Optimization Strategies

1. **Parallel execution**: Speech + Context agents run simultaneously
2. **Streaming ASR**: Start processing before user finishes speaking
3. **Speculative generation**: Begin response generation with partial context
4. **Model selection**: Haiku for speed-critical paths, Sonnet for nuance
5. **Edge caching**: Pre-compute common responses and patterns
6. **Connection reuse**: Persistent WebSocket, warm model connections

---

## 5. Data Architecture

### 5.1 Data Models

**User**
```typescript
interface User {
  id: string;
  profile: {
    name: string;
    age: number;
    conditions: string[];  // Self-reported
    medications: string[]; // Active medications
  };
  preferences: {
    checkInTime: string;   // Preferred reminder time
    shareWithCircle: boolean;
    voiceOnly: boolean;
  };
}
```

**HealthEntry**
```typescript
interface HealthEntry {
  id: string;
  userId: string;
  timestamp: Date;

  // Raw data
  audioUrl?: string;
  transcript: string;

  // Extracted data
  body: SymptomEntry[];
  mind: MoodEntry[];
  actions: ActionEntry[];
  context: ContextEntry[];

  // Generated content
  summary: string;
  aiResponse: string;

  // Metadata
  duration: number;       // Seconds
  confidence: number;     // Overall extraction confidence
  reviewed: boolean;      // Human review flag
}
```

**Pattern**
```typescript
interface Pattern {
  id: string;
  userId: string;
  type: 'recurrence' | 'correlation' | 'trend';

  description: string;
  dataPoints: string[];   // HealthEntry IDs
  confidence: number;

  firstDetected: Date;
  lastUpdated: Date;

  dismissed: boolean;     // User can dismiss patterns
}
```

### 5.2 Vector Embeddings

For semantic search and pattern detection:

```typescript
interface HealthEmbedding {
  entryId: string;
  vector: number[];       // 1536 dimensions
  metadata: {
    date: Date;
    categories: string[]; // ['body', 'mind']
    symptoms: string[];
    medications: string[];
  };
}
```

### 5.3 Storage Architecture

| Data Type | Store | Rationale |
|-----------|-------|-----------|
| User profiles | PostgreSQL | Relational, ACID |
| Health entries | PostgreSQL | Structured, queryable |
| Audio files | S3/CloudFlare R2 | Object storage, CDN |
| Embeddings | Pinecone/pgvector | Vector similarity search |
| Session state | Redis | Fast, ephemeral |
| Event stream | Kafka/SQS | Async processing |

---

## 6. Security & Privacy

### 6.1 Data Protection

| Layer | Protection |
|-------|------------|
| **Transport** | TLS 1.3, certificate pinning |
| **Storage** | AES-256 encryption at rest |
| **Access** | Row-level security, user isolation |
| **Audio** | Optional: on-device processing only |
| **Retention** | User-controlled, GDPR-compliant deletion |

### 6.2 HIPAA Readiness

| Requirement | Implementation |
|-------------|----------------|
| Access controls | RBAC, audit logging |
| Encryption | At rest and in transit |
| Audit trails | All access logged |
| BAA | Signed with all sub-processors |
| Minimum necessary | Only required data collected |

### 6.3 Privacy Features

- **Local-first option**: Process speech on-device (future)
- **Data portability**: Export all data in standard format
- **Right to delete**: Full data deletion on request
- **Anonymization**: Research data fully anonymized

---

## 7. Infrastructure

### 7.1 Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                          CDN (CloudFlare)                        │
│                    Static assets, API caching                    │
└─────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Load Balancer (ALB)                         │
│                   WebSocket + HTTP routing                       │
└─────────────────────────────────────────────────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
       ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
       │   API       │      │   API       │      │   API       │
       │   Server    │      │   Server    │      │   Server    │
       │   (ECS)     │      │   (ECS)     │      │   (ECS)     │
       └─────────────┘      └─────────────┘      └─────────────┘
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
       ┌───────────────────────────┼───────────────────────────┐
       │                           │                           │
       ▼                           ▼                           ▼
┌─────────────┐           ┌─────────────┐           ┌─────────────┐
│  PostgreSQL │           │   Redis     │           │   Pinecone  │
│  (RDS)      │           │  (Cluster)  │           │   (Managed) │
└─────────────┘           └─────────────┘           └─────────────┘
```

### 7.2 Scaling Strategy

| Component | Scaling Trigger | Target |
|-----------|-----------------|--------|
| API Servers | CPU > 70% | Auto-scale 2-20 |
| WebSocket | Connection count | Auto-scale |
| LLM Calls | Queue depth | Rate limiting |
| Database | Connection pool | Read replicas |

### 7.3 Cost Estimates (MVP)

| Service | Monthly Cost | Notes |
|---------|--------------|-------|
| LLM API (Claude) | $2,000-5,000 | ~50K daily check-ins |
| ASR (Whisper/Deepgram) | $500-1,000 | Audio processing |
| Compute (ECS) | $500-1,000 | API servers |
| Database (RDS) | $200-500 | PostgreSQL |
| Vector DB | $100-300 | Pinecone |
| Storage | $100-200 | S3, audio files |
| **Total** | **$3,400-8,000** | ~5K DAU |

---

## 8. API Specification

### 8.1 WebSocket Protocol

**Connection**
```
wss://api.ditto.health/voice/v1/session
Authorization: Bearer <jwt>
```

**Client → Server Messages**

```typescript
// Start session
{ "type": "session.start" }

// Audio chunk (streaming)
{
  "type": "audio.chunk",
  "data": "<base64 encoded audio>",
  "sequence": 1
}

// End speaking
{ "type": "audio.end" }

// User finished check-in
{ "type": "session.complete" }
```

**Server → Client Messages**

```typescript
// Real-time transcription
{
  "type": "transcript.partial",
  "text": "Had a headache this",
  "confidence": 0.87
}

// Final transcript
{
  "type": "transcript.final",
  "text": "Had a headache this morning"
}

// AI response (streaming)
{
  "type": "response.chunk",
  "text": "That sounds"
}

// Extraction complete
{
  "type": "extraction.complete",
  "data": { /* HealthEntry */ }
}

// Chart update
{
  "type": "chart.update",
  "charts": [ /* Chart data */ ]
}
```

### 8.2 REST Endpoints

```
GET  /api/v1/entries                    # List health entries
GET  /api/v1/entries/:id                # Get single entry
GET  /api/v1/patterns                   # Get detected patterns
GET  /api/v1/summary?range=week         # Get period summary
POST /api/v1/entries/:id/edit           # Edit extraction
POST /api/v1/doctor-report              # Generate doctor summary
```

---

## 9. Monitoring & Observability

### 9.1 Key Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Response latency (p95) | <2000ms | >2500ms |
| Extraction accuracy | >90% | <85% |
| QC rejection rate | <5% | >10% |
| Session completion | >60% | <50% |
| Error rate | <1% | >2% |

### 9.2 Dashboards

1. **Real-time Operations**: Latency, errors, throughput
2. **AI Quality**: Extraction accuracy, QC blocks, user corrections
3. **Business**: Check-in completion, retention, engagement
4. **Infrastructure**: CPU, memory, queue depth

### 9.3 Logging

- **Request logs**: All API calls with latency
- **Agent logs**: Per-agent execution time and outputs
- **Quality logs**: QC decisions and reasons
- **Audit logs**: Data access for compliance

---

## 10. Testing Strategy

### 10.1 Test Categories

| Type | Coverage Target | Tools |
|------|-----------------|-------|
| Unit tests | 80% | Jest/pytest |
| Integration tests | Key flows | Playwright |
| E2E tests | Critical paths | Cypress |
| Load tests | 10x expected | k6 |
| AI quality tests | Extraction accuracy | Custom harness |

### 10.2 AI Testing Approach

**Test Set**: 500+ labeled voice samples across categories

| Test Category | Metric | Minimum |
|---------------|--------|---------|
| Symptom extraction | Precision/Recall | 90% |
| Medication extraction | Precision/Recall | 95% |
| Severity detection | Accuracy | 85% |
| Safety compliance | Pass rate | 100% |

---

## 11. Implementation Phases

### Phase 1: Foundation (Weeks 1-2)
- WebSocket infrastructure
- Basic ASR integration
- Simple extraction (symptoms only)
- Transcript display

### Phase 2: Core Agents (Weeks 3-4)
- Speech Agent with full extraction
- Context Agent with basic retrieval
- Response Agent with follow-ups
- QC Agent baseline

### Phase 3: Quality & Polish (Weeks 5-6)
- Pattern detection
- Chart visualization
- QC refinement
- Performance optimization

### Phase 4: Launch Prep (Weeks 7-8)
- Load testing
- Security audit
- Documentation
- Beta rollout

---

## 12. Open Technical Questions

- [ ] On-device ASR vs. cloud trade-offs?
- [ ] How to handle poor audio quality gracefully?
- [ ] Should we support offline mode?
- [ ] What's the retention policy for audio files?
- [ ] Multi-language priority and approach?

---

## 13. References

- [PRD: Voice Health Check-in](./PRD.md)
- [Competitive Analysis](./competitive-analysis.md)
- [Design Panel Consensus](./mockups/panel-consensus.md)
- [Anthropic Claude API Documentation](https://docs.anthropic.com)
- [Whisper API Documentation](https://platform.openai.com/docs/guides/speech-to-text)

---

**Document Control**
- Created: 2026-02-05
- Last Updated: 2026-02-05
- Owner: Engineering Architecture
- Reviewers: CTO, AI Lead, Security Lead
