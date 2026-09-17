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
1. Seed list from initial web sweep (already collected: Stanford 3.33, Keck, Buffalo, HMS, AAMC, HopGPT, SGIM position statement, PMC surveys).
2. Enumerate the full US MD school list (AAMC / US News research ranking as frame).
3. Per-school web search: `<school> generative AI policy medical students handbook`.
4. Save raw policy text (markdown extract) + PDF snapshot where offered; record metadata.
4b. Health systems attached to each school (teaching hospital side).
5. Analyze: coverage, banned/permitted/PHI clauses, assessment rules, secure-tool mandates, dates.

## Budget
50 agent runs, 5 concurrency. Reserve ≥10 runs for verification/audit pass.
