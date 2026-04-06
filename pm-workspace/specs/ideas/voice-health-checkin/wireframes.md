# Wireframe Specification: Voice-First Health Check-in

## Overview
**PRD Reference**: voice-health-checkin/prd.md
**Designer**: Wireframe Designer Agent
**Version**: 1.0
**Last Updated**: 2026-01-31

---

## Information Architecture

### Sitemap
```
[Home/Dashboard]
├── [Voice Check-in]
│   ├── [Recording Interface]
│   ├── [AI Conversation]
│   └── [Session Summary]
├── [Daily Notes]
│   ├── [Note Detail View]
│   └── [Transcript View]
├── [Timeline]
│   └── [Date Filter]
├── [Trends]
│   ├── [Symptom Charts]
│   ├── [Mood Charts]
│   └── [Activity Charts]
└── [Settings]
    ├── [Reminders]
    ├── [Sharing]
    └── [Voice Preferences]
```

### Navigation Structure
| Level | Location | Items |
|-------|----------|-------|
| Primary | Bottom Tab Bar | Home, Timeline, Trends, Settings |
| Contextual | Home FAB | Start Check-in (prominent) |
| Contextual | Note Detail | View Transcript, Share, Delete |
| Modal | Check-in Flow | Back (cancel), Complete |

---

## User Flows

### Flow 1: Daily Check-in (Push Notification Entry)

**Entry point**: Push notification tap
**Goal**: Complete a voice health check-in and capture symptoms/mood/notes
**Success state**: Session saved with extracted health data displayed

```
[Push Notification] → [Voice Check-in Screen] → [User speaks] → [AI processes]
                                                                      ↓
                                                              [AI responds]
                                                                      ↓
                                                    ┌─────────────────┴─────────────────┐
                                                    ↓                                   ↓
                                           [Follow-up Q]                    [User says "done"]
                                                    ↓                                   ↓
                                           [Continue loop]                  [Session Summary]
                                                                                       ↓
                                                                            [Save to Timeline]
                                                                                       ↓
                                                                              [Return Home]
```

**Decision points**:
1. AI decides follow-up: Based on content analysis, AI determines if clarification needed
2. User ends session: Explicit "done" or timeout after silence
3. Session timeout: After 2 min inactivity, prompt to continue or save

**Error states**:
1. Microphone permission denied: Show permission request modal with instructions
2. Network error during AI processing: Queue locally, show "will sync when online"
3. Speech recognition failure: Offer text input fallback
4. AI service unavailable: Save audio for later processing, confirm saved

---

### Flow 2: Manual Check-in (Home Screen Entry)

**Entry point**: Home screen FAB button
**Goal**: Initiate check-in without notification
**Success state**: Same as Flow 1

```
[Home Screen] → [Tap FAB] → [Voice Check-in Screen] → [Same as Flow 1...]
```

---

### Flow 3: Review Historical Data

**Entry point**: Timeline tab or Trends tab
**Goal**: Review past check-ins and identify patterns
**Success state**: User views desired historical data

```
[Timeline Tab] → [Scroll/Filter] → [Tap Entry] → [Daily Note View]
                                                        ↓
                                              ┌─────────┴─────────┐
                                              ↓                   ↓
                                    [View Transcript]    [View Extracted Data]
```

---

## Screen Specifications

---

### Screen: Home/Dashboard

**URL/Route**: `/` or `/home`
**Purpose**: Central hub showing recent activity, streak, and quick access to check-in
**Entry points**: App launch, tab navigation, post-check-in redirect
**Exit points**: Start check-in, view note detail, navigate to other tabs

#### Layout (Mobile - Primary)
```
┌─────────────────────────────────────────────────────┐
│  ┌───────────────────────────────────────────────┐  │
│  │  Good morning, [Name]              [Profile]  │  │
│  │  How are you feeling today?                   │  │
│  └───────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  🔥 [7] Day Streak                            │  │
│  │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━                 │  │
│  │  [M] [T] [W] [T] [F] [S] [S]                  │  │
│  │   ✓   ✓   ✓   ✓   ✓   ✓   ○                  │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Recent Check-ins                        [See all]  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  Today, 8:30 AM                               │  │
│  │  ┌─────┐ Mood: Good | Energy: Medium          │  │
│  │  │ ☀️  │ Headache (mild), Fatigue             │  │
│  │  └─────┘ "Slept better last night..."         │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  Yesterday, 9:15 AM                           │  │
│  │  ┌─────┐ Mood: Okay | Energy: Low             │  │
│  │  │ 🌥️  │ Back pain (moderate), Insomnia       │  │
│  │  └─────┘ "Rough night, couldn't sleep..."     │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  Jan 28, 7:45 AM                              │  │
│  │  ┌─────┐ Mood: Great | Energy: High           │  │
│  │  │ ☀️  │ No symptoms reported                 │  │
│  │  └─────┘ "Feeling really good today!"         │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│                    ┌─────────────┐                  │
│                    │             │                  │
│                    │  ( 🎙️ )     │  ← FAB          │
│                    │ Check in    │                  │
│                    └─────────────┘                  │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [🏠]        [📅]        [📊]        [⚙️]          │
│  Home      Timeline     Trends     Settings        │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory

| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Greeting Header | Text + Icon | Yes | Personalized, time-aware |
| 2 | Profile Avatar | Button | Yes | Navigate to profile/settings |
| 3 | Streak Card | Card | Yes | Gamification element |
| 4 | Week Progress | Visual Indicator | Yes | 7-day view with checkmarks |
| 5 | Recent Check-ins List | List | Yes | Last 3-5 entries |
| 6 | Check-in Card | Card | Yes | Preview of daily note |
| 7 | Check-in FAB | Floating Action Button | Yes | Primary CTA |
| 8 | Bottom Navigation | Tab Bar | Yes | 4 primary sections |

#### Component Details

##### Component 1: Greeting Header

**Type**: Text Display
**Purpose**: Personalized welcome, set tone for interaction
**Location**: Top of screen, below status bar

**Content**:
| Element | Content | Character limit |
|---------|---------|-----------------|
| Greeting | "Good [morning/afternoon/evening], [Name]" | 40 |
| Subtext | "How are you feeling today?" | 30 |

**Logic**:
- Morning: 5am-12pm
- Afternoon: 12pm-5pm
- Evening: 5pm-5am

---

##### Component 5: Recent Check-ins List

**Type**: Scrollable List
**Purpose**: Quick access to recent health data
**Location**: Main content area

**Empty State**:
```
┌───────────────────────────────────────────────────┐
│                                                   │
│            No check-ins yet                       │
│                                                   │
│     Start your first check-in to see your        │
│     health data appear here.                     │
│                                                   │
│           [ Start Check-in ]                     │
│                                                   │
└───────────────────────────────────────────────────┘
```

---

##### Component 6: Check-in Card

**Type**: Card (Tappable)
**Purpose**: Display check-in summary, navigate to detail
**Location**: Within Recent Check-ins List

**States**:
| State | Appearance | Behavior |
|-------|------------|----------|
| Default | White background, shadow | Displays data |
| Pressed | Slight scale down, darker | Navigate to detail |
| Today | Subtle highlight border | Indicate current day |

**Content Structure**:
| Element | Content | Character limit |
|---------|---------|-----------------|
| Timestamp | "Today, 8:30 AM" or "Jan 28, 7:45 AM" | 20 |
| Mood Icon | Weather-style emoji | 1 |
| Mood Label | "Mood: [Good/Okay/Poor]" | 15 |
| Energy Label | "Energy: [High/Medium/Low]" | 15 |
| Symptoms | Comma-separated, with severity | 50 (truncate) |
| Preview | First line of transcript | 40 (truncate) |

**Interactions**:
- Tap: Navigate to Daily Note View

**Accessibility**:
- ARIA label: "Check-in from [date], mood [mood], [symptoms count] symptoms"
- Keyboard: Tab to focus, Enter to select
- Screen reader: Reads full summary

---

##### Component 7: Check-in FAB (Floating Action Button)

**Type**: Floating Action Button
**Purpose**: Primary action to start voice check-in
**Location**: Bottom right, above tab bar (or bottom center)

**States**:
| State | Appearance | Behavior |
|-------|------------|----------|
| Default | Circular, primary color, mic icon | Tap to start |
| Pressed | Scale down, ripple effect | Feedback |
| Recording Active | Pulsing animation, red accent | Visual feedback |

**Content**:
| Element | Content | Character limit |
|---------|---------|-----------------|
| Icon | Microphone | N/A |
| Label | "Check in" | 10 |

**Interactions**:
- Tap: Navigate to Voice Check-in Screen
- Long press: Optional quick tips tooltip

**Accessibility**:
- ARIA label: "Start voice check-in"
- Keyboard: Tab to focus, Enter/Space to activate
- Screen reader: "Button, Start voice check-in, double tap to activate"

---

### Screen: Voice Check-in Screen (Main Interaction)

**URL/Route**: `/check-in`
**Purpose**: Primary voice interaction interface for health check-in
**Entry points**: FAB tap, push notification, reminder
**Exit points**: Complete session, cancel/back, timeout

#### Layout (Mobile - Listening State)
```
┌─────────────────────────────────────────────────────┐
│  [←]                                    [?]         │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │                                               │  │
│  │        ╭─────────────────────────╮           │  │
│  │        │                         │           │  │
│  │        │     ~~~~~~~~           │           │  │
│  │        │   ~~~  ▲  ~~~          │           │  │
│  │        │     ~~~~~~~~           │           │  │
│  │        │                         │           │  │
│  │        │   ● LISTENING           │           │  │
│  │        │                         │           │  │
│  │        ╰─────────────────────────╯           │  │
│  │                                               │  │
│  │        Real-time waveform visualization       │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  AI: How are you feeling today? Tell me about │  │
│  │      anything on your mind - symptoms, mood,  │  │
│  │      sleep, or just how your day is going.    │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  You: "I woke up with a headache again this   │  │
│  │        morning, but it's not as bad as..."    │  │
│  │        ● (speaking)                           │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │                                             │    │
│  │     [  Pause  ]        [ I'm Done ]        │    │
│  │                                             │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Layout (Mobile - AI Responding State)
```
┌─────────────────────────────────────────────────────┐
│  [←]                                    [?]         │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │                                               │  │
│  │        ╭─────────────────────────╮           │  │
│  │        │                         │           │  │
│  │        │         ◉◉◉             │           │  │
│  │        │       ◉     ◉           │           │  │
│  │        │      ◉   ◉   ◉          │           │  │
│  │        │       ◉     ◉           │           │  │
│  │        │         ◉◉◉             │           │  │
│  │        │                         │           │  │
│  │        │   ● THINKING...         │           │  │
│  │        │                         │           │  │
│  │        ╰─────────────────────────╯           │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Conversation Area (scrollable)                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  AI: How are you feeling today?               │  │
│  └───────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────┐  │
│  │  You: I woke up with a headache again this    │  │
│  │       morning, but it's not as bad as         │  │
│  │       yesterday. Maybe a 4 out of 10.         │  │
│  └───────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────┐  │
│  │  AI: ●●●                                      │  │
│  │      (typing indicator)                       │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │                                             │    │
│  │     [  Pause  ]        [ I'm Done ]        │    │
│  │                                             │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Layout (Mobile - AI Speaking/Responding)
```
┌─────────────────────────────────────────────────────┐
│  [←]                                    [?]         │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │                                               │  │
│  │        ╭─────────────────────────╮           │  │
│  │        │                         │           │  │
│  │        │     🤖                  │           │  │
│  │        │                         │           │  │
│  │        │   ● RESPONDING          │           │  │
│  │        │                         │           │  │
│  │        ╰─────────────────────────╯           │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  AI: I'm sorry to hear about the headache.    │  │
│  │      A 4 out of 10 is an improvement from     │  │
│  │      yesterday though. Did you notice any     │  │
│  │      triggers - like stress, certain foods,   │  │
│  │      or changes in sleep?                     │  │
│  │      (streaming in real-time)                 │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │                                             │    │
│  │   [ Tap to respond ]                        │    │
│  │                                             │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory

| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Back Button | Icon Button | Yes | Cancel check-in |
| 2 | Help Button | Icon Button | Yes | Voice tips |
| 3 | Status Indicator | Visual + Text | Yes | Listening/Thinking/Responding |
| 4 | Waveform Visualizer | Canvas/Animation | Yes | Real-time audio feedback |
| 5 | AI Message Bubble | Chat Bubble | Yes | Left-aligned, distinct color |
| 6 | User Message Bubble | Chat Bubble | Yes | Right-aligned, different color |
| 7 | Typing Indicator | Animated Dots | Yes | Shows AI processing |
| 8 | Conversation Container | Scrollable View | Yes | Chat history |
| 9 | Pause Button | Secondary Button | No | Pause recording |
| 10 | Done Button | Primary Button | Yes | Complete session |
| 11 | Voice Input Trigger | Button/Automatic | Yes | Start/resume recording |

#### Component Details

##### Component 3: Status Indicator

**Type**: Visual Status Display
**Purpose**: Clear communication of system state (critical for voice-first UX)
**Location**: Center top area, prominent

**States**:
| State | Visual | Text | Color |
|-------|--------|------|-------|
| Idle | Static mic icon | "Tap to speak" | Gray |
| Listening | Pulsing waveform | "● LISTENING" | Green |
| Processing | Animated dots/spinner | "● THINKING..." | Blue |
| Responding | AI icon with subtle animation | "● RESPONDING" | Purple |
| Error | Warning icon | "Connection issue" | Red |

**Animation Specifications**:
- Listening: Waveform responds to voice amplitude, pulse every 500ms
- Processing: 3 dots sequential fade, 300ms interval
- Responding: Gentle breathing animation, 1s cycle

**Accessibility**:
- ARIA live region: Announces state changes
- Screen reader: "[Status] - Listening for your voice" / "Processing your response" / "AI is responding"

---

##### Component 4: Waveform Visualizer

**Type**: Real-time Audio Visualization
**Purpose**: Visual feedback that voice is being captured
**Location**: Center of status area

**Technical Specs**:
- Updates: 60fps during recording
- Bars: 20-40 vertical bars
- Amplitude: Maps to microphone input level
- Smoothing: 100ms rolling average

**Visual States**:
| State | Appearance |
|-------|------------|
| Silent | Flat line, minimal height |
| Low voice | Small wave amplitude |
| Normal voice | Medium wave amplitude |
| Loud voice | Large wave amplitude, caps at max |

**Accessibility**:
- Hidden from screen readers (decorative)
- Pair with text status for accessibility

---

##### Component 5: AI Message Bubble

**Type**: Chat Bubble
**Purpose**: Display AI responses and follow-up questions
**Location**: Left side of conversation area

**States**:
| State | Appearance | Behavior |
|-------|------------|----------|
| Typing | Three animated dots | Indicates processing |
| Streaming | Text appearing word-by-word | Near real-time display |
| Complete | Full message, no animation | Static display |

**Content**:
| Element | Content | Character limit |
|---------|---------|-----------------|
| Message | AI response text | No limit (scrollable) |
| Timestamp | Optional, subtle | 10 |

**Streaming Behavior**:
- Words appear as received from API
- Scroll follows new content
- Typing indicator transitions to text

**Styling**:
- Background: Light gray or subtle brand color
- Border radius: 16px (rounded)
- Padding: 12px 16px
- Max width: 80% of container

---

##### Component 6: User Message Bubble

**Type**: Chat Bubble
**Purpose**: Display transcribed user speech
**Location**: Right side of conversation area

**States**:
| State | Appearance | Behavior |
|-------|------------|----------|
| Recording | Partial text + "●" indicator | Live transcription |
| Complete | Full transcribed text | Static display |
| Error | Error styling, retry option | "Couldn't hear that" |

**Live Transcription**:
- Words appear as recognized
- Visual indicator (●) shows recording active
- Brief delay acceptable (200-500ms)

**Styling**:
- Background: Primary brand color (user owns this)
- Text: White or contrasting
- Border radius: 16px (rounded)
- Max width: 80% of container

---

##### Component 10: Done Button

**Type**: Primary Action Button
**Purpose**: End check-in session and proceed to summary
**Location**: Bottom of screen, prominent

**States**:
| State | Appearance | Behavior |
|-------|------------|----------|
| Default | Solid primary color | Tap to complete |
| Disabled | Grayed out | During AI response |
| Pressed | Darkened | Feedback |
| Loading | Spinner | Processing final data |

**Content**:
| Element | Content | Character limit |
|---------|---------|-----------------|
| Label | "I'm Done" | 10 |

**Interactions**:
- Tap: Process conversation, extract data, navigate to summary
- Voice: "I'm done" or "That's all" triggers same action

**Accessibility**:
- ARIA label: "Complete check-in session"
- Keyboard: Tab to focus, Enter to activate

---

### Screen: Session Summary (Post Check-in)

**URL/Route**: `/check-in/summary`
**Purpose**: Display extracted health data for review before saving
**Entry points**: Completing voice check-in
**Exit points**: Save and return home, edit data, discard

#### Layout
```
┌─────────────────────────────────────────────────────┐
│  [←]           Check-in Complete            [Edit]  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  ✓ Great job! Here's what I captured:         │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Mood & Energy                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │  ┌─────────┐  ┌─────────┐                     │  │
│  │  │  ☀️     │  │  ⚡      │                     │  │
│  │  │  Good   │  │  Medium │                     │  │
│  │  │  Mood   │  │  Energy │                     │  │
│  │  └─────────┘  └─────────┘                     │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Symptoms                                           │
│  ┌───────────────────────────────────────────────┐  │
│  │  ┌──────────────────────────────────────────┐ │  │
│  │  │  🤕 Headache                             │ │  │
│  │  │  Severity: ████░░░░░░ 4/10               │ │  │
│  │  │  Location: Temples                       │ │  │
│  │  │  "Woke up with it, better than yesterday"│ │  │
│  │  └──────────────────────────────────────────┘ │  │
│  │                                               │  │
│  │  ┌──────────────────────────────────────────┐ │  │
│  │  │  😴 Fatigue                              │ │  │
│  │  │  Severity: ███░░░░░░░ 3/10               │ │  │
│  │  │  "Feeling a bit tired but manageable"    │ │  │
│  │  └──────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Sleep                                              │
│  ┌───────────────────────────────────────────────┐  │
│  │  Hours: 7.5    Quality: Good                  │  │
│  │  "Slept better than the night before"         │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Additional Notes                                   │
│  ┌───────────────────────────────────────────────┐  │
│  │  • Taking Advil helped yesterday              │  │
│  │  • Noticed headache worse after screen time   │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │           [ Save Check-in ]                 │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  [View Full Transcript]                             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory

| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Success Banner | Feedback Card | Yes | Positive reinforcement |
| 2 | Mood Card | Data Card | Yes | Extracted mood |
| 3 | Energy Card | Data Card | Yes | Extracted energy level |
| 4 | Symptom Card | Data Card | Yes | For each symptom |
| 5 | Severity Bar | Progress Indicator | Yes | Visual severity scale |
| 6 | Sleep Summary | Data Card | Conditional | If sleep mentioned |
| 7 | Notes List | Bullet List | Conditional | Additional observations |
| 8 | Save Button | Primary Button | Yes | Confirm and save |
| 9 | Transcript Link | Text Link | Yes | View full conversation |
| 10 | Edit Button | Icon Button | Yes | Modify extracted data |

#### Component Details

##### Component 4: Symptom Card

**Type**: Expandable Data Card
**Purpose**: Display extracted symptom with severity and context
**Location**: Symptoms section

**Content Structure**:
| Element | Content | Source |
|---------|---------|--------|
| Icon | Symptom-specific emoji | Mapped from symptom type |
| Name | "Headache", "Fatigue", etc. | NLP extraction |
| Severity | 1-10 scale with visual bar | Explicit or inferred |
| Details | Location, duration, triggers | NLP extraction |
| Quote | Relevant transcript excerpt | Extracted quote |

**Severity Visual**:
```
1-3:  ███░░░░░░░ (Green - Mild)
4-6:  ██████░░░░ (Yellow - Moderate)
7-10: █████████░ (Red - Severe)
```

**States**:
| State | Appearance | Behavior |
|-------|------------|----------|
| Collapsed | Icon, name, severity bar | Default view |
| Expanded | Full details and quote | Tap to expand |
| Editing | Editable fields | After tap Edit |

**Interactions**:
- Tap: Expand/collapse details
- Tap Edit: Enter edit mode for this symptom
- Swipe left: Delete symptom (with undo)

---

### Screen: Daily Note View

**URL/Route**: `/notes/:id`
**Purpose**: Detailed view of a single check-in with all extracted data
**Entry points**: Tap check-in card from Home or Timeline
**Exit points**: Back to list, Share, Delete

#### Layout
```
┌─────────────────────────────────────────────────────┐
│  [←]        January 31, 2026         [•••]         │
│             8:30 AM                                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │                                             │    │
│  │    ☀️ Good Mood    ⚡ Medium Energy         │    │
│  │                                             │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ─────────────────────────────────────────────────  │
│                                                     │
│  Symptoms (2)                                       │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  🤕 Headache                     4/10       │    │
│  │  ──────────────────────────────────────     │    │
│  │  Location: Temples                          │    │
│  │  Duration: Since waking                     │    │
│  │  ──────────────────────────────────────     │    │
│  │  "woke up with a headache again this        │    │
│  │   morning, but it's not as bad as           │    │
│  │   yesterday"                                │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  😴 Fatigue                      3/10       │    │
│  │  ──────────────────────────────────────     │    │
│  │  "feeling a bit tired but manageable"       │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ─────────────────────────────────────────────────  │
│                                                     │
│  Sleep                                              │
│  ┌─────────────────────────────────────────────┐    │
│  │  💤 7.5 hours        Quality: Good          │    │
│  │  "slept better last night"                  │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ─────────────────────────────────────────────────  │
│                                                     │
│  Observations                                       │
│  • Taking Advil helped yesterday                    │
│  • Headache worse after screen time                 │
│                                                     │
│  ─────────────────────────────────────────────────  │
│                                                     │
│  [ View Full Transcript ]                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory

| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Date Header | Text | Yes | Full date and time |
| 2 | More Menu | Icon Button | Yes | Share, Delete, Edit |
| 3 | Mood/Energy Summary | Horizontal Card | Yes | At-a-glance status |
| 4 | Section Divider | Visual | Yes | Separate content sections |
| 5 | Symptom Detail Card | Card | Yes | Full symptom information |
| 6 | Sleep Card | Card | Conditional | If sleep data exists |
| 7 | Observations List | Bullet List | Conditional | AI-extracted insights |
| 8 | Transcript Button | Secondary Button | Yes | Navigate to full transcript |

---

### Screen: Timeline View

**URL/Route**: `/timeline`
**Purpose**: Chronological view of all check-ins with filtering
**Entry points**: Bottom tab navigation
**Exit points**: Tap entry for detail, filter by date range

#### Layout
```
┌─────────────────────────────────────────────────────┐
│              Timeline                               │
│  ┌────────────────────────────────────────────────┐ │
│  │ [All] [Week] [Month] [Custom]                  │ │
│  └────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────┤
│                                                     │
│  January 2026                                       │
│                                                     │
│  ─○─ Today, Jan 31                                  │
│   │  ┌─────────────────────────────────────────┐   │
│   │  │ ☀️ Good • ⚡ Medium                      │   │
│   │  │ Headache (4), Fatigue (3)               │   │
│   │  │ "Woke up with a headache..."            │   │
│   │  └─────────────────────────────────────────┘   │
│   │                                                 │
│  ─○─ Yesterday, Jan 30                              │
│   │  ┌─────────────────────────────────────────┐   │
│   │  │ 🌥️ Okay • ⚡ Low                         │   │
│   │  │ Back pain (5), Insomnia                 │   │
│   │  │ "Rough night, couldn't sleep..."        │   │
│   │  └─────────────────────────────────────────┘   │
│   │                                                 │
│  ─○─ Jan 29                                         │
│   │  ┌─────────────────────────────────────────┐   │
│   │  │ 🌥️ Okay • ⚡ Medium                      │   │
│   │  │ Headache (6)                            │   │
│   │  │ "Headache started in the afternoon..."  │   │
│   │  └─────────────────────────────────────────┘   │
│   │                                                 │
│  ─○─ Jan 28                                         │
│      ┌─────────────────────────────────────────┐   │
│      │ ☀️ Great • ⚡ High                       │   │
│      │ No symptoms reported                    │   │
│      │ "Feeling really good today!"            │   │
│      └─────────────────────────────────────────┘   │
│                                                     │
│  ─────────── December 2025 ───────────             │
│                                                     │
│  ─○─ Dec 31                                         │
│      ...                                            │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [🏠]        [📅]        [📊]        [⚙️]          │
│  Home      Timeline     Trends     Settings        │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory

| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Filter Tabs | Segmented Control | Yes | Time range filters |
| 2 | Month Header | Section Header | Yes | Group by month |
| 3 | Timeline Entry | Card with connector | Yes | Single check-in summary |
| 4 | Timeline Connector | Visual line | Yes | Connect entries vertically |
| 5 | Date Label | Text | Yes | Day indicator |
| 6 | Severity Indicator | Color coding | Yes | Visual severity hint |

#### Component Details

##### Component 3: Timeline Entry

**Type**: Connected Card
**Purpose**: Show check-in summary in timeline context
**Location**: Main timeline list

**Visual Elements**:
- Circle node on left (connects to timeline line)
- Date label beside node
- Card to the right with summary
- Color accent based on overall day severity

**Color Coding**:
| Overall Status | Node Color | Card Accent |
|----------------|------------|-------------|
| Good day | Green | Green left border |
| Mixed day | Yellow | Yellow left border |
| Difficult day | Red | Red left border |

**Content**:
| Element | Content | Character limit |
|---------|---------|-----------------|
| Mood icon + label | "☀️ Good" | 10 |
| Energy icon + label | "⚡ Medium" | 15 |
| Symptoms | Name (severity), comma separated | 40 |
| Preview | First line of transcript | 35 |

---

### Screen: Trend Charts

**URL/Route**: `/trends`
**Purpose**: Visualize health patterns over time
**Entry points**: Bottom tab navigation
**Exit points**: Tap chart for detail, change date range

#### Layout
```
┌─────────────────────────────────────────────────────┐
│              Trends                                 │
│  ┌────────────────────────────────────────────────┐ │
│  │ [Week] [Month] [3 Months] [Year]               │ │
│  └────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Symptom Frequency                                  │
│  ┌───────────────────────────────────────────────┐  │
│  │ Headache    ████████████████░░ 12 days        │  │
│  │ Fatigue     ████████████░░░░░░  9 days        │  │
│  │ Back pain   ██████░░░░░░░░░░░░  5 days        │  │
│  │ Insomnia    ████░░░░░░░░░░░░░░  3 days        │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Headache Severity Over Time                        │
│  ┌───────────────────────────────────────────────┐  │
│  │  10│                                          │  │
│  │    │      ╭╮                                  │  │
│  │   5│   ╭──╯╰╮    ╭─╮                         │  │
│  │    │ ╭─╯    ╰────╯ ╰─╮                       │  │
│  │   0│─╯               ╰───────                │  │
│  │    └────────────────────────────             │  │
│  │     M   T   W   T   F   S   S                │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Mood Distribution                                  │
│  ┌───────────────────────────────────────────────┐  │
│  │                                               │  │
│  │    ☀️ Great  ████████░░ 40%                   │  │
│  │    🌤️ Good   ██████░░░░ 30%                   │  │
│  │    🌥️ Okay   ████░░░░░░ 20%                   │  │
│  │    🌧️ Poor   ██░░░░░░░░ 10%                   │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Energy Levels                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │  High  │  ●   ●       ●   ●                   │  │
│  │  Med   │    ●   ● ●     ●                     │  │
│  │  Low   │          ●             ●             │  │
│  │        └─────────────────────────             │  │
│  │          M   T   W   T   F   S   S            │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [🏠]        [📅]        [📊]        [⚙️]          │
│  Home      Timeline     Trends     Settings        │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory

| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Time Range Selector | Segmented Control | Yes | Filter data range |
| 2 | Symptom Frequency Chart | Horizontal Bar Chart | Yes | Most common symptoms |
| 3 | Severity Line Chart | Line Chart | Yes | Severity over time |
| 4 | Mood Distribution | Stacked Bar/Pie | Yes | Mood breakdown |
| 5 | Energy Scatter/Line | Dot/Line Chart | Yes | Energy patterns |
| 6 | Insight Cards | Card | Optional | AI-generated insights |

#### Component Details

##### Component 3: Severity Line Chart

**Type**: Interactive Line Chart
**Purpose**: Visualize symptom severity trends over time
**Location**: Main content area

**Features**:
- X-axis: Time (days/weeks depending on range)
- Y-axis: Severity 0-10
- Line per symptom (toggle-able)
- Touch to see specific data point
- Pinch to zoom time range

**Interactions**:
- Tap point: Show tooltip with date, severity, notes
- Long press: Highlight that day's check-in
- Swipe: Pan through time
- Tap legend: Toggle symptom visibility

**Accessibility**:
- VoiceOver: Read trends as "Headache severity, trending down, average 5.2 this week"
- Data table alternative available

**Empty State**:
```
┌───────────────────────────────────────────────────┐
│                                                   │
│     Not enough data yet                           │
│                                                   │
│     Check in for at least 3 days to see          │
│     your symptom trends.                         │
│                                                   │
│     [ Start Today's Check-in ]                   │
│                                                   │
└───────────────────────────────────────────────────┘
```

---

### Screen: Settings

**URL/Route**: `/settings`
**Purpose**: Configure reminders, sharing, and preferences
**Entry points**: Bottom tab navigation
**Exit points**: Back, individual setting screens

#### Layout
```
┌─────────────────────────────────────────────────────┐
│              Settings                               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Reminders                                          │
│  ┌───────────────────────────────────────────────┐  │
│  │  Daily Check-in Reminder        [====•    ]   │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Reminder Time                    8:00 AM  >  │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Reminder Days           Every day         >  │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Sharing                                            │
│  ┌───────────────────────────────────────────────┐  │
│  │  Share with Care Team           [    •====]   │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Manage Care Team                          >  │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Export Data                               >  │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Voice Preferences                                  │
│  ┌───────────────────────────────────────────────┐  │
│  │  AI Voice                      Warm & Calm >  │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Speaking Rate                    Normal   >  │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Auto-start Listening           [    •====]   │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Privacy                                            │
│  ┌───────────────────────────────────────────────┐  │
│  │  Audio Storage                  Device only>  │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Delete All Data                           >  │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  About                                              │
│  ┌───────────────────────────────────────────────┐  │
│  │  Help & Support                            >  │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Privacy Policy                            >  │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Version                              1.0.0   │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [🏠]        [📅]        [📊]        [⚙️]          │
│  Home      Timeline     Trends     Settings        │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory

| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Section Header | Text | Yes | Group related settings |
| 2 | Toggle Setting | Toggle Switch | Yes | On/off settings |
| 3 | Navigation Setting | List Item | Yes | Opens sub-screen |
| 4 | Value Display | List Item | Yes | Shows current value |
| 5 | Time Picker | Modal Picker | Yes | For reminder time |
| 6 | Day Selector | Multi-select | Yes | For reminder days |

---

## Interaction Patterns

### Pattern: Voice Recording Cycle

**Use case**: User speaking during check-in
**Components involved**: Status Indicator, Waveform, User Bubble, Done Button

**Behavior**:
1. User taps mic or screen auto-listens
2. Status changes to "LISTENING"
3. Waveform animates with voice amplitude
4. User bubble shows real-time transcription
5. Silence detected (2-3 seconds)
6. Status changes to "THINKING"
7. User bubble finalizes
8. AI processes and responds

**Animation/Transition**:
- Waveform: Continuous 60fps update during recording
- Status text: 200ms fade transition
- Bubble appear: 300ms slide up + fade in

```
[Idle] --tap--> [Listening + Waveform] --silence--> [Thinking] --response--> [AI Speaking]
                     │                                                              │
                     └──────────────────[User speaks again]─────────────────────────┘
```

---

### Pattern: AI Response Streaming

**Use case**: AI delivers response in real-time
**Components involved**: AI Bubble, Typing Indicator, Status

**Behavior**:
1. Typing indicator appears (3 dots)
2. First word received, typing indicator replaced with text
3. Words stream in as received (50-100ms between words)
4. When complete, bubble shows full response
5. Status changes to invite user response

**Animation/Transition**:
- Typing dots: Sequential fade 300ms interval
- Word appear: Instant with scroll follow
- Completion: Subtle pulse on bubble

---

### Pattern: Symptom Card Expansion

**Use case**: User wants more detail on extracted symptom
**Components involved**: Symptom Card

**Behavior**:
1. User taps collapsed symptom card
2. Card expands to show all details
3. Other content pushes down
4. Tap again to collapse

**Animation/Transition**:
- Duration: 250ms
- Easing: ease-out
- Properties: height, content opacity

```
[Collapsed: Icon + Name + Bar] --tap--> [Expand animation] --complete--> [Full details]
```

---

### Pattern: Pull-to-Refresh

**Use case**: User wants to sync latest data
**Components involved**: Timeline list, Home list

**Behavior**:
1. User pulls down on list
2. Refresh indicator appears
3. Data syncs from server
4. List updates, indicator hides

**Animation/Transition**:
- Pull threshold: 60px
- Spinner: Circular loading
- Duration: Until sync complete

---

## Responsive Behavior

### Breakpoints
| Name | Width | Layout Changes |
|------|-------|----------------|
| Mobile | < 768px | Single column, bottom tabs, FAB |
| Tablet | 768-1024px | Two-column on Dashboard, side tabs possible |
| Desktop | > 1024px | Three-column, sidebar navigation, expanded charts |

### Screen: Voice Check-in - Responsive

**Mobile** (Primary):
```
┌────────────────────────────────────────┐
│  [←]                            [?]    │
│                                        │
│        [Waveform + Status]            │
│                                        │
│  ┌──────────────────────────────────┐  │
│  │  Conversation (stacked)          │  │
│  │  AI bubble                       │  │
│  │  User bubble                     │  │
│  └──────────────────────────────────┘  │
│                                        │
│  [Pause]              [Done]          │
└────────────────────────────────────────┘
```

**Tablet**:
```
┌─────────────────────────────────────────────────────────────────────┐
│  [←]                    Voice Check-in                         [?]  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────────────────────┐  ┌────────────────────────────┐  │
│  │                               │  │                            │  │
│  │    [Waveform + Status]        │  │    Conversation            │  │
│  │                               │  │    (scrollable)            │  │
│  │    Large visual feedback      │  │                            │  │
│  │                               │  │    AI bubbles              │  │
│  │                               │  │    User bubbles            │  │
│  │                               │  │                            │  │
│  │    [Pause]   [Done]           │  │                            │  │
│  │                               │  │                            │  │
│  └───────────────────────────────┘  └────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Data Requirements

### Screen: Voice Check-in

| Data Point | Source | Format | Update Frequency |
|------------|--------|--------|------------------|
| Audio stream | Device mic | PCM/WAV | Real-time |
| Transcription | Speech-to-Text API | String | Real-time streaming |
| AI response | LLM API | String | Streaming |
| Extracted data | NLP processing | JSON | End of session |

### Screen: Home/Dashboard

| Data Point | Source | Format | Update Frequency |
|------------|--------|--------|------------------|
| Recent check-ins | Local DB + API | Array<CheckIn> | On load, pull-to-refresh |
| Streak count | Calculated | Number | On load |
| User profile | API/Local | Object | On app start |

### Screen: Trends

| Data Point | Source | Format | Update Frequency |
|------------|--------|--------|------------------|
| Check-in history | API | Array<CheckIn> | On load |
| Symptom aggregates | Calculated | Object | On time range change |
| Mood distribution | Calculated | Object | On time range change |

### Empty States
| Scenario | Content | Action |
|----------|---------|--------|
| No check-ins | "Start your health journey" | [Start First Check-in] |
| No symptoms | "No symptoms recorded this period" | N/A |
| No trends data | "Check in for 3+ days to see trends" | [Start Check-in] |
| Offline | "You're offline. Data will sync when connected." | [Try Again] |
| Error loading | "Couldn't load your data" | [Retry] |

---

## Technical Questions

### For Engineering Review

| # | Question | Context | Impact |
|---|----------|---------|--------|
| 1 | What speech-to-text API will be used? | Affects real-time transcription latency and accuracy | Determines if we can show live transcription or only final |
| 2 | Can AI responses stream in real-time? | LLM streaming support needed | Affects perceived response time, UX of conversation |
| 3 | What is acceptable voice recording latency? | Waveform must feel responsive | Sets technical requirements for audio processing |
| 4 | How will NLP extraction work? | AI extracts symptoms, mood, severity | Determines summary screen accuracy and edit needs |
| 5 | Offline support requirements? | Chronic patients may have connectivity issues | Affects local storage, sync architecture |
| 6 | What accessibility APIs are available? | Screen reader support for voice UI | May need custom VoiceOver announcements |
| 7 | Audio storage: local vs cloud? | Privacy concerns for health data | Affects architecture and compliance |
| 8 | How to handle mid-conversation app backgrounding? | Users may be interrupted | Determines session persistence strategy |

### Known Constraints
- **iOS/Android permissions**: Microphone access required, must handle denial gracefully
- **Network dependency**: AI responses require network (unless edge AI)
- **Privacy regulations**: Health data subject to HIPAA/GDPR considerations
- **Battery impact**: Continuous voice recording can drain battery

### Assumptions
- Users have stable internet for AI interactions (with offline fallback)
- Speech-to-text can achieve >90% accuracy for health terminology
- AI can reliably extract structured data from conversational input
- Users are comfortable with voice interaction (fallback to text available)

---

## Functional Requirements Matrix

| Screen | Component | Requirement | Priority | Story Ref |
|--------|-----------|-------------|----------|-----------|
| Home | Check-in FAB | Tap opens voice check-in | Must | US-001 |
| Home | Streak Display | Show consecutive check-in days | Should | US-002 |
| Home | Recent Cards | Display last 3-5 check-ins | Must | US-003 |
| Voice | Waveform | Respond to voice amplitude in real-time | Must | US-004 |
| Voice | Status Indicator | Show Listening/Thinking/Responding states | Must | US-005 |
| Voice | User Bubble | Live transcription during speech | Must | US-006 |
| Voice | AI Bubble | Stream AI response word-by-word | Should | US-007 |
| Voice | Done Button | End session and process data | Must | US-008 |
| Summary | Symptom Cards | Display extracted symptoms with severity | Must | US-009 |
| Summary | Edit Function | Allow user to correct extracted data | Should | US-010 |
| Timeline | Filter Tabs | Filter by week/month/custom | Should | US-011 |
| Timeline | Entry Cards | Show summary with severity indicator | Must | US-012 |
| Trends | Line Chart | Severity over time, interactive | Should | US-013 |
| Trends | Frequency Bar | Most common symptoms | Should | US-014 |
| Settings | Reminder Toggle | Enable/disable daily reminder | Must | US-015 |
| Settings | Time Picker | Set reminder time | Must | US-016 |
| Settings | Share Toggle | Enable sharing with care team | Could | US-017 |

---

## Accessibility Specifications

### Voice-First Accessibility
| Consideration | Implementation |
|---------------|----------------|
| VoiceOver support | All buttons, states announced; conversation read aloud |
| Reduce motion | Disable waveform animation, use static indicators |
| Large text | All text scales with system font size |
| High contrast | Support high contrast mode for all states |
| Switch control | All actions accessible via external switch |
| Keyboard navigation | Full keyboard support on iPad/Mac |

### Chronic Patient Accommodations
| Consideration | Implementation |
|---------------|----------------|
| Fatigue-friendly | Minimal taps required; voice-first reduces physical interaction |
| Cognitive load | Simple, predictable flows; no complex branching |
| Memory support | Visible conversation history; saved transcripts |
| Flexible timing | No rush; natural conversation pace; pause support |

---

## Handoff Checklist

### For Visual Design
- [x] All screens documented (6 primary screens)
- [x] All states defined (idle, listening, thinking, responding, error)
- [x] All interactions specified (tap, swipe, pull, voice)
- [x] Responsive behavior noted (mobile, tablet, desktop)
- [ ] Content/copy finalized (placeholder copy, needs review)
- [ ] Technical questions answered (pending engineering review)

### For Development
- [x] Component inventory complete (all screens)
- [x] Data requirements documented (per screen)
- [x] API needs identified (STT, LLM, NLP)
- [x] Accessibility requirements noted (voice-first specific)
- [x] Edge cases covered (offline, errors, permissions)

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-31 | Initial wireframe specification |
