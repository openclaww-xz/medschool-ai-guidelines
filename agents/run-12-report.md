# Run 12 report
Agent scope: Group F — Brown (Warren Alpert), Boston University (Chobanian), Tufts, Georgetown, George Washington (SMHS), U Rochester, Albert Einstein (Yeshiva), Hofstra (Zucker), Drexel (COM), Thomas Jefferson (SKMC); health systems: Brown Univ Health/Lifespan, Boston Medical Center, Tufts Medicine, MedStar Georgetown, GW Hospital/MFA, UR Medicine, Montefiore Einstein, Northwell, Tower Health, Jefferson Health. (Geisel skipped — done in earlier run.)

Sources saved:
- raw/us-med-schools/bu-chobanian--md-program-ai-use-policy.pdf.md | Artificial Intelligence Use Policy for the MD Program (PDF, eff. 2025-06-26) | https://www.bumc.bu.edu/camed/files/2025/07/AI-Use-Policy-for-the-MD-Program.docx-7.10.25.pdf | OK (binary also at pdf/bu-chobanian--md-program-ai-use-policy.pdf)
- raw/us-med-schools/gw-smhs--md-student-ai-use-guidelines.md | Guidelines for the Use of AI for the MD Program | https://smhs.gwu.edu/academics/md-program/current-students/policies/ai-use-guidelines | OK (full policy w/ task-force purpose, appendices)
- raw/us-med-schools/tufts-university--genai-usage-guidelines.md — FAILED save (page renders empty via requests); replaced by the two IT pages below
- raw/us-med-schools/tufts-university--it-guidance-using-ai.md | Guidance for Using AI at Tufts | https://it.tufts.edu/ai/guidance-using-ai-tufts | OK
- raw/us-med-schools/tufts-university--it-guidelines-use-genai-tools.md | Guidelines for Use of Generative AI Tools | https://it.tufts.edu/guidelines-use-generative-ai-tools | OK
- raw/us-med-schools/tufts-university--genai-guidelines-risks-tools.md | Generative AI Guidelines & Risks of Alternative Tools | https://access.tufts.edu/generative-ai-guidelines-risks-alternative-tools | OK (short page)
- raw/us-med-schools/georgetown-university--ai-guidelines.md | Generative AI at Georgetown (university-wide guidelines) | https://aiguidelines.georgetown.edu/ | OK
- raw/us-med-schools/hofstra--ai-policy-faculty-students.md | AI Policy for Faculty and Students | https://www.hofstra.edu/provost/ai-policy-faculty-students.html | OK
- raw/us-med-schools/hofstra--ai-at-hofstra-overview.md | AI at Hofstra (overview incl. ChatGPT Edu program) | https://www.hofstra.edu/about/ai/ | OK
- raw/us-med-schools/drexel--provost-ai-policies.md | AI Policies (repository page listing PO 103 etc.) | https://drexel.edu/provost/ai/pedagogy-guidance/policies | OK (index-style page, short)
- raw/us-med-schools/drexel--provost-ai-guidance-students.md | AI Guidance for Students | https://drexel.edu/provost/ai/pedagogy-guidance/students | OK
- raw/us-med-schools/drexel--it-genai-guidance.md | IT Generative AI Guidance | https://drexel.edu/it/security/policies-regulations/ai-guidance/ | OK (fetched via headless browser; requests got empty body)
- raw/us-med-schools/u-rochester--provost-genai-use-in-education.md | Generative AI Use in Education | http://rochester.edu/provost/gen-ai-education | OK
- raw/us-med-schools/u-rochester--responsible-use-ai-tools-data-security.md | Responsible Use of AI Tools and Institutional Data Security | https://www.rochester.edu/provost/responsible-use-of-ai-tools-and-institutional-data-security/ | OK
- raw/us-med-schools/u-rochester--libguide-ai-ethics-policy.md | URMC Miner Library AI guide: Ethics & Policy | https://libguides.urmc.rochester.edu/c.php?g=1315586&p=9675179 | OK (via headless browser)
- raw/us-med-schools/albert-einstein--ai-tools-resources.md | AI Tools & Resources (Einstein-approved GenAI tools + user responsibilities) | https://einsteinmed.edu/administration/ai-tools-resources | OK (via Internet Archive; direct 403)
- raw/us-med-schools/brown--provost-ai-resources-course-policy-tools.md | Announcing AI Resources & Course Policy Tools (GAITL) | https://provost.brown.edu/communications/announcing-ai-resources-course-policy-tools | OK
- raw/health-systems/bmc--responsible-ai-statement.md | BMC Health System Responsible AI Statement | https://www.bmc.com/content/dam/bmc/corporate/responsible-ai-statement.pdf | OK (binary at pdf/bmc--responsible-ai-statement.pdf)
- raw/health-systems/jefferson-health--bold-ai-strategy.md | Jefferson Health's Bold AI Strategy (system-wide AI strategy) | https://www.jeffersonhealth.org/about-us/news/2025/09/jh-bold-ai-strategy-to-reclaim-time-empower-clinicians-and-transform-healthcare | OK (via headless browser)
- raw/health-systems/medstar-health--ai-center-of-excellence.md | MedStar Health AI Center of Excellence | https://www.medstarhealth.org/innovation-and-research/ai-center-of-excellence | OK
- raw/health-systems/medstar-georgetown--ai-colab.md | MedStar-Georgetown Collaborative Center for AI in Healthcare | https://www.medstarhealth.org/innovation-and-research/ai-colab | OK

Failures:
- https://www.bumc.bu.edu/camed/offices-services/md-program-offices/medical-education/policies/artificial-intelligence-use-policy-for-the-md-program/ | HTML page returned 0 extractable chars (JS-rendered); recovered full policy from the official PDF instead
- https://ovpe.tufts.edu/initiatives/ai/ai-guidelines/ | empty body via requests; Tufts IT guidance/guidelines pages captured as substitutes
- https://einsteinmed.edu/education/life-einstein/for-students/policies-procedures (and MD Student Handbook) | direct 403, browser-rendered index lists ~15 intranet-token policies, none AI-specific → no dedicated Einstein student AI policy found
- https://georgetown.box.com/s/tm95s608473mngydj69vlkyda1jwxkon | Georgetown SOM "AI Policy" (linked from meded.georgetown.edu educational policies) sits behind Georgetown SSO login wall — cannot capture
- Drexel PO 103 "Academic Integrity Pertaining To Artificial Intelligence" full text | not on open web at a stable URL (policy repository page captured instead)

no_policy_found (searched, nothing that governs med-student/resident AI use):
- Thomas Jefferson / SKMC (school side): no AI usage policy located; only honor code/values pages — Jefferson Health system strategy captured instead
- Albert Einstein: no student/resident AI policy beyond the AI Tools & Resources page (captured)
- Montefiore Einstein (health system): no public AI use policy; only news/PR pages
- Northwell Health (Hofstra's health system): no public AI use policy; only PR/press coverage of ambient AI (Abridge) deployment
- GW Hospital / MFA: no public AI policy
- UR Medicine (health system): no public clinical AI policy; URMC captured via library guide + university provost pages
- Tufts Medicine (health system): no public AI policy; GME pages have none
- Brown University Health / Lifespan (health system): no public AI use policy; only PR on AI health-literacy pilots; Brown acceptable-use IT policy has no AI clause
- Tower Health (Drexel partner): no AI policy found

Notes:
- BU Chobanian is the strongest find: a formal, LCME-mapped "Artificial Intelligence Use Policy for the MD Program" (approved by Medical Education Committee, effective June 26, 2025) — PDF saved to pdf/ and text-extracted.
- GW SMHS AI-use guidelines page contains the full task-force-developed policy text (28k chars) incl. appendices.
- Georgetown SOM's actual "AI Policy" is on Georgetown Box behind SSO; university-wide aiguidelines.georgetown.edu guidelines captured as the accessible substitute. Parent may want to note the Box link for a credentialed fetch later.
- r.jina.ai 401s confirmed; Cloudflare/JS pages were recovered via real browser (Drexel IT, Jefferson Health, URMC LibGuide) or Internet Archive (Einstein).
- Geisel skipped per instructions (already collected in run 01–10 set).
