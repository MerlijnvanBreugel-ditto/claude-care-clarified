# Idea: Voice-First Daily Health Check-in

**Jira Reference**: BIGB-62
**Status**: Discovery Complete
**Date**: 2026-01-31

---

## Phase 1a: High-Level Description

### Problem Statement

**Which problem are we solving, for whom, and why is this important to solve?**

People in healthcare journeys need to track their health but currently face major friction:
- They don't track at all
- They forget to track regularly
- They use different apps for different aspects (medication, symptoms, vitals)
- They resort to paper which gets lost or disorganized

This matters because tracking health data helps people manage their own health better AND prepares them for doctor visits - giving them ownership and agency in their care. The problem is that existing tools (medication reminder apps, etc.) require too much manual work and are fragmented across multiple places.

**For whom**: Chronically ill patients and people in severe health trajectories - such as cancer patients, those managing autoimmune conditions, or people going through intensive treatment. These patients have the highest need for consistent tracking and the most to gain from better preparation for doctor visits.

### Feature Description

A voice-first daily health check-in that:
- Users talk to their phone naturally (no typing/clicking)
- AI asks probing questions based on context ("You mentioned headaches last week - how are those?")
- Responds in near real-time to feel conversational and alive
- Automatically extracts medical facts and observations from voice
- Creates a daily note with structured data
- Tracks observations over time (severity, frequency, patterns)
- Generates doctor-ready summaries on demand
- Enables sharing updates with loved ones/caregivers

**The "wow" factor**: The AI truly understands what you're saying and remembers context from previous conversations. When it asks "How's that nausea you mentioned on Tuesday?" users feel genuinely heard and understood - not like they're talking to a dumb form.

**Key insight**: Voice-first dramatically lowers friction compared to manual typing/clicking, enabling higher frequency and making health tracking feel effortless.

### Expected Impact on North Star Metric

**Primary impacts**:
- **Engagement/Retention**: Daily check-in creates a natural habit loop, increasing usage frequency from occasional to daily. Voice interaction is lower friction, reducing drop-off.
- **Activation**: Voice-first gets users to their first value moment faster - they can log their first health data in seconds versus minutes of manual entry.

**Secondary impacts**:
- **Acquisition**: High wow factor - voice logging feels magical and is highly shareable/demo-able
- **Referral**: Sharing feature creates natural viral loop when users share updates with family

### Validation Approach

Competitor analysis + user interviews:
- Research existing voice health logging solutions (what works, what doesn't)
- Interview 10-15 chronically ill patients about current behaviors, willingness to do daily voice check-ins, value of doctor summaries
- Create low-fidelity prototype for concept testing

### Risks & Concerns

- Not all chronically ill patients are comfortable with voice interfaces - especially older patients
- Privacy concerns about speaking health information out loud
- Voice input quality/accuracy might be inconsistent
- Daily check-ins might feel burdensome if users have nothing to report
- Medical data extraction is complex - errors could undermine trust
- Retention might drop after novelty wears off
- May not be differentiated enough from existing voice assistants

---

## Phase 1b: Early Experiment

### Technical Spike
Test voice-to-medical-data extraction quality with existing LLMs (GPT-4, Claude). Can we reliably extract structured medical observations from natural speech? Critically - can we do this fast enough to feel real-time (<2 seconds response time)?

### Value Experiment
Manual concierge test - have 5-10 chronically ill patients send daily voice notes for 2 weeks. Manually process and return summaries. Measure:
- Completion rate (how many days do they actually do it?)
- Quality of extracted data
- User perceived value
- Does the "wow" factor emerge - do they feel understood?
- Would they pay for this?

---

## Phase 2: Specification

### Context

During user research, we consistently hear that people in healthcare journeys struggle to track their health despite knowing it's important. Current solutions require too much manual effort - typing symptoms, remembering to log vitals, managing multiple apps. Meanwhile, voice interfaces have become mainstream and natural for users (Siri, Alexa, etc.).

The convergence of powerful LLMs and ubiquitous voice interfaces creates a unique moment to reimagine health tracking - especially for chronically ill patients who have the most to gain from consistent tracking.

### User Profile

**Primary**: Chronically ill patients and people in severe health trajectories:
- Cancer patients undergoing treatment or monitoring
- People with chronic autoimmune conditions (Crohn's, lupus, MS, etc.)
- Those managing complex chronic conditions (diabetes, heart disease, chronic pain)
- Patients in intensive treatment protocols
- Caregivers tracking for seriously ill loved ones

**Key characteristics**:
- High need for consistent health tracking
- Frequent doctor visits where preparation matters
- Complex symptom patterns that benefit from longitudinal tracking
- Motivated to track but exhausted by current manual tools
- May vary in tech-savviness and comfort with voice interfaces
- Want to feel prepared and empowered at doctor visits

### Core Flow

1. **Daily prompt**: User receives reminder for daily health check-in (push notification)
2. **Voice conversation**: User talks naturally to their phone - no forms or typing
3. **AI responds in near real-time** (<2 seconds) to feel truly conversational
4. **AI asks contextual questions** based on previous mentions
5. **"Wow" moment**: User feels genuinely understood
6. **Automatic extraction**: AI extracts medical observations (symptoms, severity, medications, vitals, mood)
7. **Daily note created**: Structured data + natural language summary
8. **Timeline view**: Users can see trends over time
9. **Doctor summaries**: On-demand generation of visit-ready summaries
10. **Sharing**: Optional auto-updates to loved ones/caregivers

### Key Differentiators

- Voice-first with near real-time responses (feels alive, not robotic)
- Deep contextual memory - remembers what you mentioned before
- Creates "wow it really understands me" moments through intelligent follow-ups
- Automatic structuring (no manual categorization)
- All-in-one (replaces fragmented apps)
- AI-generated insights and summaries

### Technical Specifications

**Input**:
- Voice recording (30-180 seconds typical)
- Triggered by reminder or user-initiated
- Near real-time responses (<2 seconds)

**Processing**:
- Streaming speech-to-text transcription
- LLM extraction of structured medical data:
  - Symptoms (type, severity 1-10, frequency, duration)
  - Medications (name, dose, time, adherence)
  - Vitals (BP, HR, weight, temperature)
  - Mood/energy (qualitative assessment)
  - Activities/triggers
- Entity resolution (linking to previous entries)
- Context retrieval (past week/month)
- Contextual follow-up question generation

**Output**:
- Real-time conversational responses
- Daily note (natural language + structured data)
- Timeline view of observations
- Charts/visualizations of trends
- On-demand doctor summaries
- Optional sharing with contacts

### MVP Scope

**INCLUDED**:
- Voice input (user talks, we record and transcribe)
- Near real-time responses (<2 seconds)
- Basic LLM extraction (symptoms, severity, medications)
- Contextual memory - AI remembers past mentions
- Contextual follow-up questions (1-2 per session)
- Daily notes generated from voice
- Timeline view showing observations over time
- Simple charts (frequency/severity over time)
- Daily reminder notification

**EXCLUDED (v2)**:
- Doctor summaries
- Sharing with loved ones
- Advanced visualizations/insights
- Wearable integrations
- Multi-language support

### Success Metrics

- 60% of users who start a check-in complete it
- 30% of activated users check in 5+ times in first week
- 80%+ report the feature is "very valuable"
- 70%+ report experiencing "wow" moments (feeling understood)
- 40% 7-day retention

### Timeline

6-8 weeks to ship MVP to beta users (chronically ill patient cohort)
