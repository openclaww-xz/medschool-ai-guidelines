# Findings: cross-cutting patterns in US med-school / health-system AI policy sources

Basis: `analysis/clauses.csv` — 161 rows (121 `raw/us-med-schools/`, 40 `raw/health-systems/`).
Every count below is derived from the CSV; blank CSV fields mean the source document does not
state the item (nothing was inferred). Extractions were run over the full `raw/` tree at the
end of collection (includes late-arriving files from runs 12–13).

## 1. Formal policy vs guidance

| Instrument | Rows | Share |
|---|---|---|
| Guidance (guides, IT pages, announcements, hub pages) | 113 | 70.2% |
| Formal policy (numbered/named policy, SOP, approved program policy) | 37 | 23.0% |
| Handbook section | 6 | 3.7% |
| Curricular (program/course descriptions) | 5 | 3.1% |

- UME-side sources: 31/121 (25.6%) formal policies vs health systems 6/40 (15.0%).
- Only 53/161 rows (32.9%) carry any explicit effective/approval date, and several of those
  are news or revision dates rather than true effective dates — most guidance pages are undated.
- Where dates exist they cluster: 2023 (7), 2024 (11), 2025 (13), 2026 to date (21) — i.e.,
  dated adoption roughly doubles each year, with 2026 already the largest cohort.

## 2. Commonest banned uses (themes across `banned_uses`)

Counts = rows whose banned_uses text matches the theme (rows can match several).

| Banned use | UME (n=121) | Health systems (n=40) | All (n=161) |
|---|---|---|---|
| Public/unapproved/unvetted AI tools (esp. with institutional data) | 26 | 7 | 33 |
| AI on exams/quizzes/assessments | 18 | 1 | 19 |
| PHI / patient identifiers into AI tools | 16 | 3 | 19 |
| Clinical documentation (H&P, notes) by AI outside approved systems | 10 | 1 | 11 |
| Submitting AI work as one's own / plagiarism | 8 | 0 | 8 |

- The single most common prohibition pattern is **tool-based** (public vs approved), not
  use-based: 33/161 rows ban entering data into public or unapproved tools.
- Assessment bans are almost exclusively a UME phenomenon (18 vs 1).
- Distinctive one-off bans worth noting: Baylor surgery clerkship bans AI on work assessing
  clinical reasoning; Mayo respiratory-care bans AI on any exam/quiz question; UNC bans
  AI meeting summaries without participants' consent; U Chicago IM residency bans PGY-1
  (intern) use of Abridge entirely; UT Austin invokes Texas state law against autonomous
  consequential decisions; NIH peer-review AI bans are repeated at Harvard, UAB, UChicago, U Iowa.

## 3. PHI clause language clusters

- Only 63/161 rows (39.1%) contain any PHI/patient-data rule; 98 say nothing the extractor
  could capture (recorded as blank or `none`).
- Of those 63, language clusters by verb modality:
  - "never" formulations ("never input", "never be put into", "never sharing"): 8
  - "must not"/"may not" formulations: 8
  - "only into approved tools" (permissive-with-guardrail, e.g. OHSU GME-48, CUIMC, U-Mich): 3
  - "not be entered/input" passive: 2
  - explicit "public AI tools" as the named danger: 6
  - de-identification/synthetic-data carve-outs (UCSF, Yale, Sinai): 3
- 25 of the 63 PHI clauses name HIPAA explicitly; a handful extend to FERPA (7 rows mention
  FERPA somewhere in the PHI/disclosure fields, e.g. Harvard, Tufts, Tulane, OHSU).
- Notable strict formulations: UCSF ("potentially a crime"), Stanford ("strictly forbidden"),
  Buffalo ("AI tools must never be used to input, analyze, or transmit identifiable patient
  information"), BU ("Patient information should never be put into any LLM or AI tool
  (including Terrier GPT) as they are not HIPAA compliant"), Penn ("even if deidentified …
  may not be exposed to open or public AI tools").
- Counter-pattern: 3 sources explicitly *permit* PHI inside institution-approved enterprise
  tools (UCSF ChatGPT Enterprise, U-Michigan U-M GPT/M365 Copilot, UTSW HIPAA-compliant
  ChatGPT), the "approved-tool carve-out" cluster.

## 4. AAMC alignment

- Only 1/161 rows cites AAMC AI principles: `utsouthwestern-libguides--ai-medical-healthcare-education.md`
  links both the *AAMC Principles for the Responsible Use of AI in and for Medical Education*
  and the *AAMC Principles for Responsible AI in Medical School and Residency Selection*.
- 2 further rows cite AAMC for non-AI purposes (Baylor surgery clerkship cites Core EPAs;
  Utah SoM handbook cites EPAs/MSOP/VSLO) — recorded as "no" for AI alignment.
- Despite an AAMC principles document existing in the corpus (national-frameworks), **school
  and system policies essentially never anchor to it (1/161, 0.6%)** — the clearest gap finding.

## 5. GME vs UME differences

- Only 6/161 rows apply to residents/fellows/GME trainees: OHSU GME-48, UChicago IM residency
  Abridge policy, NYU Grossman (students+residents), UCSF Bridges (students+GME+staff),
  UW GME announcement, Einstein (postdocs). GW SMHS explicitly *excludes* GME from its UME
  guidelines; GME is governed separately.
- Substance differs: GME/health-system documents govern **clinical documentation and ambient
  scribes** (Abridge at UChicago/UPMC/Yale/Weill Cornell; DAX at VUMC/UVA; ambient consent at
  Dartmouth Health) and **approval registries/governance committees** (OHSU registry, Duke
  ABCDS, Mount Sinai AIRB, UCLA HAIC, Michigan TSPs), while UME documents govern
  **assessments and academic integrity** (assessment bans 18 UME vs 1 HS).
- GME policies are more likely to be formal and numbered (OHSU "GME-48", UW "COMP.308",
  MSHS P&P) whereas UME relies more on handbook sections and guidance pages.

## 6. Dating / adoption timeline (from the 53 dated rows)

- Pre-GenAI ancestor: UMN Statement of Intellectual Responsibility (2015 revision; AI addendum undated).
- 2023 first wave (7): VUMC network block (Jun 2023), CWRU SoM assignment policy (Aug 3, 2023),
  Yale provost guidelines (Sep 20, 2023), UCSF PharmD AI policy (Oct 18, 2023), UNC GMB guidance
  (Jul 2023), Vanderbilt (effective Jan 2024), Geisel coursework policy (effective Jul 1, 2024,
  drafted late 2023).
- 2024 consolidation (11): Buffalo/PSOM precursor guidance, UW-Madison policies (Aug 2024),
  NYU Grossman (Aug 2024), Northwestern Feinberg policy approved Dec 4, 2024, UCSF Bridges
  (Dec 10, 2024), Dartmouth coursework (Jul 2024), Temple (Sep 2024), Pitt report (Mar 2024),
  Georgetown era, U Rochester.
- 2025 maturation (13): Icahn MSSM policy (Sep 2025), Geisel UME-CNTRL-0019 (effective Aug 1,
  2025), Keck/USC policy (Dec 17, 2025), BU MD program (Jul 10, 2025), VCU SoM (Jun 13, 2024
  version listed 2025 in file), UW GME application guidelines (Dec 2025), HopGPT launch (Dec 2025).
- 2026 explosion to date (21): OHSU GME-48 (Feb 12, 2026), Perelman UME policy (Jul 21, 2026),
  UNC OMSE (Jul 2026), Pitt SoM academic-integrity (Mar 24, 2026), ECU Brody SOP (Mar 1, 2026),
  Buffalo Jacobs (Mar 31, 2026), Utah system guidelines (Sep 2026), UW COMP.308 (Aug 25, 2026),
  MUSC framework rollout, Brown course-policy push (Aug 2026), GW SMHS guidelines — i.e., the
  field moved from "IT guidance" (2023) to "medical-school-specific formal policy" (2025–2026).

## 7. Other cross-cutting counts

- Disclosure/acknowledgement clause present: 77/161 (47.8%).
- Explicit enforcement/consequences stated: 60/161 (37.3%) — most guidance pages have none.
- Named secure/enterprise tools: 89/161 (55.3%). Most-named: ChatGPT/Edu variants (49),
  Microsoft Copilot (34), Claude (19), Gemini (15), Epic-embedded tools (7), Abridge (5),
  HopGPT (3), UCSF Versa (3), Harvard AI Sandbox (3), DAX (2), Stanford Secure GPT (1),
  BU Terrier GPT (1).
- Institutional-pattern: nearly every research university routes users to an
  enterprise/tenant instance (Copilot with university login is the most common single
  recommendation), while free-standing medical schools more often issue use-based rules
  without naming tools.

## 8. Caveats

- `doc_type` reflects the document's self-presentation (titled "Policy", numbered SOP, etc.).
- 25 files arrived from concurrent collection runs mid-extraction and were extracted from
  snippets at the end; thin pages (e.g., UF Health AI Governance, 404 chars) legitimately
  have mostly blank fields.
- phi_rule entries are verbatim or lightly ellipsised quotes from the source; bracketed
  ellipses mark cuts.
