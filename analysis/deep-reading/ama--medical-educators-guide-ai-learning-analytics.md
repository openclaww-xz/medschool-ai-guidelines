---
source_file: raw/national-frameworks/ama--medical-educators-guide-ai-learning-analytics.md
read_status: full
approx_words_read: 2631
---

# AMA — The Medical Educator's Guide to Projects Leveraging Artificial Intelligence and Learning Analytics (Kimberly D. Lomis, MD; Mar 2025)

## (a) Authority and authorship
- Publisher: AMA; sole named author **Kimberly D. Lomis, MD** (AMA VP Medical Education Innovations, leader of ChangeMedEd). A 9-page practical guide with suggested citation and full reference list — the most authorially accountable document in the corpus.
- Powers claimed: none; advisory guide for "medical educators" building AI/learning-analytics projects "across the continuum of medical school, residency, and practice." Its authority is pedagogical and reputational.

## (b) Policy philosophy
- Posture: **responsible-builder enablement** — teaches educators to be competent procurers/co-designers, guarding against both vendor capture and magic-wand thinking. Framing quotes:
  - "Medical educators are enthused about the potential to leverage artificial intelligence, learning analytics, and other emerging technologies to improve medical training and promote **precision education**... However, **many educators lack experience in developing and deploying such technologies**."
  - "it is critical to assemble **multi-disciplinary teams**... to ensure responsible development and deployment."
  - Anti-shiny-thing: "an intriguing technological advance can lure teams to instead seek a place to apply the '**shiny thing**,' especially when approached by **vendors with a solution to sell**."

## (c) Complete clause inventory (by the guide's seven sections)
**1. Problem Definition**
1. "Clearly articulating what burden is to be relieved or what advancement is desired is critical to maintaining focus."
2. "**Gathering input from stakeholders (learners, supervisors, patients) and engaging them in co-production** will clarify how the envisioned initiative could make a meaningful impact."
**2. Affordances of Technology**
3. "A common pitfall is to **reproduce old models in new digital formats**. While such an approach may offer convenience or efficiency, it is limiting. Emerging technologies should drive us to think entirely differently about a given task."
4. "educators are at risk of **envisioning AI as a magic wand that makes everything possible**... Active dialogue with technical experts, as well as engaging learners or other stakeholders in co-production, should **avoid premature closure**."
**3. Data Considerations**
5. "educators **must take deliberate action to promote trust** in the quality, application, and protection of the data being used. Educators should ask about **data provenance, measurement, and quality** issues."
6. Features/NLP: "Are those features in structured data fields, or will it be necessary to create a process to extract them (such as natural language processing, NLP)? **Monitoring the performance of an algorithm may reveal a need to change features or alter the weighting of features to fine-tune the tool.**"
7. Annotation: "if training an algorithm to review images of pathologic specimens... the training data would include examples labelled as normal or abnormal. In education, we would similarly need to label data samples as correct/incorrect... **Experts can be engaged to annotate sufficient samples, although this can be resource intensive.**" Workaround example: "the ICD and CPT codes registered by the physician of record... could be considered the 'correct' answer to which the learner's work is compared."
8. Representativeness: "training an algorithm against expert performance **may not provide nuanced understanding of appropriate novice performance** among early learners."
9. Bias mechanism: "**Technological solutions are not inherently biased, but the data sets on which they are trained — or the way that development teams identify features of interest — commonly have inherent bias that could be amplified by an application.**"
10. Access: "Educational teams must consider access to sufficient data not only for initial training of an algorithm, but also for **monitoring and continued refinement**"; connect with "chief medical informatics officers (CMIOs)"; "**Application programming interfaces (APIs)** facilitate this process, but teams should account for this process in project timelines and budgets. Potential **federated structures** that allow for training on data sets across institutions without sharing sensitive data can also be explored."
11. Protection: "Educational applications could involve **protected health information, learner data protected under FERPA**, and data about supervisors... **Educators must exercise caution that sensitive data is not exposed through integration of systems.** The concept of an **education data warehouse** can be applied at the institutional level."
12. "Educators **have a duty** to ensure data will be managed appropriately and **should ask technical colleagues or vendors** how this issue will be addressed **prior to pursuing each project**."
**4. Limitations of Technology** (pitfall catalog)
13. "Bias in data sets used for training and validation or bias in the process of data preparation."
14. "Potential **inequities in access to tools, application of tools, and outcomes associated with tools**."
15. "**Non-stationarity of data** — a term that reflects the inconsistency in how health care and educational data may be recorded over time or in one setting versus another, **impacting the performance of a model**." — data-drift concept, named precisely.
16. "**Confounding inputs or label leakage** — if the labels of interest... inadvertently contaminate the data set such that the algorithm can 'see' the answer, a model **may appear to perform better than it actually does**." Worked example: chest X-ray severity tool keying on **supine vs upright position** — canonical ML failure case imported into med-ed guidance.
17. "**Overtraining** refers to providing too much oversight during model development, resulting in **lack of external validity** when handling data beyond the training set." [Note: guide's usage is idiosyncratic — this describes overfitting.]
18. "User error: Well-intentioned actors may misuse the technology or misapply its outputs due to a lack of training. **Malicious actors may deliberately tamper with a system to alter outputs.**"
19. "An activity referred to as **'red teaming**,' in which stakeholders actively try to 'break' the application, can be useful to anticipate pitfalls."
**5. Costs**
20. "educators **should push for clarity around their business model** to understand both immediate and long-term costs. They should also address **whether the vendor will capture institutional data that could be used for other purposes**." — data-capture-in-vendor-contracts clause.
21. Cost list: "Computing power/cloud services; Programmer services; Data management; Subject matter experts for data annotation; Statistical analysis; Subscription and licensing fees, such as for large language models (LLMs); Integration costs (APIs) and IT effort; Hardware (especially for AR/VR...); Legal fees for contracts and data agreements; Evaluation costs associated with continuous monitoring."
**6. Implementation Science**
22. "**Trust must be earned.** It is important to consider the human-AI collaboration needed for an intervention to be successful."
23. "The **human-in-the-loop concept requires that educational leaders deploying novel technologies embrace accountability and actively engage in monitoring tool performance over time.**"
24. "**Learners interacting with new tools should be recruited to assist in co-production and monitoring** of altered educational workflows as well as new technologies."
25. "**To avoid the perception of a surveillance state, educators should ensure that data is used to benefit stakeholders.**" — surveillance framing, unique in corpus.
26. "Data-driven solutions are particularly vulnerable to context. Variations in workflows and stakeholder incentives impact the feasibility and accuracy of implementation... educators should clarify whether the context for which the tool was originally developed **algins** [sic] with their intended use case."
27. "Interpretability and explainability are common challenges... Developers, especially commercial vendors, may be hesitant to share proprietary intellectual property, but **educators should press for an understanding of how predictions or recommendations are formulated**."
**7. Responsible Deployment**
28. "Educators pursuing technological solutions **have a duty beyond the development phase to ensure responsible deployment and ongoing monitoring**."
29. "Stakeholders interacting with a given tool **must understand enough about how the technology works to recognize problems**."
30. "Users should be recruited to aid in continuous monitoring and refinement of tools. **Resources must be devoted to upskilling all involved.**"
31. "Institutional structures **should include an organizational committee that articulates guiding principles**... Local teams should review, clarify, and publicize their institutional process."
32. "**Institutional assets, such as safe AI playgrounds or enterprise-sanctioned generative pre-trained transformers (GPTs), can support experimentation while protecting intellectual property, health information, and learner data.**"
33. "Training, to include foundational knowledge coupled with active application experiences such as **prompt-a-thons and red-teaming exercises**, is essential."
**Canon cited**: NAM "AI for Health Professions Educators" (Lomis co-author, 2021); Russell et al. "Competencies for the Use of AI-Based Tools" (Acad Med 2023); AMA learning series; **BEME Guide No. 84**; two precision-education papers; AMA Advancing AI (2023); **AAMC Principles**.

## (d) Sophistication markers
- **The most technically sophisticated document in the corpus.** Names and explains: non-stationarity (data drift), label leakage with a worked radiology example, overfitting (as "overtraining"), red teaming, federated training, FERPA/PHI dual protection, enterprise GPT sandboxes, vendor data-capture risk, surveillance-state risk. No other national-body text teaches failure modes at this depth.
- Evidence: real citation base (NAM, Acad Med competencies, BEME scoping review); worked examples rather than assertions.
- Mandates: duty-language twice ("have a duty"), several must/should; still advisory, but the strongest duty-framing outside FSMB.
- Assessment-validity: implicit (label leakage/validity of "correct" labels), not assessment-security.

## (e) Distinctives vs sibling frameworks
- Only document that treats the educator as a **procurement-literate co-developer** (vendor negotiation, budget lines, contract law).
- Surveillance-state clause and learner co-production of monitoring are unique.
- Minor flaw: "overtraining" defined as overfitting — a terminology error an expert committee would have caught; sole-author risk.

## (f) Provisional classification
**pioneer** (practitioner-tooling niche) — converts everyone else's principles into an operational checklist with real ML literacy. Where AAMC principles gesture "Monitor and Evaluate," this guide explains label leakage. The single best artifact of genuine AI understanding among the US national bodies.
