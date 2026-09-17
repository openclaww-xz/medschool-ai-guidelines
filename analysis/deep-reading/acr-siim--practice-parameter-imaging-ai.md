---
source_file: raw/national-frameworks/acr-siim--practice-parameter-imaging-ai.md
read_status: full
approx_words_read: 5755
---

# ACR–SIIM — Practice Parameter for Imaging Artificial Intelligence (adopted 2026, Resolution 13)

## (a) Authority and authorship
- Joint **ACR Commission on Informatics + Commission on Quality and Safety with SIIM** (Society for Imaging Informatics in Medicine). Writing committee: **Tessa Cook, MD, PhD (Chair)** + 9 ACR members and 3 SIIM members (Kikano, Kottler, Roth); sponsoring Committee on Practice Parameters and Technical Standards (Caplin chair); Comments Reconciliation Committee listed; **adopted 2026 by ACR Council (Resolution 13)**, effective Oct 1 cycle. Full consensus-process disclosure.
- Powers claimed: ACR practice parameters are "policy statement[s] by the College" for radiology practice — with an explicit **anti-standard-of-care disclaimer**: "Practice Parameters and Technical Standards are not inflexible rules or requirements of practice and are not intended, nor should they be used, to establish a legal standard of care," citing case law (Iowa 2013; Stanley v. McCarver 2003). Binds radiology practices de facto via accreditation/payer expectations; applies to "all practitioners and support personnel... who deploy, interpret, interact with, support or act upon AI-derived outputs."

## (b) Policy philosophy
- Posture: **operational governance — lifecycle management of deployed models**. Framing quote: the goal "is to define the **infrastructure, personnel, processes and governance** needed to establish a comprehensive framework for the **safe, effective and transparent integration** of artificial intelligence (AI) into imaging practice... AI governance, selection of AI solutions, **local acceptance testing and real-world performance monitoring**."
- Not an ethics paper: no framing debate about embrace vs risk; the technology is assumed deployed, and the document engineers its management.

## (c) Complete clause inventory (the densest operational regime in the corpus)
**Definitions with normative force**
- "**Qualified end-user**: a licensed physician with the necessary qualifications and training to **independently provide the equivalent medical service without the aid of the AI solution**, and who possesses qualifications and training in the use of the AI solution, including the ability to **assess the validity of its output**." (Rooted in ACR's 2024 Model Legislative Language — i.e., this definition is being shopped to state legislatures.)
- "**Drift** describes gradual degradation in the performance of an AI model over time... including changes in the type of inputs provided to the model." — the only corpus document to define and operationalize drift.
- Governance group: "responsible for the administrative, clinical and technical aspects of AI deployment... **A diagnostic imaging physician should be part of this group**."
**Personnel duties (Section III)**
- End-users "should have a clear understanding of how it works, including the type of input required, the data used for inference, regulatory clearance and intended use, the nature of the output, and how to interpret that output"; "should be made aware **when the AI solution has run**"; should understand how "**machine manufacturer and model, protocol, acquisition and reconstruction parameters, image quality** and patient characteristics (**age, gender, race, ethnicity**) may influence performance," and "**how disease prevalence affects AI performance**."
- Medical physicists: "essential contributors... verifying input fidelity, evaluating protocol dependencies and establishing baseline technical performance"; "help define **rollback criteria and sunsetting procedures**."
- II/IT: configure infrastructure, "ensure the system is secure, managed for privacy requirements," maintain "post-deployment monitoring, such as **integration with registries (e.g., Assess-AI)**."
- Data scientists: "design of statistically robust local validation protocols," "automated data pipelines... ongoing monitoring," "synthesizing feedback into actionable insights."
- Technologists "should: be certified... possess unrestricted state licensure... **be trained on the AI use case and imaging parameters of the expected AI inputs; AI input image quality evaluation and remediation; AI-related quality assurance**."
- Manufacturers: "required to provide standard guidance (IFU)"; "should deliver comprehensive documentation, including **release notes and model versioning, and proactively notify customers prior to deploying new versions**"; "encouraged to provide: summaries of training data and internal and external evaluation data; **model performance in relevant subgroups**; scope of any FDA-authorized **predetermined change control plan (PCCP)**; **per-version change notes that flag subgroup-specific changes in performance**; model explainability and inference transparency; status of AI model output (processing, inferenced, rejected); reason for data rejection; **confidence scores or output uncertainty**...; patient age groups intended."
- Legal/compliance/privacy: advise on "scope of FDA clearance... and **off-label uses**"; FDA/HIPAA/ONC/OCR; "common law and ethics"; ensure deployment within "institutional guidelines and local, state and national legislation"; contracts/IRB oversight.
**Governance (IV.A)**
- "Practices **should establish an AI governance group** responsible for oversight of **selection, local acceptance testing, deployment, monitoring, rollback and sunsetting** of AI solutions."
- "should include **at least one diagnostic imaging physician**"; "Members... are expected to be **impartial**... a manufacturer or developer of an AI solution would not be expected to participate in governance discussions related to the deployment of their product" (COI recusal rule).
- "The group should meet regularly and **keep minutes that record decisions, any risk acceptances, and defined rollback or sunset criteria**."
**Documentation and inventory (IV.B)**
- "Practices should maintain an up-to-date local inventory of all deployed AI solutions," with: "model name and documented version or build; deployment date and environment; IFU/labeling and intended use...; scope/identifier of any FDA-authorized PCCP; local acceptance testing protocol and results; relevant routing rules (DICOM/HL7/FHIR) and inclusion/exclusion criteria...; qualified end-user training logs; **postdeployment monitoring data and drift checks**; acceptance/rejection logging configuration; contact information."
**Security and compliance (IV.C)**
- HIPAA: "AI solutions should adhere to the HIPAA Privacy, Security and Breach Notification Rules"; "Data used for model fine-tuning, local acceptance testing or retraining **should be de-identified to HIPAA Safe Harbor standards whenever feasible. If PHI is retained, a business associates' agreement (BAA)... should be executed before deployment**"; "The HIPAA Notice of Privacy Practices (NPP) should be reviewed and updated if any new AI use cases are not covered."
- Security: "encryption... in transit and at rest"; "access restricted to approved networks, devices, endpoints and authenticated users"; "multifactor authentication... when feasible."
- **Downtime planning** (unique): "Qualified end-users should design or be trained on **processes for reverting to non-AI clinical operations during AI outages**"; notify stakeholders; "AI updates should be scheduled during low-impact periods."
- Audit: "Data accessed by AI solutions should be logged. Logs should be auditable"; unauthorized PHI access "should be reported... to HHS... if required."
- Law scan list: HIPAA/HITECH, FDA SaMD, **EU MDR, EU AI Act, GDPR**, US Civil Rights Act Title VII + ADA "(discrimination and bias)," state/local laws.
**Model selection (IV.D)**: "defined process and criteria"; pediatric clause — "If selecting an adult-only AI solution in mixed practices, **a rationale and mitigation plan should be documented to address excluded populations**."
**Local acceptance testing (IV.E)**: "qualified end-users evaluate initial AI performance **using local data**"; "local data should come from **a variety of machine manufacturers, models and protocols, and reflect a spectrum of image quality**," including "dose-optimized or ultra-low-dose images"; "**Predefined metrics for acceptable AI performance should be agreed upon prior to the evaluation process** and tailored to relevant patient populations"; pediatric age-group breakdowns stated.
**Training/IFU (IV.F)**: "Documented training procedures are recommended"; "IFU/labeling be readily accessible"; "**Supplemental training is required after each model/version or intended-use change**"; notification protocols for contemporaneous use.
**Monitoring (IV.G)**: "**continuous monitoring with periodic reports on routing rule adherence, accuracy, calibration, drift and subgroup performance**"; "**Acceptance, rejection and overrides of AI outputs should be logged in a standardized form**"; "Practices should submit to or benchmark... against **qualified registries (e.g., Assess-AI)**"; adverse events "triaged for **medical device reporting (MDR)**"; "Practices should decide **who has authority to take an AI solution offline**... Specific **stop rules**... in instances of significant degradation in pediatric subgroup performance, repeated misrouting of pediatric exams, and sustained high pediatric override rates."
**Non-FDA-regulated models (IV.H)**: "additional oversight and compliance with local governance is recommended. This includes locally developed models as well as emerging technologies such as **generative AI (e.g., large language models, vision-language models, foundation models)**"; "review by the organization's IRB, additional resources for postdeployment monitoring, and extra review by... legal, compliance and privacy professionals."
**Other considerations (V)**
- Output release: "consider how their AI solutions release outputs (e.g., directly into the patient's record... or **only after review by a qualified end-user**)"; "whether the qualified end-user reports the AI output (**which may be required by law in certain states**)"; portal visibility — "Misclassified AI results in a portal could cause patient or caregiver anxiety or inappropriate action"; pediatric proxy access and "delayed release rules for adolescents."
- "**It is recommended that AI solutions only be used by qualified end-users who can accurately assess the veracity of their outputs.**"
- Off-label: "AI triage software that is not intended to be used as a diagnostic device **should not be used as such** unless the practice has made an informed decision to use it 'off-label.' Furthermore, if an AI solution intended for use on adult patients is considered for 'off-label' use on pediatric patients, **the practice should evaluate it on data from the intended pediatric population prior to use**."
- "**Communication and permanent storage of AI outputs is not recommended without qualified end-user incorporation of the output into the standard of care reporting workflow.**"
- Liability: "**Both practices and their qualified end-users ultimately bear responsibility and liability for the care rendered when an AI solution is used.**"
- Foundation models: "not currently regulated by the FDA... considerations... including, but not limited to, **drift and unpredictability, limited clinical validation, and unclear regulatory governance and medical malpractice liability**."

## (d) Sophistication markers
- The most **operationally mature** document in the corpus: drift defined and monitored, PCCPs, model versioning, subgroup change-flags, confidence/uncertainty outputs, rollback/sunset criteria, stop rules, override logging, registry benchmarking (Assess-AI), BAA/Safe Harbor mechanics, downtime reversion, EU AI Act/GDPR awareness, foundation-model caution.
- Pediatric subgroup protections recur across five separate sections — the strongest age-specific regime in the corpus.
- Evidence: references modest (13) but each load-bearing (FDA IFU guide, AAPM TG 273, IAEA physicist guidance, ACR model legislation).
- Mandates: nearly everything is "should," but with governance machinery (minutes, inventories, logs, stop rules) that makes deviations auditable; "required" appears for post-version-change training and vendor IFU (FDA-backed).

## (e) Distinctives vs sibling frameworks
- Only document that treats AI as a **managed clinical asset class** (inventory, lifecycle, rollback) rather than an ethical question — the radiology ecosystem (FDA-cleared devices, registries, physicists) makes this possible.
- The qualified-end-user definition doubles as **model legislation** (ref 7) — ACR is actively statutory-lobbying, a different power move than AMA advocacy.
- Pediatric depth (stop rules on pediatric override rates; adolescent portal release rules) is unmatched.
- Explicit non-liability disclaimer vs FSMB's explicit accountability doctrine — opposite legal postures by design.

## (f) Provisional classification
**progressive-structured (operationally pioneer)** — not conceptually novel, but the deepest implementation regime in the corpus: drift, rollback, stop rules, registries, COI-recommended governance. If pioneer status is awarded for governance execution rather than ideas, this document and FSMB's report are the two contenders. I rate it pioneer-adjacent progressive-structured because it governs one specialty's pipeline rather than the profession's frame.
