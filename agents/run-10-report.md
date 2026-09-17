# Run 10 report
Agent scope: GME (ACGME, residency/fellowship), specialty societies (ACP, AAFP, AAP, ACR, ACC, AMA GME), institutional GME AI policies, NBME/FSMB beyond collected, foundations (AMA ChangeMedEd, Macy).

Sources saved:
- raw/national-frameworks/acgme--genai-revolution-acgme2024-session.md | ACGME2024 Session Summary: The Generative AI Revolution and Innovations and Opportunities in Medical Education | https://www.acgme.org/newsroom/blog/2024/acgme2024-session-summary-the-generative-ai-revolution-and-innovations-and-opportunities-in-medical-education/ | OK
- raw/national-frameworks/acgme--harnessing-ai-gme-office-acgme2026.md | #ACGME2026 Session Summary: Harnessing AI in the GME Office | https://www.acgme.org/newsroom/blog/2026/03-march/acgme2026-session-summary-harnessing-ai-in-the-gme-office/ | OK
- raw/national-frameworks/acp--ai-provision-of-health-care-position-paper-2024.md | Artificial Intelligence in the Provision of Health Care: An ACP Policy Position Paper (Annals, full text via browser past Cloudflare) | https://www.acpjournals.org/doi/10.7326/M24-0146 | OK (88.5k chars)
- raw/national-frameworks/acp--ethics-professionalism-ai-position-paper-2026.md | Ethics and Professionalism in Artificial Intelligence and Medical Practice: A Position Paper From ACP (Annals, full text via browser) | https://www.acpjournals.org/doi/10.7326/ANNALS-26-01792 | OK (47.5k chars)
- raw/national-frameworks/aafp--ethical-application-ai-family-medicine.md | Ethical Application of Artificial Intelligence in Family Medicine | https://www.aafp.org/about/policies/ethical-ai | OK
- raw/national-frameworks/aap--ai-in-pediatric-health-care.md | Artificial Intelligence in Pediatric Health Care (AAP resource hub + webinar series incl. GenAI for Medical Education in Pediatrics) | https://www.aap.org/en/practice-management/health-information-technology/artificial-intelligence-in-pediatric-health-care/ | OK (short hub page; AAP has no standalone AI policy statement yet)
- raw/national-frameworks/acr-siim--practice-parameter-imaging-ai.md | ACR-SIIM Practice Parameter for Imaging Artificial Intelligence (AI) (first-ever, adopted ACR 2026) + pdf/acr-siim--practice-parameter-imaging-ai.pdf | https://gravitas.acr.org/PPTS/DownloadPreviewDocument?DocId=217 | OK (42.9k chars)
- raw/national-frameworks/acc--ai-action-plan-rfi-comments-2025.md | ACC comments on White House AI Action Plan RFI (clinician autonomy, trust, governance) + pdf | https://www.acc.org/-/media/Non-Clinical/Files-PDFs-Excel-MS-Word-etc/2025/03/ACC-AI-Action-Plan-RFI-Comments_March-15_final.pdf | OK
- raw/national-frameworks/ama--changemeded-ai-medical-education-resources.md | AMA ChangeMedEd AI in medical education resource collection | https://www.ama-assn.org/education/changemeded-initiative/ai-medical-education | OK
- raw/national-frameworks/ama--advancing-ai-medical-education-ethics-evidence-equity.md | Advancing AI in medical education through ethics, evidence and equity (AMA framework) | https://www.ama-assn.org/education/changemeded-initiative/advancing-ai-medical-education-through-ethics-evidence-and-equity | OK
- raw/national-frameworks/ama--medical-educators-guide-ai-learning-analytics.md | The Medical Educator's Guide to Projects Leveraging AI and Learning Analytics (Lomis, Mar 2025) + pdf | https://www.ama-assn.org/system/files/ai-educator-guide.pdf | OK
- raw/national-frameworks/fsmb--recommendations-ethical-ai-clinical-practice.md | FSMB news release on AI recommendations (May 2024) | https://www.fsmb.org/advocacy/news-releases/fsmb-releases-recommendations-on-the-responsible-and-ethical-incorporation-of-ai-into-clinical-practice/ | OK (403 to plain HTTP client; content via extraction layer)
- raw/national-frameworks/fsmb--navigating-responsible-ethical-ai-clinical-practice-report.md | Navigating the Responsible and Ethical Incorporation of AI into Clinical Practice (full FSMB report) + pdf | https://www.fsmb.org/siteassets/advocacy/policies/incorporation-of-ai-into-practice.pdf | OK (32k chars)
- raw/national-frameworks/nbme--ai-in-assessment-executive-summary.md | NBME AI in Assessment: Ethics, Innovation and Research (executive summary) + pdf | https://www.nbme.org/wp-content/uploads/2024/03/AI_in_Assessment_Executive_Summary-dd5.pdf | OK
- raw/national-frameworks/macy-foundation--ai-in-med-ed-grants-program.md | Macy Foundation AI in Medical Education grants program (2025 recipients incl. resident-focused projects) | https://macyfoundation.org/our-grantees/ai-in-med-ed | OK
- raw/health-systems/uw-gme--ai-guidelines-residency-fellowship-applications.md | UW GME AI Guidelines for Residency and Fellowship Applications (updated 12/25) | https://sites.uw.edu/uwgme/ai/ | OK
- raw/health-systems/uchicago-im-residency--clinical-ai-use-policy.md | UChicago Internal Medicine Residency Clinical AI Use Policy (Abridge ambient AI, PGY2-3 only, consent workflow) | https://medchiefs.bsd.uchicago.edu/resources/clinical-ai-use-policy/ | OK

PDFs saved to pdf/: acr-siim--practice-parameter-imaging-ai.pdf, acc--ai-action-plan-rfi-comments-2025.pdf, ama--medical-educators-guide-ai-learning-analytics.pdf, fsmb--navigating-responsible-ethical-ai-clinical-practice-report.pdf, nbme--ai-in-assessment-executive-summary.pdf

Failures:
- https://www.acr.org/News-and-Publications/Media-Center/2026/first-practice-parameter-for-imaging-ai | ACR press page renders via JS; requests got 345-char shell. Dropped (full practice parameter PDF already captured).
- ACP acponline.org "policy library" PDFs are 1-page cover sheets, not the papers; used Annals full text instead.

No policy found (searched, none exists as of 2026-09-17):
- ACC: no dedicated AI health policy statement / GME AI guidance; only 2025 RFI comments, JACC journal AI policies, and an AI resource page. Closest formal doc captured.
- ACGME: no formal AI accreditation standard or policy document; only blog/session summaries (2024, 2026 captured). AI not yet in Milestones/Common Program Requirements.
- AAP: no AI-specific policy statement published (one referenced as "upcoming" in the 2026 Digital Ecosystems statement); resource hub captured.
- Carnegie Foundation: no medical-education AI report found (Carnegie's med-ed work predates genAI; no AI policy located).
- NBME beyond the captured exec summary + existing nbme-usmle--program-discusses-chatgpt: no further standalone AI assessment policy found.

Notes: ACP Annals full texts required a real browser session to pass Cloudflare (plain HTTP and extraction services returned login walls); texts include abstract, full body positions/recommendations and references. UW GME guidelines and UChicago IM residency policy are the two clearest exemplar institutional GME AI policies found (Yale IM AI pathway is a curriculum, not a policy). FSMB full report is the substantive doc; news release kept as companion. Committed as 'run-10: GME + foundations'. Did not touch index.md/metadata/sources.json.
