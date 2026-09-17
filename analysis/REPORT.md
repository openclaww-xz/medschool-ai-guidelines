# Generative-AI Policy in Medical Education: A Synthesis of 378 Sources

**Basis.** This report synthesizes the full corpus of this repository: 378 collected raw sources
(`index.md`; `metadata/sources.json`) — 26 national frameworks, 212 US medical-school/university documents,
67 health-system/teaching-hospital documents, 47 peer-reviewed full texts, and 26 international documents
(`index.md` section counts) — plus PDF snapshots under `pdf/`. Structured clause extraction covers 274 US
school and health-system documents recorded in `analysis/clauses.csv` (extended by run-23 after the
report was drafted; counts in Sections 1 and 7 cite both vintages where they differ). Descriptive
statistics were computed in R (`analysis/figures.Rmd`, figures in `analysis/figs/`). Every claim below
cites the file it rests on. Where the clause matrix and the raw text disagree, both are reported.

---

## 1. Landscape overview: what actually exists

The corpus contains four distinct layers of governance material, and they are very unevenly matched.

**National frameworks are abundant but non-binding.** The 26 documents in `raw/national-frameworks/`
include the AAMC's *Principles for the Responsible Use of AI in and for Medical Education*
(`raw/national-frameworks/aamc--principles-ai-use.md`), the AMA's augmented-intelligence principles and
AI-literacy policy (`raw/national-frameworks/ama--ai-principles.md`,
`raw/national-frameworks/ama--ai-literacy-medical-education-policy.md`), AMEE Guides 158 and 178 on
ethics and assessment (`raw/national-frameworks/amee--guide-158-ethical-use-ai-hpe.md`,
`raw/national-frameworks/amee--guide-178-ai-hpe-assessment.md`), NBME's assessment executive summary
(`raw/national-frameworks/nbme--ai-in-assessment-executive-summary.md`), USMLE's ChatGPT statement
(`raw/national-frameworks/nbme-usmle--program-discusses-chatgpt.md`), LCME re-visioning materials
(`raw/national-frameworks/lcme--strategic-re-visioning-standards-2025.md`), ACP and FSMB clinical-AI
position papers (`raw/national-frameworks/acp--ai-provision-of-health-care-position-paper-2024.md`,
`raw/national-frameworks/fsmb--navigating-responsible-ethical-ai-clinical-practice-report.md`), and a
WHO-Europe readiness report (`raw/national-frameworks/who-europe--ai-reshaping-health-systems-readiness.md`).
None of these is an accreditation requirement; LCME's document is a conference session on strategic
re-visioning, not a standard.

**Formal school policy is the rarest layer.** Of the 161 extracted US documents, only 37 (23.0%) are
formal, numbered/named policies; 113 (70.2%) are guidance of some kind (guides, IT pages, hub pages),
6 (3.7%) are handbook sections, and 5 (3.1%) are curricular descriptions (`analysis/findings.md` §1;
`analysis/summary-stats.md`). In other words, roughly seven in ten documents that govern a medical
student's AI use in this corpus are web guidance that can be silently edited or removed, not policy
that requires a governance process to change.

**Health-system documents skew toward marketing and governance descriptions, not clinician rules.**
The 66 documents under `raw/health-systems/` include genuine governance instruments — Mount Sinai's
AI implementation and use policy (`raw/health-systems/mount-sinai-health-system--ai-implementation-and-use-policy.md`),
UW Medicine's COMP.308 (`raw/health-systems/uw-medicine--comp308-use-of-ai.md`), Duke's ABCDS oversight
process (`raw/health-systems/duke-health--abcds-oversight-process.md`), OHSU's AI governance page
(`raw/health-systems/ohsu-health--ai-governance.md`) — but the sector split in the clause matrix
(26 classified health-system rows vs 119 UME rows; `analysis/summary-stats.md`) shows the extractable
*rules* concentrate on the student side.

**Peer-reviewed literature exists but lags practice.** The 47 full texts under `raw/peer-reviewed/`
are dominated by surveys and position analyses; the AAMC's own IT-survey executive summary reports
that few schools had written policies at survey time
(`raw/national-frameworks/aamc--girl-survey-ai-executive-summary.md`).

---

## 2. A typology of policy models

Close reading of the corpus yields five recurring models. They differ on the default rule, the unit
of governance (tool vs use vs assessment), and who holds authority to permit.

### Model 1 — Default-permit with carve-outs
The dominant posture. AI use is permitted for learning, with prohibitions listed for specific risky
uses. Einstein's model is characteristic: two institutionally approved tools (ChatGPT Edu, enterprise
Copilot) for everyone, with restrictions carried by tool tier rather than use case
(`raw/us-med-schools/albert-einstein--ai-tools-resources.md`). Most guidance pages in the corpus
(113/161 documents are guidance; `analysis/findings.md` §1) fit here: permissive tone, banned-use
list, no enforcement machinery.

### Model 2 — Default-prohibition unless the instructor permits
The strictest UME model. Geisel's numbered policy **UME-CNTRL-0019** (effective Aug 1, 2025) states:
"Unless explicitly stated by the instructor, students are not permitted to utilize generative AI"
in coursework, and bars uploading Geisel course materials unless explicitly allowed
(`raw/us-med-schools/geisel-dartmouth--genai-educational-environments-policy.pdf.md`). Keck/USC's
policy (approved Dec 17, 2025) applies a targeted version of the same default to assessment:
"prohibited for assignments, activities, and other required coursework that is intended to evaluate a
student's own knowledge, reasoning, skills or reflections unless explicitly permitted by the course
director or supervising faculty" — a violation of the Code of Professional Behavior if breached
(`raw/us-med-schools/usc-keck--medical-student-genai-tools-policy.md`). Stanford's MD policy is a
softer relative: AI use "discouraged" for evaluated activities absent faculty permission
(`analysis/clauses.csv`, row `raw/us-med-schools/stanford-md--genai-policy-3-32.md`).

### Model 3 — Assessment-tier classification ("lane" systems)
Rules attach a classification label to every assessment, with a defined default. UCSF runs the most
developed examples: the PharmD policy defines **AI-1 (Disallowed), AI-2 (Restricted), AI-3
(Documented)** and rules that "If an assessment or deliverable does not have a classification
provided, it is assumed to be classified AI-1"
(`raw/us-med-schools/ucsf-som--pharmd-ai-assessments-policy.md`); the IGHS policy applies the same
scheme with an explicit "unclassified work defaults to AI-Disallowed" rule and grading deductions for
unverified AI facts (`raw/us-med-schools/ucsf-som--ighs-ai-policy.md`). ECU Brody's SOP requires every
graded assignment to carry a Green/Yellow/Red tier in the syllabus, with AI barred on Red-tier and
proctored work (`raw/us-med-schools/ecu-brody--responsible-use-of-ai.md`; tier detail in
`analysis/clauses.csv` row for that file). MUSC's framework is an adaptation of the published AI
Assessment Scale (Perkins et al. 2024), "contextualized for health sciences education" and approved
through Education Advisory, Student Affairs, and Provost councils
(`raw/us-med-schools/musc--ai-acceptable-use-framework-page.md`,
`raw/us-med-schools/musc--acceptable-use-framework.pdf-sourced.md`). Icahn MSSM requires every
syllabus to state a permitted-use level (`raw/us-med-schools/icahn-mssm--student-ai-policy.md`);
Johns Hopkins assigns GenAI-use categories per course component
(`raw/us-med-schools/johns-hopkins-som--student-guidance-genai.md`).

### Model 4 — Acceptable-use routing through professionalism machinery
VCU's School of Medicine policy ("Acceptable Use of Generative Artificial/Augmented Intelligence (AI)
Applications Policy") permits use where course/clerkship directors articulate acceptability, requires
acknowledgement of AI assistance, and routes violations through the Valued Interactions and
Professionalism (VIP) process under the Professionalism Policy, citing LCME Standard 3.5
(`raw/us-med-schools/vcu-som--acceptable-use-generative-ai-applications-policy.md`; clause row in
`analysis/clauses.csv`). Columbia treats instructor-prohibited AI use as "unauthorized assistance
and/or plagiarism" while cautioning that AI detection is "a guideline not a grading metric"
(`raw/us-med-schools/columbia-vagelos--university-genai-policy.md`). This model's signature is that
enforcement borrows existing honor-code/professionalism channels rather than inventing new ones.

### Model 5 — Approved-tool carve-outs (the enterprise exception)
The counter-model to blanket PHI bans: PHI is *permitted* inside institutionally contracted tools.
UCSF's Bridges curriculum policy allows its Azure-hosted ChatGPT Enterprise "including patient care
activity at UCSF Health sites because it is HIPAA compliant and approved for UCSF data including
patient information" (`raw/us-med-schools/ucsf-som--bridges-curriculum-genai-usage-policy.md`).
Michigan's guideline approves U-M GPT, Maizey, and M365 Copilot "for use with data classified as
high (e.g., PHI)" (`raw/us-med-schools/umich-medical-school--acceptable-ai-use-guideline.md`;
`raw/health-systems/michigan-medicine--using-ai-tools-at-mm.md`). OHSU's GME-48 permits PHI/PII
"only … into OHSU prior-approved AI tools," backed by an institutional registry of approved and
prohibited tools (`raw/us-med-schools/ohsu-som--gme-48-ai-use-in-gme.md`). GW SMHS states the model's
logic negatively: PHI "may not be entered into public or non-approved AI tools"
(`raw/us-med-schools/gw-smhs--md-student-ai-use-guidelines.md`) — the *approval boundary*, not AI
itself, is the regulatory line.

A structural finding cuts across all five models: the single most common prohibition is **tool-based
rather than use-based** — 33/161 rows ban entering data into public or unapproved tools
(`analysis/findings.md` §2).

---

## 3. PHI and confidentiality clauses

Only 63 of 161 extracted documents (39.1%) contain any substantive PHI/patient-data rule; the
extractor recorded the rest as blank or "none" (`analysis/findings.md` §3). (Counting convention
matters: `analysis/summary-stats.md` reports 87 non-empty `phi_rule` cells, which includes literal
"none" notations.) Of the 63, 25 name HIPAA explicitly, and 7 rows extend to FERPA — e.g., Harvard's
"Comply with regulations such as HIPAA, FERPA, and sponsor-specific data requirements"
(`raw/us-med-schools/harvard-hms-it--generative-ai-guidelines.md`), and OHSU's blanket "Never input
Protected Health Information (PHI), FERPA-protected student data … or other restricted or
private/sensitive information" (`raw/us-med-schools/ohsu--libguides-genai-student-guide.md`).

The prohibitive language clusters into graded intensities, verbatim from the sources:

- **Criminal framing** — UCSF: entry of patient or student information "is a violation of UCSF
  policies and potentially a crime" (`raw/us-med-schools/ucsf-som--ighs-ai-policy.md`).
- **Strict prohibition** — Stanford MD policy: "The use of patient-identifying information or
  protected health information (PHI) in public AI tools is strictly forbidden"
  (`raw/us-med-schools/stanford-md--genai-policy-3-32.md`).
- **Categorical never** — Buffalo/Jacobs: "AI tools must never be used to input, analyze, or transmit
  identifiable patient information" (`raw/us-med-schools/buffalo-jacobs--genai-use-policy-medical-students.md`);
  BU: "Patient information should never be put into any LLM or AI tool (including Terrier GPT) as
  they are not HIPAA compliant" (`raw/us-med-schools/bu-chobanian--md-program-ai-use-policy.pdf.md`);
  Keck: "it is never permissible to enter patient protected health information into a generative AI
  tool unless explicitly approved and sanctioned by the applicable health system and clinical setting"
  (`raw/us-med-schools/usc-keck--medical-student-genai-tools-policy.md`).
- **De-identification-insufficient** — Penn Medicine: patient data "even if deidentified … may not be
  exposed to open or public AI tools or services, absent institutional approval"
  (`raw/health-systems/penn-medicine--isc-ai-guidance.md`). CUIMC takes the data-classification
  route: anything that "could identify a patient … may only be entered into tools approved for
  Sensitive Data" (`raw/health-systems/cuimc--ai-and-generative-technology-use.md`).
- **De-identification carve-out** — Yale counsels using "de-identified or synthetic data instead of
  actual patient data" wherever possible (`raw/us-med-schools/yale--using-ai-safely-health-care.md`).

The Model-5 carve-out cluster (UCSF, Michigan, OHSU; §2 above) is the doctrinal opposite of the
"categorical never" group, and the corpus shows both operating inside the same university systems —
UCSF bans PHI on commercial platforms in one document
(`raw/us-med-schools/ucsf-som--bridges-curriculum-genai-usage-policy.md`) while permitting it on its
own enterprise instance in the same policy. For a drafter, the lesson is that "PHI into AI" is no
longer a single rule: the live question is *which contractual boundary (BAA, enterprise tenant)
the tool sits inside*, as Utah's rule makes explicit — PHI requires BAA-covered vendors
(`raw/us-med-schools/uutah--ai-use-guidelines-2026.md`,
`raw/us-med-schools/uutah--ai-use-guidelines-it-perspective.md`).

---

## 4. Assessment and academic-integrity rules

Assessment rules are present in only 38/161 documents (23.6%) and are almost exclusively a UME
phenomenon: 18 UME documents ban AI on exams/quizzes/assessments versus 1 health-system document
(`analysis/findings.md` §2; per-sector rates in `analysis/summary-stats.md`, 34/119 UME vs 2/26 HS
documents with any assessment clause).

Three mechanisms recur:

1. **Assessment-scoped bans.** Baylor's surgery clerkship bans AI on written work "specifically
   designed to assess a student's clinical reasoning or knowledge"
   (`raw/us-med-schools/baylor-cm--surgery-clerkship-ai-guidance.pdf.md`); Mayo's respiratory-care
   program bans AI on any exam/quiz question
   (`raw/us-med-schools/mayo-mccms--respiratory-care-handbook-genai-policy.md`); Buffalo permits AI
   on assessments "only where use explicitly allowed by course/clerkship director"
   (`raw/us-med-schools/buffalo-jacobs--genai-use-policy-medical-students.md`).
2. **Default-deny classification** (Model 3 above): UCSF's AI-1/AI-2/AI-3
   (`raw/us-med-schools/ucsf-som--pharmd-ai-assessments-policy.md`), ECU's tiers
   (`raw/us-med-schools/ecu-brody--responsible-use-of-ai.md`), MUSC's AIAS adaptation
   (`raw/us-med-schools/musc--ai-acceptable-use-framework-page.md`).
3. **Detection skepticism + honor-code integration.** Columbia explicitly demotes AI-detection scores
   to "a guideline not a grading metric" (`raw/us-med-schools/columbia-vagelos--university-genai-policy.md`);
   Pitt's 2026 academic-integrity policy covers "formative and summative exams, OSCEs, and graded
   assignments" (`raw/us-med-schools/pitt-som--academic-integrity-policy-genai.pdf.md`); VCU routes
   breaches to professionalism review (`raw/us-med-schools/vcu-som--acceptable-use-generative-ai-applications-policy.md`).

One-off integrity rules worth noting: UNC bars AI meeting summaries without participants' consent;
UT Austin invokes Texas state law against autonomous consequential decisions; NIH peer-review AI bans
are repeated at Harvard, UAB, UChicago, and U Iowa (`analysis/findings.md` §2). Disclosure
requirements appear in 77/161 documents (47.8%) but stated enforcement in only 60 (37.3%) — most
guidance pages name no consequence at all (`analysis/findings.md` §7).

---

## 5. The GME–UME gap

Only 6/161 extracted documents govern residents/fellows: OHSU GME-48, UChicago's IM residency
Abridge policy, NYU Grossman (students + residents), UCSF Bridges (students + GME + staff), a UW GME
announcement, and Einstein (postdocs) (`analysis/findings.md` §5). GW SMHS *explicitly excludes* GME
from its UME guidelines, which "do not apply to Graduate Medical Education (GME), residency or
fellowship training, admissions or selection processes … all of which are governed by separate
institutional, hospital, or accrediting-body policies"
(`raw/us-med-schools/gw-smhs--md-student-ai-use-guidelines.md`).

The two worlds regulate different objects. GME/health-system documents govern **clinical
documentation and ambient scribes** — UChicago's residency program permits Abridge only for direct
patient encounters in approved settings (`raw/health-systems/uchicago-medicine--im-residency-clinical-ai-use-policy.md`);
Dartmouth Health requires ambient-documentation consent; U Chicago IM even bans PGY-1 use of Abridge
entirely (`analysis/findings.md` §2) — plus **approval registries and governance committees** (OHSU's
registry in `raw/us-med-schools/ohsu-som--gme-48-ai-use-in-gme.md`; Duke ABCDS in
`raw/health-systems/duke-health--abcds-oversight-process.md`; Mount Sinai's policy in
`raw/health-systems/mount-sinai-health-system--ai-implementation-and-use-policy.md`). UME documents
govern **assessments and academic integrity** (18 vs 1 assessment bans; `analysis/findings.md` §2).
GME instruments are also more formal — numbered policies like OHSU "GME-48" and UW "COMP.308" —
whereas UME leans on handbook sections and guidance pages (`analysis/findings.md` §5). The practical
consequence: a student moving from medical school into residency crosses a regulatory cliff, from
integrity-framed rules to documentation-framed rules, usually without any bridging document. UTSW's
GME-application guidance (Dec 2025) and the ACGME session summaries in
`raw/national-frameworks/acgme--harnessing-ai-gme-office-acgme2026.md` gesture at the gap but
neither closes it.

---

## 6. International contrast

The UK, Singapore, and Australia illustrate three alternative regulatory architectures, none of which
the US corpus replicates.

**UK — professional standards, not institutional policy.** The GMC deliberately declines to issue
AI-specific rules: doctors must "use their professional judgment to apply the principles in our
guidance to the use of innovative technologies or AI tools," with responsibility resting with the
doctor for decisions taken with AI, and disclosure to patients of uncertainties and limitations
(`raw/international/gmc--ai-and-innovative-technologies.md`, anchored in
`raw/international/gmc--good-medical-practice-2024.md`). The joint UK regulators' statement and the
Council of Deans' GenAI principles extend this principle-first approach to education
(`raw/international/uk-joint-regulators--statement-ai-in-education.md`,
`raw/international/council-of-deans-health--principles-genai-healthcare-education.md`). Contrast: US
schools write tool-and-assessment rules; the UK writes decision-maker obligations.

**Singapore — lifecycle governance by role.** MOH's AIHGle 2.0 (published March 2026) allocates
duties across developers, deployers, and users, with a risk-assessment framework and mandated staff
training (`raw/international/sg-moh--ai-in-healthcare-guidelines-aihgle-2-0.md`). No US document in
the corpus attempts role-split lifecycle governance; the closest analogues are health-system approval
committees (Duke ABCDS; `raw/health-systems/duke-health--abcds-oversight-process.md`).

**Australia — assessment-architecture reform.** The University of Sydney's "two-lane" policy (Nov 27,
2024) restructures assessment itself: "secure, in-person assessments" plus "appropriately designed
'open' assessments that support the use of all available and relevant tools"
(`raw/international/u-sydney--ai-assessment-policy-two-lane.md`; FAQ in
`raw/international/u-sydney--two-lane-assessment-faq.md`). This is a step beyond the US's labeling
models (§2 Model 3): rather than tagging each assessment, it redesigns the assessment portfolio.
Australia's AMC has framed AI-and-ethics as strategic since its 2018–2028 plan
(`raw/international/amc-australia--ai-ethics-impact-annual-report.md`). Other useful comparators:
Karolinska's student guidelines (`raw/international/karolinska--student-guidelines-generative-ai.md`),
Amsterdam UMC (`raw/international/amsterdam-umc--ai-topic-overview.md`), Toronto's AI-ready-university
guidelines (`raw/international/uoft--ai-ready-university-guidelines.md`), and Amsterdam's whole-university
framework (`raw/international/uva--policy-framework-genai-in-education.md`).

---

## 7. Adoption timeline and the AAMC-alignment paradox

Only 52–53 of 161 documents carry any parseable date, and dated adoption grows monotonically:
2023 (7), 2024 (11), 2025 (13), 2026 to date (21) (`analysis/findings.md` §6;
`analysis/summary-stats.md`; Figure 1, `analysis/figs/fig1-adoption-timeline-1.png`). The corpus
captures the genre shift across those cohorts: 2023's first wave is IT-shaped (VUMC network block,
Yale provost guidelines, UCSF PharmD policy; `analysis/findings.md` §6); 2025–2026 produces
medical-school-specific formal policy (Geisel UME-CNTRL-0019 effective Aug 1, 2025; Keck approved
Dec 17, 2025 — dates in the source files' front matter; Perelman UME policy Jul 21, 2026; ECU Brody
SOP Mar 1, 2026; Buffalo Jacobs Mar 31, 2026 — `analysis/findings.md` §6). The oldest ancestor is
Minnesota's 2015 Statement of Intellectual Responsibility, whose AI addendum is undated
(`raw/us-med-schools/umn-medical-school--intellectual-responsibility-ai-addendum.md`).

**The paradox.** The AAMC published *Principles for the Responsible Use of AI in and for Medical
Education* (dated January 3, 2025 in Geisel's citation), and the document is in the corpus
(`raw/national-frameworks/aamc--principles-ai-use.md`). Yet the clause matrix records exactly **1 of
161** school/system documents citing it: UTSW's library guide, which links both the education
principles and the residency-selection principles
(`raw/us-med-schools/utsouthwestern-libguides--ai-medical-healthcare-education.md`;
`analysis/findings.md` §4). One caveat from manual verification: Geisel's policy *does* open by
following "the guiding principles set forth by the Principles for the Responsible Use of Artificial
Intelligence in and for Medical Education … dated January 3, 2025"
(`raw/us-med-schools/geisel-dartmouth--genai-educational-environments-policy.pdf.md`), but its CSV row
records `aamc_alignment = no` (`analysis/clauses.csv`) — an extraction miss. So the honest count is
"at most 2 of 161" (1.2%): a national framework that virtually no institutional policy anchors to,
even when (as at Geisel) it demonstrably shaped the drafting. National-level principles are being
written and not cited; institutional policy is being written from scratch, school by school.

---

## 8. What is still missing

The `no_policy_found` records in the run logs are themselves data. Verified absences include:

- **Whole schools without any public AI-use policy**: Mayo Clinic Alix School of Medicine
  (`agents/run-06-report.md`), Vanderbilt SOM (`agents/run-07-report.md`), UC San Diego SOM and UCI
  School of Medicine (`agents/run-16-report.md`), Cleveland Clinic Lerner College of Medicine and
  Rosalind Franklin (`agents/run-17-report.md`), Meharry (`agents/run-18-report.md`). SHSU-COM's
  entire 2026–27 student handbook was verified to contain zero AI mentions
  (`agents/run-18-report.md`; `raw/us-med-schools/shsu-com--student-handbook.md`).
- **Health systems with governance but no public rule**: Baylor St. Luke's, UPMC, OSU Wexner, M Health
  Fairview (`agents/run-07-report.md`); Banner, OU Health, UNM Health, KU Health
  (`agents/run-16-report.md`); Loyola Medicine, UC Health Cincinnati, SLUCare (`agents/run-17-report.md`);
  Grady and Nashville General (`agents/run-18-report.md`).
- **Policies that exist but are gated**: UW Health (intranet U-Connect), Rush (UAC0039 behind login,
  `agents/run-17-report.md`), UC Davis Health's full guidelines PDF (SharePoint-auth,
  `agents/run-16-report.md`), Georgetown Box link permanently gated (`agents/run-19-report.md`),
  BCM's Policy & Procedures Manual (intranet-only, `agents/run-07-report.md`).
- **HMS and UCLA DGSOM** have no school-specific MD AI policy beyond IT guidance and university
  provost guidelines (`agents/run-04-report.md`).

Structural gaps in the *documents that do exist*: only 23.6% state any assessment rule and 37.3% any
enforcement (`analysis/summary-stats.md`); 98/161 documents say nothing about PHI
(`analysis/findings.md` §3); almost nothing governs AI in admissions/selection (Pitt's report flags it
as a recommendation, `raw/us-med-schools/pitt-som--adhoc-committee-genai-report.md`; GW excludes it,
`raw/us-med-schools/gw-smhs--md-student-ai-use-guidelines.md`); and only OHSU's PA program bars AI
use "to evaluate, rank or score applicants unless institutionally approved"
(`raw/us-med-schools/ohsu-som--pa-program-use-of-genai-policy.md`).

---

## 9. Implications for a program drafting a guideline today

Synthesizing the strongest mechanics across the corpus, a defensible 2026 guideline would:

1. **Number it and date it.** Formal, numbered policies (Geisel UME-CNTRL-0019; OHSU GME-48; UCSF
   Bridges) are the genre the field converged on in 2025–26 — and only 23% of documents are formal
   (`analysis/findings.md` §1).
2. **Pick a default and say which model it is.** Default-prohibit-unless-permitted (Geisel) is
   cleaner to enforce; tiered-labeling (UCSF/ECU/MUSC) is more flexible but requires every syllabus
   to carry a label and defines the unclassified default explicitly — UCSF's "unclassified = AI-1"
   rule (`raw/us-med-schools/ucsf-som--pharmd-ai-assessments-policy.md`) is the mechanism to copy.
3. **Write the PHI clause around the approval boundary, not the technology.** Name the approved
   enterprise tools and the contractual basis (BAA/tenant), as UCSF, Michigan, and Utah do (§3), and
   state the de-identification rule explicitly (Yale/Penn language, §3).
4. **Route enforcement through existing professionalism/honor machinery** with a stated consequence —
   VCU's LCME-3.5-anchored VIP routing (`raw/us-med-schools/vcu-som--acceptable-use-generative-ai-applications-policy.md`)
   — because half the corpus demands disclosure while naming no consequence.
5. **Do not rely on AI detectors as grading evidence** (Columbia's explicit demotion, §4).
6. **Bridge the UME–GME cliff explicitly** — say what carries into residency documentation rules
   (UChicago's Abridge policy is the template, `raw/health-systems/uchicago-medicine--im-residency-clinical-ai-use-policy.md`)
   — and cover admissions/selection uses, which almost nobody does.
7. **Cite the AAMC principles** (`raw/national-frameworks/aamc--principles-ai-use.md`) — nearly
   nobody does (§7), which is precisely the alignment gap a new policy can close for free.

### Limitations

Counts derive from `analysis/clauses.csv`, whose extraction conventions (blank = absent; "none"
recorded verbatim; 25 late-arriving files extracted from snippets) are documented in
`analysis/findings.md` §8; the Geisel/AAMC extraction miss (§7) shows why spot-verification matters.
Undated guidance pages (109/161) mean the timeline reflects *dated* documents only
(`analysis/summary-stats.md`). Absence findings are absences of *public* policy; several institutions
govern AI behind logins (§8), so "no policy found" never proves "no policy exists."

*Generated by run-25 synthesis, 2026-09-17. Regenerate all figures with
`Rscript -e 'rmarkdown::render("analysis/figures.Rmd")'`.*
