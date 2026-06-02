// Lentekabinet 2026 Sunday Ticket Sniper
// Runs a real Chromium window via Playwright, persists your seetickets login
// between runs, and reloads the Sunday category page on a tight loop. When an
// Add-to-cart advert appears, it clicks every available cart button before
// anyone else. When an "In Purchase" advert is sitting on the page, it polls
// as fast as the page reload allows so the moment the holder's timer expires
// we grab the ticket.

const { chromium } = require('playwright');
const path = require('path');
const readline = require('readline');

// ─── CONFIG ─────────────────────────────────────────────────────
const TARGET_URL       = 'https://resell.seetickets.com/lentekabinet2026/category/7785/sunday-ticket';
const SLEEP_IDLE_MS    = 500;   // sleep between cycles when 0 adverts (page is empty)
const SLEEP_WATCH_MS   = 0;     // sleep when 1+ "In Purchase" advert exists — poll flat-out
const CLICK_STAGGER_MS = 150;   // delay between successive Add-to-cart clicks
const NAV_TIMEOUT_MS   = 15000; // max time for page.goto
const IDLE_WAIT_MS     = 4000;  // max time waiting for network to settle after goto
const USER_DATA_DIR    = path.join(__dirname, '.auth-profile');
// ────────────────────────────────────────────────────────────────

const C = {
  reset: '\x1b[0m', bold: '\x1b[1m',
  red: '\x1b[31m', green: '\x1b[32m', yellow: '\x1b[33m', cyan: '\x1b[36m', gray: '\x1b[90m',
};

const ts = () => new Date().toLocaleTimeString('nl-NL');
const log = (msg) => console.log(`${C.gray}[${ts()}]${C.reset} ${msg}`);

function beep(count = 3, gapMs = 200) {
  for (let i = 0; i < count; i++) {
    setTimeout(() => process.stdout.write('\x07'), i * gapMs);
  }
}

function waitForEnter(prompt) {
  return new Promise((resolve) => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    rl.question(prompt, () => { rl.close(); resolve(); });
  });
}

// One polling cycle: reload the live page so the SPA renders the cart-btn
// divs, wait briefly for the XHR to settle, then check the live DOM. If any
// advert is "available" (cart-btn-* container without "In Purchase" badge),
// click every available cart button immediately in the same evaluate call so
// we don't pay a second navigation round-trip.
async function pollAndAct(page) {
  try {
    await page.goto(TARGET_URL, { waitUntil: 'domcontentloaded', timeout: NAV_TIMEOUT_MS });
    // The adverts list is JS-rendered after the initial HTML. Wait for the
    // network to go idle, but don't block forever if the page has no adverts
    // (no XHR will fire, or it fires fast).
    await page.waitForLoadState('networkidle', { timeout: IDLE_WAIT_MS }).catch(() => {});
  } catch (e) {
    return { error: e.message };
  }

  return page.evaluate(async (stagger) => {
    const divs = document.querySelectorAll('div[id^="cart-btn-"]');
    let available = 0;
    let inPurchase = 0;
    const availTargets = [];

    divs.forEach((div) => {
      const text = (div.innerText || div.textContent || '').toLowerCase();
      if (text.includes('in purchase')) {
        inPurchase++;
        return;
      }
      available++;
      let btn = div.querySelector('a[href], button:not([disabled]), input[type="submit"]')
             || div.querySelector('[role="button"]');
      // Last-resort click target: if the text suggests purchasing but no
      // specific button matched, click the first non-badge child.
      if (!btn && /add|cart|koop/.test(text)) {
        btn = div.querySelector('a, button, span:not(.badge), div:not(.badge)') || div;
      }
      if (btn) availTargets.push({ id: div.id, btn });
    });

    const clicked = [];
    for (let i = 0; i < availTargets.length; i++) {
      if (i > 0) await new Promise((r) => setTimeout(r, stagger));
      try { availTargets[i].btn.click(); clicked.push(availTargets[i].id); } catch (_) {}
    }

    return { total: divs.length, available, inPurchase, clicked };
  }, CLICK_STAGGER_MS);
}

function announceHit(clicked) {
  console.log(`\n\n${C.bold}${C.green}🎫🎫🎫 TICKETS CLICKED 🎫🎫🎫${C.reset}`);
  console.log(`${C.bold}${C.green}🛒 ADDED ${clicked.length} TICKET${clicked.length > 1 ? 'S' : ''} TO CART:${C.reset}`);
  clicked.forEach((id) => console.log(`   • ${id}`));
  console.log(`\n${C.bold}${C.yellow}💳 GO COMPLETE CHECKOUT IN THE BROWSER WINDOW NOW.${C.reset}\n`);
  beep(10);
  setTimeout(() => beep(10), 2500);
  setTimeout(() => beep(10), 5000);
}

async function main() {
  console.log(`${C.bold}${C.cyan}🎯 Lentekabinet 2026 Sunday Sniper${C.reset}`);
  console.log(`${C.gray}Target:${C.reset} ${TARGET_URL}`);
  console.log(`${C.gray}Login: ${C.reset} persisted at ${USER_DATA_DIR}\n`);

  const ctx = await chromium.launchPersistentContext(USER_DATA_DIR, {
    headless: false,
    viewport: { width: 1280, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });

  const page = ctx.pages()[0] || (await ctx.newPage());

  log('Opening target page…');
  await page.goto(TARGET_URL, { waitUntil: 'domcontentloaded' }).catch(() => {});

  console.log(`\n${C.bold}${C.yellow}⏸  SETUP${C.reset}`);
  console.log('   1. In the browser window: log in to seetickets if you aren\'t already.');
  console.log('   2. Confirm you\'re on the Sunday Ticket category page.');
  console.log('   3. Come back here and press ENTER to arm the sniper.\n');
  await waitForEnter('Press ENTER to start watching > ');

  log(`${C.green}Armed.${C.reset} Reloading and checking the live DOM every cycle…\n`);

  let polls = 0;
  let consecutiveErrors = 0;
  let lastInPurchaseWarn = 0;

  while (true) {
    polls++;
    const result = await pollAndAct(page);

    if (result.error) {
      consecutiveErrors++;
      process.stdout.write(`\r${C.gray}[${ts()}]${C.reset} poll #${polls}  ${C.yellow}${result.error}${C.reset}  (errors: ${consecutiveErrors})                    `);
      if (consecutiveErrors === 5) {
        console.log(`\n${C.yellow}5 consecutive errors — you may be logged out or rate-limited. Check the browser.${C.reset}`);
      }
      await new Promise((r) => setTimeout(r, 2000));
      continue;
    }
    consecutiveErrors = 0;

    if (result.clicked.length > 0) {
      announceHit(result.clicked);
      log('Sniper done. Browser stays open. Close this terminal when you\'re finished.');
      await new Promise(() => {}); // keep process alive so the browser stays
      return;
    }

    // We saw availability but couldn't click — race lost or DOM not hydrated.
    if (result.available > 0) {
      console.log(`\n${C.yellow}⚠ poll #${polls}: ${result.available} available but no clickable target found. Retrying immediately.${C.reset}`);
      continue; // no sleep, hit it again
    }

    // Build the status line. When "In Purchase" exists we surface it loudly
    // and warn once that we're now in fast-watch mode.
    let status;
    if (result.inPurchase > 0) {
      status = `${C.yellow}🟡 ${result.inPurchase} in purchase${C.reset}, ${result.total} total — ${C.bold}fast-watching for release${C.reset}`;
      if (Date.now() - lastInPurchaseWarn > 30000) {
        console.log(`\n${C.yellow}🟡 ${result.inPurchase} advert(s) currently In Purchase — switching to flat-out poll cadence. The holder's timer could expire any moment.${C.reset}`);
        lastInPurchaseWarn = Date.now();
      }
    } else {
      status = `${C.gray}${result.total} advert(s), 0 available${C.reset}`;
    }
    process.stdout.write(`\r${C.gray}[${ts()}]${C.reset} poll #${polls}  ${status}                    `);

    const sleepMs = result.inPurchase > 0 ? SLEEP_WATCH_MS : SLEEP_IDLE_MS;
    if (sleepMs > 0) await new Promise((r) => setTimeout(r, sleepMs));
  }
}

main().catch((err) => {
  console.error(`\n${C.red}${err.stack || err}${C.reset}`);
  process.exit(1);
});
