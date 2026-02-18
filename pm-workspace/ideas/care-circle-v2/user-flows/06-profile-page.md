# Flow 6: Profile Page (Follower View)

## Overview
**Goal**: Give followers a "single source of truth" about the patient

**Success Criteria**:
- Followers can find answers without asking the patient
- Patient controls what's shared
- Reduces "how are you?" and "what's happening?" questions

**Design Philosophy**:
- Profile = content even without shared updates
- FAQ reduces repetitive questions
- Bio + context helps followers understand
- Always accessible from follower's home screen

---

## Flow Diagram

```
         ┌──────────────────────────────────────┐
         │  PATIENT PROFILE (Follower View)     │
         │                                      │
         │  [Photo/Avatar]                      │
         │  [Name]                              │
         │  [Bio: "Mom of 2, Breast cancer      │
         │   patient since Jan 2026"]           │
         │                                      │
         │  ─────────────────────────────────   │
         │                                      │
         │  📋 FAQ (AI-suggested + editable)    │
         │  • What is triple-negative BC?       │
         │  • What treatment am I on?           │
         │  • When is my next appointment?      │
         │  • How can you help?                 │
         │                                      │
         │  ─────────────────────────────────   │
         │                                      │
         │  [Send Support] [Offer Help]         │
         │                                      │
         └──────────────────────────────────────┘
```

**Timing**: Profile setup happens AFTER first Care Circle setup (not during onboarding - too much friction)

---

## Screens

### Screen 1: Profile Page (Follower View - Complete)
**What follower sees when patient has set up profile**

| Section | Element | Content |
|---------|---------|---------|
| **Header** | Photo | Patient's profile photo (or avatar) |
| | Name | Patient's display name |
| | Bio | Short personal bio |
| | | "Mom of 2. Living with breast cancer since January 2026." |
| | Following since | "You've been following since [date]" |
| **Divider** | | ─────────────── |
| **About Section** | Header | "About [Name]'s Journey" |
| | Condition | "Diagnosis: Triple-negative breast cancer" |
| | Stage/Status | "Currently: In treatment" (if shared) |
| | Journey started | "Started: January 2026" |
| **Divider** | | ─────────────── |
| **FAQ Section** | Header | "📋 Frequently Asked Questions" |
| | Subheader | "Things you might want to know" |
| | FAQ items | Expandable accordion |
| **Divider** | | ─────────────── |
| **Actions** | Primary | [Send Support Card] |
| | Secondary | [Offer to Help] |
| **Divider** | | ─────────────── |
| **Updates** | Header | "Recent Updates" |
| | Updates list | Last 3-5 shared updates |
| | See all | "View all updates" → Timeline |

---

### Screen 2: FAQ Section (Expanded)
**Detailed FAQ with expandable items**

| FAQ Item | Example Content |
|----------|-----------------|
| **What is their diagnosis?** | "Triple-negative breast cancer (TNBC) is a type of breast cancer that doesn't have receptors for estrogen, progesterone, or HER2. It tends to grow and spread faster than other types." |
| **What treatment are they on?** | "Currently undergoing chemotherapy (AC-T regimen). Started in February 2026. Expected to complete in June 2026." |
| **When is the next appointment?** | "Next oncology appointment: March 15, 2026 at 2:00 PM" |
| **How can I help?** | "[Name] has shared: 'Right now, meal deliveries and rides to appointments are most helpful. Please don't send flowers - I'm allergic!'" |
| **What should I avoid asking?** | "[Name] has shared: 'Please don't ask about prognosis or survival rates. I'd rather talk about everyday life.'" |
| **How do they prefer to communicate?** | "[Name] has shared: 'Text is best. I'll respond when I have energy. Please don't take delays personally.'" |

**FAQ states**:
- **Answered**: Patient has provided content
- **Auto-generated**: AI suggestion based on condition (marked as "Based on general information")
- **Not answered**: "Ask [Name] directly" or "Not yet shared"

---

### Screen 3: Profile Page (Follower View - Minimal)
**What follower sees before patient sets up profile**

| Section | Element | Content |
|---------|---------|---------|
| **Header** | Avatar | Default avatar or initials |
| | Name | Patient's name (from invitation) |
| | Status | "Profile coming soon" |
| **Message** | | "[Name] hasn't set up their full profile yet. You'll be notified when they do." |
| **What you can do** | | "In the meantime, you can:" |
| **Actions** | Primary | [Send Support Card] - "Let them know you're thinking of them" |
| | Secondary | [Offer to Help] - "Offer practical support" |
| **Updates** | | "No updates shared yet" |
| | | "You'll be notified when [Name] shares" |

---

### Screen 4: Profile Setup (Patient View)
**How patient creates/edits their profile**

| Section | Element | Content |
|---------|---------|---------|
| **Photo** | Upload | "Add a photo" (optional) |
| | Options | Camera, gallery, skip |
| **Basic Info** | Name | Pre-filled from account |
| | Bio | Text area (200 char limit) |
| | | Placeholder: "Share a bit about yourself..." |
| | | Suggestions: "Mom of 2 going through cancer treatment" |
| **Condition** | Diagnosis | "What are you dealing with?" |
| | | Dropdown with common conditions + "Other" |
| | Started | "When did your journey begin?" |
| | | Month/Year picker |
| | Status | "Where are you in treatment?" |
| | | Options: Newly diagnosed, In treatment, In remission, Managing chronic condition |
| **Divider** | | ─────────────── |
| **FAQ Setup** | Header | "Help your followers understand" |
| | Subheader | "Answer common questions so they don't have to ask" |

---

### Screen 5: FAQ Editor (Patient View)
**Patient answers/edits FAQ items**

| Element | Content |
|---------|---------|
| Header | "Your FAQ" |
| Subheader | "These answers help your Care Circle know how to support you" |
| **AI Suggestions** | Based on condition, show suggested questions |
| | "We suggest these based on your diagnosis" |
| **Required questions** | |
| Q1 | "What is [condition]?" |
| | AI pre-fill: [explanation] |
| | [Edit] [Accept as-is] |
| Q2 | "What treatment are you on?" |
| | [Add your answer] |
| Q3 | "How can people help?" |
| | [Add your answer] |
| **Optional questions** | |
| Q4 | "What should people avoid asking?" |
| Q5 | "How do you prefer to communicate?" |
| Q6 | "What gives you strength?" |
| **Custom** | [+ Add your own question] |
| **Preview** | "See how followers will see this" |
| **Save** | [Save Profile] |

---

### Screen 6: FAQ AI Assistance
**How AI helps with FAQ content**

| Scenario | AI Behavior |
|----------|-------------|
| **Condition explanation** | Generate medical-accurate but friendly explanation |
| | "Triple-negative breast cancer is..." |
| | Patient can edit or accept |
| **Treatment description** | Suggest based on recorded appointments |
| | "Based on your appointments, it looks like you're on [treatment]" |
| | Patient confirms or corrects |
| **Next appointment** | Auto-populate from calendar |
| | Always current |
| **How to help** | Suggest common helpful actions |
| | "Common ways people help: meals, rides, errands, company" |
| | Patient personalizes |

---

### Screen 7: Profile Visibility Settings
**Patient controls what's shown**

| Setting | Options |
|---------|---------|
| **Photo** | Show to followers / Hide |
| **Bio** | Show to followers / Hide |
| **Condition details** | Full details / Basics only / Hide |
| **Treatment info** | Show current treatment / Hide |
| **Next appointment** | Show date & time / Show date only / Hide |
| **FAQ visibility** | Per-question: Show / Hide |
| **Update history** | Show all / Recent only / Hide |

---

## Profile Content States

### State 1: Empty Profile
```
[Default Avatar]
[Name]

"Profile coming soon"

[Name] hasn't set up their profile yet.

[Send Support] [Offer Help]
```

### State 2: Basic Profile
```
[Photo]
[Name]
[Bio]

──────────────────

No FAQ set up yet.

[Send Support] [Offer Help]
```

### State 3: Complete Profile
```
[Photo]
[Name]
[Bio]

About [Name]'s Journey
• Diagnosis: [condition]
• Status: [status]
• Started: [date]

──────────────────

📋 Frequently Asked Questions
▶ What is [condition]?
▶ What treatment are they on?
▶ How can I help?
▶ When is the next appointment?

──────────────────

[Send Support] [Offer Help]

──────────────────

Recent Updates
[3 most recent updates]
[View all updates]
```

---

## Profile Update Triggers

| Event | Profile Update | Notification to Followers |
|-------|----------------|---------------------------|
| Patient adds photo | Photo appears | None (subtle change) |
| Patient updates bio | Bio updates | None (subtle change) |
| Patient answers FAQ | FAQ expands | Optional: "[Name] updated their profile" |
| New appointment added | "Next appointment" updates | Optional notification |
| Treatment status changes | Status updates | Consider notification |
| Patient shares update | Appears in "Recent Updates" | Standard update notification |

---

## Edge Cases

### Follower wants info not in profile
- "Ask [Name]" link for unanswered questions
- Opens message thread (if available)
- Or: "Send a card with your question"

### Patient overshares medical details
- AI review for sensitive content (optional)
- Gentle suggestion: "This is very detailed. Are you sure you want to share?"
- Always patient's choice

### FAQ content is outdated
- Patient reminder: "Your FAQ was last updated X days ago"
- Prompt after appointments: "Update your FAQ?"
- Next appointment auto-updates

### Multiple conditions
- Support multiple condition entries
- Separate FAQ sections per condition
- Or: Combined FAQ with condition context

### Patient wants different profiles for different followers
- V2: One profile for all (descoped per-person sharing)
- Future consideration for V3

---

## Analytics Events

| Event | Trigger | Properties |
|-------|---------|------------|
| `profile_viewed` | Follower opens profile | patient_id, viewer_id |
| `faq_item_expanded` | Follower taps FAQ item | question_type |
| `faq_item_collapsed` | Follower closes FAQ item | question_type, time_open |
| `profile_action_taken` | Send support / Offer help | action_type |
| `profile_setup_started` | Patient begins setup | - |
| `profile_photo_added` | Photo uploaded | - |
| `profile_bio_added` | Bio saved | length |
| `faq_answered` | Patient answers FAQ | question_type, ai_assisted |
| `profile_completed` | All required fields done | time_to_complete |
| `profile_updated` | Any profile change | field_changed |

---

## Success Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Profile completion rate | % patients who complete profile | 50%+ |
| FAQ answer rate | % suggested FAQs answered | 60%+ |
| Profile view rate | Views per follower per week | 2+ |
| Time on profile | Average time viewing | 30+ seconds |
| Action from profile | % views → action (support/help) | 15%+ |

---

## Open Questions

1. **FAQ depth**: How much medical detail is appropriate? Should we limit?
2. **Profile sharing**: Can patient share profile publicly (beyond Care Circle)?
3. **Profile updates**: How to notify followers without being noisy?
4. **Multiple languages**: FAQ content in follower's language or patient's?

---

## Related Flows
- [Flow 1: Follower Activation](01-follower-activation.md) - Profile is destination after connecting
- [Flow 2: Patient Activation](02-patient-activation.md) - Profile setup prompt
- [Flow 4: First Connection Celebration](04-first-connection.md) - Profile shown after connection
- [Flow 5: Reactions](05-reactions.md) - Actions from profile page
