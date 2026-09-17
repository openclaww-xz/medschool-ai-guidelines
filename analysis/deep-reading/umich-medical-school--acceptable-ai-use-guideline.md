---
source_file: raw/us-med-schools/umich-medical-school--acceptable-ai-use-guideline.md
read_status: full
approx_words_read: 2010
note_author: run-27 deep read
---

# University of Michigan Medical School — Guideline: Acceptable AI Use (KB0036135)

## Authority / Authorship
- Michigan Medicine Knowledge Portal (ServiceNow KB article KB0036135, "recently revised," updated ~6 months before capture).
- "AUTHOR(s): Erin Dietrich, Deputy CIO for UMMS and HITS Senior Director for Academic IT."
- "ENDORSEMENT(s): Jack Kufahl, Michigan Medicine Chief Information Security Officer."
- IT-authored guideline (not a faculty-senate curriculum policy) — an operational/IT governance framing rather than a curricular-academic one.

## Policy Philosophy (verbatim framing)
- "existing tools such as U-M GPT may enhance education, research, innovation, and activities supporting clinical workflows while still respecting security, privacy, and responsible-use requirements."
- "Given that users are responsible for the output and application of AI tools, it is important to understand both their benefits and limitations. The guidelines below are intended to help you use AI responsibly."
- "AI should assist, not replace, human judgment."

## Complete Verbatim Clause Inventory by Theme

### Key highlights (do-list)
- "Use only approved AI services for U-M sensitive data (see the Approved AI Tools section in this guide)"
- "Follow all MM and UM policies and guidelines around safe data use"
- "Be aware of internal research requirements and policies as well as those of sponsors and outside agencies"
- "Disclose AI use when appropriate and as directed (e.g., funding agency, journal), or when used in clinical care"
- "Ensure AI-generated information and code is always reviewed by a human; faculty members must confirm the credibility of reviews"
- "Only use institutional data classified as low with AI services that do not have a contract or data agreement with U-M"

### Practices to avoid
- "Do not assume AI-generated information is correct or current"
- "Do not allow AI to replace professional judgment, expertise, or critical thinking"
- "Do not assume an AI tool is approved, secure, or appropriate simply because it is convenient"
- "Do not place sensitive data in an AI service unless there is a U-M contract or data agreement in place that permits it"
- "Do not use AI-generated code for institutional IT systems and services unless it is reviewed by a human, as well as meets the requirements of Secure Coding and Application Security (DS-18)"

### Principle 1: Data protection, privacy, compliance
- "Protecting sensitive information is a shared responsibility. When using AI tools you are accountable for the secure and compliant use of regulated and sensitive data within these systems, per U-M policies... including the Health Insurance Portability and Accountability Act (HIPAA), the Family Educational Rights and Privacy Act (FERPA), and other institutional requirements, must be followed by every user."
- "Do not share sensitive data (including PHI) with third party applications unless explicitly authorized"
- "When authorized, using only the minimum necessary sensitive data (including PHI) for the intended purpose"
- "Ensuring PHI is accessible only to individuals with authorization or a legitimate need to know"
- "Verifying AI-generated information before using it in patient care or medical decision-making"
- "Following HIPAA and institutional data protection requirements"
- Mandatory training: "Complete the following training: MM Institutional Mandatory - AI: An Introduction for Michigan Medicine Employees (UMHS-10001)"
- Related SPGs listed: 601.07 (Responsible Use of Information Resources), 601.11 (Privacy/Monitoring), 601.33 (Personally Owned Devices), 601.27 (Information Security), 601.12 (Institutional Data Stewardship).

### Principle 2: Human oversight, transparency, accuracy
- "AI can support education, research, clinical work, and administrative tasks, but its outputs may be inaccurate, biased, incomplete, or fabricated. AI should assist, not replace, human judgment. You remain responsible for reviewing AI-generated content, making informed decisions, and ensuring its appropriate use."
- "Be transparent about AI use when appropriate... Consider including an AI Usage Disclosure statement such as: 'Created with the assistance of [AI Tool Name] for [e.g., initial drafting / data visualization/slide layout generation]. All outputs were reviewed, edited, and approved by the author/team.' Do not present AI-generated work as solely human-created when that distinction matters. Remember, you are responsible and liable for the AI generated output you use."
- "Always verify AI-generated information using trusted sources, especially clinical, legal, regulatory, or policy-related topics. Review content for accuracy, bias, accessibility, and appropriateness before using or sharing it."

### Principle 3: Appropriate academic use
- "Academic and instructional requirements may vary. Students are responsible for following course, program, and instructor expectations regarding AI use in assignments, assessments, and scholarly work. Faculty should communicate AI use expectations clearly within courses and learning activities."

### Approved tools / data classification regime
- "Use of pre-approved AI vendors and technologies is the recommended approach for incorporating AI into U-M work. The following tools are optimized and approved: U-M Gen AI Services provided by ITS and M365 Copilot."
- "U-M GPT, U-M Maizey, and U-M GPT Toolkit Services and M365 Copilot are approved for use with data classified as high (e.g., PHI)."
- "Faculty, staff, and students are responsible for knowing when the use of AI tools is prohibited (e.g., grant reviews, manuscript reviews)."
- "These tools are designed for use within the U-M environment, and usage data are not shared with external developers or used to train public models. For this reason, U-M users should use these approved AI resources and must not enter institutional data into public AI services."
- "Third-party AI tools may only be used with institutional data classified as low, unless otherwise formally approved."
- "OpenClaw is currently blocked, and additional tools may be blocked in the future based on security, privacy, compliance, or operational risk."
- "If you are uncertain whether a specific AI tool is appropriate for your use case, contact MM Information Assurance before using it."

### Tool approval pathway
- "As with any technology, you must follow established processes on how to buy or incorporate new technology. AI tools are subject to the same information security standards and protocols as any new technology."
- "Partner with HITS or another Trusted IT Service Provider (TSP). TSPs are the only entities authorized to develop and/or manage applications, manage IT vendors, or anything related to IT delivery at Michigan Medicine."

### FAQs (operational clarifications)
- On citation: "users should always follow instructor, journal, disciplinary, and institutional requirements."
- On PHI: "Use only approved AI services for U-M sensitive data... which varies by service."
- On data sensitivity of U-M Gen AI Services: "High."
- Notification listserve exists (ITS-AI-Services-Notify).
- File uploads permitted in U-M GPT.
- On trusting U-M GPT: "U-M GPT does its best to generate accurate information based on the diverse range of text on which it has been trained. However, it does not verify, or fact check the information it provides. Moreover, it does not have access to real-time data or updates, nor does it understand the information it provides in the way humans do... all outputs it generates should be reviewed and verified with reliable sources."
- Incident reporting: "Users of Michigan Medicine information systems shall immediately report security incidents to the HITS Service Desk by calling 734-936-8000. If ePHI is involved, notify the Corporate Compliance Office."

## Sophistication Markers
- **Tool investment**: U-M's homegrown suite (U-M GPT, U-M Maizey, U-M GPT Toolkit) approved for HIGH-classification data including PHI, with no-training and no-external-sharing guarantees — one of the strongest university-built deployments represented in this corpus.
- **Tech understanding**: full data-classification regime (high/low) mapped to tool tiers; names a specific blocked tool (OpenClaw); anticipates future blocking; AI-code security standard (DS-18); honest LLM-limit explanation in FAQ (no real-time data, no verification).
- **Assessment redesign**: none — academic use delegated wholly to instructors ("requirements may vary").
- **Evidence citations**: internal policy web (SPGs, DS-18, Safe Computing guide); no external scholarly citations.
- **Training requirement**: mandatory institutional AI training course (UMHS-10001) — a concrete educational investment beyond policy text.

## Distinctives
- IT/security-led rather than curriculum-led; the audience is the whole Michigan Medicine workforce, with medical students as one constituency.
- Named author + CISO endorsement; live blocking of tools; incident hotlines.
- Prohibition enumeration includes research-specific contexts (grant reviews, manuscript reviews).
- Mandatory training requirement is unique in this batch.

## Provisional Classification: **progressive-structured**
Justification: institutional tool investment and classification-based governance are frontier-grade, but the document is an operational IT guideline, not an education policy: no pedagogy, no assessment philosophy, no citation format, student academic use entirely deferred to instructors. Pioneer infrastructure, progressive-structured as a school policy artifact.
