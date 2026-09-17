#!/usr/bin/env python3
"""Run 23: extend analysis/clauses.csv to cover US sources added by runs 12-19.
Appends one row per .md under raw/us-med-schools and raw/health-systems not
already present (same 13-column schema). Fields contain ONLY what the source
document states; blank when absent. phi_rule verbatim or lightly ellipsised.
"""
import csv, os

BASE = "/Users/openclaw/git/medschool-ai-guidelines"
COLS = ["file","org","doc_type","effective_date","applies_to","banned_uses",
        "permitted_uses","phi_rule","disclosure_rule","assessment_rule",
        "secure_tools_named","enforcement","aamc_alignment"]

R = []
def add(f, org, doc_type, **kw):
    row = {c: "" for c in COLS}
    row.update(file=f, org=org, doc_type=doc_type, aamc_alignment="no")
    row.update(kw)
    R.append(row)

# ---------------- us-med-schools (77) ----------------
add("raw/us-med-schools/atsu--libguides-guidelines-on-ai.md",
    "A.T. Still University (LibGuide)", "guidance", applies_to="students;faculty",
    phi_rule="Avoid utilizing generative AI applications with any form of protected health information or other legally protected data.")
add("raw/us-med-schools/atsu-its--navigating-ai-at-atsu.md",
    "A.T. Still University Information Technology", "guidance", applies_to="students;faculty;staff",
    banned_uses="Information shared with generative AI tools using default settings is not private and could expose proprietary or sensitive information to unauthorized parties.",
    permitted_uses="Connect with ITS when selecting AI tools: tools procured for the institution have appropriate privacy and security protections and vendors are vetted as to their responsible use of AI.",
    secure_tools_named="ChatGPT;Google Gemini (named as examples);Anthology CRM (enterprise AI features)",
    enforcement="Students must follow the AI policies established by their academic program, course, and instructor; adhere to existing policies and guidelines covering ethical and professional expectations.")
add("raw/us-med-schools/atsu-kcom--policies-page.md",
    "A.T. Still University Kirksville College of Osteopathic Medicine", "guidance", applies_to="students")
add("raw/us-med-schools/cincinnati--ai-at-uc-guidelines.md",
    "University of Cincinnati", "guidance", applies_to="students;faculty;staff",
    banned_uses="Use of Generative Artificial Intelligence Technologies Prohibited in NIH Peer Review Process.",
    permitted_uses="Sign into UC-licensed tools with UC credentials for privacy-protected access to approved AI tools; responsible use should align with the UC Student Code of Conduct.",
    phi_rule="Neither controlled nor restricted data are approved for use in AI tools. UC student directory data is not approved for use in AI tools.",
    enforcement="The responsible use of technology, including AI technology, should align with the UC Student Code of Conduct.")
add("raw/us-med-schools/cincinnati--ai-at-uc-policies.md",
    "University of Cincinnati", "guidance", applies_to="students;employees",
    banned_uses="AI may not be used in a manner that creates a conflict of interest;AI may not be used to engage in any form of harassment.",
    permitted_uses="Acceptable Use of Information Technology Policy is applicable to the use of AI; Information Security Reviews identify and document risk for systems including AI.",
    enforcement="The Student Code of Conduct is applicable to the use of AI; employees may receive disciplinary action, up to and including termination, for conduct and/or rules violations.")
add("raw/us-med-schools/cincinnati--ai-at-uc-students.md",
    "University of Cincinnati", "guidance", applies_to="students",
    permitted_uses="UC provides AI tools and services for students; students should consult their syllabus for course-specific guidelines on the use of AI.",
    secure_tools_named="Copilot Chat")
add("raw/us-med-schools/cwru-som--curriculum-policies-and-procedures.md",
    "Case Western Reserve University School of Medicine", "guidance", applies_to="students")
add("raw/us-med-schools/drexel--it-genai-guidance.md",
    "Drexel University Information Technology", "guidance", applies_to="students;faculty;staff",
    banned_uses="Any university sensitive data must not be shared with any of the consumer versions of these GenAI services that have not been reviewed and approved for use.",
    permitted_uses="Usage of approved services is governed by agreements that protect intellectual property, maintain privacy, and comply with legal obligations to safeguard personal data.",
    phi_rule="It's possible prompts and attached files may be processed in other countries, where compliance with U.S. law covering regulated data (e.g., academic records covered by FERPA or health records covered by HIPAA) may not be enforced.",
    enforcement="Drexel employees should contact Information Security for a risk assessment review before using a different service or building GenAI-based services such as chatbots.")
add("raw/us-med-schools/duquesne--ai-at-duquesne.md",
    "Duquesne University (Provost's Office / AI Committee)", "guidance", applies_to="faculty;students",
    banned_uses="Restricted Data may not be used in conjunction with any generative AI tool that the University has not licensed and/or contracted for use;Given the sensitivity and confidentiality of student assessment, faculty are not permitted to use AI programs in student assessment that have not been approved for use by the University;Unprotected third-party AI software is prohibited from being used to read, respond or track emails on a Duquesne email account;Default syllabus statement: Using generative artificial intelligence tools in classwork is prohibited and will be treated as a violation of academic integrity.",
    permitted_uses="Faculty may use Duquesne-approved AI programs such as Microsoft Copilot to assist in email correspondence; faculty strongly recommended to develop an AI course policy stipulating acceptable uses.",
    phi_rule="Faculty are responsible for ensuring their use of AI does not violate existing disclosure laws and policies for confidential information, including the Health Insurance Portability and Accountability Act (HIPAA), Family Educational Rights and Privacy Act (FERPA), Duquesne University's TAPs and CTS's Data Governance Service Requirements.",
    disclosure_rule="If faculty intend to use AI to assist in developing course material, assignments, or email correspondence, they should disclose this to students in their AI syllabus statement; if AI is used to support student assessment in any capacity, faculty are strongly recommended to disclose its use to students verbally and in the syllabus.",
    assessment_rule="AI tools should not be used as the only means of assessing students; if AI is used in student assessment, faculty remain fully responsible for holistically evaluating student performance; consult department chair before using AI to assist in student assessment.",
    secure_tools_named="Microsoft Copilot (Duquesne-approved, login with MultiPass credentials); CTS AI Guide approved-tools list",
    enforcement="Using generative AI tools in classwork without permission will be treated as a violation of academic integrity.")
add("raw/us-med-schools/hofstra--ai-at-hofstra-overview.md",
    "Hofstra University", "guidance", applies_to="students;faculty;staff",
    permitted_uses="Hofstra ChatGPT Edu available to all students, faculty, administrators (first institution on Long Island to launch campus-wide); pilot program began 2024 academic year; all outputs should be reviewed by the user before use or distribution.",
    disclosure_rule="In general, you should disclose when you have used ChatGPT Edu.",
    secure_tools_named="Hofstra ChatGPT Edu (OpenAI does not use data entered to train its models);GPT-5 Pro;Deep Research;Image Generation (faculty/stath advanced features)",
    enforcement="Use of Hofstra ChatGPT Edu is subject to all applicable University policies, including the Computer Networks Acceptable Use Guidelines and the Confidentiality Agreement and Security Policy; follow Hofstra's Honor Code; University reserves the right to review account content to maintain system security or investigate suspected policy violations.")
add("raw/us-med-schools/howard-university--ai-policy-100-022-full.md",
    "Howard University", "formal policy", effective_date="2026-04-24 (Policy 100-022)",
    applies_to="faculty;staff;students;contractors;affiliates",
    banned_uses="Confidential Information, Personally Identifiable Information (PII) that is sensitive information, or other protected University Data shall not be entered into AI systems unless expressly authorized in writing and subject to appropriate institutional review and approval;Confidential Information, PII, or student education records shall not be entered into AI systems in connection with teaching and learning activities;University Data and Confidential Information shall not be used to train AI systems or models;Use of AI in instructional activities shall not undermine learning objectives, assessment integrity, or the evaluation of student work;employees, students, contractors, and affiliates shall not enter into agreements with external entities involving University Data or IP for AI purposes without prior legal review",
    permitted_uses="University-wide framework for the responsible use of AI that promotes ethical conduct, protects individual and institutional interests, upholds academic integrity, and ensures alignment with applicable laws.",
    phi_rule="Use of AI in work-related activities shall comply with all applicable University policies governing data privacy, information security, and records management, including requirements related to student education records (FERPA) and protected health information (HIPAA).",
    disclosure_rule="Use of AI shall be disclosed when required by the academic, research, administrative, or operational context in which it is employed; research use documented and disclosed as required by funding agencies, publishers, or other binding external requirements.",
    assessment_rule="Student use of AI shall comply with course requirements, instructor requirements, and all applicable University academic conduct policies; in the absence of explicit course-level guidance, students shall seek clarification from the instructor prior to using AI tools for coursework or assessments.",
    enforcement="Failure to follow this policy may result in disciplinary action in accordance with applicable University policies and procedures; Provost & Chief Academic Officer is the Responsible Officer for implementation and enforcement.")
add("raw/us-med-schools/howard-university--ai-policy-100-022.md",
    "Howard University", "formal policy",
    applies_to="faculty;staff;students;contractors;affiliates",
    permitted_uses="Establishes a university-wide framework for the responsible use of AI that promotes ethical conduct, protects individual and institutional interests, upholds academic integrity, and ensures alignment with applicable laws and Howard University policies.",
    effective_date="2026-04-24 (Policy 100-022)")
add("raw/us-med-schools/howard-university--initial-genai-tools-guidelines.md",
    "Howard University Office of the Provost", "guidance", applies_to="students;faculty",
    banned_uses="According to the Academic Code of Student Conduct, it is a cause for concern when students submit work for assessment as their own, which has been substantially created using artificial intelligence tools or other content-generating tools without obtaining permission from the instructor.",
    disclosure_rule="Fairness and transparency are key to hosting an innovative and safe learning environment.",
    secure_tools_named="ChatGPT (named as example AI writing tool)",
    enforcement="Schools, colleges, departments, and faculty should develop their own AI policies with clear parameters and penalties for violation; any instructor has the right to inquire about a student's authorship of AI-related work, and students may defend themselves against such allegations.")
add("raw/us-med-schools/kcu--harnesses-ai-medical-education-blog.md",
    "Kansas City University", "curricular", applies_to="students")
add("raw/us-med-schools/kcu--medicine-reimagined-ai-blog.md",
    "Kansas City University", "curricular", applies_to="students",
    permitted_uses="KCU-COM curriculum includes comprehensive AI training beginning in year one: prompt crafting, refining system outputs, computer vision and language generation in clinical scenarios, data-analysis module on health data.",
    phi_rule="Case-based discussions and class debates encourage students to think critically about patient privacy, fairness in algorithms and how to balance speed with equity in clinical decision-making.")
add("raw/us-med-schools/kcu-library--introduction-to-ai.md",
    "Kansas City University Library", "guidance", applies_to="students;faculty",
    permitted_uses="AI tools available through library databases (e.g., Scopus AI for summaries and concept maps).",
    assessment_rule="Each college has empowered instructors and advisors to set their own standards and communicate them to students.")
add("raw/us-med-schools/ku--responsible-ai.md",
    "University of Kansas", "guidance", applies_to="students;faculty;staff",
    permitted_uses="Policies apply based on the activity and data involved, rather than the specific technology used (data privacy, security, research integrity, academic conduct, acceptable use); KUMC AI Steering Committee provides strategic leadership and governance for responsible AI use.",
    disclosure_rule="Transparency: AI use should be open and understandable to those affected.",
    enforcement="Follow university policies, use approved tools, and safeguard sensitive data.")
add("raw/us-med-schools/kumc--ai-steering-committee.md",
    "University of Kansas Medical Center", "guidance", applies_to="institution",
    permitted_uses="AI Steering Committee provides strategic leadership and governance for the responsible use of artificial intelligence across academics, administration, and research at KU Medical Center.")
add("raw/us-med-schools/lecom--college-of-medicine-catalog-2025-2026.md",
    "Lake Erie College of Osteopathic Medicine", "handbook section", effective_date="2025-2026 academic year",
    applies_to="students",
    phi_rule="Any violation of HIPAA, including placing HIPAA protected information on personal electronic devices or transmitting such information to home e-mail addresses (professionalism conduct standard; catalog contains no AI-specific policy).",
    enforcement="Honor Code; Code of Student Conduct and Discipline; adjudication of Honor Code Violations (general academic-conduct framework, not AI-specific).")
add("raw/us-med-schools/loyola-stritch--student-handbook-2025-2026.pdf.md",
    "Loyola University Chicago Stritch School of Medicine", "handbook section", effective_date="2025-2026 (updated 8/19/25)",
    applies_to="students",
    banned_uses="A student's presentation of academic work, in whole or part from any source (e.g., published literature, web resources, generative AI, third parties such as ghostwriters) as their own (whether paraphrased or copied in verbatim) is unacceptable and constitutes an academic integrity violation.",
    phi_rule="Compliance with HIPAA rules includes maintaining confidentiality of paper and electronic health records and protected health information; all students are required to complete HIPAA training.",
    disclosure_rule="Failure to disclose the unapproved use of AI is a violation of our professional standards.")
add("raw/us-med-schools/meharry-sacs--artificial-intelligence-program.md",
    "Meharry Medical College (School of Applied Computational Sciences)", "curricular", applies_to="students",
    permitted_uses="MS in Artificial Intelligence program: 14 courses, 42 graduate credits, culminating in an industry-type capstone.")
add("raw/us-med-schools/miami-miller--ai-in-medical-education-resources.md",
    "University of Miami Miller School of Medicine", "guidance", applies_to="faculty;students",
    permitted_uses="Resources page centralizes guides, instructional frameworks, toolkits, and best practices for ethical and effective integration of AI into medical teaching, learning, assessment, and scholarly work.",
    secure_tools_named="UM AI Tools;Gemini;Copilot;ChatGPT;Claude;Louis Calder Memorial Library curated AI guide",
    aamc_alignment="no (LCME@aamc.org contact in footer only)")
add("raw/us-med-schools/miami-miller--ai-in-medical-education.md",
    "University of Miami Miller School of Medicine (Office of AI in Medical Education)", "guidance",
    applies_to="faculty;students;trainees;staff",
    phi_rule="We strictly observe FERPA, HIPAA, and IRB requirements, prioritize institutionally approved and compliant AI tools, and incorporate privacy by design in all data practices.",
    disclosure_rule="We emphasize unbiased approaches to learning and assessment, require transparency in all AI tools and models, and maintain thorough documentation; all activities comply with the Miller School's AI policies, with clear expectations for disclosure and ethical conduct.",
    assessment_rule="Vision: assessment is trustworthy and competency based; faculty development empowers faculty to adopt AI responsibly in teaching, assessment, and mentorship.")
add("raw/us-med-schools/morehouse-sm--service-desk-ai-policies-guidelines.md",
    "Morehouse School of Medicine", "guidance", applies_to="students;faculty",
    permitted_uses="During the 2024-2025 academic year, Academic Affairs established an Academic Policy Working Group to develop generative AI guidance for both student learning and faculty instruction.")
add("raw/us-med-schools/morehouse-sm--student-handbook-student-use-of-ai.md",
    "Morehouse School of Medicine", "formal policy", effective_date="2026-2027 handbook",
    applies_to="students",
    banned_uses="Tools that may not be used for these assignments include chat GPT, GPT-4, Copilot, Google Bard, and other similar tools.",
    permitted_uses="The use of generative AI tools in study, learning, and assignments where this is permitted can be an important aspect of learning.",
    assessment_rule="Unless otherwise specified in the specific in-class/closed resource examination/assessment, use of generative AI content tools for examinations/assessments that are specifically not \"open book/open resource\" constitutes academic dishonesty.",
    secure_tools_named="ChatGPT;GPT-4;Copilot;Google Bard (named in prohibition)",
    enforcement="Will be grounds for SAPP referral; students inappropriately using such resources will be subject to dismissal.")
add("raw/us-med-schools/nova-kpcom--student-handbook-academic-standards-genai.md",
    "Nova Southeastern University Kiran C. Patel College of Osteopathic Medicine", "handbook section",
    effective_date="2025-2026", applies_to="students",
    banned_uses="(captured text covers general academic-responsibility standards; no AI-specific provision visible in extract)",
    disclosure_rule="Work is not original when copied from any other source unless such copying is acknowledged by the person submitting the work at the time of submission; standards of scholarship require that the writer give proper acknowledgment when the thoughts and words of another author are used.",
    enforcement="Violations of academic responsibility include plagiarism, any form of cheating, conspiracy to commit academic dishonesty, misrepresentation, bribery, forging or altering documents.")
add("raw/us-med-schools/nova-su--libguide-ai-at-nsu.md",
    "Nova Southeastern University Libraries", "guidance", applies_to="students;faculty",
    permitted_uses="Library-licensed AI databases: O'Reilly Answers, ScienceDirect AI, IBISWorld, Oxford Academic Research Assistant; Faculty Resources for AI webpage.",
    secure_tools_named="O'Reilly Answers;ScienceDirect AI;Oxford Academic Research Assistant (library-licensed)",
    effective_date="last updated 2026-06-17")
add("raw/us-med-schools/nova-su-lec--responsible-use-of-genai-infographic.md",
    "Nova Southeastern University Learning and Educational Center", "guidance", applies_to="students;faculty",
    permitted_uses="Responsible Use of Generative AI with F.A.S.T.E.R. framework (Fact-check, Aware of bias, Secure, Transparent, Ethical, Responsible).",
    disclosure_rule="TRANSPARENT: Identify content that has been produced using GAI; notify users that they are interacting with an AI tool; document decisions.")
add("raw/us-med-schools/ou-hsc--libguide-artificial-intelligence-and-genai.md",
    "University of Oklahoma Health Sciences Center (LibGuide)", "guidance", applies_to="students;faculty")
add("raw/us-med-schools/penn-state--ai-guidelines.md",
    "Penn State University", "guidance", applies_to="students;faculty;staff",
    banned_uses="Ownership and licensing of AI outputs vary depending on the platform and its terms of service, and in many cases you may not hold a copyright over AI-generated work at all.",
    permitted_uses="Penn State supports the responsible exploration and use of AI; Adobe Firefly is the approved image generation tool for distributed images.",
    assessment_rule="Use of AI Software to Assist with Grading Student Work is classified as courseware: instructors need approval from the department head and dean (or commonwealth campus leadership) prior to use; EEAAP required if accessibility gaps identified.",
    secure_tools_named="Adobe Firefly (approved image generation);ChatGPT;Standard Copilot;M365 Copilot (EEAAP templates provided)")
add("raw/us-med-schools/penn-state-com--harrell-library-genai-guide.md",
    "Penn State College of Medicine (Harrell Health Sciences Library)", "guidance",
    applies_to="students;faculty;staff", effective_date="last updated 2026-08-28",
    phi_rule="PSU Copilot is not HIPAA compliant. College of Medicine employees and students should consult with CoM IT for specific guidance and consider using the CoM instance of M365 if handling PHI information.",
    permitted_uses="AI Essentials course and AI literacy training encouraged for faculty, staff and students.",
    secure_tools_named="Claude;Gemini;ChatGPT (available in the AI Studio);Copilot (AI Guides support)")
add("raw/us-med-schools/penn-state-com--md-student-handbook.md",
    "Penn State College of Medicine", "handbook section", applies_to="students (MD and PA);faculty",
    banned_uses="Submitting AI-generated work as one's own without disclosure will constitute an academic integrity violation and misconduct.",
    phi_rule="Students shall follow the privacy regulations set forth in the Health Insurance Portability and Accountability Act (HIPAA) at all times.",
    disclosure_rule="Submitting AI-generated work as one's own without disclosure will constitute an academic integrity violation and misconduct.",
    assessment_rule="Violations in Academic Integrity are investigated at the level of the course or clerkship with assistance of the Office of Evaluation and Assessment and may be referred to the Academic Progress Committee.",
    secure_tools_named="This policy applies to the use of all generative AI tools, including but not limited to Chat GPT, Grammarly, Copilot, and other AI tools, including those provided by the university.",
    enforcement="Academic Integrity Policy G-9 lists violations that are grounds for adverse actions and/or dismissal from the MD or PA program; Student Conduct process; Appeals Committee review.",
    aamc_alignment="no (cites AAMC EPAs, Core Competencies, and VSLO for competencies/admissions — not AI principles)")
add("raw/us-med-schools/rosalind-franklin--library-ai-guide.md",
    "Rosalind Franklin University (Library)", "guidance", applies_to="faculty;students",
    permitted_uses="Research tools listed: Consensus (search engine for scientific research), Elicit.org (scholarly literature from research questions).",
    secure_tools_named="Consensus;Elicit.org (library-listed research tools)")
add("raw/us-med-schools/rosalind-franklin-cms--policies.md",
    "Rosalind Franklin University Chicago Medical School", "guidance", applies_to="students")
add("raw/us-med-schools/rush--cte-faculty-guide-to-ai.md",
    "Rush University (Center for Teaching Excellence and Innovation)", "guidance",
    applies_to="faculty;students",
    permitted_uses="Educators should design AI-enabled activities that encourage student engagement, critical thinking, and creativity; set clear policies on whether AI tool use is permitted for assignments.",
    disclosure_rule="Require your students to declare their use of AI sources with an AI Use Disclosure (or other statement) that describes which tool they used and how they used it; include even if only used for brainstorming; cite the specific AI-generated content used.",
    assessment_rule="With AI detection proving to be unreliable, instructors should design assignments that ensure authentic assessments that mitigate (or incorporate) AI use, focusing on higher-order thinking skills.",
    secure_tools_named="ChatGPT (named as text AI example)")
add("raw/us-med-schools/rush--library-guide-ai-resources-for-students.md",
    "Rush University (Library)", "guidance", applies_to="students",
    banned_uses="If you are trying to find a reference provided by ChatGPT, be aware that it may not exist.",
    assessment_rule="Students must be informed of AI course policies and under what circumstances they might responsibly use generative AI; for students in clinical situations or at off-site clinical locations, refer to the location's policy on AI use for clinical work.",
    enforcement="Any student's failure to comply with the statement on the use of generative AI tools in a course syllabus is considered a violation of academic integrity and subject to the same penalties stated in Rush University's Student Code of Conduct Policy (UAC0030) and the Academic Honesty Policy (UAC0031).")
add("raw/us-med-schools/rush--library-guide-rush-ai-policy.md",
    "Rush University (Library)", "guidance", applies_to="students;faculty",
    permitted_uses="Policy UAC0039 Generative Artificial Intelligence Use at Rush University addresses the use of generative AI tools in academic and clinical courses, to uphold Rush's reputation of academic excellence and integrity.",
    enforcement="University Policy UAC0039 Generative Artificial Intelligence Use at Rush University (Category: Student and Academic).")
add("raw/us-med-schools/shsu-com--medical-ai-institute.md",
    "Sam Houston State University College of Osteopathic Medicine", "curricular", applies_to="institution",
    permitted_uses="Medical Artificial Intelligence Institute brings together clinicians, researchers, educators, and industry leaders to shape how AI improves healthcare delivery, medical training, and patient outcomes, leveraging SHSU-COM's clinical education and GME network across Texas.")
add("raw/us-med-schools/shsu-com--student-handbook.md",
    "Sam Houston State University College of Osteopathic Medicine", "handbook section", applies_to="students",
    banned_uses="(no AI-specific provisions in captured text; exam-integrity and honor-code rules apply, e.g., recording or sharing examination questions is considered academic dishonesty)",
    phi_rule="Students receive HIPAA, OSHA, and Bloodborne Pathogen training during orientation; students must complete additional training (HIPAA, lab safety, biosafety) when appropriate (general conduct standard, not AI-specific).",
    enforcement="Academic Honor Code per SHSU Academic Policy Statement 810213; SPAP committee may invoke disciplinary measures up to and including dismissal; COCA-accredited program.")
add("raw/us-med-schools/slu--academic-integrity-policy.pdf.md",
    "Saint Louis University", "formal policy", effective_date="version 3.1 effective 2026-08-19 (amended by UADD 2026-04-09)",
    applies_to="undergraduate and graduate students (except courses delivered by the School of Law, the School of Medicine, the Center for Advanced Dentistry Education, and the Madrid campus)",
    banned_uses="Using assistance, notes, aids, artificial intelligence or other technology, cell phones, calculators, translation software, or internet-based applications not authorized by the instructor in taking quizzes or examinations or to complete assignments.",
    permitted_uses="Thoughts, words, or data created by another source other than the student are permitted only when explicitly permitted by the instructor.",
    disclosure_rule="Students practice academic integrity by acknowledging the source of information whether taken from another person, artificial intelligence, or other technology.",
    assessment_rule="Academic integrity is the foundation of the academic assessment process; violations include copying from another student's examination or work and acquiring or disseminating any academic form of assessment without prior approval.",
    enforcement="Minimum standards for reporting and adjudicating violations; Faculty-Guided Resolution or Academic Hearing Panel; sanctions may include a lowered, failing, or zero grade on the examination or assignment.")
add("raw/us-med-schools/slu--complete-ai-guidelines.md",
    "Saint Louis University (Provost's AI Guidelines)", "guidance", applies_to="students;faculty;staff",
    banned_uses="SLU community members must not input any restricted use data into generative AI tools;must not input confidential data except when permitted by validated contract language and security controls approved by ITS;must not input personal information about SLU employees, students, faculty or other stakeholders except when permitted by ITS-approved controls;prohibited from using generative AI tools to produce malicious content;Unless an instructor includes a clear statement in their syllabus granting permission, the use of generative AI tools to complete an assignment or exam is prohibited;some funding agencies (e.g., NIH, NSF) prohibit using generative AI for peer review;must not hold out any output generated by generative AI tools as their own",
    permitted_uses="When permitted by the instructor, students are encouraged to acknowledge and properly cite any use of AI applications; instructors encouraged to insert a syllabus statement regarding GAI; training on effective, ethical and legal use of AI expected before using tools that implicate policy considerations.",
    phi_rule="Privacy and data security: AI use must comply with SLU data protection policies and relevant laws (e.g., FERPA, HIPAA, GDPR).",
    disclosure_rule="Usage of AI tools in academic work, research, or administrative activities must be clearly disclosed; members who leverage generative AI to produce any written materials or work product must disclose that those materials and work product are based on or derives from the use of generative AI; always be transparent if relying on the output of a generative AI tool.",
    assessment_rule="AI technologies must be assessed for potential biases and actively designed to promote equity; careful consideration should be given when deciding if the use of these tools is appropriate for assessing student work; instructors should not inappropriately employ GAI in formative and summative assessment of student learning.",
    enforcement="Unauthorized use of AI will be treated similarly to unauthorized assistance and/or plagiarism; AI systems used in critical administrative functions such as admissions and hiring must be regularly audited for fairness and accuracy; SLU Madrid requires approval from the data protection officer.")
add("raw/us-med-schools/temple-katz--ai-task-force.md",
    "Temple University Lewis Katz School of Medicine", "guidance", applies_to="faculty;staff;students",
    permitted_uses="Katz AI Task Force with six specialized subcommittees (Curriculum/Education and Faculty AI Training; Compliance, Risk, and Ethics; etc.); will align with the University and Temple Health AI task forces for a coordinated enterprise-level approach.",
    disclosure_rule="Task force will guide development of an AI resource section for the Katz Portal providing updates, guidance, and communication materials, helping to ensure transparency and clear communication.")
add("raw/us-med-schools/touro-tuncom--libguide-ai-in-medical-education.md",
    "Touro University Nevada College of Osteopathic Medicine (LibGuide)", "guidance", applies_to="students",
    enforcement="The Touro University System (TUS) Academic Integrity Policy defines plagiarism, cheating, and other unethical conduct, including in the context of use of AI.")
add("raw/us-med-schools/touro-university--academic-integrity-ai-addendum.md",
    "Touro University System", "formal policy", effective_date="effective 2026-01-01 (syllabus statements required)",
    applies_to="students;faculty;staff",
    banned_uses="Use of AI-generated text or output to write, complete, or substantially develop any portion of a graded assessment is not permitted (default rule absent explicit instructor statement);Use of agentic AI tools, which are AI systems that generate text or outcomes with minimal human direction or oversight, is prohibited for all graded assessments;Use of non-approved AI platforms is prohibited on TUS machines;AI tools may not be used to deceive, manipulate, or harm others",
    permitted_uses="Touro University encourages the responsible use of AI tools to enhance learning and research; use of generative AI tools is permitted for pre-task support activities; permitted for grammar correction and language editing; instructors may permit unrestricted AI usage, limited AI usage, or ban AI use for specified assignments.",
    phi_rule="Only AI tools approved by the university (which are available through the TouroOne Portal) are to be used when working with confidential or personally identifiable information (PII).",
    disclosure_rule="Any use of AI tools in student work must be acknowledged; if a student uses AI and does not acknowledge said use, regardless of any statements made or not made in the syllabus, it is considered plagiarism and subject to disciplinary proceedings and sanctions.",
    assessment_rule="Instructor Autonomy: at their discretion, instructors may permit unrestricted AI usage, limited AI usage, or ban AI use for specified assignments and graded assessments.",
    secure_tools_named="University-approved AI tools via TouroOne Portal;Copilot;ChatGPT (in acknowledgement/citation examples)",
    enforcement="Violations fall under the broader TUS Academic Integrity Policy and may result in sanctions up to and including expulsion; use of non-approved platforms may result in academic, legal, or disciplinary consequences; students using non-approved platforms assume full responsibility for any academic, legal, or ethical consequences.")
add("raw/us-med-schools/touro-university--ai-policy.md",
    "Touro University", "guidance", applies_to="students;faculty;staff",
    enforcement="Formal policy framework still in development; existing Touro academic integrity policies now include guidelines related to responsible student and faculty use of AI tools.")
add("raw/us-med-schools/ttuhsc--artificial-intelligence-use.md",
    "Texas Tech University Health Sciences Center", "formal policy", applies_to="students;faculty;staff",
    banned_uses="Until formal approval is confirmed, AI tools must not be used with protected or confidential information without prior review.",
    permitted_uses="TTUHSC OP 52.21 Acceptable Use of AI Tools: AI tools may be used when appropriate and in compliance with institutional policy; approved AI tools that meet institutional privacy and security standards currently under evaluation.",
    phi_rule="Compliance page poses \"Can I enter patient information into an AI tool?\" among key FAQs under OP 52.21.",
    assessment_rule="Cross-functional committee approves AI policies, reviews and assesses AI tools and associated risks, monitors performance and compliance, evaluates vendors, oversees training, and addresses reported concerns.",
    enforcement="TTUHSC OP 52.21 Acceptable Use of AI Tools; cross-functional AI committee oversight; required AI training course and quiz.")
add("raw/us-med-schools/tufts-university--it-guidelines-use-genai-tools.md",
    "Tufts University Technology Services", "guidance", applies_to="faculty;staff;students",
    banned_uses="Faculty and staff must not use unapproved AI tools for Tufts business, instruction, research, or administration without review and approval, especially when institutional data is involved.",
    permitted_uses="When available, faculty, staff, and students should use AI tools that are approved, licensed, or supported by Tufts (reviewed for privacy and data protection, security and compliance, accessibility, contractual and licensing terms).",
    phi_rule="AI use must comply with all applicable laws and regulations, including but not limited to: FERPA, HIPAA, Research and human-subjects protections, Copyright and intellectual property laws, Accessibility requirements. Special care is required when AI is used in clinical, research, or student-facing contexts.",
    disclosure_rule="Users should be aware of whether vendor terms allow training or fine-tuning on user inputs, which may conflict with Tufts policies or legal obligations if not reviewed.",
    enforcement="Guidance grounded in Tufts values, academic integrity, data stewardship, and respect for privacy; students should understand that using AI tools does not transfer ownership, authorship, or responsibility.")
add("raw/us-med-schools/u-arizona--ai-guidelines-and-principles.md",
    "University of Arizona", "guidance", applies_to="students;faculty",
    banned_uses="Using AI without permission may violate the Code of Academic Integrity and could be treated as academic misconduct.",
    permitted_uses="No single university-wide policy specific to AI; instructors encouraged to set clear expectations; sample syllabus language based on a Red-Yellow-Green model (AI prohibited, allowed with permission, or actively encouraged); College of Medicine (Tucson) Policy on Student Use of AI listed among localized approaches.",
    disclosure_rule="For instructors: To support transparency and fairness, clearly communicate your expectations for AI use in your syllabus.",
    enforcement="Use of generative AI tools in coursework is guided by the Code of Academic Integrity, which prohibits all forms of academic dishonesty.")
add("raw/us-med-schools/u-arizona-phoenix--ai-use-by-students-policy.md",
    "University of Arizona College of Medicine - Phoenix", "formal policy", applies_to="students",
    banned_uses="Unless explicitly permitted by a course director, any use of generative AI for an assessment or assignment is prohibited;AI tools may not be used to write histories, perform physical exams, or create assessments and plans for patient care in the foundational and clinical phases of the curriculum;AI tools that do not meet HIPAA standards must not be used for processing or storing any form of PHI;AI should not be used in direct patient interactions unless authorized by supervising faculty",
    permitted_uses="AI may be used for educational purposes, such as studying, researching medical literature, and understanding complex topics; students are strongly encouraged to only use AI tools that allow users to opt out of having submitted data used for the system's own training.",
    phi_rule="Students must ensure that PHI is only used with approved AI systems and shared in a secure manner; AI tools used for clinical documentation must be certified as HIPAA-compliant; the user is responsible for ensuring clinical use of AI is compliant with HIPAA regulations.",
    disclosure_rule="Students must be transparent about AI usage and accountable for their work; any use of AI tools in assignments, research, clinical documentation, or other academic work must be clearly cited according to institutional guidelines; students must describe the nature and extent of AI assistance.",
    assessment_rule="All student contributions to any assessment or assignment must represent the student's own, original work.",
    secure_tools_named="ChatGPT;Claude;OpenEvidence (named as examples)",
    enforcement="Any suspected or evident violations of AI use can be considered a potential professionalism report or honor code violation (Honor Code Committee and Procedures and Process for Dismissal).")
add("raw/us-med-schools/u-arizona-tucson--policy-on-student-use-of-ai.pdf.md",
    "University of Arizona College of Medicine - Tucson", "formal policy", effective_date="2024-11-13",
    applies_to="students (all phases of the MD program)",
    banned_uses="AI tools may not be used for writing History and Physicals (H&Ps) in the Doctor & Patient Course;Assessments and assignments: all student contributions must represent the student's own, original work.",
    phi_rule="Any use of AI for clinical documentation must adhere to the policies and guidelines of the clinical site and comply with HIPAA regulations to ensure the confidentiality and security of patient information; students must ensure that protected health information (PHI) is only used with approved AI systems and shared in a secure manner.",
    permitted_uses="AI tools may be used for other tasks, such as researching clinical questions; where available, students must opt out of having the data they submit to generative AI systems be used for the system's own training.",
    disclosure_rule="Students must be transparent about AI usage and accountable for their work; any use of AI tools in assignments, research, clinical documentation, or other academic work must be clearly cited according to institutional guidelines; students must describe the nature and extent of AI assistance.",
    enforcement="Faculty and administrative staff will monitor compliance with this policy; plagiarism detection tools may be used to verify originality in student work; violations of the policy will be subject to disciplinary actions per the Honor Code Policy.")
add("raw/us-med-schools/u-oklahoma--ai-at-ou.md",
    "University of Oklahoma Information Technology", "guidance", effective_date="updated 2026-08-05",
    applies_to="students;faculty;staff",
    permitted_uses="Microsoft Copilot for Web available to OU faculty and staff; LiteLLM AI Sandbox infrastructure; AI-assisted Grading (grouping similar answers); Gradescope assessment tool.",
    disclosure_rule="As we continue to investigate the ability of AI features for our IT services, we are committed to providing transparent, user-friendly explanations and guidance.",
    assessment_rule="AI-assisted Grading allows instructors to automatically group similar answers and grade all the answers in each group at once; Gradescope is a feedback and assessment tool with dynamic rubrics.",
    secure_tools_named="Microsoft Copilot for Web (organizational data protection);LiteLLM;LibreChat (Libraries AI Sandbox Pilot);ChatGPT;ClaudeAI (exploration);Zoom AI meeting features",
    enforcement="View the Acceptable Use Policy for University Data.")
add("raw/us-med-schools/u-oklahoma--ai-policies.md",
    "University of Oklahoma (Center for Faculty Excellence)", "guidance", effective_date="updated 2026-03-06",
    applies_to="faculty;students;staff",
    permitted_uses="OU's AI policies support responsible, ethical, and transparent use of AI across teaching, research, and operations: AI Administrative and Operational Guidance for Staff and Employees; AI Guidance for Students; AI Governance Policies; AI Teaching Guidance for Faculty; AI Research Guidance; Chief AI Officer's AI Roadmap.")
add("raw/us-med-schools/u-rochester--libguide-ai-ethics-policy.md",
    "University of Rochester Medical Center (LibGuide)", "guidance", applies_to="students;faculty",
    permitted_uses="AS&E encourages instructors to adopt ChatGPT/AI only after they consider (a) how the tools support course learning goals, and (b) how they can create alternative assignment options for students who want to avoid uploading their personal details and/or intellectual property into these platforms.",
    disclosure_rule="Detection is complicated, encouraging disclosure is recommended; when content of a publication has been impacted (even in the absence of using AI-generated text), this should be disclosed.")
add("raw/us-med-schools/u-rochester--responsible-use-ai-tools-data-security.md",
    "University of Rochester Office of the Provost", "guidance", applies_to="faculty;staff;students",
    banned_uses="It is imperative to remember that non-public or sensitive University information should never be uploaded into external AI tools-whether free or paid-unless there is a university agreement with the vendor approved by one of the various AI governance groups.",
    permitted_uses="Take advantage of our secure version of a generative AI chatbot, designed to securely handle medium- and high-risk institutional data.",
    secure_tools_named="chat.rochester.edu (secure university chatbot, exclusively for faculty, staff, and students)")
add("raw/us-med-schools/uc-davis--md-program-acceptable-use-genai-coursework.md",
    "UC Davis School of Medicine", "formal policy", effective_date="enacted 2026-04; annual review cycle",
    applies_to="students (MD)",
    banned_uses="GenAI may not be used to directly author any portion of a submitted assignment unless faculty or course leadership grants written permission;Students are prohibited from using GenAI tools to research or generate answers for closed-book assessments unless faculty or course leadership grants written permission;Students are not permitted to use external GenAI tools to generate patient care documentation, including notes, assessments, or care plans, except as outlined in the UC Davis Health Generative AI Services and Application Use Policy",
    permitted_uses="Where the use of GenAI is permitted, the acceptable use of AI tools in a course is stated in the course syllabus or assignment instructions;only AI functionalities explicitly supported by the EHR, authorized by course leadership, and in strict adherence with University of California Health policies, may be used;where allowed for scholarly work, students must comply with GenAI disclosure requirements established by journals, conferences, or professional organizations",
    phi_rule="Under no circumstances should PHI be entered into any generative AI tool outside of a secure, institutionally supported system.",
    disclosure_rule="Any use of GenAI tools must be transparently disclosed, including the type of tool used and the nature of its contribution.",
    assessment_rule="Faculty may choose to limit students' ability to upload, copy, or input the School's curricular materials (slides, articles, assignments, examinations, proprietary instructional content) into GenAI or similar platforms.",
    enforcement="Violations of this policy constitute breaches of the Code of Academic Conduct and professionalism and will be addressed according to the School's procedures, including referrals to the Honor and Professionalism Council, the Committee on Student Promotions (CSP), and the Associate Dean for Students; consequences may result in remediation or disciplinary actions, including course failure and/or dismissal.")
add("raw/us-med-schools/uc-irvine--dtei-generative-ai-for-teaching-learning.md",
    "UC Irvine Division of Teaching Excellence and Innovation", "guidance", applies_to="faculty;students",
    permitted_uses="DTEI events, panels, and pitch competitions on leveraging generative AI in teaching and learning; video on using AI productively and responsibly at UC Irvine.")
add("raw/us-med-schools/uc-san-diego--academic-integrity-gen-ai.md",
    "UC San Diego Academic Integrity Office", "guidance", applies_to="faculty;students",
    permitted_uses="Critical AI Literacy Canvas Module (adapted from Rush University CTEI) covering Recognition, Comprehension, Critical thinking, Proficiency; guidance on redesigning assessments for the age of AI.",
    assessment_rule="How do I redesign assessments for the age of AI?; what can I do differently with grading to minimize the harms and maximize the benefits of GenAI; instructors may falsely believe AI detectors are valid and accurate.",
    secure_tools_named="ChatGPT;Claude;Grammarly (named as examples)")
add("raw/us-med-schools/uc-san-diego--libguide-ai-and-academic-integrity.md",
    "UC San Diego Library", "guidance", applies_to="students;faculty;staff",
    permitted_uses="UC San Diego is building an AI-enabled campus where students, faculty, and staff can confidently leverage trusted, secure, and responsible AI tools to enhance research, improve operations, and expand educational opportunities.",
    enforcement="UCSD Policy on Integrity of Scholarship; Academic Integrity Office Statement of Artificial Intelligence.")
add("raw/us-med-schools/uc-san-diego--privacy-guidelines-for-uses-of-ai-assistants.md",
    "UC San Diego (Campus Privacy Office)", "formal policy", applies_to="students;faculty;staff",
    banned_uses="P-4 data and sensitive P-3 data may not be discussed while AI features are enabled or the Meeting is being Captured;Individuals may not \"send\" an AI assistant to \"attend\" a Meeting on their behalf when the individual is not also present;Output of Captured Meetings may not be saved on personal devices or in personal accounts and must only be stored on university-approved services;hosts must remove AI assistants or stop Capture where an attendee objects or where Capturing is Prohibited or restricted",
    permitted_uses="Individuals may only use AI Assistants that have been reviewed for privacy and security by the Campus Privacy Office and the Office of Information Assurance and are covered by a written agreement (Appendix DS, Appendix GDPR) executed by an authorized central contract officer;Capturing of Classes using approved tools allowed for documented disability accommodations and by instructors where students and attendees have been notified prior to the Class",
    phi_rule="Use of AI assistant features is prohibited for Meetings where identifiable human subjects research is discussed, except where the use of AI is part of the research project or there are approvals from the Campus Privacy Office and the IRB.",
    disclosure_rule="A Meaningful Opportunity to Object exists where participants had advance notice the Meeting would be Captured and given the opportunity to object, or are given the opportunity at the start; use of AI assistant systems must be disclosed in the IRB protocol.",
    assessment_rule="Individuals are advised to use extreme caution when Capturing Educational Meetings where other P-3 personal or confidential information (e.g., research planning, assessments) is discussed; instructors should not Capture office hours where integrity issues are discussed.",
    enforcement="Instructors may remove unauthorized or unknown AI Assistants from Educational Meetings/Classes; a student's refusal to participate in a Meeting with AI features enabled should not be the subject of an adverse action.")
add("raw/us-med-schools/uc-san-diego--senate-admin-workgroup-genai-education-report.pdf.md",
    "UC San Diego (Senate-Admin Workgroup on GenAI in Education)", "guidance",
    effective_date="2024-08-23 (final report)", applies_to="faculty;students",
    banned_uses="Students must not offload their thinking and doing to machines unless they were expected to do so by the course instructor and/or are transparent about their use.",
    permitted_uses="Course policies should specify which GenAI uses are allowed (brainstorming, grammar checking, research assistance) and which are prohibited (completing assignments without personal engagement); recommends AI literacy education, university-provided tools, and research on GenAI effectiveness.",
    phi_rule="Any tool(s) adopted by the University or used by students/instructors must protect private data (P3 & P4 levels) and preferably not share any of our data with the vendor for training purposes.",
    disclosure_rule="Instructors should establish clear and transparent guidelines on the acceptable and unacceptable uses of GenAI tools in their class, as well as if they are using artificial intelligence in student feedback or grading.",
    assessment_rule="Protect the Integrity of Academic Assessments: no single, uniform policy recommended for all of campus; instructors should craft policies per course; existing unproctored online exams are vulnerable.",
    enforcement="Academic Senate's Academic Integrity Policy states that instructors must report all suspected integrity violations to the Academic Integrity Office.")
add("raw/us-med-schools/uconn--cetl-generative-ai.md",
    "University of Connecticut (Center for Excellence in Teaching and Learning)", "guidance",
    applies_to="faculty;students",
    permitted_uses="UConn has a contract with Microsoft for basic access to Copilot; due to protections, it is recommended, though not required, that you use Copilot.",
    disclosure_rule="You may also want to tell students whether and how you use generative AI yourself, in designing the course, developing materials, giving feedback, assessing work, or communicating with them.",
    enforcement="AI use is governed by the Data Classification Policy, the Academic, Scholarly, and Professional Integrity and Misconduct Policy, and FERPA; consult the UConn Office of Community Standards and the university's academic misconduct policy for handling plagiarism and cheating.",
    secure_tools_named="Copilot (UConn Microsoft contract, recommended);ChatGPT;Gemini;Llama;Claude;Grammarly;Midjourney;Dall-E (named as examples)")
add("raw/us-med-schools/uconn-health--ai-guidance-v20240314.pdf.md",
    "UConn / UConn Health (IT Security)", "guidance", effective_date="2024-03-14 (Ver 3/14/2024)",
    applies_to="students;faculty;staff",
    banned_uses="Allowable vs NOT ALLOWED uses per the Data Classification Policy (classification matrix in guidance).",
    permitted_uses="UConn and UConn Health are committed to using AI responsibly, transparently, and ethically across its domains.",
    secure_tools_named="ChatGPT (named as the popularized model)")
add("raw/us-med-schools/uconn-health--guidance-on-using-ai.md",
    "UConn Health (Academic IT & Systems)", "guidance", applies_to="faculty;staff;students",
    permitted_uses="Guidance page on using AI at UConn Health, updated frequently as the technology evolves.")
add("raw/us-med-schools/umass-chan--clinical-learning-environment-genai-policy.pdf.md",
    "UMass Chan Medical School", "formal policy", effective_date="clinical GenAI policy v2 draft (approval fields blank in captured template)",
    applies_to="students (SOM, clinical learning environment)",
    banned_uses="Submitting GenAI-generated work as original content without modification and attribution;Using GenAI to generate differential diagnoses or management plans de novo;Use of ambient scribes (e.g., Nuance DAX/Microsoft Dragon Copilot, Doximity) is prohibited unless permission is granted from the course director;GenAI (such as AI scribes) should not be used to create summaries of meetings as this can contain PHI/PII",
    permitted_uses="Allowed uses: Outlining; Summarizing Documents (treated as preliminary resource); Editing and Proofreading; Supplementary Learning (explanations, study questions);GenAI-powered natural language consultation tools for evidence-based clinical queries (OpenEvidence, UpToDate) with citation of its use;GenAI features embedded within institutionally provided platforms when functionality is not optional;copyrighted educational materials only within institutionally approved LLM platforms such as UMass Chan AI Commons",
    phi_rule="Use of PHI/PII in publicly available GenAI tools is not permitted due to risk for data compromise; PHI/PII may only be used in GenAI tools that are approved by the medical school or clinical system for such use.",
    disclosure_rule="Attribution Requirements: Any use of GenAI tools must be clearly disclosed in the submitted work.",
    assessment_rule="GenAI cannot replace core cognitive work, but rather can support, augment, or reinforce learning; when GenAI output influences clinical judgment, students must review conclusions with their supervising clinician; uses not described in the policy require course director permission.",
    secure_tools_named="UMass Chan AI Commons (private GenAI tools);OpenEvidence;UpToDate;Nuance DAX/Microsoft Dragon Copilot;Doximity (ambient scribes named in prohibition)",
    enforcement="Violations subject to the School of Medicine Honor Code, Technical Standards and/or Professionalism guidelines and policies, as well as sanctions from the relevant clinical system.")
add("raw/us-med-schools/umass-chan--faculty-council-ai-policy-update.pdf.md",
    "UMass Chan Medical School (Faculty Council)", "guidance", effective_date="2026-05-07",
    applies_to="faculty",
    permitted_uses="University AI policy draft in review by Scientific Council and Academic mission (GSBS, Med Ed, Nursing School) faculty; final draft to be approved by Executive Council and the Provost before signing.")
add("raw/us-med-schools/unm--ai-appropriate-use-and-guidelines.md",
    "University of New Mexico", "guidance", applies_to="students;faculty;staff",
    permitted_uses="Various UNM policies describe appropriate and inappropriate use of technology and the offices and processes through which permission must be requested to use UNM Data with any technology, including AI technology - even if there is no cost.",
    phi_rule="Before using identifiable FERPA data in AI platforms, users should contact their office's/department's IT Officer to initiate a risk assessment; Before using data subject to HIPAA regulations in AI platforms, please reach out to the HIPAA Privacy Office.",
    enforcement="Students should comply with the UNM Student Code of Conduct (Pathfinder), Faculty Handbook policy on Dishonesty in Academic matters, and any instructor syllabus guidance clarifying expectations for technology use in completing academic work.")
add("raw/us-med-schools/unm--faculty-senate-policy-use-of-genai.md",
    "University of New Mexico Faculty Senate", "formal policy",
    applies_to="faculty;students (teaching, research, service)",
    banned_uses="Since AI systems cannot meet ICMJE authorship criteria, they may not be credited as co-authors or contributors;Inputting confidential manuscript content into public AI platforms (such as ChatGPT) is strictly prohibited and constitutes a breach of ethical review practice.",
    permitted_uses="Authors may utilize generative AI tools such as ChatGPT, Grammarly, DeepL, or other large language models (LLMs) to assist in language editing, grammar correction, reference formatting, or data presentation, provided that such use does not replace the intellectual and scholarly contribution of the authors themselves.",
    disclosure_rule="Any use of generative AI tools in the preparation of a manuscript must be clearly and fully disclosed in the Acknowledgments section; be transparent regarding AI use in research methods or acknowledgements.",
    assessment_rule="All assessments must be conducted independently by qualified human experts.",
    enforcement="Undisclosed or inappropriate use of AI tools will be handled in accordance with the COPE flowcharts for ethical misconduct; editorial team may use specialized tools to detect excessive or unethical reliance on AI-generated content.")
add("raw/us-med-schools/unm--libguide-ai-in-health-sciences.md",
    "University of New Mexico Health Sciences Library", "guidance", applies_to="students;faculty",
    effective_date="last updated 2026-08-20")
add("raw/us-med-schools/unmc--ai-use-guidelines.md",
    "University of Nebraska Medical Center", "formal policy", applies_to="students;faculty;staff",
    banned_uses="UNMC employees and students are expected to not enter confidential, proprietary, or patient-related information that is subject to federal or state regulations or otherwise considered sensitive or restricted;Federal funding agencies prohibit the use of AI tools during the peer-review process",
    permitted_uses="Only public or Low Risk Data may be used with AI tools-unless a legal enterprise agreement and confidentiality agreement have been established and the required assessment process completed, or the tool is listed on the UNMC Approved Technology List;faculty and instructors can choose to prohibit, allow with attribution, or encourage use of generative AI tools",
    phi_rule="Patient data may not be used within AI tools.",
    disclosure_rule="If you are permitted to use generative AI tools, you may be required to disclose your use and cite the tools you used; at a minimum, when you use generative AI output in scholarly works, disclose and describe how you used it and identify the sections that include generative AI output.",
    assessment_rule="Any new solution involving AI-or any addition of AI to an existing solution-must go through the risk assessment process, as outlined in UNMC/Nebraska Medicine IM #63: Risk Assessment Policy.",
    secure_tools_named="UNMC Approved Technology List",
    enforcement="These guidelines are enforced through the UNMC Code of Conduct, Student Code of Conduct, and Research Integrity Policy; misuse of generative AI will be subject to the same policies and procedures as other academic misconduct.")
add("raw/us-med-schools/ut-austin--guidance-for-using-artificial-intelligence.md",
    "University of Texas at Austin (Enterprise Technology)", "guidance",
    applies_to="students;faculty;staff",
    banned_uses="AI tools without a University contract and proper data-sharing controls are not approved for use with controlled or confidential information.",
    permitted_uses="Responsible use of AI tools includes adhering to relevant policies that protect confidential, personal, and proprietary data; check the Approved AI Tools Decision Matrix before using any AI tool with University data; employees are encouraged to explore AI tools to enhance productivity.",
    disclosure_rule="Fair & Transparent: ensuring fairness, transparency, and alignment with the institution's mission, while maintaining clarity and openness about AI usage.",
    enforcement="In all cases, use of AI tools must be consistent with the Information Resources Use and Security Policy and, for students, the Acceptable Use Policy and Student Standards of Conduct; cross-organizational AI working group develops policies, standards, and guidelines.")
add("raw/us-med-schools/vcu--understanding-genai-policy-ico-blog.md",
    "Virginia Commonwealth University (ICO blog)", "guidance",
    effective_date="2026-03-13 (policy adopted 2025-11-12)", applies_to="students;faculty;staff",
    banned_uses="Using AI tools in ways that are dishonest, or misrepresent student effort, is considered academic misconduct.",
    permitted_uses="VCU's Acceptable Use of Generative AI Technology policy (adopted November 12, 2025) sets baseline boundaries: protects confidential and sensitive information, supports academic and research integrity, ensures compliance with regulations, fosters digital literacy; faculty are encouraged to provide clear guidance in syllabi.",
    phi_rule="Users do not enter confidential or sensitive data-such as personal student records, research data, financial or health information-into GenAI tools unless the tool has been approved for that level of data; content entered into public models can interfere with regulations like FERPA, HIPAA and institutional data classification standards.",
    disclosure_rule="Students must remain accountable for the content they submit, and any AI-assisted work should be verified for accuracy and properly attributed.",
    secure_tools_named="Google Gemini;Microsoft Copilot;Adobe Firefly (tools in use at VCU)")
add("raw/us-med-schools/wake-forest--ai-guidelines-for-academic-use.md",
    "Wake Forest University", "guidance", effective_date="AI Working Group report delivered March 2025",
    applies_to="faculty;students",
    banned_uses="Example definition of academic misconduct: The unauthorized use of generative AI platforms by a student, whether in the classroom, laboratory, studio, intern- and externships, independent research settings, or other spaces identified as serving educational goals.",
    permitted_uses="Instructors and students share responsibility for communicating about GAI use; permitted uses of GAI may differ by course and assignment and may change over time; any instructor whose course explicitly includes GAI tools must ensure all students have access.",
    disclosure_rule="To substantiate academic misconduct, instructional materials need to include directions regarding the authorized use of GAI, including method(s) for disclosing or citing such use; when and how GAI tools can be used, along with when and how such use should be acknowledged.",
    assessment_rule="Evidentiary standards for academic misconduct should not allow for AI detectors alone to constitute a sufficient standard of proof; GAI may impact learning contexts and assessments in ways that require new structures for producing authentic student work.",
    enforcement="The absence of GAI guidance in a course undermines the ability to recognize and adjudicate instances of academic misconduct; the College and each school should ensure existing judicial frameworks and academic honor codes adequately address academic misconduct with GAI.")
add("raw/us-med-schools/wake-forest-som--md-student-handbook.pdf.md",
    "Wake Forest University School of Medicine", "handbook section", effective_date="2024-2025 (CO 2024-2025)",
    applies_to="students (MD)",
    phi_rule="Maintain the confidentiality and security of patient information (professionalism standard; students also prohibited from recording sessions where content is inappropriate for recording due to patient privacy or relation to actual assessment questions).",
    aamc_alignment="no (introduces students to AAMC's Careers in Medicine resource — not AI principles)")
add("raw/us-med-schools/wake-forest-som--policy-compliance-companion.pdf.md",
    "Wake Forest University School of Medicine", "handbook section", effective_date="2026-2027",
    applies_to="students",
    banned_uses="Prohibited-use example: [Use that] discloses student records; protected health information (PHI); information about faculty, peers or School of Medicine staff; or clinical documentation, site details, or simulation content.",
    permitted_uses="Examples of Acceptable Use: (1) Grammar and spelling suggestions; students must ensure all submitted academic and clinical work reflects personal understanding and learning.",
    phi_rule="Compliant [use]: Adheres to privacy and regulatory standards, including the Family Educational Rights and Privacy Act (FERPA) and the Health Insurance Portability and Accountability Act (HIPAA).",
    enforcement="HIPAA Privacy and Security Sanctions Policy (Enterprise) provides guidance on applying consistent sanctions for a HIPAA violation, used in conjunction with Human Resources Corrective Action policy.",
    aamc_alignment="no (MSPE released in alignment with AAMC/ERAS timeline — not AI principles)")
add("raw/us-med-schools/wayne-state-som--md-handbook-ai-guidelines-usage-policy-announcement.md",
    "Wayne State University School of Medicine", "guidance", applies_to="students (MD)",
    banned_uses="Clarifies when AI may be used as a learning tool and when its use is not permitted (MD Handbook AI Guidelines and Usage Policy update).",
    enforcement="Policy update emphasizes ethical considerations and academic integrity.")
add("raw/us-med-schools/wvsom--ai-for-students.md",
    "West Virginia School of Osteopathic Medicine", "guidance", applies_to="students;faculty;staff",
    permitted_uses="Numerous ways to use generative AI tools without submitting university data or intellectual property: syllabus and lesson planning, correspondence when no student or employee information is provided (fake information permitted for drafts using general queries).",
    disclosure_rule="AI Use Disclosure (Recommended): a short statement in your paper, e.g., \"I used Microsoft Copilot to assist in drafting and refining this paper\", including the prompt used and a note that content was reviewed and edited; verify any factual information generated by an AI tool and reference the tool as you would any other source.",
    secure_tools_named="Microsoft 365 Copilot (WVSOM's preferred GenAI tool, covered by commercial data protection; WVSOM username/login required);ChatGPT",
    enforcement="Students should use generative AI in ways that align with university academic integrity policies and communicate with their instructors before using generative AI in their coursework.")
add("raw/us-med-schools/wvsom--ai-potential-misuse-data-sharing.md",
    "West Virginia School of Osteopathic Medicine", "guidance", applies_to="students;faculty;staff",
    banned_uses="No institutional data submitted to generative AI services without approval; when you provide information to non-approved tools (queries, student essays, grant proposals, source code, datasets), it is the same as posting information on a public website.",
    permitted_uses="WVSOM encourages the use of generative AI services, as long as no institutional data is submitted to them without approval; Currently, Microsoft 365 Copilot is the only generative AI permitted.",
    enforcement="Any other system used for official institutional data or information will need to go through review to ensure the necessary contracts and safeguards are in place to protect the data submitted and to ensure the algorithms in use are ethical, transparent and beneficial.")
add("raw/us-med-schools/wvsom--ai-procedures-and-guidance.md",
    "West Virginia School of Osteopathic Medicine", "guidance", applies_to="students;faculty;staff",
    banned_uses="Prohibited uses include transcribing meetings where the content is highly confidential or sensitive, and the risk of data breaches or inaccuracies is significant; relying on AI generated information in a legal context can lead to serious consequences and may put WVSOM at risk of liability.",
    permitted_uses="Acceptable uses of AI in any material distributed as part of an approved course include improving efficiency of note taking or study plan formation, helping generate ideas related to the course, providing challenges and platforms for problem solving.",
    phi_rule="At no time should patient or clinical data be used or stored in AI systems (see the WVSOM HIPAA Policy for more information).",
    disclosure_rule="Employ trust and transparency to ensure clarity and openness when employing AI, particularly in areas affecting decision-making or policy development.",
    assessment_rule="Unacceptable use constitutes any use of AI that would bypass learning, provide answers without student engagement or logical reasoning, complete graded assignments without student input, or assist with any summative assessment without course director approval; the course director will designate when it is acceptable to use AI in completion of an assignment or assessment.",
    secure_tools_named="Microsoft 365 Copilot (WVSOM-maintained and secure resource);ChatGPT;Grammarly;Nuance (examples)",
    enforcement="The use of generative AI is subject to all WVSOM policies and procedures, including those associated with academic integrity and professionalism; guidance aligns with Institutional Policy GA-31; students do not currently have a specific academic integrity policy around GenAI.")
add("raw/us-med-schools/wvsom--guidance-on-use-and-access-of-ai.md",
    "West Virginia School of Osteopathic Medicine (IT)", "guidance",
    applies_to="faculty;staff;students",
    banned_uses="Prohibited uses include transcribing meetings where the content is highly confidential or sensitive (e.g., closed-door strategic meetings or sensitive personal information).",
    permitted_uses="Acceptable use of AI in student curriculum: improving efficiency of note taking or study plan formation, helping generate ideas related to the course, providing challenges and platforms for problem solving.",
    phi_rule="Do not use AI when working with sensitive, private, restricted, or confidential information, including personally identifiable and protected health information.",
    disclosure_rule="Employ trust and transparency to ensure clarity and openness when employing AI, particularly in areas affecting decision-making or policy development.",
    assessment_rule="All assignments or assessments without a course-director designation should not have AI used for their completion without prior approval by the course director.",
    secure_tools_named="CoPilot;ChatGPT;Grammarly;Nuance (examples);Microsoft 365 Copilot (WVSOM-maintained secure resource)",
    enforcement="The use of generative AI is subject to all WVSOM policies and procedures, including those associated with academic integrity and professionalism; guidance supports Institutional Policy GA-31, which identifies the acceptable and unacceptable uses of data and technology; reach out to IT for purchase or use of new AI technology not previously approved.")

# ---------------- health-systems (29) ----------------
add("raw/health-systems/advocate-health--nitrd-ai-rfi-response.pdf.md",
    "Advocate Health", "guidance", effective_date="2025 (RFI response)",
    applies_to="institution (incl. GME: 2,000+ residents and fellows across 200+ programs)",
    banned_uses="AI and other similar tools must not serve as a replacement for the judgment of experienced and qualified clinicians.",
    permitted_uses="DAX Copilot allows clinicians to create draft clinical summaries automatically and securely from in-person or telehealth conversations for review and finalizing in the EHR; Epic Inbasket LLM drafts the first draft of a patient message; Enterprise Artificial Intelligence Governance Subcommittee maintains robust AI governance guided by four core principles ensuring AI is equitable and ethical, secure, transparent, and impactful.",
    disclosure_rule="Transparency with patients is of paramount concern as building and maintaining their trust and understanding of new technology is vital; strongly support regulations that ensure transparency from vendors, such as implementing a standardized AI label.",
    assessment_rule="We continue to believe that care decisions must include individualized assessment of each patient's unique context.",
    secure_tools_named="Nuance Dragon Ambient eXperience (DAX) Copilot;Epic Inbasket (LLM patient-message drafts)",
    enforcement="Enterprise Artificial Intelligence Governance Subcommittee (patient safety, health equity, ethics, clinical operations, IT, data science, research, digital innovation) maintains robust AI governance.")
add("raw/health-systems/advocate-health--smart-health-care-ai.md",
    "Advocate Health", "guidance", applies_to="patients (patient-facing info)",
    phi_rule="Your information is protected through strong security measures and compliance with federal and state privacy laws, including HIPAA; your conversation is handled safely and kept secure, just like the rest of your health information; your information is stored in approved, monitored spaces.",
    permitted_uses="During your visit, your provider may use an AI tool that listens to your conversation and captures relevant medical details (hands-free medical documentation), allowing the provider to spend more time one-on-one with you.")
add("raw/health-systems/atrium-wake-forest--smart-health-care-ai.md",
    "Atrium Health Wake Forest Baptist", "guidance", applies_to="patients (patient-facing info)")
add("raw/health-systems/bmc--responsible-ai-statement.md",
    "BMC Software (collected under health-systems; not a health system - likely collector misattribution, not Boston Medical Center)",
    "guidance", applies_to="corporation",
    permitted_uses="BMC has adopted a Generative AI Use Policy to ensure ethical and responsible application of generative technologies; mandatory developer and security personnel training; responsible AI practices training.",
    disclosure_rule="BMC is committed to making AI algorithms and data usage transparent, enabling stakeholders to understand how decisions are made; the AI services in BMC solutions also disclose the limitations of the AI technologies used.",
    assessment_rule="AI Risk Review Teams in each business area assess and manage risks associated with the use of AI technologies and their deployment in BMC solutions.")
add("raw/health-systems/cleveland-clinic--ambience-ai-platform-rollout.md",
    "Cleveland Clinic", "guidance", effective_date="2025-02-19", applies_to="clinicians",
    banned_uses="This AI technology does not diagnose or treat any disease or other medical condition.",
    permitted_uses="AI documentation software records patient appointments and generates comprehensive medical notes; the notes are then reviewed and approved by the provider and uploaded to the patient's medical record.",
    secure_tools_named="Ambience Healthcare AI platform (ambient listening, rollout to outpatient practices)")
add("raw/health-systems/cleveland-clinic--state-of-the-clinic-2025.pdf.md",
    "Cleveland Clinic", "guidance", effective_date="2025 (annual report)", applies_to="clinicians;patients",
    permitted_uses="Ambience Healthcare's AI ambient listening software was deployed to all Cleveland Clinic outpatient practices in 2025, reducing administrative burden for providers and improving communication with patients; phone-based app records clinical visits, documents the exam in the EHR, generates after-visit summaries, and helps with medical coding.",
    secure_tools_named="Ambience Healthcare AI ambient listening software (enterprise outpatient deployment)")
add("raw/health-systems/hartford-healthcare--center-for-ai-innovation-launch.md",
    "Hartford HealthCare", "guidance", effective_date="2024-02-15", applies_to="clinicians;staff",
    permitted_uses="Center for AI Innovation in Healthcare with five foundational elements, including collaboration and partnerships (MIT, University of Oxford, Google Cloud) and education equipping clinical and operational colleagues to leverage AI in a safe, trustworthy manner.")
add("raw/health-systems/hartford-healthcare--innovation-center-for-ai.md",
    "Hartford HealthCare (Innovation)", "guidance", applies_to="clinicians;staff",
    permitted_uses="The innovation space is focused on unlocking the transformative power of artificial intelligence (AI) for our patients in a safe and trustworthy way.")
add("raw/health-systems/howard-u-ai-in-healthcare-center--about.md",
    "Howard University AI in Healthcare Center", "guidance", applies_to="researchers;clinicians",
    permitted_uses="Center made up of AI experts, clinicians, healthcare experts, researchers, and administrators conducting healthcare-related research and operations projects (focusing on people from minority populations) at the intersection of AI, healthcare, and public health.")
add("raw/health-systems/howard-university--about-howard-ai.md",
    "Howard University", "guidance", applies_to="institution",
    permitted_uses="Howard AI initiative spans the Center for Applied Data Science & Analytics (CADSA), Human-Centered AI Institute, Center of Excellence in AI and Machine Learning (CoE-AIML), and Center for Digital Business, educating the next generation of AI leaders and deploying responsible technologies.")
add("raw/health-systems/jefferson-health--bold-ai-strategy.md",
    "Jefferson Health", "guidance", effective_date="2025-09-18", applies_to="clinicians;staff",
    permitted_uses="Enterprise-wide AI strategy under a unified AI Steering Committee (post Lehigh Valley Health Network combination, August 2024) designed to reclaim more than 10 million hours of clinician time by 2028; ambient listening technology already launched for physicians and advanced practice clinicians.",
    disclosure_rule="Building Trust Through Transparency - auditing all AI models for bias, co-designing solutions with key stakeholders, and ensuring human oversight in AI deployment.")
add("raw/health-systems/medstar-georgetown--ai-colab.md",
    "MedStar Health / Georgetown University (AI CoLab)", "guidance",
    applies_to="researchers;trainees",
    permitted_uses="Collaborative center for AI in healthcare: industry collaboration to assess and implement AI, technology transfer, training and education of diverse trainees in AI and ML, AI & Beyond podcast.")
add("raw/health-systems/medstar-health--ai-center-of-excellence.md",
    "MedStar Health", "guidance", applies_to="clinicians;staff",
    permitted_uses="AI Center of Excellence advances strategy, governance, and education to ensure AI is reviewed and adopted responsibly; ambient documentation solutions, predictive early-intervention models, and secure internal platforms for generative AI.",
    disclosure_rule="Transparent: We know how the AI models work and the training data is clear.",
    assessment_rule="Based on risk and impact, the AIRB determines the appropriate level of assessment so that AI technologies are introduced responsibly and consistently across the system, ranging from streamlined review, to deeper analysis, to ongoing monitoring.",
    enforcement="Every AI solution introduced at MedStar Health is evaluated by the multidisciplinary AI Review Board using the TRUSTED framework.")
add("raw/health-systems/meharry-oracle-health--nashville-partnership.md",
    "Meharry Medical College / Oracle Health", "curricular", effective_date="2024-11-29 (news)",
    applies_to="students;residents;clinicians",
    permitted_uses="Partnership to tackle health inequities in Nashville: community care and wellness center where medical students, residents, and professionals access Oracle's cloud-based clinical applications; AI-powered tools and hands-on training for future healthcare workers.")
add("raw/health-systems/nebraska-medicine--artificial-intelligence-help.md",
    "Nebraska Medicine", "guidance", applies_to="clinicians;patients")
add("raw/health-systems/nebraska-medicine--how-we-use-artificial-intelligence.md",
    "Nebraska Medicine", "guidance", applies_to="patients (patient-facing info)",
    phi_rule="Nebraska Medicine believes protecting your privacy and confidential health information is fundamental.",
    permitted_uses="DAX Copilot, a voice-activated tool that helps document care: audio recordings are stored securely and deleted within a defined period; your provider controls what is included in your medical record; nothing becomes part of your record without provider review and approval; predictive tools help identify ED patients needing urgent attention.",
    disclosure_rule="You have a choice about the use of DAX Copilot tools during your care; if you don't want it to be used, let your doctor know at the beginning of your appointment.",
    secure_tools_named="DAX Copilot")
add("raw/health-systems/penn-state-health--ai-clinical-workflow-liability.md",
    "Penn State Health", "guidance", effective_date="2026-03 (news)", applies_to="clinicians;researchers",
    permitted_uses="Research (with Brown University and Seton Hall University School of Law) finds physician liability perception is influenced by the way AI is integrated into a clinician's workflow; research summit on Human Factors and Artificial Intelligence in Healthcare.")
add("raw/health-systems/slucare-ssm-health--ai-work-ease-clinician-burden.md",
    "SLUCare / SSM Health", "guidance", effective_date="2024-09 (news)", applies_to="clinicians",
    permitted_uses="Pioneer work with Microsoft's Nuance technology allowing a physician to focus on their patient rather than a computer screen; collaboration predicting provider burnout as much as a year in advance, allowing employers to intervene and retain physicians.",
    secure_tools_named="Microsoft Nuance (ambient documentation technology)")
add("raw/health-systems/temple-health--ai-clinical-notetaking-software.md",
    "Temple Health", "guidance", applies_to="clinicians",
    permitted_uses="Dragon Ambient eXperience (DAX) Copilot uses ambient voice technology to cut note-taking time: after a patient consents to the use of the tool at the start of their appointment, the physician presses a button on the Epic Haiku app; a note is generated in Epic which physicians review and amend.",
    disclosure_rule="After a patient consents to the use of the tool at the start of their appointment, their physician presses a button on the Epic Haiku app.",
    secure_tools_named="Dragon Ambient eXperience (DAX) Copilot / Dragon Copilot;Epic Haiku")
add("raw/health-systems/uc-davis-health--ai-at-uc-davis-health.md",
    "UC Davis Health", "guidance", applies_to="clinicians;patients;students;staff",
    phi_rule="We adhere to the strictest privacy regulations, including HIPAA, to protect your health information; for research AI development, we use advanced anonymization techniques to ensure patient data is de-identified so an individual cannot be re-identified through its use.",
    permitted_uses="Abridge assists clinicians with administrative tasks such as creating visit summaries; predictive analytics identifies patients at high risk for conditions like sepsis; Viz.ai imaging; AI viewed as another doctor-supervised technology.",
    disclosure_rule="When it comes to AI in health care, issues like fairness, privacy, accountability, and transparency matter; the Data Sharing Committee ensures data are not shared with third parties unless appropriate approvals and safeguards are in place.",
    assessment_rule="BE-FAIR framework (Bias-reduction and Equity Framework for Assessing, Implementing, and Redesigning healthcare predictive models); Health Analytics Core Team analyzes potential AI applications and their use prior to adoption.",
    enforcement="Data security team reviews and pressure tests AI applications to ensure AI adoptions prioritize patient privacy and keep patient data safe; every AI recommendation is reviewed and validated by expert clinicians.",
    secure_tools_named="Abridge;Viz.ai")
add("raw/health-systems/uc-davis-health--clinical-note-taking-technology.md",
    "UC Davis Health", "guidance", applies_to="patients (patient-facing info)",
    phi_rule="Abridge is HIPAA-compliant; only your care team or authorized personnel have access to your information.",
    permitted_uses="Abridge records your conversation with your clinician during the visit; after the visit, the clinician reviews the summary for accuracy and adds it to your medical record; the recording is started, stopped, and paused by your clinician.",
    disclosure_rule="Do I have a choice about whether my clinician uses Abridge? If you do not want your clinician to use Abridge, just let them know.",
    secure_tools_named="Abridge")
add("raw/health-systems/uc-davis-health--guidelines-for-using-generative-ai.md",
    "UC Davis Health (Compliance)", "formal policy", applies_to="clinicians;staff;students",
    banned_uses="Even with approved tools, you should be careful about the information you provide and the output you receive, as generative AI may not be accurate and may reflect biases.",
    phi_rule="You should not be used generative AI tools with any patient information or other sensitive data unless the tool is specifically approved by the UC Davis Health.")
add("raw/health-systems/uci-health--approved-ai-tools.md",
    "UCI Health (CISO & Compliance/Privacy Office)", "formal policy", applies_to="clinicians;staff",
    banned_uses="Copying information from Epic or other clinical systems into AI tools is not permitted;Do not use, enter or share PHI or other clinical queries to any Large Language Models (LLMs) or AI programs, including DoxGPT, ChatGPT or OpenEvidence;Doximity tools not approved for any clinical uses and should not be used with any UCI Health data",
    permitted_uses="Permitted AI use for PHI when signed in with your hs.uci.edu account and using the correct licensed features: Abridge, within approved clinical documentation workflows, and Epic-embedded AI features where enabled, including DynaMedex and Dyna AI for clinical decision support.",
    phi_rule="At this time, only the AI tools listed are approved for use with Protected Health Information (PHI) or any other restricted UCI Health data; PHI and restricted data must not be entered into any external or consumer AI tools; Claims that an AI tool is \"HIPAA compliant\" do not mean it is approved for use at UCI Health.",
    disclosure_rule="To reinforce awareness and accountability, UCI Health will soon introduce a warning and acknowledgment page when accessing certain external AI tools from UCI-managed systems.",
    secure_tools_named="Abridge (approved clinical documentation workflows);Epic-embedded AI features (DynaMedex, Dyna AI);Epic VoIP;Epic Secure Chat",
    enforcement="Entering patient data or restricted information into unapproved or personal AI tools may result in an unauthorized disclosure and must be avoided; use of AI tools with PHI may be treated as a privacy incident and subject to review; uses of such tools is an Information Security & Privacy violation.")
add("raw/health-systems/uci-health--safe-and-approved-use-of-ai-tools.md",
    "UCI Health (IT Security)", "formal policy", applies_to="clinicians;staff",
    banned_uses="Copying information from Epic or other clinical systems into AI tools is not permitted;Do not use, enter, or share PHI or other clinical queries to any Large Language Models (LLMs) or AI programs, including DoxGPT, ChatGPT or OpenEvidence;UCI Health does not currently have any approved Doximity tools",
    permitted_uses="Permitted AI use for PHI when signed in with your hs.uci.edu account and using the correct licensed features: Abridge, within approved clinical documentation workflows, and Epic-embedded AI features where enabled, including DynaMedex and DynaAI for clinical decision support.",
    phi_rule="At this time, only the AI tools listed below are approved for use with Protected Health Information (PHI) or any other restricted UCI Health data; PHI and restricted data must not be entered into any external or consumer AI tools; Claims that an AI tool is \"HIPAA compliant\" do not mean it is approved for use at UCI Health.",
    disclosure_rule="To reinforce awareness and accountability, UCI Health will soon introduce a warning and acknowledgment page when accessing certain external AI tools from UCI-managed systems.",
    secure_tools_named="Abridge;Epic-embedded AI features (DynaMedex, DynaAI);Epic VoIP;Epic Secure Chat;Epic native video/audio visits",
    enforcement="Entering patient data or restricted information into unapproved or personal AI tools, even for drafting, summarization, or rephrasing, may result in an unauthorized disclosure and must be avoided; use of AI tools with PHI may be treated as a privacy incident and subject to review; uses of such tools is an Information Security & Privacy violation.")
add("raw/health-systems/ucsd-health--ai-at-uc-san-diego-health.md",
    "UC San Diego Health", "guidance", applies_to="patients;clinicians",
    phi_rule="At UC San Diego Health, all our AI tools are used under strict security and privacy standards and tested to ensure that they are safe and effective; strong commitment to patient privacy, safety, equity and ethical standards; predictive AI models are trained on examples of real patient data.",
    permitted_uses="One of the first health systems nationwide to use generative AI to draft responses to patient messages in the Epic EHR; care team may use AI to check that important information isn't missed.",
    disclosure_rule="We are transparent about our use of AI and provide clear information about how it's applied wherever appropriate; we require clear information from vendors and developers about how tools work.",
    assessment_rule="Whenever new AI tools are implemented, they are paired with an evaluation plan to assess their impact; we monitor AI tools to ensure they continue to work effectively over time.",
    enforcement="A multidisciplinary group of experts in clinical care, nursing, ethics, health equity, clinical operations, quality and patient safety, information security and AI methods evaluates both current and proposed AI tools.",
    secure_tools_named="Epic EHR generative AI patient messaging;ChatGPT (referenced)")
add("raw/health-systems/umass-memorial--how-we-use-ai-in-patient-care.md",
    "UMass Memorial Health", "guidance", applies_to="patients (patient-facing info)",
    phi_rule="When patient information is used with approved AI tools, it's protected by the same privacy, security, and confidentiality safeguards that apply to all patient information at UMass Memorial Health; AI tools are used only for specific purposes and don't have unrestricted access to patient information.",
    permitted_uses="Create medical notes from conversations during patient appointments; help identify emergency department patients who may need urgent attention after initial evaluation.",
    enforcement="Every digital tool we use, including AI tools, is thoroughly evaluated before it's approved for use; only approved tools are used and with human oversight.")
add("raw/health-systems/uw-medicine--ai-policy-glossary-308g1.pdf.md",
    "UW Medicine", "formal policy", effective_date="V5.0 revised 2026-08-25 (Guidance 308.G1)",
    applies_to="faculty;staff;learners",
    permitted_uses="AI Policy Glossary defines terms supporting the UW Medicine AI policy suite (Algorithm & Model, Hallucinations, Foundation Model, Ground Truth, Inclusivity, Transparency, Transformer, Validation Data Set, etc.).",
    phi_rule="Limited Data Set: a subset of Protected Health Information (PHI) that includes a narrow set of identifiable patient information elements as defined in HIPAA; FERPA applies to higher-education and postgraduate training programs (records include exams and graded assessments).")

# ---- write: append rows not already present, in file order ----
def main():
    csv_path = os.path.join(BASE, "analysis/clauses.csv")
    with open(csv_path, newline="", encoding="utf-8") as f:
        existing = {r["file"] for r in csv.DictReader(f)}
    have_rows = list(existing)
    new = [r for r in R if r["file"] not in existing]
    dupes = [r["file"] for r in R if r["file"] in existing]
    missing_kw = [k for k in (set(dict.fromkeys(x["file"] for x in R))) ]
    # verify every raw .md file is now covered
    on_disk = []
    for d in ["us-med-schools", "health-systems"]:
        for fn in sorted(os.listdir(os.path.join(BASE, "raw", d))):
            if fn.endswith(".md"):
                on_disk.append(f"raw/{d}/{fn}")
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        for r in new:
            w.writerow(r)
    with open(csv_path, newline="", encoding="utf-8") as f:
        final_rows = list(csv.DictReader(f))
    still_missing = [p for p in on_disk if p not in {r["file"] for r in final_rows}]
    print(f"existing before: {len(have_rows)}")
    print(f"appended: {len(new)}; dupes skipped: {len(dupes)}")
    print(f"total rows now: {len(final_rows)}")
    print(f"raw .md files on disk: {len(on_disk)}; still missing from csv: {len(still_missing)}")
    for p in still_missing:
        print("  MISSING:", p)

if __name__ == "__main__":
    main()
