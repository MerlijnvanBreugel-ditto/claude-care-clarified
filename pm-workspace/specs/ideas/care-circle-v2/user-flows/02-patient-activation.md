# Flow 2: Patient Activation

## Overview
**Goal**: Patient downloads → understands value → adds first appointment → invites followers

**Success Criteria**: Patient adds appointment within first session

**Primary Persona**: Someone managing their own health journey who wants to keep loved ones informed

---

## Flow Diagram

```
[Download] → [Onboarding (patient path)]
                              ↓
                    [Smart Home Screen]
                    (personalized for patient)
                              ↓
         ┌──────────────────────────────────────┐
         │  PHASE A: Understanding Value        │
         │  • "Get a summary of your next apt"  │
         │  • Social proof                      │
         │  • Why sharing relieves burden       │
         └──────────────────────────────────────┘
                              ↓
         ┌──────────────────────────────────────┐
         │  PHASE B: Commitment/Intention       │
         │  "Why share with loved ones?"        │
         │  □ Keep them informed                │
         │  □ I need support/help               │
         │  □ Less "how did it go?" questions   │
         └──────────────────────────────────────┘
                              ↓
                    [Add First Appointment]
                              ↓
                    [Set Up Profile (optional)]
                    (can defer to after first share)
                              ↓
                    [Invite Followers]
```

---

## Screens

### Screen 1: Role Selection
**Entry point after app download**

| Element | Content |
|---------|---------|
| Header | "Welcome to Ditto" |
| Subheader | "How would you like to use Ditto?" |
| Option A | **"I'm a patient"** - I want to share my health journey with loved ones |
| Option B | **"I'm following someone"** - I want to support someone's health journey |

**Interaction**: Tapping "I'm a patient" → Screen 2

---

### Screen 2: Core Value Proposition
**Why Ditto exists for patients**

| Element | Content |
|---------|---------|
| Illustration | Person at doctor's appointment with phone |
| Headline | "Never forget what your doctor said" |
| Subheadline | "Ditto records your appointments and creates clear summaries you can share" |
| Feature 1 | 🎙️ **Record** - Capture your appointment (with doctor's consent) |
| Feature 2 | 📝 **Summarize** - Get a clear breakdown of what was said |
| Feature 3 | 👥 **Share** - Keep loved ones informed without repeating yourself |
| CTA | "Continue" |

**Design notes**:
- Focus on the recording/summary value first
- Sharing is positioned as a benefit, not requirement

---

### Screen 3: Social Proof & Burden Relief
**Address the emotional weight of repeating information**

| Element | Content |
|---------|---------|
| Header | "You don't have to repeat yourself anymore" |
| Stat | "Patients answer 'how did it go?' an average of 7 times after each appointment" |
| Story | _"I used to dread calling everyone after appointments. Now they just check Ditto."_ — Maria, 52 |
| Benefit list | • Save emotional energy for recovery |
| | • Everyone gets the same accurate information |
| | • Share when you're ready, not when they ask |
| CTA | "Continue" |

**Design notes**:
- Empathetic tone
- Acknowledge the burden without being dramatic
- Position Ditto as relief, not obligation

---

### Screen 4: Intention Setting
**"Why do you want to share with loved ones?"**

| Element | Content |
|---------|---------|
| Header | "What would help you most?" |
| Subheader | "Select all that apply" |
| Option 1 | 📢 **Keep everyone informed** - Share updates once, reach everyone |
| Option 2 | 🤝 **Get practical help** - Let people know how they can support you |
| Option 3 | 💬 **Fewer "how did it go?" questions** - Update on your own terms |
| Option 4 | ❤️ **Feel supported** - Know people are thinking of you |
| Multi-select | Allow selecting multiple options |
| CTA | "Continue" |

**Logic**:
- Selection influences home screen content and suggestions
- Informs future feature prioritization

---

### Screen 5: Add First Appointment
**Get to core value quickly**

| Element | Content |
|---------|---------|
| Header | "Let's set up your first appointment" |
| Subheader | "You can record it and share the summary with your Care Circle" |
| Input: Date | "When is your appointment?" |
| Input: Time | "What time?" |
| Input: Type | "What type?" (Dropdown: Oncologist, GP, Specialist, etc.) |
| Input: Location | "Where?" (Optional) |
| Input: Notes | "Anything you want to remember?" (Optional) |
| CTA | "Add Appointment" |
| Skip | "I don't have one scheduled" (secondary) |

**Design notes**:
- Minimal required fields (date, time, type)
- Make it feel easy, not like a chore
- Skip option for users without upcoming appointments

---

### Screen 6: Profile Setup Prompt
**Soft introduction to profile (don't force completion)**

| Element | Content |
|---------|---------|
| Header | "Help your followers understand" |
| Subheader | "A brief profile helps loved ones know how to support you" |
| Preview | Mockup of profile page showing bio, FAQ |
| CTA Primary | "Set Up Profile" → Profile setup flow |
| CTA Secondary | "Do This Later" → Home screen |

**Design notes**:
- Show value of profile (followers will see this)
- Don't force completion in onboarding
- Can prompt again after first share

---

### Screen 7: Profile Setup (if chosen)
**Quick profile creation**

| Element | Content |
|---------|---------|
| Header | "Your Care Circle Profile" |
| Input: Photo | "Add a photo" (optional) |
| Input: Bio | "Write a short bio" |
| | Placeholder: "I'm going through [condition] treatment. This is my journey." |
| Input: Condition | "What are you dealing with?" (helps generate FAQ) |
| Section: FAQ | "Common questions people might have" |
| FAQ items | AI-suggested based on condition (editable) |
| | • What is my diagnosis? |
| | • What treatment am I on? |
| | • How can people help? |
| CTA | "Save Profile" |

**Design notes**:
- AI assists with FAQ generation
- Everything is editable
- Emphasize this helps followers help you

---

### Screen 8: Invite Followers Prompt
**Transition to invitation flow**

| Element | Content |
|---------|---------|
| Illustration | Card/invitation visual |
| Header | "Invite your Care Circle" |
| Body | "Create personal invitation cards for the people you want to keep in the loop" |
| Suggestion | Based on intention: "You mentioned wanting to reduce 'how did it go?' questions. Invite the people who usually ask." |
| CTA Primary | "Create Invitation Card" → Flow 3 |
| CTA Secondary | "Do This Later" → Home screen |

**Design notes**:
- Connect to stated intention
- Make invitation feel meaningful, not spammy
- Allow deferral without guilt

---

### Screen 9: Home Screen (Patient - Empty)
**State before any appointments or followers**

| Element | Content |
|---------|---------|
| Header | "Your Health Journey" |
| Section: Next Appointment | Card showing upcoming appointment |
| | Date, time, type, location |
| | "Record" button (if appointment is soon) |
| Empty state: Care Circle | "Your Care Circle is empty" |
| | "Invite loved ones to follow your journey" |
| | [Invite] button |
| Upcoming events | Calendar-style view of scheduled appointments |
| Quick actions | + Add appointment, + Invite someone |

---

### Screen 10: Home Screen (Patient - Active)
**State with appointments and followers**

| Element | Content |
|---------|---------|
| Header | "Your Health Journey" |
| Section: Next Appointment | Card showing upcoming appointment |
| | Date, time, type, countdown |
| | "Prepare" and "Record" buttons |
| Section: Care Circle | "X people following your journey" |
| | Avatars of followers |
| | [Manage] button |
| Section: Recent Activity | |
| | • Reactions received |
| | • Support cards received |
| | • New followers |
| Section: Timeline | Past appointments with summaries |
| | Each shows: date, type, summary preview, share status |

---

## Edge Cases

### User has no upcoming appointments
- Show "Add appointment when you have one"
- Focus on profile setup and invitations first
- Value prop shifts to "be ready when you need it"

### User doesn't want to share with anyone
- Ditto still works as personal health record
- Gently suggest sharing benefits over time
- Don't force social features

### User is following someone AND is a patient
- Show both views accessible
- Clear toggle or tab structure
- Respect context switching

---

## Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
| `patient_onboarding_started` | Screen 1 shown | - |
| `role_selected` | Taps patient option | role: patient |
| `value_prop_viewed` | Screen 2 shown | - |
| `intention_selected` | Screen 4 completed | intentions: array |
| `appointment_added` | Screen 5 completed | appointment_type |
| `appointment_skipped` | Skip on Screen 5 | - |
| `profile_setup_started` | Chose to set up profile | - |
| `profile_setup_completed` | Profile saved | has_photo, has_bio, faq_count |
| `profile_setup_deferred` | Chose to do later | - |
| `invitation_flow_started` | Chose to invite | - |
| `invitation_deferred` | Chose to do later | - |

---

## Open Questions

1. Should we capture condition during onboarding or wait for first appointment recording?
2. How much profile info is needed before first invite can be sent?
3. Should profile FAQ be required or optional?

---

## Related Flows
- [Flow 3: Invitation Card Creation](03-invitation-card.md) - Inviting followers
- [Flow 4: First Connection Celebration](04-first-connection.md) - When someone accepts
- [Flow 5: Reactions](05-reactions.md) - How patient receives reactions
- [Flow 6: Profile Page](06-profile-page.md) - What followers see
