# Product Feature Ideas Overview

**Date**: 2026-02-07
**Source**: BIGB Jira Product Discovery Board + pm-workspace specs
**Purpose**: Catalogue all active product feature ideas with descriptions. Identify gaps for your review.

---

## How to use this document

- **Has description**: Existing Jira description is summarized below
- **Needs description**: I've suggested one — please review and edit
- **Questions**: Where I need your input to clarify scope or intent
- Each idea links to its Jira issue for full context

---

## 1. Patient-Facing Features (Receiving/Consuming Info)

### BIGB-62: Make logging/journaling functionality (symptoms, measurements)
**Status**: Parking lot | **Category**: User-facing
**Jira**: https://dittocare.atlassian.net/browse/BIGB-62

**Existing description**: Comprehensive spec exists. Voice-first daily health check-in where users talk naturally to their phone. AI asks probing context-aware questions, extracts medical facts, creates daily notes with structured data, tracks observations over time, and generates doctor-ready summaries on demand. Targets chronically ill patients (cancer, autoimmune, complex chronic conditions). MVP: voice input, near real-time responses, basic LLM extraction, contextual memory, daily notes, timeline view, simple charts, daily reminder.

**Cross-references**: Detailed spec at `pm-workspace/ideas/voice-health-checkin/` (PRD, competitive analysis, market research, technical architecture, implementation spec, work breakdown)

---

### BIGB-44: Build dedicated medication overview and reminders
**Status**: Parking lot | **Category**: User-facing

**Existing description**: None (empty Jira doc)

**Suggested description**: A dedicated medication management feature that gives patients a clear overview of all their medications (name, dose, schedule, purpose) and sends reminders for adherence. Includes the ability to verify medication lists against prescriptions, track missed doses, and optionally alert caregivers about non-adherence. Targets patients with complex medication regimens (multiple daily meds, changing schedules).

**Questions for your input**:
- Should this be standalone or integrated with the Voice Health Check-in (BIGB-62)?
- Is medication data entry manual, or should it pull from Ditto's existing appointment/prescription data?

**Cross-references**: Part of the Activation Strategy's 3-concept initiative (`pm-workspace/ideas/activation-strategy/03-concept-selection.md`)

---

### BIGB-45: Include photos or automatic icons from medications
**Status**: Parking lot | **Category**: User-facing

**Existing description**: None

**Suggested description**: Enhance the medication overview by showing visual representations of each medication — either photos from a medication database or automatically generated icons. Helps patients visually identify their pills, reducing confusion especially for elderly patients or those with many medications.

**Questions for your input**:
- Is this about showing images in the medication overview (BIGB-44), or more broadly in event/appointment summaries?
- Should this use a medication image database (e.g., RxImage) or rely on user-uploaded photos?

---

### BIGB-46: Extract medication from photo of box
**Status**: Parking lot | **Category**: User-facing

**Existing description**: None

**Suggested description**: Allow patients to scan/photograph their medication box or packaging, and automatically extract the medication name, dosage, and other details using OCR + AI. This reduces manual data entry friction when setting up medication lists and ensures accuracy by reading directly from the source.

**Questions for your input**:
- Is this intended as an onboarding feature (quick setup of medication list) or an ongoing capture tool?

---

### BIGB-43: Include simplified medicine leaflets
**Status**: Parking lot | **Category**: User-facing (via HCP/Send)

**Existing description**: None

**Suggested description**: When a patient receives medication information through Ditto, include a simplified, patient-friendly version of the medicine leaflet (bijsluiter). Uses Ditto's AI Explainer to translate complex pharmaceutical language into understandable summaries with key information: what it's for, how to take it, common side effects, and when to contact a doctor.

**Questions for your input**:
- Is this about leaflets sent by HCPs via Ditto Send, or about patient-side medication info lookup?
- Should these be generated on-demand from existing leaflet databases, or pre-simplified and stored?

---

### BIGB-48: Create visually intuitive and appealing timeline of journey
**Status**: Parking lot | **Category**: User-facing

**Existing description**: None

**Suggested description**: Redesign the patient's health journey timeline to be visually compelling and easy to navigate. Show appointments, documents, medications, and health check-ins in a chronological, filterable view with visual cues (icons, colors, grouping). Make it easy to see the "big picture" of one's care journey at a glance.

**Questions for your input**:
- Is this a redesign of the existing event timeline, or a new supplementary view?
- Should this include non-Ditto events (manually added milestones, life events)?

**Cross-references**: Related to BIGB-65 (auto-group events into care journey)

---

### BIGB-65: Auto-group events into a care journey for easier filtering and overview
**Status**: Parking lot | **Category**: User-facing

**Existing description**: "Think about logic. Design groups, tags, filter & search."

**Suggested description**: Automatically organize events (appointments, documents, medications) into logical care journeys (e.g., "Cancer Treatment", "Cardiology Follow-up") using AI classification. Allow patients to filter, search, and tag events. Especially valuable for patients managing multiple conditions simultaneously who need to separate and navigate different care streams.

---

### BIGB-50: Load historical medical records into Ditto
**Status**: Parking lot | **Category**: User-facing

**Existing description**: None

**Suggested description**: Enable patients to import their historical medical records into Ditto, creating a comprehensive health timeline that predates their use of the app. Support uploading documents (PDFs, photos of letters), manual entry, and potentially integration with patient portals. Ditto AI processes and structures these records just like real-time events.

**Questions for your input**:
- What input formats are envisioned (PDF upload, photo scan, EPD/portal integration)?
- Should historical records be processed through the same AI Explainer pipeline?

---

### BIGB-58: Build a dedicated health document vault with key info
**Status**: Parking lot | **Category**: User-facing

**Existing description**: "Store medical records, prescriptions, and test results. Insurance cards and policy information. Emergency contact information. Advance directives."

**Cross-references**: Related to BIGB-114 (general document storage) and BIGB-98 (emergency info without login)

---

### BIGB-114: General document storage and management
**Status**: Parking lot | **Category**: User-facing

**Existing description**: "Allow users to have a library of all documents within Ditto. Be able to upload your own document, just like any cloud storage. Think about uniqueness, e.g. query with LLM or additional security."

**Questions for your input**:
- How does this differ from BIGB-58 (health document vault)? Is BIGB-58 the curated "key info" subset and BIGB-114 the general library?

---

### BIGB-98: Have emergency info available without login
**Status**: Parking lot | **Category**: User-facing

**Existing description**: "Blood type, chronics, allergies, emergency contacts."

**Suggested description (expanded)**: Make critical health information accessible from the lock screen or without full app authentication. In an emergency, first responders or bystanders could access a patient's blood type, chronic conditions, active medications, allergies, and emergency contacts. Similar to Apple's Medical ID feature but powered by Ditto's structured health data.

---

### BIGB-115: Enable chat interaction with all content
**Status**: Parking lot | **Category**: User-facing

**Existing description**: "Build ChatGPT-like interface directly within Ditto, that allows you to chat with all your included content. Build grounding and references to your own historical medical information."

---

### BIGB-29: Improve narration functionality
**Status**: Parking lot | **Category**: User-facing

**Existing description**: "Current Dutch version in iOS is with a weird accent and doesn't always work. Should be relatively small to check and validate."

**Note**: This is a quality improvement on existing functionality rather than a new feature.

---

### BIGB-56: Show preview of event photo on timeline
**Status**: Parking lot | **Category**: User-facing

**Existing description**: "For example in pregnancy journey, share pictures of echo."

**Suggested description (expanded)**: Display thumbnail previews of photos attached to events directly on the timeline view, rather than requiring users to open each event. Useful for visual milestones like ultrasound images, wound healing progress, or surgical results.

---

### BIGB-105: Allow for custom and personal blob/shape creation
**Status**: Parking lot | **Category**: User-facing (engagement)

**Existing description**: "In onboarding, allow people to create their own Ditto shape/blob based on the Ditto logo. Could be heart, Ditto pokemon, anything. Personal blob used as visual element in backgrounds. Why: engage people by making it literally 'themselves', unique personal character. Why potentially not: drives no functional value."

---

### BIGB-55: Geofencing
**Status**: Parking lot | **Category**: User-facing

**Existing description**: Detailed spec. Smart reminders to use Ditto when near healthcare locations. Auto-suggest appointment location. Notification if leaving location while still recording. All processing local on-device (no location data sent to servers). Uses geofencing APIs from Google/Apple.

**Questions for your input**:
- The Jira description includes geo-based advertisement as a use case — is that still relevant?

---

### BIGB-104: Enable scan QR to start Ditto recording
**Status**: PAUSED | **Category**: User-facing

**Existing description**: "Patients have a hard time finding the recording app on their phone. Multiple people have indicated it would be super convenient if there was a sticker/leaflet/banner with a Ditto QR on a desk that patients could scan. Solution: QR that triggers Ditto app to immediately start recording. Future: custom QR per HCP with name and organization."

---

---

## 2. HCP/Send-Side Features

### BIGB-87: Drag and drop box to make medical text understandable
**Status**: PAUSED | **Category**: HCP-facing (Send)

**Existing description**: "HCPs want as little clicks as possible. Allow users to drag any type of text or document into Ditto Send (or via copy-paste). Patient-summarization API called to 'explain' in laymen terms. Settings can be adjusted, then new version generated. AI governance panel to show reliability."

---

### BIGB-47: Generate and show QR from system tray click
**Status**: Parking lot | **Category**: HCP-facing (Send)

**Existing description**: "Pharmacists don't want to exit their normal system. Solution: Ditto Send visible in system tray. Click icon → 'Create Summary' button → takes screenshot of default screen, extracts relevant medication, makes QR code, shows in pop-up."

---

### BIGB-49: Ditto send library via Ditto specific QR for partner integration
**Status**: PAUSED | **Category**: HCP-facing (Send/Platform)

**Existing description**: "Partner with medical scribes to integrate Ditto QR in their application. Create a simple code library in a separate repository. Takes patient summary and creates Ditto QR code. Criteria: completely transparent and safe code."

---

### BIGB-52: Take picture of screen from PACS to send picture to app
**Status**: Parking lot | **Category**: HCP-facing (Send)

**Existing description**: None

**Suggested description**: Allow HCPs to photograph their PACS screen (medical imaging system) and send the captured image to the patient's Ditto app. Solves the problem of medical images being locked in hospital systems with no easy way to share with patients.

---

### BIGB-41: EHR screenshot to patient summary via OCR
**Status**: PAUSED | **Category**: HCP-facing (Send)

**Existing description**: None

**Suggested description**: Allow HCPs to capture screenshots from their EHR (Electronic Health Record) system, which Ditto then processes via OCR to extract structured medical data and generate a patient-friendly summary. Reduces friction for HCPs who can't easily copy text from their EHR systems.

**Cross-references**: Related to BIGB-87 (drag and drop text simplification)

---

### BIGB-66: More flexibility in deletion of events
**Status**: Parking lot | **Category**: HCP-facing (Send)

**Existing description**: "User preference adjustments of auto-delete after 14 days. Manual deletion of a single event."

---

### BIGB-59: Allow consumer to see summary on website rather than app
**Status**: Parking lot | **Category**: HCP-facing (Send) / User-facing

**Existing description**: "App downloads are generally low in medtech. Give patients option to see short summary on a private webpage. Patient receives text/email with link to private webpage showing summary + app download opportunity. Important for investable datapoints — if app downloads are low but webpage clicks are good, Ditto still has compelling data."

---

### BIGB-72: Find angle to boost 'Samen Beslissen' with Ditto Send
**Status**: Parking lot | **Category**: HCP-facing (Send)

**Existing description**: None

**Suggested description**: Explore how Ditto Send can support "Samen Beslissen" (Shared Decision Making) — a key Dutch healthcare initiative where patients and HCPs make treatment decisions together. Ditto's patient-friendly summaries could help patients better understand their options, enabling more informed conversations.

**Questions for your input**:
- Is this about a specific feature (e.g., decision-support templates) or a positioning/marketing angle for Ditto Send?
- Are there specific 'Samen Beslissen' tools or frameworks to integrate with?

---

### BIGB-84: Update UI based on new branding
**Status**: PAUSED | **Category**: HCP-facing (Send)

**Existing description**: None

**Suggested description**: Update the Ditto Send (HCP-facing) user interface to reflect Ditto's updated brand identity — colors, typography, iconography, and visual language.

**Note**: This is a design refresh, not a new feature. Excluding from user research matching.

---

---

## 3. Care Circle / Social Features

### BIGB-42: Share complete journey/account with family and/or caregivers
**Status**: Discovery | **Category**: Social/Sharing

**Existing description**: None

**Suggested description**: Enable patients to share their complete health journey (all events, summaries, medications, documents) with designated family members and caregivers through the Care Circle. Caregivers get a single source of truth rather than fragmented updates via WhatsApp.

**Cross-references**: Detailed spec at `pm-workspace/ideas/care-circle-v2/` — the Care Circle V2 initiative with invitation cards, personal context, short summaries, reactions, support cards, help offers, profile page, and timeline overview.

---

### BIGB-37: Sharing and finding similar patients and their journey
**Status**: Parking lot | **Category**: Social/Peers

**Existing description**: "Option to find peers that have a similar health journey or disease. Could be either anonymous or even more social as a way to reach out to 'Lotgenoten' (fellow sufferers)."

---

### pm-workspace: Care Circle V2 ("Polarsteps for Healthcare")
**Status**: Discover & Define | **Category**: Social/Sharing

**Existing description**: Full spec exists. Transforms how patients share their health journey with loved ones through meaningful assets (cards, updates, profiles) rather than ephemeral WhatsApp messages. Key features: invitation cards (Spotify-style), personal context notes, short summaries, emoji reactions, support cards, help offers, profile page, timeline overview.

**Cross-references**: `pm-workspace/ideas/care-circle-v2/` (README, design decisions, meeting transcript, 6 user flows)

---

### pm-workspace: DPMA-1964 Enhanced Sharing Personalization
**Status**: Feature Specification | **Category**: Social/Sharing

**Existing description**: Full spec exists. Allows patients to personalize what they share from appointments and control who receives it. P1: personal messaging layer, share history per appointment, edit & delete shares. P2: selective recipient selection. P3: different updates to different people, image attachments.

**Cross-references**: `pm-workspace/ideas/DPMA-1964-enhanced-sharing-personalization.md`

---

### pm-workspace: Activation Strategy (3-Concept Initiative)
**Status**: Concept Selection Complete | **Category**: Meta-initiative

**Existing description**: Strategic initiative to drive daily engagement for both patients and caregivers. Three complementary concepts: (1) Voice Health Check-In (→ BIGB-62), (2) Medication Reminders (→ BIGB-44), (3) Care Circle Pulse — daily status exchange + support gestures between patients and caregivers. Creates 3-5 daily touchpoints for patients and 1-2 for each caregiver.

**Cross-references**: `pm-workspace/ideas/activation-strategy/` (user research synthesis, market research, concept selection)

---

---

## 4. AI & Intelligence Features

### BIGB-61: Add terminology database for LLM context
**Status**: Parking lot | **Category**: AI/Platform

**Existing description**: "High degree of abbreviations in medical lingo, differs per discipline. Wrong interpretation leads to wrong output. Solution: build central repo/database with terminology, add RAG-step to extract abbreviations and medical lingo. Creates consistency in output and an appealing partnership asset."

---

### BIGB-93: Show governance report of output from Ditto AI
**Status**: Parking lot | **Category**: AI/Platform

**Existing description**: "When making medical text understandable, demonstrate fit-for-purpose through AI governance framework. Structure: fit for patient (understandability, relevance) and fit for physician (reliability, clinical risk). Use Langfuse evaluators on two levels: global on golden dataset, local on specific API input."

---

### BIGB-106: Enable HCP cross-check on Ditto AI output at a premium
**Status**: Parking lot | **Category**: AI/Platform

**Existing description**: "Service where people can get HCP feedback X times/year, or more with credits. Not second-opinion, but human-oversight check on AI output."

---

### BIGB-13: Integrate with existing ambient documentation
**Status**: Parking lot | **Category**: AI/Platform

**Existing description**: Template content only (Atlassian exploration template). No actual problem/solution definition filled in.

**Suggested description**: Integrate Ditto with existing ambient clinical documentation tools (e.g., Nuance DAX, Abridge, DeepScribe) that automatically generate clinical notes from doctor-patient conversations. Instead of competing with these tools, leverage their output as input for Ditto's patient-facing summaries.

**Questions for your input**:
- Which specific ambient documentation tools are you considering integrating with?
- Is this about using ambient doc output as Ditto Send input, or about Ditto replacing ambient doc tools?

---

---

## 5. Platform/Technical Features

### BIGB-92: Provide Ditto 'Explainer' AI service over API to partners
**Status**: Parking lot | **Category**: Platform/B2B

**Existing description**: "Partners already have apps. Most ChatGPT wrappers aren't reliable enough for medical data. Solution: API service accepting medical text, passing through Explainer Service to return patient-level summary. Partners pay per use. Provide transparency on governance: overall pipeline report based on golden dataset, specific report per output if requested."

---

### BIGB-40: Add encryption with best-practice protocol for key sharing
**Status**: Parking lot | **Category**: Platform/Security

**Existing description**: None

**Suggested description**: Implement end-to-end encryption for data shared between HCPs and patients via Ditto, using industry best-practice key exchange protocols. Ensures that even Ditto cannot read the medical data in transit or at rest — critical for healthcare data trust and compliance.

---

### BIGB-85: User verification from external partner
**Status**: Discovery | **Category**: Platform/Identity

**Existing description**: None

**Suggested description**: Enable external partners to verify user identity within the Ditto app, ensuring the right patient receives the right medical information. Required for secure data exchange with partner systems.

**Cross-references**: Related to BIGB-86 (server-side verification)

---

### BIGB-86: User verification between external partner and Ditto app
**Status**: Discovery | **Category**: Platform/Identity

**Existing description**: None

**Suggested description**: Server-side implementation of identity verification between external partner systems and the Ditto app. Establishes a trusted link so partners can send data to verified patients.

---

### BIGB-89: KYC provider for 3rd parties
**Status**: PAUSED | **Category**: Platform/Identity

**Existing description**: "Partners need patient identity data. Getting this from Ditto (with patient consent) is faster than asking during phone calls. Solution: expose API for partners to request patient data (name). Backend flows designed in Miro."

---

---

## Summary

| Category | Count | With description | Needs description |
|----------|-------|-----------------|-------------------|
| Patient-Facing | 16 | 12 | 4 |
| HCP/Send-Side | 7 | 5 | 2 |
| Care Circle/Social | 5 | 5 | 0 |
| AI & Intelligence | 4 | 3 | 1 |
| Platform/Technical | 5 | 2 | 3 |
| **Total** | **37** | **27** | **10** |

### Ideas needing your description input
1. BIGB-44: Medication overview and reminders (empty doc)
2. BIGB-45: Photos/icons for medications
3. BIGB-46: Extract medication from photo of box
4. BIGB-43: Simplified medicine leaflets
5. BIGB-48: Visual timeline of journey
6. BIGB-50: Load historical medical records
7. BIGB-52: PACS screen photo to app
8. BIGB-41: EHR screenshot to patient summary via OCR
9. BIGB-13: Integrate with ambient documentation (template only)
10. BIGB-40: Encryption with key sharing protocol

### Ideas with open questions (7)
- BIGB-44, BIGB-45, BIGB-43, BIGB-48, BIGB-50, BIGB-55, BIGB-72, BIGB-114, BIGB-13
