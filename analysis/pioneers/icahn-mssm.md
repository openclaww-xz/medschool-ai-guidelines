# Icahn School of Medicine at Mount Sinai — Using AI in Teaching, Learning, and Discovery

**Classification: pioneer** (run-27 batch A rank #3; `analysis/deep-reading/27-schoolsA-synthesis.md`)

## Who drove it

Approved September 2025, the policy was "developed in collaboration with leadership from the Graduate School, Medical Education, and Scholarly & Research Technologies" and reviewed/approved by three governance bodies: the Graduate School of Biomedical Sciences' Curriculum Committee, the Academic Affairs Steering Committee, and the Executive Education Committee of the MD Program (`raw/us-med-schools/icahn-mssm--student-ai-policy.md`; `analysis/deep-reading/icahn-mssm--student-ai-policy.md`). Critically, it is *maintained* by a standing "AI Committee on Teaching, Learning, and Discovery" with annual review — a dedicated governance body that outlives the drafting moment. At the health-system level, the same institution runs an "AI Teaching, Learning, Discovery, and Research Committee" that reviews education/research AI tools with >200 anticipated ISMMS users (MSHS Policy 223; `raw/health-systems/mount-sinai-health-system--ai-implementation-and-use-policy.md`) — school and system governance are vertically linked.

## Institutional context

Mount Sinai's research-computing stack is the enabling infrastructure no peer matches: the **Minerva supercomputing cluster**, the **Mount Sinai Data Warehouse** (MSDW — "complete sets of data extracted from the Mount Sinai Epic electronic health record"), and dual enterprise AI platforms (**ISMMS Gemini** and an institution-wide **ChatGPT Edu** instance). FAVES principles (Fairness, Appropriateness, Validity, Effectiveness, Safety) and IRB integration give the research side normative plumbing. This is a school that already had HIPAA-compliant compute before it had an AI policy.

## What they built and why it is pioneer-grade

The **widest governance scope in the corpus** — one instrument spanning education, research, and discovery — with four signature constructs:

1. **Mandatory syllabus AI-level statements**: "all course syllabi must include a statement outlining the level of AI use permitted for assignments and assessments," backed by Graduate School template language for "full use," "limited use," and "no use," plus a **six-category permitted-use menu** (Research / Structure / Proofreading / Content Generation / Programming / None) — credibly attributed: "inspired by University of Wales AI Guidelines."
2. **Data epistemics beyond anyone else's**: licensed platforms are *not* declared safe — even the ISMMS ChatGPT Edu instance requires "examining terms and conditions, consent under which the data was collected, risk assessment, de-identification or other mitigation strategies." And: vendor training-restriction "settings... change regularly and cannot be relied upon." This is the only school policy that understands enterprise licensing as a risk surface rather than a solution.
3. **Research-infrastructure depth**: IRB protocols must "clearly detail how artificial intelligence methods (such unsupervised, supervised, and reinforcement learning methods) are being used," Minerva/MSDW use is governed with explicit re-identification warning ("very detailed information that could re-identify vulnerable patients"), and a purpose-built **Mentor–Learner Agreement Regarding Use of Generative AI** documents advisor approval.
4. **An evidence-informed anti-detection stance with a licensed alternative**: "Do not enter student assignments into public AI detection tools. If assessing potential plagiarism or AI use would be helpful, Educational Technology at ISMMS can provide a license or assistance with using iThenticate."

## What they explicitly chose NOT to do

- No blanket prohibition: the default is *consultative* — "seek instructor, module or clerkship director, or supervisor guidance before beginning AI use... where it is not explicitly permitted" — less permissive than UVA/Stanford, but explicitly not a ban.
- No reliance on vendor controls — the policy explicitly refuses to trust training-opt-out settings.
- No detection-based enforcement (see above).
- It does not attempt to enumerate tools exhaustively: "As this policy cannot detail every example, it is critical that students learn how to engage with data or content owners."

## Borrowed vs original

Borrowed: the six-category use menu (University of Wales, credited); FAVES principles (NIH/NIST lineage). Original: the licensed≠safe doctrine, the settings-drift warning, IRB-protocol AI-method disclosure, the Mentor–Learner Agreement instrument, and MSDW re-identification governance. Per the national synthesis, the AMA companion document supplies the general education/research scope split (`analysis/deep-reading/26-national-synthesis.md`, §1), but no national body supplies research-infrastructure clauses at this depth — Sinai wrote those itself.

## Weaknesses / what's missing

- The consultative pre-approval default imposes a transaction cost on every non-explicitly-permitted use — "less permissive than UVA/Stanford defaults" (batch A synthesis) — and could chill legitimate low-stakes use.
- No formal tier numbering (the syllabus statements are full/limited/no rather than a scalable taxonomy like UCSF's AI-1..4 or ECU's Levels).
- No equity-of-access provisions; no assessment redesign beyond the syllabus-statement mandate.
- The policy is silent on how the standing AI Committee's decisions are recorded/appealed.

## What to steal concretely

1. **"Licensed ≠ safe" clause set** — the requirement to examine terms, consent provenance, and de-identification *even for institutionally licensed platforms*, plus the "settings change regularly and cannot be relied upon" warning. Every school with an enterprise ChatGPT/Gemini instance needs exactly this paragraph.
2. **Mandatory syllabus AI statements with template language** — the cheapest possible consistency mechanism (no new bureaucracy; the syllabus already exists).
3. The **Mentor–Learner Agreement** as a documentation instrument for research AI use.
4. **IRB-protocol disclosure of AI methods** (unsupervised/supervised/reinforcement) — a one-line requirement that makes research AI visible to existing review.
5. The **anti-detection + iThenticate-alternative** pairing — take the stance *and* fund the alternative, or the stance just frustrates faculty.
