# Feature Scope Explorer

An interactive, editable strategy tool that maps Ditto's **three product directions** against the full **feature set**, grounded in the market deep-dive. Click any feature for a pop-up with market evidence (players, sizes, retention, reimbursement, regulatory exposure, who-pays, takeaway). Click any relevance cell to change how essential a feature is for each direction. State saves in your browser; Export writes it back to JSON/Markdown.

**Live artifact:** https://claude.ai/code/artifact/912d2230-ea19-4656-8e34-4e17f2947fdd

## The three directions
1. **Intelligent care companion** — SPINE (Care Companion → Trusted Health Assistant, fuelled by the record)
2. **Social care platform** — LEAN (Care Coordination + Social Care Platform)
3. **EU healthcare navigation platform** — INTEGRATE (the Front Door, on the data layer)

## Files
| File | What it is |
|---|---|
| `data/features.json` | **Source of truth.** 49 features (34 from the vision doc + 15 `proposed` additions from the research), 3 directions, 4 therapy areas, competitor watch — all with market evidence and a `distinction` note where features overlap. Edit this. |
| `index.template.html` | The app (HTML/CSS/JS) with a `__DITTO_DATA__` placeholder. Edit for behaviour/design. |
| `index.html` | **Generated.** Self-contained build = template + data. Don't hand-edit; it's overwritten. |
| `build.py` | Injects `features.json` into the template → `index.html`. |
| `data/raw-evidence-*.md` | Raw extraction from briefs F1–F8 (the material behind the evidence cards). |

## How to iterate
1. Edit `data/features.json` (change relevance, add a feature, refine evidence).
2. Run `python3 build.py`.
3. Re-publish `index.html` as an artifact (redeploys to the same URL).

A feature record:
```json
{
  "id": "kebab-id", "name": "...", "category": "Understanding|Intelligence|Sharing|Management|Integrations",
  "why": "one line", "proposed": true,
  "relevance": { "companion": "essential|adjacent|nice|none", "social": "...", "navigation": "..." },
  "evidence": {
    "desc": "...", "players": [{ "name": "...", "metric": "...", "role": "core|sideline", "url": "" }],
    "popularity": { "level": "high|medium|low", "note": "..." },
    "retention": { "level": "strong|engineered|weak|episodic|na", "note": "..." },
    "reimbursed": { "level": "yes|conditional|no|na", "note": "..." },
    "regulatory": { "level": "none|ce-exempt|class-iia-risk|is-regulation", "note": "..." },
    "whoPays": "...", "takeaway": "..."
  }
}
```

## Source
- `../long-term-product-vision/Ditto - Product Vision Ponderings (2).pdf` (pp.5–7 feature table, pp.17–18 therapy areas)
- `../market-deep-dive/` briefs F1–F8 + synthesis 15–18

## Labels
Relevance labels are **Core** (essential), **Extra** (adjacent), **Nice to have** (nice), **Out of scope** (none). The JSON keys stay `essential / adjacent / nice / none`; only the display labels changed.

## The 15 `proposed` features added from the research
First wave: Alert-to-responder loop · Care-circle acknowledgement loop · Human / care-circle in the loop · Trial / care-pathway matching · Anonymous mode.
Second wave: Live translation (non-native + cross-border) · Care timeline / journey view · Side-effect & symptom self-management · Mental & emotional support · Nutrition & lifestyle during treatment · Post-visit action plan / checklist · Cost & insurance navigation (navigation-side) · Provider / clinician dashboard (navigation-side, the B2B view) · Practical-life & financial support · Advance care planning / wishes.
