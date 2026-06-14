import React, { useState, useMemo } from "react";

// ---- Data ---------------------------------------------------------------
const AXES = [
  { key: "intelligence", label: "Intelligence", note: "Proprietary / applied AI reasoning" },
  { key: "comprehension", label: "Comprehension", note: "Making sense of what is happening" },
  { key: "connection", label: "Connection", note: "Relational — not alone, held by others" },
  { key: "coordination", label: "Coordination", note: "Tasks, agendas, care-group orchestration" },
  { key: "continuity", label: "Continuity", note: "Your whole record, yours to carry anywhere" },
  { key: "agency", label: "Agency", note: "Internal — capacity to act & decide" },
];

const VISIONS = [
  { id: 1, name: "Care Companion", tag: "Understand the journey", color: "#d98c3f",
    scores: { intelligence: 4, comprehension: 5, connection: 2, coordination: 2, continuity: 2, agency: 3 } },
  { id: 2, name: "Social Care Platform", tag: "Shared understanding, loved ones", color: "#5a8f7b",
    scores: { intelligence: 1, comprehension: 2, connection: 5, coordination: 2, continuity: 1, agency: 1 } },
  { id: 3, name: "Care Coordination", tag: "Families manage the disease", color: "#7a7fb0",
    scores: { intelligence: 1, comprehension: 2, connection: 3, coordination: 5, continuity: 2, agency: 2 } },
  { id: 4, name: "Patient-Owned Record", tag: "You own your data", color: "#9a9388",
    scores: { intelligence: 2, comprehension: 3, connection: 1, coordination: 2, continuity: 5, agency: 1 } },
  { id: 5, name: "Trusted Health Assistant", tag: "Prevent illness, recover best", color: "#b8504a",
    scores: { intelligence: 5, comprehension: 3, connection: 1, coordination: 2, continuity: 3, agency: 5 } },
];

const MAX = 5;

// progression coordinates derived from primitives
// Empowerment: passive -> comprehending -> agentic (agency weighted as the far end)
const empowerment = (s) => 0.35 * s.comprehension + 0.65 * s.agency;
// Relational reach: self -> loved ones -> community (emotional + operational widening)
const relational = (s) => (s.connection + s.coordination) / 2;

// ---- geometry -----------------------------------------------------------
function polar(cx, cy, r, angleDeg) {
  const a = ((angleDeg - 90) * Math.PI) / 180;
  return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
}
// convex hull (Andrew's monotone chain)
function hull(points) {
  const pts = [...points].sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  if (pts.length < 3) return pts;
  const cross = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
  const lower = [];
  for (const p of pts) {
    while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], p) <= 0) lower.pop();
    lower.push(p);
  }
  const upper = [];
  for (let i = pts.length - 1; i >= 0; i--) {
    const p = pts[i];
    while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], p) <= 0) upper.pop();
    upper.push(p);
  }
  return lower.slice(0, -1).concat(upper.slice(0, -1));
}

// ---- RADAR --------------------------------------------------------------
function RadarMap({ size, active, additive, hovered }) {
  const cx = size / 2, cy = size / 2, R = size / 2 - 96;
  const n = AXES.length;
  const angleAt = (i) => (360 / n) * i;
  const rings = [1, 2, 3, 4, 5];

  const envelope = useMemo(() => {
    if (!additive || active.length === 0) return null;
    return AXES.map((ax) => Math.max(...VISIONS.filter(v => active.includes(v.id)).map(v => v.scores[ax.key])));
  }, [additive, active]);

  return (
    <svg viewBox={`0 0 ${size} ${size}`} width="100%" style={{ display: "block" }}>
      {rings.map((ring) => {
        const pts = AXES.map((_, i) => polar(cx, cy, (R * ring) / MAX, angleAt(i)));
        return <polygon key={ring} points={pts.map(p => p.join(",")).join(" ")} fill="none"
          stroke="#2a2620" strokeWidth={ring === MAX ? 1.4 : 0.7} opacity={ring === MAX ? 0.9 : 0.4} />;
      })}
      {AXES.map((ax, i) => {
        const [ex, ey] = polar(cx, cy, R, angleAt(i));
        const [lx, ly] = polar(cx, cy, R + 30, angleAt(i));
        const ang = angleAt(i);
        const anchor = ang > 10 && ang < 170 ? "start" : ang > 190 && ang < 350 ? "end" : "middle";
        return (
          <g key={ax.key}>
            <line x1={cx} y1={cy} x2={ex} y2={ey} stroke="#3a342b" strokeWidth={0.8} opacity={0.6} />
            <text x={lx} y={ly} textAnchor={anchor} dominantBaseline="middle" fontSize="13.5" fontWeight={500}
              fill="#cabfa9" fontFamily="'Newsreader', serif">{ax.label}</text>
          </g>
        );
      })}
      {!additive && VISIONS.map((v) => {
        if (!active.includes(v.id)) return null;
        const isHov = hovered === v.id, anyHov = hovered != null;
        const pts = AXES.map((ax, i) => polar(cx, cy, (R * v.scores[ax.key]) / MAX, angleAt(i)));
        return (
          <g key={v.id} opacity={anyHov ? (isHov ? 1 : 0.12) : 1} style={{ transition: "opacity 220ms" }}>
            <polygon points={pts.map(p => p.join(",")).join(" ")} fill={v.color}
              fillOpacity={isHov ? 0.26 : 0.13} stroke={v.color} strokeWidth={isHov ? 3 : 1.8} strokeLinejoin="round" />
            {pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r={isHov ? 4 : 2.6} fill={v.color} />)}
          </g>
        );
      })}
      {additive && envelope && (
        <g>
          <polygon points={AXES.map((_, i) => polar(cx, cy, (R * envelope[i]) / MAX, angleAt(i)).join(",")).join(" ")}
            fill="#d9a64f" fillOpacity={0.18} stroke="#e8b860" strokeWidth={2.4} strokeLinejoin="round" />
          {AXES.map((_, i) => { const p = polar(cx, cy, (R * envelope[i]) / MAX, angleAt(i)); return <circle key={i} cx={p[0]} cy={p[1]} r={3.4} fill="#e8b860" />; })}
        </g>
      )}
    </svg>
  );
}

// ---- PROGRESSION (2D) ---------------------------------------------------
function ProgressionMap({ size, active, additive, hovered }) {
  const pad = 64;
  const W = size, H = size;
  const x0 = pad, x1 = W - pad, y0 = H - pad, y1 = pad; // y inverted
  const sx = (e) => x0 + (e / MAX) * (x1 - x0);
  const sy = (r) => y0 + (r / MAX) * (y1 - y0);
  const rIntel = (intel) => 9 + intel * 5; // bubble radius by intelligence

  const pts = VISIONS.map(v => ({
    ...v, e: empowerment(v.scores), r: relational(v.scores),
    px: sx(empowerment(v.scores)), py: sy(relational(v.scores)),
  }));

  const activePts = pts.filter(p => active.includes(p.id));
  const hullPts = useMemo(() => {
    if (!additive) return null;
    const raw = [[sx(0), sy(0)], ...activePts.map(p => [p.px, p.py])];
    return hull(raw);
  }, [additive, active]);

  return (
    <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ display: "block" }}>
      <defs>
        <linearGradient id="substrate" x1="0" y1="1" x2="1" y2="1">
          <stop offset="0%" stopColor="#3a342b" stopOpacity="0" />
          <stop offset="100%" stopColor="#7a6233" stopOpacity="0.28" />
        </linearGradient>
      </defs>
      {/* substrate band under empowerment axis = Continuity feeding depth */}
      <rect x={x0} y={y0 - 26} width={x1 - x0} height={26} fill="url(#substrate)" />
      <text x={x1} y={y0 - 32} textAnchor="end" fontSize="11" fill="#8a7340" fontFamily="'IBM Plex Mono', monospace" letterSpacing="0.5">
        ↑ Continuity (data substrate) deepens the empowerment axis
      </text>

      {/* grid */}
      {[1,2,3,4,5].map(g => (
        <g key={g}>
          <line x1={sx(g)} y1={y0} x2={sx(g)} y2={y1} stroke="#241f19" strokeWidth={0.7} />
          <line x1={x0} y1={sy(g)} x2={x1} y2={sy(g)} stroke="#241f19" strokeWidth={0.7} />
        </g>
      ))}
      {/* axes */}
      <line x1={x0} y1={y0} x2={x1} y2={y0} stroke="#5a5240" strokeWidth={1.4} />
      <line x1={x0} y1={y0} x2={x0} y2={y1} stroke="#5a5240" strokeWidth={1.4} />

      {/* patient at origin */}
      <circle cx={sx(0)} cy={sy(0)} r={5} fill="#cabfa9" />
      <text x={sx(0) + 10} y={sy(0) + 4} fontSize="11.5" fill="#8a8170" fontFamily="'IBM Plex Mono', monospace">the patient</text>

      {/* axis labels with progression text */}
      <text x={(x0 + x1) / 2} y={H - 22} textAnchor="middle" fontSize="14" fontWeight={600} fill="#e0d4ba" fontFamily="'Newsreader', serif">Empowerment</text>
      <text x={x0 + 6} y={y0 + 32} fontSize="10.5" fill="#7d7466" fontFamily="'IBM Plex Mono', monospace">passive</text>
      <text x={x1 - 6} y={y0 + 32} textAnchor="end" fontSize="10.5" fill="#7d7466" fontFamily="'IBM Plex Mono', monospace">agentic</text>
      <g transform={`translate(20, ${(y0 + y1) / 2}) rotate(-90)`}>
        <text textAnchor="middle" fontSize="14" fontWeight={600} fill="#e0d4ba" fontFamily="'Newsreader', serif">Relational reach</text>
      </g>
      <text x={x0 - 8} y={y0 - 4} textAnchor="end" fontSize="10.5" fill="#7d7466" fontFamily="'IBM Plex Mono', monospace" transform={`rotate(-90 ${x0-8} ${y0-4})`} />

      {/* additive hull */}
      {additive && hullPts && hullPts.length >= 3 && (
        <polygon points={hullPts.map(p => p.join(",")).join(" ")} fill="#d9a64f" fillOpacity={0.13} stroke="#e8b860" strokeWidth={2} strokeDasharray="5 4" strokeLinejoin="round" />
      )}

      {/* bubbles */}
      {pts.map((p) => {
        if (!active.includes(p.id)) return null;
        const isHov = hovered === p.id, anyHov = hovered != null;
        return (
          <g key={p.id} opacity={anyHov ? (isHov ? 1 : 0.18) : 1} style={{ transition: "opacity 220ms" }}>
            <circle cx={p.px} cy={p.py} r={rIntel(p.scores.intelligence)} fill={p.color} fillOpacity={0.2} stroke={p.color} strokeWidth={isHov ? 2.6 : 1.6} />
            <circle cx={p.px} cy={p.py} r={4} fill={p.color} />
            <text x={p.px} y={p.py - rIntel(p.scores.intelligence) - 7} textAnchor="middle" fontSize="12.5" fontWeight={600} fill={p.color} fontFamily="'Newsreader', serif">{p.id}. {p.name}</text>
          </g>
        );
      })}
    </svg>
  );
}

// ---- App ----------------------------------------------------------------
export default function App() {
  const [active, setActive] = useState([1, 2, 3, 4, 5]);
  const [additive, setAdditive] = useState(false);
  const [hovered, setHovered] = useState(null);

  const toggle = (id) => setActive(a => a.includes(id) ? a.filter(x => x !== id) : [...a, id]);

  return (
    <div style={{ minHeight: "100vh", background: "radial-gradient(120% 120% at 30% 0%, #1c1813 0%, #14110d 55%, #100d0a 100%)", color: "#e8ddc8", fontFamily: "'Newsreader', Georgia, serif", paddingBottom: 60 }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
        * { box-sizing: border-box; }
        .leg:hover { transform: translateX(3px); }
      `}</style>

      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "44px 32px 22px" }}>
        <div style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: 11, letterSpacing: 3, color: "#a8794a", textTransform: "uppercase", marginBottom: 14 }}>Ditto · Product Vision · Two Lenses</div>
        <h1 style={{ fontSize: 40, lineHeight: 1.06, margin: "0 0 12px", fontWeight: 600, letterSpacing: -0.5 }}>Capability and progression.</h1>
        <p style={{ maxWidth: 760, fontSize: 17.5, lineHeight: 1.55, color: "#b4a98f", margin: 0 }}>
          The <strong style={{color:"#d8cdb6"}}>radial map</strong> treats the six primitives as independent capabilities — each vision is a profile.
          The <strong style={{color:"#d8cdb6"}}>progression map</strong> drops the visions onto the two roads that actually lead somewhere:
          empowerment (passive → agentic) and relational reach (self → community). Intelligence is bubble size — the depth that drives movement along empowerment. Continuity is the substrate beneath it.
        </p>
      </div>

      {/* controls */}
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "0 32px 8px", display: "flex", gap: 24, alignItems: "center", flexWrap: "wrap" }}>
        <div style={{ display: "flex", gap: 0, border: "1px solid #2c271f", borderRadius: 6, overflow: "hidden" }}>
          {[["separate", false], ["additive", true]].map(([lbl, val]) => (
            <button key={lbl} onClick={() => setAdditive(val)} style={{
              cursor: "pointer", padding: "9px 20px", border: "none", color: additive === val ? "#15120d" : "#b4a98f",
              background: additive === val ? "#d9a64f" : "#1a1611", fontFamily: "'IBM Plex Mono', monospace", fontSize: 12, letterSpacing: 1, textTransform: "uppercase", fontWeight: 600 }}>
              {lbl}
            </button>
          ))}
        </div>
        <div style={{ fontSize: 13.5, color: "#8a8170", fontStyle: "italic" }}>
          {additive ? "Additive — the gold envelope/region shows what the selected visions cover when stacked together." : "Separate — each selected vision drawn on its own."}
        </div>
      </div>

      {/* maps */}
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "12px 32px 0", display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
        <div style={{ background: "#15120d", border: "1px solid #2c271f", borderRadius: 8, padding: 18 }}>
          <div style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: 11, letterSpacing: 2, color: "#8a7340", textTransform: "uppercase", marginBottom: 6 }}>Radial — capabilities</div>
          <RadarMap size={520} active={active} additive={additive} hovered={hovered} />
        </div>
        <div style={{ background: "#15120d", border: "1px solid #2c271f", borderRadius: 8, padding: 18 }}>
          <div style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: 11, letterSpacing: 2, color: "#8a7340", textTransform: "uppercase", marginBottom: 6 }}>Progression — direction of travel</div>
          <ProgressionMap size={520} active={active} additive={additive} hovered={hovered} />
        </div>
      </div>

      {/* legend */}
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "20px 32px 0", display: "grid", gridTemplateColumns: "1fr 1fr 1fr 1fr 1fr", gap: 10 }}>
        {VISIONS.map((v) => {
          const on = active.includes(v.id);
          return (
            <div key={v.id} className="leg" onClick={() => toggle(v.id)} onMouseEnter={() => setHovered(v.id)} onMouseLeave={() => setHovered(null)}
              style={{ cursor: "pointer", borderRadius: 6, padding: "12px 14px", transition: "all 160ms",
                background: on ? "#1c1812" : "transparent", border: `1px solid ${on ? "#2e2820" : "transparent"}`, opacity: on ? 1 : 0.45 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 9, marginBottom: 5 }}>
                <div style={{ width: 13, height: 13, borderRadius: 3, background: v.color, boxShadow: on ? `0 0 9px ${v.color}66` : "none" }} />
                <div style={{ fontFamily: "'IBM Plex Mono', monospace", fontSize: 11, color: "#8a8170" }}>{`0${v.id}`}</div>
              </div>
              <div style={{ fontSize: 14.5, fontWeight: 600, color: on ? "#e8ddc8" : "#9a9080", lineHeight: 1.2 }}>{v.name}</div>
              <div style={{ fontSize: 11.5, color: "#7d7466", fontFamily: "'IBM Plex Mono', monospace", marginTop: 3 }}>{v.tag}</div>
            </div>
          );
        })}
      </div>

      {/* reading note */}
      <div style={{ maxWidth: 1280, margin: "0 auto", padding: "24px 32px 0" }}>
        <div style={{ background: "#17130d", border: "1px solid #2c271f", borderLeft: "3px solid #a8794a", borderRadius: 6, padding: "20px 24px", fontSize: 16, lineHeight: 1.6, color: "#c4b99f" }}>
          <strong style={{ color: "#e8ddc8" }}>What the progression map reveals.</strong> Care Companion (1) and Trusted Health Assistant (5) sit on the same low-relational line, with 5 further right and larger — it is vision 1 driven deeper by intelligence. Patient-Owned Record (4) sits back near the patient: low empowerment on its own, but it is the substrate band beneath the empowerment axis, the thing that lets 1 and 5 reach further right. Social (2) and Coordination (3) climb the relational axis instead. Flip to <em>additive</em> and select 4 · 1 · 5 to see the stack reach out from the passive patient toward full agency.
        </div>
      </div>
    </div>
  );
}
