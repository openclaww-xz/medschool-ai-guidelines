# Run 19 report — REPAIR audit-flagged files

Agent scope: repairs flagged in run-11-audit.md (4 suspect files) + run-15/parent suspect list items (ki.se re-fetch, Georgetown Box archive check, bu-chobanian rename check).

## Replacements (git rm + re-add with corrected full content)

- raw/health-systems/uf-health--ai-governance.md | RE-PLACED. Was a 404-char nav shell (worst file per run-11). Re-fetched https://privacy.health.ufl.edu/laws-and-regulations/ai-governance/ via real browser rendering (plain HTTP clients get only the nav shell; JS render yields 5,290 chars). New body (~4.7K chars substantive) covers: Generative AI definition/LLMs, privacy & security risks (FERPA/HIPAA-class restricted data prohibitions), responsible-use requirements (enterprise licensing, Integrated Risk Management risk assessment), AI meeting-transcription rules, FIPA/FERPA/HIPAA/COPPA/GDPR/EU-AI-Act compliance section, intellectual property risks. Nav/footer chrome stripped. OK.
- raw/us-med-schools/msu--ethics-genai-overview.md | RE-PLACED. Was thin (344 chars, intro paragraph only). Re-fetched https://ethics.msu.edu/gen-ai live (200) and captured the FULL page: MSU AI Ethical Values (Collaboration, Equity, Excellence, Integrity, Respect) and 7 Themes (human agency, non-discrimination, robustness, privacy, transparency, wellbeing, accountability). Page is genuinely short (~3K chars) but this is now its complete content, not an excerpt. OK.

## Removals

- raw/health-systems/uw-medicine--ai-in-healthcare-policy.md | git rm'd. Was a redundant landing stub (397 chars: purpose sentence + links). Re-fetched live to confirm the page contains nothing beyond the stub text. The substantive COMP.308 policy is already fully captured in raw/health-systems/uw-medicine--comp308-use-of-ai.md (19.9K chars, pdf/ twin present).

## New sources

- raw/health-systems/uw-medicine--ai-policy-glossary-308g1.pdf.md | NEW. UW Medicine AI Policy Glossary, Guidance 308.G1 V5.0 (rev 2026-08-25), 9-page PDF linked from the removed stub page. Saved binary to pdf/uw-medicine--ai-policy-glossary-308g1.pdf (366KB, valid PDF 1.7, 9 pages, 22.9K chars extractable). Completes the UW Medicine policy set (COMP.308 + glossary).

## Checked, no action needed

- Task 4 — Karolinska ki.se re-fetch: ki.se is STILL DOWN ("tillfälligt stängd på grund av tekniskt underhåll" maintenance page, verified via real browser for staff.ki.se/tools-and-support/ai-at-ki/generative-ai-and-education and via curl for staff.ki.se/media/169551/download — both serve only the maintenance notice in Swedish/English, no policy content). Existing Internet Archive captures (raw/international/karolinska--generative-ai-and-education.md, raw/international/karolinska--student-guidelines-generative-ai.md) remain the best available versions. No change made.
- Task 5 — Georgetown SOM AI policy (https://georgetown.box.com/s/tm95s608473mngydj69vlkyda1jwxkon): Internet Archive checked via browser playback — Wayback reports "The Wayback Machine has not archived that URL" (CDX API was 429/offline during the run, playback host gave a definitive negative). Box share is SSO-gated and unarchived → RECORD AS PERMANENTLY GATED. University-wide substitute (aiguidelines.georgetown.edu) already in corpus from run-12.
- Task 6 — pdf/bu-chobanian--md-program-ai-use-policy.pdf twin check: raw/us-med-schools/bu-chobanian--md-program-ai-use-policy.pdf.md stem exactly matches pdf/bu-chobanian--md-program-ai-use-policy.pdf. All 5 .pdf.md files in raw/ match their pdf/ twins' stems (baylor-cm, geisel-dartmouth, pitt-som, vanderbilt-som checked too). NO rename needed — parent already fixed the pdf/ side.

## Failures

- (none blocking) Internet Archive CDX API returned 429/offline during this run; definitive Wayback check done via browser playback instead.
- ki.se remains offline; KI files stay as Wayback-sourced versions (noted in their front-matter license field).

## Notes for parent

- index.md / metadata/sources.json NOT touched (per instructions) — parent must: (1) drop the uw-medicine--ai-in-healthcare-policy.md entry, (2) add the new uw-medicine--ai-policy-glossary-308g1.pdf.md entry, (3) mark Georgetown Box link as permanently gated in any absence record.
- The UF Health page renders client-side only: any future re-fetch must use a real browser, not curl.
