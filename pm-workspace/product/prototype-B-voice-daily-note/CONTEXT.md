# Voice Daily Note — Context

Domain language for ditto's voice "daily note" (Prototype B): a patient taps once and talks; the app streams the transcript and surfaces structured facts ("pills"), then saves a calm summary. This glossary is the source of truth for terminology in the spec and the SwiftUI prototype.

## Language

**Entry**:
One completed voice note — a single tap-to-start → tap-to-stop session and everything it produced (transcript, pills, timestamp).
_Avoid_: session, recording, journal entry. (User-facing word is "note" / "your day".)

**Ramble**:
The act of talking during an Entry — unstructured, tolerant of pauses, trailing off, and stretches with no extractable facts.
_Avoid_: dictation, conversation. (It is not a dialogue; ditto never talks back.)

**Pill**:
A single structured fact extracted from the Ramble, shown as a compact icon-first chip. Carries a category, a value, a source quote, an optional time, and a confidence.
_Avoid_: tag, entity, card. (A "card" is a larger UI container; a pill is the chip.)

**Pill category** (fixed v0 taxonomy):
Medication · Symptom · Mood · Treatment · Side effect · Concern · Question for doctor.

**Mood (pill)**:
A feeling the patient **states in words** ("I feel worried"). It is NOT inferred from voice tone/affect — ditto deliberately does no paralinguistic affect detection.
_Avoid_: affect, sentiment, emotion-detection.

**Source quote**:
The verbatim transcript span a Pill was extracted from, revealed when a Pill is expanded. The provenance that makes a Pill trustworthy.
_Avoid_: citation, evidence.

**Crisis signal**:
A high-urgency output (self-harm, severe danger, possible medical emergency) surfaced from the same fact-extraction pass — not a separate model in the prototype. Shows as a calm highlighted card below the recording orb (Ditto green), overriding the centre content.
_Avoid_: alert, alarm. (Tone is calm, never alarming.)

**Look-back**:
A short read across the previous 7 days, surfaced after saving, from the 2nd Entry onward.
_Avoid_: trends, analytics, insights.

**Timeline**:
The accruing list of past Entries the patient can revisit.
_Avoid_: history, feed, log.

## Relationships

- An **Entry** contains one **Ramble** and produces zero or more **Pills**.
- A **Pill** belongs to exactly one **category** and carries one **source quote**.
- A **Crisis signal** is a special high-urgency output that overrides the centre UI; in the prototype it comes from the extraction pass, not a separate detector.
- The **Look-back** reads across recent **Entries**; the **Timeline** lists them.

## Example dialogue

> **Dev:** "If the patient says 'I'm a bit worried about my scan tomorrow,' is that a Mood pill or a Concern pill?"
> **PM:** "Concern — it's about an upcoming event. Mood is how they feel in themselves ('I feel down today'). And neither is inferred from tone — only from the words."

## Flagged ambiguities

- "Mood" was ambiguous between *stated feeling* and *inferred affect from voice* — **resolved:** Mood is always content-extracted from words; affect inference is out of scope.
- "Note" (user-facing) vs "Entry" (internal) — same thing; use **Entry** in code/domain, "your day / note" in UI copy.
