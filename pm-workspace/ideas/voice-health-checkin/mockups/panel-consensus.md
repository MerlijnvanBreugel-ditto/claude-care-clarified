# Expert Design Panel Review: Voice Health Check-in

**Review Date**: 2026-02-01
**Feature**: Voice Health Check-in for Ditto Patient App
**Reviewer Panel**: Jony Ive, Paula Scher, Mike Kresch, Alan Dye, Alex Schleifer

---

## Panel Members

| Expert | Background | Lens |
|--------|------------|------|
| **Jony Ive** | Former Apple CDO | Inevitability, reduction, material honesty |
| **Paula Scher** | Pentagram Partner | Typography, bold graphics, communication |
| **Mike Kresch** | Headspace VP Design | Wellness, calm, mental health UX |
| **Alan Dye** | Apple VP Human Interface | iOS conventions, platform consistency |
| **Alex Schleifer** | Former Airbnb VP Design | Emotional connection, belonging, trust |

---

## Direction A: On-Brand (Strictly Ditto)

### Panel Ratings

| Expert | Rating | One-Line Verdict |
|--------|--------|------------------|
| Jony Ive | 3/5 | "Safe, but not inevitable. The waveform could be bolder." |
| Paula Scher | 3/5 | "Typography is functional, not expressive. The status text could work harder." |
| Mike Kresch | 3/5 | "Calm enough, but cards feel clinical. Where's the warmth?" |
| Alan Dye | 4/5 | "Solid iOS patterns. Tab bar provides orientation. Respects the platform." |
| Alex Schleifer | 3/5 | "Trustworthy, but not lovable. No emotional hook." |

**Average: 3.2/5**

### Detailed Feedback

#### Jony Ive - Inevitability & Reduction
**Praise:**
- The card-based system is honest about its structure
- Color palette restraint shows discipline
- Clear hierarchy between status, conversation, and action

**Critique:**
- The waveform visualization feels arbitrary - why this shape?
- Two buttons at the bottom create unnecessary choice
- The tab bar is a distraction in a voice-first experience
- "Can we make the listening state feel truly singular? One moment, one purpose?"

**Recommendation:** Remove the Pause button. If users need to pause, they can simply stop talking. Reduce to one inevitable action: "I'm Done."

#### Paula Scher - Typography & Communication
**Praise:**
- Clean type hierarchy
- Status indicator is readable
- AI/User message differentiation works

**Critique:**
- "LISTENING" in caps with a dot is generic - every app does this
- The greeting "How are you feeling today?" could be more personal
- Numbers (4/10) reduce human experience to metrics too quickly
- "Where's the personality? This could be any health app."

**Recommendation:** Make "LISTENING" typographically distinctive - perhaps larger, centered, with more breath around it. Consider a warmer first message from the AI.

#### Mike Kresch - Wellness & Calm
**Praise:**
- Soft colors are appropriate for healthcare
- White space is generous
- Not overwhelming

**Critique:**
- Cards create visual boundaries that feel clinical, not compassionate
- Missing the "exhale" moment - where do users release tension?
- The tab bar keeps users tethered to "app mode" vs. "care mode"
- "At Headspace, we remove navigation during meditation. This should feel like a moment apart."

**Recommendation:** Consider hiding the tab bar during voice check-in. Add a subtle animation to the status area that syncs with breathing.

#### Alan Dye - iOS Conventions
**Praise:**
- Tab bar pattern is correct for main views
- Touch targets are appropriately sized
- Back and help icons are standard iOS
- Status bar treatment is proper

**Critique:**
- The waveform card doesn't follow any iOS convention - custom elements need extra care
- Bottom button area could use more padding for thumb reach
- No clear loading/thinking state shown

**Recommendation:** Ensure waveform responds to actual voice amplitude. Add haptic feedback when state changes.

#### Alex Schleifer - Emotional Connection
**Praise:**
- Trust is established through familiarity
- The structure suggests reliability
- AI message tone is appropriate

**Critique:**
- No delight moments - when would a user smile?
- The navy user bubble feels like sending a form, not sharing feelings
- Missing any sense of "someone is really listening to me"
- "This feels transactional. Healthcare, especially for chronic patients, needs to feel like care."

**Recommendation:** Add a subtle animation when AI "receives" user message. Consider a warmer color for user's words. Add a gentle celebration when check-in completes.

---

## Direction B: Chat-Forward (Partly On-Brand)

### Panel Ratings

| Expert | Rating | One-Line Verdict |
|--------|--------|------------------|
| Jony Ive | 2/5 | "Too busy. The screen is fighting for attention." |
| Paula Scher | 4/5 | "Chat bubbles create rhythm. Quick replies are smart typography." |
| Mike Kresch | 2/5 | "Feels like work. Where's the space to breathe?" |
| Alan Dye | 4/5 | "Messaging patterns are well-established. Users will know what to do." |
| Alex Schleifer | 4/5 | "Conversational! Finally feels like talking to someone." |

**Average: 3.2/5**

### Detailed Feedback

#### Jony Ive
**Praise:**
- Real-time transcription is honest feedback
- Avatar adds presence

**Critique:**
- Too many UI elements competing
- Quick replies, input bar, mic button, send button, tab bar - chaos
- "A voice interface shouldn't have this many touch targets"

**Recommendation:** Choose: voice OR chat. Don't split attention. If voice-first, remove text input entirely.

#### Paula Scher
**Praise:**
- Chat rhythm creates visual interest
- Quick reply chips are scannable
- Timestamp hierarchies work
- "The conversation flow reads well - like a good interview"

**Critique:**
- Could push the AI avatar design further
- Input bar is generic

**Recommendation:** Give the AI a distinctive visual identity. Custom mic icon design.

#### Mike Kresch
**Praise:**
- Familiar pattern reduces learning curve
- Suggested responses lower cognitive burden for fatigued users

**Critique:**
- Screen feels crowded
- No breathing room
- "This is a tool, not a companion. At Headspace we never show this many elements during a session."

**Recommendation:** Collapse quick replies when user starts speaking. Create more negative space.

#### Alan Dye
**Praise:**
- Messages pattern follows iOS conventions
- Input accessory view pattern is correct
- Keyboard awareness implied

**Critique:**
- Mixing voice and text paradigms may confuse users
- Status in header is too subtle

**Recommendation:** Make voice mode a clear "state" - perhaps dim the text input when voice is active.

#### Alex Schleifer
**Praise:**
- Feels like a real conversation
- History visible creates context
- Quick replies reduce friction
- "I can imagine forming a relationship with this AI"

**Critique:**
- The clinical content (symptoms, 4/10) contrasts with conversational UI
- Healthcare trust may conflict with casual chat patterns

**Recommendation:** Rewrite AI copy to feel more conversational. "That doesn't sound fun" vs. "I'm sorry to hear about your headache."

---

## Direction C: Immersive Wellness (Experimental)

### Panel Ratings

| Expert | Rating | One-Line Verdict |
|--------|--------|------------------|
| Jony Ive | 5/5 | "This is inevitable. The orb IS the interface." |
| Paula Scher | 4/5 | "Bold choice. The minimal text forces visual communication." |
| Mike Kresch | 5/5 | "This is what wellness should feel like. I want to use this." |
| Alan Dye | 2/5 | "Where am I? How do I navigate? This breaks too many conventions." |
| Alex Schleifer | 5/5 | "Finally, an app that treats chronic patients like humans, not data points." |

**Average: 4.2/5**

### Detailed Feedback

#### Jony Ive
**Praise:**
- The orb is inevitable - it must exist
- Nothing can be removed without losing meaning
- Full-screen gradient is brave and correct
- "This respects the gravity of the moment - someone sharing their health"
- Material honesty: the orb IS the AI's attention

**Critique:**
- Timer in corner is the only element I'd question
- "I'm finished" button could be even softer

**Recommendation:** Consider voice activation for "I'm finished" as the primary path. The button is a fallback. Perfection.

#### Paula Scher
**Praise:**
- Restraint is a statement
- The orb communicates more than paragraphs
- "I'm listening" at this scale is powerful
- Serif typography adds warmth and humanity

**Critique:**
- Floating transcript feels separate - could integrate better
- Color palette is beautiful but may need accessibility testing

**Recommendation:** Let transcript text emerge FROM the orb, not below it. Typography is doing good work here.

#### Mike Kresch
**Praise:**
- "This is what I wish every health app looked like"
- Breathing orb will calm users automatically
- No distractions - just presence
- Full-screen commitment shows the experience matters
- "This could change how people feel about health tracking"

**Critique:**
- Users may need onboarding for this paradigm
- Some users want to see data - consider a "peek" mode

**Recommendation:** Build this. Add gentle onboarding that explains the orb. Maybe haptic pulse synced with orb breathing.

#### Alan Dye
**Praise:**
- Confidence of vision
- Animation potential is high
- Accessibility focus mode compatibility

**Critique:**
- No visible navigation is disorienting
- Users may feel lost in the app
- iOS conventions exist for a reason
- How does this connect to the rest of Ditto?
- "Users need wayfinding"

**Recommendation:** Add a subtle gesture hint to exit. Ensure VoiceOver can describe the orb meaningfully. Test with users who are new to wellness apps.

#### Alex Schleifer
**Praise:**
- "This is the most emotionally intelligent health interface I've seen"
- Chronic patients are exhausted by forms - this respects that
- The orb feels like presence, not surveillance
- Creates space for vulnerability
- "I would share things with this interface I wouldn't type"

**Critique:**
- May be too different for some Ditto users
- The transition from dashboard to this is jarring

**Recommendation:** Consider a transition animation that "opens" into this space from the home screen. Create emotional continuity.

---

## Panel Consensus

### Overall Rankings

| Rank | Direction | Average Score | Panel Verdict |
|------|-----------|---------------|---------------|
| 1 | **Direction C: Immersive** | 4.2/5 | "The future of health UX" |
| 2 | Direction A: On-Brand | 3.2/5 | "Safe but unremarkable" |
| 2 | Direction B: Chat-Forward | 3.2/5 | "Familiar but crowded" |

### Key Insights

1. **Voice-First Demands Voice-First Design**: The panel agreed that mixing voice and text paradigms (Direction B) creates confusion. Choose one.

2. **Healthcare Needs More Humanity**: Multiple panelists noted that chronic patients deserve experiences that feel caring, not clinical.

3. **The Orb is Compelling**: Every panelist engaged deeply with Direction C's orb concept. It provoked strong reactions (positive from most, concern from Alan).

4. **Navigation vs. Immersion Trade-off**: Alan's concerns about iOS conventions are valid but may be outweighed by the emotional benefits for this specific use case.

5. **Accessibility is Non-Negotiable**: All directions need robust VoiceOver support, but Direction C especially needs careful attention.

### Recommendation

**Proceed with Direction C (Immersive Wellness)** with the following modifications:

1. **Address Navigation Concerns**:
   - Add subtle swipe-down gesture to exit
   - Include gentle onboarding for first-time users
   - Create smooth transition animation from home screen

2. **Maintain Brand Connection**:
   - Use Ditto's navy (#0D164F) as a grounding color
   - Keep yellow (#F3DE70) as accent
   - Consider a small Ditto wordmark somewhere subtle

3. **Accessibility Enhancements**:
   - Ensure orb animation can be disabled (Reduce Motion)
   - VoiceOver should describe orb state meaningfully
   - Haptic feedback for state changes

4. **User Testing Priority**:
   - Test with chronic fatigue patients
   - Test with users new to wellness apps
   - Test exit/navigation discoverability

5. **Hybrid Consideration**:
   - For users who want more control, offer "Detailed Mode" (Direction A patterns) in settings
   - Default to immersive, allow opt-out

---

## Individual Expert Recommendations

### Jony Ive's Final Word
"Direction C is the answer to the question 'What should a voice health interface be?' Everything else is a compromise. Build it."

### Paula Scher's Final Word
"The typography in Direction C needs refinement, but the restraint is correct. Let the visual language do the emotional work."

### Mike Kresch's Final Word
"This could be Headspace for physical health. The breathing orb will become iconic if executed well. Please build this."

### Alan Dye's Final Word
"I have concerns, but I respect the vision. If you build Direction C, please invest heavily in the transition experience and accessibility. Don't abandon iOS users."

### Alex Schleifer's Final Word
"Direction C treats patients as people who need comfort, not users who need productivity. This is the future of healthcare design. Lead the way."

---

## Next Steps

1. **Iterate on Direction C** with panel feedback incorporated
2. **Create transition animation prototype** (home -> immersive check-in)
3. **Build accessibility specification** for the orb component
4. **User test with 5-8 chronic patients**
5. **Design onboarding flow** for immersive mode

The panel has spoken. Direction C is the path forward.
