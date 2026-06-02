// ==UserScript==
// @name         Lentekabinet 2026 Sunday Ticket Sniper
// @namespace    https://resell.seetickets.com/
// @version      5.0
// @description  Background-poll the Sunday category and auto Add-to-cart the instant a ticket is listed.
// @match        https://resell.seetickets.com/lentekabinet2026/category/7785/*
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
  'use strict';

  // ─── CONFIG ──────────────────────────────────────────────────────
  const TARGET_URL        = 'https://resell.seetickets.com/lentekabinet2026/category/7785/sunday-ticket';
  const POLL_INTERVAL_MS  = 1000;   // background fetch cadence
  const CLICK_STAGGER_MS  = 150;    // delay between successive cart clicks
  const PAUSE_AFTER_HIT   = true;   // stop polling once any cart click fires
  // ─────────────────────────────────────────────────────────────────

  if (window.self !== window.top) return;

  // ─── STATE ───────────────────────────────────────────────────────
  let paused      = false;
  let polls       = 0;
  let pollTimer   = null;
  let titleTimer  = null;
  let firedHit    = false;

  // ─── OVERLAY ─────────────────────────────────────────────────────
  const ov = document.createElement('div');
  ov.id = 'sniper-ov';
  ov.innerHTML = `
    <style>
      #sniper-ov {
        position: fixed; top: 12px; right: 12px; z-index: 2147483647;
        background: #111; color: #0f0;
        font: 13px/1.55 "SF Mono","Fira Code","Menlo",monospace;
        padding: 12px 16px; border-radius: 10px;
        border: 1px solid #0f04; box-shadow: 0 6px 28px rgba(0,0,0,.55);
        min-width: 320px; max-width: 380px; user-select: none;
      }
      #sniper-ov .t { font-weight: 700; font-size: 14px; margin-bottom: 2px; }
      #sniper-ov .d { color: #888; }
      #sniper-ov .h { color: #f44; font-weight: 700; }
      #sniper-ov .w { color: #f80; }
      #sniper-ov .m { color: #0ff; font-size: 11px; margin-bottom: 6px; }
      #sniper-ov #sv-log {
        margin-top: 8px; max-height: 140px; overflow-y: auto;
        font-size: 11px; color: #6a6; border-top: 1px solid #222; padding-top: 6px;
      }
      #sniper-ov button {
        margin-top: 8px; background: #0f0; color: #111; border: 0;
        padding: 5px 12px; border-radius: 6px; font-weight: 700; cursor: pointer;
      }
      #sniper-ov button:hover { background: #5f5; }
    </style>
    <div class="t">🎯 Sunday Sniper v5</div>
    <div class="m">Polling every ${POLL_INTERVAL_MS}ms · session cookies on</div>
    <div id="sv-status">Initializing…</div>
    <div class="d">Polls: <span id="sv-n">0</span> · <span id="sv-t"></span></div>
    <div id="sv-log"></div>
    <button id="sv-btn">⏸ Pause</button>
  `;
  document.body.appendChild(ov);

  const $ = (id) => document.getElementById(id);

  function log(msg) {
    const t = new Date().toLocaleTimeString('nl-NL');
    $('sv-log').innerHTML = `<div>[${t}] ${msg}</div>` + $('sv-log').innerHTML;
    console.log('[Sniper]', msg);
  }

  function setStatus(html) { $('sv-status').innerHTML = html; }

  $('sv-btn').addEventListener('click', () => {
    paused = !paused;
    $('sv-btn').textContent = paused ? '▶ Resume' : '⏸ Pause';
    if (paused) {
      clearTimeout(pollTimer);
      setStatus('<span class="w">Paused</span>');
    } else {
      firedHit = false;
      setStatus('Resuming…');
      schedulePoll(0);
    }
  });

  setInterval(() => { $('sv-t').textContent = new Date().toLocaleTimeString('nl-NL'); }, 1000);

  // ─── ALERTS ──────────────────────────────────────────────────────
  function playAlarm() {
    try {
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      for (let i = 0; i < 14; i++) {
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.connect(g); g.connect(ctx.destination);
        o.type = 'square';
        o.frequency.value = i % 2 === 0 ? 880 : 1200;
        g.gain.value = 0.3;
        o.start(ctx.currentTime + i * 0.15);
        o.stop(ctx.currentTime + i * 0.15 + 0.1);
      }
    } catch (_) { /* autoplay may be blocked until user interacts */ }
  }

  function flashTitle(msg) {
    if (titleTimer) return;
    const orig = document.title;
    let on = true;
    titleTimer = setInterval(() => {
      document.title = on ? msg : orig;
      on = !on;
    }, 400);
  }

  // ─── CORE: find available cart buttons in any DOM root ──────────
  // An advert is "available" if its cart-btn-* container does NOT
  // contain "in purchase" text. Each container holds either a clickable
  // (a / button / input) when buyable, or a badge when locked.
  function findAvailableCartContainers(root) {
    const containers = root.querySelectorAll('div[id^="cart-btn-"]');
    const available = [];
    containers.forEach((div) => {
      const text = (div.innerText || div.textContent || '').toLowerCase();
      if (text.includes('in purchase')) return;
      available.push(div);
    });
    return available;
  }

  function clickableInContainer(div) {
    // Prefer real interactive elements
    const direct = div.querySelector('a[href], button:not([disabled]), input[type="submit"]');
    if (direct) return direct;
    // Form fallback
    const form = div.querySelector('form');
    if (form) return form.querySelector('button, input[type="submit"], a') || form;
    // Last resort
    return div.querySelector('[role="button"]') || null;
  }

  // ─── ON-PAGE MODE: live DOM, click everything available ─────────
  function scanLiveDom() {
    const available = findAvailableCartContainers(document);
    if (available.length === 0) {
      log(`Live scan: 0 available adverts`);
      return false;
    }

    const targets = available
      .map((d) => ({ id: d.id, el: clickableInContainer(d) }))
      .filter((x) => x.el);

    if (targets.length === 0) {
      log(`Live scan: ${available.length} available but no clickable found — DOM may still be hydrating`);
      return false;
    }

    firedHit = true;
    setStatus(`<span class="h">🛒 ADDING ${targets.length} TICKET${targets.length > 1 ? 'S' : ''} TO CART!</span>`);
    playAlarm();
    flashTitle('🎫 TICKET!');
    log(`HIT: ${targets.length} cartable advert(s) — clicking with ${CLICK_STAGGER_MS}ms stagger`);

    targets.forEach((tgt, i) => {
      setTimeout(() => {
        log(`Click ${i + 1}/${targets.length}: ${tgt.id}`);
        try { tgt.el.click(); } catch (e) { log(`Click failed: ${e.message}`); }
      }, i * CLICK_STAGGER_MS);
    });

    if (PAUSE_AFTER_HIT) {
      paused = true;
      $('sv-btn').textContent = '▶ Resume';
      clearTimeout(pollTimer);
      // Re-alarm a couple times in case user is in another tab
      setTimeout(playAlarm, 2500);
      setTimeout(playAlarm, 5000);
    }
    return true;
  }

  // ─── POLLING MODE: background fetch, reload on detection ────────
  async function pollOnce() {
    polls++;
    $('sv-n').textContent = polls;

    try {
      const res = await fetch(TARGET_URL, {
        credentials: 'same-origin',
        cache: 'no-store',
        headers: { 'Accept': 'text/html' },
      });

      if (!res.ok) {
        log(`Poll HTTP ${res.status} — backing off this cycle`);
        setStatus(`<span class="w">HTTP ${res.status}</span>`);
        return;
      }

      const html = await res.text();
      const doc  = new DOMParser().parseFromString(html, 'text/html');
      const available = findAvailableCartContainers(doc);

      if (available.length > 0) {
        log(`POLL HIT: ${available.length} available advert(s) in fetched HTML — reloading`);
        setStatus(`<span class="h">🎫 ${available.length} AVAILABLE — RELOADING</span>`);
        playAlarm();
        flashTitle('🎫 RELOADING!');
        clearTimeout(pollTimer);
        // Tiny delay so the alarm starts before reload kills this context
        setTimeout(() => window.location.reload(), 50);
        return;
      }

      setStatus('No tickets. Watching…');
    } catch (e) {
      log(`Poll error: ${e.message}`);
      setStatus(`<span class="w">Fetch error — retrying</span>`);
    }
  }

  function schedulePoll(delay = POLL_INTERVAL_MS) {
    if (paused) return;
    pollTimer = setTimeout(async () => {
      if (paused) return;
      await pollOnce();
      if (!paused && !firedHit) schedulePoll(POLL_INTERVAL_MS);
    }, delay);
  }

  // ─── BOOT ────────────────────────────────────────────────────────
  // 1) Live-DOM scan first — if the page already shows availability on load, click now.
  const hitOnLoad = scanLiveDom();

  if (!hitOnLoad) {
    setStatus('Watching for Sunday tickets…');
    log('Boot complete — entering polling mode');
    schedulePoll(0);
  }

  // 2) Also re-scan the live DOM whenever it mutates (handles SPA navigations / partial updates
  //    where the page itself injects an Add-to-cart without a full reload).
  const mo = new MutationObserver(() => {
    if (paused || firedHit) return;
    // Only scan when a cart-btn-* container is involved, to avoid wasted work.
    if (document.querySelector('div[id^="cart-btn-"]')) scanLiveDom();
  });
  mo.observe(document.body, { childList: true, subtree: true });

})();
