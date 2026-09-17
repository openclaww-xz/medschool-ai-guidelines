---
source: raw/us-med-schools/uutah--ai-use-guidelines-2026.md
school: University of Utah (institution-wide, not SOM-specific)
document: "Artificial Intelligence Use Guidelines, v1.0, Sept 2026"
read: full (551 lines)
run: 29 (cohort C)
---

# Deep Read — University of Utah AI Use Guidelines (Sept 2026)

## Authority / Authorship
- Responsible Office: **Office of Artificial Intelligence (OAI)**; Guidance Officer: **Chief AI Officer**. Effective/Last Revised Sept 2026, Version 1.0.
- University-wide guideline (research, education, clinical care, admin), not a medical-school policy; applies to "All University faculty, staff, students, researchers, contractors, affiliates, and agents."
- Elaborate governance lattice: OAI (strategy, approved-tools inventory, literacy), UIT (technical/security evaluation), ISO (risk assessment, incident response), Data Stewards (Policy 4-001), Office of Research Security and Compliance, AI Leadership Team, General Counsel, Health Sciences, VPR, Purchasing.
- Supplements (does not replace) a named regulation stack: Policies 4-001, 4-004, Rules R4-004A/C, 3-100, 4-050, 7-001 (Research Misconduct), 7-020 (Authorship), 6-410 (Academic Integrity), plus HIPAA/FERPA/GRAMA.

## Philosophy (verbatim framing quotes)
- "The University recognizes AI literacy as an increasingly important dimension of undergraduate, graduate, and professional education" — literacy-first framing.
- "The University views AI not merely as a tool but as essential infrastructure — including data, models, systems, software, and hardware — that fosters innovation and the social good."
- "The goal of this guidance is to help members of the University community to balance innovation with privacy, security, compliance, integrity, responsible use, and public trust."
- "to understand when AI use enhances—and when it may undermine—human judgment, creativity, learning, and professional responsibility."

## Complete Verbatim Clause Inventory

### Definitions (§3)
- AI: "A machine-based system designed to perform tasks that typically require human intelligence, including but not limited to generating content, making predictions, analyzing data, or executing actions."
- Generative AI: "AI systems capable of producing new content (e.g., text, images, audio, code, or other outputs) based on information learned from training data."
- **Agentic AI**: "AI systems capable of planning, making decisions, and executing tasks toward defined goals with varying degrees of human direction and oversight."
- Responsible AI: "AI that is developed and used in a manner that protects privacy, security, civil rights, and civil liberties, and promotes fairness, accountability, transparency, and appropriate human oversight."
- Approved AI Tool: tool that completed "required University review processes" and is "listed on the official inventory" at ai.utah.edu/tools.
- High-Risk AI Use: application that "may materially affect an individual's rights, privacy, opportunities, academic standing, employment, financial interests, access to University services, or other significant interests, and therefore requires heightened review, oversight, and accountability."
- Consequential Decision: "A decision that materially affects an individual's academic standing, admission, financial aid, employment, access to University programs or services, or disability accommodations."
- Meaningful Human Review: "Review by a qualified individual with sufficient authority and understanding of the relevant information, the AI system's role, capabilities and limitations, and the process used to produce the output recommendation, enabling that individual to exercise independent judgment and modify or overturn the outcome when appropriate."

### Guidance statement (§4)
Use permitted provided it: (1) complies with laws/regs/contracts/sponsor requirements; (2) adheres to data classification & security standards; (3) "Uses reviewed and approved AI tools when conducting University business"; (4) "Maintains meaningful human oversight and ensures that final decision-making authority remains with qualified individuals, particularly in high-risk or consequential contexts"; (5) upholds academic integrity & research standards; (6) protects privacy/IP/institutional interests; (7) promotes responsible AI.

### Decision framework (§4.1)
Five pre-use evaluation questions: Purpose and Use Case; Data Classification; Tool Approval ("Is the AI tool included on the University's approved inventory? If not, it must be submitted for review and approved before use"); Risk Level (minimal/moderate/high); Human Oversight. "The level of review and oversight should be proportionate to the reasonably foreseeable risks."

### Approved tools & procurement (§6)
- "When conducting University business using AI with Institutional Data, University individuals must use University-approved AI tools whenever required by the applicable data classification, institutional regulation, or University guidance."
- New tools: AI Tool Form → review by OAI/UIT/ISO; "Use is not permitted until approval is granted."
- **AI Impact Assessments (AIA)**: "High-risk AI initiatives may require completion of an AI Impact Assessment before deployment." Assessment may evaluate purpose; data sources/classification; "Potential bias or disparate impacts"; privacy/security/cybersecurity risks; accessibility/disability impacts; human oversight; "Transparency, explainability, and communication to affected individuals"; "Appeals, recourse, or existing University review processes for affected individuals."

### Data use (§7)
- Data minimization: "Only the minimum data reasonably necessary to accomplish the approved purpose should be provided to an AI system."
- Public data: approved enterprise tools approved unless designated otherwise; "Approval of an AI tool does not imply authorization to use sensitive or restricted data within that tool."
- Sensitive/Restricted: only in tools "explicitly approved for that classification," with Data Steward approval (and CDO/Data Trustee where required), executed contractual safeguards, technical controls, compliant storage locations; "Most AI tools are not appropriate for Sensitive or Restricted data."
- Where applicable: BAAs, DUAs; "Vendors must contractually prohibit training on University data unless expressly authorized"; "Vendors must provide sufficient transparency into model capabilities, data-handling practices, and limitations to enable institutional risk evaluation."
- Model development on Institutional Data "requires documented review and approval consistent with Policy 4-001"; requests must identify purpose, data elements, minimization, governance, "Model lifecycle considerations including retention, retraining, access controls, and retirement." "Institutional Data may not be used for AI training without explicit authorization."

### Research (§8)
Researchers must confirm data governance, verify sponsor policies, ensure accuracy/integrity of outputs, document AI usage, and "Maintain responsibility and accountability for the accuracy, integrity, and originality of all research content."
- "AI tools may support but may not replace substantive intellectual contributions required for grant proposals or scholarly work."
- "AI does not qualify for authorship under Policy 7-020."
- Disclosure failures "may constitute research misconduct."

### Teaching & learning (§9)
- "Faculty retain authority to determine whether and how AI tools may be used in their courses"; expectations "should be clearly communicated in course syllabi."
- "Students may use non-approved tools for personal study purposes. Coursework involving Institutional Data or University business, however, must use approved tools."
- **AI-detection**: "AI-detection tools should not be treated as conclusive evidence of academic misconduct. Academic integrity determinations should be based on the totality of available evidence... Instructors should not upload student work to unapproved third-party AI detection services." (rare, explicit anti-detection clause)
- §9.1 High-risk academic uses (AI-assisted grading, integrity determinations, admissions/financial aid, progression/dismissal, employment, placements/disability accommodations): affected individuals should be informed of the use of AI, the role/scope of human review, and "How to request meaningful human review, correction, or appeal."
- §9.2 Grading expectations: "Human authority & oversight" — "instructors remain solely responsible for evaluating student work and assigning final grades"; "De-identification & privacy" — student work de-identified unless expressly authorized, "Gradebooks or identifiable student datasets should not be uploaded except as expressly authorized"; "Approved tools only" — "Instructors should not use personal/consumer AI accounts for grading tasks"; "Validation & monitoring" — pilot and validate before course-wide use, "periodically spot-check for drift or bias, and document the tool used and validation approach"; "Transparency with students" — disclose AI use, intended role, privacy protections, human-review path; "Appeals & documentation" — maintain documentation, "instructors should be able to explain how final grades were determined."

### Administration & meetings (§10–11)
- Admin use must not let AI be "the sole basis for consequential administrative decisions affecting individuals"; must comply with records retention.
- Approved AI meeting tools "currently include only: Microsoft Teams Premium; Zoom AI Companion." When an outside participant introduces an AI assistant, participants "should request that the AI assistant be disabled for that portion of the meeting" if sensitive data may arise.

### Records (§12)
- "AI interactions conducted as part of University business may constitute government records under" GRAMA; "retention... should be determined by their business purpose and applicable records retention requirements, not by the fact that AI was used."

### Security & prohibited uses (§13–14)
- Incidents to ISO; "Hallucinations, inaccurate outputs, or other AI performance issues should be reported through this process only when they result in, or reasonably could result in, a security, privacy, safety, legal, discriminatory, or material operational risk."
- Prohibited: discriminatory deployment; deceptive impersonation/synthetic content misrepresenting identity or official communications; "Fully autonomous decision-making in high-risk contexts without human review"; uses conflicting with academic freedom/civil rights; fabrication of research data, falsifying academic records, misrepresenting authorship; "Circumventing institutional data protections through unauthorized AI services"; any illegal use.

### Infrastructure & enforcement (§15–17)
- Compute/storage stewardship section (CHPC, energy efficiency, "reduce redundancy and unmanaged tool proliferation").
- Monitoring "consistent with applicable law, University regulations, academic freedom, civil rights and liberties, and reasonable expectations of privacy."
- Sanctions: "suspension of access to AI tools, disciplinary measures... or other appropriate administrative action." Annual review cycle.

## Sophistication Markers
- Definitions of **Agentic AI**, **Meaningful Human Review**, **High-Risk AI Use**, **Consequential Decision** — NIST/EO-flavored vocabulary rare in med-school documents.
- AI Impact Assessment instrument (bias/disparate impact, accessibility, recourse).
- Grading-specific clause set (validation, drift monitoring, de-identification, no consumer accounts) — the most detailed grading regime in the corpus so far.
- Explicit AI-detection skepticism with a prohibition on uploading student work to unapproved detectors.
- Named approved meeting tools; vendor training-prohibition contract language; model-lifecycle governance (retention, retraining, retirement).
- Infrastructure/environment section (energy, compute stewardship) — unique in corpus.
- GRAMA public-records framing (state-school statutory environment).

## Distinctives
- Not a SOM policy at all: an enterprise AI governance instrument that happens to cover teaching/grading. Medical education enters only via generic "clinical care" mention and §9 grading clauses.
- Carries the strongest student-facing permissive clause: non-approved tools OK for personal study.

## Provisional Classification: **Pioneer**
Justification: most institutionally mature document in cohort C — dedicated OAI with Chief AI Officer, tool inventory, AIA process, drift-monitoring grading rules, agentic-AI definitions, and enforcement teeth. Matches or exceeds the private-elite pioneers (cf. run-level benchmark: only a handful of schools define Agentic AI or mandate grading validation). Caveat: maturity is institutional/IT-governance maturity; the clinical/UME specificity is thin compared with dedicated SOM policies.
