# Run 02 report
Agent scope: peer-reviewed full texts on AI policies/guidelines in medical education (PMC/publisher, 2023-2026 priority)

Sources saved (raw/peer-reviewed/):
- artificial-intelligence-use-medical-education-best-practices-future.md | Artificial Intelligence Use in Medical Education: Best Practices and Future Directions | https://pmc.ncbi.nlm.nih.gov/articles/PMC12122599/ | OK (CC-BY, full text via Europe PMC XML; Curr Urol Rep 2025)
- analysis-generative-artificial-intelligence-governance-publicly-available-documentation.md | Analysis of Generative AI Governance in Global/Saudi Universities Offering Health Informatics Programs | https://pmc.ncbi.nlm.nih.gov/articles/PMC13525772/ | OK (CC-BY-NC, full text; Adv Med Educ Pract 2026)
- recommendations-clinicians-technologists-healthcare-organizations-use-generative-artificial.md | SGIM Position Statement: Recommendations on Generative AI in Medicine | https://pmc.ncbi.nlm.nih.gov/articles/PMC11861482/ | OK (CC-BY, full text; J Gen Intern Med 2025)
- clinical-teacher-bridging-ai-policy-gap-us-medical-schools.md | Bridging the AI Policy Gap ... US Medical Schools (PMID 41592545) | https://doi.org/10.1111/tct.70347 | PARTIAL — abstract only
- medical-student-experiences-chatgpt-national-cross-sectional-study.md | Medical Student Experiences With ChatGPT: National Cross-Sectional Study | https://pmc.ncbi.nlm.nih.gov/articles/PMC13010067/ | OK (CC-BY, full text; JMIR Form Res 2026)
- competency-framework-medical-ai-education-mixed-methods-study.md | A Competency Framework for Medical AI Education: Mixed Methods Study | https://pmc.ncbi.nlm.nih.gov/articles/PMC13189368/ | OK (CC-BY; JMIR Med Educ 2026)
- ai-literacy-undergraduate-medical-education-competency-based-interpretive.md | AI Literacy in UME: Competency-Based Interpretive Framework | https://pmc.ncbi.nlm.nih.gov/articles/PMC13407777/ | OK (CC-BY; Front Med 2026)
- use-perceptions-generative-artificial-intelligence-tools-first-year.md | Use and Perceptions of GenAI Tools Among First-Year Medical Students | https://pmc.ncbi.nlm.nih.gov/articles/PMC13436551/ | OK (CC-BY-NC; Adv Med Educ Pract 2026)
- medical-students-attitudes-perceptions-self-reported-familiarity-ai.md | Medical Students' Attitudes/Perceptions/Familiarity With AI in Health Care: Systematic Review | https://pmc.ncbi.nlm.nih.gov/articles/PMC13484950/ | OK (CC-BY; JMIR Med Educ 2026)
- current-landscape-curriculum-development-implementation-medical-artificial-intelligence.md | Current Landscape of Curriculum Development in Medical AI: Scoping Review | https://pmc.ncbi.nlm.nih.gov/articles/PMC13546630/ | OK (CC-BY-NC; J Multidiscip Healthc 2026)
- ai-tool-use-osteopathic-medical-students-pilot-digital.md | AI Tool Use Among Osteopathic Medical Students: Pilot Digital Diary Study | https://pmc.ncbi.nlm.nih.gov/articles/PMC13533313/ | OK (CC-BY; JMIR Form Res 2026)
- principles-responsible-ai-health-professions-education-research-care.md | Principles for Responsible AI in Health Professions Education (Health CARE-AI) | https://pmc.ncbi.nlm.nih.gov/articles/PMC13395757/ | OK (CC-BY; JMIR Med Educ 2026)
- ai-uk-medical-education-framework-curriculum-reform.md | AI in UK Medical Education: A Framework for Curriculum Reform | https://pmc.ncbi.nlm.nih.gov/articles/PMC13263032/ | OK (CC-BY; JMIR Med Educ 2026)
- prevalence-content-generative-artificial-intelligence-use-policies-iranian.md | Prevalence/Content of GenAI Use Policies in Iranian Medical Science Journals | https://pmc.ncbi.nlm.nih.gov/articles/PMC13404226/ | OK (CC-BY-NC-SA; 2026) [policy-prevalence survey method analogue]
- role-differentiated-ai-competencies-curriculum-implications-health-professions.md | Role-Differentiated AI Competencies and Curriculum Implications | https://pmc.ncbi.nlm.nih.gov/articles/PMC13552830/ | OK (CC-BY; JMIR Med Educ 2026)

Failures:
- PMID 41592545 (Bridging the AI Policy Gap, Clin Teach 2026) | No PMCID; isOpenAccess=N; Wiley publisher page returned HTTP 403 (subscription). Saved as abstract-only partial, clearly marked, NOT fabricated full text.

Notes:
- All 14 PMC full texts fetched via Europe PMC REST fullTextXML endpoint (pmc.ncbi.nlm.nih.gov links in front-matter source_url); converted JATS XML -> markdown; tables preserved as markdown tables, figures noted as omitted. Each file has required YAML front-matter with license noted.
- Verified each file non-empty (24k-69k chars) and containing methods/results/discussion substance, not nav/cookie text.
- No files under raw/ pre-existed; no collisions. Did not touch metadata/sources.json, index.md, README.md. No push.
- CONCURRENT-AGENT NOTE: this repo is shared by parallel runs. The 14 Europe-PMC full-text files
  under raw/peer-reviewed/ were committed by a concurrent agent's broad `git add` in commit
  ce4a5d3 ("run-03") before my commit ran; my commit 6ab8cf4 ("run-02: peer-reviewed full texts")
  contains agents/run-02-report.md, the Clin Teach abstract file, and several files other agents
  left untracked. Content is intact and verified; only commit attribution is mixed.
