# Run 11 — Independent Verification Audit

Date: 2026-09-17. Auditor: run-11 subagent (no involvement in collection runs 01–10).
Scope: all 202 raw/*.md files, 42 pdf/*.pdf binaries, cross-checks against agents/run-04..09-report.md, index.md (202 entries), metadata/sources.json (202 entries).

## Method
- Static scan (scripted): YAML front-matter completeness (source_url, title, publisher, accessed_date), suspicious markers (access denied / enable JavaScript / sign in / captcha / cookie-banner), real-text length (markdown links & symbols stripped), nav-heaviness (>40% of non-blank lines are bare links), exact-body sha256 dedupe across all files, same-source_url-multiple-files check, same-org pairwise line-Jaccard ≥ 0.6 near-dup check.
- Dynamic: HTTP status for a random (seed 11) sample of 25 source_urls; 3xx/200 = OK. The 3 non-200s browser-verified.
- PDFs: random sample of 5 — %PDF magic bytes, size, page count, pypdf text extraction of page 1. Additionally all 42 PDFs checked for magic bytes + ≥20KB (the "HTML error page saved as .pdf" failure mode).
- Report cross-check: every "no_policy_found" / "Failures" claim in run-04..09 reports checked against the current index and raw/ tree.

## Results

| Check | Result |
|---|---|
| Front-matter completeness | 202/202 have source_url, title, publisher, accessed_date |
| Substantive body (≥500 chars real text, no shell markers) | 198 OK, 4 SUSPECT (below) |
| Marker scan ('Access denied', 'Enable JavaScript', captcha, login walls) | 0 hits in any body |
| Exact-body duplicates / same-URL two files | 0 / 0 |
| Same-org near-duplicates (Jaccard ≥ 0.6) | 0 |
| URL sample (25 random) | 22×200, 3×403 — all 3 verified LIVE in real browser (bot-walls vs plain HTTP clients) |
| PDFs (5 random deep + all 42 magic/size) | 5/5 extractable text, 42/42 %PDF + >100KB |
| no_policy_found cross-check | No contradictions (see below) |
| index.md vs raw/ tree | 202 = 202, full match |

## SUSPECT files (4)

1. `raw/health-systems/uf-health--ai-governance.md` — **nav-menu shell**. Body is "Skip to main content", Recite Me banner, then a list of UF offices (Registrar, IRB, Title IX…) with zero policy text. The real AI-governance content was never captured. Worst file in the corpus.
2. `raw/health-systems/uw-medicine--ai-in-healthcare-policy.md` — landing stub (~397 chars): one purpose sentence + links to COMP.308/Glossary. Not the policy itself; the substantive COMP.308 policy IS captured separately (comp308 file, OK). Redundant shell page.
3. `raw/health-systems/mayo-clinic--genai-tools-overview.md` — thin overview tab (~334 chars); run-06 itself labeled it "partial — landing page". Weak but not fabricated.
4. `raw/us-med-schools/msu--ethics-genai-overview.md` — thin overview (~344 chars); companion student-guidance file has the substance.

No fabrication indicators anywhere: no invented policy text, no shell pages pretending to be policy (the UF file is a shell but is not disguised), no error pages saved as content, sha256 front-matter backfill present on run-04 files as claimed.

## URL check failures (3) — all resolved as bot-walls, not dead links
- `https://provost.harvard.edu/guidelines-using-chatgpt-and-other-generative-ai-tools-harvard` → 403 to plain client; browser renders full page ("Dear Members of the Harvard Community…"). Live.
- `https://icahn.mssm.edu/about/artificial-intelligence/safety` → 403 to plain client; browser renders "AI Governance and Safety | Icahn School of Medicine". Live.
- `https://icahn.mssm.edu/files/.../AI-Policy.pdf` → 403 to plain client; same Akamai wall run-06 documented; PDF is present in pdf/ with valid %PDF magic + extractable text.

## no_policy_found cross-check
- run-04 (HMS, UCLA DGSOM, JHUSOM): consistent — university/IT-level docs saved instead; no missing school claimed collected.
- run-05 (WashU, NYU Langone, NM, Duke SOM, Michigan): consistent. Michigan Medicine KB guideline IS in corpus (umich-medical-school--acceptable-ai-use-guideline.md, 12.4K chars substantive). Run-05's warning that two AAMC PDFs were 3KB HTML error stubs is **resolved**: both are now real PDFs (196KB / 6.4MB, valid magic).
- run-06 (Mayo Alix, Emory SOM, UTSW, UW): consistent; Mayo proxy docs present.
- run-07 (Baylor St. Luke's, UPMC, OSU Wexner, UW Health, M Health Fairview, VUMC SOM): consistent — absence claims, nothing claimed collected is missing.
- run-08 (DMU handbook, PCOM, Iowa Carver): consistent; closest-doc saves present.
- run-09 (Charité, AMC Australia, Temerty, India NMC, KI): consistent. Run-09's flagged duplicate (uw-gme file in two dirs) was **resolved** at merge commit 08e6e74 ("dedupe 3 duplicate-URL files"); no same-URL duplicates remain.

## Verdict
**Corpus is trustworthy.** 198/202 OK (98%). The 4 suspect files are over-collection of thin landing pages, not fabrication; only the UF Health file is truly worthless (nav shell) and should be re-fetched or dropped at merge. Link rot risk is low; provenance discipline (front-matter, run reports, honest failure notes, absence-as-data records) is unusually good. All reporter claims that could be verified checked out, including two issues (AAMC stubs, uw-gme dupes) that were already fixed by the parent's dedupe merge.

Machine-readable detail: `agents/run-11-audit.json` (per-file verdicts, URL-check results, PDF checks, near-dup scan).
