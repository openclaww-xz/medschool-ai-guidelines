# Summary statistics — US med-school / health-system AI guidelines

All numbers produced in R (tidyverse) from `analysis/clauses.csv` (161 rows ×
13 cols, `utils::read.csv`); blank cells counted as absent. Regenerate with
`Rscript -e 'rmarkdown::render("figures.Rmd")'`. Figures: `figs/*.png`,
Rmd: `figures.Rmd`.

## Corpus

```r
clauses <- utils::read.csv("clauses.csv", stringsAsFactors = FALSE)
n_docs  <- nrow(clauses)                       # 161
n_orgs  <- dplyr::n_distinct(clauses$org)      # 136
```

- **161 documents** from **136 organizations**.
- Document type: guidance 113 (70.2%), formal policy 37 (23.0%),
  handbook section 6 (3.7%), curricular 5 (3.1%).

```r
clauses %>% count(doc_type, sort = TRUE)
```

## Sector split (UME vs health system)

Sector derived from `applies_to` (and `doc_type == "curricular"` → UME);
blank `applies_to` → unclassified (excluded from split figures):

```r
clauses <- clauses %>% mutate(sector = case_when(
  str_detect(applies_to, regex("clinician|resident|fellow|VUMC|health-system|CME",
                               ignore_case = TRUE)) &
    !str_detect(applies_to, regex("student|faculty|trainee|PA |instructor",
                                  ignore_case = TRUE)) ~ "HS",
  str_detect(applies_to, regex("student|trainee|learner|curriculum",
                               ignore_case = TRUE)) |
    doc_type == "curricular" ~ "UME",
  trimws(applies_to) != "" ~ "Mixed",
  TRUE ~ NA_character_))
clauses %>% count(sector)
# UME 119 · HS 26 · Mixed 8 · NA 8
```

## Adoption timeline (Figure 1)

Only 52 of 161 documents (32.3%) carry a parseable effective date
(first 4-digit year token, 2020–2026 kept); 109 blank.

```r
clauses %>% filter(!is.na(year)) %>% count(year, doc_group)
# 2023: 7 · 2024: 11 · 2025: 13 · 2026: 21  (monotonic growth)
# dated formal-policy/handbook docs: 27 · dated guidance/curricular: 25
```

## Clause prevalence (blank = absent)

```r
clauses %>% summarise(across(c(banned_uses, permitted_uses, phi_rule,
  disclosure_rule, assessment_rule, secure_tools_named, enforcement),
  ~ sum(trimws(as.character(.x)) != "")))
```

| Clause | n / 161 | % |
|---|---|---|
| permitted_uses | 111 | 69.0% |
| secure_tools_named | 89 | 55.3% |
| phi_rule | 87 | 54.0% |
| banned_uses | 87 | 54.0% |
| disclosure_rule | 80 | 49.7% |
| enforcement | 60 | 37.3% |
| assessment_rule | 38 | 23.6% |
| aamc_alignment = yes | **1** | **0.6%** |

## UME vs health system (Figure 5)

```r
clauses %>% group_by(sector) %>%
  summarise(N = n(),
            phi  = sum(trimws(as.character(phi_rule)) != ""),
            disc = sum(trimws(as.character(disclosure_rule)) != ""),
            enf  = sum(trimws(as.character(enforcement)) != ""),
            ass  = sum(trimws(as.character(assessment_rule)) != ""),
            aamc = sum(str_detect(tolower(aamc_alignment), "^yes")),
            .groups = "drop")
```

| Sector | N | PHI | Disclosure | Enforcement | Assessment | AAMC yes |
|---|---|---|---|---|---|---|
| UME (learners) | 119 | 71 (59.7%) | 69 (58.0%) | 51 (42.9%) | 34 (28.6%) | 1 |
| Health system / GME-clinical | 26 | 9 (34.6%) | 9 (34.6%) | 6 (23.1%) | 2 (7.7%) | 0 |

UME documents specify governance clauses at roughly 1.5–3× the rate of
health-system documents. Exactly **1 of 161** documents (0.6%) aligns with the
AAMC AI principles.

## Banned-use themes (Figure 2; keyword match on `banned_uses`)

```r
themes <- c("PHI/patient data"        = "phi\\b|patient|hipaa|identifiable",
            "graded work/exams"       = "exam|graded|grade |assessment|quiz|proctored|assignment",
            "plagiarism/passing-off"  = "plagiar|one.s own|as own|original|misrepresent",
            "clinical documentation"  = "note|documentation|h&p|progress note|ehr",
            "unapproved/public tools" = "unapproved|non-approved|not approved|public tool|public or non",
            "confidential/institutional data" =
              "confidential|institutional data|university data|sensitive information|student records")
clauses %>% transmute(sector,
         across(names(themes), ~ str_detect(banned_uses,
                              regex(themes[[cur_column()]], ignore_case = TRUE))))
```

| Theme | Overall (/161) | UME (/119) | HS (/26) |
|---|---|---|---|
| PHI / patient data into AI | 29 (18.0%) | 26 | 3 |
| Graded work / exams | 26 (16.1%) | 26 | 0 |
| Confidential / institutional data | 25 (15.5%) | 24 | 1 |
| Unapproved / public tools | 17 (10.6%) | 16 | 0 |
| Clinical documentation | 12 (7.5%) | 12 | 0 |
| Plagiarism / passing off | 9 (5.6%) | 9 | 0 |

Academic-integrity bans are essentially a UME phenomenon; the HS corpus bans
almost nothing in academic terms.

## PHI language clusters (Figure 3; within the 87 docs with a phi_rule)

```r
clauses %>% filter(trimws(as.character(phi_rule)) != "") %>%
  summarise(hipaa  = sum(str_detect(phi_rule, regex("hipaa|phi", ignore_case = TRUE))),
            proh   = sum(str_detect(phi_rule, regex("never|not be (entered|input|exposed|used)|may not|prohibit|do not post|violation", ignore_case = TRUE))),
            carve  = sum(str_detect(phi_rule, regex("approved|enterprise|hipaa compliant|contract|sensitive data", ignore_case = TRUE))),
            baa    = sum(str_detect(phi_rule, regex("business associate|\\bbaa\\b", ignore_case = TRUE))),
            deid   = sum(str_detect(phi_rule, regex("de-?identif|sanitiz", ignore_case = TRUE))))
```

| Cluster | n (/161) | n (/87 with clause) |
|---|---|---|
| Any PHI clause | 87 (54.0%) | 87 (100%) |
| Mentions HIPAA/PHI | 41 (25.5%) | 47.1% |
| Prohibitive language | 19 (11.8%) | 21.8% |
| Approved/secure carve-out | 16 (9.9%) | 18.4% |
| De-identification language | 5 (3.1%) | 5.7% |
| BAA required | 4 (2.5%) | 4.6% |

## Named secure tools (Figure 4; keyword match on `secure_tools_named`)

```r
tools <- c(ChatGPT = "chatgpt|gpt-5|gpt-4|openai", Copilot = "copilot",
           Claude = "claude|anthropic", Gemini = "gemini", Grammarly = "grammarly",
           NotebookLM = "notebooklm", "Azure OpenAI" = "azure",
           "Zoom AI" = "zoom ai", Abridge = "abridge")
clauses %>% summarise(across(all_of(names(tools)),
  ~ sum(str_detect(secure_tools_named, regex(tools[[cur_column()]], ignore_case = TRUE)))))
```

| Tool | Docs naming it (/161) |
|---|---|
| ChatGPT / OpenAI | 53 (32.9%) |
| Microsoft Copilot | 34 (21.1%) |
| Claude / Anthropic | 19 (11.8%) |
| Gemini | 15 (9.3%) |
| Abridge | 5 (3.1%) |
| Azure OpenAI | 3 (1.9%) |
| Grammarly | 2 (1.2%) |
| Zoom AI | 2 (1.2%) |
| NotebookLM | 1 (0.6%) |

89 documents (55.3%) name at least one tool; OpenAI and Microsoft dominate.

## Headline findings

1. **Volume is guidance-heavy**: 70% of corpus is non-binding guidance; only
   23% formal policy.
2. **Dating is sparse but accelerating**: only 32% of docs state an effective
   date; among dated docs, counts rise monotonically 2023 (7) → 2026 (21).
3. **PHI and disclosure lead content**: PHI clauses (54%) and disclosure rules
   (49.7%) are the most common governance elements; enforcement (37%) and
   assessment rules (23.6%) lag.
4. **UME out-governs health systems** on every measured clause.
5. **AAMC principles almost never cited**: 1/161 documents.
6. **ChatGPT is the most-named tool** (33% of docs), ahead of Copilot (21%),
   Claude (12%), Gemini (9%).
