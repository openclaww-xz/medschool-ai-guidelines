# Mount Sinai Health System — AI Implementation and Use Policy (MSHS 223) + Governance Structure

**Classification: pioneer — deployment tier (governance + tooling + monitoring)** (run-30 health systems Tier 1; `analysis/deep-reading/30-health-systems-synthesis.md`)

## Who drove it

**Policy owner: DTP (Digital and Technology Partners)** — IT-led rather than CMO-led, "though clinical review is delegated to the AI Review Board and consent determinations to PPHS (Program for the Protection of Human Subjects)" (`raw/health-systems/mount-sinai-health-system--ai-implementation-and-use-policy.md`; `analysis/deep-reading/mount-sinai-health-system--ai-implementation-and-use-policy.md`). The committee lattice (original issue 2025-01-01, effective 2025-02-01, across all 8 MSHS hospitals + Faculty Practices): an **AI Executive Committee** (oversees all; reports to the Strategy Group and Clinical Chairs), an **AI Risks, Ethics, and Policy Committee**, an **AI Review Board** (clinical/operational), and an **AI Teaching, Learning, and Discovery (TLD) Committee** for education/research tools with >200 ISMMS users (`raw/health-systems/mount-sinai--ai-governance-and-safety.md`). At the school level this connects to Icahn MSSM's standing AI Committee — school and system governance are one structure.

## Institutional context

Mount Sinai's DTP runs the operational machinery: a ServiceNow **AI Idea Intake Form** routed to committees, a DTP-maintained **approved-tool registry** ("noting the current approved scope of use"), and a **centralized AI portfolio** of "all clinical, operational, and financial AI models and features" for anti-duplication. The companion governance page describes pilot→checkpoint→scale sequencing. Enterprise AI platforms (ISMMS Gemini, ChatGPT Edu) and the Minerva research stack sit on top. Run 30's finding on locus applies: "IT-owned (MSHS/DTP, Hopkins) read as process or provisioning" — MSHS is the strongest version of the IT-owned genre.

## What they built and why it is pioneer-grade

1. **The strongest monitoring cadence in the corpus**: "any AI Tool used in patient care settings, in the billing and coding of services, or in the employment context must be reviewed **at least quarterly for the first 24 months**" of use, annual minimum thereafter; reviews "documented and reported to the Committee(s) that approved the use"; concerns trigger committee/Compliance action plans; and **decommissioning duties** ("must be done in an ethical, legal, and privacy-compliant manner"). Post-deployment surveillance with a clock, a report, and an end-of-life.
2. **Use-routed approval with use-by-use granularity**: clinical/operational → AI Review Board; research → PPHS/IRB; education → TLD Committee; employment → AI Executive Committee **with express written consent** plus General Counsel consultation; and the key clause: "The approval of an AI Tool for one intended use does not mean that it is approved for different uses." Material change forces re-review.
3. **Consent/notice determination as a process**: "PPHS will determine if the patient's consent is required and, if so, will modify existing consent form(s)... or create a new consent form" — with a notice fallback hierarchy (written / verbal documented in the record / signage and website).
4. **Risk taxonomy that names hallucination**: four enumerated risk classes — input, output ("biased or unrepresentative outputs; misleading, false, or **hallucinatory** outputs"), model, oversight — plus a duty to maintain "written benchmarks, evaluation metrics, validation tests."
5. **Enforcement with teeth**: committee **suspension authority mid-investigation** ("may, in its sole discretion, decide to suspend use of the AI Tool during any such investigation"); discipline "up to and including immediate termination"; an NLRA carve-out protecting employee communications; and an AI-disclosure duty on published AI content.

## What they explicitly chose NOT to do

- No blanket consent rule: consent is *determined* per tool by PPHS rather than fixed as policy — a deliberate delegation to the IRB apparatus.
- No enterprise liability assumption: the clinician must review and sign AI-assisted documentation "within the period required" — responsibility stays with the provider.
- No tool ban lists: the approved-scope registry does the gating.
- No CMO ownership — the system chose IT ownership with clinical committees rather than clinical ownership with IT support (a structural choice, with the genre consequences run 30 documents).

## Borrowed vs original

Original in the corpus: quarterly×24-month cadence, use-by-use approval, employment-AI written-consent gate, NLRA carve-out, publication-disclosure duty, decommissioning duty. The registry/committee pattern parallels Duke's ABCDS (convergent, not cited) and matches run 32's Singapore template of "AI registry with risk classification" and lifecycle governance — MSHS is the closest US institutional analog to AIHGle-style thinking (`analysis/deep-reading/32-international-synthesis.md`, §1B).

## Weaknesses / what's missing

- **IT ownership is a genre constraint**: run 30 — "No document in this run is CMO-office-authored"; clinical ownership of AI governance remains aspirational everywhere.
- Ambient-scribe consent is generic (PPHS-determined) rather than the per-encounter operational standard UChicago's residency policy achieves.
- Whether committees perform in practice is not provable from documents (run 30's caveat).
- No equity-impact screening trigger (contrast UW); no published performance metrics of the governance program itself.

## What to steal concretely

1. **The quarterly×24-month monitoring clause** verbatim — a review clock for every deployed tool, with documented reporting to the approving committee and a decommissioning duty.
2. **Use-by-use approval** — "approval for one intended use does not mean approval for different uses," with material-change re-review. This kills scope creep at the contract level.
3. **Employment-AI written-consent gate** — no AI in hiring/promotion/termination decisions without express executive-committee-level written consent, with labor-law review.
4. **Consent-determination-by-IRB** — assign the consent question to your human-subjects office with a notice fallback hierarchy, rather than writing a universal rule that will be wrong for half the tools.
5. **Committee suspension authority during investigations** — the mid-cycle off-switch most governance policies forget.
6. **Centralized AI portfolio for anti-duplication** — publish the list of what exists; duplicate shadow procurement is a governance failure mode in itself.
