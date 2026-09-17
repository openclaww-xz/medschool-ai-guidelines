# Medical School & Teaching Hospital AI Usage Guidelines — Research Repo

Systematic collection and analysis of generative-AI usage policies governing medical
education and academic medical centers.

Scope: US MD-granting schools (priority: top teaching hospitals), national frameworks
(AAMC, AMA, LCME, NBME), health-system policies, and peer-reviewed policy research.
International: UK (GMC), Canada (AFMC), Australia (AMC), WHO — secondary priority.

## Layout
```
raw/                  Original source material, one file per source, NEVER edited
  national-frameworks/  AAMC, AMA, LCME, NBME, AMEE, WHO
  us-med-schools/       Per-school policies (Stanford, Keck, Buffalo, HMS, ...)
  health-systems/       Hospital / health-system policies (HopGPT, UCSF, ...)
  peer-reviewed/        Full-text (PMC) of policy studies & surveys
  international/        GMC, AFMC, AMC, non-US med schools
metadata/             source.json entries: url, title, publisher, date, sha256, license
pdf/                  PDF snapshots where available
index.md              Master index of all collected sources
agents/               Agent task definitions and per-run logs (one file per agent run)
README.md             This file
```

## Conventions
- Raw files: `<slug>.md` or `<slug>.pdf`, slug = `school-or-org--doc-name`.
- Each raw file gets a matching entry in `metadata/sources.json`.
- Raw content is immutable once saved; corrections go in metadata notes.
- Agent runs log to `agents/run-NN.md` with: subagent id, sources fetched, sha256, result.

## Method
1. Seed list from initial web sweep (Stanford, Keck, Buffalo, HMS, AAMC, HopGPT, SGIM, PMC surveys).
2. Enumerated US MD-granting schools (AAMC / US News research ranking frame) in per-school batches
   (runs 2–8, 12–13, 16–18), plus DO and HBCU schools (run 18).
3. Per-school web search: `<school> generative AI policy medical students handbook`; absences
   verified and recorded as data in per-run `no_policy_found` lists.
4. Saved raw policy text (markdown extract) + PDF snapshot (`pdf/`, 63 files) where offered;
   metadata (url, sha256, license) in `metadata/sources.json` for all 365 sources.
5. Collected national frameworks (AAMC/AMA/LCME/NBME/ACP/FSMB/AMEE/WHO), health systems attached to
   each school, peer-reviewed full texts (PMC), and international comparators (GMC, AFMC, AMC,
   Singapore MOH AIHGle, Sydney/Karolinska/Toronto university policies) — runs 1–9, 14.
6. Analyzed in R (`analysis/figures.Rmd`): 161-document clause matrix (`analysis/clauses.csv`)
   covering banned/permitted uses, PHI, disclosure, assessment, secure tools, enforcement, AAMC
   alignment; two independent audits (run-11, run-21; 198/202 OK, 98%).
7. Synthesis: **[analysis/REPORT.md](analysis/REPORT.md)** — the flagship deliverable, with every
   claim cited to a file path.

## Key outputs

- **[analysis/REPORT.md](analysis/REPORT.md)** — flagship synthesis (landscape, policy typology,
  PHI/assessment clause analysis, GME–UME gap, international contrast, adoption timeline,
  AAMC-alignment paradox, drafting guidance).
- [analysis/findings.md](analysis/findings.md) · [analysis/summary-stats.md](analysis/summary-stats.md) ·
  [analysis/clauses.csv](analysis/clauses.csv) · figures in `analysis/figs/`.
- [index.md](index.md) — master index of all 365 sources.
