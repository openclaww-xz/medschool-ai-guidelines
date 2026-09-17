---
run: 30
layer: health-systems
files_reviewed: 16 (all fully read; see per-file notes in analysis/deep-reading/)
date: 2026-09-17
---

# Run 30 Synthesis — Health Systems: Deployment Pioneers vs PR-Driven Adopters vs Governance-Only

## The three-leg test
A **true deployment pioneer** needs (1) governance — a defined approval pipeline with named bodies; (2) tooling — deployed AI in production plus enabling infrastructure (registries, intake, approved platforms); (3) monitoring — post-deployment surveillance, not just one-time approval. **Governance-only** systems have instruments without visible deployment. **PR-driven adopters** have deployment narratives without governance content.

## Tier 1 — True deployment pioneers (governance + tooling + monitoring)

**Duke Health (ABCDS).** The cleanest pioneer on process: mandatory registry of all patient-care algorithms, risk-tiered pathways (full / fast-track / registration-only), *independent* review committees, stage-gated checkpoints that explicitly extend "to general deployment, monitoring, and maintenance," four-way decisions (approve / approve-with-contingencies / re-review / decline), Bias Management Framework, FDA SaMD navigation. Monitoring is inside the review mandate by design. What the captured page lacks is deployment specifics — but the program exists to govern a live clinical-algorithm portfolio.

**Mount Sinai (MSHS 223 + governance page).** Policy with the strongest monitoring cadence in the corpus: quarterly reviews mandatory for the first 24 months for any tool used in patient care, billing, or employment; annual minimum thereafter; documented review reported to the approving committee; action plans; decommissioning rules; committee suspension authority mid-investigation. Tooling leg: DTP-maintained approved-tool registry, centralized AI portfolio ("all clinical, operational, and financial AI models and features"), ServiceNow idea intake, pilot→checkpoint→scale sequencing, committee structure (AI Executive Committee over AI Review Board / Risks-Ethics-Policy / TLD). Consent/notice determination for patient-care AI is assigned to PPHS with a fallback notice hierarchy. Governance + tooling + staged monitoring = pioneer, with the caveat that IT (DTP) owns the policy rather than the CMO office.

**UW Medicine (COMP.308 + Glossary 308.G1).** The best *policy instrument*: signed by the Chief Compliance Officer, effective 2026-09-01, with a 12-item elevated-risk trigger screen (patient-facing unvalidated output, patient interaction, PHI/de-identified/UW-data exposure, clinical automation, billing impact, **union labor impact**, **>$100k spend**, academic-selection impact, **equity/accessibility impacts via Equity Impact Review Tool**, change-management load), three review bodies (AI Use Case Review Council, AI Education Review Workgroup, AI Operations Subcommittee escalation), contract/BAA/security gates with periodic security reassessment, an Approved AI Tool/Application List with pragmatic named examples, and a faculty-authored, citation-backed 46-term glossary that makes the triggers enforceable. Weak leg: clinical-performance monitoring (only security reassessment is periodic; no IMPACC/ABCDS-style surveillance named). Pioneer on governance-instrument quality; monitoring partial.

**UCSF Health (portal + considerations).** Named Health AI Oversight committee (cross-disciplinary, reviewing AI "deployed within the health system") **and IMPACC monitoring** — a named post-deployment monitoring program — plus a single authorized platform (Versa), IRB guidance for LLMs, and GPT-development guidance (builds its own tools). The captured pages are thin, so classification is **pioneer by inference** (all three legs referenced, none elaborated in this corpus slice).

**UChicago Medicine IM residency (Abridge policy).** Pioneer at the *operational* end rather than the enterprise end: the deepest ambient-scribe governance anywhere in the corpus — per-encounter verbal consent from patient AND all third parties present, `.ABRIDGEVERBALCONSENT` smartphrase documentation, documented declination with no care impact, mandatory pre-access orientation on "common AI error patterns," PGY-2/3-only eligibility, physical-presence anti-passive-recording rule, MDM/encryption device requirements, resident-responsibility + attending-attestation liability chain ("same expectations ... as traditional documentation"), annual reassessment with revocable approval, and named prohibited/approved alternative tools. If the test is "governance + deployed tooling + review cycle" at the point of clinical risk, this program-level policy outperforms most enterprise policies.

## Tier 2 — Structured, credible, but with a missing leg

**Ochsner.** Broad verifiable deployment (DeepScribe ambient, sepsis/HF prediction, imaging triage, pharmacy automation, Clara AI agent, avatars) with the best patient-facing consent and transparency practice after UChicago: verbal consent before ambient listening each visit, on/off anytime, recording-window limits, AI self-identification duty, opt-out without care impact, minimal-data agent scoping, human-authored avatar content. Governance is committee-named (Data Governance + AI Steering, multidisciplinary composition disclosed) with a continuous-fairness-monitoring *claim* — but no pipeline or evidence. Deployed-and-honest, governance-asserted.

**Michigan Medicine.** Named Clinical Intelligence Committee chaired by an **Associate CMIO for AI** (the clearest clinically-led governance in the run) plus an "Appropriate Clinical Use of GenAI Tools Policy," approved-services infrastructure, and HITS/TSP channel discipline — but this artifact is only the KB signpost; depth unverifiable here.

**UC Davis Health.** Compliance-owned guidelines referencing an Analytics Oversight Committee + a real deployed ambient scribe (Abridge) with 15-language patient materials, 30-day recording deletion, and an opt-out consent model. Governance thin on the surface, consent model mid-tier (opt-out vs per-encounter opt-in).

**Johns Hopkins.** Enterprise tooling pioneer (HopGPT: secure ChatGPT/Claude/Llama gateway behind JHED, phased rollout, training site) paired with a 4-bullet responsible-use guideline whose only liability clause is "You are responsible for any AI-generated content that you produce or publish." Infrastructure-first, governance-light: **deployment without governance depth** — the inverse of governance-only.

## Tier 3 — PR-driven adopters

**Cleveland Clinic.** The largest disclosed production footprint in the run — Ambience ambient scribe across **all** outpatient practices (>4.5K PCPs), AKASA inpatient coding AI with throughput specs, AI on its own Safety Event Reporting System, first-US-center prostate-AI trial, DASI cath-lab copilot, quantum computing, Oracle and Khosla partnerships — presented in a CEO annual report with **zero** governance, monitoring, consent, or liability content. The Ambience paragraph describes visit recording with no consent or opt-out mention whatsoever. Elite adopter; as a published posture, deploys first and explains later.

**Houston Methodist.** Innovation-office case study: 20+ clinician-built vICU algorithms with a 37% codes-reduction claim, HDAI and Pieces pilots, "succeed fast, fail fast" framing, and a safety sentence with no measures behind it ("the most comprehensive degree of safety and security measures"). No committees, no consent, no monitoring, no liability positioning.

## Cross-cutting findings

1. **Governance locus predicts genre.** Compliance-owned (UW) and program-owned (Duke) documents read as enforceable instruments; IT-owned (MSHS/DTP, Hopkins) read as process or provisioning; innovation- and communications-owned (Houston Methodist, Cleveland Clinic, Ochsner) read as marketing. No document in this run is CMO-office-authored; the closest to clinical ownership is Michigan Medicine's Associate-CMIO-chaired committee and UChicago's residency leadership.
2. **Ambient-scribe consent is the sharpest differentiator.** Spectrum: UChicago (per-encounter verbal consent, all parties, charted consent AND declination) > Ochsner (verbal consent each use, on/off anytime) > UC Davis (opt-out, no documentation duty) > Cleveland Clinic (none mentioned). System-level policies (MSHS 223) delegate consent determination to IRB/PPHS rather than fixing a rule.
3. **Liability is uniformly devolved downward.** Every explicit statement puts responsibility on the individual: UW ("Users are responsible for reviewing outputs"), Hopkins ("You are responsible for any AI-generated content"), MSHS (clinician must review and sign AI documentation), UChicago (resident full responsibility + attending attestation — the only two-tier chain). No system assumes enterprise liability or offers indemnification language.
4. **Monitoring is the rarest leg.** Only Duke (lifecycle checkpoints through maintenance), Mount Sinai (quarterly × 24 months), UCSF (IMPACC, named only), and Ochsner (one fairness-monitoring sentence) evidence anything beyond one-time approval. Cleveland Clinic and Houston Methodist report outcomes but no surveillance regime.
5. **Unusual triggers worth flagging in the matrix:** UW's union-labor-impact and $100k thresholds; UW's equity trigger tied to an Equity Impact Review Tool; MSHS's AI Executive Committee written-consent gate for any employment AI and its NLRA carve-out; Duke's named-role accountability ("Clinical and Model Owners") for low-risk tools; MSHS's AI-disclosure duty on published AI content.

## Verdict table

| System | Governance | Tooling/deployment | Monitoring | Classification |
|---|---|---|---|---|
| Duke Health | Registry + risk tiers + independent committees | Implied portfolio | In-mandate (to maintenance) | **Pioneer** |
| Mount Sinai | Committee-routed lifecycle policy | Registry, portfolio, intake, pilots | Quarterly×24mo, annual min | **Pioneer** |
| UW Medicine | Best-in-class signed policy + glossary | Approved-tool list | Security reassessment only | **Pioneer (governance-led)** |
| UCSF Health | Oversight committee (named) | Versa platform, GPT building | IMPACC (named) | **Pioneer (inferred — thin artifacts)** |
| UChicago (IM residency) | Program-level, operational | Abridge live | Annual reassessment, revocable | **Pioneer (operational tier)** |
| Ochsner | Committee-asserted | Broad deployed stack | Claimed, unevidenced | Progressive-structured |
| Michigan Medicine | Clinical Intelligence Cmte (Assoc. CMIO) | Approved services (ecosystem) | Unknown | Progressive-structured (thin artifact) |
| UC Davis Health | Analytics Oversight Cmte reference | Abridge deployed | None shown | Progressive-structured / cautious |
| Johns Hopkins | 4-bullet guidelines | HopGPT enterprise gateway | None | Progressive-structured (tooling-led) |
| Cleveland Clinic | None published | Largest disclosed footprint | None published | **PR-driven adopter** |
| Houston Methodist | None published | vICU 20+ algorithms, pilots | None published | **PR-driven adopter** |

**Governance-only** (instruments without visible deployment) — no system in this 16-file set qualifies; the closest inversions are JHU (deployment without governance) and UW (governance ahead of demonstrated clinical-AI deployment).
