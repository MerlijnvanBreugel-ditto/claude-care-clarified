# Mobbin Research: Voice Health Check-in UI Inspiration

**Date**: 2026-02-01
**Research Focus**: Voice assistant UI, health tracking, AI conversation interfaces, wellness app design

---

## 1. Voice Recording & Assistant UI Patterns

### Key Findings from [Mobbin Audio Recorder Screens](https://mobbin.com/explore/mobile/screens/audio-video-recorder)

**Common Patterns:**
- **Microphone-centric design**: Large, central microphone button is the universal standard
- **Voice search modals**: Overlay prompts with clear "speak now" indicators
- **Waveform visualization**: Audio player patterns show waveforms with real-time feedback
- **Status indicators**: Clear visual states for listening, processing, and responding

**Best Practices:**
1. Modal overlays work well for focused voice input
2. Hold-to-speak vs tap-to-speak both common - tap better for accessibility
3. Cancel button always visible and accessible
4. Real-time transcription improves user confidence

### ChatGPT Voice Mode Evolution (2025)

**Previous Design:**
- Full-screen takeover with animated "orb" visualization
- Separate interface from chat
- No visible transcript by default (optional captions)
- Immersive but disconnected from conversation history

**New Integrated Design (Nov 2025):**
- Voice mode lives inside standard chat view
- Live transcript appears in real-time
- Maps, photos, links appear alongside voice response
- Waveform icon next to text field activates voice
- One-tap activation, zero configuration
- Option to revert to "Separate Mode" in settings

**Key Insight**: The industry is moving AWAY from full-screen voice UIs toward integrated experiences that maintain context. However, for a calm, healthcare-focused app, the full-screen approach may still be appropriate for reducing cognitive load.

---

## 2. Health Tracking App Patterns

### From [Mobbin Health & Fitness Apps](https://mobbin.com/explore/mobile/app-categories/health-fitness)

**Dashboard Design Patterns:**

| App | Key Pattern | Relevant for Ditto |
|-----|-------------|-------------------|
| **Apple Health** | Summary with favorites, steps/distance prominent | Simple data cards, edit button |
| **MacroFactor** | Multi-metric dashboard with progress tracking | Scale weight, nutrition, progress sections |
| **Google Fit** | Health summary with home navigation | Clean summarized view |
| **Ultrahuman** | Rich metrics dashboard (HR, HRV, temp) | Health metric visualization |
| **Withings Health Mate** | Multi-step logging flow, cycle tracking | Step-by-step data entry |
| **Lifesum** | Onboarding flow for personalized tracking | Progressive disclosure |

**Best Practices for Health Data:**
1. Card-based layouts for different metric categories
2. Visual progress indicators (bars, rings, streaks)
3. Timestamps are critical - "when" matters as much as "what"
4. Edit/correct functionality always available
5. Trend visualization with time filters (week/month/year)

---

## 3. AI Conversation Interface Patterns

### From [Mobbin Chat Bot Designs](https://mobbin.com/explore/mobile/screens/chat-bot)

**Featured Apps with AI Chat:**
- Amazon Shopping, Cleo, ZARA, Lemonade Insurance, Ada, **Claude**
- Notion AI, ChatGPT, Microsoft Copilot, WhatsApp Meta AI

**Common UI Elements:**
- Text fields with send button
- Chat bubbles with clear sender differentiation
- Typing indicators (animated dots)
- Suggested prompts/quick replies
- File/image attachment support

**Voice-Specific from [ChatGPT Android Voice Flow](https://mobbin.com/explore/flows/dc7f400c-7457-4fcb-97b7-3c594f9d294b):**
- Voice selection before conversation
- Transcribed conversation visible
- Real-time waveform during speaking

---

## 4. Meditation & Wellness App Design (Calm, Headspace)

### Headspace Design Language

From [Headspace Mobbin Collection](https://mobbin.com/explore/flows/0d7bf169-6035-4bfe-b62a-8c1d777bab6d):

**Key UI Patterns:**
- **Immersive backgrounds**: Full-screen gradients/illustrations
- **Large touch targets**: Big play buttons, minimal navigation
- **Progress tracking**: Session completion, streaks, achievements
- **Illustrations**: Friendly, hand-drawn characters
- **Soft animations**: Breathing circles, gentle transitions
- **Bottom sheets**: For detailed information without navigation

**Flows Observed:**
1. Meditate Flow - Category exploration, recommendations, group sessions
2. Completing a Session - Selection, completion, feedback, marked complete
3. Group meditation joining - Social features within calm context

### Calm Design Language

From [Calm Mobbin Collection](https://mobbin.com/apps/calm-ios-3230191e-73d8-430e-811a-0fbdd39628c1/):

**Brand Colors:**
| Color | Hex | Usage |
|-------|-----|-------|
| Cloud Burst | #1B2250 | Primary deep blue |
| Havelock Blue | #6282E3 | Accent blue |
| White | #FFFFFF | Backgrounds, text |

**Key UI Patterns:**
- **Exercise Start Screen**: Large play button, exercise details prominent
- **Episode Lists**: Clear hierarchy, prominent play button
- **Sleep Sessions**: List format with "play next" CTA
- **Dark mode friendly**: Deep blues create nighttime ambiance

**Note**: Calm's Cloud Burst (#1B2250) is remarkably similar to Ditto's Primary (#0D164F)!

---

## 5. Synthesis: Design Recommendations for Voice Health Check-in

### Voice Check-in Screen Recommendations

**Must-Have Elements:**
1. **Central status indicator** - Large, clear state communication (Listening/Thinking/Responding)
2. **Real-time feedback** - Waveform or orb animation during voice capture
3. **Visible transcript** - Both AI and user speech should be readable
4. **Escape hatch** - Clear "back" and "done" buttons always accessible
5. **Calm aesthetic** - Healthcare context demands reduced visual stress

**Three Potential Directions:**

#### Direction A: On-Brand (Ditto-Native)
- Use Ditto's existing card patterns from Carepath
- Waveform in gradient style (#F3DE70 to #BEAEF8)
- Tab bar remains visible
- Page header pattern with back/help icons
- AI messages in white cards, user messages in navy

#### Direction B: Chat-Forward (Mobbin-Inspired)
- Keep Ditto navy and yellow colors
- More prominent conversation view
- Smaller waveform, integrated into header
- ChatGPT-style transcript appearing in real-time
- Suggested responses/quick actions at bottom

#### Direction C: Immersive Wellness (Headspace/Calm-Inspired)
- Full-screen gradient background (no tab bar)
- Large, centered "breathing" orb animation
- Minimal UI - just essential elements
- Focus on user's emotional state
- Transcript as overlay or post-session

### Home/Dashboard Recommendations
- Streak visualization (Headspace-style completion tracking)
- Recent check-ins as cards (Apple Health pattern)
- Prominent FAB for voice check-in
- Time-aware greeting (morning/afternoon/evening)

### Session Summary Recommendations
- Expandable symptom cards (MacroFactor pattern)
- Mood/energy as visual icons (weather metaphors)
- Severity bars with color coding (green/yellow/red)
- "View transcript" link for full context

---

## Sources

- [Mobbin Mobile Explorer](https://mobbin.com/explore/mobile)
- [Audio & Video Recorder Screens](https://mobbin.com/explore/mobile/screens/audio-video-recorder)
- [AI App Designs](https://mobbin.com/explore/mobile/app-categories/ai)
- [Health & Fitness Apps](https://mobbin.com/explore/mobile/app-categories/health-fitness)
- [Mobile Chat Bot Designs](https://mobbin.com/explore/mobile/screens/chat-bot)
- [Headspace iOS Meditate Flow](https://mobbin.com/explore/flows/0d7bf169-6035-4bfe-b62a-8c1d777bab6d)
- [Headspace Session Completion](https://mobbin.com/explore/flows/a7d6a68b-d9af-4e4f-8871-c4fa5e2d6922)
- [Calm iOS Screens](https://mobbin.com/apps/calm-ios-3230191e-73d8-430e-811a-0fbdd39628c1/)
- [Calm Brand Colors](https://mobbin.com/colors/brand/calm-com)
- [ChatGPT Voice Mode Integration](https://techcrunch.com/2025/11/25/chatgpts-voice-mode-is-no-longer-a-separate-interface/)
- [ChatGPT-4o Voice Mode Figma](https://www.figma.com/community/file/1398853195066034643/chatgpt-4o-voice-mode)

---

## 6. Stitch Prompt Templates (Ready to Generate)

### Direction A: On-Brand (Ditto-Native)

```
Design a mobile voice check-in screen for a healthcare app called Ditto.

STRICT DESIGN SYSTEM - Match exactly:
- Primary color: #0D164F (deep navy)
- Accent yellow: #F3DE70
- Accent purple: #BEAEF8
- Background: #F1F1F1 with subtle gradient overlay
- Font: Uncut Sans (or Inter as fallback)
- Card border radius: 22px
- Spacing: 16px standard padding

LAYOUT (iPhone 393px width):
- Status bar at top (iOS style)
- Page header: "Check-in" title with back arrow and help icon
- Center: Large waveform visualization area (200px height)
  - Animated sound wave bars in gradient (yellow to purple)
  - Status text below: "LISTENING" in navy
- Below: Conversation area with chat bubbles
  - AI messages: White cards with 22px radius
  - User messages: Navy (#0D164F) cards with white text
- Bottom: Two buttons
  - "Pause" - secondary style (white with navy border)
  - "I'm Done" - primary style (navy background, white text)
- Tab bar at very bottom (Home, Carepath, Loved ones, Settings)

STATES TO SHOW: Listening state with waveform active

MOOD: Calm, trustworthy, healthcare-appropriate, matches existing Ditto app
```

### Direction B: Chat-Forward (Partly On-Brand)

```
Design a mobile voice check-in screen for a healthcare app.

KEEP THESE BRAND ELEMENTS:
- Primary color: #0D164F (deep navy)
- Accent: #F3DE70 (yellow)
- Font: Clean sans-serif
- iOS-native feel

EXPLORE NEW PATTERNS (inspired by ChatGPT, Claude):
- Chat-forward interface (conversation is the hero)
- Smaller waveform integrated into the input area
- Full-screen conversation view (no tab bar during check-in)
- Floating mic button that pulses when listening
- Real-time transcript appearing as user speaks
- AI messages with subtle animation

LAYOUT (iPhone 393px width):
- Minimal header: just back arrow and "Check-in" title
- Large conversation area taking most of screen
  - AI bubble: Light gray (#F5F5F5), rounded
  - User bubble: Navy (#0D164F), rounded
  - Typing indicator: three dots animation
- Bottom input area:
  - Text field with mic icon
  - When recording: waveform replaces text field
  - Yellow accent (#F3DE70) on active mic
- Suggested prompts as chips above input (optional)

STATES TO SHOW: User speaking with live transcript appearing

MOOD: Modern, conversational, friendly but professional
```

### Direction C: Experimental (Wellness/Headspace-Inspired)

```
Design a mobile voice check-in screen for a wellness health app.

COMPLETELY DIFFERENT DIRECTION (Challenge assumptions):
- Inspired by Headspace, Calm meditation apps
- Immersive, full-screen experience
- NO tab bar, NO heavy navigation
- Focus on calm and breathing

COLOR PALETTE:
- Background: Soft gradient (light blue to soft purple)
- Text: Dark navy or charcoal
- Accent: Warm coral or soft gold

LAYOUT (iPhone 393px width):
- Full-screen gradient background
- Top: Simple "X" close button (top right)
- Center: Large breathing orb animation (150px)
  - Subtle pulsing when listening
  - Gentle glow effect
  - Text below: "I'm listening..." in soft font
- Below orb: Minimal transcript area
  - Just the last few exchanges
  - Semi-transparent background
- Bottom: Single "Done" button
  - Soft, rounded, not aggressive
  - "I'm finished" or similar gentle language

STATES TO SHOW: Peaceful listening state with breathing animation

MOOD: Calming, meditative, spa-like, reduces anxiety
No clinical feeling - this should feel like talking to a caring friend
```

---

## 7. Expert Panel Review Framework

For each generated direction, the following experts will review:

### Jony Ive (Former Apple CDO)
**Focus**: Simplicity, inevitability, material honesty
**Questions**:
- Is it inevitable? Does it feel like the only solution that could exist?
- Can anything be removed without losing meaning?
- Does the form honestly express the function?

### Paula Scher (Pentagram Partner)
**Focus**: Typography, boldness, visual identity
**Questions**:
- Is the typography working hard enough?
- Is there enough visual courage?
- Does it have a distinctive point of view?

### Mike Kresch (Headspace Design Lead)
**Focus**: Calm design, user wellbeing, accessibility
**Questions**:
- Does this feel calm or stressful to use?
- Is there adequate breathing room (whitespace)?
- Is it accessible to all users?

### Alan Dye (Apple VP of Human Interface Design)
**Focus**: Consistency, precision, platform conventions
**Questions**:
- Does it respect iOS platform conventions?
- Is every pixel intentional?
- Are touch targets appropriately sized?

### Alex Schleifer (Former Airbnb VP of Design)
**Focus**: Storytelling, emotional design, user journey
**Questions**:
- Does this tell a story?
- Does it create an emotional connection?
- Does it build trust with users?

---

*Research prepared for product-designer agent. Stitch authentication required to generate mockups.*
