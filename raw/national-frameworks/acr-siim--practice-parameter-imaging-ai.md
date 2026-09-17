---
source_url: "https://gravitas.acr.org/PPTS/DownloadPreviewDocument?DocId=217"
title: "ACR-SIIM Practice Parameter for Imaging Artificial Intelligence (AI)"
publisher: "American College of Radiology / SIIM"
published_date: "2026-05"
accessed_date: "2026-09-17"
license: "public web page"
sha256: ""
---

ACR–SIIM PRACTICE PARAMETER FOR IMAGING
ARTIFICIAL INTELLIGENCE (AI)
The American College of Radiology, with more than 40,000 members, is the principal organization of radiologists, radiation oncologists, and clinical medical
physicists in the United States. The College is a nonprofit professional society whose primary purposes are to advance the science of radiology, improve
radiologic services to the patient, study the socioeconomic aspects of the practice of radiology, and encourage continuing education for radiologists, radiation
oncologists, medical physicists, and persons practicing in allied professional fields.
The American College of Radiology will periodically define new practice parameters and technical standards for radiologic practice to help advance the science
of radiology and to improve the quality of service to patients throughout the United States. Existing practice parameters and technical standards will be
reviewed for revision or renewal, as appropriate, on their fifth anniversary or sooner, if indicated.
Each practice parameter and technical standard, representing a policy statement by the College, has undergone a thorough consensus process in which it has
been subjected to extensive review and approval. The practice parameters and technical standards recognize that the safe and effective use of diagnostic and
therapeutic radiology requires specific training, skills, and techniques, as described in each document. Reproduction or modification of the published practice
parameter and technical standard by those entities not providing these services is not authorized.

PREAMBLE
This document is an educational tool designed to assist practitioners in providing appropriate radiologic care for
patients. Practice Parameters and Technical Standards are not inflexible rules or requirements of practice and are
not intended, nor should they be used, to establish a legal standard of care1. For these reasons and those set
forth below, the American College of Radiology and our collaborating medical specialty societies caution against
the use of these documents in litigation in which the clinical decisions of a practitioner are called into question.
The ultimate judgment regarding the propriety of any specific procedure or course of action must be made by
the practitioner considering all the circumstances presented. Thus, an approach that differs from the guidance in
this document, standing alone, does not necessarily imply that the approach was below the standard of care. To
the contrary, a conscientious practitioner may responsibly adopt a course of action different from that set forth
in this document when, in the reasonable judgment of the practitioner, such course of action is indicated by
variables such as the condition of the patient, limitations of available resources, or advances in knowledge or
technology after publication of this document. However, a practitioner who employs an approach substantially
different from the guidance in this document may consider documenting in the patient record information
sufficient to explain the approach taken.
The practice of medicine involves the science, and the art of dealing with the prevention, diagnosis, alleviation,
and treatment of disease. The variety and complexity of human conditions make it impossible to always reach
the most appropriate diagnosis or to predict with certainty a particular response to treatment. Therefore, it
should be recognized that adherence to the guidance in this document will not assure an accurate diagnosis or a
successful outcome. All that should be expected is that the practitioner will follow a reasonable course of action
based on current knowledge, available resources, and the needs of the patient to deliver effective and safe
medical care. The purpose of this document is to assist practitioners in achieving this objective.
_________________________________________________________________________________________________
1 Iowa Medical Society and Iowa Society of Anesthesiologists v. Iowa Board of Nursing, 831 N.W.2d 826 (Iowa 2013) Iowa Supreme Court refuses to find that
the "ACR Technical Standard for Management of the Use of Radiation in Fluoroscopic Procedures (Revised 2008)" sets a national standard for who may perform
fluoroscopic procedures in light of the standard’s stated purpose that ACR standards are educational tools and not intended to establish a legal standard of
care. See also, Stanley v. McCarver, 63 P.3d 1076 (Ariz. App. 2003) where in a concurring opinion the Court stated that “published standards or guidelines of
specialty medical organizations are useful in determining the duty owed or the standard of care applicable in a given situation” even though ACR standards
themselves do not establish the standard of care.

I. INTRODUCTION AND SCOPE
The goal of this practice parameter is to define the infrastructure, personnel, processes and governance needed
to establish a comprehensive framework for the safe, effective and transparent integration of artificial
intelligence (AI) into imaging practice. This practice parameter addresses principles of AI governance, selection of
AI solutions, local acceptance testing and real-world performance monitoring. It also includes special
considerations for non-FDA-regulated AI solutions and patient privacy considerations under HIPAA. The practice
parameter applies to all practitioners and support personnel — including but not limited to physicians,
technologists, medical physicists, informaticists, data scientists and administrators — who deploy, interpret,
interact with, support or act upon AI-derived outputs in the course of caring for patients during diagnostic
imaging, image-guided procedures, postprocessing and reporting of imaging. This practice parameter will be
revised as AI capabilities for diagnostic imaging evolve.

The scope of this practice parameter covers:

   • Required principles to help qualified end-users champion safe, effective and appropriate use of AI in
     diagnostic imaging.
   • Practice-based management of AI designed to process images within the clinical workflow that meets the
     FDA definition of Software as a Medical Device (SaMD), including, but not limited to, computer-aided
     detection (CADe), worklist triage (CADt), computer-aided diagnosis (CADx), and AI designed to achieve
     quantification of lesions, organ sizes, and other imaging features.
   • AI not currently subject to FDA SaMD regulation, including, but not limited to, generative AI-powered tools
     for both pixel-based and non-pixel-based use cases.

The scope does not cover:

   • 3D printing [1]
   • AI used in image acquisition or image reconstruction (e.g., for MRI acceleration, CT image reconstruction)
     [2, 3]
   • AI designed exclusively for the management of business processes, (e.g., revenue cycle management,
     patient scheduling, etc.[4])

II. PRINCIPLES FOR IMAGING AI

 A. Relevant Definitions

   • Image reconstruction: Image reconstruction is the process of creating 2D or 3D images from raw data,
     which are often projections of an object, using mathematical algorithms. Common methods include
     analytical algorithms like filtered back-projection and iterative methods that refine the image over multiple
     steps to reduce noise and artifacts.
   • Image postprocessing: Image postprocessing takes a reconstructed image and enhances or alters it to ease
     interpretation or other secondary use.
   • AI algorithm: An AI algorithm is a computational procedure that maps inputs to outputs using parameters
     estimated from data; it may include deterministic code but is not limited to hand-crafted rules. Through
     training (e.g., supervised, self-supervised or unsupervised), the algorithm’s parameters are optimized on
     example data to minimize objective loss of a defined objective, yielding a task-specific AI model.
   • AI model: An AI model is an AI algorithm that has been trained on data that provides examples of the task
     that the AI is intended to perform.
   • Inference: Inference is the process by which a trained AI model processes new inputs and generates
     outputs (optionally with uncertainty estimates).
   • AI solution: An AI solution (also known as an AI tool, application, software or product) is an AI model that
     can integrate into the healthcare enterprise using necessary standards and interfaces. In radiology, AI
     solutions can analyze images, text (such as radiology reports or notes from the medical record) and other
     data from the medical record. AI solutions can also identify and describe findings on radiology images and
     organize those findings in a particular format for review by a physician.
   • Instructions for use (IFU): The US FDA requires that AI vendors include IFU that describe how an AI solution
     is to be used and how it performed during the performance testing leading up to FDA clearance. The
     document includes information and directions for using the AI solution in practice [5, 6].
   • Qualified end-user: A qualified end-user of an AI solution is a licensed physician with the necessary
     qualifications and training to independently provide the equivalent medical service without the aid of the AI
     solution, and who possesses qualifications and training in the use of the AI solution, including the ability to
     assess the validity of its output [7].
   • Governance group: An AI governance group is responsible for the administrative, clinical and technical
     aspects of AI deployment and use. The group is essential regardless of whether the AI in question is a
     commercial product or a solution developed internally for the organization or practice. A diagnostic imaging
     physician should be part of this group.
   • Deployment: Deployment introduces an AI solution into the clinical workflow for use in patient care by
     qualified end-users.
   • Local acceptance testing: Local acceptance testing is the process of evaluating an AI solution to ensure that
     it meets the performance expectations of the practice. In some cases, this evaluation takes place in a
     “sandbox” environment that is not connected to the systems used to care for patients (i.e., prior to
     deployment), while in other cases it might occur after deployment to a small number of qualified end-users
     but not to the entire practice.
   • Drift: Drift describes gradual degradation in the performance of an AI model over time. Drift can be caused
     by multiple factors, including changes in the type of inputs provided to the model.
   • More definitions are available at the FDA Digital Health and Artificial Intelligence Glossary [8].


III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES
Successful AI deployment is a multistakeholder effort. The roles and tasks associated with each stakeholder in
the integration of AI into clinical practice are summarized in this section. A single individual may fulfill more than
one role. Some roles may be consolidated or supported by enterprise, vendor or regional collaborative resources
rather than dedicated staff in the radiology practice.
III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

A. Qualified End-Users

   1. The qualified end-user of an AI solution is defined in Section II.
   2. Qualified end-users of an AI solution should have a clear understanding of how it works, including the type
      of input required, the data used for inference, regulatory clearance and intended use, the nature of the
      output, and how to interpret that output. The qualified end-user should be made aware when the AI
      solution has run and produced an output — if it runs contemporaneously during their work. They should
      also understand the AI solution's capabilities and limitations (to the extent that they are known), how
      factors involved in the production of the images (e.g., machine manufacturer and model,
      protocol, acquisition and reconstruction parameters, image quality) and patient characteristics (e.g., age,
      gender, race, ethnicity) may influence performance and affect clinical decision making, and how disease
      prevalence affects AI performance.
   3. Qualified end-users should work closely with a practice’s AI governance group (discussed further in Section
      IV) when new AI solutions are being considered.

III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

B. Medical Physicists

   1. Qualified Medical Physicists are essential contributors to the safe and effective use of imaging AI
      technologies. Their responsibilities in imaging system performance, quality assurance and patient safety
      directly support the implementation of AI solutions by verifying input fidelity, evaluating protocol
      dependencies and establishing baseline technical performance for AI-embedded imaging functions.
      Scanner-integrated tools, such as those involved with image acquisition, reconstruction, embedded
      preprocessing algorithms and automated calibration — whether AI-based or not — can significantly impact
      the inputs to and outputs from downstream AI solutions. For applications like computer-aided detection,
      image reconstruction, image postprocessing and quantitative imaging, Qualified Medical Physicists
      contribute to site-level validation, monitor performance metrics and assess the impact of protocol or
      hardware changes on AI reliability, as outlined in the ACR–AAPM–SIIM Technical Standard and AAPM Task
      Group Report 273. In collaboration with qualified end-users and technical stakeholders, Qualified Medical
      Physicists can help define rollback criteria and sunsetting procedures, consistent with role-based lifecycle
      responsibilities outlined in the International Atomic Energy Agency’s guidance [9].
   2. The role of a Qualified Medical Physicist is described in the ACR–AAPM–SIIM Technical Standard for
      Electronic Practice of Medical Imaging [10].
   3. The American Association of Physicists in Medicine (AAPM) Task Group Report 273 details
      recommendations on best practices for AI and machine learning for computer-aided diagnosis in medical
      imaging [11].

III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

C. Imaging Informatics (II) and Information Technology (IT) Professionals

   1. Imaging informatics (II) and information technology (IT) professionals play an important role in ensuring
      that the computer systems and software that enable the care of patients in radiology work as expected. As
      such, they should participate in the planning and integration of AI into clinical practice.
   2. For successful AI deployment within a practice, they may be responsible for configuring the necessary IT
      infrastructure (in the cloud or on-site) for an AI solution, including hardware and software specifications for
      AI servers to meet expected volumes, provide timely output and integrate with other relevant clinical
      systems.
   3. II and IT professionals should also ensure the system is secure, managed for privacy requirements, and
      monitored and supported when technical issues arise. They may also configure and maintain technical
      infrastructure needed for post-deployment monitoring, such as integration with registries (e.g., Assess-AI),
      and for cybersecurity and privacy related to AI deployment [12].
   4. They may also be responsible for ensuring that images are correctly and securely transmitted to an AI
      solution, both during testing and in production, and that results are correctly presented to the qualified
      end-user and securely returned to the patient’s record in PACS, the reporting system or the medical record.
   5. Specific roles and responsibilities are described in the ACR–AAPM–SIIM Technical Standard for Electronic
      Practice of Medical Imaging [10].

III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

D. Data Scientists

   1. Data scientists can play a valuable role in supporting safe and effective AI integration. Leveraging their
      expertise in AI algorithms and model behavior, data scientists can complement the clinical perspective of
      the qualified end-user's experience of an AI solution, and can contribute across the lifecycle of an AI
      solution from local acceptance testing to postdeployment monitoring. Specific responsibilities may include:
          a. Assisting in the design of statistically robust local validation protocols, including determining exam
              volumes and types.
          b. Developing automated data pipelines and infrastructure to support ongoing monitoring of AI
              performance, data orchestration, system integration, and qualified end-user interaction with AI
              output.
           c. Synthesizing feedback into actionable insights to inform governance and quality assurance processes
              locally and contributing to national registries and monitoring programs.
   2. In addition, data scientists may also provide more advanced contributions, including but not limited to:
          a. Developing new models,
          b. Fine-tuning existing models for useand
           c. Supporting local deployment efforts, if appropriate resources and governance are in place.

III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

E. Radiology Technologists

   1. Radiologic technologists should:
          a. Be certified by the appropriate registry and possess unrestricted state licensure.
          b. Meet the qualification requirements of any existing ACR practice parameter or technical standard for
             acquisition of a particular examination.
         c. Be trained to properly operate those portions of the image data management system with which the
            individual must routinely interact.
         d. When the AI solution is part of the technologist's workflow, the technologist should be trained on
            the
                • AI use case and imaging parameters of the expected AI inputs
                • AI input image quality evaluation and remediation
                • AI-related quality assurance

III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

F. Manufacturers/Developers

   1. AI manufacturers and developers should support practices by providing clear guidance in the intended use
      of their solutions. Manufacturers of FDA-regulated AI solutions are required to provide standard guidance
      (IFU) on the product. In addition, manufacturers should deliver comprehensive documentation, including
      release notes and model versioning, and proactively notify customers prior to deploying new versions. To
      enhance transparency and support effective human–AI collaboration, manufacturers are encouraged to
      provide additional information such as:
           a. Information about model training, including:
                  a. Summaries of training data and internal and external evaluation data,
                  b. Model performance in relevant subgroups,
                   c. Scope of any FDA-authorized predetermined change control plan (PCCP) or model update
                      process, and
                  d. Per-version change notes that flag subgroup-specific changes in performance.
           b. Model explainability and inference transparency (e.g., which data were used for inference)
           c. Status of AI model output (e.g., processing, inferenced, rejected)
           d. Reason for data rejection (e.g., inadequate image quality, unsupported data format)
           e. AI model confidence scores or output uncertainty, when allowable through regulation, including
              indication of portions of the input data that most influenced model output
           f. Patient age groups for which the AI solution is intended to be used (e.g., adult, pediatric, adult and
              pediatric, etc.) and clear exceptions (e.g., low-dose chest CT performed with sedation on a pediatric
              patient)
   2. Sharing best practices from other users of the same AI solutions may also be valuable. These materials may
      be used at the discretion of the local personnel responsible for AI deployment and oversight.

III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

G. Administrators
Administrators may be involved with AI procurement, deployment and oversight at different levels of the
practice. Any designated administrative lead(s) may provide structure and leadership to the local AI program.
III. OPERATIONAL AND ADMINISTRATIVE PERSONNEL, QUALIFICATIONS AND ROLES

H. Legal/Compliance/Privacy Professionals

   1. Duties of the legal, compliance, and privacy professional may include:
          a. Advising the practice on the applicable scope of FDA clearance of a given AI solution and associated
             capabilities, limitations and off-label uses.
          b. Advising the practice on legal and regulatory considerations, including FDA, HIPAA and Health &
             Human Services/Office of the National Coordinator for Health IT/Office for Civil Rights requirements,
             plus applicable stateand local regulations and internal policies.
          c. Advising the practice on the common law and ethics of a particular AI solution, as well as AI in
             general.
          d. Ensuring that the deployment and local use of AI occurs within the boundaries of applicable
             institutional guidelines and local, state and national legislation.
         e. Confirming that any contracts, institutional review board oversight processes and documentation,
            and other legal documentation pertaining to the AI in use, are appropriately configured and
            executed.

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI

A. Governance

   1. Practices should establish an AI governance group responsible for oversight of selection, local acceptance
      testing, deployment, monitoring, rollback and sunsetting of AI solutions as necessary. If AI governance
      groups exist at other levels of the hospital, health system or organization, the practice-level AI governance
      group should expect to collaborate with them.
   2. This group should include at least one diagnostic imaging physician who may or may not also be a qualified
      end-user for an AI solution being discussed, but who is nevertheless able to lead the governance process.
      The remainder of the group should be interdisciplinary and consist of members reflecting the operational
      and administrative roles detailed in Section III.
   3. Members of the governance group are expected to be impartial with respect to the AI solution being
      considered. As such, the composition of the group may be dynamic in an effort to mitigate potential
      conflicts of interest. For example, a manufacturer or developer of an AI solution would not be expected to
      participate in governance discussions related to the deployment of their product at the practice.
   4. A qualified end-user should bring requests for new AI solutions intended for introduction into the clinical
      environment to this group for review. If the qualified end-user is already a member of the governance
      group, appropriate mitigation of potential conflicts of interest should be implemented (e.g., the qualified
      end-user should recuse themselves from the review and decision making for the AI solution in question).
   5. The group should meet regularly and keep minutes that record decisions, any risk acceptances, and defined
      rollback or sunset criteria.

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI

B. Documentation and Inventory

   1. Practices should maintain an up-to-date local inventory of all deployed AI solutions.
   2. Key documentation for deployed AI solutions should include:
          a. Model name and documented version or build
          b. Deployment date and environment
          c. IFU/labeling and intended use, including
                  • how AI outputs will be reviewed by qualified end-users, and whether and how they will be
                     recorded in the medical record
                  • specifications for intended populations (adult, adult and pediatric, pediatric, unknown, etc.)
          d. Scope/identifier of any FDA-authorized PCCP
          e. Local acceptance testing protocol and results
          f. Relevant routing rules (DICOM/Health Level Seven/Fast Healthcare Interoperability Resources) and
              inclusion/exclusion criteria (e.g., IHE AI Workflow for Imaging/AI Results/AI Result Assessment for
              Imaging conformance claims and test reports, relevant adult and/or pediatric subgroups, etc.)
          g. Qualified end-user training logs
          h. Postdeployment monitoring data and drift checks
           i. Acceptance/rejection logging configuration
           j. Contact information for qualified end-user(s) involved in the governance of the AI solution and
              manufacturer/developer of the solution

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI

C. Security and Compliance
   1. Practices are expected to adhere to their organization’s security and compliance requirements for AI. This
      includes:
          • how AI results will be incorporated into the medical record and
          • how the practice’s policy on data retention, transparency and purging will apply to these results, as
             well as
          • appropriate cybersecurity controls.
       Data privacy considerations apply to the use of AI as they do elsewhere in healthcare. The following should
   2. be considered:
          • HIPAA compliance
                 ○  AI solutions should adhere to the HIPAA Privacy, Security and Breach Notification Rules.
                 ○  Data used for model fine-tuning, local acceptance testing or retraining should be de-identified
                    to HIPAA Safe Harbor standards whenever feasible. If PHI is retained, a business associates'
                    agreement (BAA) covering the intended use or disclosure with the AI manufacturer or
                    developer should be executed before deployment, and data-handling and security controls
                    verified.
                 ○  The HIPAA Notice of Privacy Practices (NPP) should be reviewed and updated if any new AI use
                    cases are not covered under the existing notice. Even if not required, transparency with
                    patients is encouraged.
          • Data security
                 ○  Data encryption should be enforced in transit and at rest.
                 ○  AI access should be restricted to approved networks, devices, endpoints and authenticated
                    users.
                 ○  Multifactor authentication should be utilized to access AI solutions, when feasible.
          • Downtime planning
                 ○  Qualified end-users should design or be trained on processes for reverting to non-AI clinical
                    operations during AI outages.
                 ○  Protocols should be designed to notify stakeholders of downtime impact, duration and interim
                    procedures.
                 ○  AI updates should be scheduled during low-impact periods.
          • Audit and breach notification
                 ○  Data accessed by AI solutions should be logged.
                 ○  Logs should be auditable.
       Any unauthorized access or disclosure of PHI by AI solutions should be reported to the practice’s legal,
       compliance, or privacy professional and, if required, to the Department of Health and Human Services or
   3. other required external parties.
       The AI governance group should evaluate whether their use of AI might implicate one or more of the
       following laws and rules. This is not an exhaustive list. Qualified end-users should consult a healthcare
   4. lawyer in their relevant jurisdiction to obtain counsel on specific medicolegal matters.
          • HIPAA/HITECH
          • FDA Software as a Medical Device (SaMD)
          • European Union (EU) Medical Device Regulation (MDR)
          • EU AI Act
          • General Data Protection Regulation (GDPR) — Europe
          • U.S. Civil Rights Act (Title VII) and Americans with Disabilities Act (discrimination and bias)
          • Local and state laws

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI

D. Model Selection

   1. Practices should have a defined process and criteria for determining which AI solutions they will deploy.
   2. This process should include relevant clinical, technical and business considerations.
          a. If practices care for both adult and pediatric patients, this should be considered during AI selection. If
            selecting an adult-only AI solution in mixed practices, a rationale and mitigation plan should be
            documented to address excluded populations.

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI

E. Local Acceptance Testing

   1. Practices should have a process by which qualified end-users evaluate initial AI performance using local
      data.
          • For pixel-based AI, local data should come from a variety of machine manufacturers, models and
             protocols, and reflect a spectrum of image quality.
          • Local data should include dose-optimized or ultra-low-dose images, or AI-postprocessed images, as
             appropriate, since this may affect performance.
   2. Predefined metrics for acceptable AI performance should be agreed upon prior to the evaluation process
      and tailored to relevant patient populations and exam subgroups.For pediatric patient populations, the age
      or age group breakdown (e.g., neonate, infant, child, adolescent) of patients to be included should be
      stated.
   3. These metrics should align with clinical expectations and inform both AI deployment decisions and qualified
      end-user training prior to deployment.

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI

F. Training and Instructions for Use

   1. Documented training procedures are recommended for qualified end-users and should be appropriate to
      the complexity of the clinical use case.
          • Training should include instruction on applicable patient populations, specifically indicating age
            range.
   2. IFU/labeling be readily accessible to qualified end-users at deployment.
   3. Supplemental training is required after each model/version or intended‑use change and should include
      just‑in‑time help, common pitfalls, and lessons learned from monitoring, so that new issues can be shared
      across the practice and reported back to the governance group for review and appropriate action.
   4. Notification protocols should be established to ensure that qualified end-users are aware when AI solutions
      are being used contemporaneously within their scope of work.

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI

G. Monitoring

   1. Practices should establish continuous monitoring with periodic reports on routing rule adherence, accuracy,
      calibration, drift and subgroup performance.
   2. Acceptance, rejection and overrides of AI outputs should be logged in a standardized form to support peer
      learning and quality improvement.
   3. Practices should submit to or benchmark the performance of their AI solutions against qualified registries
      (e.g., Assess-AI) to capture and understand real-world performance.
   4. Complications or adverse events potentially related to AI use should be reviewed in peer-learning programs
      and findings or conclusions should be actionable. Potential safety events should be triaged for medical
      device reporting (MDR) and a documented escalation pathway should be maintained.
   5. Practices should decide who has authority to take an AI solution offline for remediation. Specific stop rules
      should be considered in instances of significant degradation in pediatric subgroup performance, repeated
      misrouting of pediatric exams, and sustained high pediatric override rates.

IV. PRACTICE SPECIFICATIONS FOR IMAGING AI
 H. Non-FDA-Regulated Models

    1. If practices are deploying non-FDA-regulated AI solutions, additional oversight and compliance with local
       governance is recommended. This includes locally developed models as well as emerging technologies such
       as generative AI (e.g., large language models , vision-language models , foundation models, etc.).
    2. Special considerations may need to be taken with this class of AI solutions, including review by the
       organization’s IRB, additional resources for postdeployment monitoring, and extra review by the practice’s
       legal, compliance and privacy professionals.

V. OTHER CONSIDERATIONS
Practices using AI clinically should consider how their AI solutions release outputs (e.g., directly into the patient’s
record — whether PACS or the medical record — or only after review by a qualified end-user). They should also
consider whether the qualified end-user reports the AI output (which may be required by law in certain states)
and any concordance/discordance with their interpretation, and whether the AI outputs are directly accessible
by other members of the care team or by patients. If AI outputs are visible in patient portals, practices should
review how those outputs are displayed in pediatric contexts (proxy access by parents or guardians, delayed
release rules for adolescents, etc.). Misclassified AI results in a portal could cause patient or caregiver anxiety or
inappropriate action. The ACR Practice Parameter for Communication of Diagnostic Imaging Findings provides
guidance on communication of radiology results. [13]

It is recommended that AI solutions only be used by qualified end-users who can accurately assess the veracity of
their outputs. Furthermore, qualified end-users should be familiar with the IFU, including the capabilities and
limitations of the AI solution and its intended use in clinical workflow. For instance, AI triage software that is not
intended to be used as a diagnostic device should not be used as such unless the practice has made an informed
decision to use it “off-label.” Furthermore, if an AI solution intended for use on adult patients is considered for
"off-label" use on pediatric patients, the practice should evaluate it on data from the intended pediatric
population prior to use. Communication and permanent storage of AI outputs is not recommended without
qualified end-user incorporation of the output into the standard of care reporting workflow. The practice’s
governance group is responsible for ensuring that qualified end-users apply the technology appropriately. Both
practices and their qualified end-users ultimately bear responsibility and liability for the care rendered when an
AI solution is used.

Foundation models for imaging that generate a holistic output rather than perform a single task are not currently
regulated by the FDA for use in patient care and, as of the writing of this practice parameter, are not marketed
for such use in the United States. There are multiple considerations when using AI solutions built on foundation
models, including, but not limited to, drift and unpredictability, limited clinical validation, and unclear regulatory
governance and medical malpractice liability.
ACKNOWLEDGEMENTS
This practice parameter was developed according to the process described under the heading The Process for
Developing ACR Practice Parameters and Technical Standards on the ACR website (https://www.acr.org/Clinical-
Resources/Practice-Parameters-and-Technical-Standards) by the Commission on Informatics and the Commission
on Quality and Safety in collaboration with SIIM.
Writing Committee – members represent their societies in the initial and final revision of this practice parameter
ACR                                                    SIIM
Cook, Tessa MD, PhD, Chair                             Kikano, Elias MD
Bumbarger, Nathan MD                                   Kottler, Nina MD
DelGaizo, Andrew MD                                    Roth, Christopher J MD
Galante, Nicholas J. MD
Goldberg Stein, Shlomit MD
Hawkins, Matt MD
Nicola, Lauren MD
Towbin, Alex MD
Wandtke, Ben MD
Yang, Roger MD

Committee on Practice Parameters and Technical Standards
(ACR Committee responsible for sponsoring the draft through the process)

Caplin, Drew M MD, Chair                               Amodio, John B MD
Bartel, Twyla B DO, MBA                                Brook, Olga R MD
Chao, Samuel MD                                        Gabriel, Helena MD
Kaufman, Claire MD                                     Keenan, Mary Ann DMP
Ko, Jane P MD                                          Shah, Lubdha MD
Siebert, Derrick MD                                    Strigel, Roberta M MD
Subhas, Naveen MD, MPH

Larson, David B MBA, MD, Chair, Commission on Quality and Safety
Wald, Christoph MBA, MD, PhD, Chair, Commission on Informatics & the Data Science Institute

Comments Reconciliation Committee
Moriarity, Andrew MD - CSC, Co-Chair                   Prosper, Ashley MD - CSC, Chair
Bumbarger, Nathan MD                                   Caplin, Drew M MD
Cook, Tessa MD, PhD                                    DelGaizo, Andrew MD
Galante, Nicholas J. MD                                Goldberg Stein, Shlomit MD
Hawkins, Matt MD                                       Kikano, Elias MD
Kottler, Nina MD                                       Larson, David B MBA, MD
Nicola, Lauren MD                                      Roth, Christopher J MD
Rubin, Eric MD - CSC                                   Schoppe, Kurt - CSC
Towbin, Alex MD                                        Wald, Christoph MBA, MD, PhD
Wandtke, Ben MD                                        Yang, Roger MD


REFERENCES
1. Ma L, Yu S, Xu X, Moses Amadi S, Zhang J, Wang Z. Application of artificial intelligence in 3D printing physical
organ models. Mater Today Bio. 2023 Dec;23():100792.
2. Brady SL. Implementation of AI image reconstruction in CT-how is it validated and what dose reductions can be
achieved. Br J Radiol. 2023 Oct;96(1150):20220915.
3. Fransen SJ, Roest C, Simonis FFJ, Yakar D, Kwee TC. The scientific evidence of commercial AI products for MRI
acceleration: a systematic review. Eur Radiol. 2025 Aug;35(8):4736-4746.
4. Marty Stempniak. Use of AI in radiology revenue cycle management. 2024.
https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/medical-billing-and-
coding/use-ai-radiology-revenue-cycle-management.
5. Brandon J. Nelson, Rongping Zeng, Marla B.K. Sammer, Donald P. Frush, Jana G. Delfino, An FDA Guide on
Indications for Use and Device Reporting of Artificial Intelligence-Enabled Devices: Significance for Pediatric Use,
Journal of the American College of Radiology,Volume 20, Issue 8,2023,Pages 738-741,ISSN 1546-
1440,https://doi.org/10.1016/j.jacr.2023.06.004.https://www.sciencedirect.com/science/article/pii/S1546144023004234)
Abstract: Radiology has been a pioneer in adopting artificial intelligence (AI)-enabled devices into the clinic.
However, initial clinical experience has identified concerns of inconsistent device performance across different
patient populations. Medical devices, including those using AI, are cleared by the FDA for their specific indications
for use (IFUs). IFU describes the disease or condition the device will diagnose or treat, including a description of
the intended patient population. Performance data evaluated during the premarket submission support the IFU
and include the intended patient population. Understanding the IFUs of a given device is thus critical to ensuring
that the device is used properly and performs as expected. When devices do not perform as expected or
malfunction, medical device reporting is an important way to provide feedback about the device to the
manufacturer, the FDA, and other users. This article describes the ways to retrieve the IFU and performance data
information as well as the FDA medical device reporting systems for unexpected performance discrepancy. It is
Adopted
crucial that2026  (Resolution
              imaging         13)
                       professionals, including radiologists, know how to access and use these tools to improve the
informed use of medical devices for patients of all ages. Keywords: Artificial intelligence; evaluations; indications
for use; patient population; pediatrics.
6. Nelson BJ, Zeng R, Sammer MBK, Frush DP, Delfino JG. An FDA Guide on Indications for Use and Device
Reporting of Artificial Intelligence-Enabled Devices: Significance for Pediatric Use. J Am Coll Radiol. 2023
Aug;20(8):S1546-1440(23)00423-4.
7. Model Legislative Language – AI Qualified End-User, Working Draft v1.0 , American College of Radiology, 2024.
https://edge.sitecorecloud.io/americancoldf5f-acrorgf92a-productioncb02-
3650/media/ACR/Files/Advocacy/Model-Legislative-Language-AI-Qualified-End-User---Working-Draft.pdf.
8. https://www.fda.gov/science-research/artificial-intelligence-and-medical-products/fda-digital-health-and-
artificial-intelligence-glossary-educational-resource.
9. Clinical Implementation of Medical Imaging Based Artificial Intelligence Tools – Guidelines for Medical Physicists
[IAEA Preprint], 2025. https://inis.iaea.org/records/gbpec-hj142.
10. American College of Radiology. ACR–AAPM–SIIM Technical Standard for Electronic Practice of Medical
Imaging. Available at https://gravitas.acr.org/PPTS/GetDocumentView?docId=136+&releaseId=2
11. Hadjiiski L, Cha K, Chan H-P, et al. AAPM task group report 273: Recommendations on best practices for AI and
machine learning for computer-aided diagnosis in medical imaging. Med Phys. 2023; 50: e1–e24.
https://doi.org/10.1002/mp.16188.
12. A Review of Cybersecurity and Privacy Standards in Medical Imaging: Consensus, Frameworks, and Best
Practices Chen, Po-Hao et al. Journal of the American College of Radiology, Volume 0, Issue 0.
13. American College of Radiology. ACR Practice Parameter for Communication of Diagnostic Imaging Findings.
Available at https://gravitas.acr.org/PPTS/GetDocumentView?docId=74+&releaseId=2
 *Practice parameters and technical standards are published annually with an effective date of October 1 in the
 year in which amended, revised, or approved by the ACR Council. For practice parameters and technical
 standards published before 1999, the effective date was January 1 following the year in which the practice
 parameter or technical standard was amended, revised, or approved by the ACR Council.
