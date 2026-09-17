# UW Medicine — COMP.308 Use of Artificial Intelligence (+ Glossary 308.G1)

**Classification: pioneer — governance-instrument tier** (run-30 health systems Tier 1; `analysis/deep-reading/30-health-systems-synthesis.md`)

## Who drove it

A formal compliance instrument: **UW Medicine Compliance** policy COMP.308, **signed by Beth DeLair, Chief Compliance Officer, UW Medicine; Associate Vice President for Medical Affairs** (approval 8/26/2026, effective 2026-09-01, next review 2029) (`raw/health-systems/uw-medicine--comp308-use-of-ai.md`; `analysis/deep-reading/uw-medicine--comp308-use-of-ai.md`). Review bodies named in the policy: **AI Use Case Review Council**, **AI Education Review Workgroup** (learner-use cases), **AI Operations Subcommittee** (escalation tier), plus UW IRB/Human Subjects Division, Information Security, and contracting teams including the Attorney General's Office. The companion Glossary (Guidance 308.G1, V5.0, revised 8/25/2026) has **named faculty authors** — "Primary Author: Jason Lau. Contributors: Ana Anderson, Trevor Cohen, Noah Hoffman, Michael Leu, Chen Liang, Gang Luo, Angad Singh, Peter Tarczy-Hornoch, Jennifer Slyker, Karen Segerson" — a biomedical-informatics authorship group writing an operational glossary (`raw/health-systems/uw-medicine--ai-policy-glossary-308g1.pdf.md`).

## Institutional context

A multi-entity academic health system (Harborview, UWMC, Airlift Northwest, UW Physicians, SoM, WWAMI) with compliance-office infrastructure able to issue signed, dated, versioned policy that binds all entities — and a biomedical-informatics faculty bench deep enough to author the definitions. The glossary cites the literature (Cohen/Patel/Shortliffe textbook; Howell BMJ Quality & Safety 2024), signaling an academic department invested in operational artifacts.

## What they built and why it is pioneer-grade

1. **The best policy instrument in the corpus**: "signed by the Chief Compliance Officer... a 12-item elevated-risk trigger screen... three review bodies... contract/BAA/security gates with periodic security reassessment, an Approved AI Tool/Application List" (run 30). The trigger screen is the heart — any of: patient-facing unvalidated output; direct patient interaction; PHI/de-identified/UW-data exposure; clinical automation; billing impact; **union labor impact** ("fundamentally changes the work functions of represented (unionized) staff or trainees"); **>$100,000 spend**; academic-selection impact; **equity/accessibility impacts via the Equity Impact Review Tool**; change-management load — routes the use case into review unless it's on the approved list.
2. **An explicit low-risk allowlist with named examples**: public chatbots for summarizing published papers; DALL-E/NanoBanana for slide images; CoPilot for meeting agendas; LangChain on open-weight models for public data; self-tutoring — "pragmatic and current" (run 30). Governing by published example prevents both over-review and chill.
3. **Learner authorization overlay (Section E)**: even approved or low-risk tools require program/supervisor/instructor authorization for coursework, assessments (a dozen named assessment types), exams and degree milestones, and the clinical learning environment — the education layer sits on top of the security layer rather than duplicating it.
4. **The 46-term faculty-authored glossary** (308.G1) — definitions from Accuracy (with sensitivity/specificity/PPV/AUC/PR-curve) through Bias, Ground Truth, and beyond, "that makes the triggers enforceable" (run 30). A policy that defines AUC in its own attachment cannot be accused of vagueness.
5. **Contract machinery**: agreements "only... executed with appropriate... delegation of authority after the proposed AI use undergoes internal review"; existing agreements "may need to be amended if AI functionality is incorporated after initial execution"; BAAs/DUAs/DPAs by data type; IT Security Terms with AI and accessibility exhibits; the Honest Broker de-identification certification pathway; and an IRB expansion — HSD "has expanded the definition of human research to include the use of data that is at high risk of re-identification."

## What they explicitly chose NOT to do

- No prohibition default: unlisted low-risk uses proceed without review (the enumerated eight).
- No detection or integrity enforcement in this instrument — Section E defers to program-level authorization and the Student Conduct Code.
- No clinical-performance monitoring program (only security reassessment is periodic) — "monitoring partial" per run 30; performance surveillance is the one leg UW lacks vs Duke/MSHS/UCSF.
- Fred Hutchinson carve-out: the policy explicitly does not apply to the affiliated cancer center — scope honesty rather than pretended universality.

## Borrowed vs original

Original in the corpus: the union-labor trigger, the $100k threshold, the Equity Impact Review Tool hookup, the Honest Broker certification pathway, the IRB re-identification expansion, and the glossary itself. The approved-list-plus-triggers architecture parallels Duke's registry/tiering (convergent evolution; no citation either way). Run 30's structural finding: "Compliance-owned (UW) documents read as enforceable instruments" — governance locus predicts genre.

## Weaknesses / what's missing

- **Clinical-performance monitoring** is the missing leg — no IMPACC/ABCDS-style post-deployment surveillance named (run 30 verdict table).
- Consent/ambient-scribe rules absent from this instrument.
- Liability fully devolved to users ("Users are responsible for reviewing outputs") — no enterprise accountability language (a corpus-wide pattern; run 30, finding 3).
- Three-year review cycle (2029) may be too slow for the technology; no incident-suspension mechanism in this document.

## What to steal concretely

1. **The 12-item trigger screen** — especially the three no one else has: union-labor impact, $100k spend threshold, equity/accessibility impacts via a named review tool. Copy the list wholesale.
2. **The published low-risk allowlist with named examples** — governance without chill; tell people exactly what they may do without asking.
3. **A faculty-authored glossary as a policy attachment** — definitions with metrics (AUC, sensitivity/specificity) make every trigger and clause contestable on shared terms. Have your informatics faculty write it and put their names on it.
4. **Learner-authorization overlay** — the clean division: enterprise security decides *where data may go*; programs decide *whether the use is educationally legitimate*.
5. **Contract-amendment clause** for AI functionality added post-signature — the vendor upsell loophole, closed.
6. **IRB re-identification expansion** — extend human-subjects review to high-re-identification-risk data uses by policy.
