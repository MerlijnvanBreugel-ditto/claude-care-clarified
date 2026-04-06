# Design Direction Comparison: Voice Health Check-in

**Date**: 2026-02-01
**Feature**: Voice Health Check-in for Ditto Patient App

---

## Quick Comparison Table

| Aspect | Direction A: On-Brand | Direction B: Chat-Forward | Direction C: Immersive |
|--------|----------------------|--------------------------|----------------------|
| **Visual Focus** | Waveform + Cards | Conversation History | Breathing Orb |
| **Navigation** | Tab bar visible | Tab bar visible | Full-screen (no nav) |
| **Input Method** | Voice primary, buttons | Voice + Text hybrid | Voice only |
| **Colors** | Exact Ditto palette | Ditto colors, new patterns | Wellness gradient |
| **Typography** | Sans-serif (Uncut) | Inter (modern) | Serif + Sans mix |
| **Mood** | Professional, calm | Conversational, dynamic | Meditative, immersive |
| **Inspiration** | Ditto Carepath | ChatGPT, Claude, WhatsApp | Headspace, Calm |
| **Panel Score** | 3.2/5 | 3.2/5 | **4.2/5** |

---

## Stitch Projects

| Direction | Project ID | URL |
|-----------|------------|-----|
| A: On-Brand | 11388786588223635928 | https://stitch.withgoogle.com/projects/11388786588223635928 |
| B: Chat-Forward | 5087132463112634065 | https://stitch.withgoogle.com/projects/5087132463112634065 |
| C: Immersive | 12397838745842858845 | https://stitch.withgoogle.com/projects/12397838745842858845 |
| Original Exploration | 9760023575061501495 | https://stitch.withgoogle.com/projects/9760023575061501495 |

---

## Visual Comparison

### Voice Check-in Screen (Primary)

#### Direction A: On-Brand
```
+----------------------+
|  [<-]          [?]   |
|                      |
| +------------------+ |
| |   ~~ WAVEFORM ~~ | |
| |    LISTENING     | |
| +------------------+ |
|                      |
| +------------------+ |
| | AI: How are you? | |
| +------------------+ |
|                      |
| +------------------+ |
| | User: I woke up  | |
| +------------------+ |
|                      |
| [Pause] [I'm Done]   |
|                      |
| [Home][Cal][📊][⚙️]  |
+----------------------+
```
**Screenshot**: [View Direction A](https://lh3.googleusercontent.com/aida/AOfcidXGC0ffpvSzarQaihjML7y-cFAEDoHxcfO5NYps3WnV5PVS_AYVZS6KMHvAskgfig9TBZ7krL0RwE84kOoCbvXXRb_vt8lfy9EcocvB998N7kfADLaCI764XJrkU4-Y2X_S9tpPnhKXfUzhBF2PM6NcZi7UHfWkdYfCBkJ9K8l-tzP4vHaWeFR5AZGlfOrZjzk1t-Ui30_4B618srDG2ZJXu8JWEwqZI0zUAey4In6fTprsEWGYaUbL4nzR)

#### Direction B: Chat-Forward
```
+----------------------+
| [<-] Listening.. [?] |
|                      |
|    +-------------+   |
|    | [AI] How    |   |
|    | are you?    |   |
|    +-------------+   |
|                      |
|  +-------------+     |
|  | I woke up   |     |
|  | with...     |     |
|  +-------------+     |
|                      |
|    +-------------+   |
|    | [AI] Did    |   |
|    | you notice? |   |
|    +-------------+   |
|                      |
| [Okay][Not great][Done]
| [______] [🎤] [>]    |
| [Home][Cal][📊][⚙️]  |
+----------------------+
```
**Screenshot**: [View Direction B](https://lh3.googleusercontent.com/aida/AOfcidX0tXYmGdNw5ZKHeAfsSp6A1xurdgvuZdbcXWFA9lKs4CS7wH1tntcd-nuX5h9VBLE5jzb0LGmQ3mIVvQjBEOVWXSm94FgSEYinXPgyLGlUA-Uw3Ddj1hVzLPUN5xa9QxzyW1LXlx367ScVjMfCEtxrPacjSyLHCOuls_wERXaEt-u8XEh67WYs5MW8mpIif4pd_PZWV_UWvKmDUoYsXM4QGsleOPdZiM637HJb8W84yhpS_s4_-OzYgM4)

#### Direction C: Immersive (Recommended)
```
+----------------------+
| [X]            1:24  |
|                      |
|                      |
|       ╭──────╮       |
|      ╱        ╲      |
|     │  ◉◉◉◉◉   │     |
|     │ BREATHING│     |
|     │   ORB    │     |
|      ╲        ╱      |
|       ╰──────╯       |
|                      |
|    I'm listening...  |
|                      |
|  ┌─────────────────┐ |
|  │Tell me how you  │ |
|  │feel today...    │ |
|  │                 │ |
|  │"I woke up..."   │ |
|  └─────────────────┘ |
|                      |
|   [ I'm finished ]   |
|  or say "I'm done"   |
|                      |
+----------------------+
```
**Screenshot**: [View Direction C](https://lh3.googleusercontent.com/aida/AOfcidVzpqkOyyJmqsk0hT4nVZBTsc5rTzFuZcBJnMbLmLIiRew5nB0M2v8WzZ3wD7lwMum7zyezAhVUDc49ZNLGzy7NVShk0ruxGqvpCVL3XviSLzcRuXDxKoP6m9oiaR4RWKj2GjpMoMbVGSwkDV6Y-bHmIHZoa1O6zFqkRcizfYUivSK-DeEcYllKzBqiEc8z2guXlA53SmwYVAe5bDOaZMpAfvl8GqAN47osjqUAYmdxWJNnk7LD0ITE7zUy)

---

## Design Trade-offs Matrix

| Consideration | A: On-Brand | B: Chat-Forward | C: Immersive |
|---------------|-------------|-----------------|--------------|
| **Learning Curve** | Low | Low | Medium |
| **Brand Consistency** | High | Medium | Low |
| **Emotional Impact** | Medium | Medium | High |
| **Cognitive Load** | Medium | High | Low |
| **Voice-First Purity** | Medium | Low | High |
| **Navigation Clarity** | High | High | Low |
| **Accessibility** | Good | Good | Needs work |
| **Development Effort** | Low | Medium | High |

---

## Expert Picks

| Expert | Top Choice | Reasoning |
|--------|------------|-----------|
| **Jony Ive** | C | "Inevitable. The orb is the interface." |
| **Paula Scher** | C | "Bold restraint. Visual > verbal." |
| **Mike Kresch** | C | "What wellness should feel like." |
| **Alan Dye** | A | "Respects iOS conventions." |
| **Alex Schleifer** | C | "Treats patients like humans." |

**Majority Pick: Direction C (4/5 experts)**

---

## Recommendation Summary

### Primary Recommendation: Direction C (Immersive Wellness)

**Why Direction C:**
1. Highest expert panel score (4.2/5)
2. Most differentiated in the market
3. Best suited for chronic patient needs (low energy, high fatigue)
4. Creates emotional connection vs. data capture
5. Pure voice-first experience

**With These Modifications:**
- Add navigation affordances (swipe to exit)
- Build onboarding for new paradigm
- Ensure Reduce Motion accessibility
- Maintain subtle Ditto brand elements

### Backup: Direction A (On-Brand)

**When to use Direction A:**
- If user testing shows Direction C confusion
- For users who prefer explicit controls
- As an "Advanced Mode" option in settings

### Not Recommended: Direction B (Chat-Forward)

**Why not B:**
- Splits attention between voice and text
- Higher cognitive load
- Doesn't commit to either paradigm
- Feels more "tech" than "care"

---

## Next Steps

1. **Iterate on Direction C** - Create V2 with panel feedback
2. **Prototype Animation** - Breathing orb + transition
3. **User Test** - 5-8 chronic patients
4. **Accessibility Audit** - VoiceOver, Reduce Motion
5. **Design Remaining Screens** - Summary, Home integration

---

## Files Generated

| File | Location |
|------|----------|
| Mobbin Research | `mockups/mobbin-research.md` |
| Direction A Specs | `mockups/direction-a-on-brand/design-specs.md` |
| Direction B Specs | `mockups/direction-b-partly-on-brand/design-specs.md` |
| Direction C Specs | `mockups/direction-c-experimental/design-specs.md` |
| Panel Consensus | `mockups/panel-consensus.md` |
| This Comparison | `mockups/comparison.md` |
