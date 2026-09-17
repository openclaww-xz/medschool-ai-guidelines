# Stanford School of Medicine — MD Handbook 3.32 Generative AI Policy

**Classification: pioneer** (run-27 batch A rank #4; `analysis/deep-reading/27-schoolsA-synthesis.md`)

## Who drove it

Handbook-level policy authority: the policy lives inside the Stanford SoM MD Handbook (section 3.32, "MD Requirements & Procedures") — "formally part of the MD/MSPA program's governing handbook... not a standalone dean's memo" (`raw/us-med-schools/stanford-md--genai-policy-3-32.md`; `analysis/deep-reading/stanford-md--genai-policy-3-32.md`). No individual author is named; it defers to Stanford's university-wide "Generative AI Policy Guidance." Updated August 2025; covers both MD and MSPA programs. The driver, structurally, is the program's own requirements machinery — AI conduct is governed where academic conduct is governed.

## Institutional context

Two institution-built secure deployments anchor the policy: **Stanford Healthcare Secure GPT** (securegpt.stanfordhealthcare.org) and the **Stanford AI Playground** (aiplayground.stanford.edu), plus Stanford's university IT **Security Risk Classifications** framework the policy links directly. This is the same pattern as UVA (enterprise provisioning enabling school policy) but with *internally built* tools rather than licensed ones — Stanford builds its own compliant LLM surfaces and can therefore tell students exactly where sensitive data may go.

## What they built and why it is pioneer-grade

1. **Enforcement realism unique in the corpus**: "While we recognize that restricting the use of AI tools cannot be strictly enforced, we expect students to optimize their learning progress" — paired with relocating the integrity burden to competency demonstration: students "will be held accountable for demonstrating competency in clinical skills and reasoning without the aid of AI tools." This is the same enforcement-physics insight the University of Sydney built an entire assessment system on (`analysis/deep-reading/32-international-synthesis.md`, §1D) — Stanford states it as policy honesty, Sydney operationalizes it structurally.
2. **The strictest citation spec in the corpus**: disclosure must include "the tool name, model/version, date, query, and output excerpt" — with a worked example: "ChatGPT (GPT-4; June 10, 2025), prompt: 'Explain ARDS pathophysiology,' output used in Section 2." Requiring the *query text* and *output location* makes verification auditable.
3. **Teaching-grade de-identification guidance**: an anonymized-input worked example ("Middle-aged woman with asthma exacerbation and aspirin allergy...") set against the progress-note counterexample ("directly copying in a patient progress note into any such public system would be a clear privacy violation"). Notably, it names clinical-AI tools (OpenEvidence, Doximity) as *also* PHI-prohibited — closing a loophole other policies leave open.
4. **A calibrated default**: AI use is "discouraged" (not prohibited) for evaluated activities, with hard prohibition reserved for closed-book contexts; learning/clarification and grammar editing are affirmatively permitted.

## What they explicitly chose NOT to do

- No prohibition-by-default for learning uses.
- No detection regime — instead the competency-demonstration shift.
- No blanket clinical-documentation ban: documentation must "adhere to the policies and guidelines for the clinical site," refraining only "unless supported by the Electronic Health Record... or permitted by the clerkship" — site deference rather than school absolutism.
- No tier taxonomy or mandatory syllabus statements (each course publishes its own boundaries).

## Borrowed vs original

The citation spec, the non-enforceability concession, and the competency-burden shift are original in the US corpus. The general permitted-use framing parallels AMA's permissive education vocabulary (`analysis/deep-reading/26-national-synthesis.md`, §1), and the university-wide guidance layer is the borrowed substrate. The deep-read note flags "indirectly Stanford via university guidance" in the batch's AI-drafting self-disclosure pattern.

## Weaknesses / what's missing

- **No external citations at all** — "relies on internal policies" (deep-read note); the policy asserts but never grounds its positions in the literature. For an institution with Stanford HAI down the road, the absence of any scholarly anchor is a choice, not an oversight.
- No assessment-redesign program: the competency framing gestures at it, but there is no secure-assessment architecture (contrast Sydney's two lanes or UCSF's taxonomy).
- No equity-of-access provisions; no faculty-side obligations — faculty appear only as rule-setters, never as governed AI users (contrast ECU/GW/UAMS).
- No formal governance/maintenance body named beyond handbook review; the "reviewed and revised as necessary" clause names no owner or cadence.
- MSPA inclusion is good, but GME, PhD, and research contexts are unaddressed in this instrument.

## What to steal concretely

1. **The non-enforceability clause + competency-burden shift** — one honest sentence ("restricting the use of AI tools cannot be strictly enforced") plus one structural response (accountability for demonstrating competency without AI). Cheapest high-value pair in the corpus.
2. **The five-element citation spec** (tool, model/version, date, query, output excerpt) with the ARDS worked example — make it the school-wide standard.
3. The **anonymized-example vs progress-note-counterexample pair** — privacy taught in two sentences.
4. **Naming clinical-AI tools as PHI-prohibited** — close the OpenEvidence/Doximity loophole explicitly.
5. Naming **internally built secure deployments with URLs** in the policy itself, so the compliant path is one click away.
