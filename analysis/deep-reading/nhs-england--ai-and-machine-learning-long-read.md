---
source_file: raw/international/nhs-england--ai-and-machine-learning-long-read.md
read_status: full
approx_words_read: 1100
---

# NHS England — Artificial intelligence (AI) and machine learning (long read, GP Good Practice Guidelines)

## (a) Authority and authorship
- Publisher: NHS England; part of "Working in a digitally transformed NHS" section of the **Good practice guidelines for GP electronic patient records**. Versioned: "Version 1.2 28 March 2025"; published 14 June 2023, last updated 7 April 2025.
- Authority: national health-system operational guidance for general practice — advisory-in-form but infrastructurally anchored (it points to the NHS AI Lab, AI Dictionary, AI Award winners, DART-Ed). Device regulation is explicitly elsewhere (MHRA).

## (b) Policy philosophy
- Posture: **managed adoption with validation-first discipline**. Framing verbatim: "To achieve its potential, **AI must be developed in a regulated way, and as a collaboration between clinicians, software engineers, data scientists and product designers**."
- Workforce prediction: "It is predicted in the **NHS AI Lab roadmap** that **general practice will be one of the most affected workforce groups in the NHS**."
- Maturity sequencing: early challenges = data quality, information governance, proof of concept; "As these initial challenges are overcome other factors will grow in importance such as **workflow integration, demonstrating evidence of real-world clinical effectiveness and providing ongoing safety**."

## (c) Complete clause inventory
1. Context/examples clause: AI used for COVID-19 chest-imaging diagnosis; secondary-care dermatology referrals ("skin analytics"); AI Award winners in retinal screening and antimicrobial stewardship; "Symptom checkers such as **NHS 111 online** are also trialling AI to help with triage."
2. Regulated-development clause (verbatim in (b)).
3. Maturity-sequence clause (verbatim in (b)).
4. IG clause: information governance issues on NHS England pages; government guide on digital/data-driven health technologies.
**Tips when implementing AI:**
5. Evidence-base clause: **Understanding healthcare workers' confidence in AI (2022)** NHS report — "essential reading" on adoption barriers.
6. Change-management clause: "Staff may be reluctant to adopt AI technologies if they feel threatened, if they are worried about the risks, or if they do not see enough evidence of effectiveness. They need to be brought onboard so that those who are worried **feel empowered to shape how the technology can used to support them**."
7. Standards clause: "NHS and GP organisations are working to regulate and design standards that support developers... minimum standards that enable greater confidence"; GPs "actively involved in this process to shape how technology is used."
8. Research clause: "Ongoing research into the impact of algorithms on decisions is needed so that clinicians can be appropriately educated."
9. Validation gate: "implementation **must only be carried out when there has been robust clinical validation**."
**Key considerations when planning AI in general practice:**
10. **Patient engagement**: "The patient must be at the centre when assessing and implementing any new technologies. Care must be taken to ensure **algorithms don't exacerbate inequalities or introduce new discrimination**." Worked bias example verbatim: "an algorithm developed to detect melanoma was trained on publicly available images which are more prevalent in white skin. As a result, it was **more accurate in detecting melanoma in white skin than black**."
11. **EHIA clause**: "**Equality and health impacts assessment (EHIA)** should be used to mitigate risks of discrimination and exacerbating health inequalities."
12. **Model cards clause**: "Information on the way AI algorithms are created and tested needs to be **shared with healthcare teams**. **Used for a different purpose or on a different population, AI will produce misleading and potentially harmful results**... a '**model cards**' or '**model facts**' label has been proposed, showing key information, and explaining to users an algorithm's capabilities and limitations **including the characteristics of the training data set**."
13. **Risk management**: "Caution should be employed with new technology. What are the risks with the real-life application of this software and how can they be minimised?"
14. **Post-market surveillance clause**: "**Post-market surveillance is essential, as with any new medication or medical device.** Medical device incidents or near misses should be reported to the manufacturer and the **MHRA via the Yellow Card reporting system**."
15. **Wider impacts clause**: "unanticipated effects on clinical workload, care pathways and payment mechanisms. For example, if symptom checkers are to risk averse, workload may increase. Similarly, **indeterminate results thrown up by algorithms may increase the need for additional diagnostic investigations**."
16. Resource signposts: "Artificial Intelligence: How to get it right"; "A Buyer's Guide to AI in Health and Care"; related GPG topics (health equalities/inclusion, interoperability, population health management, genomics, medical devices, CQRS); resources: Ada Lovelace Institute, AnalystX, **DART-Ed** (NHS education programme for AI/robotics workforce needs); reports: AMRC AI in Healthcare; RCGP/BJGP 2019 AI and Primary Care; Reform Trust; **ICO + Alan Turing Institute "Explaining decisions made with AI"**; **2019 Topol review**; NHS "vision for AI in healthcare"; GDS public-sector AI guide; FDA + UK gov Guiding Principles to AI.

## (d) Sophistication markers
- **Distribution-shift literacy**: "Used for a different purpose or on a different population, AI will produce misleading and potentially harmful results" — the corpus's most explicit statement of out-of-distribution failure, plus training-data characteristics disclosure via model cards.
- Pharmacovigilence-transposed post-market surveillance with a named reporting channel (MHRA Yellow Card) — AI treated on the safety apparatus of medicines/devices.
- Workload/pathway iatrogenics (risk-averse symptom checkers increase workload; indeterminate results cascade investigations) — systems-level second-order thinking absent elsewhere.
- Real bias case (melanoma in darker skin) rather than abstraction; EHIA as the mitigation instrument.
- Named external evidence ecosystem (Topol, Turing/ICO, Ada Lovelace, AMRC) — deepest bibliography in the corpus.

## (e) Distinctives vs sibling frameworks
- The operational clinical-care counterpart to the UK education documents (GMC, joint regulators): same professional-judgment model, applied to practice adoption rather than learners.
- Only document pairing model cards + Yellow Card + EHIA — the full lifecycle-safety toolkit at GP level. Singapore's AIiHGLE (separate note) systematizes this at national-guideline scale; NHS England's version is embedded in frontline GP workflow guidance.

## (f) Provisional classification
**cautious-informed** — deeply risk-literate, evidence-anchored, safety-system-integrated; adoption-positive but validation-gated. The strongest "informed" technical document in the corpus.
