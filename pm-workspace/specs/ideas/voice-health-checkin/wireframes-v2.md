# Wireframe Specification v2: Voice-First Health Check-in (Immersive)

## Overview
**PRD Reference**: voice-health-checkin/PRD.md (v2.0)
**Designer**: Wireframe Designer
**Version**: 2.0
**Last Updated**: 2026-02-06
**Design Direction**: Direction C — Immersive Wellness (Panel Score: 4.2/5)

### What Changed from v1
| Aspect | v1 | v2 |
|--------|----|----|
| Primary screen | Card-based with tab bar | Full-screen breathing orb, no nav |
| Check-in UI | Waveform + chat bubbles | Breathing orb IS the interface |
| Extraction model | Symptoms + Mood | 4 dimensions: Body, Mind, Actions, Context |
| Navigation | Tab bar always visible | Hidden during check-in (immersive) |
| Summary layout | Flat symptom list | 4-category grouped cards |
| Onboarding | None | First-time immersive mode tutorial |
| Transition | Hard cut | Animated portal from home to immersive |

### Panel Feedback Incorporated
- Jony Ive: "The orb IS the interface" — removed all chrome
- Paula Scher: "Let typography do emotional work" — serif + sans mix
- Mike Kresch: "Remove navigation during check-in" — full-screen immersive
- Alan Dye: "Add wayfinding" — swipe gesture hints, onboarding
- Alex Schleifer: "Transition animation for emotional continuity" — portal animation

---

## Information Architecture

### Sitemap
```
[Home/Dashboard]
├── [Voice Check-in — IMMERSIVE MODE]
│   ├── [Onboarding (first time)]
│   ├── [Breathing Orb — Listening]
│   ├── [Breathing Orb — Thinking]
│   ├── [Breathing Orb — Responding]
│   └── [Session Summary (4 dimensions)]
├── [Daily Notes]
│   ├── [Note Detail (4 dimensions)]
│   └── [Transcript View]
├── [Timeline]
│   └── [Date Filter]
├── [Trends]
│   ├── [Body Charts]
│   ├── [Mind Charts]
│   ├── [Actions Charts]
│   └── [Context Charts]
└── [Settings]
    ├── [Reminders]
    ├── [Sharing]
    ├── [Voice Preferences]
    └── [Check-in Mode (Immersive/Classic)]
```

### Navigation Structure
| Level | Location | Items |
|-------|----------|-------|
| Primary | Bottom Tab Bar | Home, Timeline, Trends, Settings |
| Contextual | Home Card/FAB | Start Check-in (prominent) |
| Immersive | Hidden during check-in | Swipe-down to exit, voice "I'm done" |
| Modal | First-time onboarding | How the orb works |

---

## User Flows

### Flow 1: First-Time Check-in (Onboarding)

**Entry point**: First tap on Check-in FAB
**Goal**: Teach the immersive orb interaction pattern

```
[Tap FAB] → [Portal Transition Animation]
                    ↓
            [Onboarding Overlay]
            "Meet your health companion"
            ┌──────────────────────┐
            │ The orb listens when │
            │ you speak and glows  │
            │ when it responds.    │
            │                      │
            │ Just talk naturally. │
            │ Say "I'm done" when  │
            │ you're finished.     │
            │                      │
            │ Swipe down to exit   │
            │ anytime.             │
            │                      │
            │    [ Got it ]        │
            └──────────────────────┘
                    ↓
            [Immersive Check-in Screen]
```

### Flow 2: Daily Check-in (Returning User)

**Entry point**: Push notification or FAB tap
**Goal**: Complete voice check-in through immersive orb

```
[Push Notification / FAB Tap]
            ↓
    [Portal Transition Animation]
    (Home screen shrinks, gradient expands, orb materializes)
            ↓
    [Immersive Check-in — Orb Idle]
    "How are you today?"
            ↓
    [User speaks — Orb Listening]
    (Orb pulses with voice amplitude)
    (Transcript appears subtly below)
            ↓
    [Silence detected — Orb Thinking]
    (Orb contracts gently)
            ↓
    [AI Responds — Orb Speaking]
    (Orb glows brighter, text streams)
            ↓
    ┌───────────────────┬───────────────────┐
    ↓                   ↓                   ↓
[User speaks      [User says          [2 min silence]
 again — loop]     "I'm done"]         [Gentle prompt]
                        ↓
                [Completion Animation]
                (Orb transforms to checkmark)
                        ↓
                [Session Summary]
                (4-dimension cards)
                        ↓
                [Save & Return Home]
                (Reverse portal transition)
```

---

## Screen Specifications

---

### Screen: Home/Dashboard (Updated)

**URL/Route**: `/home`
**Purpose**: Hub with recent activity, streak, and prominent check-in entry
**Changes from v1**: Check-in FAB now triggers portal transition, cards show 4-dimension summary

#### Layout (Mobile)
```
┌─────────────────────────────────────────────────────┐
│  ┌───────────────────────────────────────────────┐  │
│  │  Good morning, [Name]              [Profile]  │  │
│  │  How are you feeling today?                   │  │
│  └───────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  7 Day Streak                                 │  │
│  │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━                 │  │
│  │  [M] [T] [W] [T] [F] [S] [S]                  │  │
│  │   ✓   ✓   ✓   ✓   ✓   ✓   ○                  │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Recent Check-ins                        [See all]  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  Today, 8:30 AM                               │  │
│  │  Body: Headache (4)  Mind: Calm               │  │
│  │  Actions: Took Advil  Context: Slept 7.5h    │  │
│  │  "Slept better last night..."                 │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  Yesterday, 9:15 AM                           │  │
│  │  Body: Back pain (5)  Mind: Anxious           │  │
│  │  Actions: Skipped meds  Context: Poor sleep  │  │
│  │  "Rough night, couldn't sleep..."             │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│                                                     │
│                 ┌───────────────┐                   │
│                 │               │                   │
│                 │   ◉ Check in  │  ← FAB (orb icon) │
│                 │               │                   │
│                 └───────────────┘                   │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [Home]      [Timeline]     [Trends]    [Settings]  │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory
| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Greeting Header | Text + Icon | Yes | Personalized, time-aware |
| 2 | Profile Avatar | Button | Yes | Navigate to profile |
| 3 | Streak Card | Card | Yes | Gamification element |
| 4 | Week Progress | Visual Indicator | Yes | 7-day checkmarks |
| 5 | Recent Check-ins List | List | Yes | Last 3-5 entries |
| 6 | Check-in Card | Card | Yes | 4-dimension summary preview |
| 7 | Check-in FAB | Floating Action Button | Yes | Triggers portal transition |
| 8 | Bottom Navigation | Tab Bar | Yes | 4 tabs |

#### Check-in Card (Updated for 4 Dimensions)
| Element | Content | Character limit |
|---------|---------|-----------------|
| Timestamp | "Today, 8:30 AM" | 20 |
| Body | Top symptom + severity | 25 |
| Mind | Mood/cognitive state | 20 |
| Actions | Key action taken | 25 |
| Context | Sleep/environment | 25 |
| Preview | First line of transcript | 40 (truncate) |

---

### Screen: Portal Transition (Home → Immersive)

**Purpose**: Emotionally bridge from dashboard to immersive check-in
**Duration**: 600-800ms
**Triggers**: FAB tap or notification tap

#### Animation Sequence
```
Frame 1 (0ms): Home screen visible, FAB tapped
┌─────────────────────────────────────┐
│  Home screen content                │
│                                     │
│                                     │
│              [◉ FAB]                │
│  [Tab Bar]                          │
└─────────────────────────────────────┘

Frame 2 (200ms): Home content fades + scales down, gradient begins
┌─────────────────────────────────────┐
│                                     │
│     ╭─ home content ─╮             │
│     │  (80% scale,   │             │
│     │   fading out)  │             │
│     ╰────────────────╯             │
│                                     │
│  Warm gradient expanding from FAB   │
└─────────────────────────────────────┘

Frame 3 (400ms): Gradient fills screen, orb materializes
┌─────────────────────────────────────┐
│                                     │
│  ░░░░░ Gradient fills ░░░░░        │
│                                     │
│         ╭───────╮                   │
│         │  ◉◉◉  │ ← orb forming    │
│         ╰───────╯                   │
│                                     │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░        │
└─────────────────────────────────────┘

Frame 4 (700ms): Immersive mode fully active
┌─────────────────────────────────────┐
│ [X]                          0:00   │
│                                     │
│                                     │
│          ╭──────────╮               │
│         ╱            ╲              │
│        │   BREATHING  │             │
│        │     ORB      │             │
│         ╲            ╱              │
│          ╰──────────╯               │
│                                     │
│       How are you today?            │
│                                     │
│                                     │
│        [ I'm finished ]             │
└─────────────────────────────────────┘
```

#### Specifications
| Property | Value |
|----------|-------|
| Total duration | 700ms |
| Easing | cubic-bezier(0.4, 0.0, 0.2, 1) |
| Home content | Scale to 0.85, fade to 0 |
| Gradient | Radial expand from FAB position |
| Orb | Scale from 0 → 1, spring easing |
| Tab bar | Slide down + fade |
| Haptic | Medium impact on transition start |

#### Reverse Transition (Immersive → Home)
Same sequence in reverse when user completes check-in or swipes down to exit. Orb contracts, gradient recedes, home screen scales back up.

---

### Screen: Immersive Voice Check-in (Primary — v2)

**URL/Route**: `/check-in` (full-screen overlay)
**Purpose**: Immersive voice interaction through breathing orb
**Entry points**: Portal transition from FAB/notification
**Exit points**: Voice "I'm done", tap finish button, swipe down

#### Layout — Idle State (Waiting to Listen)
```
┌─────────────────────────────────────────────────────┐
│ [X]                                          0:00   │
│                                                     │
│                                                     │
│                                                     │
│                                                     │
│               ╭────────────────╮                    │
│              ╱                  ╲                   │
│             │                    │                  │
│             │    ◉  ◉  ◉  ◉     │                  │
│             │                    │                  │
│             │   Gentle pulse     │                  │
│              ╲                  ╱                   │
│               ╰────────────────╯                    │
│                                                     │
│                                                     │
│           How are you today?                        │
│                                                     │
│     Tap the orb or just start speaking              │
│                                                     │
│                                                     │
│                                                     │
│             [ I'm finished ]                        │
│           or say "I'm done"                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Layout — Listening State (User Speaking)
```
┌─────────────────────────────────────────────────────┐
│ [X]                                          0:34   │
│                                                     │
│                                                     │
│                                                     │
│               ╭────────────────╮                    │
│              ╱  ~~~~~~~~~~~~~~  ╲                   │
│             │  ~~~~~~~~~~~~~~~~  │                  │
│             │  ~~~~~ ◉◉◉ ~~~~~  │ ← responsive     │
│             │  ~~~~~~~~~~~~~~~~  │   to amplitude   │
│             │  ~~~~~~~~~~~~~~    │                  │
│              ╲                  ╱                   │
│               ╰────────────────╯                    │
│                                                     │
│              I'm listening...                       │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  "I woke up with a headache again this      │    │
│  │   morning, but it's not as bad as            │    │
│  │   yesterday. Maybe a 4 out of 10. I took    │    │
│  │   some advil and..."  ●                     │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│             [ I'm finished ]                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Layout — Thinking State (AI Processing)
```
┌─────────────────────────────────────────────────────┐
│ [X]                                          0:52   │
│                                                     │
│                                                     │
│                                                     │
│               ╭────────────────╮                    │
│              ╱                  ╲                   │
│             │      ◉◉◉◉◉       │                  │
│             │     ◉     ◉      │ ← contracts       │
│             │    ◉  ···  ◉     │   gently          │
│             │     ◉     ◉      │                  │
│             │      ◉◉◉◉◉       │                  │
│              ╲                  ╱                   │
│               ╰────────────────╯                    │
│                                                     │
│           Let me think about that...                │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  "I woke up with a headache again this      │    │
│  │   morning, but it's not as bad as            │    │
│  │   yesterday. Maybe a 4 out of 10."          │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│             [ I'm finished ]                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Layout — Responding State (AI Speaking)
```
┌─────────────────────────────────────────────────────┐
│ [X]                                          1:05   │
│                                                     │
│                                                     │
│                                                     │
│               ╭────────────────╮                    │
│              ╱   ✦  ✦  ✦  ✦   ╲                   │
│             │  ✦            ✦  │                  │
│             │ ✦   GLOWING   ✦  │ ← brighter,      │
│             │  ✦            ✦  │   expanded        │
│             │   ✦  ✦  ✦  ✦    │                  │
│              ╲                  ╱                   │
│               ╰────────────────╯                    │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  That's the third headache this week.        │    │
│  │  Is it the same location as Tuesday?         │    │
│  │  And did the Advil help faster this time?   │    │
│  │  (streaming...)                              │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│                                                     │
│         [ Tap to respond ]                          │
│                                                     │
│             [ I'm finished ]                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Layout — Completion State (Celebration)
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│                                                     │
│                                                     │
│                                                     │
│                                                     │
│               ╭────────────────╮                    │
│              ╱                  ╲                   │
│             │                    │                  │
│             │       ✓           │ ← orb morphs     │
│             │                    │   to checkmark   │
│              ╲                  ╱                   │
│               ╰────────────────╯                    │
│                                                     │
│                                                     │
│          Great check-in!                            │
│       Here's what I captured.                       │
│                                                     │
│                                                     │
│          [ See Summary ]                            │
│                                                     │
│                                                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory
| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Close Button | Icon (X) | Yes | Top-left, swipe-down also exits |
| 2 | Session Timer | Text | Yes | Top-right, subtle |
| 3 | Breathing Orb | Canvas/Animation | Yes | THE primary interface element |
| 4 | Status Text | Text | Yes | Below orb: "I'm listening..." / "Let me think..." |
| 5 | Transcript Area | Text Container | Yes | Floating below orb, shows live text |
| 6 | AI Response | Text Container | Yes | Streams AI response text |
| 7 | Finish Button | Secondary Button | Yes | "I'm finished" — soft, not prominent |
| 8 | Voice Hint | Caption Text | Yes | "or say 'I'm done'" |
| 9 | Gradient Background | Full-screen gradient | Yes | Warm, shifts with state |

#### Component Details

##### Component 3: Breathing Orb

**Type**: Animated Canvas Element
**Purpose**: The orb IS the interface — represents AI presence and attention
**Location**: Center of screen, vertically offset slightly above middle

**Visual States**:
| State | Size | Animation | Color | Duration |
|-------|------|-----------|-------|----------|
| Idle | 180px | Gentle breathing (scale 1.0↔1.05) | Warm gradient (peach → coral) | 4s cycle |
| Listening | 200px | Pulse with voice amplitude | Vibrant coral, waveform texture | Real-time |
| Thinking | 160px | Contract + gentle rotation | Muted coral, inner dots animate | 1.5s cycle |
| Responding | 220px | Expand + glow | Bright warm gold | Sync to speech |
| Complete | 180px → morphs | Orb → checkmark transformation | Green → gold | 800ms |
| Error | 180px | Slight tremble | Soft red tint | 300ms |

**Animation Specifications**:
- Breathing cycle: `scale(1.0) → scale(1.05)` with `ease-in-out`, 4s
- Voice response: Map microphone amplitude to `scale(1.0 - 1.15)`, 60fps
- Thinking: `scale(0.9)` + `rotate(0 → 360)`, 1.5s
- Glow effect: Box-shadow expands 20px during responding
- Morphing: Spring animation, overshoots slightly

**Gradient Background Sync**:
| Orb State | Background Gradient |
|-----------|---------------------|
| Idle | Warm cream (#FFFBF5 → #FFF0E6) |
| Listening | Slightly warmer (#FFF0E6 → #FFE4D6) |
| Thinking | Softly muted (#F5F0EB → #EDE5DE) |
| Responding | Bright warm (#FFF5EB → #FFE8D9) |
| Complete | Celebration (#FFF8ED → #FFFBF0 + sparkle overlay) |

**Accessibility**:
- VoiceOver: "Health companion orb, currently [state]. [status text]"
- Reduce Motion: Replace animation with static orb + state icon overlay
- Haptic: Light impact on state change, medium on completion

##### Component 5: Transcript Area

**Type**: Floating Text Container
**Purpose**: Show live transcription and conversation history
**Location**: Lower third of screen, below orb

**Behavior**:
- Appears when user starts speaking (200ms fade-in from bottom)
- Shows real-time transcription with "●" recording indicator
- When AI responds, user text scrolls up, AI text appears below
- Maximum 2 exchanges visible (scroll for more)
- Fades slightly during listening to keep focus on orb

**Styling**:
- Background: Semi-transparent warm (#FFFBF5 at 80% opacity)
- Blur: Background blur 20px
- Corner radius: 20px
- Padding: 16px 20px
- Typography: Serif for AI, sans-serif for user (per Paula Scher)
- Max height: 30% of screen

##### Component 7: Finish Button

**Type**: Ghost/Secondary Button
**Purpose**: End session — NOT the primary interaction (voice is primary)
**Location**: Bottom of screen, subtle

**Styling**:
- Background: Transparent
- Border: 1px solid rgba(255, 255, 255, 0.3)
- Text: "I'm finished" — 16px, weight 500
- Corner radius: pill (9999px)
- Opacity: 0.7 (doesn't compete with orb)

**States**:
| State | Appearance |
|-------|------------|
| Default | Ghost, subtle |
| During AI response | Slightly more visible (user might want to end) |
| Tapped | Scale 0.95, triggers completion |

---

### Screen: First-Time Onboarding Overlay

**URL/Route**: Overlay on first `/check-in` visit
**Purpose**: Teach the immersive orb paradigm
**Trigger**: First time user enters check-in

#### Layout
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  (Immersive gradient visible behind, blurred)       │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │                                             │    │
│  │   Meet your health companion               │    │
│  │                                             │    │
│  │       ╭──────╮                              │    │
│  │       │  ◉◉  │ ← mini orb illustration     │    │
│  │       ╰──────╯                              │    │
│  │                                             │    │
│  │   The orb listens when you speak            │    │
│  │   and responds with follow-up questions.    │    │
│  │                                             │    │
│  │   Just talk naturally about how you feel.   │    │
│  │                                             │    │
│  │   ─────────────────────────────────         │    │
│  │                                             │    │
│  │   ↓ Swipe down to exit anytime              │    │
│  │   🎤 Say "I'm done" to finish               │    │
│  │   ✓ Your data is saved automatically        │    │
│  │                                             │    │
│  │           [ Let's start ]                   │    │
│  │                                             │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Component Inventory
| # | Component | Type | Required | Notes |
|---|-----------|------|----------|-------|
| 1 | Title | Text | Yes | "Meet your health companion" |
| 2 | Orb Illustration | Static Image | Yes | Mini version of breathing orb |
| 3 | Description | Text | Yes | How the orb works |
| 4 | Tips List | Icon + Text List | Yes | Exit, finish, save hints |
| 5 | Start Button | Primary Button | Yes | "Let's start" |
| 6 | Blurred Background | Visual | Yes | Immersive mode visible behind |

---

### Screen: Session Summary (4 Dimensions — v2)

**URL/Route**: `/check-in/summary`
**Purpose**: Display extracted health data across 4 dimensions
**Entry points**: After check-in completion
**Exit points**: Save and return home

#### Layout
```
┌─────────────────────────────────────────────────────┐
│  [←]           Check-in Complete              [Edit] │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │  ✓ Great check-in! 1 min 24 sec              │  │
│  │    Here's what I captured:                    │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌─ BODY ────────────────────────────────────────┐  │
│  │                                               │  │
│  │  Symptoms                                     │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │  Headache                      4/10     │  │  │
│  │  │  ████░░░░░░  Temples, since waking      │  │  │
│  │  └─────────────────────────────────────────┘  │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │  Fatigue                       3/10     │  │  │
│  │  │  ███░░░░░░░  "Manageable"               │  │  │
│  │  └─────────────────────────────────────────┘  │  │
│  │                                               │  │
│  │  Vitals                                       │  │
│  │  Energy: Medium                               │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌─ MIND ────────────────────────────────────────┐  │
│  │                                               │  │
│  │  Mood: Calm but tired                         │  │
│  │  Cognitive: "A bit foggy this morning"        │  │
│  │  Stress: Low                                  │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌─ ACTIONS ─────────────────────────────────────┐  │
│  │                                               │  │
│  │  Medications                                  │  │
│  │  ┌─────────────────────────────────────────┐  │  │
│  │  │  Advil — 2 pills — This morning  ✓      │  │  │
│  │  └─────────────────────────────────────────┘  │  │
│  │                                               │  │
│  │  Self-care: "Going to rest this afternoon"    │  │
│  │                                               │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  ┌─ CONTEXT ─────────────────────────────────────┐  │
│  │                                               │  │
│  │  Sleep: 7.5 hours — Quality: Good             │  │
│  │  "Slept better than the night before"         │  │
│  │                                               │  │
│  │  Observation: "Headache worse after screen    │  │
│  │  time yesterday"                              │  │
│  │                                               │  │
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
| 1 | Success Banner | Card | Yes | Duration + positive message |
| 2 | Body Section | Grouped Card | Yes | Symptoms + Vitals |
| 3 | Symptom Card | Sub-card | Yes | Name, severity bar, details |
| 4 | Mind Section | Grouped Card | Yes | Mood, cognitive, stress |
| 5 | Actions Section | Grouped Card | Yes | Medications, self-care |
| 6 | Medication Row | List Item | Yes | Name, dose, time, adherence |
| 7 | Context Section | Grouped Card | Yes | Sleep, environment, observations |
| 8 | Save Button | Primary Button | Yes | Confirm and save |
| 9 | Transcript Link | Text Link | Yes | View full conversation |
| 10 | Edit Button | Icon Button | Yes | Modify extracted data |

#### Section Card Design
Each dimension card has:
- **Header**: Dimension name (BODY / MIND / ACTIONS / CONTEXT) with accent color
- **Content**: Extracted data items
- **Expandable**: Tap to see AI's exact quotes and reasoning
- **Editable**: Long-press any item to correct

**Dimension Colors**:
| Dimension | Accent Color | Icon |
|-----------|-------------|------|
| Body | Soft coral (#FF8A70) | Heart/body icon |
| Mind | Calm purple (#9B8FD0) | Brain/cloud icon |
| Actions | Active green (#7BC47F) | Checkmark/pill icon |
| Context | Warm amber (#FBBF24) | Moon/sun icon |

---

### Screen: Daily Note View (Updated)

**URL/Route**: `/notes/:id`
**Purpose**: Detailed view with 4-dimension organization
**Entry points**: Tap check-in card from Home or Timeline

#### Layout
```
┌─────────────────────────────────────────────────────┐
│  [←]        January 31, 2026         [•••]         │
│             8:30 AM — 1m 24s                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────┬──────────┬──────────┬──────────┐     │
│  │  Body    │  Mind    │ Actions  │ Context  │     │
│  │   ●      │   ○      │   ○      │   ○      │     │
│  └──────────┴──────────┴──────────┴──────────┘     │
│                                                     │
│  ── Body ────────────────────────────────────────   │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  Headache                          4/10     │    │
│  │  ──────────────────────────────────────     │    │
│  │  Location: Temples                          │    │
│  │  Duration: Since waking                     │    │
│  │  Compared to yesterday: Better              │    │
│  │  ──────────────────────────────────────     │    │
│  │  "woke up with a headache again this        │    │
│  │   morning, but it's not as bad"             │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  Fatigue                           3/10     │    │
│  │  ──────────────────────────────────────     │    │
│  │  "feeling a bit tired but manageable"       │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  Energy: Medium                                     │
│                                                     │
│  ─────────────────────────────────────────────────  │
│                                                     │
│  [ View Full Transcript ]                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Navigation
- **Horizontal tabs** at top for 4 dimensions (Body, Mind, Actions, Context)
- Tab indicator dot shows which has data
- Swipe horizontally between dimensions
- Or scroll vertically to see all

---

### Screen: Timeline View (Updated)

Same layout as v1 but check-in cards now show 4-dimension previews.

```
[Timeline entry card]:
─○─ Today, Jan 31
│  ┌─────────────────────────────────────────┐
│  │ Body: Headache (4), Fatigue (3)        │
│  │ Mind: Calm | Actions: Advil taken      │
│  │ Context: Slept 7.5h                    │
│  │ "Woke up with a headache..."           │
│  └─────────────────────────────────────────┘
```

---

### Screen: Trends (Updated for 4 Dimensions)

**URL/Route**: `/trends`
**Purpose**: Visualize patterns across all 4 dimensions

#### Layout
```
┌─────────────────────────────────────────────────────┐
│              Trends                                  │
│  ┌──────────┬──────────┬──────────┬──────────┐     │
│  │  Body    │  Mind    │ Actions  │ Context  │     │
│  │   ●      │   ○      │   ○      │   ○      │     │
│  └──────────┴──────────┴──────────┴──────────┘     │
│  ┌────────────────────────────────────────────────┐ │
│  │ [Week] [Month] [3 Months] [Year]               │ │
│  └────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────┤
│                                                     │
│  [Body tab selected:]                               │
│                                                     │
│  Symptom Frequency                                  │
│  ┌───────────────────────────────────────────────┐  │
│  │ Headache    ████████████████░░ 12 days        │  │
│  │ Fatigue     ████████████░░░░░░  9 days        │  │
│  │ Back pain   ██████░░░░░░░░░░░░  5 days        │  │
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
│  Energy Levels                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │  High │  ●   ●       ●   ●                   │  │
│  │  Med  │    ●   ● ●     ●                     │  │
│  │  Low  │          ●             ●             │  │
│  │       └─────────────────────────             │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  [Mind tab shows: Mood distribution, Stress levels] │
│  [Actions tab shows: Med adherence, Activity log]   │
│  [Context tab shows: Sleep patterns, Triggers]      │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [Home]      [Timeline]     [Trends]    [Settings]  │
└─────────────────────────────────────────────────────┘
```

---

### Screen: Settings (Updated)

Added "Check-in Mode" option per Alan Dye's feedback (allow classic mode).

```
┌─────────────────────────────────────────────────────┐
│              Settings                               │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Check-in Experience                                │
│  ┌───────────────────────────────────────────────┐  │
│  │  Check-in Mode            Immersive       >   │  │
│  │  ──────────────────────────────────────────   │  │
│  │  AI Voice                 Warm & Calm     >   │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Auto-start Listening     [    ●====]         │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  Reminders                                          │
│  ┌───────────────────────────────────────────────┐  │
│  │  Daily Check-in Reminder  [====●    ]         │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Reminder Time               8:00 AM      >   │  │
│  │  ──────────────────────────────────────────   │  │
│  │  Reminder Days          Every day         >   │  │
│  └───────────────────────────────────────────────┘  │
│                                                     │
│  [... rest same as v1]                              │
│                                                     │
├─────────────────────────────────────────────────────┤
│  [Home]      [Timeline]     [Trends]    [Settings]  │
└─────────────────────────────────────────────────────┘
```

**Check-in Mode Options**:
| Mode | Description |
|------|-------------|
| Immersive (default) | Full-screen breathing orb, Direction C |
| Classic | Card-based with visible nav, Direction A |

---

## Interaction Patterns

### Pattern: Breathing Orb Lifecycle

```
[Idle] ──tap/speak──→ [Listening] ──silence 2-3s──→ [Thinking]
                          │                              │
                          │                              ↓
                          │                        [Responding]
                          │                              │
                          └──────user speaks again────────┘
                                                         │
                                                   voice "done"
                                                   or tap finish
                                                         │
                                                         ↓
                                                   [Complete]
                                                         │
                                                         ↓
                                                    [Summary]
```

### Pattern: Swipe-Down Exit

**Use case**: User wants to leave check-in without completing
**Gesture**: Swipe down from top or anywhere on screen

**Behavior**:
1. Drag starts — orb follows finger slightly
2. Past 100px threshold — "Exit check-in?" hint appears
3. Release past threshold — confirmation prompt
4. Confirm — reverse portal transition back to home
5. Release before threshold — snap back

**Confirmation Prompt**:
```
┌─────────────────────────────────────────┐
│  Leave check-in?                        │
│                                         │
│  Your progress won't be saved.          │
│                                         │
│  [Keep going]        [Leave]            │
└─────────────────────────────────────────┘
```

### Pattern: AI Response Streaming

**Behavior**:
1. Orb transitions to Thinking state
2. After 0.5-1.5s, orb transitions to Responding
3. Text appears below orb, streaming word-by-word
4. AI voice plays simultaneously (if audio enabled)
5. When complete, orb returns to subtle glow
6. "Tap to respond" hint appears
7. Or user can just start speaking (auto-detect)

### Pattern: Session Timeout

**Trigger**: 2 minutes of silence after AI response
```
[2 min silence] → Orb gently pulses
                   "Still there? Tap the orb or say
                    something to continue."
                         │
               ┌─────────┴──────────┐
               ↓                    ↓
        [User responds]     [30s more silence]
               │                    │
               ↓                    ↓
        [Continue session]   [Auto-complete]
                             "All done! Let me
                              save your check-in."
```

---

## Responsive Behavior

### Mobile (Primary — 375-428px)
- Full-screen immersive, orb centered
- Transcript area in lower third
- Single column summary

### Tablet (768-1024px)
- Same immersive orb, larger
- Transcript can be wider
- Summary: 2-column for dimension cards

### Desktop (>1024px)
- Orb centered with generous margin
- Transcript to the right of orb (side panel)
- Summary: 2x2 grid for dimension cards

---

## Accessibility Specifications

### Immersive Mode — Critical Accessibility

| Consideration | Implementation |
|---------------|----------------|
| **VoiceOver** | Orb announced as "Health companion, [state]". State changes announced via ARIA live region |
| **Reduce Motion** | Orb animation disabled. Static orb with state icon overlay (mic, dots, speaker, check) |
| **Dynamic Type** | All text scales. Orb stays fixed size. Transcript area grows |
| **High Contrast** | Orb border becomes visible. Background contrast increases |
| **Switch Control** | X button, finish button, and "tap to respond" all accessible |
| **Keyboard (iPad)** | Space = toggle recording, Enter = finish, Escape = exit |

### Haptic Feedback Map
| Event | Haptic Type | Intensity |
|-------|-------------|-----------|
| Enter immersive mode | Impact | Medium |
| Start listening | Impact | Light |
| AI starts responding | Impact | Light |
| Check-in complete | Success | Medium |
| Swipe past exit threshold | Warning | Light |

---

## Data Requirements

### Immersive Check-in Screen
| Data Point | Source | Format | Update |
|------------|--------|--------|--------|
| Audio stream | Device mic | PCM | Real-time |
| Transcription | STT API | String | Streaming |
| AI response | LLM API | String | Streaming |
| Extracted data | NLP | JSON (4 dimensions) | End of session |
| Session duration | Timer | Seconds | Real-time |

### Extraction Output (4 Dimensions)
```json
{
  "body": {
    "symptoms": [{"name": "headache", "severity": 4, "location": "temples"}],
    "vitals": {"energy": "medium"},
    "physical": {"sleep_quality": "good"}
  },
  "mind": {
    "mood": "calm but tired",
    "cognitive": "a bit foggy",
    "stress": "low"
  },
  "actions": {
    "medications": [{"name": "Advil", "dose": "2 pills", "time": "morning"}],
    "selfCare": "planning to rest"
  },
  "context": {
    "sleep": {"hours": 7.5, "quality": "good"},
    "observations": ["headache worse after screen time"],
    "triggers": ["screen time"]
  }
}
```

### Empty States
| Scenario | Content | Action |
|----------|---------|--------|
| First check-in | Onboarding overlay | [Let's start] |
| No data in dimension | "Nothing captured for [dimension]" | N/A |
| Offline during check-in | "Recording saved. Will process when online." | [OK] |
| Error in extraction | "Couldn't capture everything. Review and edit." | [Edit] |

---

## Technical Questions (Updated)

| # | Question | Context | Impact |
|---|----------|---------|--------|
| 1 | Can we achieve <2s AI response with streaming? | Core UX promise | Determines if conversation feels natural |
| 2 | Orb animation at 60fps — performance on older devices? | Canvas/WebGL rendering | May need fallback for low-end devices |
| 3 | Background gradient GPU performance? | Full-screen animated gradient | Battery impact |
| 4 | 4-dimension extraction reliability? | More complex than basic symptom extraction | May need extraction confidence scores |
| 5 | Session state persistence if app backgrounds? | User interrupted mid-check-in | Need to resume or save partial |

---

## Functional Requirements Matrix

| Screen | Component | Requirement | Priority | Story |
|--------|-----------|-------------|----------|-------|
| Home | FAB | Triggers portal transition | Must | US-001 |
| Home | Check-in cards | Show 4-dimension preview | Must | US-002 |
| Transition | Portal animation | 700ms animated transition | Should | US-003 |
| Immersive | Breathing Orb | Respond to voice amplitude 60fps | Must | US-004 |
| Immersive | Status text | Show state below orb | Must | US-005 |
| Immersive | Live transcript | Stream text during speech | Must | US-006 |
| Immersive | AI response | Stream AI text word-by-word | Must | US-007 |
| Immersive | Finish button/voice | End session by tap or voice | Must | US-008 |
| Immersive | Swipe exit | Swipe down with confirmation | Should | US-009 |
| Immersive | Gradient sync | Background shifts with orb state | Should | US-010 |
| Onboarding | First-time overlay | Show on first check-in | Must | US-011 |
| Summary | 4 dimension cards | Body, Mind, Actions, Context | Must | US-012 |
| Summary | Edit function | Correct extracted data | Should | US-013 |
| Summary | Severity bar | Visual 1-10 scale | Must | US-014 |
| Note | Dimension tabs | Horizontal tab navigation | Should | US-015 |
| Trends | Dimension tabs | Filter charts by dimension | Should | US-016 |
| Settings | Check-in Mode | Toggle Immersive/Classic | Could | US-017 |
| All | Reduce Motion | Disable orb animation | Must | US-018 |
| All | VoiceOver | Full screen reader support | Must | US-019 |

---

## Handoff Checklist

### For Visual Design (Stitch Generation)
- [x] All screens documented (8 screens including transition + onboarding)
- [x] All orb states defined (idle, listening, thinking, responding, complete, error)
- [x] Portal transition specified (frame-by-frame)
- [x] 4-dimension extraction model documented
- [x] Gradient background sync specified
- [x] Accessibility requirements for immersive mode
- [x] First-time onboarding flow
- [x] Swipe-down exit pattern
- [x] Session timeout flow

### For Development
- [x] Component inventory complete (all screens)
- [x] Data requirements with 4-dimension JSON schema
- [x] Animation specifications (orb, transition, streaming)
- [x] Haptic feedback map
- [x] Edge cases covered (offline, timeout, exit, error)
- [x] Responsive breakpoints

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-02-06 | Complete redesign for Direction C (Immersive). Added portal transition, breathing orb specs, 4-dimension extraction model, onboarding flow, swipe-exit pattern, accessibility for immersive mode. Based on PRD v2 and expert panel consensus. |
| 1.0 | 2026-01-31 | Initial wireframe specification |
