---
source: raw/health-systems/uw-medicine--ai-policy-glossary-308g1.pdf.md
source_url: https://depts.washington.edu/comply/docs/308_G1.pdf
publisher: UW Medicine Compliance (Guidance 308.G1, V5.0, revised 8/25/2026)
run: 30
read: full file (333 lines, complete)
---

# UW Medicine — AI Policy Glossary (COMP.308 Attachment A, Guidance 308.G1 V5.0)

## Authority / authorship
- Attachment A to COMP.308, published by UW Medicine Compliance. Versioned (V5.0, Revised 8.25.2026) — actively maintained.
- **Named authors**: "Primary Author: Jason Lau. Contributors: Ana Anderson, Trevor Cohen, Noah Hoffman, Michael Leu, Chen Liang, Gang Luo, Angad Singh, Peter Tarczy-Hornoch, Jennifer Slyker, Karen Segerson." This is a named, multidisciplinary (clinical informatics-heavy) authorship group — biomedical-informatics faculty authorship of an operational glossary is itself a sophistication marker.
- References cite GSA AI guide, UW IT Connect, UW teaching.ethics pages, Cohen/Patel/Shortliffe textbook (2022), Howell BMJ Quality & Safety 2024 review, Stanford HAI glossary, healthit.gov CDS page.

## Philosophy (verbatim framing)
- "There is no universally accepted definition of the term 'Artificial Intelligence', and the extent to which contemporary systems constitute AI is still vigorously debated."
- "use of these approaches does not in and of itself constitute AI, a term that is typically used to refer to systems that aim to emulate or augment human capabilities such as pattern recognition, language use, and decision making."
- Scope note: AI in-scope examples — "1) diagnosis: e.g. automated interpretation of radiological images 2) prognosis: e.g. predicting clinical outcomes, such as sepsis 3) language generation and understanding (including speech recognition)". Out of scope: "1) searching for documents without summarizing or synthesizing them 2) looking for mentions of specific words in notes, without contextualizing or interpreting their meaning 3) triggering an alert when a predefined lab value is elevated."
- "The definitions provided below are intended to provide an approachable guide to interpretation of UW Medicine AI-related policies and guidelines pertaining to such systems."

## Complete verbatim clause inventory (46 defined terms; policy-relevant entries quoted)
1. **Accuracy** — "the degree to which a Model's outputs are correct when compared to ground truth ... Statistical measures that are commonly used include sensitivity, specificity, positive predictive value, area under the receiver operator characteristic (ROC) curve, and area under the precision-recall curve."
2. **Algorithm & Model** — "the algorithm is the process while the model is the trained system resulting from this process..."
3. **Annotations** — labeling "to serve as a 'Ground Truth' or 'gold standard' for training and evaluation for supervised Machine Learning"; retinal-scan example.
4. **Artificial Intelligence System** — applies AI algorithms/models to tasks "that typically require human intelligence ... can perform tasks beyond individual human capabilities, such as processing large datasets at high speeds."
5. **Bias** — "a systematic tendency of an AI tool to produce outputs that are less accurate, favorable, or appropriate for some patients or users"; arises from training data reflecting societal biases AND "the design of AI Systems reflects the values, assumptions, and experiences of the decision makers responsible for their development."
6. **Chatbot**, 7. **Classification** — standard definitions.
8. **Clinical Care** — "a continuum of services performed for a patient by health professionals, or under their direction, for the purpose of promoting, maintaining or restoring health."
9. **Clinical Decision Support** — healthit.gov-derived definition (alerts, guidelines, order sets, diagnostic support...).
10. **Clinical Learning Environment** — "settings where healthcare Learners receive their clinical education ... hospitals, medical centers, ambulatory sites, and virtual spaces."
11. **Computer Vision**, 12. **De-identified Health Information** (per COMP.103 §VI(B)), 13. **Deep Learning** — standard.
14. **Education** — "An encompassing term that includes the Learning Environment and/or involves Learners or Learner data."
15. **Equity** — "the principle of ensuring that AI Systems do not perpetuate or exacerbate social inequities and that outcomes from AI outputs are equitable for all groups. For example, an AI tool designed to detect skin cancer could be less likely to detect skin cancer in individuals with darker skin tones if there is underrepresentation of these individuals in the training data."
16. **Explainability** — "user-friendly explanation of the reasons behind an AI System's output ... to provide an understanding of its decision process."
17. **FERPA** — full definition incl. rights transfer at 18, applicability to postgraduate programs, covered records.
18. **Foundation Model** — "large Machine Learning Model pre-trained on a vast quantity of data ... e.g. GPT-4."
19. **Generative AI**, 20. **Ground Truth** ("may not always reflect the complexity and variability of the real world, so should be reviewed closely for applicability"), 21. **Hallucinations** ("untrue or inaccurate content that is not supported by real-world data ... seems plausible at first glance"), 22. **Honest Broker** (gatekeeper between covered entity and researcher, "serves as the link between HIPAA Privacy and Security") — standard.
23. **Inclusivity** — "Designing and deploying systems that accommodate and represent diverse users ... multilingual support, voice interaction for users with visual impairments, or text-to-speech."
24. **Inference**, 25. **Large Language Model** ("At their core, these models are predicting the next word in a sequence"), 26. **Learner** ("students, residents, fellows, postdocs, and other trainees"), 27. **Learning Environment** (incl. Canvas, Learning Hub), 28. **Limited Data Set**, 29. **Machine Learning**, 30. **NLP**, 31. **Neural Network**, 32. **PHI** — standard.
33. **Predictive Analytics**, 34. **Prompts**, 35. **Reinforcement Learning**, 36. **Research Data**, 37. **Secure UW Medicine Environment** ("Hosted within a UW Medicine data center, cloud data center, or with a contractually authorized partner and undergone a review by UW Medicine IT Services to ensure the required controls are in place") — definitional gate for COMP.308 trigger d.
38. **Segmentation**, 39. **Supervised Learning**, 40. **Training Data Set** — standard.
41. **Transparency** — "The degree to which an AI System's operations and decisions are clear, understandable, and accessible for review or scrutiny by users and stakeholders. Unfortunately, larger and more capable Models are often less transparent."
42. **Transformer** — "'attention' ... GPTs, developed by OpenAI, use this architecture."
43. **Validation Data Set**, 44. **Unsupervised Learning** — standard.
45. **UW Medicine Business Operations** — "healthcare, administrative and business operations supporting both the clinical enterprise and the UW School of Medicine."
46. **UW Medicine Data** — five enumerated classes: Clinical Data (incl. QI data, metadata, reference data, supply chain, lab, referral, patient-level financial); Financial Data; PII; Education Records (FERPA); Research Data; plus "Any other data used for UW Medicine business, clinical, or operations purposes (e.g., legal, IP, confidential/proprietary, trade secret, subject to contractual sharing limitations)." Exclusion: "UW Medicine data does not include UW Medicine information published for public use or has been approved for public use by an appropriate University of Washington authority (see UW Administrative Policy Statement 2.4)."

## Sophistication markers
- **Clinical deployment governance:** the glossary operationalizes COMP.308's triggers — definitional precision (Secure Environment, UW Medicine Data, Clinical Care, Learner) is what makes a risk-screen policy enforceable. This is governance plumbing, deliberately built.
- **Monitoring/validation vocabulary:** ground truth, validation data set, ROC/PPV metrics — evaluation literacy baked into policy language.
- **Model-failure handling:** hallucination and bias definitions are exact and audit-usable.
- **Ambient-scribe consent:** speech recognition appears as an in-scope AI category; no consent rules (by design — glossary only).
- **Clinician liability:** not addressed here.
- Scholarly apparatus: cited references (Shortliffe textbook, Howell 2024) and 10 named informatics contributors — academic-grade rigor attached to a compliance artifact.

## Distinctives
- The only glossary in the corpus with named human authors and external citations.
- Explicit scoping boundary (what is NOT AI — lab-value alerts, keyword search) — preempts governance-scope gaming.
- Ground-truth caveat ("may not always reflect ... the real world") shows unusual definitional honesty.

## Provisional classification
**Pioneer (supporting artifact).** A versioned, faculty-authored, citation-backed operational glossary that makes COMP.308's risk triggers enforceable. Not a standalone policy but evidence of unusually deep governance investment.
