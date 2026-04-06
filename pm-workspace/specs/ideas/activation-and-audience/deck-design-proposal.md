# Deck Design Proposal — Nostalgic Warmth Meets Brand Clarity

## The Balance

Three forces to blend:

1. **Nostalgic human warmth** — analog film photography, golden hour, grain, candid moments
2. **Apple-like clarity** — clean layouts, generous whitespace, typographic hierarchy, minimal UI
3. **Ditto brand identity** — Brand Blue (#0D164F), warm background (#FCFAF8), color accents for emphasis

## Color System

### Backgrounds
- **Primary background**: `#FCFAF8` (warm off-white — replaces pure white)
- **Dark slides**: `#0D164F` (Brand Blue — replaces black. This is the biggest brand move.)
- **Accent slides**: `#EFE9DE` (secondary warm cream from brand book)

### Text
- **Primary text**: `#0D164F` (Brand Blue — replaces near-black. Deep enough to read, branded enough to feel Ditto.)
- **Secondary text**: `#6B7280` (warm grey — stays neutral)
- **On dark slides**: `#FCFAF8` (warm white)

### Highlight Colors (for word emphasis)
Rather than coloring full headings, specific words get a brand accent:

- **Teal** `#58B6D2` — for words about understanding, clarity, insight
- **Coral/Orange** `#E8916E` — for words about warmth, care, connection
- **Green** `#F3DE70` used sparingly — for growth, scale, network

Example: "It's a <span style="color:#58B6D2">graph</span>, not a chatbot."
Example: "Care. <span style="color:#E8916E">Clarified.</span>"

This keeps body text in near-black Brand Blue for readability, but key words pop with brand color.

## Typography

- **Headlines**: Bricolage Grotesque (600 weight) — authentic, bold, modern
- **Body**: Inter — clean, readable, professional
- **Quote**: Bricolage Grotesque italic — personal, warm

## Image Treatment

### Full-bleed photos (hero slides)
- Photo fills entire viewport
- Rounded corners: NO (full bleed = edge to edge for impact)
- Overlay: gradient from Brand Blue at 70% opacity, fading to 30%
- Text sits on the overlay in warm white

### Inset photos (content slides)
- Photo displayed with **16px padding** from slide edges
- **24px border-radius** on the photo (rounded corners)
- Photo sits on the `#FCFAF8` warm background — the gap between photo and edge creates breathing room
- This is the "friendly" format — like a Polaroid feeling without being literal

### Split slides (photo + text)
- Photo takes 50% width, full height, with **16px gap** from edges and **24px border-radius**
- Text side has generous padding (80px)
- Background on text side: `#FCFAF8`

## Photo-to-Slide Mapping

| Slide | Photo | Format | Why |
|---|---|---|---|
| **1 — Title** | `89ed73da` (golden field, blurred figure) | Full bleed with Brand Blue overlay | Dreamy, atmospheric, sets the mood |
| **3 — Problem** | `e476dd8b` (grandmother + granddaughter) | Inset with rounded corners | Intimacy, intergenerational care |
| **4 — How families cope** | `Untitled_Candid` (kitchen, child in motion) | Inset with rounded corners | Real life, messy, warm |
| **6 — Life moments** | `38daf1e4` (family group, kids, blue sky) | Inset with rounded corners | Multi-generational, hopeful |
| **7 — Ditto works** | `6a397c56` (elderly man, golden light, looking up) | Split: photo left, text right | Dignified, our user, hopeful |
| **8 — Quote** | `eb83e565` (couple embracing, dining room) | Split: text left, photo right | Tenderness, the care burden |
| **10 — Graph not chatbot** | `31e50e60` (hands touching, mountains) | Full bleed with Brand Blue overlay | Connection, reaching out, expansive |
| **15 — 50+ Audience** | `061b9b0b` (man, face to sun, eyes closed) | Inset with rounded corners | Peace, trust, our audience |
| **16 — Data** | `d2df969d` (two people lying in field, golden hour) | Inset with rounded corners | Calm, grounded, "enough" |
| **20 — Why now** | `34699eca` (person running through flower fields) | Inset with rounded corners | Energy, movement, timing |
| **21 — Pitch** | `9f9f2bf6` (two people running, big sky) | Full bleed with Brand Blue overlay | Scale, hope, future |
| **22 — Close** | `1037fa00` (woman with flower, laughing) | Inset with rounded corners | Joy, warmth, hopeful ending |

### Unused but available
- `305aba89` (woman, orange glasses, plants) — too styled/generated-looking
- `f1109f74` (couple on boat, pink sunglasses) — vibrant but could be too playful
- `14a0dc94` (elderly woman with phone) — too literal for this deck
- `ecb0205f` (couple blowing bubbles) — too stock-photo
- `2c19cb42` (woman laughing, teal coat) — overcast sky doesn't match golden hour

## Layout Principles

1. **Every photo slide gets breathing room.** Never let a photo touch the browser edge (except full-bleed hero shots). The 16px padding + 24px border-radius creates a "held" feeling — like the photo is precious, not wallpaper.

2. **Text slides stay minimal.** Brand Blue background (`#FCFAF8`), plenty of whitespace, no decoration. The cleanness IS the design. Photos do the emotional work; text does the intellectual work. Never mix.

3. **Highlighted words, not highlighted blocks.** Individual words in headings get brand color pops. This creates visual interest without adding UI elements. Maximum 1-2 highlighted words per slide.

4. **Dark slides use Brand Blue, not black.** This is subtle but important — it keeps even the "serious" slides feeling warm and branded rather than corporate.

5. **Three full-bleed photos maximum.** Title, one mid-deck dramatic moment, and the pitch. Everything else is inset with rounded corners. This preserves the impact of full-bleed when it happens.

## Interaction

- Click right → next slide (same as current)
- Subtle crossfade transition (0.5s)
- Elements fade up with 20px translation (same as current, but slightly faster)
- Photos scale in from 1.03 → 1.0 (subtle Ken Burns on entry)
