---
source_url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11444356/"
title: "Examining ChatGPT Performance on USMLE Sample Items and Implications for Assessment."
publisher: "Academic medicine : journal of the Association of American Medical Colleges"
published_date: "2023-11-07"
accessed_date: "2026-09-17"
license: "CC-BY-NC-ND (full text, open access via Europe PMC)"
sha256: ""
---

## Method

As the Kung8 and Gilson7 research groups did, we used the USMLE items available from the USMLE website in early 2023.14 This sample comprised 120 Step 1 items, 120 Step 2 CK items, and 137 Step 3 items. (Three items appeared in both the Step 2 CK and Step 3 sample item sets.) These sets of sample items are substantially smaller than operational USMLE test forms (Step 1 forms have approximately 280 items; Step 2, approximately 318 items; and Step 3, approximately 503 items). Moreover, operational forms are built to conform to a complex set of content and statistical specifications that (among other objectives) minimize differences in difficulty between forms. In contrast, the publicly available sample USMLE item sets are built to condensed versions of the content blueprint, with less rigorous control of overall difficulty. Consequently, while the Step 1 and Step 2 CK sample forms were generally comparable to the operational USMLE form difficulties, the Step 3 items were notably less difficult.

As Kung and colleagues8 noted, the sample items were made public in 2022, after ChatGPT 3.5 was trained, providing strong evidence that ChatGPT could not have “memorized” the answers during training. While ChatGPT accepts a wide range of special characters and symbols, approximately 14% of the sample items contain nontext features (e.g., images, graphs), which ChatGPT cannot interpret. Nevertheless, for completeness, we presented the text for every item to ChatGPT. We separately analyzed the accuracy for items that were entirely text based and items that originally included a nontext component. A new session was initiated for each item. We collected the responses from ChatGPT 3.5 between February 20, 2023, and March 19, 2023.

### Replications

Consistent with the approach used in previous studies, we presented each item to ChatGPT verbatim as it would be presented to examinees, including presenting each option on a separate line and without providing additional instructions. We repeated this process 3 times for each item (replications) to evaluate the intra-item consistency of the responses.

### Scoring ChatGPT responses

Each of the 3 responses to each item was then independently scored by 2 raters using a rubric specifying that a response was to be scored as correct only if ChatGPT identified the keyed answer as the only correct response. We scored all other variations of responses as incorrect, including occasions when an incorrect option was indicated, no answer was indicated, an answer was indicated that was not among the options, or more than one option was indicated as correct. This ensured that the scoring matched operational practice, where, for example, selecting 2 options is not permitted. Scoring disagreements between the 2 raters were reviewed by the first author (V.Y.) who made the final scoring decision.

In addition to evaluating the overall performance for ChatGPT, we conducted preliminary analyses to identify the characteristics of items that ChatGPT answered correctly. Because all items had, at one time, appeared on actual USMLE tests, we first compared ChatGPT’s performance with the proportion of correct responses (P values) calculated using examinee responses to these items from first-time examinees from Liaison Committee on Medical Education (LCME) accredited medical schools. This was accomplished by examining the correlations between these P values and the 0/1 (incorrect/correct) scores from ChatGPT to determine the extent to which items that were more difficult for examinees were also more difficult for ChatGPT. We also considered the variability of ChatGPT’s performance across one of the major USMLE content coding schemes, physician task competency, which is a framework for assigning each item to a distinct physician competency such as foundational science or diagnosis.15 To evaluate the statistical significance of differences of performance across content, we tested each content area separately using a permutation test (100,000 permutations, 2-tailed). A Holm–Bonferroni correction was made for multiple comparisons to reduce Type 1 error. A permutation test is a form of proof by contradiction: the proposition that ChatGPT’s success is affected by the task membership of an item is first assumed to be false, and then, if a contradiction arises (in this case, an observed difference that would be highly unlikely were the proposition false), this is interpreted as evidence that the proposition is true. In other words, if a highly unlikely difference is observed, this is evidence that ChatGPT performs differently on this content.

## Results

Table 1 presents the percentage of items answered correctly by ChatGPT on the sample material for each of the 3 Steps’ sample item sets across the 3 separate replications. Results are provided separately for the full sample of items, the items with text only, and the items with a nontext component.

| Examination | No. of items | Replication 1 | Replication 2 | Replication 3 |
|---|---|---|---|---|---|
| Complete sample | 377 |  |  |  |
| Step 1 | 120 | 60.83 | 64.17 | 64.17 |
| Step 2 CK | 120 | 70.83 | 67.50 | 71.67 |
| Step 3 | 137 | 59.12 | 58.39 | 63.50 |
| Text-only items | 325 |  |  |  |
| Step 1 | 93 | 66.67 | 69.89 | 67.74 |
| Step 2 CK | 108 | 70.37 | 67.59 | 72.22 |
| Step 3 | 124 | 60.48 | 59.68 | 65.32 |
| Items with nontext component | 52 |  |  |  |
| Step 1 | 27 | 40.74 | 44.44 | 51.85 |
| Step 2 CK | 12 | 75.00 | 66.67 | 66.67 |
| Step 3 | 13 | 46.15 | 46.15 | 46.15 |

Based on the full sample of items, ChatGPT scored above 60% correct in all cases except for one Step 3 replication, with a higher percentage of correct responses for text-only items.

Variability in the percentage of correct responses across the 3 replications is also shown in Table 1. An example of this variation is reported in Chart 1, which shows both a correct and incorrect response that ChatGPT produced for a single item. Such inconsistencies were observed for 76 (20%) of the 377 sample items (26 items for Step 1, 23 for Step 2 CK, and 27 for Step 3).

The relationship between item difficulty (measured by P values based on examinee responses collected when these items were used on operational Step examinations) and the responses from ChatGPT showed a modest correspondence, at best. The mean correlation across the 3 replications was 0.22 for Step 1, 0.23 for Step 2 CK, and 0.03 for Step 3 based on the full item sample. These correlations are similar for the text-only items (0.15, 0.20, and 0.07, respectively). Although some of the correlations for individual replications were significant (P &lt; .05), none suggested a strong relationship.

Table 2 presents the proportion of items answered correctly by ChatGPT within each physician task competency assessed on the sample material. The observed difference between performance within and outside each task is also reported, along with the probability that each difference (or greater) would arise due to chance were the true difference zero. ChatGPT performed significantly worse (P &lt; .001) on items relating to practice-based learning (which cover the topics of biostatistics, epidemiology, research ethics, and regulatory issues) than it did on other items. Items belonging to different content areas were not necessarily equally difficult; the data reported in Table 2 do not account for this possibility.

|  |  | No. of items | Proportion correct |  |  |
|---|---|---|---|---|---|---|
| Item type | Physician task | Within this physician task | Not within this physician task | Within this physician task | Not within this physician task | Difference in proportion correct | Probability of observed differenceb |
| Includes items with nontext elements (n = 377) | Communicationc | 32 | 345 | .76 | .63 | .13 | .06 |
| Foundational science | 89 | 288 | .58 | .66 | −.08 | .06 |
| Diagnosis | 125 | 252 | .69 | .62 | .08 | .06 |
| Management | 106 | 271 | .68 | .63 | .05 | .18 |
| Practice-based learning | 25 | 352 | .32 | .67 | −.35 | &lt; .001 |
| Excludes items with nontext elements (n = 325) | Communicationc | 31 | 294 | .75 | .65 | .10 | .12 |
| Foundational science | 68 | 257 | .65 | .67 | −.02 | .36 |
| Diagnosis | 107 | 218 | .70 | .64 | .06 | .12 |
| Management | 95 | 230 | .68 | .66 | .03 | .28 |
| Practice-based learning | 24 | 301 | .33 | .69 | −.36 | &lt; .001 |

## Discussion

Although it is impossible to make a precise and definitive statement about “passing” based on our findings (see Table 1), taken on average across replications, ChatGPT’s performance appears consistent with “passing” for Step 1 and Step 2 CK. Given that the items in the Step 3 sample were easier to answer correctly than those on a typical Step 3 test form, ChatGPT’s performance on the Step 3 sample item set would likely translate to a score below 60% correct on the operational exam for at least 2 of the 3 replications. Moreover, an operational Step 3 exam contains an interactive computer-based simulation component that contributes to the overall score, which we did not assess in this study. Note that while these findings are generally consistent with those presented in earlier publications,7,8 they reflect uniformly higher performance for ChatGPT on the text-only items than was reported by Kung and colleagues8 or Gilson and colleagues.7

The data reported in Table 1 are noteworthy in that they include ChatGPT’s performance on all items in the sample set, including those that contained nontext elements. Perhaps not surprisingly, performance was lower on these items because ChatGPT can only interpret text. Nevertheless, ChatGPT’s performance on items that originally included a nontext component far exceeded what would be expected by chance alone.

ChatGPT performed near or above the level associated with passing on the multiple-choice component for Steps 1 and 2 CK. Inferences for passing Step 3 are limited, both because the exam contains a simulation component unassessed in this study and because of the comparative easiness of the sample items noted earlier. That said, it is worth emphasizing that ChatGPT performed well below a typical USMLE examinee. In contrast, average scores for first-time examinees from LCME-accredited schools are approximately 2 standard deviations above the passing standard.16 Moreover, although AI systems will certainly improve over time, there is an important distinction between performing well on these multiple-choice questions and being licensed to practice medicine. In addition to passing the USMLE sequence, a physician must successfully complete medical school and residency, which requires demonstrating a range of competencies not assessed by USMLE test material but critical to the provision of safe and effective patient care.

Because much of the attention given to ChatGPT has focused on performance relative to the USMLE passing standards, it is useful to consider the limitations of such interpretations. Answering 60% of items correctly is an approximation of the passing standard. Additionally, multiple forms of any Step examination can only be compared to a common cut score because they have been built to the same statistical and content specifications and have been statistically adjusted (equated) to place scores from different forms on the same scale.17 As noted, the publicly available study items were assembled with less rigorous constraints, introducing differences in content representation and difficulty compared to an operational test form. As such, any comparisons made based on publicly available USMLE items will be approximate and, as appears to be the case for Step 3, may be an imprecise approximation. This limitation is a particularly important consideration when interpreting results based solely on text-based items. Materials representing evidence-based medicine, biostatistics, radiology, dermatology, and cardiology, which typically incorporate a higher proportion of nontext elements, will likely be underrepresented when items with nontext components are excluded.

Our findings also raise questions in several areas related to medical education and assessment. Others have suggested that AI will have an important role in these areas going forward2,3—which seems like a safe prediction. At present, however, there are limitations to the usefulness of ChatGPT for medical students. ChatGPT appears equally confident whether or not its answer is correct. Promoting the use of these tools as learning aides for medical students should be avoided without first emphasizing the need for expert review of the output. Whether AI systems can be useful aids to experts writing response rationales remains an open question that needs empirical investigation. For the time being, learning and assessment will be better supported by materials that have been more rigorously vetted.

Another issue worth examining is what these findings suggest about the cognitive processes required for examinees to respond to USMLE items. Although ChatGPT claims that it “is not capable of reasoning in the same way that humans do,” as per its own response, many of its responses closely resemble human responses, despite being generated probabilistically based on word cooccurrences in a large corpus of human-generated text—raising the question of whether this form of probabilistic prediction is (or should be) included in a definition of “clinical reasoning.” Yet such a question presupposes overlap between ChatGPT’s response processes and examinees’ response processes, which has not been demonstrated.

In a survey overview of automated question-answering systems, Rogers and colleagues18 write, “It is increasingly clear that humans and machines do not necessarily find the same things difficult, which complicates direct comparisons of their performance.” This view is consistent with the modest, and frequently nonsignificant, correlations we observed between the difficulty of items for examinees and the performance of ChatGPT on those items.

The question of the cognitive processes required to answer these questions is also brought into focus when we consider the items with images and other nontext components. Previous researchers have removed these items from their study sample—presumably under the assumption that ChatGPT would be unable to respond. This is clearly not the case, however, as we found that ChatGPT provided detailed descriptions of “imagined” graphs in its responses to items with nontext components, even though no graphs were included in the input. Without additional study in this area, it is not possible to disentangle whether ChatGPT was able to answer these questions because the image is not required to arrive at the correct answer, or because it was able to draw parallels between the text and image descriptions from its training data. An interesting avenue for future research would be to investigate whether examinees would be as successful in answering these items without access to the nontext component.

What, then, are the implications of AI systems successfully answering test items? It seems clear that recent advances represent a trend that is likely to continue. Although this general trend has substantial significance for the performance of the model itself (mainly related to how useful it may be for other tasks from that domain), the implications are more modest regarding education and assessment. If improved large language models were to answer more items correctly, educators and patients would still want physicians to be familiar with foundational concepts in medicine and able to use that knowledge to build advanced skills and experience. That said, if the question is whether we should embrace innovations with AI that physicians can use to improve the quality of care, our answer is a most enthusiastic yes. Any prediction of how this may happen is premature at this stage, but it is safe to assume that as the use of AI in medical practice continues to grow, its reach will extend to how we assess medical knowledge and skills.

In conclusion, it seems appropriate that we comment on how advances in AI will impact the responsibility that assessment organizations and examinees have to the public. Medical licensing examinations are explicitly intended to protect the health of the public. Both the form and content of these tests are intended to support inferences about specific proficiencies required for the safe and effective practice of medicine.19 When new technologies change the way medicine is practiced or the way medical students learn, testing organizations must reevaluate the alignment between the form and content of their tests and the function of those tests in protecting the public. This reevaluation is an essential and ongoing part of a testing organization’s responsibility to evaluate the validity of the inferences and uses that are made based on the test scores they produce. Studies such as this represent a first step in that process of reevaluation.

## Funding/Support

All work on the research and manuscript was completed while the authors were employees of the National Board of Medical Examiners.

## Other disclosures

None reported.

## Ethical approval

This research has been determined by the American Institutes of Research as not meeting the federal definition of research with human subjects and is therefore exempt from IRB review and oversight (Project No. EX00398).

## Previous presentations

Annual meeting of the National Council on Measurement in Education, April 14, 2023, Chicago, IL.

## Data sharing

All data are from the National Board of Medical Examiners, which approved its use prior to the manuscript’s submission.

## Footnotes

## Contributor Information

Peter Baldwin, Email: pbaldwin@nbme.org.

Daniel P. Jurich, Email: djurich@nbme.org.

Kimberly Swygert, Email: kswygert@nbme.org.

Brian E. Clauser, Email: bclauser@nbme.org.

## References


