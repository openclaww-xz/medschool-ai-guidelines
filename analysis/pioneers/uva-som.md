# UVA School of Medicine — MD Program Policy on Generative AI

**Classification: pioneer** (run-27 batch A rank #1; `analysis/deep-reading/27-schoolsA-synthesis.md`)

## Who drove it

The policy was "Developed by the UVA SOM Generative AI Advisory Team and reviewed and approved by the Medical Education Management Committee," and is dated/updated July 2026 (`raw/us-med-schools/uva-som--md-program-genai-policy.md`; `analysis/deep-reading/uva-som--md-program-genai-policy.md`). Two governance facts matter: (1) authorship sits with a *dedicated advisory team* plus the standing curriculum governance body (MEMC), not an ad-hoc dean's memo; (2) the policy is explicitly subordinate to university-wide guidance — "Where the two policies overlap, the University-wide guidance takes precedence" — meaning the SOM built on top of an existing UVA enterprise layer (in.virginia.edu/genai-useguidelines) rather than inventing one.

## Institutional context that made it possible

UVA Health's deployed tooling is the precondition. The policy's provisioned tier names Microsoft CoPilot, Google AI (including Gemini Notebook), Dax CoPilot (an ambient documentation product), "and a small-scale pilot of Claude" as of July 2026 — a live, dated inventory that only exists because UVA Health signed institutional data agreements. The clinical arm (UVA Health) supplies the "safe harbor" the school policy then teaches students to use. The medical-school-specific policy is the curricular skin on an enterprise procurement capability.

## What they built and why it is pioneer-grade

Three interlocking instruments:

1. **A two-tier tool taxonomy with a contractual "safe harbor" concept.** Tier 1 = "Tools that are provisioned by UVA or UVA Health. With institutional data agreements these tools offer 'safe harbor' for content." Tier 2 = "Content-Restricted External Tools" without data agreements. This is the corpus's cleanest data-flow classification: the dividing line is *who has a contract*, not *what the tool is called* — which is the only distinction that actually determines privacy and IP exposure.
2. **The corpus's most sophisticated de-identification clause**: "Simply removing a name is not sufficient... Reliable de-identification is harder than it looks—metadata, rare diagnoses, and identifiable features can still identify a patient" — and the PHI ban extends beyond documentation to "clinical reasoning, question-asking, and image interpretation" (raw policy; deep-read note).
3. **Six worked acceptable-use scenarios** (Copilot on Panopto transcripts; immunology slides into Gemini Notebook; ChatGPT on a fictional FCM case; a generically-phrased clinical question on rounds via OpenEvidence; public/self-authored content; learning objectives into Mapify) — each applying the taxonomy to a real student behavior. No other policy in the corpus teaches by scenario this concretely (`analysis/deep-reading/27-schoolsA-synthesis.md`, §1).

It is pioneer-grade because it fuses pedagogy and operations: the AI-assisted vs AI-generated distinction ("faculty should indicate, for a given assignment, whether and at what level of involvement disclosure is required") calibrates disclosure burden to contribution level, and the UWorld/Anki IP clause ("Licensed third-party content (e.g., UWorld questions or Anki decks built from copyrighted textbooks) may not be entered into any generative AI tool") regulates the study-tool ecosystem students actually inhabit.

## What they explicitly chose NOT to do

- No formal assessment-classification scheme (no AI-1..AI-4 tiers à la UCSF PharmD) — disclosure thresholds are faculty-set per assignment, not systematized.
- No ban-by-default: the opening posture is supportive ("UVA SOM supports medical students to use generative AI... to augment learning").
- No AI-detection regime — enforcement routes to existing Honor Code/Code of Conduct processes.
- Clinical documentation is not blanket-banned: AI documentation is permitted *inside* EHR-supported tools ("e.g., Dax or Abridge") — a deliberate channeling choice, not prohibition.

## Borrowed vs original

The national synthesis (`analysis/deep-reading/26-national-synthesis.md`) shows vocabulary flowing from AMA/AAMC outward; UVA's constructs (safe-harbor tiering, scenario-based drafting, AI-assisted/generated threshold calibration, the UWorld/Anki clause) do not appear in any national framework — they are original operational inventions. What UVA borrows is the AMA's permissive-learning posture and standard citation practice (MLA Style Center link).

## Weaknesses / what's missing

- No assessment taxonomy — the biggest structural gap vs UCSF PharmD or ECU (`analysis/deep-reading/27-schoolsA-synthesis.md`, §1).
- University-guidance precedence creates a two-master problem the policy doesn't resolve.
- No equity-of-access provisions (contrast ECU's free-tool floor) and no faculty-side rules (contrast ECU/GW faculty parity).
- No named secure-LLM playground of its own beyond enterprise CoPilot/Gemini.

## What to steal concretely

1. The two-tier **contract-based tool taxonomy** ("safe harbor" vs "Content-Restricted External Tools") — copy the definitions verbatim; it resolves the grammar-tool incoherence that bedevils tool-list policies (`analysis/deep-reading/28-cohortB-synthesis.md`, cross-cohort observations).
2. The **six worked scenarios** as an appendix — they convert any policy from rules into curriculum.
3. The **metadata/rare-diagnosis de-identification paragraph** — the best student-facing privacy sentence in the corpus.
4. The **dated tool inventory with named pilots** (including the Claude pilot) — transparency about what is actually provisioned, updated with the policy.
5. The **AI-assisted vs AI-generated disclosure threshold** — a faculty-settable dial between UCSF's AI-2/AI-3 tiers without requiring a full taxonomy.
