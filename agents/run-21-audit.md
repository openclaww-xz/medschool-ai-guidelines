# Run 21 — Independent Verification Audit, Round 2

Date: 2026-09-17. Auditor: run-21 subagent (independent of collection runs 12–19).
Scope: the **164 raw/*.md files added after run-11** (identified via `git log --diff-filter=A f52b4f1..HEAD -- raw/`, minus run-11's audited set; 171 added − 7 run-11-audited repairs = 164), the **20 PDFs added since run-11**, and a **re-check of the 4 run-11 SUSPECT files** after run-19 repairs. `raw/` untouched.

## Method
Identical protocol to run-11: scripted YAML front-matter completeness (source_url/title/publisher/accessed_date); substance markers (access denied, enable JavaScript, captcha, login walls); real-text length (links/nav stripped; <500 chars = SUSPECT); nav-heaviness (>40% bare-link lines); sha256 exact-body dedupe and same-source_url multi-file check; 20 random live URL checks (seed 21, curl -L, browser verification of non-200s); %PDF magic bytes + size + pypdf page/text probe for every new PDF.

## Results

| Check | Result |
|---|---|
| Front-matter completeness | 164/164 have source_url, title, publisher, accessed_date |
| Shell markers ('Access denied', 'Enable JavaScript', captcha, login walls) | 0 hits in 164 bodies |
| Substantive body (≥500 real chars) | 159 OK, 5 SUSPECT (below) |
| Exact-body duplicates | **1 pair — Tufts (below)** |
| Same source_url in two files | 0 |
| Nav-shell ratio | 0 flagged |
| URL sample (20 random + 3 forced rechecks) | 22×200, 1×403 — bot-wall, **browser-verified LIVE** |
| New PDFs (20/20 magic + size + probe) | 20/20 valid %PDF, 89KB–4.7MB; 1 minor flag (below) |

## SUSPECT files (5) — all thin-but-real, none fabricated

1. `raw/us-med-schools/touro-tuncom--libguide-ai-in-medical-education.md` — 257 chars. Libguide pointer: 2 sentences referencing the TUS Academic Integrity Policy. Not policy text.
2. `raw/us-med-schools/atsu-kcom--policies-page.md` — 274 chars. Generic ATSU policies index; one intro sentence + handbook PDF link. No AI content.
3. `raw/us-med-schools/wayne-state-som--md-handbook-ai-guidelines-usage-policy-announcement.md` — 355 chars. News announcement *about* the AI policy, not the policy (handbook PDF captured separately).
4. `raw/us-med-schools/drexel--provost-ai-policies.md` — 363 chars. Lists "PO 103: Academic Integrity Pertaining To AI" by name only; no policy text.
5. `raw/us-med-schools/uconn-health--guidance-on-using-ai.md` — 397 chars. Placeholder page ("this page will host information…"). The substantive v20240314 PDF *is* separately captured (104KB, 2,390-char probe, OK).

All five URLs are real and live-pattern; these are honest over-collections of pointer pages, same failure mode run-11 found — **not fabrication**.

## NEW FINDING — Tufts exact-duplicate bodies (site-side)

`raw/us-med-schools/tufts-university--it-guidance-using-ai.md` and `tufts-university--it-guidelines-use-genai-tools.md` have **byte-identical rendered bodies**. Verified live: `it.tufts.edu/guidelines-use-generative-ai-tools` redirects to `/ai/guidance-using-ai-tufts` — both front-matter URLs return 200 for the same page. Faithful double-capture of a redirect pair; **drop one at merge** (keep `guidance-using-ai-tufts`, the canonical final URL). Different source_urls, so run-11's URL-dedupe wouldn't have caught it.

## URL check failure (1) — bot-wall, not dead

- `https://tech.utexas.edu/governance/guidance-for-ai` → 403 to curl; **real browser renders the full page** ("Guidance for Using Artificial Intelligence | Enterprise Technology", substantive governance text). Live. Same Akamai-style wall pattern as run-11's 3 non-200s.

All other 22 sampled URLs (PMC peer-reviewed, Rutgers IT, WVSOM, Drexel IT, UCSD, OU, Morehouse, SHSU, Nebraska Medicine, BMC PDF, NITRD PDF, etc.) returned 200.

## PDF checks (20 new since run-11)

All 20 have `%PDF` magic, 89KB–4.7MB, page counts 1–279. One minor flag:
- `pdf/wake-forest-som--md-student-handbook.pdf` — 64pp, 643KB, valid magic, but **page-1 text probe = 0 chars** (image-based cover). Companion policy PDF (279pp) extracts fine. Likely scanned-handbook; OCR only if the AI-policy section is image-only. Not a fabrication signal.

## Re-check: 4 run-11 SUSPECT files after run-19 repairs

| File | Run-11 | Run-21 |
|---|---|---|
| `uf-health--ai-governance.md` | SUSPECT (nav shell, "worst file") | **OK — REPAIRED.** ~4.7K substantive chars: restricted-data prohibitions, IRM risk assessment, AI meeting-transcription rules, FIPA/FERPA/HIPAA/COPPA/GDPR/EU-AI-Act, IP risks. URL live (200). |
| `uw-medicine--ai-in-healthcare-policy.md` | SUSPECT (landing stub) | **OK — REMOVED.** Confirmed absent from tree; COMP.308 full policy remains + new 308.G1 glossary PDF (366KB, 9pp, extractable). Set complete. |
| `msu--ethics-genai-overview.md` | SUSPECT (thin) | **OK — REPAIRED.** Full page: 5 ethical values + 7 themes. Page is genuinely short but complete. URL live (200). |
| `mayo-clinic--genai-tools-overview.md` | SUSPECT (thin tab) | **OK-ish.** Now carries Mayo-specific guidance (clinical-judgment caveats, approved-tools entry); still a libguide overview, not policy. Downgraded from SUSPECT with caveat. |

Run-19's repair claims all verified against the actual files — no repair was claimed but not done.

## Verdict

**Corpus remains trustworthy; audit round 2 passes.** 159/164 new files OK (97%), 0 fabrication indicators, 0 shell/error pages, front-matter discipline held across all collection runs. Two real actions for the parent at next merge:

1. **Dedupe the Tufts pair** (identical bodies; site redirect) — keep `tufts-university--it-guidance-using-ai.md`.
2. Optionally re-fetch or drop the 5 thin pointer files (only ATSU and Touro are truly worthless; Wayne State, Drexel, UConn each have substantive companions already in corpus).

Link rot low (22/23 plain-HTTP OK, 1 bot-wall verified live). Run-19 repairs genuine and complete. Machine-readable detail: `agents/run-21-audit.json`.
