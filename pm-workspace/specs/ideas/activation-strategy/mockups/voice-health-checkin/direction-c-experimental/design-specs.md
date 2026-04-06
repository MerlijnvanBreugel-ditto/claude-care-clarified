# Direction C: Immersive Wellness Voice Check-in

**Design Philosophy**: Challenge conventions. Create a meditation-app experience that prioritizes emotional calm over data capture. Inspired by Headspace, Calm, and therapeutic environments.

---

## Stitch Project

**Project URL**: https://stitch.withgoogle.com/projects/12397838745842858845
**Project ID**: 12397838745842858845

### Generated Screens

| Screen | Status | Screenshot URL |
|--------|--------|----------------|
| Immersive Voice Check-in | Generated | [View](https://lh3.googleusercontent.com/aida/AOfcidVzpqkOyyJmqsk0hT4nVZBTsc5rTzFuZcBJnMbLmLIiRew5nB0M2v8WzZ3wD7lwMum7zyezAhVUDc49ZNLGzy7NVShk0ruxGqvpCVL3XviSLzcRuXDxKoP6m9oiaR4RWKj2GjpMoMbVGSwkDV6Y-bHmIHZoa1O6zFqkRcizfYUivSK-DeEcYllKzBqiEc8z2guXlA53SmwYVAe5bDOaZMpAfvl8GqAN47osjqUAYmdxWJNnk7LD0ITE7zUy) |
| Wellness Home | Generating | - |
| Reflective Summary | Generating | - |

---

## Design Specifications

### Color Palette (Wellness-Inspired)

| Token | Hex | Usage |
|-------|-----|-------|
| Deep Navy | #0D164F | Text, grounding elements |
| Lavender | #BEAEF8 | Orb gradient, calm accent |
| Soft Peach | #F5D0C5 | Warm gradient tones |
| Cream | #F5F2EB | Surfaces, buttons |
| Warm White | #FEFEFE | Soft text on dark |

**Note**: Similar to Calm's Cloud Burst (#1B2250) color philosophy.

### Typography

- **Font Family**: Newsreader (elegant serif for headlines) + Inter (body)
- **Headlines**: Serif, larger, more emotional
- **Body**: Clean sans-serif, generous line height
- **Reduced text overall** - Let visuals speak

### New Components (Meditation-App Inspired)

1. **Breathing Orb** - Central animated visualization
2. **Gradient Background** - Full-screen, slowly shifting
3. **Floating Transcript** - Semi-transparent, unobtrusive
4. **Minimal Header** - Just close button and timer
5. **Soft CTA** - Inviting, not commanding

---

## Voice Check-in Screen (Immersive)

### Layout Breakdown

```
+------------------------------------------+
|  [X]                             1:24    |  <- Minimal Header
+------------------------------------------+
|                                          |
|                                          |
|                                          |
|              +----------+                |
|            /            \                |
|           |   BREATHING  |               |  <- Hero Orb
|           |     ORB      |               |     (animated, gradient)
|            \            /                |
|              +----------+                |
|                                          |
|            I'm listening...              |
|                                          |
+------------------------------------------+
|     +------------------------------+     |
|     |  Tell me how you're feeling  |     |  <- Floating Transcript
|     |  today                       |     |     (semi-transparent)
|     |                              |     |
|     |  "I woke up feeling a bit    |     |
|     |   tired, but..."             |     |
|     +------------------------------+     |
|                                          |
|        +----------------------+          |
|        |    I'm finished      |          |  <- Soft CTA
|        +----------------------+          |
|        or just say "I'm done"            |
|                                          |
+------------------------------------------+
|          (no tab bar - full screen)      |
+------------------------------------------+

BACKGROUND: Full gradient that subtly breathes
(peach -> lavender -> soft teal)
```

### Key Design Decisions

1. **Full-Screen Immersion**: No tab bar, no distractions
2. **Breathing Orb as Presence**: Represents AI companion's attention
3. **Minimal Text**: The orb communicates more than words
4. **Floating Transcript**: Appears gently, doesn't dominate
5. **Voice-First by Default**: No text input visible
6. **Session Timer**: Subtle reminder of time invested in self-care
7. **Soft Exit**: "I'm finished" is inviting, not abrupt

---

## Inspiration Sources

- **Headspace**: Breathing exercises, session completion flows
- **Calm**: Deep blue palette, sleep stories interface
- **Therapy Sessions**: The quiet attention of being truly heard
- **Sunrise/Sunset**: Natural gradients that feel restorative

---

## Strengths

- **Emotionally Resonant**: Feels like self-care, not medical tracking
- **Reduced Cognitive Load**: Minimal decisions required
- **Calming**: Users may literally relax seeing this screen
- **Differentiated**: Unlike any health app on the market
- **Voice-First Pure**: Voice is the only interaction needed

## Potential Concerns

- **Too Different**: May not feel like "Ditto" anymore
- **Lost Navigation**: Users may feel disoriented without tab bar
- **Data Visibility**: Users don't see what's being captured
- **Accessibility**: Orb animation may be problematic for some users
- **Learning Curve**: Departure from expected health app patterns

---

## Target Emotional Response

When users open this screen, they should:
1. Take a breath
2. Feel their shoulders drop
3. Think "I can share how I really feel here"
4. Not worry about getting it "right"

This is healthcare for the soul, not just the body.
