# Agent collection instructions (read fully before starting a run)

## Goal
Collect ORIGINAL source material on medical-school / teaching-hospital AI usage
guidelines into this repo. Raw full contents, not summaries.

## Hard rules
1. NEVER edit files under raw/ that already exist. Create new files only.
2. One source = one file under raw/ in your assigned subdirectory.
   File naming: `<org-slug>--<doc-short-name>.md` (lowercase, hyphens).
3. Do NOT touch metadata/sources.json, index.md, or README.md — parent merges those.
   Instead write your run report to `agents/run-<NN>-report.md` (NN = your run number).
4. Each raw .md file must start with a YAML front-matter block:

```
---
source_url: "https://..."
title: "..."
publisher: "..."
published_date: "YYYY-MM-DD or unknown"
accessed_date: "YYYY-MM-DD"
license: "e.g. public web page / copyright, fair-use excerpt / CC-BY"
sha256: "<sha256 of this file body computed after save, may be added by parent>"
---
```

Then the full extracted text of the document.

5. For PDFs (AAMC downloads, policy PDFs): save binary to pdf/<slug>.pdf AND
   extract text to raw/<category>/<slug>.md with the same front-matter.
6. PubMed/PMC articles: fetch full text from PMC (pmc.ncbi.nlm.nih.gov), not just
   the abstract. Use the PMC "Format: ... XML/PDF" or print view if needed.
7. Verify before claiming: check the saved file is non-empty and contains the
   policy substance (not a nav menu or cookie banner). If a page fails
   (403/429/paywall), retry once with a different strategy, then record the
   failure in your report and move on. Do not fabricate content.
8. After each batch of saves, `git add raw pdf agents` and commit with message
   `run-NN: collect <short description>`. Do NOT push (parent pushes).

## Run report format (agents/run-<NN>-report.md)
```
# Run NN report
Agent scope: <schools/orgs assigned>
Sources saved:
- raw/<path> | <title> | <url> | OK/partial
Failures:
- <url> | <reason>
Notes: <anything the parent should know>
```

## Search recipe
- `<school name> generative AI policy medical students`
- `site:<school med domain> AI policy handbook`
- also check: academic integrity office pages, residency/GME pages, health system IT pages
- A policy counts if it governs AI use by medical students, residents, or
  clinical faculty in education/clinical-documentation contexts.
