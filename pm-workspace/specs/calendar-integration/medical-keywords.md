# Medical Keyword List — Calendar Scan (PRO-386)

**Owner:** Merlijn | **Consumer:** Łukasz | **Linked:** [PRO-386](https://linear.app/ditto-care/issue/PRO-386), [PRO-335](https://linear.app/ditto-care/issue/PRO-335), [PRO-333](https://linear.app/ditto-care/issue/PRO-333), [PRO-334](https://linear.app/ditto-care/issue/PRO-334)

## What this is

A starter keyword list for the on-device fuzzy scan of users' default calendar (iOS/macOS, Outlook, Google). Used as the fallback path when Apple Intelligence on-device classification is unavailable or returns nothing. Lean and tunable.

**Total: 175 keywords across 2 locales (nl-NL: 95, en-GB: 80), 7 categories per locale.** Ships as `medical-keywords.json` next to this file, remote-configurable so we can tune post-launch.

## File structure

```
locales.{nl-NL,en-GB}.categories.{name}.keywords[]
```

Bare arrays per category, no per-keyword metadata in the JSON. All rationale, FP analysis, and matcher guidance lives in this markdown. The dev consumes `medical-keywords.json` as pure data.

## Category counts

| Category | nl-NL | en-GB |
|---|---|---|
| general_medical | 8 | 8 |
| care_settings | 8 | 8 |
| specialist_professions | 20 | 20 |
| allied_health | 6 | 6 |
| procedures_and_exams | 13 | 13 |
| hospitals | 35 | 20 |
| private_clinics | 5 | 5 |
| **Total** | **95** | **80** |

NL hospital list is broader because NL is the primary market (Menzis partnership, full user base). UK is sized to the top 20 + 5 private chains.

## Design principles

| Principle | What it means in practice |
|---|---|
| **High recall, controlled FP** | Aim for >80% recall on real medical events; tolerate some FP since users confirm before import. |
| **Tokens, not phrases** | Fuzzy matchers work best on single distinctive tokens. Hospital names use only the distinctive part (`Erasmus`, not `Erasmus MC Rotterdam`; `Marsden`, not `The Royal Marsden Hospital`). |
| **Stem, don't enumerate** | `huisarts` → covers `huisartsen`, `huisartsenpost`. `bloed` → covers `bloedprikken`, `bloedonderzoek`, `bloedafname`. `blood` (UK) → covers `blood test`, `bloods`, `bloodwork`. |
| **Avoid generic words** | `afspraak`, `consult`, `controle`, `appointment` cause more FP than signal. Excluded. |
| **Locale parity, not translation** | EN side is optimized for UK calendar conventions, not literal NL→EN translation. UK-specific terms like `consultant`, `health visitor`, `A&E`, `jab`, `NHS`, `OOH` are first-class. |

## Coverage methodology

Three concentric rings of keyword sources, in priority order:

1. **Generic medical terms** — words that essentially only appear in a medical context (NL: `huisarts`, `tandarts`, `polikliniek`, `apotheek`, `spreekuur`, `bloed`; UK: `GP`, `dentist`, `NHS`, `surgery`, `clinic`).
2. **Roles (who you're seeing)** — BIG-registered specialists for NL + FMS, GMC/RCP titles for UK. Paramedic professions on both sides.
3. **Locations (where you're going)** —
   - **NL:** 35 hospitals (7 UMCs + 27 largest regional/general incl. Prinses Máxima for pediatric oncology) + 5 private clinic chains (Bergman, DC Klinieken, Equipe, Annatommie, Mauritskliniek).
   - **UK:** 20 hospitals (London teaching hospitals + specialty hospitals Marsden/Christie/GOSH/Moorfields/Papworth/Brompton + major regional Oxford/Cambridge/Manchester/Birmingham/Bristol) + 5 private chains (Bupa, Spire, Nuffield, Circle Health, HCA).

Layered on top: **procedures and exams** (MRI, echo/ultrasound, CT, röntgen/X-ray, chemo, bestraling/radiotherapy, bevalling/antenatal).

## Why these UK hospitals

Selection optimized for distinctive single-token matching + recognition in patient calendars:

- **System marker:** NHS (catches "NHS appointment", "NHS letter").
- **London teaching hospitals:** St Thomas, Guys, Kings College, UCLH, Royal Free, Royal London, Hammersmith, Chelsea Westminster.
- **Specialty hospitals (highest signal for diagnosis cohort):** Royal Marsden (adult oncology), Christie (Manchester oncology), Great Ormond Street (paediatric), Moorfields (eye), Papworth (heart/lung), Royal Brompton (heart/lung).
- **Major regional teaching hospitals:** Addenbrooke (Cambridge), John Radcliffe (Oxford), QEHB (Birmingham), Bristol Royal, Manchester Royal.

## Why these UK private clinics

Top 5 by size and recognition in patient calendars:

1. **Bupa** — household name (also major insurer; users write "Bupa appointment").
2. **Spire Healthcare** — 38 hospitals, largest standalone private chain.
3. **Nuffield Health** — 31 hospitals + recognised brand (charity model).
4. **Circle Health Group** — 50+ facilities post-BMI merger.
5. **HCA Healthcare UK** — London-focused premium chain (Wellington, Princess Grace, Harley Street).

## What changed from v0.2 → v0.3

- **Bilingual structure.** Split into `locales.nl-NL` and `locales.en-GB`. Old `english_fallback` category dropped; full EN parity now lives in the en-GB locale.
- **+ 20 UK hospitals** (NHS + London teaching + specialty + major regional).
- **+ 5 UK private clinics** (Bupa, Spire, Nuffield, Circle Health, HCA).
- **+ 60 EN keywords across the 6 non-hospital categories** to mirror NL coverage.
- **JSON stripped of metadata.** Removed `fp_risk`, `description`, `fp_flagged`, `excluded_considered`, `matcher`, `tuning_recommendations`. The dev gets pure data; this markdown carries all rationale and guidance.

## Excluded set (rationale only — not in JSON)

Considered but excluded due to high false-positive rate in personal calendars. Documented here so they aren't re-added without reason:

| Term | Locale | Why excluded |
|---|---|---|
| afspraak / appointment / appt | both | Generic — used for any appointment. |
| consult | both | Overlaps with business consulting. |
| controle / check / check-up | both | Vehicle/tax/security checks. |
| behandeling / treatment | both | Used for any treatment (hair, spa). |
| onderzoek / research / investigation | both | Generic. |
| intake / referral | both | HR/admin overlap. |
| recept / recipe | both | Cooking recipes. |
| Dr. | both | Personal title noise (Dr. Janssen / Dr. Smith). |
| arts (alone) | NL | Substring FP (start, darts, parts). Compounded forms only. |
| MC (alone) | NL | Too short. Always require full 'Erasmus MC' form. |
| prik (alone) | NL | FP (prikbord, prikkel). Keep `prikpost` + `bloed`. |
| op (alone) | UK | Too short. Use `operation`. |
| labour / delivery | UK | Generic words; covered by `midwife` + `antenatal`. |

## FP-watch list (kept but to monitor in PRO-334 experiment)

These passed the inclusion bar but carry medium FP risk — first candidates to drop or down-weight if confirmation rate is poor:

- **nl-NL:** `scan`, `echo`, `CT`, `Bergman` (personal name), `Equipe` (French noun "team")
- **en-GB:** `surgery` (overlaps with operation context AND GP office), `clinic`, `consultant`, `Circle Health` ("circle" overlap), `HCA` (also Healthcare Compliance Association)

## Matcher recommendations to Łukasz

Not in the JSON — implement in code:

- **Case-insensitive, diacritics-normalized** (`röntgen` ↔ `rontgen`, `diëtist` ↔ `dietist`, `Máxima` ↔ `Maxima`, `Addenbrooke's` ↔ `Addenbrooke`).
- **Edit distance 1** for typos and inflections; allow 2 for stems >10 chars.
- **Prefix-aware matching** so `huisarts` catches `huisartsenpost`, `bloed` catches the whole bloed* family, `blood` catches `bloods`/`bloodwork`.
- **Punctuation-stripping tokenizer.** Treat `A&E`, `X-ray`, `walk-in`, `out-of-hours` as either single tokens or canonical multi-token sequences depending on your tokenizer choice — but make sure they don't get lost on the `&`, `-`, or `'`.
- **Multi-token entries** (`Amsterdam UMC`, `Jeroen Bosch`, `Albert Schweitzer`, `DC Klinieken`, `Prinses Maxima`, `Maxima MC`, `Royal Free`, `Great Ormond Street`, `John Radcliffe`, `St Thomas`, `Circle Health`, `health visitor`, `urgent care`, `mental health`, `walk-in`, `out-of-hours`, `Chelsea Westminster`, `occupational therapist`, `speech therapist`, `Kings College`, `Manchester Royal`, `Bristol Royal`, `Royal London`, `Royal Brompton`, `Royal Marsden`) should match if all tokens appear in the event within a small window.
- **Locale selection** should follow the user's device language / calendar default. Running both locales simultaneously is fine for bilingual users — minor extra cost, broader recall.

## Coverage by Life Moment

| Segment | Covered by (NL) | Covered by (UK) |
|---|---|---|
| Serious diagnosis / chronic | oncoloog, chemo, bestraling, biopsie, bloed, Antoni van Leeuwenhoek, Prinses Maxima, all UMCs | oncologist, chemo, radiotherapy, biopsy, blood, Royal Marsden, Christie, Great Ormond Street |
| Expecting / young parents | verloskundige, gynaecoloog, echo, bevalling, consultatiebureau, kinderarts | midwife, gynaecologist, ultrasound, antenatal, health visitor, paediatrician |
| Sudden chronic | internist, cardioloog, reumatoloog, diëtist, trombosedienst, polikliniek, bloed | consultant, cardiologist, rheumatologist, dietitian, blood, clinic |
| Neurodegenerative | neuroloog, psycholoog, psychiater, ergotherapeut, logopedist | neurologist, psychologist, psychiatrist, occupational therapist, speech therapist |

## What to do after ship

The list is v0.3. Real signal comes from the experiment (PRO-334):

1. **Instrument per-keyword match counts and per-keyword user-confirmation rate.** A keyword with <20% confirmation rate is hurting more than helping — drop or down-weight. Pay special attention to the FP-watch list above.
2. **Mine the false-negative set** — events users confirmed manually but the scanner missed — for keywords to add.
3. **Re-evaluate scope by locale** after 2 weeks. If UK volume is low (NL is primary market), consider keeping en-GB enabled only for users with `en-GB` device language to reduce noise.

## Open questions for Łukasz

1. Does the matcher support per-keyword weights, or is it binary match/no-match? If binary, I can split into tiers more aggressively.
2. Word-boundary vs substring matching? Recommendation: word-boundary + prefix.
3. Are notes/location fields searched in addition to the title?
4. How is locale selected — device language, calendar account locale, both? Confirms whether running both locales simultaneously is the right default.

## Acceptance criteria status (from PRO-386)

- [ ] Final keyword list reviewed with Łukasz — **pending this hand-off**
- [x] Format suitable for shipping as remote-configurable data — JSON in this folder
- [ ] Documented next to the design hand-off (PRO-333) — link this spec from PRO-333 once reviewed
