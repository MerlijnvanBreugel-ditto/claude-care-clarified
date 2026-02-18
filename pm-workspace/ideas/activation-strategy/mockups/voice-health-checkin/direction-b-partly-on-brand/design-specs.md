# Direction B: Chat-Forward Voice Check-in

**Design Philosophy**: Keep Ditto colors, but adopt modern AI chat interface patterns from ChatGPT, Claude, and messaging apps.

---

## Stitch Project

**Project URL**: https://stitch.withgoogle.com/projects/5087132463112634065
**Project ID**: 5087132463112634065

### Generated Screens

| Screen | Status | Screenshot URL |
|--------|--------|----------------|
| Voice Check-in Chat View | Generated | [View](https://lh3.googleusercontent.com/aida/AOfcidX0tXYmGdNw5ZKHeAfsSp6A1xurdgvuZdbcXWFA9lKs4CS7wH1tntcd-nuX5h9VBLE5jzb0LGmQ3mIVvQjBEOVWXSm94FgSEYinXPgyLGlUA-Uw3Ddj1hVzLPUN5xa9QxzyW1LXlx367ScVjMfCEtxrPacjSyLHCOuls_wERXaEt-u8XEh67WYs5MW8mpIif4pd_PZWV_UWvKmDUoYsXM4QGsleOPdZiM637HJb8W84yhpS_s4_-OzYgM4) |
| Home Dashboard | Generating | - |
| Session Summary | Generating | - |

---

## Design Specifications

### Color Palette (Ditto Colors, New Context)

| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #0D164F | User bubbles, active elements |
| Yellow | #F3DE70 | Active mic indicator, highlights |
| Purple | #BEAEF8 | Accent, decorative |
| Background | #F1F1F1 | Page background |
| AI Bubble | #F5F5F5 | Light gray for AI messages |
| Off-white | #EFE9DE | Quick reply chips |

### Typography

- **Font Family**: Inter (modern, readable)
- **Chat Text**: 16px for readability
- **Timestamps**: 12px, gray
- **Status**: 14px, medium weight

### New Components (Mobbin-Inspired)

1. **Compact Status Header** - Integrated listening indicator
2. **Chat Bubbles** - Rounded, with avatar for AI
3. **Live Transcription** - Real-time text with pulsing indicator
4. **Quick Reply Chips** - Suggested responses
5. **Smart Input Bar** - Text + voice hybrid

---

## Voice Check-in Screen (Chat-Forward)

### Layout Breakdown

```
+------------------------------------------+
|  [<-]    [Listening...] pulse    [?]     |  <- Compact Header
+------------------------------------------+
|                                          |
|     +--------------------------------+   |
|     | [AI] How are you feeling today?|   |  <- AI Bubble (left)
|     | Tell me about symptoms, mood,  |   |
|     | or anything on your mind.      |   |
|     +--------------------------------+   |
|                                          |
|  +--------------------------------+      |
|  | I woke up with a headache again |      |  <- User Bubble (right)
|  | this morning, but it's not as   |      |
|  | bad as yesterday. Maybe 4/10.   |      |
|  +--------------------------------+      |
|                                          |
|     +--------------------------------+   |
|     | [AI] I'm sorry to hear that.   |   |
|     | Did you notice any triggers?   |   |
|     +--------------------------------+   |
|                                          |
|  +--------------------------------+      |
|  | The pain is mostly in my temp...|  *  |  <- Live Transcription
|  +--------------------------------+      |
|                                          |
+------------------------------------------+
|  [I'm feeling okay] [Not great] [Done]   |  <- Quick Replies
+------------------------------------------+
|  [____________________] [MIC*] [Send]    |  <- Input Bar
+------------------------------------------+
| [Home] [Timeline] [Trends] [Settings]    |  <- Tab Bar
+------------------------------------------+
```

### Key Design Decisions

1. **Conversation is Hero**: Chat history takes center stage
2. **Compact Status**: Listening indicator in header, not separate card
3. **AI Avatar**: Small icon to personify the AI companion
4. **Quick Replies**: Reduce cognitive load with suggested responses
5. **Hybrid Input**: Support both voice and text seamlessly
6. **Real-time Transcription**: Words appear as user speaks

---

## Inspiration Sources

- **ChatGPT Voice Mode** (Nov 2025): Integrated voice in chat view
- **Claude Mobile**: Clean chat bubbles with AI avatar
- **WhatsApp**: Familiar messaging patterns
- **Notion AI**: Inline AI chat experience

---

## Strengths

- **Familiar Pattern**: Feels like texting/chatting
- **Conversation History Visible**: Context always available
- **Lower Barrier**: Quick replies for low-energy moments
- **Hybrid Flexibility**: Voice or text, user's choice
- **Modern Feel**: Matches expectations from AI apps

## Potential Concerns

- **Less Immersive**: May feel too "appy" vs. therapeutic
- **Visual Clutter**: More elements on screen
- **Voice De-emphasized**: Mic button competes with text input
- **Healthcare Identity**: May feel too casual for medical context
