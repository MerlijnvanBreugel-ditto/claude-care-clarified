# Work Breakdown: Voice Health Check-in MVP

**Version**: 1.0
**Date**: 2026-02-05
**Target**: 8-week MVP to beta launch

---

## Parallel Workstream Overview

```
WEEK  1    2    3    4    5    6    7    8
      │    │    │    │    │    │    │    │
WS1   ████████████████████████████░░░░░░░░  Voice Pipeline
WS2   ████████████████████████████░░░░░░░░  AI Agents
WS3   ████████████████████████░░░░░░░░░░░░  Data & Backend
WS4   ░░░░░░░░████████████████████████████  Mobile Client
WS5   ░░░░░░░░░░░░░░░░████████████████████  QA & Safety
      │    │    │    │    │    │    │    │
      ▼    ▼    ▼    ▼    ▼    ▼    ▼    ▼
INT         I1   I2       I3   I4   I5   BETA
```

**Integration Points:**
- I1 (Week 2): Voice → Transcript display
- I2 (Week 3): Transcript → Extraction → Storage
- I3 (Week 5): Full check-in flow with agents
- I4 (Week 6): Timeline + charts connected
- I5 (Week 7): Care Circle sharing flow

---

## Workstream 1: Voice Pipeline

**Team**: 2 engineers
**Dependencies**: None (can start immediately)

### Week 1-2: Infrastructure

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| WebSocket server setup | P0 | 3d | Server accepts connections, handles auth |
| Audio chunk protocol | P0 | 2d | Client can stream audio in 2s chunks |
| ASR integration (Deepgram) | P0 | 3d | Audio → transcript with <500ms latency |
| Streaming transcript to client | P0 | 2d | Client displays words as spoken |

**Deliverable**: Can record voice and see real-time transcript

### Week 3-4: Extraction Pipeline

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Speech Agent implementation | P0 | 4d | Transcript → structured extractions |
| Extraction schema validation | P0 | 2d | Output matches HealthEntry schema |
| Confidence scoring | P0 | 2d | All extractions have confidence 0-1 |
| Error handling | P0 | 2d | Graceful handling of audio issues |

**Deliverable**: Voice → transcript → structured health data

### Week 5-6: Optimization

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Latency optimization | P0 | 3d | <400ms for Speech Agent |
| Streaming extraction | P1 | 2d | Begin extraction before speech ends |
| Batch processing for history | P1 | 2d | Can reprocess old entries |
| Audio quality detection | P1 | 1d | Warn user if audio is poor |

---

## Workstream 2: AI Agents

**Team**: 2 AI engineers
**Dependencies**: Implementation spec prompts

### Week 1-2: Core Prompts

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Response Agent v1 | P0 | 4d | Generates empathetic responses |
| QC Agent v1 | P0 | 3d | Blocks diagnosis/prescription |
| Testing harness setup | P0 | 2d | Can run prompts against fixtures |
| Prompt iteration (10 rounds) | P0 | 3d | 90%+ pass rate on test cases |

**Deliverable**: Working Response + QC agents with tested prompts

### Week 3-4: Memory & Patterns

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Context Agent v1 | P0 | 4d | Retrieves relevant history |
| Embedding pipeline | P0 | 2d | Health entries → vectors |
| Pattern detection rules | P0 | 3d | Recurrence, correlation, trend |
| Follow-up question generation | P0 | 2d | 1-2 smart follow-ups per session |

**Deliverable**: AI remembers history and suggests follow-ups

### Week 5-6: Safety & Quality

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Crisis detection classifier | P0 | 3d | 100% recall on test cases |
| QC edge case handling | P0 | 2d | Handles subtle violations |
| Agent orchestration | P0 | 3d | Parallel execution, latency budget |
| Response tone calibration | P1 | 2d | Warm but not saccharine |

**Deliverable**: Safe, high-quality AI agent network

---

## Workstream 3: Data & Backend

**Team**: 1 engineer
**Dependencies**: Data model spec

### Week 1-2: Core Data Layer

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| PostgreSQL schema setup | P0 | 2d | All tables created with migrations |
| HealthEntry CRUD API | P0 | 2d | Create, read, update entries |
| User profile API | P0 | 1d | Profile with conditions, meds |
| Audio file storage (S3) | P0 | 1d | Upload, retrieve, delete audio |

**Deliverable**: Can store and retrieve health entries

### Week 3-4: Vector & Patterns

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Vector store setup (Pinecone) | P0 | 2d | Connection, basic operations |
| Embedding storage pipeline | P0 | 2d | Entries automatically embedded |
| Pattern storage model | P0 | 2d | CRUD for patterns |
| Summary generation API | P0 | 2d | On-demand summaries |

**Deliverable**: Vector search and pattern storage working

### Week 5-6: Care Circle

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Care Circle data model | P0 | 2d | Groups, members, permissions |
| Sharing API | P0 | 2d | Share entry to circle |
| Notification service | P1 | 2d | Push notifications to circle |
| Privacy controls | P0 | 2d | User controls what's shared |

**Deliverable**: Basic Care Circle sharing functional

---

## Workstream 4: Mobile Client

**Team**: 2 engineers (iOS/Android)
**Dependencies**: WebSocket protocol spec, design mockups

### Week 3-4: Voice UI

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Voice recording component | P0 | 3d | Record, stream to server |
| Immersive orb interface | P0 | 4d | Breathing animation, states |
| Transcript display | P0 | 2d | Real-time text as spoken |
| WebSocket client | P0 | 2d | Connect, send/receive messages |

**Deliverable**: Can do voice check-in with orb UI

### Week 5-6: Data Display

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Timeline view | P0 | 3d | See past check-ins by date |
| Entry detail view | P0 | 2d | Full entry with extractions |
| Chart components | P1 | 3d | Symptom frequency/severity |
| Edit extraction UI | P1 | 2d | User can correct extractions |

**Deliverable**: Timeline and charts working

### Week 7-8: Polish & Sharing

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Onboarding flow | P0 | 2d | First-time user experience |
| Share to Care Circle UI | P0 | 2d | Share flow with options |
| Notification handling | P1 | 2d | Receive and display notifications |
| Accessibility pass | P0 | 2d | VoiceOver, large text, reduce motion |

**Deliverable**: Complete mobile experience

---

## Workstream 5: QA & Safety

**Team**: 1 engineer
**Dependencies**: Test fixtures, safety spec

### Week 5-6: Test Suite

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Unit test framework | P0 | 1d | Jest/pytest configured |
| API integration tests | P0 | 2d | All endpoints tested |
| AI quality test harness | P0 | 3d | Run extraction tests automatically |
| 500+ labeled test fixtures | P0 | 4d | Voice samples with expected outputs |

**Deliverable**: Automated test suite

### Week 7-8: Launch Prep

| Task | Priority | Effort | Definition of Done |
|------|----------|--------|-------------------|
| Load testing | P0 | 2d | 10x expected load, <2s p95 |
| Security audit | P0 | 3d | No critical/high vulnerabilities |
| Safety compliance check | P0 | 2d | 100% pass on safety tests |
| Beta test coordination | P1 | 3d | 50 beta users recruited |

**Deliverable**: Ready for beta launch

---

## AI Agent Task Assignment

For AI coding agents to pick up implementation:

### Agent Team A: Speech Agent

```yaml
task: Implement Speech Agent
files_to_create:
  - src/agents/speech/index.ts
  - src/agents/speech/prompt.ts
  - src/agents/speech/schema.ts
  - src/agents/speech/tests.ts

inputs:
  - Audio transcript (string)
  - Patient conditions (string[])
  - Patient medications (string[])

outputs:
  - HealthEntry extractions (body, mind, actions, context)
  - Confidence scores
  - Extraction flags

spec_reference: implementation-spec.md#speech-agent
test_fixtures: fixtures/extraction/
success_criteria:
  - 90%+ precision/recall on symptom extraction
  - 95%+ precision/recall on medication extraction
  - <400ms execution time
```

### Agent Team B: Response Agent

```yaml
task: Implement Response Agent
files_to_create:
  - src/agents/response/index.ts
  - src/agents/response/prompt.ts
  - src/agents/response/tests.ts

inputs:
  - Current extraction
  - User history (past 14 days)
  - Detected patterns
  - Conversation turn number

outputs:
  - Response text
  - Follow-up question (optional)
  - Should end conversation
  - Sentiment classification

spec_reference: implementation-spec.md#response-agent
test_fixtures: fixtures/response/
success_criteria:
  - 0% diagnosis language
  - 0% prescription language
  - 100% empathetic tone on emotional inputs
  - <500ms execution time
```

### Agent Team C: Context Agent

```yaml
task: Implement Context Agent
files_to_create:
  - src/agents/context/index.ts
  - src/agents/context/retrieval.ts
  - src/agents/context/patterns.ts
  - src/agents/context/tests.ts

inputs:
  - User ID
  - Current session transcript
  - Current extractions

outputs:
  - Recent entries (summarized)
  - Detected patterns
  - Suggested follow-ups
  - Open threads

spec_reference: implementation-spec.md#context-agent
test_fixtures: fixtures/context/
success_criteria:
  - Retrieves relevant history in <300ms
  - Pattern detection with 3+ data points
  - No spurious correlations
```

### Agent Team D: QC Agent

```yaml
task: Implement QC Agent
files_to_create:
  - src/agents/qc/index.ts
  - src/agents/qc/prompt.ts
  - src/agents/qc/classifier.ts
  - src/agents/qc/tests.ts

inputs:
  - Proposed response
  - Original patient message
  - Extractions

outputs:
  - Approved (boolean)
  - Violation list
  - Suggested revision (if blocked)

spec_reference: implementation-spec.md#quality-control-agent
test_fixtures: fixtures/qc/
success_criteria:
  - 100% block rate on diagnosis phrases
  - 100% block rate on prescription phrases
  - 0% false positives on safe responses
  - <100ms execution time
```

### Agent Team E: Mobile Voice UI

```yaml
task: Implement Voice Check-in UI
files_to_create:
  - src/screens/CheckIn/index.tsx
  - src/components/Orb/index.tsx
  - src/components/Transcript/index.tsx
  - src/hooks/useVoiceSession.ts

design_reference: mockups/panel-consensus.md (Direction C)

requirements:
  - Full-screen immersive mode
  - Breathing orb animation
  - Real-time transcript display
  - Graceful error states
  - Accessibility: VoiceOver, reduce motion

spec_reference: implementation-spec.md#conversation-examples
success_criteria:
  - 60fps orb animation
  - <100ms transcript update latency
  - VoiceOver fully describes orb state
```

---

## Dependency Graph

```
Week 1-2:
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  WS1: Voice │     │  WS2: AI    │     │  WS3: Data  │
│  Pipeline   │     │  Prompts    │     │  Schema     │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                           ▼
                    Integration I1
                    (Transcript Display)

Week 3-4:
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  WS1: Full  │     │  WS2: Memory│     │  WS4: Voice │
│  Extraction │     │  + Patterns │     │  UI         │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                           ▼
                    Integration I2, I3
                    (Full Check-in Flow)

Week 5-6:
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  WS1: Perf  │     │  WS2: Safety│     │  WS3: Share │
│  Optimize   │     │  + QC       │     │  + Circle   │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                           ▼
                    Integration I4
                    (Timeline + Charts)

Week 7-8:
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  WS4: Polish│     │  WS5: Test  │     │  WS5: Load  │
│  + Onboard  │     │  Suite      │     │  + Security │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                           ▼
                      BETA LAUNCH
```

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| ASR accuracy on accents | Medium | High | Test with diverse speakers, fallback options | WS1 |
| Response latency >2s | Medium | High | Optimize prompts, model selection | WS2 |
| Crisis detection false negatives | Low | Critical | Extensive test suite, conservative threshold | WS2 |
| Mobile app store rejection | Low | High | Pre-submission review, accessibility compliance | WS4 |
| Beta user recruitment | Medium | Medium | Start recruiting week 4 | WS5 |

---

## Definition of Done: MVP

- [ ] Complete 30-second voice check-in via immersive UI
- [ ] Real-time transcript display (<100ms lag)
- [ ] AI responds with contextual follow-up in <2 seconds
- [ ] Extractions stored with 90%+ accuracy
- [ ] Timeline shows past 30 days of check-ins
- [ ] Basic charts for top 3 symptoms
- [ ] At least 1 pattern detection working
- [ ] Crisis detection 100% recall
- [ ] QC blocks 100% of diagnosis/prescription phrases
- [ ] Care Circle basic sharing functional
- [ ] VoiceOver accessible
- [ ] 50 beta users complete 5+ check-ins each

---

## Launch Readiness Checklist

**Technical:**
- [ ] <2 second p95 latency
- [ ] <1% error rate
- [ ] Load tested to 10x expected
- [ ] Security audit passed
- [ ] HIPAA compliant

**Product:**
- [ ] NPS >40 from beta
- [ ] 40%+ 7-day retention
- [ ] 60%+ check-in completion
- [ ] No critical bugs in 1 week

**Operations:**
- [ ] Monitoring dashboards live
- [ ] On-call rotation set
- [ ] Incident response documented
- [ ] User support ready

---

**Hand this to your AI team. Let's build.**
