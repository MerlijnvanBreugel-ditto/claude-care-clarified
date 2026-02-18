# Product Requirements Document: Voice Health Check-in

**Version**: 2.0
**Date**: 2026-02-05
**Status**: Ready for Review
**Priority**: P0 - Strategic Initiative

---

## Executive Summary

**Voice Health Check-in** transforms daily health tracking from a chore into a 30-second conversation. Patients speak naturally to their phone, and AI extracts structured health data across body, mind, actions, and context — building a longitudinal health record that reveals patterns, prepares appointments, and keeps loved ones informed.

**Why now**: Voice AI has matured (<2s latency, 94% accuracy). No competitor combines voice-first + contextual memory + chronic illness focus + caregiver sharing. The market gap is clear and timing is optimal.

---

## 1. Problem Statement

### The Problem

Chronically ill patients need to track their health but don't:

| Barrier | Impact |
|---------|--------|
| **Manual entry fatigue** | Forms and tapping exhaust patients already depleted |
| **Fragmented tools** | Symptoms in one app, meds in another, mood in a third |
| **No contextual memory** | Apps don't remember yesterday, let alone last week |
| **Doctor visits unprepared** | "I don't remember when the headaches started" |
| **Loved ones uninformed** | Repeating status updates to 10 people is exhausting |

### Who Has This Problem

| Segment | Size (US) | Urgency |
|---------|-----------|---------|
| **Cancer patients** (active treatment) | 2M new/year, 20M survivors | Critical - complex side effects, frequent appointments |
| **Autoimmune patients** | 15-50M | High - flare patterns, trigger identification |
| **Multi-chronic patients** | 54M with 2+ conditions | High - coordination nightmare |
| **Caregivers tracking for others** | 53M unpaid caregivers | High - proxy tracking needs |

### Evidence

| Source | Finding |
|--------|---------|
| User research | "Maintaining a daily diary requires discipline" — Gerda |
| User research | "I forget 50% of what happens" — multiple patients |
| Competitive gap | No voice-first chronic illness tracker exists |
| Market data | Voice AI healthcare market: 37.85% CAGR through 2035 |

---

## 2. Solution Overview

### Core Concept

A daily voice conversation that feels like talking to a thoughtful friend who remembers everything:

```
MORNING NOTIFICATION
        ↓
   "How are you?"
        ↓
 PATIENT SPEAKS (30-90s)
 "Had a rough night, headache
  came back around 3am, took two
  ibuprofen, feeling a bit better
  now but tired..."
        ↓
 AI RESPONDS (<2 seconds)
 "That's the third headache this
  week. Is it the same location
  as Tuesday?"
        ↓
 PATIENT CONTINUES
        ↓
 STRUCTURED DATA EXTRACTED
 • Symptom: headache, 3am onset
 • Medication: ibuprofen, 2 pills
 • Mood: tired
 • Pattern: 3rd this week
        ↓
 DAILY NOTE CREATED
        ↓
 TRENDS UPDATED
        ↓
 CARE CIRCLE NOTIFIED (optional)
```

### Key Differentiators

| Differentiator | Why It Matters |
|----------------|----------------|
| **Voice-first design** | Speak, don't tap. Critical for fatigue/brain fog |
| **<2 second responses** | Feels like real conversation, not waiting for AI |
| **Contextual memory** | "How's that headache from Tuesday?" — remembers everything |
| **Multi-dimensional extraction** | Body + Mind + Actions + Context in one conversation |
| **Not a medical device** | Wellness companion, not diagnostic tool |
| **60+ accessible** | Large text, voice-only path, no complexity |

---

## 3. Extraction Categories

The AI extracts structured data across four dimensions:

### Body (Symptoms & Vitals)
- Symptoms: type, location, severity (1-10), frequency, duration
- Vitals: blood pressure, heart rate, temperature, weight
- Physical state: energy level, sleep quality, appetite

### Mind (Emotions & Cognition)
- Mood: emotional state, intensity
- Cognitive: brain fog, focus, memory
- Mental health: anxiety level, stress, motivation

### Actions (Behaviors & Interventions)
- Medications: name, dose, timing, adherence
- Exercise: type, duration, intensity
- Treatments: therapy sessions, medical procedures
- Self-care: meditation, rest, social activities

### Context (Environment & Triggers)
- Sleep: hours, quality, disturbances
- Social: interactions, support, isolation
- Environment: weather sensitivity, travel
- Life events: stress triggers, celebrations

---

## 4. Core Features (MVP)

### P0 - Must Have

| Feature | Description |
|---------|-------------|
| **Voice check-in** | Natural conversation, 30-90 seconds typical |
| **Real-time transcription** | See words as you speak |
| **AI follow-up questions** | 1-2 contextual questions per session |
| **Multi-category extraction** | Body, Mind, Actions, Context |
| **Daily note generation** | Structured + narrative summary |
| **Timeline view** | See history by day/week/month |
| **Simple trend charts** | Symptom frequency/severity over time |
| **Daily reminder** | Configurable notification |

### P1 - Should Have (v1.1)

| Feature | Description |
|---------|-------------|
| **Pattern detection** | "Headaches increase on Mondays" |
| **Doctor summary** | Generate appointment-ready report |
| **Care Circle sharing** | Push daily status to loved ones |
| **Voice-only mode** | Complete check-in without looking at screen |

### P2 - Could Have (v2.0)

| Feature | Description |
|---------|-------------|
| **Caregiver proxy entry** | Log for elderly/incapacitated loved one |
| **Social post mode** | "Thinking of you" style shareable updates |
| **Wearable integration** | Auto-import sleep, heart rate, activity |
| **Multi-language** | Dutch, German, Spanish support |

---

## 5. Design Direction

Based on expert panel review (Jony Ive, Paula Scher, Mike Kresch, Alan Dye, Alex Schleifer), the selected direction is:

### Direction C: Immersive Wellness

**Concept**: Full-screen breathing orb that represents AI attention. Minimal UI. The orb IS the interface.

**Panel verdict**: 4.2/5 — "The future of health UX"

**Key principles**:
- Remove navigation during check-in (immersive moment)
- Breathing orb animation syncs with voice activity
- Warm gradient background (off-white base)
- Minimal text — visual language does emotional work
- Serif typography for humanity

**Accessibility requirements**:
- VoiceOver describes orb state meaningfully
- Reduce Motion option disables animation
- Large text alternative available
- Haptic feedback for state changes

---

## 6. User Experience

### Target Experience Qualities

| Quality | Target |
|---------|--------|
| **Effortless** | Complete in <60 seconds |
| **Trusted** | "This app gets me" |
| **Calm** | No anxiety from health tracking |
| **Accessible** | Usable by 60+ with vision/dexterity challenges |
| **Reliable** | Works every time, extracts accurately |

### The "Wow" Moment

When the AI asks:

> "You mentioned nausea on Tuesday and again Thursday. Is it related to your new medication?"

The patient thinks: "This actually remembers and understands me."

---

## 7. Regulatory & Trust Positioning

### What We Are

- **Wellness companion** for daily health awareness
- **Personal health record** owned by the user
- **Communication tool** for care circles
- **Preparation assistant** for medical appointments

### What We Are NOT

- **Diagnostic tool** — we don't diagnose conditions
- **Medical device** — we don't require FDA clearance
- **Treatment recommender** — we don't suggest interventions
- **Emergency system** — we don't handle crisis situations

### Guardrails

| Guardrail | Implementation |
|-----------|----------------|
| No diagnosis | AI never suggests "you might have X" |
| No treatment advice | AI never says "you should take Y" |
| Crisis escalation | Detect distress, suggest professional help |
| Data sovereignty | Users own and can delete all data |
| Transparency | Clear explanation of AI limitations |

---

## 8. Success Metrics

### Primary (North Star)

| Metric | Current | Target | Rationale |
|--------|---------|--------|-----------|
| **7-day retention** | N/A | 40%+ | Habit formation indicator |
| **Weekly check-in frequency** | N/A | 5+ per week | Daily engagement goal |

### Secondary

| Metric | Target | Measurement |
|--------|--------|-------------|
| Check-in completion rate | 60%+ | Started → Finished |
| "Wow" moment rate | 70%+ | Survey: "Felt understood" |
| Perceived value | 80%+ | Survey: "Very valuable" |
| Extraction accuracy | 90%+ | Human audit sample |
| Response latency | <2 seconds | P95 AI response time |

### Guardrails (Must Not Decrease)

- Core app retention (existing features)
- Care Circle engagement rate
- App Store rating

---

## 9. Target Users

### Primary: Sarah, 47, Fibromyalgia + IBS

**Context**: Diagnosed 5 years ago. Good days and bad days. Sees rheumatologist quarterly.

**Behaviors**:
- Tried Bearable but stopped — too much tapping on bad days
- Keeps mental notes, forgets by appointment time
- Husband wants to help but doesn't know how

**Needs**:
- Track without energy expenditure
- Show doctor patterns, not just "I've been tired"
- Let husband see status without asking

**Quote**: "On bad days I can barely hold my phone. I can always talk."

### Secondary: Michael, 64, Diabetes + Hypertension

**Context**: Managing two chronic conditions. Takes 6 medications. Daughter helps coordinate care remotely.

**Behaviors**:
- Uses paper notebook, loses it
- Forgets which days were good/bad
- Doesn't text well, prefers voice

**Needs**:
- Simple voice interface, big text
- Share updates with daughter without technology hassle
- Remember medication timing and effects

**Quote**: "My daughter set up my phone. If she can set this up too, I'll use it."

---

## 10. Competitive Positioning

### Positioning Statement

> **For** chronically ill patients exhausted by manual health tracking,
> **Voice Health Check-in is** a conversational AI companion
> **That** remembers your health journey and asks the right follow-up questions,
> **Unlike** symptom trackers that require tapping and forget you between visits.
> **We** transform tracking from a chore into a 30-second daily conversation.

### Competitive Matrix

| Capability | Bearable | Ada Health | Wysa | Alexa Health | **Ditto Voice** |
|------------|----------|------------|------|--------------|-----------------|
| Voice-first | No | No | Limited | Yes | **Yes** |
| Chronic illness focus | Yes | No | Mental only | No | **Yes** |
| Contextual memory | No | No | Limited | No | **Yes** |
| <2s response | N/A | Slow | Moderate | Fast | **<2s** |
| Caregiver sharing | Reports | No | No | No | **Real-time** |
| Multi-category extraction | Manual | Manual | No | Limited | **Automatic** |

---

## 11. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Voice accuracy issues** | Medium | High | Confirmation step, edit capability |
| **Extraction errors** | Medium | High | Human-in-loop review for ambiguous cases |
| **Older users struggle** | Medium | Medium | Onboarding guidance, voice-only path |
| **Privacy concerns** | Medium | Medium | Transparent data policies, local option |
| **Habit doesn't form** | Medium | High | Smart reminders, streak mechanics |
| **Regulatory creep** | Low | High | Clear wellness positioning, legal review |

---

## 12. Open Questions

- [ ] What's the minimum viable check-in duration? (Target: 30s)
- [ ] Should we support text-only fallback for voice-averse users?
- [ ] How do we handle multi-language households?
- [ ] What's the right notification timing/frequency?
- [ ] Should we integrate with Apple Health / Google Fit from day 1?

---

## 13. References

- [Competitive Analysis](./competitive-analysis.md)
- [Market Research](./market-research.md)
- [User Research Synthesis](../activation-strategy/01-user-research-synthesis.md)
- [Design Panel Consensus](./mockups/panel-consensus.md)
- [Idea Specification](./idea-spec.md)

---

**Document Control**
- Created: 2026-02-05
- Last Updated: 2026-02-05
- Owner: Product Management
- Reviewers: Engineering Lead, Design Lead, Clinical Advisor
