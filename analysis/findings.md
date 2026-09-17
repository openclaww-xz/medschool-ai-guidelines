# Findings: cross-cutting patterns in US med-school / health-system AI policy sources

Basis: `analysis/clauses.csv` — 275 rows (208 `raw/us-med-schools/`, 67 `raw/health-systems/`).
Covers every US source on disk as of run 23 (runs 12–22 gap-fill included; one legacy row,
`uw-medicine--ai-in-healthcare-policy.md`, was renamed by run 19 to `comp308-use-of-ai.md`
and appears under its old filename). Every count below is derived from the CSV; blank CSV
fields mean the source document does not state the item (nothing was inferred).

## 1. Formal policy vs guidance

| Instrument | Rows | Share |
|---|---|---|
| Guidance (guides, IT pages, announcements, hub pages) | 193 | 70.2% |
| Formal policy (numbered/named policy, SOP, approved program policy) | 59 | 21.5% |
| Handbook section | 13 | 4.7% |
| Curricular (program/course descriptions) | 10 | 3.6% |

- UME-side sources: 49/208 (23.6%) formal policies vs health systems 10/67 (14.9%).
- 90/275 rows (32.7%) carry any explicit effective/approval date; several of those are
  news or revision dates rather than true effective dates — most guidance pages are undated.
- Where dates exist they cluster: 2015 (1, the UMN ancestor), 2023 (7), 2024 (18), 2025 (23),
  2026 to date (38) — dated adoption roughly doubles each year, with 2026 already the
  largest cohort.

## 2. Commonest banned uses (themes across `banned_uses`)

Counts = rows whose banned_uses text matches the theme (rows can match several).

| Banned use | UME (n=208) | Health systems (n=67) | All (n=275) |
|---|---|---|---|
| Public/unapproved/unvetted AI tools (esp. with institutional data) | 38 | 8 | 46 |
| AI on exams/quizzes/assessments | 34 | 1 | 35 |
| PHI / patient identifiers into AI tools | 25 | 5 | 30 |
| Clinical documentation (H&P, notes) by AI outside approved systems | 14 | 1 | 15 |
| Submitting AI work as one's own / plagiarism | 14 | 0 | 14 |

- The single most common prohibition pattern is still **tool-based** (public vs approved),
  not use-based: 46/275 rows ban entering data into public or unapproved tools.
- Assessment bans remain almost exclusively a UME phenomenon (34 vs 1).
- New one-off bans added by runs 12–22 worth noting: Howard 100-022 bars University Data
  being used to *train* AI models; Touro bans *agentic* AI for all graded assessments;
  UC San Diego privacy guidelines bar AI assistants "attending" meetings on one's behalf;
  U Arizona (both campuses) bars AI-written H&Ps; UMass Chan bars ambient scribes without
  course-director permission; UNR Med bars using AI to de-identify PHI (reverse-engineering
  risk); JABSOM bars AI-generated differential diagnoses/treatment plans outright.
- NIH peer-review AI bans now appear at Harvard, UAB, UChicago, U Iowa, Cincinnati, SLU,
  UNMC, UNM (8 sources).

## 3. PHI clause language clusters

- 108/275 rows (39.3%) contain any PHI/patient-data rule; 167 say nothing the extractor
  could capture (blank or `none`).
- Of those 108, language clusters by verb modality:
  - "never" formulations ("never input", "never be put into", "never sharing"): 8
  - "must not"/"may not"/"shall not"/"cannot" formulations: 16
  - "only into approved tools" (permissive-with-guardrail, e.g. OHSU GME-48, CUIMC,
    U-Mich, UAMS, UCI Health, UVM, UMass Chan, U Kentucky): 11
  - explicit "public" tools named as the danger: 11
  - de-identification/synthetic-data carve-outs (UCSF, Yale, Sinai, UC Davis Health,
    JABSOM, UVM): 8
- 51 of the 108 PHI clauses name HIPAA explicitly; 22 also mention FERPA.
- Notable strict formulations: UCSF ("potentially a crime"), Stanford ("strictly forbidden"),
  Buffalo ("AI tools must never be used to input, analyze, or transmit identifiable patient
  information"), BU ("Patient information should never be put into any LLM or AI tool
  (including Terrier GPT) as they are not HIPAA compliant"), Penn ("even if deidentified …
  may not be exposed to open or public AI tools"), UVM ("Inputting NPPD into an open system
  is considered a breach of data security laws, such as HIPAA and the Vermont Data Breach
  Notification law"), LSUHSC-NO (never place PHI in non-approved AI tools).
- Counter-pattern: 4 sources explicitly *permit* PHI inside institution-approved enterprise
  tools (UCSF ChatGPT Enterprise, U-Michigan U-M GPT/M365 Copilot, UTSW HIPAA-compliant
  ChatGPT, UCI Health Abridge/Epic-embedded) — the "approved-tool carve-out" cluster.
- New clear PHI exemplars from the extension: UCI Health ("Claims that an AI tool is
  'HIPAA compliant' do not mean it is approved for use at UCI Health"), UAMS (PHI only with
  AI Governance Committee approval + fully executed BAA), UC Davis SOM ("Under no
  circumstances should PHI be entered into any generative AI tool outside of a secure,
  institutionally supported system").

## 4. AAMC alignment

- Only 1/275 rows cites AAMC AI principles: `utsouthwestern-libguides--ai-medical-healthcare-education.md`
  links both the *AAMC Principles for the Responsible Use of AI in and for Medical Education*
  and the *AAMC Principles for Responsible AI in Medical School and Residency Selection*.
- 5 further rows cite AAMC for non-AI purposes (Baylor surgery clerkship Core EPAs; Utah
  SoM EPAs/MSOP/VSLO; Penn State COM EPAs; Wake Forest SOM Careers-in-Medicine and
  AAMC/ERAS MSPE timeline) — recorded as "no" for AI alignment.
- Despite an AAMC principles document existing in the corpus (national-frameworks), **school
  and system policies essentially never anchor to it (1/275, 0.4%)** — still the clearest
  gap finding, and it survived a +114-row corpus expansion.

## 5. GME vs UME differences

- 11/275 rows apply to residents/fellows/GME trainees/postdocs: OHSU GME-48, UChicago IM
  residency Abridge policy, NYU Grossman (students+residents), UCSF Bridges
  (students+GME+staff), UW GME announcement, Einstein (postdocs), JABSOM (learners incl.
  UH residents/fellows), UAMS (trainees incl. residents/postdocs), Advocate Health RFI
  (2,000+ residents/fellows context), Meharry-Oracle partnership, UW GME application
  guidelines. GW SMHS explicitly *excludes* GME from its UME guidelines; GME is governed
  separately.
- Substance differs: GME/health-system documents govern **clinical documentation and ambient
  scribes** (Abridge at UChicago/UPMC/Yale/Weill Cornell/UC Davis/UCI; DAX at VUMC/UVA/
  Nebraska/Temple/SSM/Advocate; Ambience at Cleveland Clinic) and **approval registries/
  governance committees** (OHSU registry, Duke ABCDS, Mount Sinai AIRB, MedStar TRUSTED/
  AIRB, UCLA, Michigan TSPs, UAMS AI Governance Committee, UK ADVANCE/Demand Management),
  while UME documents govern **assessments and academic integrity** (assessment bans
  34 UME vs 1 HS).
- GME policies remain more likely to be formal and numbered (OHSU "GME-48", UW "COMP.308",
  MSHS P&P, Howard "100-022", UAMS "2.1.6", UVM "645.00", SLU v3.1) whereas UME relies
  more on handbook sections and guidance pages.

## 6. Dating / adoption timeline (from the 90 dated rows)

- Pre-GenAI ancestor: UMN Statement of Intellectual Responsibility (2015 revision; AI addendum undated).
- 2023 first wave (7): VUMC network block (Jun 2023), CWRU SoM assignment policy (Aug 3, 2023),
  Yale provost guidelines (Sep 20, 2023), UCSF PharmD AI policy (Oct 18, 2023), UNC GMB guidance
  (Jul 2023), Vanderbilt (effective Jan 2024), Geisel coursework (effective Jul 1, 2024,
  drafted late 2023).
- 2024 consolidation (18): Buffalo/PSOM precursor guidance, UW-Madison policies (Aug 2024),
  NYU Grossman (Aug 2024), Northwestern Feinberg policy approved Dec 4, 2024, UCSF Bridges
  (Dec 10, 2024), Dartmouth coursework (Jul 2024), Temple (Sep 2024), Pitt report (Mar 2024),
  Hartford AI center launch (Feb 2024), UConn guidance (Mar 2024), Arizona Tucson student
  AI policy (Nov 13, 2024), Cleveland Clinic Ambience rollout (Feb 2024).
- 2025 maturation (23): Icahn MSSM policy (Sep 2025), Geisel UME-CNTRL-0019 (effective Aug 1,
  2025), Keck/USC policy (Dec 17, 2025), BU MD program (Jul 10, 2025), JABSOM learner
  guidelines (May 2025), UVM Larner Policy 645.00 (Jul 15, 2025), VCU SoM, UW GME
  application guidelines (Dec 2025), HopGPT launch (Dec 2025), Jefferson AI strategy
  (Sep 2025).
- 2026 explosion to date (38): OHSU GME-48 (Feb 12, 2026), Perelman UME policy (Jul 21, 2026),
  UNC OMSE (Jul 2026), Pitt SoM academic-integrity (Mar 24, 2026), ECU Brody SOP (Mar 1, 2026),
  Buffalo Jacobs (Mar 31, 2026), Utah system guidelines (Sep 2026), UW COMP.308 (Aug 25, 2026),
  Howard 100-022 (Apr 24, 2026), SLU policy v3.1 (Aug 19, 2026), UC Davis SOM coursework
  policy (Apr 2026), UNR Med (Jan 8, 2026), VCU system policy adopted Nov 12, 2025, MUSC,
  Brown, GW SMHS, Rush UAC0039, Touro AI addendum (Jan 1, 2026 syllabus deadline) — i.e.,
  the field moved from "IT guidance" (2023) to "medical-school-specific formal policy"
  (2025–2026), with 2026 alone now contributing 38 of 90 dated rows.

## 7. Other cross-cutting counts

- Disclosure/acknowledgement clause present: 131/275 (47.6%).
- Explicit enforcement/consequences stated: 118/275 (42.9%) — most guidance pages have none.
- Named secure/enterprise tools: 132/275 (48.0%). Most-named: ChatGPT/Edu variants (75),
  Microsoft Copilot (54), Claude (26), Gemini (21), Epic-embedded tools (13), DAX/Dragon
  ambient (6), Abridge (9), Adobe Firefly (5), Harvard AI Sandbox (4), HopGPT (3), UCSF
  Versa (3), OpenEvidence (3), UpToDate (2).
- Institutional-pattern: nearly every research university routes users to an
  enterprise/tenant instance (Copilot with university login remains the most common single
  recommendation), while free-standing medical schools more often issue use-based rules
  without naming tools.
- New tool patterns from the extension: WVSOM restricts to M365 Copilot as the *only*
  permitted GenAI tool; UNR Med makes Copilot the approved tool with a required attestation
  for any non-Copilot use; UCI Health explicitly permits Abridge and Epic-embedded AI for
  PHI while naming DoxGPT/ChatGPT/OpenEvidence as prohibited for clinical queries.

## 8. Caveats

- `doc_type` reflects the document's self-presentation (titled "Policy", numbered SOP, etc.).
- The 114 rows added by run 23 were extracted from full captured text via the run-15
  keyword-window method; thin pages (index/hub pages, patient-facing brochures) legitimately
  have mostly blank fields. Several new rows are news/announcement or partnership pages
  (Cleveland Clinic, Jefferson, Hartford, Advocate RFI, Meharry-Oracle) with narrative
  rather than policy content.
- One row (`raw/health-systems/uw-medicine--ai-in-healthcare-policy.md`) refers to a file
  renamed in run 19 to `uw-medicine--comp308-use-of-ai.md`; the current file has its own
  row, so UW Medicine policy is covered under both names.
- `bmc--responsible-ai-statement.md` is BMC *Software*'s corporate responsible-AI statement
  (likely a collector misattribution for Boston Medical Center) — retained as collected.
- phi_rule entries are verbatim or lightly ellipsised quotes from the source; bracketed
  ellipses mark cuts. Typos in sources (e.g. "HIPPA", "You should not be used generative
  AI tools" in the UC Davis Health guidelines) are preserved verbatim.
