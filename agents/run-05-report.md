# Run 05 report
Agent scope: University of Michigan Medical School, Yale, Duke, Washington University in St. Louis, NYU Grossman, Cornell (Weill), Northwestern (Feinberg); health systems Michigan Medicine, NYU Langone, NYP/Weill Cornell, Duke Health, Northwestern (NM), BJC/WashU.

Sources saved:
- raw/us-med-schools/umich-medical-school--acceptable-ai-use-guideline.md | Guideline: Acceptable AI Use at the University of Michigan Medical School (KB0036135) | https://michmed.service-now.com/kb?id=kb_article_view&sysparm_article=KB0036135 | OK (JS-rendered ServiceNow page captured via browser; ~13KB full guideline)
- raw/health-systems/michigan-medicine--using-ai-tools-at-mm.md | Using Artificial Intelligence (AI) Tools at MM (KB0023639) | https://michmed.service-now.com/kb?id=kb_article_view&sysparm_article=KB0023639 | OK (JS-rendered)
- raw/us-med-schools/yale--ai-standards-health-sciences.md | Yale Standards for Using AI Tools and Chatbots in Health Sciences | https://ai.yale.edu/yales-ai-tools-and-resources/yale-standards-for-using-ai-tools-and-chatbots-in-health-sciences | OK (hub page; accordion content lives in 2 sub-pages saved separately)
- raw/us-med-schools/yale--using-ai-safely-health-care.md | Using AI Safely and Responsibly in Health Care and Research | https://ai.yale.edu/yales-ai-tools-and-resources/health-sciences/using-ai-safely-and-responsibly-in-health-care | OK
- raw/us-med-schools/yale--choosing-right-ai-tool.md | Choosing the Right AI Tool for Clinical Health Care and Research | https://ai.yale.edu/yales-ai-tools-and-resources/health-sciences/choosing-the-right-ai-tool | OK
- raw/us-med-schools/yale--provost-genai-guidelines.md | Guidelines for the Use of Generative AI Tools | https://provost.yale.edu/news/gguidelines-use-generative-ai-tools (correct URL below) | OK
  -> source_url in file: https://provost.yale.edu/news/guidelines-use-generative-ai-tools
- raw/us-med-schools/duke--ai-guidelines-and-tools.md | Guidelines and Tools (AI at Duke) | https://ai.duke.edu/ai-resources/guidelines-policies-and-ai-tools/ | OK
- raw/health-systems/duke-health--abcds-oversight-process.md | ABCDS Oversight Process | https://healthaigovernance.duke.edu/abcds-oversight/abcds-oversight-process | OK
- raw/us-med-schools/washu--office-of-education-ai-guidance.md | WashU Addresses AI Technology | https://education.med.wustl.edu/washu-addresses-ai-technology/ | OK
- raw/us-med-schools/nyu-grossman--education-genai-guidelines.md | Guidelines for the Educational use of Generative AI Tools (IIME, rev. 2024-08-13) | https://navigator.med.nyu.edu/static/Education_Generative_AI_Guidelines.pdf | OK (PDF saved to pdf/nyu-grossman--education-genai-guidelines.pdf; 2 pages, text extracted)
- raw/us-med-schools/weill-cornell--ai-ethics-responsible-use.md | Ethics, Policy & Responsible Use of AI (LibGuide) | https://med.cornell.libguides.com/ai/ethics | OK
- raw/us-med-schools/weill-cornell--mededai-wcm.md | MedEdAI @ WCM (AI competencies in medical education) | https://teach.weill.cornell.edu/medical-education/mededai-wcm | OK
- raw/health-systems/nyp-weill-cornell--ai-at-nyp-wcm-copilot.md | AI at NYP/WCM (Copilot LibGuide) | https://med.cornell.libguides/ai/copilot (correct URL in file) | OK
- raw/us-med-schools/northwestern-feinberg--genai-tools-policy.md | Use of Generative AI Tools - Medical Student Policy (LCME 3.5, approved 12/4/2024) | https://www.feinberg.northwestern.edu/md-education/docs/policies/professionalism-learning-environment/use-of-generative-ai-tools-policy.pdf | OK (PDF saved to pdf/northwestern-feinberg--genai-tools-policy.pdf)
- raw/us-med-schools/northwestern-feinberg--galter-genai-guide-students.md | For Students - Generative AI Guide (Galter Library) | https://libguides.galter.northwestern.edu/c.php?g=1389126&p=10274753 | OK
- raw/us-med-schools/northwestern--it-genai-guidance.md | Northwestern Guidance on the Use of Generative AI | https://www.it.northwestern.edu/about/policies/guidance-on-the-use-of-generative-ai.html | OK

No policy found (absence is data):
- Washington University in St. Louis (School of Medicine): NO med-student-specific or school-specific generative-AI policy findable. Closest sources: university-wide IT guidance ("WashU Addresses AI Technology", saved), WashU IT AI pages (ChatGPT Edu, procurement/risk-assessment guidance — not learner policy), and Ombuds medical student policies index (no AI mentions). WashU/BJC activity is curricular/research (Center for Health AI, AIHealth institute), not usage policy.
- NYU Langone Health (health system): NO public health-system-wide generative-AI usage policy findable. Best available is the NYU Grossman IIME educational guidelines PDF (saved) which self-describes as "not an official policy of NYU Langone or NYU Grossman School of Medicine". NYU Langone AI pages are program descriptions, not policy.
- Northwestern Medicine (NM, health system): NO public NM-specific generative-AI clinical-use policy findable; saved the Northwestern University IT guidance as the governing document. NM's public AI presence is news/radiology PR, not policy.
- Duke School of Medicine (education side): NO SOM-specific AI usage policy findable. Duke's AI-in-education rules live in university-level pages (AI at Duke + Duke Community Standard, saved); the SOM bulletin policy index has no AI policy. Health-system side is governed by ABCDS Oversight (saved).
- Michigan Medical School students are covered by the Michigan Medicine KB guideline (saved under us-med-schools) plus Michigan Medicine IT KB (health-systems). No separate UMMS-only document found beyond the KB guideline.

Failures:
- https://michmed.service-now.com/kb?id=kb_article_view&sysparm_article=KB0036135 | Direct fetch (Exa/curl) returned only "Loading..." SPA shell — recovered via browser rendering; content captured fully.

Notes:
- Two pdf/ AAMC stub files (aamc--girl-survey-ai-executive-summary.pdf, aamc--meeting-the-moment.pdf) pre-existed as 3KB HTML error pages from another run; left untouched (hard rule 1).
- Concurrent runs (run-01 etc.) were committing to the same working tree while I worked; my files may have been swept into another run's commit. I commit only my files explicitly. Two Yale sub-page files were uncommitted before my commit.
- Yale ai.yale.edu hub page's accordion sub-pages contain the substantive rules; saved as separate files so each URL maps to one file.
