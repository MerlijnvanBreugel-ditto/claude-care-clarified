# The Interface: Design Panel Brainstorm

**Exercise**: 10 head-of-design personas, 10 approaches, cross-critique, 3 merge directions.
**Date**: 2026-04-15
**Author**: Mewtwo
**Status**: Brainstorm artifact. Input to interface design decisions, not a spec.
**Parent doc**: [Care Brain Master Synthesis](care-brain-master-synthesis.md)

---

## 1. The design brief (why this is hard)

The interface has to hold 45 jobs-to-be-done, 22 wow moments, and eight emotional registers ranging from "you finished your antibiotic" to "your cancer is progressing." It has to serve Jan the 74-year-old multi-condition patient, Aysel the working caregiver, Corrie at 81 with cognitive decline, and Pieter's 8-year-old granddaughter. It has to work for the patient AND their care circle. It has to be a better vessel than a chatbot for every one of the wow moments, without collapsing into a generic dashboard or a taxonomy of tabs.

Three design tensions define the problem:

**Modular vs. distinctive.** A pure card system (the obvious answer) scales to 45 JTBD but risks looking like every admin dashboard. A bespoke interface per wow moment differentiates but cannot cover 45 jobs. Neither extreme works.

**Emotional vs. operational.** Mara after her oncology appointment needs presence. Aysel managing her mother's care needs speed. Corrie needs radical simplicity. A single interface that serves all three is not obvious.

**Anticipatory vs. navigable.** The magic formula (removal, articulation, anticipation) favors an assistant that appears when needed. But patients also need to navigate their own record, look things up, revisit yesterday's summary. Pure anticipation is a black box. Pure navigation is an app.

The brief, compressed: *the interface must hold the full JTBD catalogue without feeling like a catalogue, feel human at the hardest moments, and be shareable in a way that makes the recipient want one too.*

The chat interface fails every test. It is linear when the journey is parallel. It is textual when the truth is visual. It is one-voice when the user has a circle. It is amnesic when the memory is the moat. The question is not "what replaces chat" but "what shape holds this product."

---

## 2. The panel

Ten designers, picked for range (visual-to-textual, industrial-to-editorial, warm-to-systematic, AI-native-to-pre-digital). Each represents a tradition with a defensible answer to the brief.

| # | Designer | Tradition | Why in the room |
|---|---|---|---|
| 1 | **Jony Ive** (LoveFrom, ex-Apple) | Reductive craft | The "one object" tradition. The material-honesty instinct. |
| 2 | **Joe Gebbia** (Airbnb) | Hospitality-first | The "welcome" instinct. Warmth at the door. |
| 3 | **Ian Spalter** (Instagram, YouTube) | Feed & story | The shareability instinct. Circle-native thinking. |
| 4 | **Yin Yin Wu + Andy Puddicombe's team** (Headspace) | Emotional pace | The "product has a nervous system" instinct. |
| 5 | **Dieter Rams** (Braun, via principles) | Functional discipline | The "less, but better" conscience. |
| 6 | **Karri Saarinen** (Linear) | Operator-grade | The density-with-elegance instinct. Caregiver mode. |
| 7 | **Jason Yuan** (Dia, New Computer) | AI-native ambient | The "canvas, not chat" instinct. |
| 8 | **Michael Bierut** (Pentagram) | Editorial identity | The "this life is worth documenting" instinct. |
| 9 | **Jesper Kouthoofd** (Teenage Engineering) | Tactile character | The "objects can be loved" instinct. |
| 10 | **Susan Kare** (original Mac) | Pictographic warmth | The "crosses language, age, cognition" instinct. |

Each gets to propose one approach. No diplomatic hedging, no consensus. Real opinions.

---

## 3. The ten approaches

### Approach 1 — Jony Ive: *The One Object*

The interface is not a collection of screens. It is a single material object that transforms. After a recording, the object is a summary. Before an appointment, it is a briefing. When hard news is in it, it desaturates and slows. The object is always one thing, because the patient can only think about one thing.

**Defining mechanics**
- A single hero surface at any moment. Peripheral navigation is gestural: pull down for time (the journey), pull right for the circle, pull up for the next thing on the horizon.
- Transitions have weight. Motion is physical, not stylistic.
- Typography is the center of gravity. One custom serif for patient content. One neutral sans for system labels. No icons as primary UI.
- Near-monochrome by default. A single warm tint when the moment calls for care. Hard-news states drain color.
- No tabs. No chrome buttons. Every affordance is the material responding.

**What it's great at**: Dignified moments. Mara after her oncology visit. The cancer-progression share. Anything where restraint is the message.
**What it struggles with**: Caregivers managing five concurrent concerns. The 45 JTBD risk piling into one surface that is serene and unusable.
**One sentence**: "If the product can only say one thing at a time, make that one thing beautiful and honest."

### Approach 2 — Joe Gebbia: *The Home*

Ditto is not a dashboard, it is a home with rooms. You are welcomed in. Someone hands you the summary. When you leave, someone sees you out. The hospitality framing converts every interaction from utility to relationship.

**Defining mechanics**
- Opening line, not opening dashboard: *"Welcome back, Mara. You've just been with Dr. de Jong. Come in when you're ready."*
- Rooms instead of tabs: The Summary Room, The Circle Room, The Journey Room, The Upcoming Room. Each has its own warm interior atmosphere (natural light aesthetic, low chrome, human-scale).
- Moving between rooms feels like walking through a doorway. Subtle parallax, warm fade.
- Shares are letters, not links. The recipient receives a framed card, addressed to them by name, from Ditto on behalf of the patient.
- Copy is second-person, present, warm. The AI never refers to itself.

**What it's great at**: Trust. First-time use. The circle onboarding moment. The "I want this too" feeling when Sanne receives her father's update.
**What it struggles with**: Power users. Caregivers under time pressure. Density. The "room" metaphor gets in the way of Aysel at 11pm managing four prescriptions.
**One sentence**: "Hospitality is the product. Warmth first, utility second."

### Approach 3 — Ian Spalter: *The Story Feed*

A health journey is content. Content has a native shape: stories and a feed. Stories at the top (the quick glance: today's summary, tomorrow's prep, the circle's updates). Feed below (reverse-chronological life, each moment a card). Tap to expand, swipe to share.

**Defining mechanics**
- Story ring up top. Three to five stories: your most recent summary, tomorrow's prep, new items from the circle, a doctor's note that just arrived.
- Main feed: each post is a card with cover imagery, title, timestamp, and reactions from the circle. Summary post, prep post, pattern post, lab-result post, share post.
- Immersive detail views: full-bleed when you tap in. Pinchable charts. Haptic transitions.
- Reactions and comments from the circle appear under each post (threaded).
- Share is native and the hero: one tap produces adapted previews for each recipient.

**What it's great at**: Virality. Circle-native behavior. The share-that-writes-itself is effortless here because the whole app is share-shaped.
**What it struggles with**: Dignity. Hard news in a feed feels trivializing. Also risks the "scrolling your own illness" anti-pattern.
**One sentence**: "The patient's journey is content. Design for the shape of content."

### Approach 4 — Headspace team: *The Breath*

The product has a nervous system. Every pipeline output carries a weight token (routine / important / heavy / grief-adjacent), and the interface physically responds. Pace, color, motion, audio, and whether-to-interrupt are all functions of the weight.

**Defining mechanics**
- Emotional weight token passes from pipeline to render layer. UI shell reads it and adjusts.
- Heavy weight: the app opens slowly. A single breath cycle before the content appears. Desaturated palette. Soft illustration. "Take a moment."
- Routine weight: quick, punchy, efficient. Feels like Linear.
- Audio is first-class. Any summary can be read aloud in a warm voice. A subtle ambient tone underlies the hard moments.
- "Call someone?" prompt after heavy content. A single warm button, not a sidebar widget.
- Soft illustrative language (abstract shapes: ring, cloud, flow). No medical imagery. No photography of patients.

**What it's great at**: Mara, Corrie's son, Leila learning her MS is progressing. The hardest moments are the ones where product feel matters most.
**What it struggles with**: Day-to-day operational care. Aysel at 11pm does not want a breath cycle before she can check a medication. Without a mode switch, calm becomes friction.
**One sentence**: "Speed is the ChatGPT default. Presence is the differentiator."

### Approach 5 — Dieter Rams: *The Principle*

Strict functional discipline. Every element earns its place. No flourishes. No "magical" animation, no storytelling chrome. The beauty is in the rigor. If a section does not carry function, it is deleted.

**Defining mechanics**
- Fixed modular grid. Six core modules: Summary, Medications, Timeline, Circle, Upcoming, Questions. Each a card with a function label and scannable content. No decorative framing.
- One typographic family, three weights. One accent color, used sparingly for action states.
- Copy tone: honest, plain, no performative warmth. The warmth comes from the content inside, not from the frame.
- Every interaction is predictable. No hidden gestures. The same action produces the same result at the same location.
- No illustrations. No ambient illustration. No stock photography.

**What it's great at**: Trust via predictability. Works for Jan the retired engineer, works for healthcare-literate caregivers. The opposite of AI-slop.
**What it struggles with**: The emotional peaks. A cancer progression summary delivered in a functional card feels bureaucratic. No room for the keystone magic.
**One sentence**: "Trust is built through discipline, not styling. Everything else is theater."

### Approach 6 — Karri Saarinen: *The Operator Console*

Health is complex. Treat the user as capable. Give them speed, density, precision, and the ability to navigate their own record like a power user.

**Defining mechanics**
- Command palette (Cmd-K): jump to any doctor, any medication, any question, any appointment. Available on web and iPad-with-keyboard. Mobile gets a "quick find" analog.
- Dense cards. More information per screen than Headspace, less than a spreadsheet. Monospace-informed typography in secondary data, humanistic sans in narrative.
- Every entity has a URL. `/mara/conditions/colon-cancer`, `/mara/appointments/2026-04-20`. Shareable, bookmarkable, linkable.
- Keyboard shortcuts for the caregiver cohort. Custom views saved per user.
- Motion is functional micro-animation. No emotion in the chrome. Emotion lives in the content.

**What it's great at**: Aysel managing her mother's care. Pieter tracking his wife's MS across specialists. The caregiver segment, the engineer segment, the power users who currently use Notion for their own health records.
**What it struggles with**: Mara on the worst day of her life. Corrie at 81. This is the wrong surface for either.
**One sentence**: "The caregiver is a professional. Design the tool a professional would choose."

### Approach 7 — Jason Yuan: *The Ambient Mind*

AI-native. The interface is a living canvas where the AI places cards, draws connections, and responds to intent. Chat is one modality among many; the primary modality is cards the AI renders without being asked.

**Defining mechanics**
- On open, the canvas is not empty. The AI has placed what it thinks you need most right now (prep for tomorrow, an unresolved concern from last week, the new lab result).
- Intent entry point: one input field, always present. Text, voice, or dictated. Results come back as composed cards, not as chat bubbles.
- Cards are pinnable. You pin a medication card, a chart card, and a source card into a "board" that persists, shareable and re-openable.
- Threading: every life event (appointment, scan, symptom) is a thread. The AI shows thread relationships as light connecting lines.
- The AI is a character but minimal. Text appears in negative space, not in bubbles. It talks only when useful.

**What it's great at**: The 45 JTBD. Because the interface is not a fixed set of surfaces but a composition engine, new pipelines slot in natively. Also great at the "asking what you didn't know to ask" moment.
**What it struggles with**: First-time use. The blank canvas problem. Power users love it; Corrie is baffled by it. Needs strong anticipation to be navigable.
**One sentence**: "The navigation is intent. The interface composes itself."

### Approach 8 — Michael Bierut: *The Publication*

The app is a personal publication about the patient. Editorial framing gives every piece of content hierarchy, dignity, and meaning. The patient's life is worth documenting. The publication shape is how the documentation becomes legible.

**Defining mechanics**
- Masthead on the home surface: *"Mara's Care Journal. Volume 4. April 2026."*
- Lead story: this week's most important thing (the scan result, the medication change, tomorrow's appointment). Below the fold: standing sections.
- Standing sections, named editorially: "The Doctor Said", "The Circle Says", "Questions Outstanding", "What's Next", "Looking Back".
- Serif headlines, sans body. Editorial hierarchy (lead, byline, pullquote, subhead, body).
- Archive is a first-class view: past issues, bookbindered by month. The journey page IS the back-catalogue.
- Share: the shared card is a pullquote card, the kind the daughter screenshots and sends to a sibling.

**What it's great at**: Dignity, memory, the journey page, the moments that deserve a masthead. Mara's condition page comes alive as an ongoing feature story about her.
**What it struggles with**: Daily micro-interactions. "Did I take my pill?" should not require a feature article. Needs a utility layer beneath the editorial shell.
**One sentence**: "A life is not a dashboard. It's a story being written."

### Approach 9 — Jesper Kouthoofd: *The Instrument Pack*

Each pipeline output is an "instrument," a compact, tactile, characterful mini-app with its own personality. Cards are collectible, playable, joyful. People fall in love with objects that have character. Most medical apps have none.

**Defining mechanics**
- The medication card is a drawer you pull open. It clicks (haptic + sound).
- The summary card is a tape you play. Scrubbable audio timeline with transcript underlay.
- The circle card is a mixer. Each circle member is a channel with a waveform of their activity.
- Utility colors used rigorously: orange = action, green = done, blue = know, red = urgent.
- Haptics are loud, specific, and differentiated per instrument.
- Typography and iconography are unified in a single utility-device aesthetic. Feels like an OP-1, not a WebMD.

**What it's great at**: Fighting the medical-app-boredom ceiling. Giving patients a reason to open the app on a day where nothing is happening. Daily retention.
**What it struggles with**: Cancer progression. The tactile-joy register does not translate to heavy news without a clear mode switch. And the aesthetic risks being more seen than felt by an older cohort.
**One sentence**: "Dignity is not the same as solemnity. People can love their care object."

### Approach 10 — Susan Kare: *The Picture Book*

Pictographic warmth. Every person, place, medication, and concept has a small, hand-crafted icon. The interface is iconographic, not typographic. Icons cross language, age, and cognition where typography cannot.

**Defining mechanics**
- Each doctor has a hand-drawn avatar (crafted portrait, dignified, not cartoonish).
- Each medication has a unique icon. Not stock pill clip-art, a crafted pictogram.
- The care circle is literally drawn: the patient at center, each circle member a portrait around them.
- The journey is a path with way-markers. Each way-marker is a small scene.
- Copy is minimal. The iconography carries most of the meaning.

**What it's great at**: Corrie. The granddaughter. Cross-language cohorts (Aysel's Turkish-speaking mother). Cognitive decline. The accessibility case.
**What it struggles with**: Density. A caregiver with 12 medications across three doctors cannot navigate 36 hand-drawn icons. Iconography scales until it doesn't.
**One sentence**: "Icons welcome. Typography excludes. Craft makes the difference between warm and childish."

---

## 4. The brainstorm

A fictional room. They have read each other's approaches. The tension is real.

### Round 1 — the opening shots

**Ive to Yuan**: "Your canvas has no anchor. A patient in a waiting room with wet eyes does not want a composition engine. They want one thing, handled. The stone is an object you can hold. An ambient AI is vapor."

**Yuan to Ive**: "Your stone has one facet. The Care Brain has 45 facets. A patient with a cancer journey, a chronic condition, a caregiving role, and an aging parent has four journeys running simultaneously. One surface cannot hold that without becoming a stack of screens, at which point you have an app, not an object."

**Gebbia to Rams**: "Your grid is honest but it does not welcome. People in pain do not need a form. They need a room. Your product will be correct and nobody will love it."

**Rams to Gebbia**: "Your hospitality is performed. 'Welcome back, Mara' is a line of copy, not a relationship. People in pain distrust performance. Discipline IS warmth when everything else in their life is uncertain."

**Puddicombe's team to Saarinen**: "Your operator console is wrong for Mara. Speed is not the virtue, presence is. You are optimizing for the 10% of interactions where the patient is a caregiver. You are losing the 90% where she is a human being."

**Saarinen to Puddicombe**: "Your slowness is a form of paternalism. Pieter caring for his wife does not have time for a breath cycle. Don't prescribe calm to people who need capability. The product has to stop assuming the user is grieving."

### Round 2 — the feed, the magazine, and the share

**Spalter to Bierut**: "Your magazine is beautiful and it is for one reader. Feeds work because they carry. Publications do not. The share is the growth loop, and you have designed the one shape that does not travel."

**Bierut to Spalter**: "Feeds are amnesiac. A health journey is not a scroll. Your feed makes every week equivalent to every other week, which is the opposite of how a patient experiences their own life. The publication form IS the memory. And the pullquote is, in fact, the most shareable object in print history."

**Kouthoofd to Ive**: "Your stone is cold. People fall in love with objects that hum. Your dignity is real, but you have removed the thing that makes people open an app on a quiet day."

**Ive to Kouthoofd**: "Your instruments are costumes. Personality is not performance. Materials have dignity. Instruments trivialize. A patient does not want their cancer to have a sound effect."

### Round 3 — Kare's challenge

**Kare to the room**: "None of you have solved for Corrie. You've designed for Mara, Aysel, Jan, Pieter. Corrie is 81 and her cognition is declining. Typography excludes her. Feeds confuse her. Command palettes exclude her. Publications exclude her. Iconography is not optional if the product is going to be what the master synthesis says it is."

**The room back to Kare**: "Icons scale until they don't. The 45 JTBD cannot be represented iconographically without becoming a toy. Where does the language go for a drug interaction explanation? For an advance directive? For the cross-doctor catch?"

**Kare**: "It's a component, not a whole app. You design the complex surface for the competent, and the pictographic surface for the cognitively constrained. The mistake is thinking you need one interface. The 45 JTBD is not the problem. The range of users is."

### Round 4 — the convergences

After the fireworks, things settle. Points of agreement emerge:

**Agreement 1 — one interface cannot serve the whole cohort.** Ive wants dignity for Mara. Saarinen wants capability for Aysel. Kare is right that Corrie needs her own surface. *The interface is not singular. It is a base system with modes.* This was the first real unlock in the room.

**Agreement 2 — the card is the unit, but how cards compose is the interesting question.** Everyone except Ive agrees that cards are the atomic unit. Ive holds out for the single object, but concedes that "one card at a time" is a compatible framing. The debate moves from "is it cards?" to "what governs their composition, pace, and presentation?"

**Agreement 3 — the share is the hero surface.** Unanimous. Gebbia frames it as a letter, Spalter as a post, Bierut as a pullquote, Kare as a picture, Kouthoofd as a keepsake. Different framings, same conclusion. The share is where the most design craft goes.

**Agreement 4 — an emotional weight system is needed.** Puddicombe's weight token is not just a Headspace idea. It becomes the mechanism by which every other designer's product stays true in hard moments. Ive uses it to slow motion and drain color. Saarinen uses it to suppress density. Spalter uses it to change how a feed item presents. It is an infrastructural primitive, not a cosmetic layer.

**Agreement 5 — there must be an anticipatory layer on top of any navigable one.** Pure anticipation (Yuan) is too opaque for first-time use. Pure navigation (Rams) is amnesic about what the user needs now. Every approach has to have both. The default view is what the AI thinks you need. The escape is the ability to navigate.

**Agreement 6 — editorial framing is undervalued.** Bierut wins a quiet victory. Most of the other designers admit, reluctantly, that the editorial form answers a problem no other form answers: *how do you make a patient feel their own journey is significant?* Even Rams concedes that if there is one exception to his principle of function-over-form, it is the journey page.

**Agreement 7 — iconography earns its place in accessibility and shares.** Kare wins a similar quiet victory. Even Saarinen concedes that for the care-circle member opening a share link on a phone while walking their dog, a crafted icon of the doctor doing the talking IS the right affordance. Icons travel where typography doesn't.

### Round 5 — the remaining fault lines

Two tensions do not resolve in the room:

**Tension A — object vs. canvas.** Ive and Yuan are still at opposite poles. Ive believes the patient experiences one thing at a time. Yuan believes the assistant's value is composing multiple threads. The room does not converge. It concludes that the answer depends on *which surface*: the primary home surface is singular (Ive), the power-user surface is composable (Yuan). This is a design decision to be made, not a consensus.

**Tension B — solemnity vs. character.** Kouthoofd and Ive represent opposite instincts about how a care product should feel. The room splits roughly 50/50. Kouthoofd's instinct is correct for daily retention. Ive's instinct is correct for the peaks. A tone-switching mechanism (again, the weight token) may mediate, but the room acknowledges this is a judgment call that Ditto's brand team owns.

---

## 5. Three merge directions

These are directions the panel could collectively stand behind, not Frankensteins of everything said. Each resolves the fault lines differently. Each optimizes for a different strategic goal.

### Direction α: *The Living Paper*

**The merge**: Ive × Bierut × Headspace × a seasoning of Kare

**Core thesis**: The interface is a living personal publication. One lead story at a time. Editorial restraint. Pace and color governed by emotional weight. Typography does most of the work. Iconography handles people, places, and accessibility.

**Defining mechanics**
- Home surface: a masthead and one lead story. Everything else is below the fold.
- Emotional weight token drives pace, color saturation, whether the app opens with a breath.
- Standing sections organize the 45 JTBD as editorial departments: "The Doctor Said," "The Circle Says," "Questions Outstanding," "What's Next," "Looking Back."
- Typography-first. One serif, one sans. Iconography reserved for people (doctors, circle members, patient) and accessibility surface (Corrie mode).
- Share is a pullquote card. Adapted per recipient, beautiful enough to screenshot.
- Archive is first-class. The journey page is the back-catalogue, bound by month.

**What it's great at**: Dignity. Memory. The journey page. The keystone share. Mara's condition page as an ongoing feature story. First-time wow for patients who want their illness taken seriously.
**What it struggles with**: Caregivers under time pressure. Aysel at 11pm does not want a masthead, she wants the medication list. Needs a utility escape hatch.
**Who signs on**: Ive, Bierut, Puddicombe, Kare (for accessibility layer), Gebbia (with reservations about warmth).
**Who dissents**: Saarinen (too slow for operators), Kouthoofd (too solemn for daily), Yuan (too fixed for the 45 JTBD).
**Strategic fit**: emotional dignity. The Mara journey. The moral center of Ditto.

### Direction β: *The Home Feed*

**The merge**: Gebbia × Spalter × Kare × Kouthoofd's warmth

**Core thesis**: The interface is a feed-shaped home for the patient and their circle. Hospitality framing on entry. Story ring above, journey feed below. Rooms for depth. Iconography throughout. The circle is a first-class presence, not a share destination.

**Defining mechanics**
- Opening is a warm line, not a dashboard. The circle is visible from the first screen (avatars, status, activity).
- Story ring up top: today's summary, tomorrow's prep, new from the circle, a doctor's note. Glanceable, tappable.
- Main feed: reverse-chronological journey cards with cover imagery, pullquotes, and circle reactions.
- Rooms for depth: tap into a condition, a medication, a doctor, a circle member. Each room is a warm interior space, not a tab page.
- Shares are letters, delivered with hospitality framing to the recipient. The recipient's first view is a welcoming card, not a notification.
- Iconography: doctor portraits, medication icons, circle avatars. Every person and thing has a face.
- Circle member dashboard (wow moment #9) is the same shape as the patient's feed, scoped to what's been shared.

**What it's great at**: The care circle. Sharing. The circle-to-patient conversion (wow moment #12). First-time use. The "I want this too" instinct when Sanne sees her father's update. Aysel's adapted update for her mother.
**What it struggles with**: Power users managing many threads. Dignity in hard moments (the feed shape, even adapted, can trivialize). Operator-grade workflow.
**Who signs on**: Gebbia, Spalter, Kare, Kouthoofd, Puddicombe (for the weight-adapted cards).
**Who dissents**: Rams (too atmospheric), Saarinen (too slow), Ive (too many things at once), Bierut (no archival density).
**Strategic fit**: relational virality. The growth engine. The circle-net-invitation loop. B2B2C appeal (insurer partners see a consumer product, not a dashboard).

### Direction γ: *The Atelier*

**The merge**: Rams × Saarinen × Yuan × Ive's discipline × Kare's accessibility

**Core thesis**: A disciplined modular card system with ambient AI composition, command-palette intent navigation, and Ive-grade typographic restraint. Cards are the atomic unit. An AI layer composes them per intent. A separate pictographic surface serves cognitively constrained users.

**Defining mechanics**
- A strict card system. Every card is either content (summary, medication, chart, doctor, question, timeline) or action (share, book, record). Each card has an emotional weight property that adjusts its presentation.
- On the home surface, the AI composes the cards it thinks you need most right now. You can pin cards, dismiss them, save views.
- Intent input is always present: text, voice, or dictation. Asking "show me my meds" composes a medication board inline.
- Command palette for operators (Cmd-K): jump to any entity, any pipeline output, any saved view. On mobile, a quick-find analog.
- Entity URLs for deep linking and sharing.
- Cognitive-adaptation mode (Corrie mode) is a parallel surface: one card at a time, pictographic, voice-read-aloud, one action.
- Editorial layer (the journey page, condition page) lives inside this system as a specific card composition, not a separate app.

**What it's great at**: The 45 JTBD. Caregivers. Power users. Longitudinal depth. The "new pipeline ships as a new card type" extensibility. Pieter managing his wife's care. Jan navigating five specialists.
**What it struggles with**: First-time use without anticipation. Emotional moments without the weight system working hard. The solemn register for heavy news (cards, even beautiful cards, can feel transactional).
**Who signs on**: Rams, Saarinen, Yuan, Ive (with reservations about density), Kare (for the parallel surface).
**Who dissents**: Gebbia (no hospitality), Spalter (not shareable-native enough), Kouthoofd (too restrained), Bierut (editorial framing is secondary, not primary).
**Strategic fit**: longitudinal capability. The moat. The 45 JTBD scaled without feature bloat.

---

## 6. Recommendation

Each direction is internally coherent. Each optimizes for one strategic need at the cost of the others. Picking one means losing two.

**The real answer is that Ditto needs elements of all three, stratified by role.** Not as a compromise, but as a deliberate stratification.

| Layer | Role | Direction that wins | Why |
|---|---|---|---|
| The shell | First impression, the home surface, the hard moments | **α — Living Paper** | Sets tone. A patient opening Ditto for the first time after a hard appointment needs dignity. The editorial framing gives significance. This is the brand surface. |
| The share | The keystone wow, the circle-facing surface | **β — Home Feed** | The share is where virality lives. Hospitality framing on delivery, iconographic warmth, feed-shape for circle members. This is the growth surface. |
| The operator mode | The caregiver, the power user, the deep workflow | **γ — Atelier** | Aysel, Pieter, Jan. Command palette, dense cards, intent navigation, deep links. This is the retention surface for the high-intent segment. |
| The accessibility mode | Corrie, the granddaughter, the cross-language cohort | **Kare's picture book** (component of all three) | Pictographic, one-card-at-a-time, voice-first. The Corrie mode is a parallel surface, not an override. |

**What this means concretely for the interface work**:

1. **Build a card system as the atomic unit.** Cards are unavoidable, and γ is right about that. Every pipeline output is a card type. Card has a weight token that governs its presentation. Card has a density mode (Rams) and a presence mode (Ive/Puddicombe). Card can be shared, pinned, composed into boards.

2. **Make the home surface editorial, not dashboard.** α wins here. One lead story, standing sections below. The lead story adapts to emotional weight. The sections are editorial departments, not tabs. This is what stops it feeling like a medical admin tool.

3. **Design the share as the hero.** β wins here. Pullquote card, hospitality framing on delivery, iconographic warmth, per-recipient adaptation. This is the feature that deserves the most design craft in Ditto's entire product surface.

4. **Unlock an operator mode for the caregiver segment.** γ wins here. Command palette, saved views, deep URLs, keyboard support on web/iPad. This is a mode toggle, not a separate app. Patients who self-identify as caregivers get access; others don't see the surface complexity.

5. **Build a cognitive-adaptation mode as a first-class surface.** Kare's insistence is correct. Corrie is 15% of the long-term TAM once Ditto serves aging parents. The pictographic mode is a single-card, voice-read, high-contrast, one-action surface. It is not a settings-menu "large text" toggle. It is a rendered alternative of the same data.

6. **Implement the emotional weight system as infrastructure.** Every pipeline emits a weight. Every card renders against it. Every navigation motion is paced by it. This is the primitive that makes the whole thing work across Mara's hardest day and Aysel's busiest night. It is also what no competitor will copy, because it is architectural.

**One thing NOT to do**: don't try to invent a wholly new paradigm. The chatbot-replacement instinct is where most AI-native products fail. All ten designers agreed, in their own terms, that the primitive is the card (or the object) and the innovation is in composition, pace, and craft. The interface is not the differentiator. The interface is the vessel. The differentiator is the architecture underneath and the taste that shapes the vessel.

**Open questions before picking a lane**:

- Is the home surface editorial (α) by default, or does it adapt per user segment? Editorial-by-default is the stronger brand move.
- Does the operator mode (γ) ship at launch or after Tier 1 proves retention? Arguably after — caregivers are a cohort you earn into, not onboard into.
- How does the Corrie mode get toggled on? Self-selection feels wrong; family-member-activated is more natural.
- Does the share always use Direction β's hospitality framing, or does its framing flex per recipient-role? Probably flexes.

**Next step**: prototype the home surface under Direction α with the β share as the most prominent action and γ's command affordance as a secondary surface. Build three panels and react. The design decisions that matter most are shape-of-the-home-surface and shape-of-the-share. Everything else falls out.
