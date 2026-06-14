# Care Brain MVP: Timeline, UX Frameworks & Operational Guide

**Date**: 2026-04-08
**Status**: Companion to [care-brain-mvp-spec.md](care-brain-mvp-spec.md)
**Purpose**: Visual reference for sprint timeline, team tracks, UX research methodology, design frameworks, risk register, and success metrics. The spec defines what and how; this document makes it scannable.

---

## 12-Week Sprint Timeline

### Overview

```
WEEK    1    2    3    4    5    6    7    8    9   10   11   12
SPRINT  ├─ S1 ─┤  ├─ S2 ─┤  ├─ S3 ─┤  ├─ S4 ─┤  ├─ S5 ─┤  ├─ S6 ─┤
SLICE   ├──── Slice 1: Core Brain ────┤  ├── Slice 2: Living Memory ──┤  ├─ Slice 3: Proactive ─┤  Polish
GATE                            GATE 1                          GATE 2                    GATE 3
```

### Track-by-Track Breakdown

#### UX Research Track

| Weeks | Sprint | Activity | Output |
|---|---|---|---|
| 1-2 | S1 | Define 5 personas, heuristic framework, trust signals checklist | Persona cards, evaluation rubrics |
| 3-4 | S2 | Synthetic patient walkthroughs of Slice 1 (summaries, suggestions, Q&A) | Scored findings, design recommendations for Slice 2 |
| 5-6 | S3 | Voice input persona walkthroughs (focus: Jan 74, Corrie 81) | Voice UX findings, confirmation card recommendations |
| 7-8 | S4 | Heuristic audit of full Slice 1+2 build (10-point checklist per screen) | Pass/fail per screen, fix list for Sprint 5 |
| 9-10 | S5 | Prep + sharing walkthroughs (focus: Aysel for translation, Pieter for caregiver) | Adaptation quality findings |
| 11-12 | S6 | Final usability audit, full journey walkthrough with all 5 personas | Ship readiness report |

#### Design Track

| Weeks | Sprint | Activity | Output |
|---|---|---|---|
| 1-2 | S1 | Summary view with suggestion chips, Q&A answer expansion, typography system | Figma designs for Slice 1 UI |
| 3-4 | S2 | Q&A polish, answer streaming, "Ask something else" | Refined Slice 1 designs |
| 5-6 | S3 | Profile tab layout, voice input flow, confirmation cards, document capture | Figma designs for Slice 2 UI |
| 7-8 | S4 | Document explanation view, conflict resolution, prep screen | Figma designs for Slice 2 polish + Slice 3 prep |
| 9-10 | S5 | Sharing preview with role badges, language switching | Figma designs for Slice 3 |
| 11-12 | S6 | Micro-interactions, empty states, error states, accessibility polish | Final design polish |

#### Infrastructure Track

| Weeks | Sprint | Deliverable |
|---|---|---|
| 1-2 | S1 | Event bus + worker framework + Health Profile Store + FastAPI skeleton + config |
| 3-4 | S2 | Profile Store API + SSE streaming + answer cache layer |
| 5-6 | S3 | Profile versioning + audit log + diff engine + conflict detection + voice event types |
| 7-8 | S4 | Image upload + profile scoped queries + voice API |
| 9-10 | S5 | Prep pipeline trigger + sharing preview infrastructure |
| 11-12 | S6 | Load testing + hardening + performance optimization |

#### Engineering: Pipelines Track

| Weeks | Sprint | Pipelines built |
|---|---|---|
| 1-2 | S1 | Recording pipeline (summarize_worker + extract_worker + profile merge) |
| 3-4 | S2 | Answer pipeline (answer_worker + streaming + caching) + suggest_worker |
| 5-6 | S3 | Voice input pipeline + change detection pipeline + recording pipeline upgrade (cross-appointment context) |
| 7-8 | S4 | Document pipeline (explain_worker + extract + merge) |
| 9-10 | S5 | Appointment prep pipeline + sharing adaptation (adapt_worker + translate_worker) |
| 11-12 | S6 | Bug fixes, edge cases, full integration testing |

#### Engineering: Mobile (iOS) Track

| Weeks | Sprint | Screens built |
|---|---|---|
| 1-2 | S1 | Summary view refactor + suggestion chips area + API client + loading states |
| 3-4 | S2 | Suggestion chips UI + inline answer with streaming + source attribution + "Ask something else" |
| 5-6 | S3 | Profile tab + manual correction + voice input UI + confirmation cards + change indicator |
| 7-8 | S4 | Document capture + explanation view + profile source attribution + conflict resolution UI |
| 9-10 | S5 | Prep screen + manual appointment entry + sharing preview + role/language switching |
| 11-12 | S6 | Navigation polish + empty states + error states + accessibility pass (VoiceOver, Dynamic Type) |

#### Prompt Engineering Track

| Weeks | Sprint | Work |
|---|---|---|
| 1-2 | S1 | Author summarize + extract prompts. Create 10 synthetic conversations with ground truth. |
| 3-4 | S2 | Author answer + suggest prompts. Build eval harness. Run full eval. |
| 5 | S3a | Build eval harness infrastructure |
| 6 | S3b | Tune extract for voice input. Create 10 voice test cases. Tune suggest for cross-appointment. |
| 7-8 | S4 | Author explain prompt. Create 8 documents. Full regression (conversations + voice + documents). |
| 9-10 | S5 | Author prep + adapt + translate prompts. Create eval sets (5 prep, 4 adaptation). |
| 11-12 | S6 | Full regression testing across all workers. |

#### QA Track

| Weeks | Sprint | Work |
|---|---|---|
| 1-2 | S1 | 10 sample conversations through recording pipeline |
| 3 | S2a | Quality evaluation of Slice 1 outputs |
| 4 | S2b | **GATE 1** evaluation (all criteria, documented pass/fail) |
| 5-7 | S3-4a | Profile accuracy testing, voice edge cases, document type coverage |
| 8 | S4b | **GATE 2** evaluation (includes Slice 1 regression) |
| 9-10 | S5 | Prep quality, adaptation differentiation, translation accuracy |
| 11 | S6a | **GATE 3** evaluation (includes full regression) |
| 12 | S6b | Final audit, demo preparation |

---

## Quality Gates

### Gate 1 — End of Week 4 (Slice 1 complete)

**Question**: Can a patient record, get a summary with suggestions, tap a suggestion, and get a grounded answer?

| # | Criterion | Target | Method | Pass/Fail |
|---|---|---|---|---|
| 1 | Summary quality | ≥95% accuracy on 10 conversations | Manual review by PO | |
| 2 | Suggestion specificity | 80%+ conversation-specific, not generic | Manual review | |
| 3 | Answer grounding | 100% reference source material | Automated + manual | |
| 4 | Answer hallucination | 0 hallucinated medical claims in eval set | Manual review | |
| 5 | End-to-end latency | Summary <10s, answer first token <3s | Automated measurement | |
| 6 | Profile extraction | Correct medications/conditions in 8/10 conversations | Manual comparison | |
| 7 | Event tracing | Every pipeline step logged with correlation ID | Log inspection | |

**Blocking rule**: If criteria 3 or 4 fail, Slice 2 does not start.

### Gate 2 — End of Week 8 (Slice 2 complete)

**Question**: Does the brain accumulate knowledge? Can a patient update their profile by voice and photo?

| # | Criterion | Target | Method | Pass/Fail |
|---|---|---|---|---|
| 1 | Profile accuracy | ≥90% correct after 3+ recordings per patient | Automated comparison | |
| 2 | Voice extraction | Correct extraction in 8/10 voice test cases | Manual review | |
| 3 | Voice confirmation | Ambiguous inputs trigger clarification | Manual edge case test | |
| 4 | Document explanation | Patient-friendly, accurate for 7/8 doc types | Manual review | |
| 5 | Profile versioning | Audit log captures every mutation with source | Automated test | |
| 6 | Conflict detection | Contradictory data flagged, not silently overwritten | Manual test | |
| 7 | Cross-appointment Q&A | Answers reference previous visits when relevant | Manual review | |
| 8 | User correction | user_verified fields survive future extractions | Automated test | |
| 9 | Regression | All Gate 1 criteria still pass | Re-run eval suite | |

**Blocking rule**: If criterion 3 fails (silent wrong update), voice input does not ship.

### Gate 3 — End of Week 11 (Slice 3 complete)

**Question**: Does the brain proactively help and adapt for different audiences?

| # | Criterion | Target | Method | Pass/Fail |
|---|---|---|---|---|
| 1 | Prep relevance | Suggested questions reference actual patient data in 4/5 scenarios | Manual review | |
| 2 | Prep grounding | Zero prep items not derivable from patient journey | Manual review | |
| 3 | Adaptation differentiation | Partner and friend versions meaningfully different | Blind comparison | |
| 4 | Translation accuracy | Medical terms preserved, meaning intact (NL, EN, TR) | Native speaker review | |
| 5 | Elderly usability | 8/10 heuristic items pass per screen | UX researcher eval | |
| 6 | Full journey test | End-to-end synthetic journey completes without errors | Automated + manual | |
| 7 | Regression | All Gate 1 + Gate 2 criteria still pass | Re-run eval suites | |
| 8 | Pipeline observability | Any event traceable via correlation_id | Manual trace of 5 events | |

---

## Synthetic Patient Personas

### Mara (68) — Oncology, elderly, partner-involved

- **Condition**: Colon cancer, stage 3b
- **Life**: Retired teacher. Lives with partner Hans. Moderate smartphone use (WhatsApp, photos).
- **Emotional state**: Anxious about treatment changes. Wants to understand everything but forgets after appointments.
- **Care circle**: Hans handles logistics. Daughter lives 2 hours away.
- **Tech comfort**: Medium. Uses apps her daughter set up. Can navigate familiar interfaces. Gets lost in new ones.
- **Tests**: Summary comprehension, suggestion relevance, answer trust, sharing preview for Hans
- **Critical scenario**: Medication change from capecitabine to oxaliplatin. Does Mara understand what changed and why?

### Jan (74) — Chronic multi-condition, low-tech, solo

- **Conditions**: Diabetes type 2, cardiac arrhythmia, mild hypertension
- **Life**: Widower, lives alone. Daughter Sanne checks in weekly by phone.
- **Emotional state**: Stoic but quietly overwhelmed. Forgets which doctor said what.
- **Care circle**: Sanne (daughter), GP, cardiologist, diabetes nurse
- **Tech comfort**: Low. Calls and basic apps only. Big text essential. Confused by navigation.
- **Tests**: Profile comprehension (multiple medications, multiple sources), voice input usability, tap target sizes
- **Critical scenario**: Voice input "Ze hebben mijn medicijn veranderd." Ambiguous. Does the confirmation flow resolve it without confusing Jan?

### Aysel (52) — Multilingual, dual-care, working

- **Condition**: Breast cancer, remission monitoring (6-month scans)
- **Life**: Turkish-Dutch, bilingual. Full-time logistics coordinator. Mother (76) speaks only Turkish.
- **Emotional state**: Competent but stretched thin. Managing own care AND mother's appointments.
- **Care circle**: Mother (Turkish-only), husband, two sisters
- **Tech comfort**: High. Uses multiple apps daily. Expects things to work fast.
- **Tests**: Translation accuracy (NL → TR), sharing adaptation for Turkish-speaking mother, multi-patient scenario
- **Critical scenario**: Sharing scan results with mother. Turkish adaptation must be medically accurate AND gentle. Aysel currently translates everything herself.

### Pieter (45) — Caregiver, tech-savvy, complex meds

- **Condition**: Caregiver for wife Lisa (43) with relapsing MS
- **Life**: Product manager. Attends all of Lisa's appointments. Manages medication schedule. Two kids (8, 11).
- **Emotional state**: Organized, determined, occasionally overwhelmed by coordination burden.
- **Care circle**: Lisa (patient), Pieter's mother (helps with kids), Lisa's neurologist, MS nurse, GP
- **Tech comfort**: Very high. Wants structured data, not narratives. Power user.
- **Tests**: Profile completeness for complex medication regimen, prep utility before neurologist, caregiver-adapted sharing
- **Critical scenario**: Lisa's neurologist changes DMT (disease-modifying therapy). Does the profile correctly track the switch? Does prep reference the previous therapy and its issues?

### Corrie (81) — Cognitive decline, assisted living, maximum simplicity

- **Condition**: Early cognitive decline, recent hip replacement, mild heart failure
- **Life**: Assisted living facility. Son Henk manages everything. Uses iPad with large text.
- **Emotional state**: Easily confused by new things. Trusts "the app her son set up."
- **Care circle**: Henk (son, primary manager), facility care team
- **Tech comfort**: Minimal. If it doesn't look like what she expects, she puts the iPad down.
- **Tests**: Maximum simplicity. Can Corrie tap a suggestion? Can she understand the summary? Does the interface confuse her?
- **Critical scenario**: Everything. If any screen fails the Corrie test, it needs redesign. She is the design constraint.

---

## Persona Walkthrough Rubric

Used for every synthetic patient test. Score 1-5 per dimension.

| Dimension | 1 (Fail) | 3 (Acceptable) | 5 (Excellent) |
|---|---|---|---|
| **Comprehension** | Persona would not understand the content | Persona would understand with effort | Persona immediately gets it |
| **Trust** | Persona would distrust or be alarmed | Persona would accept but with reservation | Persona feels confident and reassured |
| **Utility** | Content adds no value over current workaround | Content is somewhat helpful | Content solves the problem better than any workaround |
| **Emotional fit** | Tone is wrong for the moment (too clinical, too casual, alarming) | Tone is neutral | Tone matches the emotional context perfectly |
| **Actionability** | Persona doesn't know what to do next | Persona has a vague sense of next steps | Persona knows exactly what to do and feels equipped |

**Minimum passing score**: Average ≥ 3.5 across all dimensions for each persona. Any single dimension scoring 1 requires a fix before gate review.

---

## Design Principles: Magic, Not AI

### The six principles

| # | Principle | Do | Don't |
|---|---|---|---|
| 1 | **Intelligence is Invisible** | "Ditto prepared this for you" / "Based on your conversation" | "Our AI analyzed..." / "Generated by Claude" / Robot icons |
| 2 | **Suggest, Don't Demand** | Suggestion chips below content / Confirmation cards | Auto-updating meds / Chat-style "How can I help?" |
| 3 | **Source Everything** | "From your appointment on April 4" / Doctor name + date | Floating facts with no origin / Generic health info |
| 4 | **Big, Clear, Calm** | Card layouts / Single column / 44pt+ tap targets / 16pt+ text | Dense tables / Small toggles / Multi-column / Hamburger menus |
| 5 | **Progressive Depth** | Summary → tap for explanation → tap for source | Everything visible at once / Hidden expandable sections |
| 6 | **Familiar Patterns Only** | Tap / Scroll / Back arrow / Clear labels | Swipe actions / Long-press / Drag / Floating action buttons |

### Trust signals for 65+ users

| Signal | How it manifests |
|---|---|
| **Doctor attribution** | Every summary, answer, suggestion names doctor + date |
| **Your data, your control** | Profile shows what Ditto knows. Patient corrects anything. Source per item. |
| **Medical humility** | Every answer: "For medical advice, contact your care team." Never "you should" about treatment. |
| **Confirmation before action** | Voice input shows what it heard. Document extraction asks "Is this right?" |
| **Source transparency** | Every profile item: "From your appointment on April 4" or "You told Ditto on March 15" |
| **Consistent tone** | Same warm, clear voice across all surfaces. Like a trusted friend. |

---

## Elderly Usability Heuristics (10-point checklist)

Applied at every gate review. Scored pass/fail per screen.

| # | Heuristic | Test method | Automated? |
|---|---|---|---|
| 1 | Text ≥ 16pt body, ≥ 20pt headings | Scan rendered screens | Yes |
| 2 | Contrast ratio ≥ 4.5:1 (WCAG AA) | Accessibility scanner | Yes |
| 3 | Tap targets ≥ 44x44pt with ≥ 8pt spacing | Layout inspection | Semi |
| 4 | One primary action per screen | Design review | No |
| 5 | No gesture beyond tap and scroll | Interaction audit | No |
| 6 | Loading state visible within 500ms | Performance test | Yes |
| 7 | Error messages in plain language with next step | Error state review | No |
| 8 | Always clear where I am and how to go back | 3-second persona test | No |
| 9 | Medical content readable without domain knowledge | Flesch reading ease ≥ 60 | Yes |
| 10 | VoiceOver announces all interactive elements | Screen reader test | Semi |

**Gate threshold**: 8/10 pass per screen. Heuristics 1-3 (accessibility basics) must always pass.

---

## Risk Register

### Critical risks (product-breaking if they occur)

**Medical hallucination**
- Impact: Patient acts on fabricated medical information
- Likelihood: Medium without strict grounding
- Mitigation: Strict grounding rules in every worker prompt. Source attribution required. "Cannot answer from available data" fallback. Eval harness checks grounding on every prompt change.
- Detection: Automated grounding check in CI. Manual review of 50 random answers/week post-launch.

**Silent wrong profile update**
- Impact: Brain updates medication incorrectly without patient knowing
- Likelihood: Low with confirmation flow
- Mitigation: All voice/document extractions require user confirmation. Low-confidence items flagged. user_verified fields survive future extraction.
- Detection: Audit log review. No profile mutation without corresponding confirmation event.

### High risks (significant impact, manageable)

**Extraction accuracy degrades**
- Impact: Dutch medical terminology, code-switching, abbreviations cause failures
- Likelihood: High for edge cases
- Mitigation: Diverse eval harness. Confidence scoring. Low-confidence requires confirmation.
- Detection: Weekly eval run. Accuracy dashboard per entity type.

**Model API downtime/latency**
- Impact: Summaries and answers stop working
- Likelihood: Low but unpredictable
- Mitigation: Graceful degradation. Recording saved, retry queue. "Processing, we'll notify you."
- Detection: Health check endpoint. Alert on >5s latency or >1% errors.

**Prompt regression**
- Impact: Improvement to one worker degrades another
- Likelihood: Medium, increases with complexity
- Mitigation: Regression eval in CI. Version-controlled prompts. Model pinning.
- Detection: CI pipeline triggers full eval on any prompt change.

### Medium risks (manageable with discipline)

**Over-reliance on brain**
- Impact: Patient trusts Ditto more than they should
- Likelihood: Low in MVP
- Mitigation: Medical disclaimer everywhere. "Contact your care team." Never imperative about treatment.
- Detection: Track "could not answer" ratio.

**Scope creep**
- Impact: Timeline extends beyond 12 weeks
- Likelihood: High
- Mitigation: Slice boundaries are hard cuts. Gate criteria pass/fail. Unplanned work to backlog.
- Detection: Weekly scope review.

**Timeline too aggressive**
- Impact: Infrastructure or prompts take longer than estimated
- Likelihood: Medium
- Mitigation: Slices priority-ordered. Slice 3 is the cut candidate. Slice 1 + 2 alone is a viable product.
- Detection: Gate reviews include timeline assessment. Late Gate 1 → re-scope Slice 3.

---

## Success Metrics

### Primary (non-negotiable)

| Metric | Target | Why |
|---|---|---|
| **Suggestion tap rate** | 20%+ of summary viewers tap ≥1 suggestion | Proves brain adds value beyond summarization |
| **Profile accuracy** | 90%+ correct medications/conditions after 3+ recordings | Brain's memory must be trustworthy |
| **Answer grounding** | 100% reference source material | Zero hallucination for medical trust |

### Secondary

| Metric | Target | Why |
|---|---|---|
| **Summary latency** | <10s from recording to summary | Must feel like magic |
| **Answer speed** | <3s to first token | Streaming helps, first token matters most |
| **Elderly usability** | 8/10 heuristic items pass per screen | Primary audience is 50+ |
| **Summary revisits** | +15% within 7 days | Brain gives reason to come back |
| **Voice adoption** | 15% of active users in 30 days | Second input channel |
| **Prep utility** | 70%+ rated "helpful" internally | Must be personalized, not templated |

### Guardrails (must not decrease from current)

- Summary generation quality
- Summary generation latency
- App performance

---

## Ticket Summary by Sprint

| Sprint | Weeks | Slice | Tickets | Key deliverable |
|---|---|---|---|---|
| **S1** | 1-2 | Slice 1 | ~21 | Event bus, worker framework, recording pipeline, summary UI |
| **S2** | 3-4 | Slice 1 | ~14 | Q&A pipeline, streaming answers, eval harness, **GATE 1** |
| **S3** | 5-6 | Slice 2 | ~16 | Profile store, voice input pipeline, profile tab |
| **S4** | 7-8 | Slice 2 | ~13 | Document pipeline, conflict resolution, **GATE 2** |
| **S5** | 9-10 | Slice 3 | ~13 | Prep pipeline, sharing adaptation, preview UI |
| **S6** | 11-12 | Polish | ~14 | Integration testing, accessibility, **GATE 3**, demo prep |

**Total**: ~91 tickets across 12 weeks

### Sizing legend

- **S** (Small): Half day of work
- **M** (Medium): 1-2 days of work
- **L** (Large): 3-4 days of work

Full ticket breakdown with IDs and sizes is in [care-brain-mvp-spec.md](care-brain-mvp-spec.md#sprint-level-ticket-breakdown).

---

## References

- [Care Brain MVP Spec](care-brain-mvp-spec.md) — Full delivery specification
- [Care Brain Strategy](care-brain-strategy.md) — Approved strategic framing
- [Direction C: The Nervous System](direction-c-nervous-system.md) — Architecture spec with system prompts and schemas
- [Smart Suggestions Phase 1](care-brain-phase1-smart-suggestions.md) — Detailed feature spec for Q&A
- [Business Case](business-case.md) — Financial model, TAM, moat analysis
- [Competitive Analysis](competitive-analysis.md) — Market positioning
