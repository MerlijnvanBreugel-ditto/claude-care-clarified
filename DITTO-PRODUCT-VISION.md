# Ditto: From "Useful" to "Magic" — Product Vision

> **The One-Liner**: Ditto gives care relationships a memory, a voice, and a future.

## The Core Diagnosis

Conversation summary is strong but not defensible. A summary is a **commodity**. OpenAI can ship one. Google can ship one. Every EHR vendor will bolt one on. If the moat is "we summarize conversations well," we're in a features race with infinite-resource competitors.

The question isn't "how do we make the summary better." It's **"what product could only exist if you had every conversation?"**

---

## Seven Founder Perspectives

### 1. Jobs to Be Done (Tobi Lütke lens)

Nobody wants a conversation summary. The real jobs:

- **Before session**: "Help me walk in and make this person feel like they're my only client" (presence, not preparation)
- **During session**: "Let me be fully here because nothing will slip through the cracks" (permission to be human)
- **After session**: "Don't make me do 20 minutes of documentation for a 50-minute session" (time liberation)
- **Patient/client**: "I want to feel like someone actually remembers me" (being known)

**Contrarian take**: Stop building for the practitioner's workflow. Build for the **relationship itself** as the primary entity.

### 2. Network Effects (Brian Chesky lens)

A summary tool is single-player. Zero network effects. Zero switching cost.

Every conversation Ditto processes makes the *next* conversation more valuable. After 6 months, Ditto knows:
- Linguistic patterns around specific emotional states
- Which interventions were tried and response trajectories
- Topics circled around but never addressed directly
- How relationships with specific people have evolved

This is **emergent intelligence** from longitudinal observation. A practitioner switching away from Ditto is voluntarily giving themselves amnesia.

### 3. Invert Everything (Patrick Collison lens)

Everyone in AI-for-care builds tools **for practitioners.** What if the most magical thing is serving the person receiving care?

After a session, the client gets a gentle "reflection" — a mirror of their own words:

> *"Today you talked about feeling stuck at work but realized the feeling might be connected to what happened with your dad last year. You said 'I think I'm afraid of succeeding because then I can't blame anyone else.' You committed to journaling about that this week."*

**No product does this.** The patient feels heard at a level that isn't humanly possible. Now you're embedded in BOTH sides of the relationship. Neither side wants to leave.

### 4. Time Machine (Stewart Butterfield lens)

Summaries are backward-looking. Magic collapses time in both directions.

**Backward (queryable relationship memory):**
- "What did Sarah say about sleep in the last 3 months?"
- "When did Marcus first mention his brother?"
- "Show me how Elena's language about work has changed since January"

**Forward (predictive care intelligence):**
- "Sarah's language patterns match a pattern — in 3 of 4 similar cases, the client was about to disclose something significant."
- "Marcus hasn't mentioned the coping strategy from 3 weeks ago."
- "Elena's anxiety has plateaued for 4 sessions. Similar cases respond well to a modality shift."

### 5. Behavioral Loops (Nir Eyal lens)

Current flow: Conversation -> Summary -> (maybe) Read it -> Next session. Dead-end.

**The magical loop:**

```
BEFORE: Ditto primes you (30-second pre-session brief)
     |
DURING: You're fully present (Ditto handles cognitive load)
     |
AFTER: Ditto shows the delta (what changed, not what happened)
     |
BETWEEN: Client engages with their own reflection
     |
BEFORE: Ditto is smarter for next session (variable reward)
```

The variable reward — each pre-session brief surfaces something you didn't consciously know — creates the habit loop.

### 6. Wedge to Platform (Parker Conrad lens)

| Phase | What Ditto Is | Moat |
|-------|--------------|------|
| Now | Conversation summary | None (commodity) |
| +6mo | Longitudinal relationship memory | Data gravity |
| +12mo | Pre-session intelligence + between-session engagement | Behavioral lock-in |
| +18mo | Practice-wide pattern recognition | "Your practice is 23% more effective on anxiety since Ditto" |
| +24mo | Cross-practice anonymized insights | Network effects |
| +36mo | The quality layer for care | Standard of care |

Endgame: **Ditto is to care relationships what Salesforce is to sales relationships** — except it actually makes the relationship *better*.

### 7. What's the Artifact? (Jony Ive lens)

Summaries are ephemeral. What if Ditto created an artifact with lasting value?

**The Relationship Map**: A visual, living document that evolves over time:
- **Themes** (sized by frequency and emotional weight)
- **Trajectories** (is anxiety trending up or down?)
- **Turning points** (sessions where something fundamentally shifted)
- **Unexplored territory** (mentioned but never addressed)
- **The client's own model** (how they describe their world, in their words)

10 seconds with this map > 50 pages of session notes.

---

## The Magical Experience, Moment by Moment

### 1. The 30-Second Pre-Session Brief

Not a summary. A **strategic brief:**

> *"Session #14 with Sarah. Last session she opened up about her father for the first time — breakthrough after 3 sessions of circling the topic. Anxiety scores down 20% since body scan exercise (6 weeks ago) but she hasn't mentioned it in 2 sessions. She committed to talking to her manager — ask how it went. Watch for: language about work shifting from 'frustrated' to 'resigned' over 4 sessions."*

30 seconds to read. 20 minutes to reconstruct from notes. The practitioner walks in **feeling like a genius.**

### 2. Invisible During Session

Ditto doesn't show up during the conversation. Its presence is felt in its absence — no scribbling notes, no trying to remember follow-ups, no worrying about documentation. **100% present.**

### 3. The Delta, Not the Summary

After the session, Ditto shows the **diff:**

> **NEW**: Sarah disclosed childhood emotional neglect for the first time.
> **SHIFT**: Language about work moved from 'resigned' to 'angry' — first time anger appeared in 14 sessions.
> **PROGRESS**: Followed through on manager conversation — positive outcome.
> **DROPPED**: Body scan exercise not mentioned (3 sessions now).
> **CONTRADICTION**: Said she's 'doing great' but described 3 panic attacks this week.

Plus: auto-populated clinical documentation, ready for EHR.

### 4. The Client Mirror

The client gets their own experience between sessions:

> *"Here's what you explored today, in your own words..."*
> *"You committed to: [specific actions]"*
> *"Something to sit with: [a reflection]"*

Client engagement between sessions increases. They come to the next session more prepared, more self-aware, more invested.

### 5. The Relationship Map

Over months, a living visualization emerges — themes, trajectories, turning points, blind spots. A **third intelligence** born from the relationship itself.

---

## The Moat Stack

| Layer | Moat Type | Why competitors can't copy |
|-------|-----------|---------------------------|
| Longitudinal data | Data gravity | Every conversation makes switching more costly |
| Behavioral loops | Habit | Practitioners can't imagine working without the pre-brief |
| Both-sided value | Network | Both practitioner and client are embedded |
| Relationship intelligence | Compounding | 6 months of Ditto > any competitor's day-one |
| Practice-wide patterns | Learning | Your data trains your models, not theirs |

---

## Priority Stack: What to Build Next

### P0: Pre-Session Briefs
The "magic moment." If someone uses this once before a session, they never go back. This changes the value prop from "useful" to "I can't practice without this."

### P1: Conversation Deltas (not summaries)
Show what changed, not what happened. Paradigm shift from documentation tool to intelligence tool.

### P2: Client-Facing Reflections
The moat. Both sides of the relationship use Ditto = un-displaceable. Also the word-of-mouth engine: clients tell other practitioners.

### P3: Relationship Map / Longitudinal View
The "aha" at 3-6 months. Practitioner sees a pattern they never would have seen. Ditto becomes indispensable.

### P4: Practice-Wide Intelligence
The platform play. "Across your 40 clients, here's what's working and what isn't." Worth 10x whatever you charge.

---

## The Litmus Test

Before shipping any feature, ask: **"Would a practitioner describe this to a colleague at a dinner party?"**

- "It summarizes my sessions" — Nobody talks about this at dinner.
- "It told me something about my client I'd missed for 3 months, and it changed the entire trajectory of their care" — That's a dinner party story. **That's magic.**
