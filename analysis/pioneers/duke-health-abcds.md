# Duke Health — Algorithm-Based Clinical Decision Support (ABCDS) Oversight

**Classification: pioneer — deployment tier (governance + tooling + monitoring)** (run-30 health systems Tier 1; `analysis/deep-reading/30-health-systems-synthesis.md`)

## Who drove it

The **Duke Health AI Evaluation & Governance Program** — a dedicated, named program with its own domain (healthaigovernance.duke.edu), an AI Oversight Policy, a Standard Operating Procedure, an **Implementation Subcommittee**, **independent Review Committees**, office hours, and a registry (`raw/health-systems/duke-health--abcds-oversight-process.md`; `analysis/deep-reading/duke-health--abcds-oversight-process.md`). This is not a compliance-office policy: it is a standing evaluation institution with named bodies and intake infrastructure (a registration form, an email address, bookable office hours). Duke's documented scholarly work on algorithmic clinical decision support safety is the program's intellectual foundation.

## Institutional context

Duke's academic informatics and clinical-analytics depth supplies the reviewers: an "independent Review Committee" model only works where there are qualified faculty independent of the project team to staff them. The program's maturity also reflects timing — Duke built algorithm oversight (predictive CDS, sepsis models, imaging tools) before the generative-AI wave, so when LLM tools arrived there was already a registry, a risk-tiering scheme, and review committees to receive them. The page also shows regulatory fluency: the FDA Digital Health Policy Navigator and SaMD guidance are built into the submission path.

## What they built and why it is pioneer-grade

Run 30's three-leg test — governance, tooling, monitoring — and Duke is "the cleanest pioneer on process":

1. **A mandatory registry of ALL patient-care algorithms**: "ABCDS Oversight manages a registry of all algorithmic solutions under consideration for use in patient care at Duke Health." Nothing deploys outside the registry — the shadow-AI problem is solved by definition of scope, not by exhortation.
2. **Risk-tiered pathways**: the Implementation Subcommittee reviews each registration, completes a risk assessment, and routes to **Full review (high risk) / Fast-track (moderate) / Registration only (low risk)** — with low-risk tools delegating validation to **named "Clinical and Model Owners."** Accountability for low-risk tools is named-role-based, not committee-based — governance proportional to risk.
3. **Independent, stage-gated review through the lifecycle**: "an independent Review Committee is assigned to perform evaluations at checkpoints throughout the lifecycle — from procurement or development to general deployment, **monitoring, and maintenance**." Monitoring is inside the review mandate by design — post-deployment surveillance is not a separate program that may or may not exist.
4. **Four-way decision outcomes**: "Approval; Approval with contingencies; Re-Review; Decline" — conditional approval and mandatory re-review are built into the decision vocabulary, and non-approval requires "details of and a timeline to resolve gaps."
5. **Published instrument set**: submission templates and checklists per checkpoint for both pathways, a **Bias Management Framework** ("to understand how biases may be introduced into algorithmic solutions and/or associated workflows"), and FDA SaMD navigation guidance.

## What they explicitly chose NOT to do

- No tool-by-tool policy page — the process governs *any* algorithm by risk, whether predictive or generative, homegrown or vendor.
- No committee rubber-stamping of low-risk tools: registration-only exists precisely so oversight doesn't drown in trivia.
- No PR-forward deployment narrative: the artifact is a process description, not a capabilities brochure (contrast run 30's Tier-3 systems).
- Consent/notice and ambient-scribe rules are *not* on this page — deliberately out of scope for algorithm oversight.

## Borrowed vs original

The architecture borrows regulator logic (registry, risk tiers, lifecycle checkpoints echo FDA premarket/postmarket structures and WHO/EU system-governance vocabulary; `analysis/deep-reading/26-national-synthesis.md`, §1 Tier 1) but transposes it into a voluntary institutional program — run 32's Singapore analysis names the registry/risk-matrix/monitoring triad as the importable clinical-governance template, and Duke is the US instance of exactly that pattern (`analysis/deep-reading/32-international-synthesis.md`, §2 secondary import). Within the corpus it is original: no other US health system publishes a comparable pipeline.

## Weaknesses / what's missing

- **Deployment specifics are not on the captured page** — "what the captured page lacks is deployment specifics — but the program exists to govern a live clinical-algorithm portfolio" (run 30). The SOP's operational details and portfolio contents are not public here.
- No ambient-scribe consent regime (the UChicago gap runs the other way).
- No equity-impact trigger like UW's (bias is handled as a framework, not a screening gate).
- Committee throughput and volume metrics unpublished — whether the pipeline scales is unverifiable from the corpus.

## What to steal concretely

1. **"Registry of all algorithmic solutions under consideration for use in patient care"** — the single sentence that eliminates shadow AI; make registration the precondition for procurement, not just deployment.
2. **The three-pathway risk routing** (full / fast-track / registration-only) with named Clinical and Model Owners for low-risk tools — oversight proportional to risk, with accountability always named.
3. **Four-way decision outcomes including "Approval with contingencies" and "Re-Review"** — adopt the vocabulary; binary approve/decline is too coarse for drifting models.
4. **Checkpoint templates and checklists published per stage** — make submission quality the proposer's problem.
5. **Monitoring inside the review mandate** ("to general deployment, monitoring, and maintenance") — reviewers stay attached to the tool for its life, not just launch day.
6. **Office hours + email intake** — two lines of accessibility that convert a governance program from obstacle to service.
