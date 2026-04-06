# Flow 3: Invitation Card Creation

## Overview
**Goal**: Create a meaningful, shareable invitation asset (not just a link)

**Success Criteria**: User creates and shares at least one invitation card

**Design Philosophy**:
- Creating something (card, asset) = commitment + meaning
- More meaningful than a WhatsApp message = recipient feels valued
- Solves empty state = sender has content in app
- Reusable mechanism for reactions (support cards)

**Inspiration**: Spotify's "send to you" sharing cards with customizable backgrounds

---

## Flow Diagram

```
                    [Start Invitation]
                              ↓
         ┌──────────────────────────────────────┐
         │  STEP 1: Select Visual Element       │
         │  • Flowers (warm, caring)            │
         │  • Heart circle (connection)         │
         │  • Other warm illustrations          │
         └──────────────────────────────────────┘
                              ↓
         ┌──────────────────────────────────────┐
         │  STEP 2: Add Personal Message        │
         │  Pre-filled based on intention:      │
         │  "I want to keep you close on my     │
         │   health journey" (customizable)     │
         └──────────────────────────────────────┘
                              ↓
         ┌──────────────────────────────────────┐
         │  STEP 3: Fill in Name                │
         │  "Dear [____]"                       │
         │  (just name - no phone number yet)   │
         └──────────────────────────────────────┘
                              ↓
                    [Generate Card Preview]
                    (Spotify-style shareable image)
                              ↓
                    [Share to WhatsApp]
                    (image + Ditto link)
                              ↓
                    [View Sent Invitations]
                    (in-app record of cards created)
```

---

## Screens

### Screen 1: Choose Visual Style
**Select the background/illustration for the card**

| Element | Content |
|---------|---------|
| Header | "Create an Invitation" |
| Subheader | "Choose a style that feels right" |
| Grid of options | 6-8 visual styles to choose from |
| Style 1 | 🌸 **Flowers** - Soft, warm, caring |
| Style 2 | 💜 **Heart Circle** - Connection, togetherness |
| Style 3 | 🌿 **Nature** - Calm, peaceful, growth |
| Style 4 | ☀️ **Sunrise** - Hope, new beginnings |
| Style 5 | 🤝 **Hands** - Support, solidarity |
| Style 6 | ✨ **Abstract** - Modern, neutral |
| Preview area | Shows selected style applied to card template |
| CTA | "Next" |

**Design notes**:
- Options should feel warm, not clinical
- Consider testing "too feminine?" concern
- Abstract/neutral options for broader appeal
- Real-time preview as user browses

**Visual specifications**:
- Card dimensions: Optimized for WhatsApp/social sharing (1080x1350 or similar)
- High-contrast text overlay area
- Illustrations should be original, not stock

---

### Screen 2: Personalize Message
**Add/edit the message on the card**

| Element | Content |
|---------|---------|
| Header | "Add your message" |
| Card preview | Shows visual + message area |
| Pre-filled message | Based on user's stated intention (from onboarding) |
| Message options | Dropdown or suggestions: |
| | • "I want to keep you close on my health journey" |
| | • "I'd love for you to be part of my Care Circle" |
| | • "Will you follow along as I navigate this?" |
| | • "I want you to be in the loop" |
| Custom option | Text area for custom message (character limit: 150) |
| CTA | "Next" |

**Pre-fill logic based on intention**:
| Intention Selected | Pre-filled Message |
|--------------------|--------------------|
| Keep informed | "I want to keep you in the loop on my health journey" |
| Get support/help | "I could use your support. Will you follow along?" |
| Fewer questions | "I'll share updates here so we don't have to repeat myself" |
| Be there emotionally | "Having you follow my journey means everything to me" |

**Design notes**:
- Show message on card in real-time
- Keep messages short and heartfelt
- Avoid medical jargon

---

### Screen 3: Add Recipient Name
**Personalize with recipient's name**

| Element | Content |
|---------|---------|
| Header | "Who is this for?" |
| Card preview | Shows "Dear [name]" area highlighted |
| Input: Name | "Enter their name" |
| | Placeholder: "Mom", "Sarah", "The Family" |
| Name preview | Updates on card in real-time |
| Optional: Relationship | Dropdown: Mom, Dad, Partner, Friend, Sibling, Other |
| | (Used for personalization, not shown on card) |
| CTA | "Preview Card" |

**Design notes**:
- Just first name or nickname is fine
- No phone number required at this step
- Relationship helps with analytics and future features

---

### Screen 4: Card Preview
**Final preview before sharing**

| Element | Content |
|---------|---------|
| Header | "Your invitation is ready" |
| Full card preview | Complete card with: |
| | • Visual background |
| | • "Dear [Name]" |
| | • Personal message |
| | • Ditto branding (subtle) |
| Edit options | [Change Style] [Edit Message] [Change Name] |
| Share preview | "This is what [Name] will see" |
| CTA Primary | "Share via WhatsApp" |
| CTA Secondary | "Share to..." (other options) |
| CTA Tertiary | "Save to Photos" |

**Card layout**:
```
┌─────────────────────────────────┐
│                                 │
│     [Visual illustration]       │
│                                 │
│     Dear [Name],                │
│                                 │
│     [Personal message text      │
│      goes here, centered]       │
│                                 │
│     ───────────────────         │
│                                 │
│     Join my Care Circle         │
│     on Ditto                    │
│                                 │
│     [QR Code or "Tap to join"]  │
│                                 │
│     ditto • health journeys     │
│                                 │
└─────────────────────────────────┘
```

---

### Screen 5: Share Flow
**Sharing to WhatsApp or other channels**

| Element | Content |
|---------|---------|
| Action | Native share sheet OR direct WhatsApp integration |
| Shared content | 1. Card image (generated) |
| | 2. Text: "I'm inviting you to follow my health journey on Ditto. [link]" |
| Deep link | ditto.app/invite/[unique-code] |
| After share | Return to Ditto → Screen 6 |

**Technical requirements**:
- Generate high-quality image server-side
- Unique invite link per invitation
- Track when link is opened/clicked
- Track when invite is accepted

---

### Screen 6: Invitation Sent Confirmation
**Celebrate and show next steps**

| Element | Content |
|---------|---------|
| Animation | Confetti or gentle celebration |
| Header | "Invitation sent!" |
| Subheader | "We'll let you know when [Name] joins" |
| Card preview | Thumbnail of sent card |
| Next steps | "While you wait:" |
| | • [Invite someone else] |
| | • [Set up your profile] (if not done) |
| | • [Add an appointment] (if not done) |
| CTA | "Done" → Home screen |

---

### Screen 7: Sent Invitations (Management)
**View and manage all sent invitations**

| Element | Content |
|---------|---------|
| Header | "Sent Invitations" |
| List of invitations | Each shows: |
| | • Card thumbnail |
| | • Recipient name |
| | • Date sent |
| | • Status: Pending / Accepted / Expired |
| Status: Pending | "Waiting for [Name] to join" |
| | [Resend] [Send Reminder] |
| Status: Accepted | "✓ [Name] joined on [date]" |
| | [View Profile] |
| Status: Expired | "Link expired after 14 days" |
| | [Send New Invitation] |
| Empty state | "No invitations sent yet" |
| | [Create Invitation] |

**Invitation lifecycle**:
- Pending: Sent but not accepted (14-day expiry)
- Accepted: Recipient downloaded app and connected
- Expired: Link no longer valid
- Resend: Generates new link, same card

---

## Card Creation for Followers (Inviting Patient)
**Variant when follower initiates invitation to patient**

Same flow but with adjusted copy:

| Screen | Follower Variant |
|--------|------------------|
| Header | "Invite [Name] to share with you" |
| Pre-filled messages | "I'd love to follow your health journey" |
| | "I want to be there for you. Will you share your updates with me?" |
| | "I care about you and want to stay in the loop" |
| What recipient gets | Invitation to become a patient and share |

---

## Technical Requirements

### Card Generation
- Server-side image generation (consistent quality)
- Multiple resolution outputs (sharing, thumbnail, full)
- Template system for easy addition of new styles
- Localization support for text on cards

### Invitation Links
- Unique, non-guessable codes
- Expiration (14 days default)
- Deep linking to app store if not installed
- Track: created, clicked, app_installed, accepted

### Data Model
```
Invitation {
  id: string
  sender_id: string
  recipient_name: string
  recipient_relationship: string?
  visual_style: string
  message: string
  invite_code: string
  status: pending | accepted | expired
  created_at: timestamp
  expires_at: timestamp
  accepted_at: timestamp?
  accepted_by: string? (user_id)
}
```

---

## Edge Cases

### Recipient already has Ditto
- Link should recognize and connect accounts
- Don't require re-download
- Show "You're now connected to [Sender]"

### Invitation sent to wrong person
- Allow canceling pending invitations
- Canceled invitations show "Link no longer valid" when clicked

### Sender wants to edit after sending
- Can't edit sent cards (already shared)
- Can send new invitation with different content
- Old invitation can be canceled

### Multiple invitations to same person
- Allow it (relationships change)
- Show all in sent invitations list
- Accepting any one connects them

---

## Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
| `invitation_started` | Flow begins | source: onboarding/home/profile |
| `visual_style_selected` | Style chosen | style_id |
| `message_customized` | User edits message | message_length, used_suggestion |
| `recipient_named` | Name entered | relationship |
| `card_previewed` | Preview screen shown | - |
| `card_shared` | Share initiated | channel: whatsapp/other/saved |
| `invitation_sent` | Share completed | invite_id |
| `invitation_clicked` | Link opened | invite_id, device |
| `invitation_accepted` | Recipient connected | invite_id, time_to_accept |
| `invitation_expired` | 14 days passed | invite_id |

---

## Open Questions

1. **Visual styles**: Are flowers too feminine? Need user testing with diverse groups
2. **QR code**: Include on card for easy scanning or just deep link?
3. **Group invitations**: Allow sending same card to multiple people at once?
4. **Card templates**: Seasonal/holiday variations?

---

## Related Flows
- [Flow 1: Follower Activation](01-follower-activation.md) - Leads to this flow
- [Flow 2: Patient Activation](02-patient-activation.md) - Leads to this flow
- [Flow 4: First Connection Celebration](04-first-connection.md) - After acceptance
- [Flow 5: Reactions](05-reactions.md) - Same card mechanism, different purpose
