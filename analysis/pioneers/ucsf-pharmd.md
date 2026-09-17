# UCSF School of Pharmacy — Policy on Use of AI in Assessments and Deliverables

**Classification: pioneer** (run-27 batch A rank #2; `analysis/deep-reading/27-schoolsA-synthesis.md`)

## Who drove it

A formal school-level policy "approved by CEPC October 18, 2023" — the (Pharmacy) Committee on Educational Policy — making it committee-enacted governance with a date, not a guidance page (`raw/us-med-schools/ucsf-som--pharmd-ai-assessments-policy.md`; `analysis/deep-reading/ucsf-som--pharmd-ai-assessments-policy.md`). What makes the authorship notable is the date: October 2023 places this at the very front of the assessment-redesign wave — most schools were still writing prohibition memos. That earliness signals a curriculum committee that treated ChatGPT as a psychometric problem, not a conduct problem.

## Institutional context

UCSF had existing data-protection machinery the policy could lean on: it cross-references "UCSF Data Protection and Large Language Models (requires MyAccess login)" for tool authorization, and grounds its legal threat in campus policy — "entry of patient or student information (identified or de-identified) into such systems is a violation of UCSF policies and potentially a crime." The school also had scholarly-infrastructure habits: the policy is externally cited (Sentient Syllabus Project; UNESCO ChatGPT quick-start guide; Monash University AI policy) — evidence of a drafting process that scanned the world literature rather than starting from a blank page. Separately, UCSF's MD-side Bridges curriculum policy names an "Associate Dean for Assessment, Improvement, and Accreditation and Director of AI" as accountable officer (CCEP-approved 12/10/2024; `raw/us-med-schools/ucsf-som--bridges-curriculum-genai-usage-policy.md`) — a named Director of AI is part of the institutional context any UCSF-level policy sits inside.

## What they built and why it is pioneer-grade

The **four-level classification taxonomy** applied to every assessment and deliverable:

- **AI-1 Disallowed** (default: "If an assessment or deliverable does not have a classification provided, it is assumed to be classified AI-1")
- **AI-2 Restricted** (tool- or aspect-limited with documentation)
- **AI-3 Documented** (any use allowed with documentation)
- **AI-4 Unregulated** (no documentation required — explicitly absorbing embedded grammar/spellcheck: "AI products are increasingly integrated into standard software packages... Current versions of such products do not require citation")

Instructors may classify "blanket... for a learning experience or provide separate classification for individual assessments." This is the corpus's benchmark assessment redesign because it changes the *assessment contract itself*: every assignment now carries an AI label the way it carries a point value. Three supporting instruments make it real: (1) **submission-as-attestation** clauses ("By submitting an assessment or deliverable for evaluation: Students assert that they have respected all specific requirements..."); (2) a **citation appendix** with a verbatim summary-statement template ("I acknowledge the use of [insert AI system(s) and link] to [specific use]... The prompts used include [list of prompts]...") plus a fully worked example (ChatGPT/Monash, dated 4 January 2023); (3) a **hard legal boundary** — the policy "is designed to apply to assessments and deliverables used in the pedagogical process, not as part of direct patient care or human subjects research," with patient-care/research AI requiring "direct, positive confirmation from a preceptor or research director."

The pedagogical rationale is articulated, not assumed: "Learning is not simply memorization of facts—it is building flexible knowledge structures... to evaluate the value of an AI's proposed solution, it is necessary to have adequate proficiency in that domain" (raw policy).

## What they explicitly chose NOT to do

- No AI detection: integrity is enforced through classification + attestation, not surveillance.
- No tool-by-tool rules — the taxonomy classifies *assignments*, not tools, so it survives vendor churn.
- No attempt to ban AI-4 ambient functionality — embedded spelling/grammar AI is explicitly exempted, anticipating the word-processor problem by years.
- No secure deployment of its own named in this policy (tooling deferred to UCSF-wide guidance) — a deliberate scope choice that keeps the policy purely about assessment architecture.

## Borrowed vs original

The taxonomy is original in the US medical-education corpus; the disclosure template traces to Monash University, and the general framing to UNESCO's quick-start guide and the Sentient Syllabus Project — an international, not national, borrowing lineage (`analysis/deep-reading/ucsf-som--pharmd-ai-assessments-policy.md`, References). Per the national synthesis, no US national body had anything comparable in 2023 — NBME was writing construct-defense posts, not classification systems (`analysis/deep-reading/26-national-synthesis.md`, §1 Tier 2). Downstream, per run 29, LSUHSC-NO cites UCSF in its own policy's lineage — UCSF PharmD is now a *source* for other schools (`analysis/deep-reading/29-cohortC-synthesis.md`, pattern 2).

## Weaknesses / what's missing

- No named secure platform inside the policy itself — "the only gap vs #1" (UVA) per the batch-A synthesis.
- Default-to-AI-1 (disallowed) puts the burden of permission on faculty; a silent instructor produces prohibition, which can quietly revert the school to default-deny.
- PharmD scope: the pattern demonstrably transfers (it is the most-copied assessment design in the corpus), but UCSF's own MD program runs a separate instrument.
- No equity provisions and no faculty-development obligations attached to the classification duty.

## What to steal concretely

1. The **AI-1..AI-4 taxonomy verbatim**, including the AI-4 embedded-AI exemption — the single most transferable assessment artifact in the corpus (run 28's model verdict: tiering "dominates on every evaluation axis"; `analysis/deep-reading/28-cohortB-synthesis.md`).
2. The **default-classification rule** (unclassified = AI-1) — an explicit failure-safe that most tier systems lack.
3. **Submission-as-attestation clauses** — converting every submission into a signed claim, which is cheaper and fairer than detection.
4. The **summary-statement template with prompt listing** and its worked example.
5. The **explicit scope carve-out** ("pedagogical process, not patient care or research") that prevents a coursework policy from being misread as clinical authorization.
