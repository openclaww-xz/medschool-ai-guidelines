---
source_url: "https://www.ama-assn.org/system/files/ai-educator-guide.pdf"
title: "The Medical Educator's Guide to Projects Leveraging Artificial Intelligence and Learning Analytics"
publisher: "American Medical Association"
published_date: "2025-03"
accessed_date: "2026-09-17"
license: "public web page"
sha256: ""
---

Kimberly D. Lomis, MD
   The Medical Educator’s Guide to Projects Leveraging
       Artificial Intelligence and Learning Analytics

Introduction
Medical educators are enthused about the potential to leverage artiﬁcial intelligence,
learning analytics, and other emerging technologies to improve medical training and
promote precision education across the continuum of medical school, residency, and
practice. However, many educators lack experience in developing and deploying such
technologies. Collaborations with technical experts (in-house and/or commercial vendors)
will be needed.

This guide outlines the core issues to consider when designing technological solutions. The
contents may seem daunting to medical educators not trained in analytics and AI,
particularly since capabilities in this space continue to evolve rapidly. This is why it is
critical to assemble multi-disciplinary teams of people who bring complementary areas of
expertise to such projects to ensure responsible development and deployment. This guide
provides educators an overview of key points for discussion with their potential technical
partners, facilitating essential details in planning and implementation that give projects the
greatest chance at success.




Suggested citation: Lomis KD. The Medical Educator’s Guide to Projects Leveraging
Artiﬁcial Intelligence and Learning Analytics. American Medical Association. Published
March 2025.




© 2025 American Medical Association. All Rights Reserved.                          Page 1 of 9
1. Problem Deﬁnition
 What problem are you trying to solve?
 What meaningful action will result from the proposed intervention?
Educators are trained in backward design: ﬁrst determining desired learning outcomes,
then identifying the appropriate experiences and assessments needed to support those
outcomes. A similar approach is needed in developing a technical solution to educational
needs, but an intriguing technological advance can lure teams to instead seek a place to
apply the “shiny thing,” especially when approached by vendors with a solution to sell.

Clearly articulating what burden is to be relieved or what advancement is desired is critical
to maintaining focus while broadening the range of potential solutions. Gathering input
from stakeholders (learners, supervisors, patients) and engaging them in co-production
will clarify how the envisioned initiative could make a meaningful impact upon the
experience of those involved.


2. Affordances of Technology
 What assumptions do we have about how to approach this problem?
 What speciﬁc technological capabilities could help?




                   Examples of speciﬁc capabilities of artiﬁcial intelligence


© 2025 American Medical Association. All Rights Reserved.                         Page 2 of 9
We often hold preconceived notions about how to approach a given challenge. A common
pitfall is to reproduce old models in new digital formats. While such an approach may offer
convenience or efficiency, it is limiting. Emerging technologies should drive us to think
entirely differently about a given task; educators may need to confer with those from other
disciplines to fully appreciate possible solutions. Recent advances enable us to increase
the volume and types of data we can capture, scale our capacity to process data, and offer
new ways to synthesize data to inform meaningful actions.

At the same time, due to a lack of training in AI and data science, educators are at risk of
envisioning AI as a magic wand that makes everything possible. We often lack knowledge
to be speciﬁc regarding the capabilities that would be most useful for a given task. Because
the ﬁeld of AI is evolving so rapidly, capabilities are constantly changing. Active dialogue
with technical experts, as well as engaging learners or other stakeholders in co-production,
should avoid premature closure and can generate multiple possible solutions to the
deﬁned problem.


3. Data Considerations
 What data is/could be available to address this problem?
 How will data be managed?
For learners and supervisors to embrace data-driven technological interventions to
improve education, educators must take deliberate action to promote trust in the quality,
application, and protection of the data being used. Educators should ask about data
provenance, measurement, and quality issues relevant to the use of a particular data
source.

What data is available?
Solutions leveraging analytics and artiﬁcial intelligence rely upon rich data sets for training.
Teams should consider what the data relevant to the desired outcome is, or could be,
available. If one can anticipate meaningful patterns within a data set, AI could be a
powerful tool.

What features within the data set are of interest?
Teams can predetermine speciﬁc data elements (referred to as features) of interest to be
included in a tech solution. Are those features in structured data ﬁelds, or will it be
necessary to create a process to extract them (such as natural language processing, NLP)?
Monitoring the performance of an algorithm may reveal a need to change features or alter
the weighting of features to ﬁne-tune the tool. An advantage of applying AI to large data
sets is the potential to identify unanticipated patterns. AI may reveal alternative features
that impact outcomes. This capability could be particularly valuable in educational
research to identify previously unrecognized factors associated with performance.



© 2025 American Medical Association. All Rights Reserved.                            Page 3 of 9
Is the data annotated?
When using a data set to train a model, we need to provide guidance regarding the
outcome of interest to which features will be correlated. As a clinical example, if training an
algorithm to review images of pathologic specimens to predict risk of cancer, the training
data would include examples labelled as normal or abnormal. In education, we would
similarly need to label data samples as correct/incorrect or some other dimension
appropriate to the outcome of interest. Experts can be engaged to annotate sufficient
samples, although this can be resource intensive. Developers also consider whether other
existing features in the data set would represent the “answer.” For example, if we seek to
assess a learner’s clinical appraisal of a patient from their clinical note in the EHR, the ICD
and CPT codes registered by the physician of record for a given patient could be considered
the “correct” answer to which the learner’s work is compared.

Is the data representative of the population targeted for intervention?
Education teams must consider the alignment between the data that is available for
development of a tool and the target population for deployment. For example, training an
algorithm against expert performance may not provide nuanced understanding of
appropriate novice performance among early learners. Technological solutions are not
inherently biased, but the data sets on which they are trained — or the way that
development teams identify features of interest — commonly have inherent bias that could
be ampliﬁed by an application.

Is the data accessible to the education team?
Educational teams must consider access to sufficient data not only for initial training of an
algorithm, but also for monitoring and continued reﬁnement. If data is not directly
accessible, what relationships should be pursued? Health systems commonly have
dedicated units managing clinical data. Educators can connect with health system
leadership roles such as chief medical informatics officers (CMIOs) or quality officers to
explore possibilities for integration of educational applications with existing clinical data
systems. Educators may underestimate the challenge of such integration. Application
programming interfaces (APIs) facilitate this process, but teams should account for this
process in project timelines and budgets. Potential federated structures that allow for
training on data sets across institutions without sharing sensitive data can also be
explored.

How will data be protected?
Educational applications could involve protected health information, learner data
protected under FERPA, and data about supervisors and practicing health professionals.
Such data is appropriate to use for educational purposes but must be protected. Educators
must exercise caution that sensitive data is not exposed through integration of systems.
The concept of an education data warehouse can be applied at the institutional level to
support learning analytics or across institutions to support educational research.


© 2025 American Medical Association. All Rights Reserved.                          Page 4 of 9
Educators have a duty to ensure data will be managed appropriately and should ask
technical colleagues or vendors how this issue will be addressed prior to pursuing each
project.


4. Limitations of Technology
 What limitations of the technology will impact this speciﬁc project?
Educators may lack sufficient training to recognize potential risks or failures of a proposed
technological solution. Educators should ask collaborators for explanations of these
issues and work to create appropriate safeguards.

Common pitfalls include:

   •   Bias in data sets used for training and validation or bias in the process of data
       preparation
   •   Potential inequities in access to tools, application of tools, and outcomes
       associated with tools
   •   Technical issues, such as
          o non-stationarity of data

                  Non-stationarity is a term that reﬂects the inconsistency in how health
                  care and educational data may be recorded over time or in one setting
                  versus another, impacting the performance of a model.

          o confounding inputs or label leakage

                  When training an algorithm, if the labels of interest (e.g., correct/incorrect
                  or normal/abnormal) inadvertently contaminate the data set such that
                  the algorithm can “see” the answer, a model may appear to perform
                  better than it actually does. One example of such label leakage was seen
                  in a study of a tool to predict severity of illness by analyzing chest X-rays.
                  The algorithm came to recognize that ﬁlms taken in the supine rather than
                  upright position indicated increased severity of illness. Once the
                  algorithm indexed on that singular feature, it was not adding any new
                  insights.

          o overtraining

                  Overtraining refers to providing too much oversight during model
                  development, resulting in lack of external validity when handling data
                  beyond the training set.




© 2025 American Medical Association. All Rights Reserved.                           Page 5 of 9
   •   User error
          o Well-intentioned actors may misuse the technology or misapply its outputs
              due to a lack of training.
          o Malicious actors may deliberately tamper with a system to alter outputs.

An activity referred to as “red teaming,” in which stakeholders actively try to “break” the
application, can be useful to anticipate pitfalls.


5. Costs
Educators may not understand the resources needed to develop and deploy such
technological solutions. Input from experts will help to plan appropriate budgets for
projects. Most projects to support precision education will require collaboration across
units or departments that may not have existing relationships (for example, a medical
education unit collaborating with a clinical informatics team). Establishing in advance
which teams will provide each resource to a project will strengthen budgetary planning.

When negotiating with a vendor, educators should push for clarity around their business
model to understand both immediate and long-term costs. They should also address
whether the vendor will capture institutional data that could be used for other purposes.

Costs to consider include, but are not limited to

   •   Computing power/cloud services
   •   Programmer services
   •   Data management
   •   Subject matter experts for data annotation
   •   Statistical analysis
   •   Subscription and licensing fees, such as for large language models (LLMs)
   •   Integration costs (APIs) and IT effort
   •   Hardware (especially for AR/VR, augmented reality or virtual reality applications)
   •   Legal fees for contracts and data agreements
   •   Evaluation costs associated with continuous monitoring


6. Implementation Science
 What change management strategies will be necessary for deployment?
 What is the context in which data is generated and in which the proposed tool would be
  used?
Trust must be earned. It is important to consider the human-AI collaboration needed for an
intervention to be successful. Teams should explore and specify the relationship and
workﬂow between the educator, the learner, and the technology. The human-in-the-loop


© 2025 American Medical Association. All Rights Reserved.                           Page 6 of 9
concept requires that educational leaders deploying novel technologies embrace
accountability and actively engage in monitoring tool performance over time. Learners
interacting with new tools should be recruited to assist in co-production and monitoring of
altered educational workﬂows as well as new technologies. To avoid the perception of a
surveillance state, educators should ensure that data is used to beneﬁt stakeholders.
Educational teams should be transparent about the purpose of each technological
solution, and leaders must demonstrate awareness of potential limitations.

Data-driven solutions are particularly vulnerable to context. Variations in workﬂows and
stakeholder incentives impact the feasibility and accuracy of implementation. This is
important when considering whether to buy an existing tool versus building a custom
solution. If considering an existing product, educators should clarify whether the context
for which the tool was originally developed algins with their intended use case.

Interpretability and explainability are common challenges of AI solutions. Developers,
especially commercial vendors, may be hesitant to share proprietary intellectual property,
but educators should press for an understanding of how predictions or recommendations
are formulated. Increasingly, AI solutions are proactively designed to provide more insight
into their own processes.


7. Responsible Deployment
 Do all involved have adequate training for optimal use of the technology?
 Has the organization put appropriate structures in place for deployment and ongoing
  monitoring?



                                                                      Snapshot from the AMA
                                                                       guide Advancing AI in
                                                                        Medical Education
                                                                     through Ethics, Evidence
                                                                            and Equity




© 2025 American Medical Association. All Rights Reserved.                        Page 7 of 9
Educators pursuing technological solutions have a duty beyond the development phase to
ensure responsible deployment and ongoing monitoring. Stakeholders interacting with a
given tool must understand enough about how the technology works to recognize
problems. Users should be recruited to aid in continuous monitoring and reﬁnement of
tools. Resources must be devoted to upskilling all involved.

Institutional structures should include an organizational committee that articulates guiding
principles. Multiple frameworks are arising from various leadership organizations. Local
teams should review, clarify, and publicize their institutional process. Resources must be
put in place to support ongoing evaluation of the performance of these tools. Institutional
assets, such as safe AI playgrounds or enterprise-sanctioned generative pre-trained
transformers (GPTs), can support experimentation while protecting intellectual property,
health information, and learner data. Training, to include foundational knowledge coupled
with active application experiences such as prompt-a-thons and red-teaming exercises, is
essential for all involved in the use of these tools.


Conclusion
Educational projects leveraging artiﬁcial intelligence and learning analytics demand a
multi-disciplinary strategy, bridging educational and technical expertise. Although the
speciﬁc capabilities of these technologies are rapidly evolving, educators can apply this
framework to address key considerations with team members embarking on any
technology-enabled project. A deliberate and informed approach — addressing problem
deﬁnition, affordances of technology, data considerations, limitations of technologies,
costs, implementation science, and responsible deployment — will position educators to
deploy such tools responsibly, to the optimal beneﬁt of learners at all levels and the
patients they serve.


Useful resources
Lomis KP, Jeffries A, Palatta M, Sage J, Sheikh C, Sheperis, Whelan A. 2021. Artiﬁcial
Intelligence for Health Professions Educators. NAM Perspectives. Discussion Paper,
National Academy of Medicine, Washington, DC.

Russell RG, Lovett Novak L, Patel M, Garvey KV, Craig KJT, Jackson GP, Moore D, Miller BM.
Competencies for the Use of Artiﬁcial Intelligence-Based Tools by Health Care
Professionals. Acad Med. 2023 Mar 1;98(3):348-356

American Medical Association. Artiﬁcial Intelligence Learning Series (online modules).

American Medical Association. StepsForward Innovation Academy: Navigating AI in Health
Care.



© 2025 American Medical Association. All Rights Reserved.                         Page 8 of 9
Gordon M, Daniel M, Ajiboye A, et al. A scoping review of artiﬁcial intelligence in medical
education: BEME Guide No. 84. Med Teach. 2024 Apr;46(4):446-470

Lomis KD. Precision education: investing in informatics and emerging technologies to bring
competency-based education to fruition. International Clinician Educators Blog. February
6, 2025.

Desai SV, Burk-Rafel J, et al. Precision education: The future of lifelong learning in
medicine. Acad Med. 2024;99(4S Suppl 1):S14-S20.

American Medical Association. Advancing AI in medical education through ethics,
evidence and equity. Published September 21, 2023.

Association of American Medical Colleges. Principles for the Responsible Use of Artiﬁcial
Intelligence in and for Medical Education.




© 2025 American Medical Association. All Rights Reserved.                            Page 9 of 9
