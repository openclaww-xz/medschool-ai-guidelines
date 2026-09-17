# Run 36 — Independent Verification of the Deep-Reading Layer

**Method.** Random sample (seed 36) of 30 notes from `analysis/deep-reading/` (10 pioneer-classified, 6 conservative-naive-classified, 14 other), stratified to prioritize the classifications that drive the typology. For each note: (1) opened the note's own `source_file` raw document; (2) extracted every quoted string ≥25 chars and verified each against the normalized source text (whitespace/punctuation/smart-quote/diacritic-insensitive), with manual grep adjudication of every non-match; (3) checked clause-inventory completeness by extracting normative sentences (must/shall/prohibit/required) from the source and testing whether each is covered by quote or paraphrase in the note; (4) read each note's classification rationale against the source content; (5) checked `read_status: full` / `approx_words_read` consistency against actual source lengths.

Two early automated passes over-flagged (24/30) because of quote-parity artifacts, elision stitching, and paraphrase blindness; every flag was manually adjudicated by direct grep with context. Results below are after adjudication.

## Per-note verdicts (30)

| Note | Class | Verdict |
|---|---|---|
| aamc--meeting-the-moment | progressive-structured | faithful — all spot-checked quotes present (incl. "Inaugural 16 members representing over 10 countries", Engage/Embed/Evaluate, Macy collaboration, admissions principles title) |
| aamc--principles-ai-use | progressive-structured w/ naive-tech caveat | faithful — all 7 principles verbatim-verified incl. ChatGPT-4.0 drafting disclosure |
| ai-family-nursing-policy-framework | (unclassified summary) | faithful — 5 policy domains paraphrase-match source exactly; core quote verified |
| ama--ai-principles | pioneer | faithful — 62 quotes checked, all traced incl. "defaulted to public 'agreements'", quadruple-aim clause; 86k-char source, 12.3k words read: consistent with full read |
| ama--cme-report-4-a19 | pioneer | minor-omissions — 11 adopted recommendations covered as claimed; ~19 uncovered normative sentences are background/quoted LCME-AAMC material, not the report's own directives, but "complete clause inventory" slightly overstates |
| amee--guide-178-ai-hpe-assessment | pioneer | faithful — 90k-char source, 12.5k words claimed: plausible full read; key quotes verified (essay-purpose passage, AI-detectors, learning-paths) |
| amsterdam-umc--ai-topic-overview | conservative-naive (non-governing showcase) | faithful — classification explicitly justified (no governance content in source); news-item quotes verified |
| artificial-intelligence-use-medical-education-best-practices | (summary) | faithful w/ sloppiness — "co-design" is a fair paraphrase of "involving physicians in AI design and development"; internal inconsistency quoting the same sentence two ways |
| bu-chobanian--md-program-ai-use-policy | — | faithful — form-field quotes (Effective Date June 26 2025, Terrier GPT) verified |
| buffalo-jacobs--genai-use-policy | — | faithful — 52/52 quotes ≥0.9 shingle match; Sedhom & Torous citation incl. the note's own flag of a malformed DOI actually present in source |
| clinical-teacher-bridging-policy-gap | — | faithful — honestly marked abstract-only (2.6k-char source), no quotes to check |
| cwru--provost-ai-policies | progressive-structured | faithful |
| cwru-som--genai-assignments-policy | — | faithful — WR2/CSC approval line verified verbatim |
| fsmb--navigating-responsible-ethical-ai | pioneer | faithful — core recommendations verified ("tool for medical practice", state-board disclosure guidelines, deviation-documentation duty) |
| geisel-dartmouth--genai-policy | cautious-informed | faithful — scope sentence, honor-code/plagiarism clause, GPT-4.1-mini drafting disclosure all verbatim in source |
| genai-medical-training-utilization | (summary) | faithful — no quotes, counts-based summary consistent |
| kcu--medicine-reimagined-blog | — | faithful |
| **mayo-mccms--respiratory-care-handbook-genai-policy** | conservative-naive | **fabricated-quote (one)** — see below |
| medical-student-experiences-chatgpt | (summary) | faithful |
| medical-students-attitudes-perceptions | (summary) | faithful — 69k-char source, 11.1k words claimed: consistent |
| nbme-usmle--program-discusses-chatgpt | cautious-informed | faithful — "insufficient evidence" and MedQA/third-party findings verbatim; "AI passing the exam ≠ exam compromised" is the note's own gloss, punctuated as such; "optimistic... mindful of the risks" both words present in one sentence |
| osu-com--ai-responsible-use | progressive-structured | faithful — self-check questions ("Have I checked for hallucinations", "unfair advantage", "bypass the learning process") all verbatim |
| pcom--academic-integrity-policy | conservative-naive (pre-AI code) | faithful — Rutgers provenance credit verified; "no AI-specific clause" claim spot-checked, holds |
| touro-university--ai-policy | cautious-informed (under construction) | faithful — "formal policy framework is still in development" verbatim |
| tufts-university--it-guidance-using-ai | progressive-structured (IT layer) | faithful — all 8 normative items (approval regime, vendor-T&C literacy, data classes, "no longer private") covered |
| u-arizona--ai-guidelines | progressive-structured | faithful — both governing quotes verbatim |
| ucla-dgsom--responsible-use-principles | cautious-informed | faithful — MFA/access-control and bias/ethics items verified; numbered-list compression is the note's own format, not quoted |
| ucsf-som--bridges-curriculum-genai-usage-policy | pioneer | faithful — LCME 5.9/7.4/7.7 anchors, sensitive-data prohibition on commercial platforms, CCEP 12/10/2024 approval all verbatim |
| weill-cornell--mededai-wcm | pioneer | faithful — competency items ("Carry out AI-enhanced clinical encounters", "Describe basic concepts in AI, ML...") verified verbatim (my first-pass miss was an encoding artifact in the raw file) |
| yale--ai-standards-health-sciences | cautious-informed | faithful — all framing text verbatim |

## The one fabrication found

**mayo-mccms--respiratory-care-handbook-genai-policy.md** quotes a section header as `"ARTIFICIAL INTELIGENAL [sic]"`. The actual source header (line 1180 of the raw handbook) reads `USE OF GENERATIVE ARTIFICAL INTELLIGENCE PLATFORMS` — a real typo ("ARTIFICAL"), but a *different* typo than the one the note claims to quote verbatim. "INTELIGENAL" appears nowhere in the 86k-char source in any case variant. Every substantive clause in the note (all 5 inventory items, the person-analogy framing) IS verbatim-present, and the note's scoped read_status ("full read of AI policy cluster... no other AI mentions (verified)") is accurate — the handbook's only AI content is that one cluster, which I confirmed by scanning all AI-term matches across the full document. So this is an invented **detail** (a misquoted [sic]), not invented substance. Bluntly: the note dresses up a plausible-looking typo it never actually saw — exactly the failure mode verification exists to catch, and a warning that even "verbatim [sic]" quotes need grep-verification before being cited downstream.

## Aggregate

- **Faithful: 28** (2 of these with minor sloppiness: best-practices internal quote inconsistency; ama-cme "complete inventory" overstatement → counted as minor-omissions where flagged above: 2 minor-omissions)
- **Fabricated-quotes: 1** (mayo — one invented [sic] detail; substance otherwise verified)
- **Misclassified: 0.** Every classification checked (10 pioneer, 6 conservative-naive, others) carries an explicit rationale that matches what the source actually says. Borderline calls (amsterdam-umc as "conservative-naive in the governance sense... non-governing showcase artifact"; UCSF as pioneer on operational-deployment grounds) are argued, not asserted.
- **Honesty rate: 29/30 (97%)** substantively faithful; quote-level fabrication rate 1/30 (~3%), confined to one non-substantive detail.
- **read_status integrity:** good. `full` claims pair with plausible word counts on long sources (AMEE 90k chars/12.5k words; AMA 86k/12.3k; attitudes study 69k/11.1k; AMA-CME 55k/8.2k; FSMB 32k/4.6k). The one note that could have overclaimed (mayo, 86k-char handbook) explicitly scopes its read to the AI cluster instead of claiming a full read — honest.

## Bottom line

**The deep-read layer is trustworthy enough to base the typology on.** ~460 individual quoted strings were checked; every substantive quote traces to the source. The single fabrication is a cosmetic [sic] detail in a note whose substance fully verifies, and the note's own read-scoping is honest. The typology-driving classifications (pioneer / conservative-naive) are all justified by verifiable source content.

Methodological caveat for downstream runs: naive verbatim-grep of quotes produces ~4× false-positive "fabrication" flags on this corpus because the notes (a) stitch elisions without ellipses, (b) normalize smart quotes/OCR artifacts, and (c) paraphrase in summary-format notes. Any future verification must adjudicate flags manually, as done here.
