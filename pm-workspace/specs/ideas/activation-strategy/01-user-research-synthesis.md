# User Research Synthesis: Activation Strategy

**Researcher**: Claude (AI-Assisted)
**Date**: 2026-02-02
**Version**: 1.0
**Source**: Ditto User Insights NotebookLM (ID: 00a28a7f-ac6c-4f37-8ff4-81ee4dcdf8c2)

---

## Executive Summary

Ditto's activation challenge stems from its fundamentally episodic nature—users only engage during medical appointments, which may be weeks or months apart. User research reveals strong unmet needs for **daily health tracking**, **medication management**, and **low-friction caregiver communication** that could drive daily engagement. Caregivers specifically need a "single source of truth" and logistical coordination tools. The highest-impact opportunity is creating engagement loops between appointments through symptom tracking, medication reminders, and Care Circle touchpoints.

### The User Need
Users want to feel supported and stay connected to their care network between appointments, but currently have no compelling reason to open the app daily.

### The Recommendation
Build features that create daily touchpoints: health check-ins, medication reminders, and lightweight social engagement (emoji support, help coordination) for the Care Circle.

### The Evidence
15+ user interviews and surveys confirm: daily health diary, medication adherence, and low-friction caregiver interaction are the top-requested daily engagement features.

---

## 1. Research Inputs Summary

### 1.1 Sources Analyzed
| Source | Type | Volume | Key Finding |
|--------|------|--------|-------------|
| Care Circle Interviews (Gerda, Wil Jan, Peter, R1, R2) | Qualitative | 5 | Caregivers need filtered sharing + logistical coordination |
| Ditto Dierbaren Interviews (Aisha, Gert, John, Marieke) | Qualitative | 4 | Loved ones want single source of truth, low-burden updates |
| AYA Interview | Qualitative | 1 | Younger patients want digital-first features (PDF upload) |
| Care Circle V2 Feedback | Quantitative | N/A | Privacy concerns block sharing feature adoption |
| Typeform App Feedback | Mixed | N/A | Daily tracking + medication features most requested |
| Anonymized Feedback | Mixed | N/A | Technical friction + episodic usage patterns |

### 1.2 Key User Segments
| Segment | Characteristics | Primary Need |
|---------|----------------|--------------|
| **Patients (Active Treatment)** | Regular appointments, high engagement during care episodes | Memory support, information translation |
| **Patients (Monitoring)** | Infrequent appointments, want to disengage | Minimal friction, optional daily tracking |
| **Primary Caregivers** | Partners, children managing care | Logistical coordination, verified information |
| **Extended Network** | Friends, distant family | Brief updates, low-pressure support |

---

## 2. Barriers to Daily Engagement

### 2.1 Root Cause: Episodic App Design
The app is fundamentally designed around medical events that don't occur daily:

| Barrier | Frequency | User Evidence |
|---------|-----------|---------------|
| **Event-driven usage** | Universal | "No need yet" / "When applicable" |
| **Desire to disengage** | Common | "Want to stop being a patient" |
| **No daily value** | High | "Requires discipline" without daily features |

### 2.2 Key User Quotes

> "I want to stop being a patient for the coming year."
> — Patient (monitoring phase)

> "Maintaining a daily log requires discipline. What's the point unless I can track daily measurements?"
> — Gerda, Interview

> "I only use the app when I have an appointment or receive a letter."
> — Multiple respondents

### 2.3 Functional Barriers Compounding the Issue
| Barrier | Impact | User Request |
|---------|--------|--------------|
| Can't upload PDFs directly | High | "I have digital letters—why must I print to scan?" |
| Can't record phone calls | High | "Many consultations are by phone" |
| Can't easily edit AI errors | Medium | "Wrong medication names make me hesitant to share" |

---

## 3. What Creates Motivation to Return

### 3.1 Current Triggers (Event-Based)
| Trigger | Type | Engagement |
|---------|------|------------|
| **Upcoming appointment** | External | Opens app to prepare/check details |
| **Post-appointment** | Internal | Views AI summary, checks accuracy |
| **Received medical letter** | External | Scans to translate medical jargon |
| **Care Circle notification** | Social | Opens to see shared update |

### 3.2 Value Users Receive
| Value Pillar | Description | Quote |
|--------------|-------------|-------|
| **Cognitive Support** | Memory aid—"I forget 50% of what's said" | "The app is a safety net" |
| **Social Efficiency** | Share once, inform everyone | "Prevents the telephone game" |
| **Emotional Peace** | "Rust" (peace) during appointments | "I don't have to memorize everything" |

### 3.3 Key Insight: The "Care Circle Loop"
The strongest current engagement pattern is social:
1. Patient shares summary → triggers notifications
2. Loved ones open app to view update
3. Loved ones may respond with support

**Opportunity**: Amplify this loop with daily lightweight interactions (not tied to appointments).

---

## 4. Needs Between Appointments

### 4.1 Gap Period Needs
Users explicitly identified needs during the time between medical visits:

| Need | Frequency | Feature Request |
|------|-----------|-----------------|
| **Store questions for next visit** | High | "Write down questions as they arise" |
| **Track symptoms/measurements** | High | "Diary for pain scores, side effects" |
| **Medication reminders** | Medium | "Tips for medication adherence" |
| **Calendar sync** | High | "Sync with Outlook/Google Calendar" |
| **Automatic follow-up reminders** | Medium | "Remind me to check complaint in 2 weeks" |

### 4.2 Key User Quotes

> "I need a 'dagboek' (diary) to record pain scores, side effects, symptoms I'm worried about."
> — User Interview

> "Can Ditto provide logic for medication schedules? My friend has a 'terrible list of medicines'—amounts, times—it's a big chaotic mess on paper."
> — Interview

> "I already use the notes section to create reminders about what to discuss regarding my prognosis."
> — User Interview

---

## 5. Daily Feature Requests (Explicit)

### 5.1 Most-Requested Daily Features
| Feature | Request Frequency | User Segment |
|---------|------------------|--------------|
| **Health Diary / Symptom Tracking** | Very High | Patients |
| **Medication Management** | High | Patients (complex conditions) |
| **Actionable Reminders** | Medium-High | Patients with ADHD, complex care |
| **Low-friction social gestures** | High | Caregivers + Patients |
| **Shared family agenda** | High | Primary caregivers |

### 5.2 Health Diary & Symptom Tracking
Users want to log:
- Pain scores
- Side effects
- Symptoms they're worried about
- Measurements (blood pressure, weight, etc.)
- "Own feeling about their condition"

### 5.3 Medication Management
Needs identified:
- **Complex schedule organization** (amounts, times, frequency)
- **Verification** that app medication list matches reality
- **Adherence reminders** (especially for ADHD users)

### 5.4 Low-Friction Social Engagement
> "Send simple signals like emojis (hearts, flowers) to show I'm thinking of them without expecting a reply."
> — Loved One Interview

> "A feature where loved ones can offer specific practical help (cooking, transportation) through the app."
> — User Interview

---

## 6. Caregiver-Specific Needs

### 6.1 Core Caregiver Needs
| Need | Description | Quote |
|------|-------------|-------|
| **Single Source of Truth** | One place with all updates, summaries, letters | "Chinese whispers—information gets distorted" |
| **Filtered Sharing** | Choose what to share with whom | "Share diagnosis but not lifestyle advice" |
| **Logistical Coordination** | Shared agenda, task management | "Who is going with mom? Who is cooking?" |
| **Proxy Access** | Manage care for elderly/less digital parents | "I set up the app for my mother" |
| **Low-pressure engagement** | Show support without demanding response | "Send a flower emoji, no reply needed" |

### 6.2 Information Tiering Request
Users strongly requested ability to share different levels of detail:
- **Inner Circle (partner, parents)**: Full details
- **Outer Circle (friends, neighbors)**: "Short summary" or bullet points

> "I want to share the diagnosis with friends but exclude the 'stop drinking' lifestyle advice."
> — Patient Interview

### 6.3 Caregiver Pain Points
| Pain Point | Impact | Solution Direction |
|------------|--------|-------------------|
| **Inaccurate information from patient** | High | Caregiver access to verified summaries |
| **Information scattered (WhatsApp, email, verbal)** | High | Centralized timeline |
| **Burden of asking "how did it go?"** | Medium | Push updates eliminate need to ask |
| **Coordinating logistics manually** | High | Shared agenda/task feature |

---

## 7. Opportunity Analysis: Daily Engagement Features

### 7.1 Opportunity Prioritization
| Feature Concept | Impact | User Evidence | Fit with Ditto |
|-----------------|--------|---------------|----------------|
| **Voice Health Check-In** | High | Diary + symptom tracking requests | High (extends recording capability) |
| **Medication Reminders** | High | Explicit requests, complex schedules | High (natural extension) |
| **Care Circle Pulse** | High | Low-friction engagement requests | High (amplifies sharing) |
| **Symptom/Measurement Tracking** | Medium-High | Diary requests | Medium (requires new UI) |
| **Shared Family Agenda** | Medium | Caregiver coordination needs | Medium (scope increase) |

### 7.2 The "Loved Ones Multiplier"
Current state: 1 patient → N caregivers as passive recipients

**Opportunity**: Create engagement for caregivers independent of patient actions:
- Daily "thinking of you" gestures
- Offer help (cooking, transport) via app
- View (filtered) health trends
- Coordinate logistics

### 7.3 Counterpoint: Discipline Fatigue
> "Maintaining a daily diary requires a lot of discipline. Taking medication daily is already a struggle."
> — Gerda, Interview

**Implication**: Daily features must be extremely low-friction. Voice-first (30 second check-in) is promising; complex forms are not.

---

## 8. Recommendations for Activation Strategy

### 8.1 Primary Recommendations

#### 1. Voice Health Check-In (Confirmed)
**Rationale**: Extends Ditto's core voice capability; enables symptom/mood tracking without typing; AI can structure unstructured voice input.

**User Evidence**:
- "Diary for pain scores, side effects" requested
- Voice recording is already trusted/valued
- Low friction = higher adherence

#### 2. Medication Reminders (Confirmed)
**Rationale**: Explicit user requests; high daily frequency; caregiver visibility creates network effects.

**User Evidence**:
- "Terrible list of medicines—amounts, times"
- "Extra tips for medication adherence"
- Caregiver need for verified information

#### 3. Care Circle Engagement (Candidate for 3rd Concept)
**Rationale**: Creates daily touchpoints for caregivers (larger user base); enables "loved ones multiplier"; requested emoji/help features.

**User Evidence**:
- "Send hearts, flowers without expecting reply"
- "Offer specific practical help through the app"
- "Who is going with mom?"

### 8.2 What NOT to Build
Based on user evidence, avoid:
- Complex daily logging forms (discipline fatigue)
- Features that require doctor participation (resistance documented)
- All-or-nothing sharing (privacy concerns)

### 8.3 Success Metrics (Suggested)
| Metric | Current | Target |
|--------|---------|--------|
| Weekly Active Users | ~35% | 60%+ |
| Care Circle Share Rate | 35-40% | 55%+ |
| Daily App Opens | Low | 3+ per week |
| Caregiver DAU | Unknown | Track |

---

## 9. Knowledge Gaps

### 9.1 Questions for Further Research
| Question | Method | Priority |
|----------|--------|----------|
| What's the minimum viable daily check-in? | Prototype testing | High |
| Which medications do users struggle most with? | Survey | Medium |
| Do caregivers want a separate app experience? | Interview | Medium |
| What triggers caregiver app abandonment? | Analytics | High |

---

## Appendix: Source Documents

- AYA Interview
- Care Circle Interviews: Gerda, Wil Jan, Peter, R1, R2
- Ditto Dierbaren Interviews: Aisha, Gert, John, Marieke
- Anonymized Feedback (260130)
- Care Circle V2 Feedback Results
- Care Network (Zorg voor naaste) Results
- Typeform App Feedback
- DG-Product Canonical Description

---

## Key Takeaways

1. **The app is episodic by design**—users have no daily reason to return
2. **Daily features are explicitly requested**: health diary, medication management, low-friction social gestures
3. **Caregivers are an underserved, high-potential segment** with distinct needs for coordination and filtered access
4. **Voice-first is the right approach** for daily engagement—reduces discipline burden
5. **The Care Circle loop is the engagement engine**—amplify it with daily touchpoints
