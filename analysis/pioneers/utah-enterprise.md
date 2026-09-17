# University of Utah — AI Use Guidelines v1.0 (enterprise, Office of Artificial Intelligence)

**Classification: pioneer** (run-29 cohort C; `analysis/deep-reading/29-cohortC-synthesis.md`)

## Who drove it

The **Office of Artificial Intelligence (OAI)**, with a named **Chief AI Officer** as Guidance Officer — "the most institutionally mature document in cohort C — dedicated OAI with Chief AI Officer, tool inventory, AIA process, drift-monitoring grading rules, agentic-AI definitions, and enforcement teeth" (`raw/us-med-schools/uutah--ai-use-guidelines-2026.md`; `analysis/deep-reading/uutah--ai-use-guidelines-2026.md`). The governance lattice around it: OAI (strategy, approved-tools inventory, literacy), UIT (technical/security evaluation), ISO (risk assessment, incident response), Data Stewards (Policy 4-001), Office of Research Security and Compliance, AI Leadership Team, General Counsel, Health Sciences, VPR, Purchasing. Utah built a *statutory-style* institution: the guideline supplements named regulations (Policies 4-001, 4-004, Rules R4-004A/C, 3-100, 4-050, 7-001, 7-020, 6-410) plus HIPAA/FERPA/**GRAMA** (the state records law).

## Institutional context

Two enablers: (1) Utah's state legal environment — the GRAMA public-records framing ("AI interactions conducted as part of University business may constitute government records") and a state Chief AI Officer ecosystem; (2) an enterprise that had already built the OAI, tool inventory (ai.utah.edu/tools), and review processes before writing the teaching guidance. Run 29's counter-pattern is instructive: "Utah SOM's own handbook clause (one prohibition-default paragraph) lags its own university's pioneer guideline by miles — institutional maturity ≠ curricular propagation" (`analysis/deep-reading/29-cohortC-synthesis.md`, pattern 4). The pioneer artifact here is the enterprise layer; the SOM layer is conservative-naive. That divergence is itself a finding.

## What they built and why it is pioneer-grade

1. **NIST/EO-grade vocabulary in a university instrument**: definitions of **Agentic AI** ("planning, making decisions, and executing tasks toward defined goals with varying degrees of human direction"), **High-Risk AI Use**, **Consequential Decision**, and **Meaningful Human Review** ("a qualified individual with sufficient authority... enabling that individual to exercise independent judgment and modify or overturn the outcome"). These are the definitions regulators use — almost no medical school document contains them.
2. **The AI Impact Assessment (AIA)**: high-risk initiatives may require pre-deployment assessment covering bias/disparate impact, accessibility, human oversight, transparency, and "Appeals, recourse, or existing University review processes for affected individuals" — an algorithmic-impact instrument modeled on regulatory practice.
3. **The most detailed grading regime in the corpus** (§9.2): human authority ("instructors remain solely responsible... for assigning final grades"), de-identification of student work, approved-tools-only ("Instructors should not use personal/consumer AI accounts for grading tasks"), **validation and drift monitoring** ("pilot and validate before course-wide use, periodically spot-check for drift or bias, and document the tool used and validation approach"), transparency-to-students, and appeals documentation.
4. **Evidence-calibrated detection stance**: "AI-detection tools should not be treated as conclusive evidence of academic misconduct... Instructors should not upload student work to unapproved third-party AI detection services."
5. **Due-process rights for high-risk academic AI** (§9.1): for AI-assisted grading, integrity determinations, admissions, progression/dismissal — affected individuals should be informed of the use, the human-review scope, and "How to request meaningful human review, correction, or appeal."
6. **Contract and procurement teeth**: vendors "must contractually prohibit training on University data unless expressly authorized"; model-development on institutional data requires lifecycle governance ("retention, retraining, access controls, and retirement"); approved meeting tools named (Teams Premium, Zoom AI Companion) with a third-party-assistant disable-request norm.

## What they explicitly chose NOT to do

- No prohibition default: "Students may use non-approved tools for personal study purposes" — the strongest student-facing permissive clause in cohort C.
- No detection-centered integrity process (see above).
- No attempt to enumerate clinical AI rules at enterprise level — clinical specifics defer to health-sciences governance; equally, the SOM handbook's prohibitionism is left uncoordinated.
- The guideline "does not replace" the regulation stack — it supplements, refusing to duplicate existing authority.

## Borrowed vs original

Definitions and instruments track NIST AI RMF / federal-EO vocabulary (the national synthesis shows WHO/EU lineage for such terms internationally; `analysis/deep-reading/26-national-synthesis.md`, §1) — Utah imports regulator-grade concepts rather than medical-education ones. The grading-validation/drift clauses and §9.1 appeal rights are original in this corpus. No US med-school peer supplied source material; run 29 notes the diffusion network runs state-school-to-state-school (OHSU credits UT Health San Antonio, not Utah — these are parallel convergent builds).

## Weaknesses / what's missing

- **The med-school gap**: clinical/UME specificity is thin — "Medical education enters only via generic 'clinical care' mention and §9 grading clauses" (deep-read). The SOM's own handbook clause remains prohibition-default; the enterprise pioneer has not propagated into the curriculum.
- An enterprise guideline binds weakly at course level; faculty enforcement mechanics are left to existing academic-integrity policy.
- No worked examples or scenarios — instrument-grade, not teaching-grade.
- AIA is discretionary ("may require") — no published criteria for when it is mandatory.

## What to steal concretely

1. **The four definitions** (Agentic AI, High-Risk AI Use, Consequential Decision, Meaningful Human Review) — drop them into any policy's definitions section; they are regulator-tested and future-proof.
2. **The §9.2 grading clause set** — especially "pilot and validate before course-wide use, periodically spot-check for drift or bias, and document the tool used and validation approach." This is the only grading-AI validation standard in the corpus.
3. **§9.1 notice-and-appeal rights** — anyone affected by AI-assisted grading/admissions/progression decisions gets informed use, human-review scope, and an appeal path.
4. **The detection clause pair**: not-conclusive-evidence + never-upload-to-unapproved-detectors.
5. **Vendor contract language**: contractual training prohibition + model-lifecycle (retention/retraining/retirement) obligations in every AI procurement.
6. **The lesson of the divergence**: enterprise maturity does not automatically reach the curriculum — pair the enterprise instrument with an explicit SOM-level implementation mandate, which Utah has yet to do.
