# Recording Permission Support — Reducing the Fear Barrier

**Status**: Draft — Awaiting Feedback
**Date**: 2026-03-16
**Mode**: Explore
**Origin**: User profiling canvas exercise — identified as unaddressed problem for elderly patients
**Prior art**: Existed as idea on BIGB board (doctor explainer sheet)

---

## Problem

Older patients are afraid to ask their doctor for permission to record. This fear of authority is a documented barrier from user interviews — it prevents them from ever using Ditto's core feature, even after installing.

The existing idea on the BIGB board was a sheet/explainer for the doctor explaining why the patient wants to record. This spec expands on that concept.

## Who this affects

| Persona | Impact | Why |
|---|---|---|
| Elderly / Low-Digital | High | Fear of authority is strongest here. Often don't know their rights. |
| Language Barrier | High | Additional anxiety from language/cultural gap with provider |
| Neurodegenerative | Medium | Caregiver often handles the conversation — may face pushback from provider |
| All new users | Low-Medium | First-time recorders across all segments report some hesitation |

## Current user behavior

1. **Avoid recording** — simply don't use the core feature, making the app useless
2. **Record secretly** — creates anxiety and guilt, undermines the experience
3. **Ask awkwardly** — "Can I record this?" without context, which can feel confrontational
4. **Bring a family member** — the family member handles the ask (proxy confidence)

## Proposed solution directions

### Direction A: Doctor Information Sheet (original BIGB idea)
A printable or shareable one-pager explaining:
- Why the patient wants to record (to remember, not to sue)
- What Ditto does (AI summary, not raw recording storage)
- Privacy: recording is processed and deleted, not stored as audio
- Legal context: patients have the right to record in NL

**Delivery**: PDF in app, shareable link, or physical leaflet via HCP partnerships.

### Direction B: In-App Permission Script
A guided conversation starter shown before the first recording:
- "Here's what you can say to your doctor:"
- "I use an app called Ditto to help me remember our conversation. It creates a summary for me. Is that okay?"
- Option to customize (formal/informal, Dutch/English)
- One-tap share to show the doctor on screen

### Direction C: QR-Triggered Doctor Context
Extension of BIGB-104 (QR to start recording). When a QR sticker is at the doctor's office:
- The practice has already opted in (no permission needed)
- Patient scans → recording starts with confidence
- This eliminates the permission conversation entirely for participating practices

### Direction D: Ditto Send Partnership Angle
For practices that already use Ditto Send:
- The doctor already knows Ditto
- Patient recording is a natural extension
- The practice could display "We support Ditto recording" signage

## Recommendation

**Start with B (In-App Permission Script)** — zero external dependencies, addresses the moment of anxiety directly. Complement with A (Doctor Sheet) as a downloadable asset.

C and D are longer-term and depend on HCP partnerships scaling.

## Open questions for Merlijn

1. Did the original BIGB idea have a ticket number? Should this replace or extend it?
2. Is there data on how many users record secretly vs. ask permission vs. don't record at all?
3. Should the permission script be part of onboarding or triggered before the first recording?
4. Any legal nuance beyond "patients can record in NL" that we should address?
5. Is there appetite to make this part of the HCP partnership pitch (practices displaying "Ditto-friendly" signage)?

---

## RISCE (preliminary)

| Dimension | Score | Rationale |
|---|---|---|
| Reach | 3 | Primarily elderly + language barrier segments, not all users |
| Impact | 4 | Removes a complete blocker — these users currently get zero value |
| Strategic | 3 | Supports activation and trust, but not a north star mover |
| Confidence | 3 | Behavioral barrier is documented but solution hasn't been tested |
| Effort | 5 | Direction B is very low effort (copy + UI) |
| **RISCE** | **540** | |

---

*Feedback? (optional)*
1. *Yes, let me share*
2. *Not now / later*
3. *Not needed — you were perfect*
