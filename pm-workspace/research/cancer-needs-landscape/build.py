#!/usr/bin/env python3
"""Generate players.csv and the self-contained Ditto-branded HTML explorer
from players.json (the single source of truth) + the needs-landscape markdown.

Run:  python3 build.py
Outputs (same folder):
  - players.csv                         (structured data for AI agents / spreadsheets)
  - cancer-market-explorer.html         (self-contained two-tab interactive tool)
"""
import csv, json, re, os

HERE = os.path.dirname(os.path.abspath(__file__))
PLAYERS = os.path.join(HERE, "players.json")
NEEDS_MD = os.path.join(HERE, "cancer-patient-needs-and-solution-landscape.md")
CSV_OUT = os.path.join(HERE, "players.csv")
HTML_OUT = os.path.join(HERE, "cancer-market-explorer.html")

COLUMNS = ["name","segment","category","hq","markets","what","features","needs",
           "mechanism","differentiation","users","revenue","funding","retention",
           "business_model","verdict","status","ditto_flag","source_tier","source_url","notes"]

NEED_LABELS = {
 1:"Understanding the diagnosis", 2:"Trustworthy answers",
 3:"Appointment prep & decisions", 4:"Symptom self-management",
 5:"Medication management", 6:"Coordination & overview (PHR)",
 7:"Caregiver access & proxy", 8:"Updating loved ones",
 9:"Emotional & existential", 10:"Peer community",
 11:"Lifestyle adaptation", 12:"Logistics & admin",
 13:"Financial, work & insurance", 14:"Survivorship & end-of-life"
}

EU = ["EU","Europe","Netherlands","NL","Germany","France","United Kingdom","UK","Finland",
      "Sweden","Spain","Poland","Denmark","Switzerland","Portugal","Slovakia","Belgium","Italy"]
US = ["United States","US"]
ASIA = ["China","Japan","Korea","India","Indonesia","Singapore","Malaysia","UAE","Asia"]

def regions(rec):
    blob = (rec.get("hq","") + " " + rec.get("markets","")).lower()
    out = []
    if any(k.lower() in blob for k in EU): out.append("EU")
    if any(re.search(r"\b"+re.escape(k.lower())+r"\b", blob) for k in US): out.append("US")
    if any(k.lower() in blob for k in ASIA): out.append("Asia")
    if "global" in blob: out.append("Global")
    return sorted(set(out)) or ["Other"]

def aliases(name):
    """Distinctive prose aliases to make player names clickable in Tab 1."""
    stop = {"zero","cake","levels","balance","hero","forward","inspire","notion","hinge",
            "tinder","strava","ash","tia","clue","calm","cleo","monzo","noom","yuka","flo",
            "dario","lark","zoe","docus","ebb","stoic","daylio","consensus","gemini","claude"}
    cands = set()
    n = name.strip()
    cands.add(n)
    cands.add(re.sub(r"\s*\([^)]*\)", "", n).strip())          # drop parenthetical
    cands.add(n.split(" / ")[0].strip())                        # before " / "
    cands.add(n.split(" (")[0].strip())                         # before " ("
    cands.add(re.sub(r"\s+(Health|Care|Therapeutics)$", "", n).strip())
    out = set()
    for a in cands:
        if len(a) < 4: continue
        if a.lower() in stop: continue
        out.add(a)
    return out

def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s.lower())).strip()

def main():
    data = json.load(open(PLAYERS, encoding="utf-8"))
    # normalise: ensure all columns exist
    for r in data:
        for c in COLUMNS:
            r.setdefault(c, "" if c != "needs" else [])
        r["_regions"] = regions(r)

    # ---- CSV ----
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(COLUMNS + ["regions"])
        for r in data:
            row = []
            for c in COLUMNS:
                v = r[c]
                if c == "needs": v = ";".join(str(x) for x in v)
                row.append(v)
            row.append(";".join(r["_regions"]))
            w.writerow(row)

    # ---- alias map (alias -> index) ----
    alias_map = {}
    for i, r in enumerate(data):
        for a in aliases(r["name"]):
            alias_map[norm(a)] = i
    # explicit helpful aliases
    for nm, idx in list(alias_map.items()):
        pass
    extra = {"ditto care circle":"Ditto Care", "ditto":"Ditto Care", "kin":"Kin Health",
             "chatgpt":"ChatGPT / ChatGPT Health", "chatgpt health":"ChatGPT / ChatGPT Health",
             "mijian":"MiJian (觅健)", "welby":"Welby (MyKarte ONC)", "kakao pasta":"Kakao Healthcare (PASTA)",
             "ping an":"Ping An Health", "thuisarts nl":"Thuisarts.nl"}
    name_to_idx = {r["name"]: i for i, r in enumerate(data)}
    for a, target in extra.items():
        if target in name_to_idx:
            alias_map[a] = name_to_idx[target]

    needs_md = open(NEEDS_MD, encoding="utf-8").read()

    tpl = TEMPLATE
    tpl = tpl.replace("/*PLAYERS_JSON*/", json.dumps(data, ensure_ascii=False))
    tpl = tpl.replace("/*ALIAS_MAP*/", json.dumps(alias_map, ensure_ascii=False))
    tpl = tpl.replace("/*NEED_LABELS*/", json.dumps(NEED_LABELS, ensure_ascii=False))
    tpl = tpl.replace("__COUNT__", str(len(data)))
    tpl = tpl.replace("<!--NEEDS_MD-->", needs_md)
    open(HTML_OUT, "w", encoding="utf-8").write(tpl)

    print("Wrote", CSV_OUT, "(", len(data), "rows )")
    print("Wrote", HTML_OUT)

TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ditto — Cancer Needs & Market Explorer</title>
<style>
:root{
  --navy:#0d164f; --navy-soft:#1a2570; --blue:#58b6d2; --blue-lt:#7dd4e8; --blue-bg:#eef7fa;
  --mint:#e0fbd5; --green:#2e8b57; --green-bg:#e0fbd5; --amber:#d4a832; --amber-bg:#fbf6ea;
  --coral:#d94f4f; --coral-bg:#fbeaea; --purple:#beaef8; --paper:#f8f7f4; --card:#ffffff;
  --ink:#16203f; --muted:#7c8297; --line:#e6e8ef;
}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:var(--paper);color:var(--ink);line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:#1f6f8b}
header{background:var(--navy);color:#fff;padding:18px 28px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.logo{font-weight:800;font-size:1.4rem;letter-spacing:-.02em;display:flex;align-items:center;gap:8px}
.logo .dot{width:11px;height:11px;border-radius:50%;background:var(--blue-lt);display:inline-block}
.logo small{display:block;font-weight:500;font-size:.62rem;letter-spacing:.18em;text-transform:uppercase;color:var(--blue-lt);margin-top:-2px}
.htitle{font-size:.95rem;color:#c7cbe0;font-weight:500;margin-left:auto}
.tabs{display:flex;gap:4px;background:var(--navy-soft);padding:0 28px}
.tab{appearance:none;border:0;background:transparent;color:#b9bedf;padding:14px 20px;font-size:.95rem;font-weight:600;
  cursor:pointer;border-bottom:3px solid transparent;font-family:inherit}
.tab:hover{color:#fff}
.tab.active{color:#fff;border-bottom-color:var(--blue-lt)}
.wrap{max-width:1180px;margin:0 auto;padding:26px 28px 80px}
.view{display:none}.view.active{display:block}

/* ---- Tab 1 needs render ---- */
#needs h1{font-size:1.8rem;letter-spacing:-.02em;margin:.2em 0 .3em}
#needs h2{font-size:1.35rem;letter-spacing:-.01em;margin:1.6em 0 .5em;padding-top:1.2em;border-top:1px solid var(--line);color:var(--navy)}
#needs h2:first-of-type{border-top:0}
#needs h3{font-size:1.02rem;color:var(--navy-soft);margin:1.1em 0 .3em}
#needs p{margin:.55em 0;color:#27314f}
#needs ul{margin:.4em 0 .8em;padding-left:1.2em}#needs li{margin:.28em 0}
#needs blockquote{margin:.7em 0;padding:.5em .9em;border-left:3px solid var(--blue);background:var(--blue-bg);
  color:#33405e;border-radius:0 8px 8px 0;font-style:italic}
#needs code{background:#eef0f6;padding:.08em .35em;border-radius:5px;font-size:.86em}
#needs hr{border:0;border-top:1px solid var(--line);margin:1.6em 0}
#needs table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.86rem;background:var(--card);
  border:1px solid var(--line);border-radius:10px;overflow:hidden}
#needs th{background:var(--navy);color:#fff;text-align:left;padding:9px 11px;font-weight:600}
#needs td{padding:8px 11px;border-top:1px solid var(--line);vertical-align:top}
#needs tr:nth-child(even) td{background:#faf9f6}
#needs strong{color:var(--navy)}
.plink{cursor:pointer;color:#1f6f8b !important;border-bottom:1.5px dotted var(--blue);font-weight:600}
.plink:hover{background:var(--blue-bg)}
.note{background:var(--blue-bg);border:1px solid #d4ebf2;border-radius:10px;padding:10px 14px;margin:0 0 18px;
  font-size:.9rem;color:#33405e}

/* ---- Tab 2 catalogue ---- */
.toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:16px;
  background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px}
.toolbar input,.toolbar select{font-family:inherit;font-size:.88rem;padding:8px 10px;border:1px solid var(--line);
  border-radius:8px;background:#fff;color:var(--ink)}
.toolbar input[type=search]{flex:1;min-width:200px}
.seg-chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px}
.chip{appearance:none;border:1px solid var(--line);background:#fff;padding:6px 12px;border-radius:999px;
  font-size:.82rem;cursor:pointer;font-family:inherit;color:#3a4566;font-weight:600}
.chip.active{background:var(--navy);color:#fff;border-color:var(--navy)}
.count{color:var(--muted);font-size:.85rem;margin-left:auto;white-space:nowrap}
.btn-clear{background:var(--blue-bg);border:1px solid #cfe7ef;color:#1f6f8b;border-radius:8px;padding:8px 12px;
  cursor:pointer;font-family:inherit;font-weight:600;font-size:.84rem}
table.cat{border-collapse:collapse;width:100%;background:var(--card);border:1px solid var(--line);
  border-radius:12px;overflow:hidden;font-size:.86rem}
table.cat th{position:sticky;top:0;background:var(--navy);color:#fff;text-align:left;padding:10px 12px;font-weight:600;
  cursor:pointer;white-space:nowrap}
table.cat th .ar{opacity:.5;font-size:.75em}
table.cat td{padding:10px 12px;border-top:1px solid var(--line);vertical-align:top}
table.cat tbody tr{cursor:pointer}
table.cat tbody tr:hover{background:var(--blue-bg)}
.nm{font-weight:700;color:var(--navy)}
.sub{color:var(--muted);font-size:.78rem}
.badge{display:inline-block;padding:2px 9px;border-radius:999px;font-size:.72rem;font-weight:700;white-space:nowrap}
.b-proven{background:var(--green-bg);color:#1d6b3f}
.b-growing{background:var(--blue-bg);color:#1f6f8b}
.b-mixed{background:var(--amber-bg);color:#9a7415}
.b-niche{background:#eef0f6;color:#5a6079}
.b-struggling,.b-dead{background:var(--coral-bg);color:#b23535}
.flag{display:inline-block;padding:1px 8px;border-radius:6px;font-size:.7rem;font-weight:700}
.f-innovate{background:#efeaff;color:#5b46b8}.f-adopt{background:var(--green-bg);color:#1d6b3f}
.f-avoid{background:var(--coral-bg);color:#b23535}.f-watch{background:#eef0f6;color:#5a6079}
.f-self{background:var(--navy);color:#fff}
.geo{font-size:.74rem;color:#3a4566}
.empty{padding:40px;text-align:center;color:var(--muted)}

/* ---- overlay ---- */
.overlay{position:fixed;inset:0;background:rgba(13,22,79,.45);display:none;align-items:flex-start;
  justify-content:center;padding:40px 16px;z-index:50;overflow-y:auto}
.overlay.open{display:flex}
.modal{background:#fff;max-width:680px;width:100%;border-radius:16px;box-shadow:0 24px 60px rgba(13,22,79,.3);
  overflow:hidden;animation:pop .14s ease}
@keyframes pop{from{transform:translateY(8px);opacity:.6}to{transform:none;opacity:1}}
.modal .top{background:var(--navy);color:#fff;padding:18px 22px;position:relative}
.modal .top h2{margin:0;font-size:1.3rem}
.modal .top .meta{color:#b9bedf;font-size:.82rem;margin-top:3px}
.modal .x{position:absolute;top:14px;right:16px;background:rgba(255,255,255,.15);border:0;color:#fff;
  width:30px;height:30px;border-radius:8px;font-size:1.1rem;cursor:pointer}
.modal .body{padding:20px 22px}
.modal .badges{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.modal .what{font-size:1rem;color:#27314f;margin:0 0 16px}
.kv{display:grid;grid-template-columns:130px 1fr;gap:6px 14px;font-size:.88rem;margin-bottom:8px}
.kv dt{color:var(--muted);font-weight:600}.kv dd{margin:0;color:#27314f}
.section-h{font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);font-weight:700;
  margin:16px 0 7px}
.tags{display:flex;gap:6px;flex-wrap:wrap}
.tag{background:var(--blue-bg);color:#1f6f8b;border-radius:999px;padding:3px 10px;font-size:.78rem;font-weight:600}
.tag.clickable{cursor:pointer;border:1px solid #cfe7ef}.tag.clickable:hover{background:#dcf0f6}
.tag.feat{background:#f2f1f7;color:#5a6079}
.modal .actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px;padding-top:16px;border-top:1px solid var(--line)}
.act{border-radius:9px;padding:9px 15px;font-weight:700;font-size:.85rem;cursor:pointer;text-decoration:none;
  font-family:inherit;border:1px solid var(--line)}
.act.primary{background:var(--navy);color:#fff;border-color:var(--navy)}
.act.ghost{background:#fff;color:#1f6f8b;border-color:#cfe7ef}
footer{color:var(--muted);font-size:.8rem;text-align:center;padding:26px;border-top:1px solid var(--line)}
@media(max-width:640px){.kv{grid-template-columns:1fr}.htitle{display:none}}
</style>
</head>
<body>
<header>
  <div class="logo">ditto<span class="dot"></span>
    <span><small>Care. Clarified.</small></span>
  </div>
  <div class="htitle">Cancer Patient Needs &amp; Solution Market Explorer</div>
</header>
<div class="tabs">
  <button class="tab active" data-tab="needs">① Needs &amp; Solution Landscape</button>
  <button class="tab" data-tab="catalogue">② Market Catalogue (__COUNT__ players)</button>
</div>

<div class="wrap">
  <section id="view-needs" class="view active">
    <div class="note">Tip: <b>bold solution names</b> below are clickable — open a detail card and jump to the full market catalogue.</div>
    <div id="needs"></div>
  </section>

  <section id="view-catalogue" class="view">
    <div class="seg-chips" id="segChips"></div>
    <div class="toolbar">
      <input type="search" id="q" placeholder="Search name, what it does, mechanism, traction…">
      <select id="fNeed"><option value="">All needs (1–14)</option></select>
      <select id="fGeo">
        <option value="">All regions</option><option>EU</option><option>US</option>
        <option>Asia</option><option>Global</option><option>Other</option>
      </select>
      <select id="fVerdict">
        <option value="">All verdicts</option><option>Proven</option><option>Growing</option>
        <option>Mixed</option><option>Niche</option><option>Struggling</option><option>Dead</option>
      </select>
      <button class="btn-clear" id="clearBtn">Clear</button>
      <span class="count" id="count"></span>
    </div>
    <table class="cat">
      <thead><tr>
        <th data-sort="name">Player <span class="ar">↕</span></th>
        <th data-sort="segment">Segment <span class="ar">↕</span></th>
        <th data-sort="geo">Geo <span class="ar">↕</span></th>
        <th>What it does</th>
        <th>Traction</th>
        <th data-sort="verdict">Verdict <span class="ar">↕</span></th>
        <th>Ditto</th>
      </tr></thead>
      <tbody id="rows"></tbody>
    </table>
    <div class="empty" id="empty" style="display:none">No players match these filters.</div>
  </section>
</div>

<div class="overlay" id="overlay"><div class="modal" id="modal"></div></div>

<footer>Ditto Care · generated from <code>players.json</code> (__COUNT__ players) + the needs-landscape research · self-contained, offline-capable.</footer>

<script type="application/json" id="players-data">/*PLAYERS_JSON*/</script>
<script type="application/json" id="alias-map">/*ALIAS_MAP*/</script>
<script type="text/markdown" id="needs-md"><!--NEEDS_MD--></script>
<script>
const PLAYERS = JSON.parse(document.getElementById('players-data').textContent);
const ALIAS = JSON.parse(document.getElementById('alias-map').textContent);
const NEED_LABELS = /*NEED_LABELS*/;
PLAYERS.forEach((p,i)=>p._i=i);

/* ---------- region helper ---------- */
const EU=["eu","europe","netherlands","nl","germany","france","united kingdom","uk","finland","sweden","spain","poland","denmark","switzerland","portugal","slovakia","belgium","italy"];
const ASIA=["china","japan","korea","india","indonesia","singapore","malaysia","uae","asia"];
function regions(p){
  const b=((p.hq||'')+' '+(p.markets||'')).toLowerCase();const o=new Set();
  if(EU.some(k=>b.includes(k)))o.add('EU');
  if(/\bus\b/.test(b)||b.includes('united states'))o.add('US');
  if(ASIA.some(k=>b.includes(k)))o.add('Asia');
  if(b.includes('global'))o.add('Global');
  return o.size?[...o]:['Other'];
}
PLAYERS.forEach(p=>p._r=regions(p));

/* ---------- minimal markdown renderer ---------- */
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function inline(s){
  s=esc(s);
  s=s.replace(/`([^`]+)`/g,'<code>$1</code>');
  s=s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>');
  s=s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
  s=s.replace(/(^|[^*])\*([^*]+)\*/g,'$1<em>$2</em>');
  return s;
}
function renderMD(md){
  const lines=md.split('\n');let html='';let i=0;
  const flushP=(buf)=>{if(buf.length){html+='<p>'+inline(buf.join(' '))+'</p>';}return [];};
  let para=[];
  while(i<lines.length){
    let ln=lines[i];
    // table
    if(/^\s*\|/.test(ln) && i+1<lines.length && /^\s*\|?[\s:\-|]+\|/.test(lines[i+1])){
      para=flushP(para);
      const head=ln.split('|').slice(1,-1).map(c=>c.trim());
      i+=2;let body=[];
      while(i<lines.length && /^\s*\|/.test(lines[i])){
        body.push(lines[i].split('|').slice(1,-1).map(c=>c.trim()));i++;
      }
      html+='<table><thead><tr>'+head.map(h=>'<th>'+inline(h)+'</th>').join('')+'</tr></thead><tbody>';
      html+=body.map(r=>'<tr>'+r.map(c=>'<td>'+inline(c)+'</td>').join('')+'</tr>').join('');
      html+='</tbody></table>';continue;
    }
    let m;
    if(/^\s*$/.test(ln)){para=flushP(para);i++;continue;}
    if(m=ln.match(/^(#{1,6})\s+(.*)/)){para=flushP(para);const l=m[1].length;html+='<h'+l+'>'+inline(m[2])+'</h'+l+'>';i++;continue;}
    if(/^---+\s*$/.test(ln)){para=flushP(para);html+='<hr>';i++;continue;}
    if(/^\s*>\s?/.test(ln)){para=flushP(para);let q=[];
      while(i<lines.length && /^\s*>\s?/.test(lines[i])){q.push(lines[i].replace(/^\s*>\s?/,''));i++;}
      html+='<blockquote>'+inline(q.join(' '))+'</blockquote>';continue;}
    if(/^\s*[-*]\s+/.test(ln)){para=flushP(para);let items=[];
      while(i<lines.length && /^\s*[-*]\s+/.test(lines[i])){items.push(lines[i].replace(/^\s*[-*]\s+/,''));i++;}
      html+='<ul>'+items.map(it=>'<li>'+inline(it)+'</li>').join('')+'</ul>';continue;}
    para.push(ln.trim());i++;
  }
  flushP(para);
  return html;
}
function nrm(s){return s.toLowerCase().replace(/[^a-z0-9]+/g,' ').replace(/\s+/g,' ').trim();}
function linkify(container){
  container.querySelectorAll('strong').forEach(s=>{
    const t=nrm(s.textContent);
    let idx=ALIAS[t];
    if(idx===undefined){ // light prefix match for multiword (e.g. "ditto care circle")
      for(const a in ALIAS){ if(a.includes(' ') && (t===a || t.startsWith(a+' '))){idx=ALIAS[a];break;} }
    }
    if(idx!==undefined){s.className='plink';s.dataset.idx=idx;}
  });
}
const needsEl=document.getElementById('needs');
needsEl.innerHTML=renderMD(document.getElementById('needs-md').textContent);
linkify(needsEl);
needsEl.addEventListener('click',e=>{const a=e.target.closest('.plink');if(a)openOverlay(+a.dataset.idx);});

/* ---------- tabs ---------- */
function setTab(name){
  document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('active',t.dataset.tab===name));
  document.getElementById('view-needs').classList.toggle('active',name==='needs');
  document.getElementById('view-catalogue').classList.toggle('active',name==='catalogue');
  window.scrollTo(0,0);
}
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>setTab(t.dataset.tab));

/* ---------- verdict / flag styling ---------- */
function vClass(v){v=(v||'').toLowerCase();
  if(v.includes('proven'))return'b-proven';if(v.includes('growing'))return'b-growing';
  if(v.includes('mixed'))return'b-mixed';if(v.includes('struggl'))return'b-struggling';
  if(v.includes('dead'))return'b-dead';return'b-niche';}
function fClass(f){f=(f||'').toLowerCase();
  if(f.includes('self'))return'f-self';if(f.includes('innovate'))return'f-innovate';
  if(f.includes('adopt'))return'f-adopt';if(f.includes('avoid'))return'f-avoid';return'f-watch';}
function tr1(s,n){s=s||'';return s.length>n?s.slice(0,n-1)+'…':s;}
function traction(p){return [p.users,p.revenue,p.funding].filter(Boolean).join(' · ')||'—';}

/* ---------- segment chips + need filter ---------- */
const SEGS=[...new Set(PLAYERS.map(p=>p.segment))];
const segChips=document.getElementById('segChips');
let activeSeg='';
function buildChips(){
  segChips.innerHTML='';
  const mk=(label,val)=>{const b=document.createElement('button');b.className='chip'+(activeSeg===val?' active':'');
    b.textContent=label+(val?' ('+PLAYERS.filter(p=>p.segment===val).length+')':' ('+PLAYERS.length+')');
    b.onclick=()=>{activeSeg=val;buildChips();render();};return b;};
  segChips.appendChild(mk('All',''));
  SEGS.forEach(s=>segChips.appendChild(mk(s,s)));
}
const fNeed=document.getElementById('fNeed');
Object.keys(NEED_LABELS).forEach(k=>{const o=document.createElement('option');o.value=k;o.textContent=k+'. '+NEED_LABELS[k];fNeed.appendChild(o);});

/* ---------- filtering / sorting / render ---------- */
const q=document.getElementById('q'),fGeo=document.getElementById('fGeo'),fVerdict=document.getElementById('fVerdict');
let sortKey='name',sortDir=1;
function matches(p){
  if(activeSeg && p.segment!==activeSeg)return false;
  const need=fNeed.value;if(need && !(p.needs||[]).map(String).includes(need))return false;
  const geo=fGeo.value;if(geo && !p._r.includes(geo))return false;
  const v=fVerdict.value;if(v && !(p.verdict||'').toLowerCase().includes(v.toLowerCase()))return false;
  const term=q.value.trim().toLowerCase();
  if(term){const blob=[p.name,p.what,p.mechanism,p.differentiation,p.category,p.users,p.revenue,p.funding,p.business_model,p.hq,p.markets].join(' ').toLowerCase();
    if(!blob.includes(term))return false;}
  return true;
}
function sortVal(p){if(sortKey==='geo')return p._r.join();if(sortKey==='verdict')return p.verdict||'';return (p[sortKey]||'').toLowerCase();}
function render(){
  let list=PLAYERS.filter(matches);
  list.sort((a,b)=>{const x=sortVal(a),y=sortVal(b);return x<y?-1*sortDir:x>y?1*sortDir:0;});
  const rows=document.getElementById('rows');rows.innerHTML='';
  list.forEach(p=>{
    const tr=document.createElement('tr');tr.onclick=()=>openOverlay(p._i);
    tr.innerHTML='<td><span class="nm">'+esc(p.name)+'</span><div class="sub">'+esc(p.category||'')+'</div></td>'+
      '<td><span class="sub">'+esc(p.segment)+'</span></td>'+
      '<td><span class="geo">'+p._r.join(', ')+'</span></td>'+
      '<td>'+esc(tr1(p.what,90))+'</td>'+
      '<td><span class="sub">'+esc(tr1(traction(p),64))+'</span></td>'+
      '<td><span class="badge '+vClass(p.verdict)+'">'+esc(p.verdict||'—')+'</span>'+
        (p.status==='Defunct'?' <span class="sub">defunct</span>':p.status==='Acquired'?' <span class="sub">acq.</span>':'')+'</td>'+
      '<td><span class="flag '+fClass(p.ditto_flag)+'">'+esc(p.ditto_flag||'—')+'</span></td>';
    rows.appendChild(tr);
  });
  document.getElementById('empty').style.display=list.length?'none':'block';
  document.getElementById('count').textContent=list.length+' of '+PLAYERS.length+' players';
}
[q,fNeed,fGeo,fVerdict].forEach(el=>el.addEventListener('input',render));
document.getElementById('clearBtn').onclick=()=>{activeSeg='';q.value='';fNeed.value='';fGeo.value='';fVerdict.value='';buildChips();render();};
document.querySelectorAll('th[data-sort]').forEach(th=>th.onclick=()=>{
  const k=th.dataset.sort;if(sortKey===k)sortDir*=-1;else{sortKey=k;sortDir=1;}render();});

/* ---------- overlay ---------- */
const overlay=document.getElementById('overlay'),modal=document.getElementById('modal');
function kv(label,val){return val?'<dt>'+label+'</dt><dd>'+esc(val)+'</dd>':'';}
function openOverlay(idx){
  const p=PLAYERS[idx];
  const needTags=(p.needs||[]).map(n=>'<span class="tag clickable" data-need="'+n+'">'+n+'. '+(NEED_LABELS[n]||'')+'</span>').join('');
  const feats=(p.features||'').split(';').map(s=>s.trim()).filter(Boolean)
    .map(f=>'<span class="tag feat">'+esc(f)+'</span>').join('');
  modal.innerHTML=
    '<div class="top"><button class="x" id="closeX">×</button>'+
      '<h2>'+esc(p.name)+'</h2>'+
      '<div class="meta">'+esc([p.segment,p.category].filter(Boolean).join(' · '))+
        (p.hq?' · '+esc(p.hq):'')+'</div></div>'+
    '<div class="body">'+
      '<div class="badges">'+
        '<span class="badge '+vClass(p.verdict)+'">'+esc(p.verdict||'—')+'</span>'+
        (p.status?'<span class="badge b-niche">'+esc(p.status)+'</span>':'')+
        (p.ditto_flag?'<span class="flag '+fClass(p.ditto_flag)+'">Ditto: '+esc(p.ditto_flag)+'</span>':'')+
        (p.source_tier?'<span class="badge b-niche">'+esc(p.source_tier)+'</span>':'')+
      '</div>'+
      (p.what?'<p class="what">'+esc(p.what)+'</p>':'')+
      '<dl class="kv">'+kv('Geography',(p.markets||p.hq))+kv('Mechanism',p.mechanism)+
        kv('Differentiator',p.differentiation)+kv('Business model',p.business_model)+
        kv('Users',p.users)+kv('Revenue',p.revenue)+kv('Funding / val.',p.funding)+
        kv('Retention',p.retention)+kv('Notes',p.notes)+'</dl>'+
      (needTags?'<div class="section-h">Patient needs served</div><div class="tags">'+needTags+'</div>':'')+
      (feats?'<div class="section-h">Key features</div><div class="tags">'+feats+'</div>':'')+
      '<div class="actions">'+
        (p.source_url?'<a class="act ghost" href="'+esc(p.source_url)+'" target="_blank" rel="noopener">Read more ↗</a>':'')+
        '<button class="act primary" id="viewCat">View in catalogue ↗</button>'+
      '</div>'+
    '</div>';
  overlay.classList.add('open');
  document.getElementById('closeX').onclick=closeOverlay;
  document.getElementById('viewCat').onclick=()=>{closeOverlay();activeSeg='';fNeed.value='';fGeo.value='';fVerdict.value='';
    q.value=p.name;buildChips();render();setTab('catalogue');};
  modal.querySelectorAll('[data-need]').forEach(t=>t.onclick=()=>{closeOverlay();activeSeg='';q.value='';fGeo.value='';fVerdict.value='';
    fNeed.value=t.dataset.need;buildChips();render();setTab('catalogue');});
}
function closeOverlay(){overlay.classList.remove('open');}
overlay.addEventListener('click',e=>{if(e.target===overlay)closeOverlay();});
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeOverlay();});

buildChips();render();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
