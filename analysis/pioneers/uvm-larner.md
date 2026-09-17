# UVM Larner College of Medicine — Policy 645.00, Use of AI in Medical Education

**Classification: pioneer** (run-29 cohort C; `analysis/deep-reading/29-cohortC-synthesis.md`)

## Who drove it

Handbook Policy 645.00, "adopted/affirmed 7/15/2025 by the **Medical Curriculum Committee**," with policy oversight assigned to the **Associate Dean for Students** (`raw/us-med-schools/uvm-larner--policy-645-use-of-ai-in-medical-education.md`; `analysis/deep-reading/uvm-larner--policy-645-use-of-ai-in-medical-education.md`). Technical authority is delegated to **COMTS** (COM Technology Services) and UVM ETS for system approval: "Unless the AI system is a pre-approved, UVM instance, the determination on whether a system is closed must be made by COMTS. Prior authorization is required before using AI." A small school running standard curriculum-governance machinery — the policy passed through the same committee that owns every other student policy.

## Institutional context

Vermont's statutory environment is embedded directly: "Inputting NPPD into an open system is considered a breach of data security laws, such as HIPAA and the Vermont Data Breach Notification law, both of which require notification to government oversight agencies and to the individual" — the state breach statute gives the taxonomy legal teeth. UVM's campus IT (ETS) provides the approval pathway. Run 29's pattern: "Vermont state breach law embedded in UVM's taxonomy" — state schools carry compliance plumbing privates skip (`analysis/deep-reading/29-cohortC-synthesis.md`, pattern 3).

## What they built and why it is pioneer-grade

1. **The cleanest data-flow classification in the corpus**: four defined system classes — **Open System** ("input data is accessible outside of UVM and provides no meaningful privacy protections"), **Closed System** ("input data is not used in training or made accessible to any non-authorized user or agent"), **Closed Compliant System** (adds FERPA/HIPAA compliance), and **UVM Instance** (reviewed/approved/sanctioned by COMTS or ETS). Every permission rule then keys off the class ("If FERPA or HIPAA data will be input, only use Closed Compliant System") — the same contract-and-dataflow logic as UVA's safe harbor, but as formal definitions with an approval authority behind them.
2. **An AI-literacy curriculum embedded in the policy**: users should be able to explain "in their own words": Model; model types (deep learning, generative AI, LLMs); **Agent/Instance**; Dataset; Training; Input/output; supervised/unsupervised learning; **"Model evaluation metrics (accuracy, benchmarks, AUC, etc.)"**; Hallucination. No other policy in the corpus defines evaluation metrics — this is a measurable literacy standard, effectively an examinable syllabus.
3. **Evidence-based-learning as a selection criterion**: AI tools "should facilitate or utilize evidence-based learning methods," naming retrieval practice, interleaving, spaced practice, elaborative interrogation, concrete examples — tying AI tool legitimacy to learning science.
4. **Faculty dual disclosure**: faculty must disclose AI in materials development AND "if AI products are used for analysis of student performance (e.g. OSCE or note review and feedback)" — with responsibility for accuracy retained. Learner-data protection follows: performance evaluations, assessments, narrative assignments, demographics "may only be entered into secure COMTS approved closed systems."
5. **Human-override machinery**: "Human reviewers must have the authority to override AI-generated outcomes if necessary."

## What they explicitly chose NOT to do

- No tool names at all — the policy governs system classes, so it never needs updating when vendors change.
- No detection regime; the burden is placed on the user ("Users are solely responsible for verifying whether the version of the AI system is open or closed").
- No blanket permissive or prohibitive default for coursework: students author their own work on graded items "unless explicitly permitted by faculty," but self-study/self-assessment AI use is affirmatively permitted, and universal disclosure is required "including reflections and case reports."
- Clinical documentation is EHR-bounded ("AI-generated clinical documentation outside of supported EHR systems is prohibited") with hosting-facility deference — no attempt to regulate clinical sites from Burlington.

## Borrowed vs original

Almost nothing here is borrowed boilerplate — run 29 classes it as "original conceptual architecture." The open/closed taxonomy, the literacy syllabus, and the learning-science test have no visible national-framework source (the AMA/AAMC documents contain nothing comparable; `analysis/deep-reading/26-national-synthesis.md`). The deep-read note flags only editorial roughness ("HIPPAA/HIPPA" typos) as evidence of lighter copyediting — a small-school trade-off.

## Weaknesses / what's missing

- No assessment-redesign instrument (no tiers, no attestation architecture) — disclosure is universal but the disclosure *format* is unspecified.
- No worked examples or scenarios — conceptually complete but not yet a teaching document (contrast UVA/JABSOM).
- No equity-of-access provisions; no faculty-development program.
- Editorial quality (repeated HIPAA misspellings) signals limited administrative bandwidth — a sustainability risk for a policy requiring COMTS determinations per tool.
- "Related LCME standards: Not Applicable" — no accreditation linkage claimed.

## What to steal concretely

1. The **Open / Closed / Closed-Compliant / Approved-Instance taxonomy** with a named approval authority (your IT unit) — the most durable scope architecture available; it survives every model release because it classifies data flow, not products.
2. The **state-breach-law enforcement hook** — cite your own state's notification statute in the violation clause; it converts an internal rule into a legal duty students already have.
3. The **AI-literacy concept list as an assessable standard** ("in their own words," including AUC and hallucination) — the cheapest real AI curriculum any school can adopt; it fits on one page and can be tested.
4. **Faculty disclosure of AI-analyzed student performance** (OSCE/note review) — the learner-data protection most schools haven't noticed they need.
5. The **learning-science selection criterion** — a one-line justification rule for adopting any AI study tool: does it implement retrieval/spacing/interleaving, yes or no.
6. **Override-authority requirement** — any AI-influenced decision must have a named human who can overturn it.
