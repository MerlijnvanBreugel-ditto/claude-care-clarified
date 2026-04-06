# Flow 5: Reactions (Shared Event → Response)

## Overview
**Goal**: After patient shares an update, followers can respond meaningfully

**Success Criteria**:
- Followers have low-friction ways to show support
- Patients feel supported, not interrogated
- Reactions feel meaningful, not cheap

**Design Philosophy**:
- Emojis alone feel cheap for serious health news
- Cards = "digital get-well cards" = thoughtful gesture
- Offer help = actionable support
- Same card mechanism as invitations (reusable component)

---

## Flow Diagram

```
                    [Patient Shares Event]
                    (appointment summary + optional personal note)
                              ↓
                    [Followers Get Notification]
                              ↓
         ┌──────────────────────────────────────┐
         │  Follower Response Options:          │
         │                                      │
         │  QUICK REACTIONS:                    │
         │  ❤️ 🤗 💪 (low-pressure)             │
         │                                      │
         │  CARD REACTION:                      │
         │  [Send a Support Card]               │
         │  (same mechanism as invitation)      │
         │                                      │
         │  OFFER HELP:                         │
         │  [Offer Practical Help]              │
         │  □ Cooking  □ Transport  □ Company   │
         └──────────────────────────────────────┘
                              ↓
                    [Patient Receives Cards]
                    (viewable in timeline + notification center)
```

---

## Patient Sharing an Update

### Screen S1: Share Update Options
**Patient chooses what to share after appointment**

| Element | Content |
|---------|---------|
| Header | "Share with your Care Circle" |
| Summary preview | AI-generated summary from appointment |
| Share options | |
| **Full Summary** | "Share the complete summary" |
| | Everything from the appointment |
| **Short Summary** | "Share key points only" |
| | Diagnosis, next steps, dates |
| **Custom** | "Choose what to include" |
| | Checkboxes for each section |
| Add personal note | "How are you feeling about this?" |
| | Placeholder: "Add your thoughts (optional)" |
| CTA | "Share Update" |

**Personal note examples**:
- "Feeling hopeful after today"
- "This was tough but I'm staying strong"
- "Processing everything, will update more soon"

---

### Screen S2: Confirm Share
**Review before sending to Care Circle**

| Element | Content |
|---------|---------|
| Header | "Review your update" |
| Recipients | "Sharing with X people in your Care Circle" |
| Preview | What followers will see |
| Personal note | Highlighted if included |
| Edit option | [Edit] to go back |
| CTA | "Share Now" |

---

## Follower Receiving Update

### Screen F1: Push Notification
**Follower receives notification**

| Notification | Content |
|--------------|---------|
| Title | "[Patient Name] shared an update" |
| Body | Preview of summary (first line) |
| Action | Tap to open |

---

### Screen F2: Update View
**Full update as seen by follower**

| Element | Content |
|---------|---------|
| Header | [Patient Name] • [Date] |
| Update type | "Oncology Appointment" |
| Summary | Full or short summary based on patient choice |
| Personal note | (if included) Styled differently, more personal |
| | "How I'm feeling: [patient's note]" |
| Divider | ─────────────── |
| **Reaction Section** | |
| Quick reactions | ❤️ 🤗 💪 (tap to react) |
| | "Show your support" |
| Send card | [Send Support Card] |
| Offer help | [Offer to Help] |
| Reactions display | "❤️ Mom, Sarah +2 others" |

---

### Screen F3: Quick Reactions
**Emoji reactions (lowest friction)**

| Element | Content |
|---------|---------|
| Reaction bar | ❤️ 🤗 💪 |
| ❤️ | Love/Heart - "Sending love" |
| 🤗 | Hug - "Virtual hug" |
| 💪 | Strength - "You've got this" |
| Interaction | Single tap to react |
| | Tap again to change/remove |
| Feedback | Brief animation when selected |
| | Reaction appears in count |

**Design notes**:
- Limited to 3 options (avoid decision paralysis)
- Each has clear meaning
- Can only select one per update
- Low commitment, always appropriate

---

### Screen F4: Support Card Creation
**Same mechanism as invitation cards**

| Element | Content |
|---------|---------|
| Header | "Send [Patient] a card" |
| Subheader | "More meaningful than just an emoji" |
| **Step 1: Visual** | |
| Options | 💪 Strength theme |
| | ❤️ Love theme |
| | 🌸 Thinking of you |
| | ☀️ Brighter days |
| | 🌿 Peaceful/calm |
| **Step 2: Message** | |
| Pre-filled options | "Thinking of you" |
| | "You're so strong" |
| | "I'm here for you" |
| | "One step at a time" |
| Custom | Text input (150 char limit) |
| **Step 3: Preview** | |
| Card preview | Full card with visual + message |
| CTA | "Send Card" |

**Card layout**:
```
┌─────────────────────────────────┐
│                                 │
│     [Visual illustration]       │
│                                 │
│     [Follower Name] says:       │
│                                 │
│     "[Message text here]"       │
│                                 │
│     ───────────────────         │
│                                 │
│     💜 Sent with love           │
│                                 │
└─────────────────────────────────┘
```

---

### Screen F5: Offer Practical Help
**Actionable support options**

| Element | Content |
|---------|---------|
| Header | "Offer to help" |
| Subheader | "Let [Patient] know what you can do" |
| Help categories | Multi-select checkboxes |
| 🍳 **Meals** | "I can bring food or cook" |
| 🚗 **Transport** | "I can give rides" |
| 👋 **Company** | "I can visit or hang out" |
| 🛒 **Errands** | "I can run errands or shop" |
| 🏠 **Household** | "I can help around the house" |
| 👶 **Childcare** | "I can help with kids" |
| 💬 **Other** | Free text: "Anything else?" |
| Availability | "When are you available?" |
| | This week / Next week / Anytime |
| Message | "Add a note (optional)" |
| CTA | "Send Offer" |

**What patient receives**:
```
[Follower Name] wants to help!

They offered:
✓ Meals - "I can bring food"
✓ Transport - "I can give rides"

Available: This week

"Let me know what you need! - [Name]"

[Accept] [Reply] [Decline]
```

---

## Patient Receiving Reactions

### Screen P1: Notification Center
**All reactions and cards in one place**

| Element | Content |
|---------|---------|
| Header | "Support Received" |
| Filter tabs | All / Cards / Help Offers / Reactions |
| **Cards section** | |
| Card preview | Thumbnail + sender name + preview |
| | Tap to view full card |
| **Help offers section** | |
| Offer card | Sender name, what they offered |
| | [Accept] [Reply] [Decline] |
| **Reactions section** | |
| Grouped | "❤️ from Mom, Dad, Sarah" |
| | "💪 from Mike, Lisa" |

---

### Screen P2: View Support Card
**Full card view when patient opens it**

| Element | Content |
|---------|---------|
| Full card display | Complete card as created by follower |
| Sender info | "From [Follower Name]" |
| Received date | "Received [date/time]" |
| Actions | [Send Thanks] [Save to Gallery] |

---

### Screen P3: Respond to Help Offer
**Managing help offers**

| Element | Content |
|---------|---------|
| Offer display | What was offered + availability |
| **Accept** | "Great! [Name] will be notified" |
| | Optional: Add message or schedule |
| **Reply** | "Send [Name] a message" |
| | Opens message thread |
| **Decline** | "Not right now" |
| | Optional: "Maybe later" or "Thanks, I'm okay" |

---

### Screen P4: Timeline View with Reactions
**Updates shown with all reactions**

| Element | Content |
|---------|---------|
| Update card | Summary, date, type |
| Reactions bar | "❤️ 5 🤗 3 💪 2" |
| Cards indicator | "📬 3 cards received" |
| Help offers | "🤝 2 help offers" |
| Expand | Tap to see who reacted |
| View cards | Tap to see all cards |

---

## Reaction Types Summary

| Type | Friction | Meaning | When to Use |
|------|----------|---------|-------------|
| ❤️ Emoji | Very low | "I saw this, I care" | Always appropriate |
| 🤗 Emoji | Very low | "Virtual hug" | Emotional support |
| 💪 Emoji | Very low | "You've got this" | Encouragement |
| Support Card | Medium | "I took time to create this" | Bigger moments |
| Help Offer | High | "I want to do something concrete" | When patient needs help |

---

## Edge Cases

### Multiple reactions to same update
- Followers can emoji + send card
- Each reaction type shows separately
- Patient sees aggregated view

### Follower wants to react to old update
- All past updates are accessible
- Reactions still valid on older content
- "Better late than never"

### Patient receives overwhelming support
- Group similar reactions
- Card gallery for browsing
- "30 reactions" instead of listing all

### Help offer not accepted
- After 7 days, auto-decline with kind message
- Follower gets: "[Patient] appreciated your offer"
- Doesn't feel like rejection

### Patient doesn't want certain reactions
- Settings: "Allow reactions: Yes/No"
- Settings: "Allow help offers: Yes/No"
- Defaults to all enabled

---

## Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
| `update_shared` | Patient shares | summary_type, has_note |
| `update_viewed` | Follower views update | update_id, time_since_share |
| `emoji_reaction_sent` | Emoji tapped | emoji_type, update_id |
| `card_creation_started` | Card flow begun | update_id |
| `card_sent` | Card completed | update_id, visual_style |
| `help_offer_created` | Offer submitted | categories, availability |
| `help_offer_accepted` | Patient accepts | offer_id, time_to_accept |
| `help_offer_declined` | Patient declines | offer_id, reason |
| `card_viewed` | Patient views card | card_id |
| `reactions_viewed` | Patient opens reactions | update_id |

---

## Success Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Reaction rate | % updates that get ≥1 reaction | 70%+ |
| Card send rate | % reactions that are cards | 20%+ |
| Help offer rate | % updates with help offers | 10%+ |
| Help offer acceptance | % offers accepted | 30%+ |
| Time to first reaction | Minutes after share | <60 min |

---

## Open Questions

1. **Reaction timing**: Should reactions expire or always be possible?
2. **Message thread**: When help offer starts conversation, where does it live?
3. **Anonymous reactions**: Should patient always see who reacted?
4. **Reaction limits**: Max one emoji per update, or allow all three?

---

## Related Flows
- [Flow 3: Invitation Card Creation](03-invitation-card.md) - Same card component
- [Flow 4: First Connection Celebration](04-first-connection.md) - Welcome cards
- [Flow 6: Profile Page](06-profile-page.md) - "Send Support" from profile
