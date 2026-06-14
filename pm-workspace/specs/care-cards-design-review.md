# Care Cards — Design Kitchen Review

> Reviewed: 2026-03-25
> Perspective: Apple (craft & restraint), Headspace (emotional design), Meta (social patterns)
> Status: Pre-iteration critique

---

## What's Good

1. **The core insight is right.** Intent → compose → send is the correct skeleton. Guiding people through "how do you want to reach out" before asking them to write is genuinely good UX. The Lovable prototype nailed this.
2. **Memories as a collection** is emotionally powerful. The idea that cards accumulate into a private gallery of support is unique — no one else does this in healthcare.
3. **The share-outside-Ditto → invite mechanic** is smart. A card is warmer than a cold invite link.

## What's Wrong — Honest Critique

### Problem 1: It looks like a form, not an experience

**Apple lens:** Apple's best interactions feel inevitable — each step reveals itself naturally. Our wireframes feel like a multi-step form wizard. Screen 1 is a list of radio buttons. Screen 2 is a form with a textarea. Screen 3 is a confirmation page. This is the pattern of an insurance claim, not a love letter.

**What's missing:** Emotional progression. The screens don't build feeling — they collect inputs. There's no moment where the user thinks "oh, this is beautiful." The card should be the hero from the first moment, not something that appears at the end.

**Direction:** The card itself should be visible and evolving from Step 1. Every choice the user makes should visually change the card in real-time. Think of how Apple's Watch face customizer works — you're always looking at the thing you're creating, not at a form.

### Problem 2: The intent selection is too cognitive

**Headspace lens:** Headspace asks "How are you feeling?" with soft illustrations and one-word answers. We ask "How do you want to reach out?" with 4 text-heavy tiles that require reading descriptions. This is a thinking task when it should be a feeling task.

**What's missing:** Visual/emotional entry points. "Thinking of them" vs. "Offer support" vs. "Express love" — these are intellectual distinctions that most people can't articulate in the moment. They just know they feel something.

**Direction:** Replace text-heavy intent tiles with visual moods — large illustrations or color fields with a single word. "Warmth." "Strength." "Joy." "Love." Let the visual do the heavy lifting. Or even simpler: skip intent entirely for event-triggered cards and go straight to the card composer with suggested visuals based on the event type.

### Problem 3: The compose screen tries to do too much in too little space

**Apple lens:** Our compose screen has: a card preview, a visual area, a writing cue, a text input, a sender name, AND a visual picker strip. That's 6 distinct UI elements competing for attention on a 393px screen. Apple would never.

**What's missing:** Focus. The compose experience should feel like writing on a beautiful piece of stationery, not filling out a card template.

**Direction:** Split compose into a two-phase interaction:
- **Phase A: Visual** — Full-screen card with swipeable backgrounds. No text yet. Just pick the vibe. This should feel like browsing an art gallery, not a color picker.
- **Phase B: Write** — The card zooms in, keyboard rises, and the user writes directly on the card. Writing cue appears as ghost text. The visual is decided — now just write.

### Problem 4: The visual picker is an afterthought

**Headspace lens:** In Headspace, visuals ARE the product — every screen is a crafted illustration that sets the emotional tone. In our wireframes, the visual picker is a tiny strip of 4 emoji-sized thumbnails at the bottom. The visuals — which are supposed to make this card worth receiving — are the smallest element on screen.

**What's missing:** Visuals should be immersive, not a thumbnail grid. The flower/abstract imagery from the Figma concepts is beautiful. It deserves full-screen treatment.

**Direction:** Make visual selection a full-bleed, swipeable experience. Each visual fills the card. Swipe horizontally to browse. The card transforms with each swipe. This is the "delight" moment — the step where people go "oh, this is lovely."

### Problem 5: The card itself isn't special enough

**Meta lens:** Meta learned with Facebook birthday cards and Messenger effects that the delivered artifact has to feel premium enough to be worth the effort. Our card wireframe is: visual + text + sender name on a white rectangle with a shadow. It looks like a notification card, not a keepsake.

**What's missing:** The card needs to feel like an object — something with weight, texture, maybe even a subtle animation when received. Think of iOS's message effects (confetti, balloons) but as a permanent artifact, not a one-time animation.

**Direction:**
- Cards should have a distinct "card" shape — not just a rounded rectangle. Consider a slight paper texture, a folded corner, or a postage-stamp-style border.
- The visual should bleed to the edges of the card (not sit in a smaller box inside the card).
- On the receiver's side, the card should "open" — either a flip animation or an unfold. The message isn't visible at first. You open it.
- In the Memories grid, cards should look like a scattering of physical cards, not a Bootstrap grid.

### Problem 6: Receiving feels passive

**Meta lens:** Meta's strongest social features create reciprocity loops. Someone sends you a message → you feel compelled to respond. Our "Receive" screen shows the card with a "Send one back" button, which is fine, but there's no moment of emotional surprise.

**What's missing:** The reveal moment. When you get a care card, the first screen should be an emotional beat — not immediately showing the full message. Build anticipation.

**Direction:**
1. Push notification: "Michelle is thinking of you 💛"
2. Open: See the card back/envelope — visual only, message hidden
3. Tap to reveal: Card flips/opens, message appears with a gentle animation
4. After reading: "Send one back" appears naturally

This turns receiving from a single moment into a 3-beat emotional arc.

### Problem 7: The deepening question may not be needed

**Apple lens:** Every additional screen is a dropout risk. The deepening question ("What made you think of Sarah?") adds a screen that exists to generate better writing cues. But if the writing cues are good enough without it, this screen is pure friction.

**Direction:** Test without it first. The intent alone ("Thinking of them") may be enough to generate a good writing cue. If writing quality suffers, add deepening back as an optional "need inspiration?" toggle on the compose screen — not a mandatory step.

---

## Proposed Iteration Directions

### Direction A: "Card-First Composer" (recommended)

The card is always visible. Every interaction modifies the card in real-time.

```
Flow: [Pick visual (full-bleed swipe)] → [Write on card (keyboard on card)] → [Preview & send]
```

- 3 screens total for event-triggered, 4 for unprompted (add intent)
- Visual selection is full-screen and immersive
- Writing happens directly on the card, not in a separate textarea
- Card preview IS the compose screen — not a separate step

### Direction B: "Feeling-First"

Start with mood/emotion, let everything follow from that.

```
Flow: [How are you feeling? (visual moods)] → [Card auto-generates with visual + cue] → [Edit & personalize] → [Send]
```

- Fewer decisions — the system makes opinionated choices based on the mood selection
- User adjusts rather than builds from scratch
- Higher completion rate but less personalization

### Direction C: "Story Arc"

Lean into the Lovable prototype's guided narrative, but make it feel like an interaction, not a form.

```
Flow: [Who? (recipient)] → [Why? (intent, visual)] → [What? (write)] → [Send (reveal preview)]
```

- Keep all the steps but redesign each as an immersive, single-action screen
- Each screen has one question, one action, one visual
- Full-screen transitions between steps
- The card builds progressively — visible in the background getting more complete

---

## Quick Wins (Apply to Any Direction)

1. **Full-bleed visuals** — No more thumbnail strips. Visuals fill the card.
2. **Card flip on receive** — Add a reveal moment, don't show message immediately.
3. **Scattered memories layout** — Cards in the collection should feel organic, not gridded.
4. **Writing cues as ghost text** — Show the cue inside the message area, not above it.
5. **Haptic feedback** — On send, on receive-reveal, on visual swipe. Makes it feel physical.
6. **Progressive card assembly** — Show the card getting built as user progresses through steps.
7. **Uncut Sans italic for card messages** — Distinguish the card content from UI text.

---

## Recommendation

Start with **Direction A (Card-First Composer)** because:
- Fewest screens → highest completion rate
- Card is always visible → highest emotional engagement
- Visual selection as the first step → sets the delight tone immediately
- Directly comparable to the Lovable prototype's best moment (the card preview)

Apply all Quick Wins regardless of direction chosen.
