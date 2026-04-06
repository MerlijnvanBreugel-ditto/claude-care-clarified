#!/usr/bin/env node

/**
 * Ditto Productivity Powerhouse — Repo Explainer Generator
 *
 * Scans the repo, extracts metadata from every file, and generates
 * a single self-contained HTML repo explainer. No dependencies — pure Node.js.
 *
 * Usage: node scripts/generate-dashboard.mjs
 * Output: repo-explainer.html (repo root)
 */

import { readFileSync, writeFileSync, readdirSync, statSync, existsSync } from 'fs';
import { join, relative, basename, extname, dirname } from 'path';
import { execSync } from 'child_process';

const REPO_ROOT = join(dirname(new URL(import.meta.url).pathname), '..');
const WORKSPACE = join(REPO_ROOT, 'pm-workspace');
const CLAUDE_MD = join(REPO_ROOT, 'CLAUDE.md');
const OUTPUT = join(REPO_ROOT, 'repo-explainer.html');

// ─── Helpers ───

function readJSON(path) {
  try { return JSON.parse(readFileSync(path, 'utf-8')); } catch { return null; }
}

function readText(path) {
  try { return readFileSync(path, 'utf-8'); } catch { return ''; }
}

function gitAuthor(filePath) {
  try {
    const author = execSync(`git log --format='%an' -1 -- "${filePath}"`, { cwd: REPO_ROOT, encoding: 'utf-8' }).trim();
    return author || 'Merlijn van Breugel';
  } catch { return 'Merlijn van Breugel'; }
}

function gitBranch() {
  try { return execSync('git branch --show-current', { cwd: REPO_ROOT, encoding: 'utf-8' }).trim(); }
  catch { return 'unknown'; }
}

function extractTitle(content) {
  const match = content.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : null;
}

function extractBlockquote(content) {
  // Extract all consecutive blockquote lines after the title as the TL;DR
  const lines = content.split('\n');
  const bqLines = [];
  let pastTitle = false;
  for (const line of lines) {
    if (!pastTitle && line.startsWith('# ')) { pastTitle = true; continue; }
    if (!pastTitle) continue;
    if (line.trim() === '') { if (bqLines.length) break; continue; }
    if (line.startsWith('> ')) { bqLines.push(line.slice(2).trim()); }
    else if (bqLines.length) break;
  }
  return bqLines.join(' ') || null;
}

function extractDescription(content) {
  const bq = extractBlockquote(content);
  if (bq) return bq;
  const lines = content.split('\n');
  for (const line of lines) {
    const t = line.trim();
    if (t && !t.startsWith('#') && !t.startsWith('>') && !t.startsWith('---') && !t.startsWith('```') && !t.startsWith('name:') && !t.startsWith('description:') && !t.startsWith('tools:') && !t.startsWith('mcpTools:') && !t.startsWith('model:')) {
      return t.length > 200 ? t.slice(0, 200) + '...' : t;
    }
  }
  return '';
}

function extractFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const fm = {};
  for (const line of match[1].split('\n')) {
    const [key, ...rest] = line.split(':');
    if (key && rest.length) {
      fm[key.trim()] = rest.join(':').trim().replace(/^["']|["']$/g, '');
    }
  }
  return fm;
}

function hasTodos(content) {
  return /TODO|PLACEHOLDER|TBD|\[ \]/i.test(content);
}

function extractReferences(content) {
  const refs = new Set();
  const pathMatches = content.matchAll(/pm-workspace\/[^\s)>\]"']+/g);
  for (const m of pathMatches) refs.add(m[0]);
  const wfMatches = content.matchAll(/\[([^\]]+)\]\(\.\/([^)]+)\)/g);
  for (const m of wfMatches) refs.add(m[2]);
  return [...refs];
}

function scanDir(dir, base = dir) {
  const results = [];
  if (!existsSync(dir)) return results;
  for (const entry of readdirSync(dir)) {
    if (entry.startsWith('.') || entry === 'node_modules' || entry === 'repo-explainer.html') continue;
    const full = join(dir, entry);
    const stat = statSync(full);
    if (stat.isDirectory()) {
      results.push(...scanDir(full, base));
    } else {
      results.push({ path: full, relative: relative(base, full), modified: stat.mtime, size: stat.size });
    }
  }
  return results;
}

function categorize(relPath) {
  if (relPath.startsWith('workflows/')) return 'workflow';
  if (relPath.startsWith('agents/')) return 'agent';
  if (relPath.startsWith('commands/')) return 'command';
  if (relPath.startsWith('context/')) return 'context';
  if (relPath.startsWith('how-we-run-product/')) return 'process';
  if (relPath.startsWith('templates/')) return 'template';
  if (relPath.startsWith('learnings/')) return 'learning';
  if (relPath.startsWith('specs/')) return 'spec';
  if (relPath.startsWith('data/')) return 'data';
  if (relPath.startsWith('backlog/')) return 'backlog';
  if (relPath.startsWith('registry/')) return 'registry';
  if (relPath.startsWith('tmp/')) return 'tmp';
  if (relPath.startsWith('scripts/')) return 'script';
  return 'other';
}

// ─── Scan ───

console.log('Scanning workspace...');

const files = scanDir(WORKSPACE);
const mdFiles = files.filter(f => extname(f.path) === '.md');
const jsonFiles = files.filter(f => extname(f.path) === '.json');

const registry = readJSON(join(WORKSPACE, 'registry', 'registry.json'));
const backlog = readJSON(join(WORKSPACE, 'backlog', 'backlog.json'));

// Build registry lookup for richer metadata
const registryLookup = {};
if (registry) {
  for (const a of registry.artifacts || []) registryLookup[a.path] = a;
  for (const w of registry.workflows || []) registryLookup[w.path] = w;
  for (const c of registry.commands || []) registryLookup[c.path] = c;
  for (const t of registry.templates || []) registryLookup[t.path] = t;
  for (const l of registry.learnings || []) registryLookup[l.path] = l;
}

const items = [];
for (const file of [...mdFiles, ...jsonFiles]) {
  const cat = categorize(file.relative);
  if (cat === 'registry' || cat === 'backlog' || cat === 'tmp' || cat === 'script') continue;

  const content = readText(file.path);
  const fm = extractFrontmatter(content);
  const regEntry = registryLookup['pm-workspace/' + file.relative];

  const title = fm.name || regEntry?.title || regEntry?.name || extractTitle(content) || basename(file.path, extname(file.path)).replace(/-/g, ' ');
  // TL;DR: frontmatter description (agents), then blockquote (commands/workflows), then registry
  const tldr = fm.description || extractBlockquote(content) || regEntry?.summary || '';
  const description = tldr || extractDescription(content);
  const todos = hasTodos(content);
  const refs = extractReferences(content);
  const author = gitAuthor(file.path);
  const status = regEntry?.status || (todos ? 'has-todos' : 'active');

  items.push({
    idx: items.length,
    path: file.relative,
    fullPath: 'pm-workspace/' + file.relative,
    category: cat,
    title,
    tldr,
    description,
    hasTodos: todos,
    references: refs,
    author: author || 'Merlijn van Breugel',
    modified: file.modified.toISOString().split('T')[0],
    size: file.size,
    status,
    registryId: regEntry?.id || null,
  });
}

// Group by category
const grouped = {};
for (const item of items) {
  if (!grouped[item.category]) grouped[item.category] = [];
  grouped[item.category].push(item);
}

const stats = {
  workflows: (grouped.workflow || []).length,
  agents: (grouped.agent || []).length,
  commands: (grouped.command || []).length,
  contexts: (grouped.context || []).length,
  processes: (grouped.process || []).length,
  templates: (grouped.template || []).length,
  learnings: (grouped.learning || []).length,
  specs: (grouped.spec || []).length,
  data: (grouped.data || []).length,
  totalFiles: items.length,
  backlogItems: backlog?.items?.length || 0,
  registryArtifacts: registry?.artifacts?.length || 0,
};

const integrations = [
  { name: 'Figma', desc: 'Design system extraction', status: 'configured', agent: 'product-designer' },
  { name: 'Google Stitch', desc: 'AI mockup generation', status: 'configured', agent: 'product-designer' },
  { name: 'NotebookLM', desc: 'User research insights', status: 'configured', agent: 'user-researcher' },
  { name: 'Atlassian', desc: 'Jira + Confluence', status: 'pending', backlogId: 'bl-006' },
  { name: 'Mixpanel', desc: 'Product analytics', status: 'pending', backlogId: 'bl-007' },
];

const flowStages = [
  { id: 'discover', label: 'Discover', desc: 'User research & insights', commands: ['/refine-idea'], workflows: ['Product Idea Refinement'] },
  { id: 'refine', label: 'Refine', desc: 'Score, validate, structure', commands: ['/refine-idea'], workflows: ['Product Idea Refinement'] },
  { id: 'scope', label: 'Scope', desc: 'Specs, epics, tickets', commands: ['/scope-feature'], workflows: ['Functional Scoping'] },
  { id: 'design', label: 'Design', desc: 'Mockups & panel review', commands: ['/mockup'], workflows: [] },
  { id: 'measure', label: 'Measure', desc: 'Metrics & tracking plan', commands: ['/measure-feature'], workflows: ['Feature Measurement'] },
  { id: 'ship', label: 'Ship', desc: 'Release & activation', commands: [], workflows: ['Shipping & Release'] },
  { id: 'learn', label: 'Learn', desc: 'Evaluate & iterate', commands: ['/review'], workflows: ['Process Product Strategy Meeting'] },
];

const branch = gitBranch();
const generated = new Date().toISOString();

console.log(`Found ${items.length} files across ${Object.keys(grouped).length} categories`);
console.log(`  Workflows: ${stats.workflows}, Agents: ${stats.agents}, Commands: ${stats.commands}`);
console.log(`  Context: ${stats.contexts}, Process: ${stats.processes}, Templates: ${stats.templates}`);
console.log(`  Specs: ${stats.specs}, Learnings: ${stats.learnings}, Data: ${stats.data}`);
console.log(`  Backlog items: ${stats.backlogItems}, Registry artifacts: ${stats.registryArtifacts}`);

// ─── Generate HTML ───

const DATA = JSON.stringify({
  items, grouped, stats,
  backlog: backlog?.items || [],
  integrations, flowStages,
  meta: { branch, generated },
});

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ditto Productivity Powerhouse</title>
<style>
/* ─── Design Tokens ─── */
:root {
  --bg: #f5f5f7;
  --surface: #ffffff;
  --surface-secondary: #fafafa;
  --surface-hover: rgba(0,0,0,0.03);
  --border: rgba(0,0,0,0.08);
  --border-strong: rgba(0,0,0,0.12);
  --text: #1d1d1f;
  --text-secondary: #6e6e73;
  --text-tertiary: #aeaeb2;
  --accent: #0071e3;
  --accent-hover: #0077ed;
  --accent-bg: rgba(0,113,227,0.08);
  --green: #34c759;
  --green-bg: rgba(52,199,89,0.1);
  --yellow: #ff9f0a;
  --yellow-bg: rgba(255,159,10,0.1);
  --red: #ff3b30;
  --red-bg: rgba(255,59,48,0.1);
  --purple: #af52de;
  --purple-bg: rgba(175,82,222,0.1);
  --orange: #ff9500;
  --orange-bg: rgba(255,149,0,0.1);
  --radius: 12px;
  --radius-sm: 8px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.04);
  --shadow: 0 2px 8px rgba(0,0,0,0.06), 0 0 1px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 30px rgba(0,0,0,0.08), 0 0 1px rgba(0,0,0,0.1);
  --shadow-xl: 0 20px 60px rgba(0,0,0,0.12), 0 0 1px rgba(0,0,0,0.1);
  --font: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', system-ui, sans-serif;
  --mono: 'SF Mono', 'Fira Code', 'Cascadia Code', 'Menlo', monospace;
  --ease: cubic-bezier(0.25, 0.1, 0.25, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --panel-width: 420px;
}
[data-theme="dark"] {
  --bg: #000000;
  --surface: #1c1c1e;
  --surface-secondary: #2c2c2e;
  --surface-hover: rgba(255,255,255,0.05);
  --border: rgba(255,255,255,0.1);
  --border-strong: rgba(255,255,255,0.15);
  --text: #f5f5f7;
  --text-secondary: #98989d;
  --text-tertiary: #636366;
  --accent: #0a84ff;
  --accent-hover: #409cff;
  --accent-bg: rgba(10,132,255,0.15);
  --green: #30d158;
  --green-bg: rgba(48,209,88,0.15);
  --yellow: #ffd60a;
  --yellow-bg: rgba(255,214,10,0.15);
  --red: #ff453a;
  --red-bg: rgba(255,69,58,0.15);
  --purple: #bf5af2;
  --purple-bg: rgba(191,90,242,0.15);
  --orange: #ff9f0a;
  --orange-bg: rgba(255,159,10,0.15);
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.2);
  --shadow: 0 2px 8px rgba(0,0,0,0.3);
  --shadow-lg: 0 8px 30px rgba(0,0,0,0.4);
  --shadow-xl: 0 20px 60px rgba(0,0,0,0.5);
}

/* ─── Reset ─── */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  line-height: 1.47;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

/* ─── Layout ─── */
.container { max-width: 1120px; margin: 0 auto; padding: 0 28px; }

/* ─── Header ─── */
header {
  background: rgba(245,245,247,0.72);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
}
[data-theme="dark"] header {
  background: rgba(0,0,0,0.72);
}
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 52px;
}
.identity {
  display: flex;
  align-items: center;
  gap: 10px;
}
.logo {
  width: 28px;
  height: 28px;
  background: linear-gradient(135deg, var(--accent) 0%, var(--purple) 100%);
  border-radius: 7px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 15px;
  font-weight: 700;
}
.identity h1 {
  font-size: 16px;
  font-weight: 600;
  letter-spacing: -0.2px;
}
.identity h1 span {
  color: var(--text-secondary);
  font-weight: 400;
}
.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}
.icon-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: transparent;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-secondary);
  font-size: 16px;
  transition: all 0.2s var(--ease);
}
.icon-btn:hover {
  background: var(--surface-hover);
  color: var(--text);
}
.search-box {
  background: var(--surface-hover);
  border: 1px solid transparent;
  border-radius: var(--radius-sm);
  padding: 6px 12px 6px 32px;
  font-size: 13px;
  width: 220px;
  color: var(--text);
  font-family: var(--font);
  outline: none;
  transition: all 0.2s var(--ease);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23aeaeb2' stroke-width='2' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cpath d='m21 21-4.35-4.35'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: 10px center;
}
.search-box:focus {
  border-color: var(--accent);
  background-color: var(--surface);
  box-shadow: 0 0 0 3px var(--accent-bg);
  width: 280px;
}
.search-box::placeholder { color: var(--text-tertiary); }

/* ─── Stats Bar ─── */
.stats-bar {
  display: flex;
  gap: 6px;
  padding: 20px 0 8px;
  flex-wrap: wrap;
}
.stat {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-secondary);
  background: var(--surface);
  border: 1px solid var(--border);
  white-space: nowrap;
  transition: all 0.15s var(--ease);
  cursor: default;
}
.stat:hover { border-color: var(--border-strong); }
.stat strong {
  font-size: 13px;
  color: var(--text);
  font-weight: 600;
}

/* ─── Navigation ─── */
nav {
  display: flex;
  gap: 2px;
  padding: 10px 0;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}
nav::-webkit-scrollbar { display: none; }
.nav-btn {
  background: none;
  border: none;
  padding: 7px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  color: var(--text-secondary);
  font-family: var(--font);
  transition: all 0.2s var(--ease);
}
.nav-btn:hover { background: var(--surface-hover); color: var(--text); }
.nav-btn.active {
  background: var(--text);
  color: var(--bg);
}

/* ─── Sections ─── */
section { padding: 24px 0 32px; display: none; }
section.active { display: block; }
.section-header { margin-bottom: 24px; }
.section-header h2 {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -0.5px;
}
.section-header p {
  color: var(--text-secondary);
  font-size: 15px;
  margin-top: 4px;
  font-weight: 400;
}

/* ─── Category Groups ─── */
.category-group { margin-bottom: 32px; }
.category-label {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 12px;
  padding-left: 4px;
}

/* ─── Cards Grid ─── */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 10px;
}
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  cursor: pointer;
  transition: all 0.2s var(--ease);
  position: relative;
}
.card:hover {
  box-shadow: var(--shadow);
  border-color: var(--border-strong);
  transform: translateY(-1px);
}
.card:active { transform: translateY(0); }
.card-header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.card-icon {
  width: 36px;
  height: 36px;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
}
.card-icon.workflow { background: var(--accent-bg); }
.card-icon.agent { background: var(--purple-bg); }
.card-icon.command { background: var(--orange-bg); }
.card-icon.context { background: var(--green-bg); }
.card-icon.process { background: var(--accent-bg); }
.card-icon.template { background: var(--yellow-bg); }
.card-icon.learning { background: var(--purple-bg); }
.card-icon.spec { background: var(--green-bg); }
.card-icon.data { background: var(--accent-bg); }
.card-body { flex: 1; min-width: 0; }
.card-title {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: -0.1px;
  line-height: 1.3;
}
.card-desc {
  color: var(--text-secondary);
  font-size: 12px;
  margin-top: 3px;
  line-height: 1.45;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card-footer {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
  flex-wrap: wrap;
}
.card-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.2px;
}
.tag-status-active { background: var(--green-bg); color: var(--green); }
.tag-status-draft { background: var(--yellow-bg); color: var(--yellow); }
.tag-status-placeholder { background: var(--red-bg); color: var(--red); }
.tag-status-refined { background: var(--accent-bg); color: var(--accent); }
.tag-status-has-todos { background: var(--yellow-bg); color: var(--yellow); }
.card-meta-row {
  display: flex;
  gap: 12px;
  font-size: 11px;
  color: var(--text-tertiary);
  margin-top: 8px;
}
.card-meta-row span {
  display: flex;
  align-items: center;
  gap: 3px;
}

/* ─── Side Panel ─── */
.panel-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.3);
  opacity: 0;
  visibility: hidden;
  z-index: 200;
  transition: opacity 0.3s var(--ease), visibility 0.3s;
}
.panel-overlay.open { opacity: 1; visibility: visible; }
[data-theme="dark"] .panel-overlay { background: rgba(0,0,0,0.5); }

.side-panel {
  position: fixed;
  top: 0;
  right: 0;
  width: var(--panel-width);
  max-width: 90vw;
  height: 100vh;
  background: var(--surface);
  box-shadow: var(--shadow-xl);
  z-index: 201;
  transform: translateX(100%);
  transition: transform 0.35s var(--ease);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.side-panel.open { transform: translateX(0); }

.panel-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 24px 24px 16px;
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}
.panel-header-content { flex: 1; min-width: 0; padding-right: 12px; }
.panel-title {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -0.3px;
  line-height: 1.3;
}
.panel-category {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--accent);
  margin-bottom: 4px;
}
.panel-close {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: none;
  background: var(--surface-hover);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-secondary);
  font-size: 16px;
  flex-shrink: 0;
  transition: all 0.15s;
}
.panel-close:hover { background: var(--border); color: var(--text); }

.panel-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px 24px 32px;
  -webkit-overflow-scrolling: touch;
}
.panel-section { margin-bottom: 20px; }
.panel-section-label {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}
.panel-tldr {
  font-size: 15px;
  line-height: 1.65;
  color: var(--text);
  padding: 14px 16px;
  background: var(--surface-secondary);
  border-radius: var(--radius-sm);
  border-left: 3px solid var(--accent);
}
.panel-desc {
  font-size: 14px;
  line-height: 1.6;
  color: var(--text-secondary);
}
.panel-meta-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}
.panel-meta-item {
  background: var(--surface-secondary);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
}
.panel-meta-item .label {
  font-size: 10px;
  font-weight: 600;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.3px;
}
.panel-meta-item .value {
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
  margin-top: 2px;
}
.panel-ref-list { list-style: none; }
.panel-ref-list li { margin-bottom: 4px; }
.panel-ref-list a {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-family: var(--mono);
  padding: 3px 8px;
  border-radius: 5px;
  background: var(--surface-secondary);
  color: var(--accent);
  transition: all 0.15s;
  word-break: break-all;
}
.panel-ref-list a:hover {
  background: var(--accent-bg);
  text-decoration: none;
}
.panel-open-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  background: var(--accent);
  color: white;
  font-size: 13px;
  font-weight: 500;
  border: none;
  cursor: pointer;
  font-family: var(--font);
  transition: background 0.15s;
  text-decoration: none;
}
.panel-open-btn:hover { background: var(--accent-hover); text-decoration: none; }

/* ─── Info Overlay ─── */
.info-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.4);
  z-index: 300;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s var(--ease);
}
.info-overlay.open { opacity: 1; visibility: visible; }
[data-theme="dark"] .info-overlay { background: rgba(0,0,0,0.6); }
.info-modal {
  background: var(--surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  width: 640px;
  max-width: 90vw;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  transform: scale(0.95) translateY(10px);
  transition: transform 0.3s var(--ease);
}
.info-overlay.open .info-modal { transform: scale(1) translateY(0); }
.info-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px 16px;
  border-bottom: 1px solid var(--border);
}
.info-modal-header h2 {
  font-size: 18px;
  font-weight: 700;
  letter-spacing: -0.2px;
}
.info-modal-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px 24px 28px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--text-secondary);
  -webkit-overflow-scrolling: touch;
}
.info-modal-body h3 {
  font-size: 15px;
  font-weight: 600;
  color: var(--text);
  margin: 20px 0 8px;
}
.info-modal-body h3:first-child { margin-top: 0; }
.info-modal-body p { margin-bottom: 8px; }
.info-modal-body ul { margin: 4px 0 12px 18px; }
.info-modal-body li { margin-bottom: 4px; }
.info-modal-body code {
  font-family: var(--mono);
  font-size: 12px;
  background: var(--surface-secondary);
  padding: 1px 5px;
  border-radius: 4px;
}
.info-modal-body .rule {
  display: flex;
  gap: 10px;
  padding: 10px 14px;
  background: var(--surface-secondary);
  border-radius: var(--radius-sm);
  margin-bottom: 8px;
  font-size: 13px;
}
.info-modal-body .rule-icon { font-size: 16px; flex-shrink: 0; }
.info-modal-body .antipattern {
  border-left: 3px solid var(--red);
  padding: 8px 14px;
  background: var(--red-bg);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  margin-bottom: 8px;
  font-size: 13px;
}

/* ─── Process Flow ─── */
.flow-pipeline {
  display: flex;
  align-items: stretch;
  gap: 0;
  padding: 24px 0;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
.flow-stage {
  flex: 1;
  min-width: 130px;
  position: relative;
  display: flex;
  align-items: stretch;
}
.flow-node {
  flex: 1;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px 14px;
  margin: 0 4px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s var(--ease);
}
.flow-node:hover {
  box-shadow: var(--shadow);
  border-color: var(--accent);
  transform: translateY(-2px);
}
.flow-node h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: -0.1px;
  margin-bottom: 4px;
}
.flow-node p {
  font-size: 11px;
  color: var(--text-secondary);
  line-height: 1.35;
}
.flow-node .flow-cmds {
  margin-top: 8px;
}
.flow-node .flow-cmds code {
  display: inline-block;
  background: var(--accent-bg);
  color: var(--accent);
  padding: 2px 7px;
  border-radius: 4px;
  font-family: var(--mono);
  font-size: 10px;
  font-weight: 500;
}
.flow-connector {
  position: absolute;
  right: -6px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
  color: var(--text-tertiary);
  font-size: 12px;
}

/* ─── Integrations ─── */
.integration-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 10px;
}
.integration-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.integration-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.integration-indicator.configured { background: var(--green); box-shadow: 0 0 6px rgba(52,199,89,0.4); }
.integration-indicator.pending { background: var(--yellow); box-shadow: 0 0 6px rgba(255,159,10,0.3); }
.integration-info { flex: 1; }
.integration-name { font-size: 14px; font-weight: 600; }
.integration-desc { font-size: 12px; color: var(--text-secondary); margin-top: 1px; }

/* ─── Gap Cards ─── */
.gap-card {
  border-style: dashed;
  opacity: 0.75;
}
.gap-card:hover { opacity: 1; }
.gap-priority {
  display: inline-flex;
  align-items: center;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.2px;
}
.priority-high { background: var(--red-bg); color: var(--red); }
.priority-medium { background: var(--yellow-bg); color: var(--yellow); }
.priority-low { background: var(--green-bg); color: var(--green); }
.gap-type {
  display: inline-flex;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 600;
  background: var(--purple-bg);
  color: var(--purple);
}

/* ─── Footer ─── */
footer {
  padding: 20px 0;
  border-top: 1px solid var(--border);
  margin-top: 16px;
  font-size: 11px;
  color: var(--text-tertiary);
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
}
footer code {
  font-family: var(--mono);
  background: var(--surface-secondary);
  padding: 1px 5px;
  border-radius: 3px;
  font-size: 11px;
}

/* ─── Responsive ─── */
@media (max-width: 768px) {
  .cards-grid { grid-template-columns: 1fr; }
  .flow-pipeline { flex-direction: column; }
  .flow-connector { display: none; }
  .flow-stage { min-width: auto; }
  .search-box { width: 160px; }
  .search-box:focus { width: 200px; }
  .side-panel { width: 100vw; }
  .stats-bar { gap: 4px; }
  .stat { padding: 4px 10px; font-size: 11px; }
  .info-modal { max-width: 95vw; max-height: 90vh; }
  .panel-meta-grid { grid-template-columns: 1fr; }
}

/* ─── Print ─── */
@media print {
  header { position: static; }
  .icon-btn, .search-box, nav { display: none; }
  section { display: block !important; }
  .side-panel, .panel-overlay, .info-overlay { display: none !important; }
}

/* ─── Scrollbar (Webkit) ─── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-strong); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-tertiary); }
</style>
</head>
<body>

<!-- Side Panel -->
<div class="panel-overlay" id="panelOverlay"></div>
<div class="side-panel" id="sidePanel">
  <div class="panel-header">
    <div class="panel-header-content">
      <div class="panel-category" id="panelCategory"></div>
      <div class="panel-title" id="panelTitle"></div>
    </div>
    <button class="panel-close" id="panelClose" title="Close">&times;</button>
  </div>
  <div class="panel-body" id="panelBody"></div>
</div>

<!-- Info Overlay -->
<div class="info-overlay" id="infoOverlay">
  <div class="info-modal">
    <div class="info-modal-header">
      <h2>About This Repo</h2>
      <button class="panel-close" id="infoClose">&times;</button>
    </div>
    <div class="info-modal-body">
      <h3>What You're Looking At</h3>
      <p>This is the <strong>Ditto Productivity Powerhouse</strong> &mdash; an interactive map of Mewtwo, Ditto Care's AI-powered PM co-pilot. It shows every command, workflow, agent, integration, and knowledge artifact that powers our product development process.</p>

      <h3>How It Works</h3>
      <ul>
        <li><strong>Commands</strong> (<code>/refine-idea</code>, <code>/scope-feature</code>, etc.) are the entry points. Type them in Claude Code to trigger workflows.</li>
        <li><strong>Workflows</strong> are multi-step processes that produce artifacts (specs, tickets, mockups).</li>
        <li><strong>Agents</strong> are specialists (product-designer, user-researcher) dispatched by Mewtwo when their tools are needed.</li>
        <li><strong>Context files</strong> are the knowledge base &mdash; product strategy, brand positioning, design system references.</li>
      </ul>

      <h3>How to Contribute</h3>
      <ul>
        <li>Add new workflows in <code>pm-workspace/workflows/</code></li>
        <li>Add new commands in <code>pm-workspace/commands/</code></li>
        <li>Always update <code>registry/registry.json</code> when creating artifacts</li>
        <li>Spot something missing? Add it to <code>backlog/backlog.json</code></li>
        <li>Regenerate this page: <code>node scripts/generate-dashboard.mjs</code></li>
      </ul>

      <h3>Rules of the Game</h3>
      <div class="rule"><span class="rule-icon">&#x1F3AF;</span><span><strong>Solve real problems.</strong> Every feature must answer: what problem, for whom, how painful?</span></div>
      <div class="rule"><span class="rule-icon">&#x2702;&#xFE0F;</span><span><strong>Less is more.</strong> A sharp 5-line spec beats a 50-line novel.</span></div>
      <div class="rule"><span class="rule-icon">&#x1F4CA;</span><span><strong>Data over opinion.</strong> Prefer evidence. When intuition leads, validate cheaply.</span></div>
      <div class="rule"><span class="rule-icon">&#x1F50D;</span><span><strong>Multi-perspective rigor.</strong> Every spec gets stress-tested from 6 angles: user, dev, strategy, growth, business, privacy.</span></div>
      <div class="rule"><span class="rule-icon">&#x1F504;</span><span><strong>Self-improving.</strong> Feedback loop after every workflow. Learnings get captured.</span></div>

      <h3>Anti-Patterns</h3>
      <div class="antipattern"><strong>Ship without tracking.</strong> Nothing goes out without measurement tickets. No exceptions.</div>
      <div class="antipattern"><strong>Skip multi-perspective review.</strong> Every spec gets reviewed from 6 lenses before it's "done."</div>
      <div class="antipattern"><strong>Build features nobody asked for.</strong> Start with evidence, not assumptions.</div>
      <div class="antipattern"><strong>Write documentation nobody reads.</strong> If it's longer than it needs to be, cut it.</div>
    </div>
  </div>
</div>

<header>
  <div class="container header-inner">
    <div class="identity">
      <div class="logo">D</div>
      <h1>Ditto Productivity Powerhouse <span>&mdash; Mewtwo</span></h1>
    </div>
    <div class="header-actions">
      <input type="text" class="search-box" placeholder="Search..." id="searchBox">
      <button class="icon-btn" id="infoBtn" title="About this repo">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
      </button>
      <button class="icon-btn" id="themeToggle" title="Toggle theme">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" id="themeIconSvg"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      </button>
    </div>
  </div>
</header>

<div class="container">
  <div class="stats-bar" id="statsBar"></div>
  <nav id="mainNav"></nav>
  <main id="mainContent"></main>
  <footer>
    <span>Generated <span id="genTime"></span> &middot; Branch: <code id="genBranch"></code></span>
    <span>Ditto Productivity Powerhouse v2.0</span>
  </footer>
</div>

<script>
const DATA = ${DATA};
const REPO_BASE = ${JSON.stringify(REPO_ROOT)};

// ─── Helpers ───
function esc(s) {
  if (!s) return '';
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function fileLink(path) {
  return 'vscode://file/' + REPO_BASE + '/pm-workspace/' + path;
}
function fileLinkFull(fullPath) {
  return 'vscode://file/' + REPO_BASE + '/' + fullPath;
}
const catIcons = {
  workflow: '\\u2699\\uFE0F', agent: '\\uD83E\\uDD16', command: '\\u26A1',
  context: '\\uD83D\\uDCCB', process: '\\uD83D\\uDCD6', template: '\\uD83D\\uDCC4',
  learning: '\\uD83D\\uDCA1', spec: '\\uD83D\\uDCDD', data: '\\uD83D\\uDCCA',
};
const catLabels = {
  command: 'Command', workflow: 'Workflow', agent: 'Agent',
  context: 'Context', process: 'Process', template: 'Template',
  learning: 'Learning', spec: 'Spec', data: 'Data',
};
const statusLabels = {
  active: 'Active', draft: 'Draft', placeholder: 'Placeholder',
  refined: 'Refined', 'has-todos': 'Has TODOs',
};

// ─── Theme ───
let darkMode = localStorage.getItem('ditto-dark') === '1';
function applyTheme() {
  document.documentElement.setAttribute('data-theme', darkMode ? 'dark' : 'light');
  document.getElementById('themeIconSvg').innerHTML = darkMode
    ? '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>'
    : '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>';
}
applyTheme();
document.getElementById('themeToggle').addEventListener('click', () => {
  darkMode = !darkMode;
  localStorage.setItem('ditto-dark', darkMode ? '1' : '0');
  applyTheme();
});

// ─── Info Modal ───
const infoOverlay = document.getElementById('infoOverlay');
document.getElementById('infoBtn').addEventListener('click', () => infoOverlay.classList.add('open'));
document.getElementById('infoClose').addEventListener('click', () => infoOverlay.classList.remove('open'));
infoOverlay.addEventListener('click', (e) => { if (e.target === infoOverlay) infoOverlay.classList.remove('open'); });

// ─── Side Panel ───
const panelOverlay = document.getElementById('panelOverlay');
const sidePanel = document.getElementById('sidePanel');
function openPanel(item) {
  document.getElementById('panelCategory').textContent = (catLabels[item.category] || item.category).toUpperCase();
  document.getElementById('panelTitle').textContent = item.title;

  let body = '';

  // TL;DR (prominent summary)
  if (item.tldr) {
    body += '<div class="panel-section"><div class="panel-tldr">' + esc(item.tldr) + '</div></div>';
  } else if (item.description) {
    body += '<div class="panel-section"><div class="panel-tldr">' + esc(item.description) + '</div></div>';
  }

  // Metadata grid
  body += '<div class="panel-section"><div class="panel-section-label">Details</div><div class="panel-meta-grid">';
  body += '<div class="panel-meta-item"><div class="label">Status</div><div class="value">' + esc(statusLabels[item.status] || item.status) + '</div></div>';
  body += '<div class="panel-meta-item"><div class="label">Last Updated</div><div class="value">' + esc(item.modified) + '</div></div>';
  body += '<div class="panel-meta-item"><div class="label">Author</div><div class="value">' + esc(item.author) + '</div></div>';
  body += '<div class="panel-meta-item"><div class="label">Category</div><div class="value">' + esc(catLabels[item.category] || item.category) + '</div></div>';
  body += '</div></div>';

  // File path + open button
  body += '<div class="panel-section"><div class="panel-section-label">File</div>';
  body += '<a class="panel-open-btn" href="' + fileLinkFull(item.fullPath) + '" title="Open in VS Code">';
  body += '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>';
  body += esc(item.fullPath) + '</a></div>';

  // References
  const refs = (item.references || []).filter(r => !r.includes(item.path));
  if (refs.length) {
    body += '<div class="panel-section"><div class="panel-section-label">References (' + refs.length + ')</div><ul class="panel-ref-list">';
    refs.forEach(r => {
      body += '<li><a href="' + fileLinkFull(r) + '" title="Open in VS Code">';
      body += '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg> ';
      body += esc(r) + '</a></li>';
    });
    body += '</ul></div>';
  }

  document.getElementById('panelBody').innerHTML = body;
  panelOverlay.classList.add('open');
  sidePanel.classList.add('open');
}
function closePanel() {
  panelOverlay.classList.remove('open');
  sidePanel.classList.remove('open');
}
panelOverlay.addEventListener('click', closePanel);
document.getElementById('panelClose').addEventListener('click', closePanel);
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') { closePanel(); infoOverlay.classList.remove('open'); }
});

// ─── Stats ───
const statsBar = document.getElementById('statsBar');
const statDefs = [
  ['\\u26A1', 'Commands', DATA.stats.commands],
  ['\\u2699\\uFE0F', 'Workflows', DATA.stats.workflows],
  ['\\uD83E\\uDD16', 'Agents', DATA.stats.agents],
  ['\\uD83D\\uDCCB', 'Context', DATA.stats.contexts],
  ['\\uD83D\\uDCD6', 'Processes', DATA.stats.processes],
  ['\\uD83D\\uDCDD', 'Specs', DATA.stats.specs],
  ['\\uD83D\\uDCA1', 'Learnings', DATA.stats.learnings],
];
statsBar.innerHTML = statDefs.filter(s => s[2] > 0).map(s =>
  '<div class="stat">' + s[0] + ' <strong>' + s[2] + '</strong> ' + s[1] + '</div>'
).join('');

// ─── Navigation ───
const sections = [
  { id: 'capabilities', label: 'Capabilities' },
  { id: 'flow', label: 'Process Flow' },
  { id: 'knowledge', label: 'Knowledge Base' },
  { id: 'integrations', label: 'Integrations' },
  { id: 'gaps', label: 'Gaps' },
];
const mainNav = document.getElementById('mainNav');
mainNav.innerHTML = sections.map((s, i) =>
  '<button class="nav-btn' + (i===0?' active':'') + '" data-section="' + s.id + '">' + s.label + '</button>'
).join('');

function showSection(id) {
  document.querySelectorAll('section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  const sec = document.getElementById('sec-' + id);
  if (sec) sec.classList.add('active');
  const btn = document.querySelector('[data-section="' + id + '"]');
  if (btn) btn.classList.add('active');
}
mainNav.addEventListener('click', (e) => {
  if (e.target.classList.contains('nav-btn')) showSection(e.target.dataset.section);
});

// ─── Card Builder ───
function buildCard(item, extra) {
  const icon = catIcons[item.category] || '\\uD83D\\uDCC1';
  const statusCls = 'tag-status-' + (item.status || 'active');
  const statusText = statusLabels[item.status] || item.status || 'Active';

  return '<div class="card' + (extra ? ' ' + extra : '') + '" data-idx="' + item.idx + '" data-title="' + esc(item.title) + '" data-desc="' + esc(item.description) + '" data-path="' + esc(item.path) + '">' +
    '<div class="card-header">' +
      '<div class="card-icon ' + item.category + '">' + icon + '</div>' +
      '<div class="card-body">' +
        '<div class="card-title">' + esc(item.title) + '</div>' +
        '<div class="card-desc">' + esc(item.description) + '</div>' +
      '</div>' +
    '</div>' +
    '<div class="card-footer">' +
      '<span class="card-tag ' + statusCls + '">' + esc(statusText) + '</span>' +
    '</div>' +
    '<div class="card-meta-row">' +
      '<span>' + esc(item.author) + '</span>' +
      '<span>' + item.modified + '</span>' +
    '</div>' +
  '</div>';
}

// ─── Build Sections ───
const mainContent = document.getElementById('mainContent');
let html = '';

// 1. Capabilities
html += '<section id="sec-capabilities" class="active">';
html += '<div class="section-header"><h2>Capabilities</h2><p>The commands, workflows, and agents that power Mewtwo.</p></div>';
for (const cat of ['command', 'workflow', 'agent']) {
  const items = DATA.grouped[cat];
  if (!items || !items.length) continue;
  const labels = { command: 'Commands', workflow: 'Workflows', agent: 'Agents' };
  html += '<div class="category-group"><div class="category-label">' + labels[cat] + '</div><div class="cards-grid">';
  items.forEach(item => { html += buildCard(item); });
  html += '</div></div>';
}
html += '</section>';

// 2. Process Flow
html += '<section id="sec-flow"><div class="section-header"><h2>Process Flow</h2><p>How ideas travel from discovery to learning.</p></div>';
html += '<div class="flow-pipeline">';
DATA.flowStages.forEach((stage, i) => {
  const cmds = stage.commands.map(c => '<code>' + c + '</code>').join(' ');
  html += '<div class="flow-stage">' +
    '<div class="flow-node" data-stage="' + stage.id + '">' +
      '<h3>' + stage.label + '</h3>' +
      '<p>' + stage.desc + '</p>' +
      (cmds ? '<div class="flow-cmds">' + cmds + '</div>' : '') +
    '</div>' +
    (i < DATA.flowStages.length - 1 ? '<span class="flow-connector">\\u203A</span>' : '') +
  '</div>';
});
html += '</div></section>';

// 3. Knowledge Base
html += '<section id="sec-knowledge"><div class="section-header"><h2>Knowledge Base</h2><p>Context, process docs, templates, learnings, specs, and research data.</p></div>';
for (const cat of ['context', 'process', 'template', 'learning', 'spec', 'data']) {
  const items = DATA.grouped[cat];
  if (!items || !items.length) continue;
  const labels = {
    context: 'Context Files', process: 'Process Documentation',
    template: 'Templates', learning: 'Learnings',
    spec: 'Specs & Ideas', data: 'Data & Research',
  };
  html += '<div class="category-group"><div class="category-label">' + labels[cat] + ' (' + items.length + ')</div><div class="cards-grid">';
  items.forEach(item => { html += buildCard(item); });
  html += '</div></div>';
}
html += '</section>';

// 4. Integrations
html += '<section id="sec-integrations"><div class="section-header"><h2>Integrations</h2><p>MCP tool connections and their status.</p></div>';
html += '<div class="integration-grid">';
DATA.integrations.forEach(intg => {
  html += '<div class="integration-card">' +
    '<div class="integration-indicator ' + intg.status + '"></div>' +
    '<div class="integration-info">' +
      '<div class="integration-name">' + esc(intg.name) + '</div>' +
      '<div class="integration-desc">' + esc(intg.desc) +
        (intg.agent ? ' &middot; Agent: ' + esc(intg.agent) : '') +
        (intg.backlogId ? ' &middot; Pending setup' : '') +
      '</div>' +
    '</div>' +
  '</div>';
});
html += '</div></section>';

// 5. Gaps
html += '<section id="sec-gaps"><div class="section-header"><h2>Gaps & Opportunities</h2><p>Backlog items and files with unresolved TODOs.</p></div>';
html += '<div class="category-group"><div class="category-label">Backlog (' + DATA.backlog.length + ')</div><div class="cards-grid">';
DATA.backlog.forEach(bl => {
  html += '<div class="card gap-card" data-title="' + esc(bl.title) + '" data-desc="' + esc(bl.description) + '">' +
    '<div class="card-header">' +
      '<div class="card-icon context">\\uD83D\\uDCCB</div>' +
      '<div class="card-body">' +
        '<div class="card-title">' + esc(bl.title) + '</div>' +
        '<div class="card-desc">' + esc(bl.description) + '</div>' +
      '</div>' +
    '</div>' +
    '<div class="card-footer">' +
      '<span class="gap-priority priority-' + bl.priority + '">' + bl.priority.toUpperCase() + '</span>' +
      '<span class="gap-type">' + esc(bl.type) + '</span>' +
    '</div>' +
    '<div class="card-meta-row"><span>' + bl.id + '</span><span>Added ' + bl.added + '</span></div>' +
  '</div>';
});
html += '</div></div>';

const todoFiles = DATA.items.filter(i => i.hasTodos);
if (todoFiles.length) {
  html += '<div class="category-group"><div class="category-label">Files with TODOs (' + todoFiles.length + ')</div><div class="cards-grid">';
  todoFiles.forEach(item => { html += buildCard(item); });
  html += '</div></div>';
}
html += '</section>';

mainContent.innerHTML = html;

// ─── Card Click → Side Panel ───
document.addEventListener('click', (e) => {
  const card = e.target.closest('.card');
  if (!card || card.classList.contains('gap-card')) return;
  const idx = parseInt(card.dataset.idx);
  if (isNaN(idx)) return;
  const item = DATA.items[idx];
  if (item) openPanel(item);
});

// ─── Flow Node Click ───
document.querySelectorAll('.flow-node').forEach(node => {
  node.addEventListener('click', () => {
    const stage = DATA.flowStages.find(s => s.id === node.dataset.stage);
    if (!stage) return;
    const pseudo = {
      path: '', fullPath: '',
      category: 'workflow',
      title: stage.label,
      description: stage.desc + (stage.workflows.length ? '. Workflows: ' + stage.workflows.join(', ') : '') + (stage.commands.length ? '. Commands: ' + stage.commands.join(', ') : ''),
      author: 'Merlijn van Breugel',
      modified: DATA.meta.generated.split('T')[0],
      status: 'active',
      references: [],
    };
    openPanel(pseudo);
  });
});

// ─── Search ───
const searchBox = document.getElementById('searchBox');
searchBox.addEventListener('input', () => {
  const q = searchBox.value.toLowerCase().trim();
  document.querySelectorAll('.card').forEach(card => {
    const t = (card.dataset.title || '').toLowerCase();
    const d = (card.dataset.desc || '').toLowerCase();
    const p = (card.dataset.path || '').toLowerCase();
    card.style.display = (!q || t.includes(q) || d.includes(q) || p.includes(q)) ? '' : 'none';
  });
});

// ─── Footer ───
document.getElementById('genTime').textContent = new Date(DATA.meta.generated).toLocaleString();
document.getElementById('genBranch').textContent = DATA.meta.branch;
</script>
</body>
</html>`;

writeFileSync(OUTPUT, html, 'utf-8');
console.log('\\nRepo explainer written to: repo-explainer.html');
console.log('Open in browser to view.');
