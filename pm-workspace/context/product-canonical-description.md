# Product Canonical Description
> Source: DG-Product Canonical Description-101225-141554.pdf
> Version: December 2025 | Status: Living Document

## 1. Problem Statement

### Who Experiences This Problem
- **Elderly patients with care needs**: Comprehension difficulties, often attend alone, struggle to relay info to family
- **Caring family members (mantelzorgers)**: 5 million in NL, receive fragmented second-hand health information
- **Patients with serious illnesses**: Cancer, complex conditions, multiple specialists, overwhelming information
- **Patients facing language barriers**: Migrants, non-native Dutch speakers struggling with medical terminology
- **Pregnant women and partners**: Positive use case with intrinsic sharing eagerness (95% share pregnancy updates, >50% with 6+ people), high info load

### Why This Problem Remains Unsolved
- Healthcare systems designed for providers, not patients (EHRs serve clinicians, portals are fragmented)
- Privacy regulations create sharing barriers (GDPR, accessing care info on behalf of others)
- Technology gap: transforming medical conversations into understandable, shareable info requires AI capabilities only recently possible

### Jobs to Be Done
1. **Understand**: "Help me understand what the doctor just told me"
2. **Remember**: "I need to recall what was discussed"
3. **Share**: "I want to keep my family informed without repeating myself"
4. **Organize**: "I need one place for all my healthcare information"
5. **Prepare**: "Help me know what to ask at my next appointment"
6. **Support**: "I want to help my loved one manage their care"

## 2. Product Scope

**DittoCare** is a privacy-first mobile app that transforms medical confusion into clarity.
- Mission: "We clarify and connect care journeys for you and your loved ones"
- Positioning: "Polarsteps of healthcare"
- Value prop: "Care. Clarified."
- Explicitly **not a medical device**. Patient support tool — no medical advice, diagnosis, or replacement for professional care.

## 3. Core Features

### Capture
- **Voice Recording**: Record medical conversations (with consent), audio stored locally, encrypted
- **Document Scanning & Upload**: Scan/upload discharge papers, prescriptions, medical letters; AI extracts and simplifies
- **Medical Scribe Integrations**: QR code-based sharing from provider AI scribes to patient app

### Clarify
- **Transcription**: Medical conversations → text, optimized for Dutch medical terminology
- **Summarization**: AI rewrites at B1 Dutch reading level; sections: what was discussed, diagnoses, medications, next steps; explains medical terms
- **Translation**: Dutch, English, Turkish, Arabic (in development: Farsi, Polish, German)
- **Quality Validation**: Medication names cross-checked with Dutch national pharmacy databases, multiple safety layers

### Connect (Care Circle)
- Share summaries with support network; choose what to share (toggle sections, exclude sensitive info)
- Add personal messages; share via invite links (WhatsApp, Signal, email)
- Followers/following with approval-required follow requests
- Per-event privacy; make events private anytime; remove followers to revoke access
- Followers cannot see each other
- Notifications for follow requests, acceptances, new shared events

## 4. Supporting Features

### Everything in One Place
- Healthcare timeline with structured overview
- Manual event creation for unrecorded appointments
- Organization/provider tagging per event
- File attachments; build your own health record

### Onboarding
- Funnel: Install → Caretype selection → Consent → FaceID → Registration → First event
- Registration rate: ~35-40% of first opens
- Video tutorials, user stories, care context selection (dynamic based on situation)

### Security & Privacy
- Biometric authentication (Face ID / fingerprint)
- Works without device lock
- TLS encryption in transit
- End-to-end encryption for Care Circle
- Local storage (medical data on device, not servers)
- EU data processing (AI processing in EU, deleted within minutes)

## 5. Future Direction

- **More Languages**: German for Q1 international expansion; more summarization languages
- **Social Care Circle**: Engagement/reactions, sharing context, personal messages, follower responses
- **Care Journey Visualization**: Better UX for displaying journeys, visual representation of conditions/treatments over time
- **Beyond Text Summaries**: Narration (text-to-speech), visual summaries (infographics), images illustrating trajectory

## 6. Current Metrics (December 2025)
| Metric | Value |
|---|---|
| Registered users | ~35,000 |
| MAU (creating summaries) | 679 |
| WAU | 217 |
| App Store rating | 4.7 |
| User satisfaction | 98% |
| Share rate per summary | 35-40% |
