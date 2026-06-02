# Lentekabinet Sunday Sniper

Auto-buys Sunday tickets at https://resell.seetickets.com/lentekabinet2026/category/7785/sunday-ticket the instant they appear.

## One-time setup

You need Node.js 18+. Check by running `node -v` in Terminal. If you don't have it: `brew install node` (or download from https://nodejs.org).

Then, in Terminal:

```bash
cd /Users/merlijnvanbreugel/Documents/GitHub/Ditto/claude-care-clarified/tmp/sniper-app
npm install
```

`npm install` also downloads a private Chromium build (~150 MB). One-time, takes 1–2 min.

## Running the sniper

```bash
npm start
```

This:
1. Opens its own Chromium window with a saved profile (so you only log in once, ever).
2. Loads the Sunday Ticket category page.
3. Pauses and asks you to confirm in the terminal.

In the **browser** window:
1. Log in to seetickets (only needed the first time — it persists).
2. Make sure you're on the Sunday Ticket category page.

Back in the **terminal**, press **ENTER**.

The sniper now reloads the page on a tight loop and inspects the live DOM each cycle. The browser stays usable. The terminal shows a live ticker:

- `0 advert(s), 0 available` — page is empty, polling gently (~1.5s/cycle)
- `🟡 1 in purchase, 1 total — fast-watching for release` — someone is holding a ticket. The script drops all sleep and reloads back-to-back so we grab it the instant their 10-min timer expires.

## When a ticket appears

1. The terminal prints `🎫🎫🎫 TICKETS CLICKED 🎫🎫🎫` and your terminal beeps loudly.
2. The script has already clicked **Add to cart** on every available advert (staggered 150ms apart) in the same render where it found them — no second reload.
3. **You take over**: complete checkout in the browser. The script does *not* auto-checkout.

If the script sees availability but can't click (race lost in the same millisecond), it retries instantly with no sleep.

## Tweaking

Edit the CONFIG block at the top of `sniper.js`:

- `SLEEP_IDLE_MS` — default 500. Sleep between cycles when 0 adverts are listed. Lower = faster but risks rate-limiting.
- `SLEEP_WATCH_MS` — default 0. Sleep when an "In Purchase" advert is sitting on the page. Keep at 0 for max speed.
- `CLICK_STAGGER_MS` — default 150. Delay between successive Add-to-cart clicks.

## Files

- `sniper.js` — the script
- `package.json` — Node dependencies
- `.auth-profile/` — created on first run, stores your seetickets login (do not commit, do not share)
- `node_modules/` — created by `npm install`

## Stopping

Press `Ctrl+C` in the terminal. The browser closes too. Run `npm start` again to resume — your login is remembered.

## Troubleshooting

- **"command not found: node"** — install Node.js (see One-time setup).
- **"command not found: npm"** — same fix; npm ships with Node.
- **Browser opens but stays blank** — check your internet, then `Ctrl+C` and run `npm start` again.
- **Keeps saying `HTTP 302` or login redirects** — your session expired. Log in again in the browser window, no need to restart.
- **5+ consecutive errors warning** — usually a logout. Re-login in the open browser; script will recover on its own.
