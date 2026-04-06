# Flow 1: Follower Activation

## Overview
**Goal**: User sees ad → downloads → understands value → invites first person

**Success Criteria**: User completes invitation within first session

**Primary Persona**: Someone who wants to follow a loved one's health journey (not a patient themselves)

---

## Flow Diagram

```
[Meta Ad] → [App Store] → [Download]
                              ↓
                    [Smooth Onboarding]
                              ↓
                    [Smart Home Screen]
                    (personalized for follower)
                              ↓
         ┌──────────────────────────────────────┐
         │  PHASE A: Understanding & Trust      │
         │  • Social proof ("40% share...")     │
         │  • Stories of families using Ditto   │
         │  • Why sharing helps BOTH parties    │
         └──────────────────────────────────────┘
                              ↓
         ┌──────────────────────────────────────┐
         │  PHASE B: Intention Setting          │
         │  "Why do you want to follow someone?"│
         │  □ I want to be informed             │
         │  □ I want to help them               │
         │  □ I want to be there emotionally    │
         └──────────────────────────────────────┘
                              ↓
                    [Create Invitation Card]
                    (engaging flow - see Flow 3)
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

**Interaction**: Tapping "I'm following someone" → Screen 2

---

### Screen 2: Social Proof & Trust Building
**Build confidence before asking for action**

| Element | Content |
|---------|---------|
| Illustration | Warm illustration of family connection |
| Headline | "You're not alone in wanting to help" |
| Stat 1 | "40% of people already share medical summaries with loved ones" |
| Stat 2 | "87% of patients feel less burdened when family stays informed" |
| Story snippet | _"My mom doesn't have to repeat herself anymore. We all know what's happening."_ — Sarah, daughter |
| CTA | "Continue" |

**Design notes**:
- Soft colors, warm imagery
- Stats should feel human, not clinical
- Story should be relatable and emotional

---

### Screen 3: Why This Helps Both of You
**Address the anxiety: "Am I being intrusive?"**

| Element | Content |
|---------|---------|
| Header | "Why sharing helps both of you" |
| Benefit for them | **For your loved one**: Less "how did it go?" texts. Less repeating themselves. More energy for recovery. |
| Benefit for you | **For you**: Stay informed without pestering. Know how to actually help. Feel connected, not helpless. |
| CTA | "I understand" |

**Design notes**:
- Two-column or alternating layout
- Icons for each benefit
- Emphasize mutual benefit, not surveillance

---

### Screen 4: Intention Setting
**"Why do you want to follow someone?"**

| Element | Content |
|---------|---------|
| Header | "What matters most to you?" |
| Subheader | "This helps us personalize your experience" |
| Option 1 | ❤️ **I want to be there emotionally** - Show them I care, even from afar |
| Option 2 | 📋 **I want to stay informed** - Know what's happening without asking |
| Option 3 | 🤝 **I want to help practically** - Offer support when they need it |
| Multi-select | Allow selecting multiple options |
| CTA | "Continue" |

**Logic**:
- Selection influences pre-filled message in invitation card
- Selection stored for analytics and personalization

**Pre-filled messages based on selection**:
- Emotional: "I want to be there for you, even when I can't be there in person."
- Informed: "I want to stay in the loop so you don't have to repeat yourself."
- Practical: "I want to help you however I can. Let me know what you need."

---

### Screen 5: Transition to Invitation
**Bridge to card creation flow**

| Element | Content |
|---------|---------|
| Illustration | Card/envelope visual |
| Header | "Send an invitation" |
| Body | "Create a personal invitation card for your loved one. It's more meaningful than just a link." |
| CTA | "Create Invitation Card" |
| Skip option | "I'll do this later" (subtle, secondary) |

**Design notes**:
- Show preview of what card might look like
- Make it feel special, not transactional
- Skipping should go to home screen with empty state

---

### Screen 6: Home Screen (Follower - No Connections)
**Empty state for users who skip or haven't connected yet**

| Element | Content |
|---------|---------|
| Header | "Care Circle" |
| Empty state illustration | Warm illustration of connection |
| Empty state text | "Your Care Circle is empty" |
| Empty state subtext | "Invite someone to follow their health journey" |
| Primary CTA | "Create Invitation" |
| Secondary content | Education cards (existing blue cards) explaining app value |

**Design notes**:
- Don't make it feel sad or empty
- Education cards give something to explore
- Gentle nudge to complete invitation

---

### Screen 7: Home Screen (Follower - With Connections)
**Active state showing followed people**

| Element | Content |
|---------|---------|
| Header | "Care Circle" |
| Section: My People | Grid/list of people being followed |
| Person card | Photo, name, last update preview, time since update |
| Person card tap | → Profile page (Flow 6) |
| Section: Recent Updates | Timeline of updates from followed people |
| Update card | Person name, event type, summary preview, reactions |
| FAB/CTA | "+ Invite someone" |

**Design notes**:
- Clear visual hierarchy: people first, updates second
- Easy to see "who needs attention"
- Quick access to send support

---

## Edge Cases

### User already has Ditto account as patient
- Show option to "Switch to follower view" or "Add role"
- Maintain existing patient data
- Home screen shows both roles

### User taps wrong role initially
- Easy way to switch in settings
- Or during onboarding: "Actually, I'm a patient" link

### Invitation not accepted after 48 hours
- Gentle reminder notification
- Option to resend or send different card
- Don't make user feel like they failed

---

## Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
| `follower_onboarding_started` | Screen 1 shown | - |
| `role_selected` | Taps follower option | role: follower |
| `social_proof_viewed` | Screen 2 shown | - |
| `intention_selected` | Screen 4 completed | intentions: array |
| `invitation_flow_started` | CTA on Screen 5 | - |
| `invitation_skipped` | Skip on Screen 5 | - |
| `home_screen_viewed` | Home screen shown | state: empty/active |

---

## Open Questions

1. Should we ask for notification permissions in this flow or wait until first update?
2. How do we handle multiple followed people with different update frequencies?
3. Should "I'll do this later" be more prominent or less?

---

## Related Flows
- [Flow 3: Invitation Card Creation](03-invitation-card.md) - Next step after this flow
- [Flow 4: First Connection Celebration](04-first-connection.md) - When invitation accepted
- [Flow 6: Profile Page](06-profile-page.md) - What followers see after connecting
