# Flow 4: First Connection Celebration

## Overview
**Goal**: Celebrate when someone accepts an invitation and establish the new connection

**Success Criteria**:
- Patient feels supported when follower joins
- Follower immediately has meaningful content to explore
- Both parties understand what happens next

**Design Philosophy**:
- Celebrate the connection (it's a big deal!)
- Give follower immediate value (profile page, FAQ, context)
- Reduce anxiety on both sides

---

## Flow Diagram

```
                    [Follower Accepts Invite]
                              ↓
         ┌──────────────────────────────────────┐
         │  Patient Notification:               │
         │  "🎉 [Name] is now following you!"   │
         │                                      │
         │  [View their profile]                │
         │  [Set up your profile for them]      │
         └──────────────────────────────────────┘
                              ↓
         ┌──────────────────────────────────────┐
         │  Follower Receives:                  │
         │  • Patient's profile page (if set)   │
         │  • FAQ about patient's condition     │
         │  • Bio and context                   │
         │  • Option to send support card       │
         └──────────────────────────────────────┘
```

---

## Follower Side: Accepting Invitation

### Screen F1: Invitation Landing Page
**What follower sees when clicking invite link**

| Element | Content |
|---------|---------|
| Card display | The invitation card they received |
| Header | "[Patient Name] invited you to their Care Circle" |
| Explanation | "Follow [Name]'s health journey and be there for them" |
| What you'll get | • Updates when they share |
| | • Ways to show support |
| | • Their health FAQ & bio |
| CTA Primary | "Accept Invitation" |
| CTA Secondary | "Learn more about Ditto" |

**If app not installed**:
- Show same content on web page
- CTA changes to "Download Ditto to Accept"
- App store badges prominent

---

### Screen F2: Follower Onboarding (Quick)
**Minimal onboarding for invitation accepters**

| Element | Content |
|---------|---------|
| Context | "You're joining [Patient Name]'s Care Circle" |
| Step 1 | Name (pre-filled from invitation if available) |
| Step 2 | Profile photo (optional, can skip) |
| Step 3 | Notification preferences |
| | • When [Name] shares an update |
| | • When [Name] has an appointment |
| Skip | "Set these up later" option |
| CTA | "Join Care Circle" |

**Design notes**:
- Much shorter than full onboarding
- Get them connected fast
- They can always adjust settings later

---

### Screen F3: Connection Celebration (Follower)
**Moment of connection**

| Element | Content |
|---------|---------|
| Animation | Hearts, connection animation |
| Header | "You're now connected!" |
| Subheader | "You're following [Patient Name]'s health journey" |
| What's next | "Here's what you can do:" |
| Action 1 | [View their profile] - "Learn about their journey" |
| Action 2 | [Send a support card] - "Let them know you're here" |
| Action 3 | [Explore Ditto] - Go to home screen |
| CTA | "Continue" |

---

### Screen F4: Patient Profile (Follower View)
**What follower sees after connecting**

| Element | Content |
|---------|---------|
| Header | [Patient Name] |
| Profile section | Photo, name, bio |
| | "Mom of 2. Breast cancer patient since Jan 2026" |
| Divider | ─────────────── |
| FAQ Section | 📋 "About [Name]'s Journey" |
| FAQ Item 1 | **What is [condition]?** |
| | AI-generated explanation (patient-approved) |
| FAQ Item 2 | **What treatment are they on?** |
| | Details if patient has shared |
| FAQ Item 3 | **How can I help?** |
| | Patient's guidance on support |
| FAQ Item 4 | **When is the next appointment?** |
| | Date/time if shared |
| Divider | ─────────────── |
| Actions | [Send Support] [Offer Help] |

**Content states**:
- **Profile set up**: Full content as above
- **Profile not set up**: Placeholder with patient's name only
  - "Profile coming soon. [Name] will share more when ready."
  - Still shows actions (send support, offer help)

---

### Screen F5: Send Welcome Support Card
**Optional: Follower can immediately send support**

| Element | Content |
|---------|---------|
| Header | "Send [Name] a card" |
| Context | "Let them know you're here for them" |
| Visual options | Same card mechanism as invitations |
| | 💪 Strength, ❤️ Love, 🌸 Thinking of you |
| Pre-filled messages | "I'm here for you" |
| | "So glad I can follow along" |
| | "Thinking of you always" |
| CTA | "Send Card" |
| Skip | "Maybe later" |

---

## Patient Side: Receiving Notification

### Screen P1: Push Notification
**Immediate notification when follower accepts**

| Notification | Content |
|--------------|---------|
| Title | "🎉 [Follower Name] joined your Care Circle!" |
| Body | "[Name] is now following your health journey" |
| Action | Tap to open app |

---

### Screen P2: In-App Notification
**Detailed notification in app**

| Element | Content |
|---------|---------|
| Card style | Celebration card with follower's photo |
| Header | "[Follower Name] is now following you!" |
| Subheader | "They accepted your invitation" |
| Timestamp | "Just now" |
| Actions | [View their profile] [Send thanks] |
| Context | "They can now see your updates when you share" |

---

### Screen P3: Connection Celebration (Patient)
**When patient opens app after acceptance**

| Element | Content |
|---------|---------|
| Modal/Overlay | Celebration moment |
| Animation | Confetti, hearts, warm animation |
| Header | "🎉 [Name] joined your Care Circle!" |
| Follower preview | Photo, name, relationship (if known) |
| Body | "They'll receive updates when you share" |
| Nudge (if no profile) | "Set up your profile so [Name] can learn more about your journey" |
| CTA Primary | [Set Up Profile] (if not done) |
| | OR [View Care Circle] (if profile exists) |
| CTA Secondary | "Continue" |

---

### Screen P4: Profile Setup Prompt (if needed)
**Prompt to complete profile after first connection**

| Element | Content |
|---------|---------|
| Header | "Help [Follower Name] understand" |
| Body | "[Name] is following you but doesn't have much context yet. Would you like to set up your profile?" |
| What profile includes | • Your bio |
| | • FAQ about your condition |
| | • How people can help |
| CTA Primary | "Set Up Profile" |
| CTA Secondary | "Do This Later" |

---

### Screen P5: Care Circle Management
**Updated Care Circle view showing new follower**

| Element | Content |
|---------|---------|
| Header | "Your Care Circle" |
| Count | "3 people following your journey" |
| Follower list | Each shows: |
| | • Photo/avatar |
| | • Name |
| | • Relationship (if set) |
| | • "Following since [date]" |
| New follower | Highlighted/badged as "New" |
| Actions per follower | [View] [Remove] |
| Add more | [Invite More People] |

---

## Handling Edge Cases

### Patient hasn't set up profile yet
- Follower sees: "Profile coming soon"
- Patient gets nudge: "Set up your profile"
- Follower can still send support card
- Connection still valid and functional

### Follower already has Ditto account
- Skip account creation
- Quick "confirm connection" flow
- "You're now following [Name]"

### Multiple invitations from different patients
- Each is a separate connection
- Home screen shows all followed patients
- Clear separation in UI

### Patient removes follower later
- Follower sees: "You're no longer connected"
- Past shared content remains? (Design decision needed)
- Follower can request reconnection

### Invitation accepted but patient deleted account
- Show graceful error
- "This Care Circle is no longer available"
- Offer to start fresh with someone else

---

## Notifications Summary

| Event | Patient Notification | Follower Notification |
|-------|---------------------|----------------------|
| Invite accepted | "🎉 [Name] joined!" | "Welcome to [Name]'s Care Circle" |
| Profile updated | - | "[Name] updated their profile" |
| First share coming | Reminder to share | "Stay tuned for [Name]'s first update" |

---

## Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
| `invite_link_clicked` | Link opened | invite_id, referrer |
| `invite_landing_viewed` | Landing page shown | invite_id, has_app |
| `invite_accepted_started` | Accept button clicked | invite_id |
| `invite_accepted_completed` | Account connected | invite_id, time_to_accept |
| `connection_celebration_viewed` | Celebration screen shown | role: patient/follower |
| `welcome_card_sent` | Follower sends card | invite_id |
| `profile_prompt_shown` | Profile nudge displayed | - |
| `profile_prompt_accepted` | Started profile setup | - |
| `profile_prompt_dismissed` | Deferred profile | - |

---

## Success Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Invite acceptance rate | Accepted / Sent | 40%+ |
| Time to accept | Hours from send to accept | <48 hours |
| Welcome card sent rate | % followers who send card | 30%+ |
| Profile completion after connection | % patients who complete profile within 24h | 50%+ |
| Follower return rate (D1) | % followers who return next day | 60%+ |

---

## Open Questions

1. **What if patient doesn't want to accept a follower?** (Not current flow, but edge case)
2. **Should connections be mutual by default?** (Patient can also follow follower's health if they're a patient)
3. **How much profile info is shown before vs. after connection?**

---

## Related Flows
- [Flow 3: Invitation Card Creation](03-invitation-card.md) - Creates the invitation
- [Flow 5: Reactions](05-reactions.md) - Sending support cards
- [Flow 6: Profile Page](06-profile-page.md) - What follower sees after connecting
