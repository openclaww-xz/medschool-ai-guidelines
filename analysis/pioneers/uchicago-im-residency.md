# UChicago Medicine — Internal Medicine Residency Clinical AI Use Policy (Abridge)

**Classification: pioneer — ambient-scribe operational-governance tier** (run-30 health systems Tier 1; `analysis/deep-reading/30-health-systems-synthesis.md`)

## Who drove it

The **IM residency program itself** — chief residents/program leadership, not the health system: "program-level policy... Department-of-medicine governance over trainees; attending supervision rules anchor it clinically. Annual reassessment each June by the program" (`raw/health-systems/uchicago-medicine--im-residency-clinical-ai-use-policy.md`; `analysis/deep-reading/uchicago-medicine--im-residency-clinical-ai-use-policy.md`). The authorship locus is the finding: governance can live at the training-program layer, where the actual clinical risk (a resident with a microphone and an attending with attestation duty) is located. No enterprise committee needed to write the deepest ambient-scribe controls in the corpus.

## Institutional context

A deployed tool (Abridge ambient scribe) live in approved clinical settings (continuity clinic, urgent care, inpatient rotations, ED), institutional privacy/HIPAA policy and MDM/encryption infrastructure behind it, and a residency-program culture with annual policy-review machinery already in place. University of Chicago Medicine's approved-AI intranet list (Phoenix AI, UpToDate named) supplies the enterprise tool floor the program policy builds on.

## What they built and why it is pioneer-grade

Run 30: "the deepest ambient-scribe governance anywhere in the corpus" — clause by clause:

1. **Per-encounter verbal consent from the patient AND all third parties present** ("For visits involving family members or other third parties in the room, verbal consent must be obtained from all participants"), documented via a standard **`.ABRIDGEVERBALCONSENT` smartphrase**; **declination also charted**; "Patients may decline without impact on their care." Consent operationalized to the EHR-artifact level — run 30's consent spectrum ranks it alone at the top, ahead of Ochsner (verbal each use), UC Davis (opt-out), and Cleveland Clinic (none mentioned).
2. **The anti-passive-recording rule**: "The resident must be physically present in the room during the entire recording duration to prevent 'passive' recording of private family conversations" — a workflow designed around an actual failure mode.
3. **Training gate + tiered eligibility**: mandatory pre-access orientation "covering consent workflows, documentation review expectations, and **common AI error patterns**," completion tracked by the program coordinator; **PGY-2/3 only; PGY-1 interns excluded** — supervision-caliber judgment as an eligibility criterion.
4. **Liability equivalence and a two-tier chain**: "AI-assisted notes are subject to the same expectations for review, attestation, and accuracy as traditional documentation"; residents "fully responsible for reviewing... prior to forwarding to attending faculty for attestation"; attendings "retain standard supervisory responsibility." AI confers no shield and creates no new duty class — run 30 notes this is the only two-tier liability chain in the corpus.
5. **Scope and device discipline**: use only in direct patient encounters in approved settings (not rounds, handoffs, conferences, or evaluations); hospital-issued or MDM/encryption-compliant personal devices only; recordings and AI content banned from teaching/research/external use without institutional approval; named competitor ban ("Other Ambient Listening Scribe technology (i.e. Doximity Scribe) are not allowed") and a PHI hard line against non-approved models.
6. **Revocable annual approval**: "revisited and reassessed annually in June. Continued approval may be modified or revoked based on program evaluation, compliance, or institutional guidance."

## What they explicitly chose NOT to do

- No enterprise pretensions: one program, one vendor, one clinical workflow — depth over breadth.
- No opt-out consent model: per-encounter opt-in with charted consent AND charted declination — the most demanding standard, chosen deliberately.
- No intern access — they accepted the equity/efficiency cost of excluding PGY-1s in exchange for supervision-caliber judgment.
- No secondary use of recordings — teaching and research reuse explicitly walled off without approval.

## Borrowed vs original

Everything operational here is original in the corpus (the smartphrase mechanism, the third-party consent rule, physical-presence requirement, PGY gating). Conceptually it instantiates the same supervision-first logic as Buffalo's NEJM-derived framework and OHSU GME-48's scribe-consent clause — convergent state-of-the-art across programs rather than cited borrowing. Run 32's Singapore parallel: the DTC duty ("patients are clearly informed that they are interacting with AI") and deskilling-contingency thinking — UChicago implements the patient-communication doctrine at workflow level (`analysis/deep-reading/32-international-synthesis.md`, §1B).

## Weaknesses / what's missing

- **Vendor-specific by design**: Abridge is named throughout; the policy must be rewritten if the vendor changes (contrast system-level registry approaches).
- No model-performance monitoring: "annual program reassessment + compliance-based revocation; no performance monitoring of the model itself" (run 30).
- Single-program scope: other UChicago residencies and the health system are governed elsewhere; nothing guarantees propagation.
- No equity analysis of PGY-1 exclusion (documentation-burden disparity between intern and senior classes).

## What to steal concretely

1. **The consent package**: per-encounter verbal consent, all third parties present, EHR smartphrase documentation, charted declination, no-care-impact assurance. Five clauses, adoptable verbatim by any program tomorrow.
2. **The physical-presence anti-passive-recording rule** — the clause nobody thinks of until the first family-conversation incident.
3. **PGY-tiered eligibility + mandatory error-pattern orientation** — access as a supervised privilege earned by training year and orientation completion.
4. **Liability-equivalence sentence** ("same expectations for review, attestation, and accuracy as traditional documentation") — prevents AI notes from becoming a shadow documentation class.
5. **Revocable annual approval** of the whole program-vendor arrangement — sunset built into the permission, not just the policy document.
6. **The program-layer lesson**: if your health system is slow, a residency program can publish gold-standard operational governance for its own trainees this quarter. Duke and Sinai built institutions; UChicago proves the program layer is enough.
