# UK English — Translation Changes

Source: `tmp/ditto-receive-en.json`
Scope: spelling, grammar, word choice, typos. Pure language conversion. Anything tied to UK healthcare context (NHS, GP surgery vs doctor's practice, Dutch references) lives in `uk-cultural-localization.md`.

Apostrophes: the file mixes straight `'` and curly `'` (e.g. lines 388, 618, 621). Not a UK/US issue, but worth normalising in the same pass. Listed separately at the bottom.

---

## 1. `-ize / -ization` → `-ise / -isation`

| Key | Current | Suggested |
|---|---|---|
| `audio.summarize.button` | Summarize recording | Summarise recording |
| `audio.summarize.inProgress` | Summarizing... | Summarising... |
| `audio.transcription.completed.message` | Your recording has been transcribed and summarized | Your recording has been transcribed and summarised |
| `onboarding.notifications.personalize.title` | Personalize your Ditto | Personalise your Ditto |
| `onboarding.notifications.personalization.title` | Personalization | Personalisation |
| `onboarding.notifications.personalization.description` | …personalize your experience… | …personalise your experience… |
| `onboarding.notifications.trackingConsent.title` | Personalize your Ditto | Personalise your Ditto |
| `onboarding.notifications.trackingConsent.description` | …personalize the app and improve it for you. | …personalise the app and improve it for you. |
| `onboarding.intent.option.appointmentSummaries` | Summarize my medical conversations | Summarise my medical conversations |
| `ocr.info.description` | the system recognizes texts from the image | the system recognises texts from the image |
| `share.sheet.customize` | Customize what to share | Customise what to share |
| `newFeature.bullet2` | Questions are organized by your type of care | Questions are organised by your type of care |
| `activation.infographic.analysis.description` | Ditto's AI analyzes your conversation… | Ditto's AI analyses your conversation… |
| `profileSetup.firstName.subtitle` | We'll use this to personalize your Ditto experience | We'll use this to personalise your Ditto experience |
| `question.library.18` | Is there a patient organization for people with the same illness as me? | Is there a patient organisation for people with the same illness as me? |

Already correct (UK form): `loader.finalisingSummary` ("Finalising summary"), `careCircle.followers.cancelled.toast` and `error.invitationNotFound.message` ("cancelled").

---

## 2. `afterward` → `afterwards`

| Key | Current | Suggested |
|---|---|---|
| `home.meetTeam.tip1.description` | You'll get a clear summary afterward. | You'll get a clear summary afterwards. |
| `onboarding.termsAndConditions.fulltext` (item 4) | …your data is temporarily processed on secure EU servers and deleted immediately afterward. | …deleted immediately afterwards. |

Already correct: `onboarding.privacy.dataInEU` uses "afterwards".

---

## 3. `caregiver` → `carer`

In UK English, the unpaid family helper or paid social-care worker is a "carer". "Caregiver" sounds American.

| Key | Current | Suggested |
|---|---|---|
| `onboarding.profile.option.caregiver` | As a caregiver | As a carer |
| `activation.infographic.summary.item3` | Easy sharing with family and caregivers | Easy sharing with family and carers |
| `hcp.type.maternity` | Maternity Caregiver | Maternity Carer — but see cultural file: the Dutch *kraamverzorgster* role has no direct UK equivalent. |

Note: `onboarding.persona.option.caregiver` value is "I care for someone regularly" — already neutral, no change.

---

## 4. `healthcare` vs `health care` (one word in UK as a compound noun)

| Key | Current | Suggested |
|---|---|---|
| `inbox.careCircleUpdate.body` | You have received health care update! | You have received a healthcare update! *(also fixes missing article)* |
| `newFeature.card5.subtitle` | Show and receive support on health care appointment updates… | Show and receive support on healthcare appointment updates… |

`onboarding.intent.option.healthFitnessData` ("Track health and fitness data") — fine, this is "health and fitness" not a compound.

---

## 5. Compound words / hyphenation

| Key | Current | Suggested |
|---|---|---|
| `onboarding.welcome.getStarted` | That brings you smart\ncare, pocket sized | That brings you smart\ncare, pocket-sized |
| `question.category.lifestyleAdvice` | Life-style advice | Lifestyle advice |

---

## 6. Typos and grammar errors (not UK-specific, but caught in the pass)

| Key | Current | Suggested |
|---|---|---|
| `careCircle.error.cannotJoinOwn.message` | You can' invite yourself as a follower. | You can't invite yourself as a follower. |
| `appReview.description` | Give us a rating and let other know that Ditto is helpful! | Give us a rating and let others know that Ditto is helpful! |
| `scanner.firstTime.description` | …an easy-to-understand explanation of a complex medical documents. | …an easy-to-understand explanation of a complex medical document. |
| `scanner.firstTime.comingSoon.description` | Keep an eye out on the Play Store updates… | Keep an eye on Play Store updates… |
| `appointment.firstTime.notification.message` | Record the conversation with your Doctor via Ditto. | Record the conversation with your doctor via Ditto. |
| `discover.userStories.story1.title` | Most Doctors already know Ditto | Most doctors already know Ditto |
| `common.errors.network` | Something went wrong as connection was lost. Try again while keeping the app open. | Something went wrong because the connection was lost. Try again while keeping the app open. |
| `audio.network.message` | Ditto could not make a summary as connection was lost. | Ditto could not make a summary because the connection was lost. |
| `home.addEvent.title` | Doctor's appointment coming up? | Got a doctor's appointment coming up? *(missing subject; or rewrite — see cultural file)* |
| `timeline.now` / `timeline.today` | NOW, %@ | UK convention typically lowercase: "Now, %@" |

---

## 7. Brand / product name capitalisation

| Key | Current | Suggested |
|---|---|---|
| `settings.help.whatsapp` | Contact on Whatsapp | Contact on WhatsApp |
| `help.summaryNotPossible.whatsapp` | Contact via Whatsapp | Contact via WhatsApp |
| `help.summaryNotPossible.body` and `body2` | "via WhatsApp" elsewhere | already correct |
| `help.summaryNotPossible.email` | Contact via e-mail | Contact via email *(modern UK preference; "e-mail" with hyphen is dated)* |

---

## 8. Date / time formatting

UK uses day-month order and 12h with lowercase am/pm (or 24h).

| Key | Current | Suggested |
|---|---|---|
| `home.resources.card.nomination.howToVote.deadline` | Voting closes April 14 at 5:00 PM. | Voting closes 14 April at 5pm. *(content also Dutch-specific — see cultural file)* |
| `appointment.firstTime.notification.time` | 14:03 | OK in UK (24h) — keep |

---

## 9. Phone country code default

| Key | Current | Suggested |
|---|---|---|
| `userInfo.phone.help` | Include country code, e.g. +31 | Include country code, e.g. +44 |

---

## 10. Tone — preserve brand voice

✅ **Keep Ditto's positivity, freshness, and authenticity.** No tone changes in this pass. The only "tone-adjacent" item to fix is one that's actually broken English, not just upbeat:

| Key | Current | Suggested |
|---|---|---|
| `videoActivation.getStarted.title` | Start yourself with Ditto | Get started with Ditto *(broken phrasing, not a register issue)* |

"We're super happy you've downloaded our app", exclamation marks, and the cheerful onboarding voice all stay as-is.

---

## 11. Apostrophe consistency (not UK-specific, but flag in same pass)

The file mixes ASCII `'` with the typographic `'`. Examples:

- `onboarding.account.skipConfirmation.message` — "Ditto's" (curly)
- `error.audio.durationTooShort` — "can't" (curly)
- `error.validation.classificationFailed` — "didn't" (curly)
- Most other strings use straight `'`

Recommendation: normalise to one style across the file. Curly is preferable typographically; straight is safer for older renderers.

---

## 12. Items checked and correct in UK English

These read fine — no change needed:

- `hcp.type.physio` — "Physiotherapist" (UK form; US would be "Physical Therapist")
- `hcp.type.gp` — "General Practitioner"
- `loader.finalisingSummary` — already "Finalising"
- `careCircle.followers.cancelled.toast` and elsewhere — "cancelled" (double-l, UK)
- `onboarding.privacy.dataInEU` — "afterwards"
- `audio.error.speechPermission` — fine
- All instances of "colour", "favourite", "behaviour", "centre", "licence" — *none present to check*

No instances found of: `analyze` (singular), `color`, `behavior`, `favorite`, `center`, `defense`, `license`, `traveler`, `gray`, `aluminum`, `pediatric`, `tumor`, `anesthesia`, `diarrhea`, `fetus`, `estrogen`, `gotten`. The vocabulary is largely already neutral.

---

## Summary count

- **`-ize/-ization` changes**: 15 keys
- **`afterward` → `afterwards`**: 2 keys
- **`caregiver` → `carer`**: 3 keys (one overlaps with cultural file)
- **`healthcare` consolidation**: 2 keys
- **Compound/hyphen fixes**: 2 keys
- **Typos / grammar**: 9 keys
- **Brand capitalisation**: 3 keys
- **Date/phone format**: 2 keys
- **Phrasing fix (not tone)**: 1 key
- **Apostrophe normalisation**: ~10 keys (consistency sweep)

Total: **≈40 touched strings**, almost all mechanical. Brand voice preserved.
