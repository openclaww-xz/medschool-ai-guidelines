# The Master Typology — Classifying AI Governance in Medical Education

**Run 35 deliverable.** Evidence base: all 378 corpus sources (`metadata/sources.json`), 326 per-file deep-reading notes plus 9 run syntheses (`analysis/deep-reading/`), the 274-row clause matrix (`analysis/clauses.csv`), and `analysis/findings.md` / `analysis/summary-stats.md`. Citations in parentheses reference files in `analysis/deep-reading/` unless prefixed `raw/`, `analysis/`, or `metadata/`. Classification counts below were extracted programmatically from the per-file notes (not hand-tallied) and sum exactly to the corpus.

**Corpus accounting.** 378 sources = 212 US med-school artifacts + 67 health-system artifacts + 26 national-framework documents + 26 international documents + 47 peer-reviewed papers. The peer-reviewed 47 are literature, not governance instruments, and are excluded from the institutional map (their findings anchor the verdict in §6); the 331 governance artifacts are all placed (§4).

---

## 1. The five axes

Five independent dimensions emerged from the deep reads. They are genuinely orthogonal in the corpus: posture does not predict sophistication (Penn and Sinai pair prohibition-consultative defaults with elite infrastructure — `27-schoolsA-synthesis.md`), and sophistication does not predict authority (the guidance layer outclasses formal policy on quality while lacking any power to bind — `33-guidance-layer-synthesis.md`).

### Axis 1 — Posture: default-permit / tiered / default-deny

What the document presumes when it is silent about a specific use.

- **Default-permit**: AI use presumptively allowed within enumerated zones, prohibitions reserved for assessment integrity, PHI, and clinical-reasoning substitution. Cohort B instances: Buffalo Jacobs (study-aid permissive, clinical supervised), BU Chobanian (encourage-with-avoid-list), GW-half, UMass Chan's clinical task-allow list (`28-cohortB-synthesis.md`). The rarest polarity at school level: only two inverted defaults appear in batch A (Stanford's "discouraged, not prohibited"; UNC OMSE's allow-listed learning uses — `27-schoolsA-synthesis.md`).
- **Tiered**: every graded assignment carries a declared level; disclosure burden scales with stakes. Reference implementations: ECU Brody's three-level traffic-light with mandatory syllabus declaration and Methods Note; Penn State COM's three approved syllabus models with a non-waivable exam/SOAP floor; UCSF PharmD's AI-1…AI-4 taxonomy; informally GW (`28-cohortB-synthesis.md`; `ucsf-som--pharmd-ai-assessments-policy.md`).
- **Default-deny**: AI on graded work prohibited unless permission is granted — via express faculty permission (VCU), written permission (UC Davis), instructor discretion (LECOM, Touro), course-director permission (both Arizona campuses), or purpose-built AI-required exercises (CWRU) (`28-cohortB-synthesis.md`).

Posture is measurable and does not equal ideology: run 28 shows two default-deny documents (Touro, UC Davis) that are "highly engineered — precision definitions, prompt-level citation, machine-level tool bans — proving the model is not intrinsically naive." The grammar-tool split exposes posture's drafting granularity: exempted at VCU and functionally at Touro/UC Davis, swept in by Penn State's naming of Grammarly — "tool-list-based scope is incoherent across the corpus" (`28-cohortB-synthesis.md`).

### Axis 2 — Sophistication: four binary-able sub-dimensions

1. **Technical understanding.** Does the document name real failure modes — hallucination, drift, re-identification, ambient integration? Positive markers: UVA's "metadata, rare diagnoses, and identifiable features can still identify a patient" (`uva-som--md-program-genai-policy.md`); Icahn's "training-restriction settings change regularly and cannot be relied upon" (`27-schoolsA-synthesis.md`); CWRU's 2023 foresight that AI "will undoubtedly become increasingly integrated into software including word processing programs" (clause 7, `cwru-som--genai-tools-medical-school-assignments-policy.md`); NBME's "AI is never neutral or impartial" (`26-national-synthesis.md`). Negative markers: stale model claims (McGovern's simultaneous "currently using GPT-5" and "post-2021" training cutoff — `uth-mcgovern--policy-on-ai-generative-tools.md`), tool lists naming retired brands (Morehouse's "Google Bard" — `morehouse-sm--student-handbook-student-use-of-ai.md`).
2. **Evidence citation.** Does it cite anything external? UCSF PharmD cites Sentient Syllabus, UNESCO, Monash; GW's disclosure architecture derives from AMEE Guide 192; Icahn credits the University of Wales for its six-category menu (`27-schoolsA-synthesis.md`, `28-cohortB-synthesis.md`). At the other pole, AAMC's principles carry one citation and a disclosed ChatGPT-4.0 first draft (`26-national-synthesis.md`); most conservative-naive documents cite nothing.
3. **Assessment redesign.** Does it restructure the assessment contract rather than prohibit? UCSF PharmD's AI-1…4, ECU's declared tiers, Penn State's statement menu, UNC GMB's eight assignment-type rules, Sydney's two-lane portfolio. In the 168-file guidance layer, exactly three artifacts restructure assessment (UCSF-IGHS taxonomy clone, MUSC's five categories, JHU-EP's Red/Yellow/Green) — "everything else leaves assessment integrity to 'ask your instructor'" (`33-guidance-layer-synthesis.md`).
4. **Tool investment.** Does the institution name a provisioned secure platform? UVA (Dax CoPilot, Claude pilot, Perplexity, OpenEvidence), Stanford (Secure GPT, AI Playground), Sinai (Gemini, ChatGPT Edu, Minerva), U-M (GPT/Maizey rated for PHI), Penn (PMACS matrix), BU (Terrier GPT). "Tool investment is the strongest pioneer separator — every top-5 policy names at least one provisioned platform" (`27-schoolsA-synthesis.md`); the same marker holds in the guidance layer (~40% provision) and health systems.

### Axis 3 — Authority: binding policy / guidance / hub

- **Binding policy**: committee-approved with enforcement hooks — LECOM embeds AI exam use directly in its Honor Code infraction list; Touro's addendum is expulsion-backed and Provost-maintained; Morehouse routes to SAPP with dismissal on the table; UW Medicine's COMP.308 is CCO-signed with named review bodies; Howard's 100.022 is provost-owned (`28-cohortB-synthesis.md`, `uw-medicine--comp308-use-of-ai.md`, `howard-university--ai-policy-100-022-full.md`).
- **Guidance**: substantively normative but self-disclaiming — Harvard's "not new University policy; rather, they leverage existing University policies" is the genre's signature sentence, echoed at WashU, UTSW library, Tufts (`33-guidance-layer-synthesis.md`).
- **Hub/pointer**: routing artifacts with no operative clauses — Morehouse's service-desk KB, HMS's "work with GenAI" page, the provisioned-but-clauseless HopGPT and UTSW AIM portals. 60 of 331 governance artifacts (18%) are hubs or PR pieces (§4).

The corpus's structural finding on this axis: the offices that write guidance (IT, libraries, provosts, teaching centers) lack authority over academic conduct, while the offices with authority (curriculum committees, honor councils, OMEs) were the last to write — "the binding rule a med student most often faces is a data-classification policy designed for employees" (`33-guidance-layer-synthesis.md`). Nationally the same inversion appears at scale: "the bodies that could bind (LCME, FSMB-through-boards) publish the fewest/softest clauses; the bodies with no enforcement publish the most 'must' statements" (`26-national-synthesis.md`).

### Axis 4 — Actor: who holds the pen

Authorship of the guidance layer (n=168, `33-guidance-layer-synthesis.md`): central IT/CISO ~30%, libraries ~15%, provosts ~15%, teaching centers ~8%, **medical-school education units ~8%**, committees/task forces ~8%, compliance ~4%, news/marketing ~7%, handbooks ~5%. Health systems show the same pattern with a twist: "governance locus predicts genre" — compliance-owned (UW) and program-owned (Duke) documents read as enforceable instruments; IT-owned (Mount Sinai DTP, Hopkins) as process; innovation/communications-owned (Houston Methodist, Cleveland Clinic, Ochsner) as marketing; "no document in this run is CMO-office-authored" (`30-health-systems-synthesis.md`).

### Axis 5 — Maturity: adoption wave

Of 90 dated governance rows: 2015 ancestor (1), 2023 (7), 2024 (18), 2025 (23), 2026-to-date (38) — "dated adoption roughly doubles each year, with 2026 already the largest cohort" (`analysis/findings.md`). Wave membership is a blind date-stamp on drafting culture: the 2023 cohort wrote brief, prohibition-default documents by analogy to plagiarism; the 2025–26 cohort writes encyclopedic instruments with governance metadata, tiering, equity clauses, and detection skepticism. Detection stance is "the sharpest generational marker": pro-detection (McGovern/Turnitin, Tucson endorsement, 2023-vintage) → skeptical-but-permitted with FERPA de-identification (JABSOM, SLU) → evidentiary limits outright (Utah "not conclusive evidence"; UAMS "inaccurate and unreliable" plus committee approval before grading-adjacent AI) (`29-cohortC-synthesis.md`).

---

## 2. The sophistication tiers — and the conservative split formalized

The deep-read phase classified every artifact into five tiers. The tiers are the sophistication axis operationalized; this section makes the conservative band's internal split — the corpus's most consequential distinction — scorable by anyone.

**The tiers.** (1) **Pioneer** — permissive-by-default learning posture or full tier architecture, plus real tool investment or assessment redesign, plus technical/evidentiary sophistication. (2) **Progressive-structured** — governance-clean and competent, missing at least one pioneer leg (Penn's administrative completeness without a permissive core; U-M's IT guideline without pedagogy). (3) **Cautious-informed (= knowledge-conservative)** — deliberate, documented caution without pioneer infrastructure. (4) **Conservative-naive (= naive-conservative)** — boilerplate prohibition without evidence of understanding the technology. (5) **Not-a-policy / PR-driven** — hubs, pointers, news, absence.

### Knowledge-conservative vs naive-conservative: operational criteria

The distinction is *not* how restrictive a document is — CWRU bans more than Morehouse — but whether the restriction is chosen with understanding. Score any new document on the two lists below; **knowledge-conservative requires ≥3 K-markers and ≤1 N-marker; naive-conservative requires ≥3 N-markers and ≤1 K-marker**; mixed scores denote transitional documents (the commonest real case, e.g. U Arizona–Tucson: well-governed, committee-approved, but detector-endorsing).

**K-markers (knowledge):**
- K1. Pedagogical rationale stated in the institution's own words (CWRU's "learning is an active and constructive process that requires effort and struggle" — `cwru-som--genai-tools-medical-school-assignments-policy.md`).
- K2. Governance metadata present: named approver, date, review cycle, responsible committee (CWRU: "Approved By: WR2/CSC… annual review"; USC Keck: MECCC-approved; ECU: EAC-approved with expiration date).
- K3. Forward-looking acknowledgment of technological change — ambient integration, tool-list decay, review commitment (CWRU clause 7; Geisel's dated draft→MEC→DAB→Faculty Council lineage; UC Davis's EHR-only clinical scope).
- K4. A deliberate exposure valve: permitted study uses, AI-required exercises, or carved-out tool classes (CWRU's AI-required assignments; VCU's study-aid permission; UC Davis grammar/organizing band).
- K5. Technically accurate, current statements about models; correct failure-mode vocabulary (hallucination named accurately, re-identification understood).
- K6. Enforcement calibrated to evidence — no reliance on AI detectors; sanctions proportional and routed through named bodies.

**N-markers (naive):**
- N1. Tool-name-dependent enumeration that is dated or consumer-chatbot-framed (Morehouse: "chat GPT, GPT-4, Copilot, Google Bard" — Bard was retired before the 2026–27 handbook appeared; `morehouse-sm--student-handbook-student-use-of-ai.md`).
- N2. Zero clinical/data-governance awareness — no PHI, HIPAA, or clinical-environment content in a document governing medical students (Morehouse, McGovern, KPCOM, Mayo MCCMS clause; `29-cohortC-synthesis.md`, `28-cohortB-synthesis.md`).
- N3. Reliance on AI-detection software for enforcement (McGovern's automatic Turnitin/Canvas detection; Tucson's endorsement — the cohort outliers; `uth-mcgovern--policy-on-ai-generative-tools.md`, `28-cohortB-synthesis.md`).
- N4. No governance metadata — no approver, no date, no review path (Morehouse: "no named author, approval body, effective date, or review cycle"; `morehouse-sm--student-handbook-student-use-of-ai.md`).
- N5. Stale or internally inconsistent factual claims, indicating accretive editing without reconciliation (McGovern's GPT-5 vs "post-2021" cutoff contradiction).
- N6. Boilerplate by analogy — ghostwriter/plagiarism framing transposed wholesale, person-analogy rules with no AI-specific mechanics (`33-guidance-layer-synthesis.md` on the person-analogy rule's shared source pool).
- N7. Internal incoherence in the operative text (Morehouse's permissive-assignment default colliding with dismissal-level exam severity; "chat GPT" orthography).

**Calibration against the corpus.** CWRU scores K1, K2, K3, K4, K5 (accurate for 2023), K6 → 6 K, 0 N: knowledge-conservative, the type specimen. Morehouse scores N1, N2, N4, N7 with one partial saving grace (citation elements + hallucination literacy, its notes' own verdict) → naive-conservative. McGovern scores N2, N3, N5 against K-markers for citation format and humanities-grounded reflective-writing protection → naive-conservative despite early adoption and historical influence (it is cited by LSUHSC-NO — influence and quality are different variables). The seven US naive-conservative documents are: Morehouse handbook, UTHealth McGovern, UF COM OSA page, Nova KPCOM handbook, PCOM integrity code, Mayo MCCMS respiratory-care clause, Utah SOM handbook clause (per-file notes; §4). The Utah SOM case adds a subtlety the criteria capture: a *handbook clause* can be naive inside an institution whose *university* guidelines are pioneer-grade — classification attaches to documents, not institutions (`29-cohortC-synthesis.md`: "institutional maturity ≠ curricular propagation").

---

## 3. Why the split matters

The conservative split is the corpus's predictive engine. Every knowledge-conservative document already contains the hooks for upgrade — a review cycle to trigger, a permitted-use band to widen, a governance body to hand tiering to. Naive-conservative documents lack upgrade paths: their tool lists age (N1), their enforcement premise (detection) is being withdrawn by the evidence, and nobody owns revision (N4). The 2023-vintage naive documents have mostly not been revised — McGovern's "post-2021" line survived into an October 2025 update — while the knowledge-conservative 2023 documents (CWRU, Yale provost, UCSF PharmD) seeded the 2025–26 wave's vocabulary. The typology therefore predicts institutional trajectory better than posture does: a default-deny-but-informed school (UC Davis, Touro) is one faculty-development cycle from tiered maturity; a naive-permissive school would be a contradiction the corpus does not yet contain.

---

## 4. The map: every institution placed

Counts extracted programmatically from the per-file classification sections; rows sum to the corpus. Health-system rows combine the 16 deep-read notes with a clause-matrix/keyword triage of the 51 remaining artifacts (governance-keyword density vs PR-language density vs zero operative clauses, cross-checked against `analysis/clauses.csv`).

| Sector | Pioneer | Progressive-structured | Cautious-informed (knowledge-conservative) | Conservative-naive | Not-a-policy / PR | Total |
|---|---|---|---|---|---|---|
| US med schools | 40 | 62 | 61 | 7 | 42 | 212 |
| Health systems | 7 | 24 (5 deep-read + 19 governance-bearing) | 18 (2 + 16 thin) | 0 | 18 (10 hub/news + 8 PR) | 67 |
| National frameworks | 16 | 5 | 4 | 1 (AAP) | 0 | 26 |
| International | 3 | 14 | 6 | 3 | 0 | 26 |
| **Total** | **66** | **105** | **89** | **11** | **60** | **331** |
| Peer-reviewed (literature, unclassified) | — | — | — | — | — | 47 |
| **Corpus** | | | | | | **378** |

**Named placements (selection; full lists in per-file notes).**

- **US pioneers (40)**: UVA, UCSF (PharmD/Bridges/IGHS), Icahn MSSM, Stanford, UNC (GMB + OMSE), ECU Brody, GW SMHS, Buffalo Jacobs, Perelman, U-M, Penn State COM, BU, Touro, UMass Chan, JABSOM, UVM Larner, UAMS, Utah (system), OHSU (GME-48), UKY GME, MUSC, LSUHSC-NO, NYU Grossman, Rochester provost, Pitt Ad Hoc, UCSD (Senate-Admin + privacy), Wake Forest AIWG, Vanderbilt AA, Weill Cornell MedEdAI, Feinberg, SLU, CU SOM, KCU, JHU GenAI hub, UNC OMSE, UNC GMB.
- **US naive-conservative (7)**: Morehouse SM handbook; UTHealth McGovern center policy; UF COM OSA page; Nova KPCOM handbook clause; PCOM integrity code; Mayo MCCMS respiratory-care clause; Utah SOM handbook clause.
- **Health-system pioneers (7)**: Duke Health (ABCDS), Mount Sinai (MSHS 223 + governance), UW Medicine (COMP.308 + glossary), UCSF Health (inferred), UChicago IM residency (Abridge); plus, in the triaged 51, OHSU Health's governance page and UI Health Care's digital-health AI tool governance (highest governance-keyword densities).
- **Health-system PR-driven**: Cleveland Clinic (largest disclosed footprint, zero governance/consent content), Houston Methodist ("succeed fast, fail fast"), plus triaged Jefferson strategy, MedStar Georgetown AI co-lab, UCLA patient-communication automation, VCU Health workgroup news, VUMC research-advances news, Penn State Health liability news, Hartford launch coverage, Meharry–Oracle partnership.
- **National frameworks**: pioneers AMA (×5 documents), AAFP, ACP, NBME/USMLE (×2), FSMB (×2), AMEE (×2), ACR–SIIM, WHO Europe, AAMC GIR survey; progressive-structured AAMC principles, ACGME plenaries, Macy; cautious-informed LCME (challenge identified, Element 7.2 clause in comment to Jan 2026); conservative-naive AAP webinar hub (`26-national-synthesis.md`).
- **International**: pioneers Sydney (two-lane ×2), UK joint regulators; progressive-structured HEE, MSC, CoDH, Melbourne, Karolinska, Amsterdam UMC rules, UvA, Toronto, Royal College, Singapore AIHGle 2.0; naive Temerty MD index, Amsterdam UMC topic overview, India NMC (~150 words of AI content across a 2.96 MB compendium) (`32-international-synthesis.md`).

Two map-level facts deserve emphasis. First, **sophistication's center of gravity is not the private elites**: "the two most complete documents in this cohort are from small/public state schools (JABSOM, UVM) or state systems (Utah, UAMS, OHSU)… elites wrote early (Feinberg 9/2023) and concise; state schools wrote later (2025–2026) and encyclopedic" (`29-cohortC-synthesis.md`). Second, **the modal artifact is not a policy at all**: 60 of 331 (18%) are hubs, news, or PR, and another large band is IT data-classification pages — a student searching their institution's guidance most often lands on a CISO page or a LibGuide, not a curriculum-committee instrument (`33-guidance-layer-synthesis.md`).

---

## 5. Diffusion: who borrows from whom

### 5.1 State-to-state, not elite-to-mass

The citation network among schools runs sideways and downhill. OHSU's GME-48 — one of the corpus's best GME instruments — credits **UT Health San Antonio**, a state school, as its source. LSUHSC-NO's reference list cites McGovern (a *center-level* humanities policy), Feinberg, UCSF, UVA, and UAB. MUSC adapts an academic-publishing scale (Perkins et al.'s AIAS) under CC license and is itself mirrored by Marshall University (`29-cohortC-synthesis.md`). "Elite origin is not the dominant propagation pattern" — no corpus document cites Harvard's, Yale's, or Stanford's school-level text as its template, while cross-state adaptation of ECU-style tiers, MUSC's categories, and UT-system language is documented.

### 5.2 Library and teaching-center networks are the real diffusion channels

Run 33 traces the intermediate nodes: Rush CTEI's AI-literacy module → UCSD's adaptation; UCSF Pharmacy's AI-1…4 taxonomy → UCSF-IGHS clone; Arizona libraries → Penn State tutorial; U. Arizona → Rush guides; Canada's GOC framework → NSU infographic; ACM's proportionality rule → Rochester and UNC; AMEE Guide 192 → GW's disclosure architecture; the University of Wales menu → Icahn. "Policy diffusion in medical-ed AI runs through libraries and teaching centers, not through deans' offices" (`33-guidance-layer-synthesis.md`). The same layer is ahead of policy on detection skepticism "because librarians and teaching centers read the literature."

### 5.3 The 2023-elite-early vs 2025–26-state-encyclopedic pattern

The dated corpus shows two qualitatively different waves. The 2023 first wave (7 dated documents: VUMC network block, CWRU, Yale provost, UCSF PharmD, UNC GMB, Vanderbilt, Geisel) came from elite-adjacent institutions reacting to ChatGPT with brief, prohibition-default or courageously-permissive texts. The 2025–26 wave (61 dated documents, 38 in 2026 alone) is dominated by state and public institutions writing encyclopedic instruments — OHSU GME-48, Perelman UME.AC.119, ECU SOP, Buffalo Jacobs, Utah system guidelines, UW COMP.308, Howard 100.022, SLU v3.1 — with governance metadata, tiering, equity clauses, and self-disclosure of AI-assisted drafting (GW's task force, UMass's ChatGPT-5.2 review, Touro's AI-summary acknowledgment — "a new genre marker of 2026-vintage documents," `28-cohortB-synthesis.md`). Notably, "institutional self-scrutiny is a state-school phenomenon… no elite-private document does either" (`29-cohortC-synthesis.md`).

### 5.4 National-leader vs school-practice disconnect

At the framework layer the borrow-direction is well-documented: AMA is "the corpus's conceptual center of gravity" — its ethics/evidence/equity architecture, Augmented Intelligence vocabulary, and role-partitioned responsibility model recur everywhere; FSMB translates AMA/AAFP ethics into state-board-enforceable form; NBME opened the assessment-validity space; WHO supplies the system-governance vocabulary (`26-national-synthesis.md`). But the outbound citations stop at the national layer. Despite the AAMC principles existing in-corpus, "school and system policies essentially never anchor to it (1/275, 0.4%)" (`analysis/findings.md`) — the single aligning document being Penn's, which used the AAMC checklist (`27-schoolsA-synthesis.md`). AMA leads the thinking; AAMC is institutionally weighty but textually ignored; LCME — the only body with binding power over medical schools — is functionally absent, with one clause in revised Element 7.2 in public comment to January 2026 (`26-national-synthesis.md`). The result: national frameworks generate vocabulary, schools generate instruments, and almost nothing binds the two — must-density and enforceability are inversely distributed.

### 5.5 International imports waiting to happen

The international synthesis identifies the Australia two-lane model as "the only model that is honest about enforcement physics" — its axiom "any unenforceable restriction damages assessment validity" is precisely the problem US school policies wrestle with via detector reliance and per-course patches; its migration cost is lowest for medical schools, which already run the lane-1 toolkit (OSCEs, shelves, clerkship observership) (`32-international-synthesis.md`). No US school has yet imported it; Stanford's enforcement realism ("restricting the use of AI tools cannot be strictly enforced") and Sydney's axiom are independently converged conclusions — the classic precondition for diffusion.

---

## 6. The landscape verdict: 2026–27 and what the typology predicts

**Where the field is.** The corpus's center of mass has moved from guidance (2023) to formal policy (2025–26): formal policy 58 of 274 matrix rows, with 2026 the largest dated cohort. The demand side is settled — meta-analytic prior use 63.2% across 96 studies/45,000+ students, 88.7% ever-use among US medical students, 21–46.5% already using GenAI for clinical notes/differentials (`31-peer-reviewed-synthesis.md`) — while the supply side lags everywhere it has been censused (ASPPH: 11.6% formal policy; our matrix: 21.5%). The gap is closing from an unexpected direction: state schools, GME offices, and health systems, not the elites and not the national bodies.

**What the typology predicts for 2026–27 — falsifiably:**

1. **Tiering becomes the dominant architecture.** Run 28's model comparison finds the tiered model "dominates on every evaluation axis that matters," and its cheapest variant (Penn State's statement menu) requires no new bureaucracy. Prediction: the 2026–27 cohort of formal policies will be majority tiered or statement-menu, absorbing the current default-deny band's knowledgeable half (UC Davis, Touro, VCU types). The naive-conservative rump will not upgrade — it will simply age (§3).
2. **Detection skepticism becomes the due-process norm.** The generational marker is already clean: 2023 adopters endorse, 2025–26 state documents treat detection as an evidentiary problem. Expect the pro-detection holdouts (a shrinking set after McGovern-type revisions) to flip or delete; expect honor-code case law — not policy text — to force the flip, as at Columbia, where detection reports already "cannot be sole proof in Dean's Discipline" (`33-guidance-layer-synthesis.md`).
3. **LCME Element 7.2 converts the cautious-informed middle.** The single drafted clause ("appropriate use of artificial intelligence and other emerging technologies") is in comment to Jan 2026. If adopted, every accredited school acquires an external reason to move from handbook clause to designed policy — the typology predicts the biggest single-step sophistication jump in the corpus's naive-conservative and not-a-policy cells, because accreditation is the one lever that reaches institutions that ignore AAMC (0.4% uptake) and AMA alike.
4. **Agentic AI is the next drafting wave, and almost nobody is ready.** Exactly one document in 331 contemplates agents (Touro's ban); ACGME's 2026 plenary is the only national treatment (`28-cohortB-synthesis.md`, `26-national-synthesis.md`). When agent-native tools reach clinical learning environments in 2026–27, the corpus's tool-list-based scopes (the incoherence run 28 flags) fail first; expect a 2027 revision wave led — per the diffusion pattern — by the same state-school/GME tier that wrote the encyclopedic 2026 instruments.
5. **The clinical layer plays catch-up, inverted.** AAMC's GIR survey shows education with MORE policy than clinical missions (69% vs 51%) — frameworks ahead of practice exactly where patients are (`26-national-synthesis.md`). Health-system governance is arriving (UW COMP.308 effective 2026-09-01; monitoring regimes at Duke, Mount Sinai, UCSF), but PR-driven adopters (Cleveland Clinic's consent-silent Ambience rollout) remain the largest disclosed footprints with the least governance. Expect the three-leg test (governance + tooling + monitoring) to become the health-system norm at compliant systems while the PR tier keeps deploying — the typology's PR cell is the corpus's highest-risk population.
6. **The guidance layer formalizes or fossilizes.** The 60 hub/not-a-policy artifacts and the self-discharging guidance tier face a choice as binding policy arrives: either they become the literacy-and-citation craft layer on top of formal policy (the Rush/Dartmouth library pattern) or they are superseded. The diffusion evidence (§5.2) says the library network will keep outperforming the policy layer per-word — and keeps being ignored by it.
7. **Equity remains the least-diffused mature element.** Free-tool floors, non-AI alternatives, and premium-tool-gap clauses appear almost exclusively at ECU, GW, BU, and Sydney (`28-cohortB-synthesis.md`, `32-international-synthesis.md`). No external force (LCME, AAMC, AMA) currently mandates it; prediction: it stays rare through 2027 absent an accreditation hook.

**The one-sentence verdict.** Medical education's AI governance is being built from the middle out — state schools borrowing from each other through libraries and teaching centers, ahead of their national bodies and behind their own health systems — and the typology's tier structure says the field's next two years are the cautious-informed middle's migration upward into tiered, detection-skeptical, equity-aware policy, while a small naive-conservative rump and a large PR-driven clinical tier persist as the corpus's unfinished business.

---

*Cross-references: `analysis/REPORT.md` (flagship synthesis), `analysis/findings.md` (counts), `analysis/deep-reading/26–33 syntheses` (sector evidence), per-file notes throughout `analysis/deep-reading/` (all placements).*
