# Care Circle V2 - Design Decisions

## Vision
**"Polarsteps for Healthcare"** — Keeping loved ones in the loop on your healthcare journey

Unlike WhatsApp messages that feel ephemeral, Care Circle creates meaningful **assets** (cards, updates, profiles) that show care and commitment.

---

## Core Design Principles

### 1. Assets > Messages
Creating something tangible (card, profile, update) = commitment + meaning

**Why this matters**:
- A WhatsApp message is forgotten in hours
- An invitation card shows you took time to create something
- A profile is a gift of context to your Care Circle
- Support cards are "digital get-well cards" — kept and treasured

**Application**:
- Invitations are cards, not links
- Reactions include card creation, not just emojis
- Profiles are living documents, not just account info

### 2. Social Proof Builds Trust
"40% of patients already share summaries with loved ones"

**Why this matters**:
- Users worry they're being weird or intrusive
- Knowing others do this normalizes the behavior
- Reduces friction at key decision points

**Application**:
- Onboarding includes statistics and stories
- "Join X others who follow someone" messaging
- Success stories from real families

### 3. Commitment/Intention First
Ask "why do you want to follow?" before enabling action

**Why this matters**:
- Users who articulate intention are more committed
- Helps personalize the experience
- Pre-fills content based on stated goals
- Creates emotional investment

**Application**:
- Intention selection in both patient and follower onboarding
- Pre-filled messages match stated intentions
- Analytics track intention → behavior correlation

### 4. One-to-Many Sharing (Not 1:1)
Share to ALL followers with customizable detail level

**Why this matters**:
- Per-person sharing is too complex for V2
- Most patients want everyone to get the same info
- Reduces cognitive load on already-stressed patients
- Short vs. full summary covers 80% of sharing needs

**Application**:
- No per-follower visibility controls (V2)
- Summary options: Full / Short / Custom
- All followers in one Care Circle

### 5. Cards Are Reusable
Same mechanism for invitations AND reactions

**Why this matters**:
- Consistent UX pattern = easier to learn
- Reduces development complexity
- Cards feel special in both contexts
- Creates visual consistency

**Application**:
- Invitation card flow → Support card flow (same component)
- Visual style options shared between both
- Message customization works identically

---

## Key Design Decisions

### Decision 1: Invitation Method

| Option | Chosen | Rationale |
|--------|--------|-----------|
| **Cards** | ✅ Yes | Creates commitment, solves empty state, more meaningful |
| Links only | ❌ No | Too transactional, easily ignored |
| Email invitation | ❌ No | Low open rates, feels corporate |
| SMS invitation | ❌ No | Too personal for sensitive topic |

**Implementation**:
- Visual style picker (6-8 options)
- Pre-filled messages based on intention
- Shareable image + deep link
- In-app record of sent invitations

---

### Decision 2: Reaction Mechanism

| Option | Chosen | Rationale |
|--------|--------|-----------|
| **Cards + Emojis** | ✅ Yes | Cards for meaningful, emojis for quick |
| Emojis only | ❌ No | Feels cheap for serious health news |
| Comments only | ❌ No | Too high friction, can feel intrusive |
| No reactions | ❌ No | Followers feel helpless |

**Implementation**:
- 3 emoji options: ❤️ 🤗 💪
- Support card creation (same as invitation flow)
- Help offers with categories
- All visible to patient in one place

---

### Decision 3: Profile Timing

| Option | Chosen | Rationale |
|--------|--------|-----------|
| **After first share** | ✅ Yes | Don't overwhelm onboarding |
| During onboarding | ❌ No | Too much friction, abandonment risk |
| Never (optional only) | ❌ No | Profile provides value to followers |

**Implementation**:
- Soft prompt after first connection accepted
- Gentle reminder after first shared update
- Profile shown to followers even if incomplete
- AI assists with FAQ generation

---

### Decision 4: Per-Person Sharing

| Option | Chosen | Rationale |
|--------|--------|-----------|
| **Descoped (V2)** | ✅ Yes | Too complex; short/full summary covers 80% of need |
| Full per-person control | ❌ No | High complexity, low validated need |
| Groups/Circles | ❌ No | Deferred to V3 |

**Implementation**:
- V2: One Care Circle, all followers see same content
- Summary options provide flexibility: Full / Short / Custom
- V3 consideration: Inner circle / Outer circle

---

### Decision 5: Calendar Integration

| Option | Chosen | Rationale |
|--------|--------|-----------|
| **Export only (V1)** | ✅ Yes | Most users have calendar already |
| Full sync (import + export) | ❌ No | High complexity, privacy concerns |
| No integration | ❌ No | Missed opportunity for convenience |

**Implementation**:
- "Add to calendar" button for appointments
- Export to Google Calendar, Apple Calendar
- No automatic import (user adds manually)

---

### Decision 6: Follower Discovery Tab

| Option | Chosen | Rationale |
|--------|--------|-----------|
| **Education cards (existing)** | ✅ Yes | Pragmatic, provides value while waiting |
| Empty state only | ❌ No | Feels abandoned, no reason to return |
| AI-generated content | ❌ No | Too complex for V2 |

**Implementation**:
- Move existing blue cards to discovery
- Content about supporting loved ones
- Tips for being a good follower
- Condition-specific resources (when known)

---

## Feature Priority Matrix

### V2 (Current Release)

| Feature | Priority | Status |
|---------|----------|--------|
| Personal context/notes | High | ✅ In spec |
| Short update option | High | ✅ In spec |
| Simple reactions (emoji) | High | ✅ In spec |
| Support cards | High | ✅ In spec |
| Better follower onboarding | High | ✅ In spec |
| Timeline overview | High | ✅ In spec |
| Profile page with FAQ | High | ✅ In spec |
| Invitation cards | High | ✅ In spec |
| Help offers | Medium | ✅ In spec |

### V3 (Future Consideration)

| Feature | Priority | Reason for Descope |
|---------|----------|-------------------|
| Shared calendar/tasks | Medium | High complexity, caregiver coordination |
| Groups/Circles | Medium | Per-person sharing needs validation |
| Status indicator | Low | "Today I'm..." not validated |
| Bidirectional following | Low | Edge case, needs research |
| Message threads | Low | Could compete with existing messaging |

---

## Descoped Features (with Rationale)

### 1. Per-Person Sharing Controls
**What**: Choose what each specific follower can see
**Why descoped**:
- Adds significant complexity to sharing flow
- User research shows 80% just want "share with everyone"
- Short/full summary provides sufficient granularity
- Can reconsider for V3 with circles/groups

### 2. Caregiver Calendar/Task Coordination
**What**: Shared task list, appointment sign-ups, schedules
**Why descoped**:
- Very high complexity
- Requires coordination features (who's doing what)
- Existing tools (Google Calendar, Meal Train) serve this
- Not validated as critical need

### 3. Status Indicator
**What**: "Today I'm feeling..." quick status
**Why descoped**:
- Not validated in user research
- Could feel like obligation to update
- Personal notes in updates serve similar purpose
- May reconsider based on V2 feedback

### 4. Message Threading
**What**: Direct messaging between patient and followers
**Why descoped**:
- Competes with WhatsApp, iMessage, etc.
- Users already have messaging tools
- Focus should be on async updates, not real-time chat
- Help offers provide structured communication

---

## Open Questions for Validation

### Must Validate Before Launch

1. **Card visuals**: Are flowers too feminine? Test with diverse user groups
2. **Emoji set**: Are ❤️ 🤗 💪 the right 3 options?
3. **FAQ depth**: How much medical detail is appropriate?
4. **Profile completion**: What's minimum viable profile?

### Research Questions for V3 Planning

1. **Bidirectional following**: Do patients want to follow their followers?
2. **Group messaging**: Is there need for Care Circle group chat?
3. **Caregiver coordination**: How do families currently coordinate help?
4. **Multi-patient following**: How to handle following multiple patients?

---

## Success Criteria

### V2 Launch Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Invitation sent rate | 60%+ | % users who send ≥1 invitation |
| Invitation acceptance rate | 40%+ | % invitations that convert |
| Card creation rate | 20%+ | % reactions that are cards (vs emoji only) |
| Profile completion | 50%+ | % patients who complete profile |
| Follower retention (D7) | 40%+ | % followers who return after 7 days |
| Patient retention (D30) | 50%+ | % patients active after 30 days |

### Qualitative Success Indicators

- Patients report feeling "less burdened"
- Followers report feeling "more connected"
- Invitation cards shared on social media
- Organic word-of-mouth referrals
- Support cards described as "meaningful"

---

## Technical Dependencies

### Backend Requirements

1. **Card generation service**
   - Server-side image rendering
   - Multiple resolution outputs
   - Template management system

2. **Deep linking infrastructure**
   - Unique invite codes
   - App store redirect logic
   - Tracking (created, clicked, accepted)

3. **Notification system**
   - Push notifications for updates
   - In-app notification center
   - Email fallback (optional)

4. **Profile data model**
   - Bio, photo, condition
   - FAQ items (AI-assisted)
   - Visibility settings

### Frontend Requirements

1. **Card creation component**
   - Reusable for invitations and reactions
   - Visual style picker
   - Message customization

2. **Profile page**
   - Patient edit view
   - Follower read view
   - FAQ accordion

3. **Reaction system**
   - Emoji picker
   - Card creation flow
   - Help offer form

---

## Risk Mitigation

### Risk: Low Invitation Acceptance Rate
**Mitigation**:
- A/B test card designs
- Optimize landing page
- Follow-up reminders (gentle)
- Research why people don't accept

### Risk: Profile Abandonment
**Mitigation**:
- AI-assisted content generation
- Progressive disclosure (minimal required)
- Reminders tied to connection moments
- Show value to patient (FAQ reduces questions)

### Risk: Reaction Fatigue
**Mitigation**:
- Limited emoji options (3)
- Cards require effort (filters low-quality)
- Grouped display (not overwhelming)
- Patient can disable reactions

### Risk: Privacy Concerns
**Mitigation**:
- Clear sharing controls
- No public profiles (V2)
- Delete/revoke follower access
- Transparent about what's shared

---

## Appendix: Research References

### Lyssna Research Summary
- 40% of patients already share medical info with family
- Top ask: "personal context" beyond medical facts
- Followers anxious about "what can I do?"
- Cards preferred over plain links

### Meeting Transcript Insights
- Ilayda: Focus on "assets over messages"
- Inês: Profile page critical for follower value
- Team: Descope per-person sharing for V2
- Consensus: Cards mechanism is reusable and valuable

### Competitive Analysis
- Polarsteps: Journey-based sharing, visual stories
- CaringBridge: Updates + guestbook, feels dated
- Lotsa Helping Hands: Task coordination, complex
- **Opportunity**: Modern, mobile-first, cards-based approach
