---
run: 33 — guidance-layer schools deep-read synthesis
date: 2026-09-17
files_read: 168 (all remaining raw/us-med-schools files without prior notes)
companion_notes: 168 per-file notes in this directory mirroring source filenames
---

# Run 33 Synthesis — The Guidance Layer: Anatomy of the Layer That Governs While Policy Doesn't

## What this cohort is

The 168 files remaining after runs 27–29 are, overwhelmingly, **not formal medical-school AI policy**. They are the layer *beneath, above, and beside* policy: IT security pages, library LibGuides, provost letters, teaching-center faculty guides, task-force announcements, committee reports, product catalogs, news blogs, and handbooks with an AI clause bolted in. Read together they answer a different question than runs 27–29 asked. Those runs asked "what do enacted policies say?" This run asked: **who is actually steering medical students' AI behavior at institutions without enacted policy — and what happens as a result?**

## 1. Who writes the guidance layer

Counting primary authorship of the substantive documents (n=168; many are multi-layer stacks):

| Author type | Share (approx.) | Exemplars |
|---|---|---|
| **University/central IT & CISO offices** | ~30% | Harvard HUIT, Northwestern IT, UW-Madison IT, UT-Austin ISO, Temple IT, Wayne State C&IT, UNLV IT, Tulane IT, Rutgers OIT, U Rochester IT, WashU, UConn AITS, ATSU ITS, Drexel IT |
| **Libraries (health-sciences and campus)** | ~15% | Rush, OHSU, UTSW, Weill Cornell, VCU, Penn State Harrell, KCU, UNM HSLIC, RFU Boxer, Galter, NSU, URMC Miner, UCSD, DMU, Stanford Lane, OU-HSC, Touro-TUN |
| **Provosts / offices of academic affairs** | ~15% | Yale, Harvard, Brown, Columbia, Georgetown, Vanderbilt (Academic Affairs), Dartmouth, Rochester, Hofstra, Wake Forest, Duquesne, SLU, UF |
| **Teaching centers (CTE/CETL/CTEI/DTEI)** | ~8% | Rush CTEI, UConn CETL, MUSC CATL, UCI DTEI, OU CFE, TAMU CTE-adjacent, UCSD AIO |
| **Medical-school units (OME, education offices, institutes)** | ~8% | NYU Grossman IIME, CU SOM MD program, Miami Miller Office, WCM MedEdAI, Pritzker ASCEnD, UF COM, Baylor clerkship/COD, OHSU DMICE (single instructor), Einstein |
| **Committees & task forces (advisory/deliberative)** | ~8% | Pitt Ad Hoc Committee, UCSD Senate-Admin Workgroup, KUMC Steering, Temple Katz TF, UMass Chan draft, UK ADVANCE, KU Taskforce/Risk Council |
| **Compliance/privacy offices** | ~4% | UNMC (compliance-owned), UCSD Privacy Office, VCU ICO, UAB |
| **News/marketing/blogs** | ~7% | KCU blogs, PCOM Georgia feature, UMMC VC Notes, MUSC announcements, Hofstra/AI symposium pages |
| **Handbooks/catalogs with embedded clauses** | ~5% | Wake Forest companion, Loyola Stritch, Mayo MCCMS, KPCOM, USD SSOM, Nova, SHSU (absent), Pitt UPSOM, SLU (excludes SoM), UMN SIR |

The headline: **IT and libraries — not curriculum committees — are the default AI governance layer in American medical education.** Where a school has no enacted policy, the artifact a student actually finds is a CISO data-classification page or a LibGuide. Only ~8% of this cohort's substance comes from the medical-school education offices that own learner conduct.

## 2. What the guidance layer does

Five functions, in descending order of frequency:

1. **Data security (near-universal).** Every IT-authored page converges on the same clause: no confidential/PHI/FERPA/PII/restricted data into unapproved public tools, gated by a data-classification regime (Harvard Levels 1–5; Utah Rule 4-004C; UW classifications; UC P1–P4; UNM P-class; CU three-tier). The best versions add genuinely sophisticated variants: foreign-processing jurisdiction risk (Drexel), BAA-on-file-for-PHI (Utah), PHI banned even in *approved* enterprise tools (Einstein), DUA-overrides-tool-approval (HMS), "web search functionality must be disabled" contract terms (UT-Austin), statistical small-cell-size rule (Wayne State).
2. **Tool provisioning (~40%).** Secure instances: HopGPT, nyugpt, chat.rochester.edu, PhoenixAI/ChatUCM, DartmouthChat/Claude, ChatGPT Edu (Hofstra campus-wide, Einstein, UMass, UMN), Copilot everywhere, Qualified Chat UR/URMC for health-system data, MSIT's PHI-rated ambient catalog (Abridge/DAX). Provisioning is the strongest pioneer marker here too: NYU, Rochester, Hofstra, Einstein, Harvard/HMS, Geisel, UTSW(intranet).
3. **Routing/deferral (~35%).** The layer's signature move: "no university-wide policy; ask your instructor" (Iowa, UNLV, KCU library, WVSOM, OHSU library, UConn CETL, UCLA Conduct Code, Rutgers, UNM, Columbia). It is honest, decentralized, and pushes the entire pedagogical decision to the weakest unit — the individual course director with no template.
4. **Literacy & citation craft (~20%).** Libraries and teaching centers teach what policies assume: APA/MLA AI citation formats (Rush CTEI's are the most complete), acknowledgment templates (Dartmouth's three verbatim samples with model/version/date/prompt), prompt frameworks (TRACI at WVSOM, C.R.A.F.T. at PSOM), disclosure schemas (Rochester/UNC adopting ACM's proportionality rule), AI-literacy modules (UCSD adapting Rush's CTEI module — visible diffusion chain Rush→UCSD).
5. **Misconduct boundary-setting (~15%).** The person-analogy rule — "treat AI like assistance from another person" — recurs at NYU Grossman, Mayo MCCMS, UNLV, USD SSOM, and (as a classmate at Vanderbilt) suggesting a shared source pool; prohibition-default clauses appear in KPCOM, Columbia VP&S, Dartmouth undergrad, Pitt UPSOM, SLU.

## 3. What the guidance layer does NOT do

- **It does not assess.** Only three artifacts in 168 restructure the assessment contract: UCSF-IGHS (a clone of the Pharmacy AI-1..4 taxonomy), MUSC's five-category framework (announced layer), and JHU-EP's Red/Yellow/Green student guidance. Everything else leaves assessment integrity to "ask your instructor."
- **It does not govern clinical learning environments.** Baylor's surgery-clerkship COD is the only clerkship-level AI rule set; NYU Grossman's matrix is the only public/private routing for clinical cases; UTSW gates its clinical rules behind VPN. Ambient-documentation procurement (UTHealth MSIT, UMMC, UW) proceeds *ahead of* any learner rules for those tools.
- **It does not enforce.** Guidance disclaims itself constantly: "not new University policy; rather, they leverage existing University policies" (Harvard, WashU, UTSW library, Tufts). Enforcement lives in honor codes that mostly predate GenAI (PCOM's Rutgers-derived code has no AI clause; RFU's policy index lists none; SLU's new policy explicitly excludes the School of Medicine).
- **It rarely detects-differently.** The exception cluster is notable: Rush's UAC0039 (false positives, bias against non-native English writers), Columbia (detection reports cannot be sole proof in Dean's Discipline), Rochester provost (unreliable, biased, easily defeated), Rush CTEI (perplexity/burstiness literacy), Duquesne, Hofstra, OSU. Guidance is ahead of policy on detection skepticism because librarians and teaching centers read the literature.
- **It does not close its own loops.** UMass Chan shows a draft in committee; Temple Katz announces a task force; Touro says the framework is "still in development"; Einstein's full role-specific policy is linked but uncaptured; UMMC's policy has been "under development" since Dec 2024; WVSOM states outright that "students do not have a specific academic integrity policy around GenAI."

## 4. The governance vacuum, precisely stated

1. **Ownership gap.** The offices that own AI guidance (IT, libraries, provosts, CTEs) lack authority over academic conduct; the offices with authority (curriculum committees, honor councils, SOM education offices) are the last to write. Result: the binding rule a med student most often faces is a data-classification policy designed for employees, or a one-clause handbook prohibition written by analogy to ghostwriters (Loyola, KPCOM, Wake Forest companion).
2. **Layer inversion.** Where both layers exist, the school is frequently *stricter* than its university: Columbia's permissive-encouraging university policy ("we encourage you to explore") sits above VP&S's prohibition-default; Dartmouth's default-deny undergrad guidelines sit beside Geisel's committee-approved policy. Students crossing layers meet contradictions nobody reconciles.
3. **Investment without rules.** UF ($10M/yr QPSi, first-in-nation AI curriculum), SHSU-COM (Medical AI Institute), UTSW (AIM), KCU (AI from year one + AI-guided POCUS), UMMC (deployed ambient and predictive AI) — institutions build world-class AI *capability* while their learner-facing corpus is a blog post and an AI-free handbook. The gap is not resources; it is that governance of learner conduct has no natural owner in the modern medical enterprise.
4. **The vacuum is filled from below, unevenly.** Single instructors write better rules than their institutions (Hersh's evidence-based OHSU course policy); libraries write better citation norms (Rush, Dartmouth); teaching centers write better detection policy (CTEI); committees write better architecture than anyone (Pitt, UCSD, Wake Forest) — and all of it is non-binding. The corpus's few pioneers that are also *enforceable* (UCSF-IGHS/Pharmacy taxonomy, MUSC framework + Honor Code) prove the layer can be closed.
5. **Public-record exposure.** FOIA/CPRA clauses (VCU ICO, UCSD privacy guidelines) reveal a risk almost no school communicates to students: AI chats about university business may be public records — even from personal accounts. Only guidance layers at public universities know this.
6. **State law is arriving through the guidance layer first.** UT-Austin's ISO embeds the Texas consequential-decision statute (now including "medical or mental health diagnosis, treatment, or advice"); U-Arizona tracks HB 2175 (AI in claim denials); UNLV maps NSHE statutes. Medical schools' formal policies (runs 27–29) almost never cite statute — their IT offices already live under it.

## 5. Classification of the 168 files

| Classification | Count | Notes |
|---|---|---|
| Pioneer (guidance/deliberation tier) | 9 | NYU Grossman IIME guidelines; Rochester provost education guidelines; UCSF-IGHS (taxonomy clone); MUSC framework page + announcement; Pitt Ad Hoc report; UCSD Senate-Admin report; UCSD privacy guidelines (AI assistants); Wake Forest AIWG guidelines; WCM MedEdAI (curriculum tier) |
| Progressive-structured | 58 | incl. Vanderbilt AA guidance (2023 default-permit), Columbia university policy, HMS IT, UChicago, UT-Austin ISO, Tufts TTS, UNMC, CU SOM MD guidelines, Baylor clerkship, Rush trio (policy/guide/CTEI), JHU teaching + EP guidance, Geisel GAIN, MUSC ecosystem pages, WVSOM hub, Hofstra pair, UNLV, UCSD AIO, Emory pair, Georgetown, Penn State, Arizona hub, Einstein, UMMC, UK ADVANCE, KUMC, etc. |
| Cautious-informed | 41 | Harvard provost/HUIT/ARI, Yale trio, Rutgers, U Iowa pair, UNM pair, Temple, Wayne State, CWRU provost, Cincinnati trio, MSU pair, UCLA DTS, Pitt UPSOM integrity, Columbia VP&S plagiarism, Dartmouth coursework, SLU, UF regulation, Tulane, Northwestern pair, Galter, ATSU pair, UAB trio, Touro, Weill Cornell library, WashU, USD SSOM, etc. |
| Conservative-naive | 3 | Mayo MCCMS respiratory-care clause; KPCOM handbook clause; PCOM integrity code (no AI clause) |
| Not-a-policy (hub/pointer/absence/news/program pages) | 57 | including 4 verified AI-free handbooks (Wake Forest MD, SHSU-COM, RFU index, Baylor MD index — absence itself documented), 1 mismatched capture (UNM faculty-senate URL returns a journal's publishing policy — re-crawl), 1 duplicate (Rush excerpts), and the provisioned-but-clauseless hubs (JHU HopGPT, UTSW AIM, UF COM, Miami, OU) |

**Majority stance: cautious-informed / progressive-structured guidance (~59% of files combined), with the modal artifact a data-security-plus-ask-your-instructor page.** If the hub pages are excluded and only substantive documents are counted, the modal stance is progressive-structured (58 of 111 substantive). The guidance layer is *more permissive, more detection-skeptical, and more tool-aware* than the formal-policy cohort of runs 27–29 — because its authors (librarians, teaching centers, provost committees) read the literature and talk to students, while policy authors write from risk-management briefs. The layer's fatal flaw is not quality; it is authority.

## 6. Cross-run finding

Runs 27–29 showed formal policy clustering at cautious-informed with a state-school pioneer surge. Run 33 shows the guidance layer *preceding, enabling, and often outclassing* that policy — and reveals the diffusion network's intermediate nodes: Rush CTEI → UCSD module; UCSF Pharmacy → IGHS; Arizona libraries → Penn State tutorial; U. Arizona → Rush guides; Canada GOC → NSU infographic; AIAS (Perkins/Furze) → MUSC; ACM → Rochester/UNC. Policy diffusion in medical-ed AI runs through libraries and teaching centers, not through deans' offices. Any strategy for improving school AI governance must route through the layer that is already doing the work.
