---
source_file: raw/peer-reviewed/chatgpt-llm-medical-licensing-exams-worldwide-systematic-review.md
read_status: full
approx_words_read: 5641
---

# LLM Performance on Medical Licensing Exams Worldwide: Systematic Review + Network Meta-Analysis (Cureus, 2025)

## Research question
What is the pooled accuracy of LLMs across national medical licensing exams, and how do model version, exam language, and exam system moderate performance?

## Methods
PRISMA systematic review (PubMed/WoS/IEEE, 2021–Jun 2025); QUADAS-2 adapted; random-effects meta-analysis, network meta-analysis (P-scores), mixed-effects meta-regressions (language; exam system), leave-one-out sensitivity; R (metafor/netmeta).

## Sample
41 studies, 120 evaluations, 10 exam systems (USMLE, CNMLE, JMLE, GMLE, PMLE, etc.) in 9 languages; 16 model variants from GPT-3.5 through GPT-o1/DeepSeek-R1.

## Key findings (with counts)
- Pooled accuracy: GPT-o1 95.4%, DeepSeek-R1 92.0%, GPT-4o 89.4%, GPT-4 82.7% (k=45, most-connected node), GPT-3.5 56.3%, LLaMA-13B 44.1%.
- 13/16 models exceed a 60% passing benchmark; only GPT-3.5, GPT-3.5-Turbo, LLaMA-13B fail.
- NMA vs GPT-4: GPT-o1 +12.8%, DeepSeek-R1 +10.7%, GPT-4o +6.7%; GPT-3.5 −22.6%, Bard −23.5%, LLaMA-13B −39.3%.
- Language effects (adj.): Chinese −7.97pp, Japanese −7.20pp, German +6.71pp vs English. Exam effects: CNMLE/JMLE/IMLE lower, PMLE/GMLE higher than USMLE.
- Moderators explained ~87–89% of heterogeneity (I² residual ~88%); leave-one-out stable (73.69–74.21%).
- Risk of bias: no study high-risk; 100% low risk on prompting/consistency domains.

## What it says about WHO leads policy
Implicit for licensing bodies: knowledge-based MCQ licensing exams no longer discriminate between AI and passing humans for current models — assessment validity re-evaluation is now non-optional everywhere, not just USMLE (ties to NBME's own statement). Recommends the question shift "from whether to how."

## Limitations
High residual heterogeneity; small subgroups; some exams translated to English pre-testing; accuracy ≠ safety/consistency; MCQ-only.

## Corroboration/contradiction with our corpus
Quantifies the trajectory our corpus's assessment policies respond to: the 2023 NBME baseline (ChatGPT ~60%) is now GPT-o1 at 95%. Corroborates our school-policy corpus's near-universal assessment restrictions as the rational response. Language-effect finding (Chinese/Japanese penalty) adds an equity dimension absent from US policy texts we hold.
