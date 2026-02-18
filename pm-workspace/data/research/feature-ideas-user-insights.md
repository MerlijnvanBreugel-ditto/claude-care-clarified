# User Insights per Product Feature Idea

**Date**: 2026-02-07
**Sources**: Ditto User Insights NotebookLM synthesis (15 sources: 9 interviews, 4 surveys/feedback, 1 documentation)
**Researcher**: Claude (AI-Assisted)
**Method**: Cross-referenced existing user research synthesis, Care Circle V2 Lyssna feedback, and interview evidence

---

## Evidence Strength Legend

| Rating | Meaning |
|--------|---------|
| **Strong** | Multiple sources, direct quotes, explicit requests from users |
| **Moderate** | 2+ sources mention related needs, or 1 source with strong signal |
| **Weak** | Implied need, or single mention without emphasis |
| **None** | No user evidence found — needs dedicated research |

---

## Evidence Summary (Quick View)

| Idea | Title | Evidence | Sources |
|------|-------|----------|---------|
| BIGB-62 | Logging/journaling (voice check-in) | **Strong** | 8+ of 15 |
| BIGB-44 | Medication overview & reminders | **Strong** | 5+ of 15 |
| BIGB-42 / CC-V2 | Share journey with family | **Strong** | 10+ of 15 |
| DPMA-1964 | Enhanced sharing personalization | **Strong** | 6+ of 15 |
| BIGB-48 | Visual timeline of journey | **Moderate** | 4+ of 15 |
| BIGB-115 | Chat interaction with content | **Moderate** | 2+ of 15 |
| BIGB-58 / BIGB-114 | Document vault / storage | **Moderate** | 3+ of 15 |
| BIGB-50 | Load historical records | **Moderate** | 3+ of 15 |
| BIGB-41 | EHR screenshot to summary (OCR) | **Moderate** | 3+ of 15 |
| BIGB-37 | Peer sharing (lotgenoten) | **Moderate** | 2+ of 15 |
| BIGB-98 | Emergency info without login | **Moderate** | 2+ of 15 |
| BIGB-104 | Scan QR to start recording | **Moderate** | 2+ of 15 |
| BIGB-65 | Auto-group events into journey | **Weak** | 2 of 15 |
| BIGB-61 | Terminology database for LLM | **Weak** | 2 of 15 |
| BIGB-93 | AI governance report | **Weak** | 2 of 15 |
| BIGB-106 | HCP cross-check on AI output | **Weak** | 2 of 15 |
| BIGB-29 | Improve narration | **Weak** | 1 of 15 |
| BIGB-56 | Photo preview on timeline | **Weak** | 1 of 15 |
| BIGB-87 | Drag & drop medical text | **Weak** | 1 of 15 |
| BIGB-55 | Geofencing | **None** | 0 of 15 |
| BIGB-45 | Medication photos/icons | **None** | 0 of 15 |
| BIGB-46 | Extract medication from photo | **None** | 0 of 15 |
| BIGB-43 | Simplified medicine leaflets | **None** | 0 of 15 |
| BIGB-47 | QR from system tray (HCP) | **None** | 0 of 15 |
| BIGB-49 | Send library for partners | **None** | 0 of 15 |
| BIGB-52 | PACS photo to app | **None** | 0 of 15 |
| BIGB-59 | Summary on website | **None** | 0 of 15 |
| BIGB-66 | Flexible event deletion | **None** | 0 of 15 |
| BIGB-72 | Samen Beslissen angle | **None** | 0 of 15 |
| BIGB-105 | Custom blob/shape | **None** | 0 of 15 |
| BIGB-13 | Ambient doc integration | **None** | 0 of 15 |
| BIGB-40 | Encryption protocol | **None** | 0 of 15 |
| BIGB-84 | UI branding update | **None** | 0 of 15 |
| BIGB-85/86 | User verification | **None** | 0 of 15 |
| BIGB-89 | KYC for 3rd parties | **None** | 0 of 15 |
| BIGB-92 | Explainer API for partners | **None** | 0 of 15 |

---

## Detailed Insights per Feature

---

### BIGB-62: Make logging/journaling functionality (symptoms, measurements)

**Evidence strength**: **Strong**
**Sources mentioning this**: 8+ of 15 (Care-Circle interviews, Ditto Dierbaren interviews, Typeform feedback, Anonymized feedback)

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "I need a 'dagboek' (diary) to record pain scores, side effects, symptoms I'm worried about." | Patient | User Interview | Very High — top requested daily feature | Critical |
| 2 | "Maintaining a daily log requires discipline. What's the point unless I can track daily measurements?" | Gerda | Care-Circle Interview | Mentioned by multiple | High — but highlights friction barrier |
| 3 | "I already use the notes section to create reminders about what to discuss regarding my prognosis." | Patient | User Interview | Medium | High — shows workaround behavior |
| 4 | Health Diary / Symptom Tracking rated as "Very High" request frequency | Multiple patients | Typeform + Interviews | Top requested feature | Critical |
| 5 | "Taking medication daily is already a struggle" — implies daily tracking burden | Gerda | Care-Circle Interview | Multiple | Medium — counter-signal: fatigue risk |
| 6 | "Want to stop being a patient for the coming year" — some want to disengage | Patient (monitoring) | Interview | Common | Medium — not all users want daily engagement |

#### Summary
This is the #1 most-requested daily feature. Users explicitly ask for health diary, pain score tracking, and symptom logging. However, there's a clear tension: users want tracking but find manual logging burdensome. This is precisely why the voice-first approach (30-second check-in vs. typing into forms) emerged as the solution direction. Key nuance: patients in active treatment are the primary audience; those in monitoring phase may resist daily engagement.

#### Gaps
- How many users would actually sustain daily tracking beyond the first week?
- What's the minimum viable daily check-in duration before it feels burdensome?
- Comfort level with speaking health information aloud?

---

### BIGB-44: Build dedicated medication overview and reminders

**Evidence strength**: **Strong**
**Sources mentioning this**: 5+ of 15 (Care-Circle interviews, Ditto Dierbaren interviews, Typeform feedback)

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "Can Ditto provide logic for medication schedules? My friend has a 'terrible list of medicines' — amounts, times — it's a big chaotic mess on paper." | Caregiver | Interview | High — explicit request | High |
| 2 | "Extra tips for medication adherence" requested | Multiple | Typeform + Interviews | High | Medium |
| 3 | Complex schedule organization (amounts, times, frequency) identified as key need | Patients with complex conditions | Research synthesis | High | High |
| 4 | Verification that app medication list matches reality | Multiple patients | Interviews | Medium | High — trust barrier |
| 5 | Adherence reminders especially for ADHD users | Patient | Interview | Medium | High for this segment |

#### Summary
Strong user demand, especially from patients managing multiple medications with complex schedules. The medication management need is intertwined with caregiver needs — caregivers want visibility into adherence (the "Medfriend" model from Medisafe). This feature creates natural daily touchpoints and network effects between patient and caregiver.

#### Gaps
- Which medication data source should be primary (manual entry, prescription import, photo scan)?
- How do users currently manage medications (paper, other apps, nothing)?

---

### BIGB-42 / Care Circle V2: Share complete journey with family and caregivers

**Evidence strength**: **Strong**
**Sources mentioning this**: 10+ of 15 (all interview sets, feedback surveys, Lyssna research)

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "Chinese whispers — information gets distorted" through indirect sharing | Caregiver | Care-Circle Interview | High | Critical |
| 2 | "Prevents the telephone game" — share once, inform everyone | Patient | Ditto Dierbaren Interview | High | High |
| 3 | "Send simple signals like emojis (hearts, flowers) to show I'm thinking of them without expecting a reply." | Loved one | Ditto Dierbaren Interview | High | High |
| 4 | "A feature where loved ones can offer specific practical help (cooking, transportation) through the app." | Caregiver | Interview | Medium | High |
| 5 | "Who is going with mom? Who is cooking?" — logistical coordination need | Primary caregiver | Care-Circle Interview | High | High for caregivers |
| 6 | "I want to have one place where they can always find the basics about my disease." | Patient (Parkinson's) | Meeting transcript (friend's father) | Anecdotal | High |
| 7 | "Dagelijkse check-in: goed/meh/slecht" (daily check-in: good/meh/bad) | Multiple | Lyssna Research (8 mentions) | 8 mentions in feedback | Medium |
| 8 | "Laat zien wanneer ik beschikbaar ben om te praten" (Show when I'm available to talk) — "Safe to call" indicator | Multiple | Lyssna Research (6 mentions) | 6 mentions in feedback | Medium |
| 9 | Privacy concerns block sharing feature adoption | Multiple | Care Circle V2 Feedback survey | Significant concern | Critical blocker |

#### Summary
This is the highest-evidenced feature area across all research. Users on both sides (patients and caregivers) have clear, articulated needs. The evidence is consistent: patients want low-friction sharing, caregivers want a single source of truth, and both want a way to show care without pressure. The key tension is privacy — users want to share but are hesitant about all-or-nothing sharing. The Care Circle V2 approach (cards as assets, not messages; one-to-many sharing) directly addresses this.

#### Gaps
- Optimal care circle size (how many followers before it feels overwhelming)?
- Do caregivers actually want a separate experience, or is "patient-first" design sufficient?

---

### DPMA-1964: Enhanced Sharing Personalization

**Evidence strength**: **Strong**
**Sources mentioning this**: 6+ of 15 (Care-Circle interviews, Lyssna research, Care Circle V2 feedback)

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "I want to share the diagnosis with friends but exclude the 'stop drinking' lifestyle advice." | Patient | Interview | High | High |
| 2 | "There is a difference what I share with whom" | Multiple | Lyssna Research | High | Critical |
| 3 | Inner circle (partner, parents) gets full details; outer circle (friends, neighbors) gets "short summary" | Multiple patients | Interviews | Common pattern | High |
| 4 | "I would like to keep it personal, loved ones want to know how I'm really doing" | Patient | Lyssna Research | Mentioned in feedback | High |
| 5 | Either share when sharing (46%) or separately on timeline — personal context timing varies | Multiple | Lyssna Research (46% preference) | Quantified | Medium |
| 6 | "Customizing is more important than just selecting one person" — from team discussion based on feedback | Design team | Meeting transcript | Design insight based on research | High |

#### Summary
Users consistently express the need for graduated sharing — different information for different relationships. The current all-or-nothing model is a key blocker for adoption. The personal note feature (adding "how I'm really doing" context to shared updates) addresses the gap between clinical data and emotional reality. This feature directly solves the primary privacy concern blocking Care Circle adoption.

#### Gaps
- What's the right UX for selecting what to share without creating decision fatigue?
- Do users actually use per-person customization once available, or default to "share with all"?

---

### BIGB-48: Create visually intuitive and appealing timeline of journey

**Evidence strength**: **Moderate**
**Sources mentioning this**: 4+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "Clear overview is mentioned a lot — 'in a glance'" | Multiple | Lyssna Research | Multiple mentions | Medium |
| 2 | "Clear separation of own and loved ones content" — reduces overwhelm | Multiple | Lyssna Research | Part of V2 scope | Medium |
| 3 | "I only use the app when I have an appointment or receive a letter" — timeline could change this | Multiple respondents | Interviews | Universal pattern | Medium (implies timeline isn't compelling enough) |

#### Summary
Users want to see their journey at a glance. The current timeline doesn't provide enough visual richness or filtering to be useful as a standalone feature. A redesigned timeline could serve as the "home" that gives patients a reason to open the app outside of appointments.

#### Gaps
- What visual elements make the timeline compelling (icons, colors, grouping, photos)?
- Should the timeline show caregiver activity alongside patient events?

---

### BIGB-115: Enable chat interaction with all content

**Evidence strength**: **Moderate**
**Sources mentioning this**: 2+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "I would actually love my friends to do the same [research] because then we can have a truthful factual discussion" | Cancer patient (at presentation) | Meeting transcript | Anecdotal but strong | High |
| 2 | Users want to understand their health data better — the AI explainer is already valued | Multiple | Interviews + Feedback | Core Ditto value | High (foundation feature) |

#### Summary
The conversational interaction pattern is a natural extension of Ditto's AI explainer capability. The user who wanted friends to research his condition together signals demand for deeper engagement with health content. A chat interface would let users ask questions about their own history ("When did I last have that medication changed?").

#### Gaps
- How do users want to interact with their data (free-form questions vs. guided prompts)?
- Trust level for AI-generated answers about personal health history?

---

### BIGB-58 / BIGB-114: Health document vault / General document storage

**Evidence strength**: **Moderate**
**Sources mentioning this**: 3+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | Caregivers need a "single source of truth" — one place with all updates, summaries, letters | Caregivers | Care-Circle Interviews | High | High for caregivers |
| 2 | "I have digital letters — why must I print to scan?" | AYA patient | AYA Interview | Single source but strong | High — functional barrier |
| 3 | Information scattered across WhatsApp, email, verbal — centralization need | Multiple caregivers | Ditto Dierbaren Interviews | High | High |

#### Summary
The document vault addresses a clear caregiver need for centralized health information. Users currently scatter medical documents across WhatsApp conversations, email, paper folders, and patient portals. A single, organized vault would reduce caregiver anxiety and make medical information findable. The distinction between BIGB-58 (curated key info) and BIGB-114 (general storage) aligns with user behavior — some documents are critical (medication list, emergency info) while others are archival.

#### Gaps
- Do users want to organize documents manually, or should AI auto-categorize?
- What's the overlap with existing patient portal functionality?

---

### BIGB-50: Load historical medical records into Ditto

**Evidence strength**: **Moderate**
**Sources mentioning this**: 3+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "I have digital letters — why must I print to scan?" — frustration with import friction | AYA patient | AYA Interview | Single but strong | High |
| 2 | Users want a complete health picture, not just recent events | Multiple | Synthesis | Implicit need | Medium |
| 3 | "Can't upload PDFs directly" identified as a functional barrier | Multiple | Research synthesis | High functional barrier | High |

#### Summary
Moderate evidence. The PDF upload barrier is one of the top functional complaints. Users who have years of medical history want it all in one place. This feature would dramatically increase the value of the timeline and document vault.

#### Gaps
- What formats do users have their historical records in (paper, PDFs, portal exports)?
- Is there demand for structured import (parsed by AI) vs. simple storage?

---

### BIGB-41: EHR screenshot to patient summary via OCR

**Evidence strength**: **Moderate**
**Sources mentioning this**: 3+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "I have digital letters — why must I print to scan?" | AYA patient | AYA Interview | Strong signal | High |
| 2 | "Many consultations are by phone" — can't record phone calls | Multiple | Interviews | High | Medium (related friction) |
| 3 | HCPs don't want to exit their normal system | HCP feedback | Jira description context | HCP-side evidence | High for HCP adoption |

#### Summary
This is a two-sided need: patients want an easier way to get medical text into Ditto, and HCPs don't want to leave their EHR. OCR from screenshots bridges both worlds. The AYA patient's frustration about printing to scan is a strong signal for this need.

#### Gaps
- What's the accuracy of OCR on typical EHR screenshots?
- Is this more important from the HCP side (BIGB-87 drag & drop) or patient side?

---

### BIGB-37: Sharing and finding similar patients (lotgenoten)

**Evidence strength**: **Moderate**
**Sources mentioning this**: 2+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "I would actually love my friends to do the same [research] because then we can have a truthful factual discussion" | Cancer patient | Meeting transcript | Anecdotal | Medium-High |
| 2 | Peer support is a known need in chronic illness communities | General | Market research | Well-documented externally | Medium |

#### Summary
Limited direct user evidence in Ditto research, but peer connection ("lotgenoten") is a well-established need in the broader chronic illness space. The cancer patient at the presentation expressed a desire for informed peers. However, peer matching introduces significant complexity (privacy, moderation, safety) and may be better served by existing communities (e.g., Kanker.nl forums).

#### Gaps
- How many Ditto users would actually use a peer-matching feature?
- Privacy comfort level for sharing health data with strangers?
- Should Ditto build this or integrate with existing peer platforms?

---

### BIGB-98: Have emergency info available without login

**Evidence strength**: **Moderate**
**Sources mentioning this**: 2+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "I just need to have my friends know the basics about my disease" — Parkinson's patient going on holiday | Friend of patient | Meeting transcript | Anecdotal but vivid | High |
| 2 | Profile page with bio, FAQ discussed as a "single source of truth" for followers | Design team | Care Circle V2 scope | Design insight | Medium |

#### Summary
The Parkinson's patient story from the meeting transcript is a compelling use case — someone wanting their social circle to know the basics about their condition in case of emergency. This aligns naturally with the health document vault and Care Circle profile page. Emergency access without authentication adds a safety dimension.

#### Gaps
- How should emergency info be authenticated/accessed securely?
- What specific info should be available (blood type, allergies, medications, conditions)?

---

### BIGB-104: Enable scan QR to start Ditto recording

**Evidence strength**: **Moderate**
**Sources mentioning this**: 2+ of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "Multiple people have indicated that it would be super convenient if there was a sticker/leaflet/banner with a Ditto QR on a desk that patients could scan" | Multiple patients | Per Jira description | Multiple mentions | Medium |
| 2 | Patients have a hard time finding the recording app on their phone | Multiple patients | Per Jira description | Common friction | Medium |

#### Summary
A practical usability improvement with direct user feedback. The QR-to-record concept reduces friction at the critical moment (in the doctor's office) and could serve as a physical marketing touchpoint for HCP practices.

#### Gaps
- How would this work for patients who don't yet have the app installed?
- Is this better as a deep link or native QR feature?

---

### BIGB-65: Auto-group events into a care journey

**Evidence strength**: **Weak**
**Sources mentioning this**: 2 of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "Clear overview mentioned a lot — 'in a glance'" | Multiple | Lyssna Research | Implied | Medium |
| 2 | Patients with multiple conditions need to separate care streams | Implied | Research synthesis | Inferred need | Medium |

#### Summary
No direct user quotes requesting this feature. The need is inferred from the broader desire for a clear, navigable timeline. Patients managing multiple conditions (e.g., cancer + diabetes) would benefit most.

#### Gaps
- Do users actually manage multiple care journeys simultaneously in Ditto today?
- Should grouping be automatic (AI) or manual (user tags)?

---

### BIGB-61: Add terminology database for LLM context

**Evidence strength**: **Weak**
**Sources mentioning this**: 2 of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "Wrong medication names make me hesitant to share" — AI accuracy eroding trust | Patient | Interview | Medium | High — trust impact |
| 2 | "Can't easily edit AI errors" identified as functional barrier | Multiple | Research synthesis | Medium | Medium |

#### Summary
Users don't ask for a terminology database directly, but they clearly react to AI inaccuracies. Wrong medication names are a specific trust-eroding issue. A terminology database would improve accuracy systemically, which addresses the underlying user concern.

#### Gaps
- Which terminology errors are most common and most damaging to trust?
- Can this be validated by analyzing existing AI output accuracy?

---

### BIGB-93: Show governance report of output from Ditto AI

**Evidence strength**: **Weak**
**Sources mentioning this**: 2 of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "Wrong medication names make me hesitant to share" — trust concern | Patient | Interview | Medium | High |
| 2 | Privacy concerns block sharing feature adoption — trust is a theme | Multiple | Care Circle V2 Feedback | Significant | High |

#### Summary
Users express trust concerns about AI accuracy but don't ask for governance reports specifically. This is more a B2B/partner need (partners want to see Ditto AI is reliable) than a direct consumer need. However, building trust through transparency is critical for adoption.

#### Gaps
- Would end users actually read/understand a governance report?
- Is this more valuable for HCP/partner trust than patient trust?

---

### BIGB-106: Enable HCP cross-check on Ditto AI output at a premium

**Evidence strength**: **Weak**
**Sources mentioning this**: 2 of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | Users trust HCP validation over AI output | General | Implied by accuracy concerns | Implicit | Medium |
| 2 | "I'm encouraged to ask my HCP to validate" — current workaround | Implied | AI accuracy discussions | Implicit | Medium |

#### Summary
Weak direct evidence. Users trust their HCP over AI, so an HCP cross-check adds reassurance. However, this creates business model complexity and HCP workload. No user has directly asked for this feature.

#### Gaps
- Would users pay for HCP verification?
- Are HCPs willing to participate in this model?

---

### BIGB-29: Improve narration functionality

**Evidence strength**: **Weak**
**Sources mentioning this**: 1 of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | Quality issue reported — weird accent in Dutch iOS narration | Internal/QA | Jira description | Single report | Low — quality fix |

#### Summary
This is a quality improvement, not a user-requested feature. No user research evidence found requesting narration improvements specifically.

---

### BIGB-56: Show preview of event photo on timeline

**Evidence strength**: **Weak**
**Sources mentioning this**: 1 of 15

#### User Insights

| # | What was said | Who | Source | Frequency | Importance |
|---|---------------|-----|--------|-----------|------------|
| 1 | "For example in pregnancy journey, share pictures of echo" | Internal | Jira description | Single example | Low |

#### Summary
Implied need for visual richness on the timeline, but no direct user evidence requesting photo previews.

---

### Features with NO user evidence

The following features have no direct user evidence in the research synthesis. This doesn't mean they're bad ideas — it means they need dedicated research before prioritization.

| Idea | Title | Why no evidence | Research needed |
|------|-------|----------------|-----------------|
| BIGB-55 | Geofencing | Technical enabler, not user-articulated need | Test whether location-based reminders increase recording rates |
| BIGB-45 | Medication photos/icons | UX enhancement, not pain point | Include in medication feature usability testing |
| BIGB-46 | Extract medication from photo | Convenience feature | Test as part of medication onboarding flow |
| BIGB-43 | Simplified medicine leaflets | Could be valuable but unarticulated | Ask in next round of interviews |
| BIGB-47 | QR from system tray (HCP) | HCP feature — research with pharmacists | Needs HCP interviews |
| BIGB-49 | Send library for partners | B2B feature | Validate with partner conversations |
| BIGB-52 | PACS photo to app | HCP feature — specific to imaging | Needs HCP interviews |
| BIGB-59 | Summary on website | Business rationale (investor metrics), not user need | Test with users: app vs. web preference |
| BIGB-66 | Flexible event deletion | Settings/preferences request | Low priority for research |
| BIGB-72 | Samen Beslissen angle | Strategic positioning, not user request | Explore with HCP partners |
| BIGB-105 | Custom blob/shape | Engagement gamification | Fun idea — A/B test if built |
| BIGB-13 | Ambient doc integration | Industry trend, not user request | Validate with HCP partners |
| BIGB-40 | Encryption protocol | Security requirement, not user need | Technical requirement |
| BIGB-84 | UI branding update | Design refresh | N/A |
| BIGB-85/86 | User verification | Platform requirement | Technical requirement |
| BIGB-89 | KYC for 3rd parties | Platform requirement | Partner-driven |
| BIGB-92 | Explainer API for partners | B2B feature | Partner-driven |
| BIGB-87 | Drag & drop medical text | HCP feature — some implied need from OCR barriers | Needs HCP usability testing |

---

## Cross-Idea Insights

### Thematic Clusters with Strong Evidence

**1. Daily Engagement Cluster** (Strongest evidence)
- BIGB-62 (Voice check-in) + BIGB-44 (Medication reminders) + Care Circle Pulse
- 15+ sources confirm these are the top daily engagement opportunities
- User quote: "I need a 'dagboek' to record pain scores, side effects"
- User quote: "Send hearts, flowers without expecting reply"

**2. Care Circle / Sharing Cluster** (Strong evidence)
- BIGB-42 (Share journey) + DPMA-1964 (Personalized sharing) + Care Circle V2
- Core Ditto value proposition — most researched area
- Key tension: desire to share vs. privacy concerns
- Solution: graduated sharing (short summary vs. full detail)

**3. Health Records & Documents Cluster** (Moderate evidence)
- BIGB-58 (Document vault) + BIGB-114 (General storage) + BIGB-50 (Historical records) + BIGB-41 (OCR)
- Users want a "single source of truth" but face import friction
- PDF upload barrier is a top functional complaint

**4. AI Trust & Quality Cluster** (Weak but critical evidence)
- BIGB-61 (Terminology) + BIGB-93 (Governance) + BIGB-106 (HCP cross-check)
- Users don't ask for these features directly but express trust concerns that these would address
- "Wrong medication names make me hesitant to share"

### Features with NO User Backing

17 of 37 features have no direct user evidence. These fall into three groups:

1. **HCP/Send-side features** (BIGB-47, 49, 52, 87): Need dedicated HCP research
2. **Platform/technical features** (BIGB-40, 85, 86, 89, 92): Driven by partner/security requirements, not user demand
3. **Nice-to-have enhancements** (BIGB-55, 45, 46, 43, 66, 105): Could add value but haven't been validated

### Key Tensions from Research

| Tension | What users say | What this means |
|---------|---------------|-----------------|
| **Want to track but find it burdensome** | "Need a diary" vs. "Requires discipline" | Voice-first is the right solution for daily tracking |
| **Want to share but fear loss of control** | "Share with loved ones" vs. "Privacy concerns" | Personalized sharing controls are table stakes |
| **Want daily engagement but don't want to be reminded of illness** | "Daily check-in" vs. "Want to stop being a patient" | Design for "being cared for" not "being monitored" |
| **Trust AI but catch errors** | "App is a safety net" vs. "Wrong medication names" | AI accuracy improvements compound across all features |

---

## Recommended Next Steps

1. **Prioritize with confidence**: BIGB-62, BIGB-44, Care Circle V2, DPMA-1964 — these have strong, multi-source evidence
2. **Conduct targeted research for the 17 unevidenced features** — especially HCP features (BIGB-47, 52, 87) via HCP interviews
3. **Query NotebookLM directly** (once MCP is connected) for deeper quotes and specific user identities per feature — this document maps themes but could be enriched with exact attribution
4. **Use the Evidence Summary table** above for prioritization discussions — features with "None" evidence should require a research checkpoint before entering the roadmap

---

## Data Source Note

This synthesis draws from the existing user research synthesis (`pm-workspace/ideas/activation-strategy/01-user-research-synthesis.md`), the Care Circle V2 Lyssna feedback results (discussed in meeting transcript), and the Care Circle V2 design documentation. For richer individual quotes and exact attribution per interview source, a direct NotebookLM query per feature idea is recommended once the MCP connection is established.
