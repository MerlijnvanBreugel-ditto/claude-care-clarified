# Direction A: On-Brand Voice Check-in

**Design Philosophy**: Strictly follows Ditto's existing Figma design patterns from Carepath screens.

---

## Stitch Project

**Project URL**: https://stitch.withgoogle.com/projects/11388786588223635928
**Project ID**: 11388786588223635928

### Generated Screens

| Screen | Status | Screenshot URL |
|--------|--------|----------------|
| Voice Check-in (Listening) | Generated | [View](https://lh3.googleusercontent.com/aida/AOfcidXGC0ffpvSzarQaihjML7y-cFAEDoHxcfO5NYps3WnV5PVS_AYVZS6KMHvAskgfig9TBZ7krL0RwE84kOoCbvXXRb_vt8lfy9EcocvB998N7kfADLaCI764XJrkU4-Y2X_S9tpPnhKXfUzhBF2PM6NcZi7UHfWkdYfCBkJ9K8l-tzP4vHaWeFR5AZGlfOrZjzk1t-Ui30_4B618srDG2ZJXu8JWEwqZI0zUAey4In6fTprsEWGYaUbL4nzR) |
| Home Dashboard | Generating | - |
| Session Summary | Generating | - |

---

## Design Specifications

### Color Palette (Exact Ditto Match)

| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #0D164F | Buttons, text, active states |
| Yellow | #F3DE70 | Waveform accent, highlights |
| Purple | #BEAEF8 | Decorative elements |
| White | #FFFFFF | Card backgrounds |
| Grey/800 | #82828A | Secondary text |
| Grey/900 | #666670 | Inactive icons |

### Typography

- **Font Family**: Uncut Sans (or Inter as fallback in Stitch)
- **H1**: 32px, Regular
- **H3**: 20px, Medium
- **Body**: 14px, Medium
- **Label**: 14px, Semibold
- **Caption**: 13px, Medium

### Components Used

1. **Page Header** - Back arrow + help icon, 44px touch targets
2. **Cards** - White, 22px border radius, 24px padding
3. **Waveform Visualizer** - Yellow-purple gradient bars
4. **Chat Bubbles** - AI (white), User (navy)
5. **Buttons** - Primary (solid navy), Secondary (outlined)
6. **Tab Bar** - 4 tabs, 90px height

---

## Voice Check-in Screen (Listening State)

### Layout Breakdown

```
+------------------------------------------+
|  [<-]                              [?]   |  <- Header (60px)
+------------------------------------------+
|                                          |
|  +------------------------------------+  |
|  |                                    |  |
|  |     ~~~~ WAVEFORM ~~~~            |  |  <- Status Card
|  |     (yellow-purple gradient)       |  |
|  |                                    |  |
|  |     [*] LISTENING                  |  |
|  |                                    |  |
|  +------------------------------------+  |
|                                          |
|  +------------------------------------+  |
|  | AI: How are you feeling today?    |  |  <- AI Message
|  | Tell me about symptoms, mood...   |  |
|  +------------------------------------+  |
|                                          |
|  +------------------------------------+  |
|  | You: I woke up with a headache    |  |  <- User Message (navy bg)
|  | again this morning, but it's...   |  |
|  +------------------------------------+  |
|                                          |
|  +----------------+ +----------------+   |
|  |     Pause      | |   I'm Done     |   |  <- Action Buttons
|  +----------------+ +----------------+   |
|                                          |
+------------------------------------------+
| [Home] [Timeline] [Trends] [Settings]    |  <- Tab Bar (90px)
+------------------------------------------+
```

### Key Design Decisions

1. **Waveform as Hero**: Central visual element matching Ditto's gradient style
2. **Card-Based Messages**: Same white cards as Carepath appointment cards
3. **Status Prominence**: Clear "LISTENING" indicator with green dot
4. **Tab Bar Visible**: Maintains app context and navigation
5. **Dual Buttons**: Explicit pause and done actions

---

## Strengths

- **Brand Consistency**: Looks like it belongs in Ditto today
- **Familiar Patterns**: Users of Carepath will recognize card styling
- **Clear Hierarchy**: Status > Conversation > Actions
- **Accessible**: High contrast, large touch targets

## Potential Concerns

- **Less Immersive**: Tab bar may distract from voice focus
- **Clinical Feel**: Cards feel more data-focused than emotional
- **Waveform Size**: May need to be larger for visual impact
