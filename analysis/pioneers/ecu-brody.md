# ECU Brody School of Medicine — Responsible Use of Artificial Intelligence (v1.1)

**Classification: pioneer — reference implementation of the tiered model** (run-28 cohort B rank #1; `analysis/deep-reading/28-cohortB-synthesis.md`)

## Who drove it

An Educational Affairs Committee-approved SOP with full document control: "Version 1.1; Implementation Date March 1, 2026; Approval by EAC February 25, 2026; Expiration Date February 25, 2029," owned by the **Office of Medical Education, with Compliance and IT Security** (`raw/us-med-schools/ecu-brody--responsible-use-of-ai.md`; `analysis/deep-reading/ecu-brody--responsible-use-of-ai.md`). Three governance facts are unusual: (1) the policy carries an **expiration date** — it sunsets unless affirmatively renewed; (2) a 36-month review cycle "or sooner if platform or regulatory changes occur"; (3) an **emergency-amendment procedure** (OME interim updates notified within 5 business days and logged). The drafting coalition — education + compliance + IT security jointly — is exactly the triad most schools fail to assemble.

## Institutional context

ECU Brody is a public state school serving eastern North Carolina — not an elite private with a research-computing stack. The enabling context is procedural, not infrastructural: an existing educational-policy SOP apparatus (versioning, EAC approval, related-policy cross-references to ECU's AI-systems regulation, HIPAA regulation, and faculty manual), and a Microsoft campus agreement making **Copilot the free approved-tool floor** ("Microsoft Copilot meets the baseline access requirement"). The 2026 vintage also means ECU drafted *after* the early cohorts' texts circulated — it visibly learned from the field (its tier structure systematizes what UCSF PharmD began and what run-28 peer GW left unsystematized).

## What they built and why it is pioneer-grade

The **complete tiered implementation**, end to end:

- **Universal tier labels**: "Every graded assignment must list its AI tier (Level 1, 2, or 3) in syllabi, LMS, or verbally" — Level 1 open use (no disclosure), Level 2 conditional use with a **Methods Note**, Level 3 prohibited. Disclosure burden scales with stakes ("Proportionality – Disclosure should match assignment stakes").
- **The Methods Note** — the most usable disclosure artifact in the corpus: three elements ("Tool used, what AI generated, one verification step") with a worked example: "Tool: Copilot; AI drafted slides; verified dosing vs ADA 2024."
- **Faculty parity including grading governance**: identical tiers apply to faculty; Level 3 (faculty) bans autonomous grading, AI-determined pass/fail, releasing unreviewed AI feedback, and uploading OSCE cases/exam items/student work; narrative-feedback drafting is Level 2 with mandatory human review.
- **Equity of access as an enforceable principle**: "Students must have free access to one approved tool" plus a duty to "provide equivalent non-AI learning options when AI use is encouraged."
- **Oral-defense integrity**: faculty may request "a short oral defense of understanding, comprehension, or reasoning" or a process artifact — assessment-based integrity instead of surveillance.
- **Verification keyed to function, not tools**: verification is required "when AI adds or changes factual, quantitative, or clinical content," exempt for grammar/formatting — resolving the grammar-tool divergence that incoherently splits the rest of the corpus (`analysis/deep-reading/28-cohortB-synthesis.md`, cross-cohort observations).

## What they explicitly chose NOT to do

- No AI detection anywhere — integrity runs through tiers, Methods Notes, and oral defense.
- No tool-by-tool enumeration of permissions; tools are approved/Non-Approved by IT/Compliance, with a hard floor: "Until PHI-approved tools exist, assume no PHI entry is permitted."
- No blanket ban option for faculty; and symmetrically no blanket permission — the tier must be *declared*.
- Research uses are excluded outright ("governed by separate IRB and research integrity policies") — a deliberate scope cut rather than an omission.

## Borrowed vs original

The tier concept has lineage (UCSF PharmD's AI-1..4 as the classification ancestor; traffic-light language from ECU's own prior version — the "Green = Level 1; Yellow = Level 2; Red = Level 3" disclaimer documents in-policy evolution). Original: the Methods Note, faculty grading-governance tiers, the equity floor with non-AI alternatives, oral defense as integrity mechanism, the expiration date, and the near-PHI defined term. Run 28's verdict: "the reference implementation of the tiered model."

## Weaknesses / what's missing

- Tier discipline depends on faculty actually declaring tiers; the mandate exists but no auditing mechanism is described (run 28: "tier discipline decays if declarations lapses").
- Clinical-environment depth trails Buffalo (no supervision framework, no BAA requirement for site tools; `analysis/deep-reading/28-cohortB-synthesis.md`, ranking §3).
- No external scholarly citations; no disclosure-culture apparatus (contrast GW's AMEE-derived templates).
- Away-rotation compliance duty is one line — outside-institution AI policies are flagged but not operationalized.

## What to steal concretely

1. The **three-tier system with mandatory per-assignment declaration and ready-to-paste syllabus language** — run 28's model verdict says tiering "dominates on every evaluation axis that matters."
2. The **Methods Note** (tool / what AI generated / one verification step) as the universal disclosure instrument.
3. **Faculty grading-governance tiers** — ban autonomous grading *by rule*, with the one-line syllabus disclosure: "AI may assist instructors in drafting narrative feedback; final grades and comments are determined by the instructor after human review."
4. **Equity floor + non-AI alternatives** as paired duties — the least-diffused mature element in the corpus (`analysis/deep-reading/28-cohortB-synthesis.md`).
5. **Policy expiration date + emergency-amendment procedure** — governance hygiene that forces re-authorization as the technology moves.
6. **Oral defense / process-artifact verification** — integrity checking that AI cannot defeat, because it measures the human.
