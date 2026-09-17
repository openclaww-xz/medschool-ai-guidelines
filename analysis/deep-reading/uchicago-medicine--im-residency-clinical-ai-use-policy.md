---
source: raw/health-systems/uchicago-medicine--im-residency-clinical-ai-use-policy.md
source_url: https://medchiefs.bsd.uchicago.edu/resources/clinical-ai-use-policy/
publisher: University of Chicago Medicine Internal Medicine Residency Program
run: 30
read: full file (105 lines, complete)
---

# UChicago Medicine — IM Residency Clinical AI Use Policy (Abridge)

## Authority / authorship
- Program-level policy authored by the **IM residency program (chief residents/program leadership)** — not a health-system policy. Department-of-medicine governance over trainees; attending supervision rules anchor it clinically. Annual reassessment each June by the program.

## Philosophy (verbatim framing)
- "This policy defines the approved use of AI/Abridge by residents ... to support clinical documentation during patient encounters while ensuring patient consent, data integrity, and appropriate supervision."

## Complete verbatim clause inventory
1. Scope: "eligible Internal Medicine residents using AI/Abridge during direct patient encounters in approved clinical settings."
2. Approved settings: "Continuity clinic; Urgent/Immediate care clinic; Inpatient rotations; ED."
3. "Use of Abridge outside of direct patient encounters (e.g., teaching rounds, handoffs, case conferences, evaluations, or informal discussions) is not permitted."
4. "Only PGY-2 and PGY-3 residents will be eligible to register for and use Abridge."
5. "Prior to first use, eligible residents must complete a program-designated ambient AI orientation covering consent workflows, documentation review expectations, and common AI error patterns. Completion will be tracked by the program coordinator."
6. "Eligibility will be reviewed yearly."
7. "PGY-1 residents (interns) are not permitted to use Abridge."
8. "Attending physicians retain standard supervisory responsibility for all documentation."
9. "AI-assisted notes are subject to the same expectations for review, attestation, and accuracy as traditional documentation."
10. **Consent (per-encounter, all parties, charted):** "Residents must obtain verbal consent from the patient prior to using Abridge at each encounter. For visits involving family members or other third parties in the room, verbal consent must be obtained from all participants."
11. "Consent must be documented in the medical record using the standard '.ABRIDGEVERBALCONSENT' smartphrase."
12. "If a patient declines consent, Abridge must not be used, and the declination must be documented in the medical record."
13. "Patients may decline without impact on their care."
14. "Abridge-generated content is intended to support documentation only."
15. "Residents are fully responsible for reviewing Abridge output for accuracy, completeness, and appropriateness."
16. "Residents must correct any errors, omissions, or inaccuracies prior to forwarding to attending faculty for attestation."
17. "Use of Abridge does not replace clinical judgment or professional responsibility."
18. "Residents should meaningfully edit and synthesize AI-generated content."
19. "Residents should not rely on AI output without verification"
20. "Use of Abridge must comply with all institutional privacy, security, and HIPAA policies."
21. "Recording without patient consent is strictly prohibited."
22. "Ambient AI may only be used on hospital-issued mobile devices or personal devices that meet the institution's mobile device management (MDM) and encryption requirements."
23. **Anti-passive-recording rule:** "The resident must be physically present in the room during the entire recording duration to prevent 'passive' recording of private family conversations."
24. "AI-generated content and audio recordings must not be used for teaching, research, or external sharing unless explicitly approved through appropriate institutional processes."
25. "Use of Abridge within the Internal Medicine Residency Program will be revisited and reassessed in annually in June. Continued approval may be modified or revoked based on program evaluation, compliance, or institutional guidance."
26. "Failure to comply with this policy may result in revocation of Abridge access and may be addressed through residency program professionalism or disciplinary processes, as appropriate."
27. **Other AI:** "Residents should NEVER put Protected Health Information (PHI) into non UCM approved AI models (Chat GPT, Claude, Gemini, DoxGPT etc) · Approved AI systems can be found on the UCM Intranet these include but are not limited to Phoenix AI, UpToDate, etc"
28. "Residents are encouraged to use Open Evidence or other medical based search engines that link to primary articles or reviewed literature for searching medical content"
29. "Other Ambient Listening Scribe technology (i.e. Doximity Scribe) are not allowed"

## Sophistication markers
- **Ambient-scribe consent rules: the gold standard of this run** — per-encounter verbal consent; consent of ALL third parties present; EHR smartphrase documentation of consent; documented declination; explicit no-care-impact assurance; recording-without-consent prohibited; resident physical-presence requirement to prevent passive capture.
- **Clinician liability positioning:** two-tier — residents fully responsible for output accuracy and meaningful editing; attendings retain standard supervisory responsibility and attestation; "AI-assisted notes are subject to the same expectations for review, attestation, and accuracy as traditional documentation" (documentation-liability equivalence — AI confers no special shield or new duty).
- **Training gate:** mandatory orientation on "consent workflows, documentation review expectations, and common AI error patterns" before access; completion tracked; PGY-1 exclusion (supervision-caliber judgment gate).
- **Deployment governance:** program-level approval pipeline (setting allowlist, eligibility, annual reassessment, revocable approval, device/MDM requirements, secondary-use ban, competitor-scribe ban).
- **Monitoring:** annual program reassessment + compliance-based revocation; no performance monitoring of the model itself.

## Distinctives
- The only policy in this corpus that operationalizes ambient-scribe consent to the smartphrase level.
- PGY-tiered eligibility and physical-presence rule — workflows designed around real failure modes (passive recording of family conversations).
- Named prohibited alternatives (Doximity Scribe, DoxGPT) and named approved tools (Phoenix AI, UpToDate).
- Residency-program (not enterprise) authorship — governance can live at the training-program layer.

## Provisional classification
**Pioneer (ambient-scribe operational governance tier).** Narrow scope (one program, one vendor) but the deepest operational consent + liability + training + device controls in this run. A model policy other systems could adopt verbatim.
