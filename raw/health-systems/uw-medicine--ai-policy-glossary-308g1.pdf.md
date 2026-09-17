---
source_url: "https://depts.washington.edu/comply/docs/308_G1.pdf"
title: "UW Medicine AI Policy Glossary (Guidance 308.G1, V5.0)"
publisher: "UW Medicine Compliance"
published_date: "2026-08-25"
accessed_date: "2026-09-17"
license: "public web page"
sha256: ""
---

Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
UW Medicine Artificial Intelligence (AI) Policy Glossary 
 
There is no universally accepted definition of the term “Artificial Intelligence”, and the extent to which contemporary systems constitute AI is 
still vigorously debated. Many approaches have been developed since the 1950s with the goal of emulating intelligent human behavior. These 
range from symbolic (“rule-based”) approaches in which knowledge is manually encoded in computable form, to classical Machine Learning 
Models and Neural Networks that learn from large data sets directly. However, use of these approaches does not in and of itself constitute AI, a 
term that is typically used to refer to systems that aim to emulate or augment human capabilities such as pattern recognition, language use, and 
decision making.  
 
Examples of applications that are within scope of AI as used in this document include but are not limited to: 
 1) diagnosis: e.g. automated interpretation of radiological images 
 2) prognosis: e.g. predicting clinical outcomes, such as sepsis 
 3) language generation and understanding (including speech recognition) 
Examples of applications that are not considered within the scope of AI as used in this document include but are not limited to: 
 1) searching for documents without summarizing or synthesizing them 
2) looking for mentions of specific words in notes, without contextualizing or interpreting their meaning  
3) triggering an alert when a predefined lab value is elevated 
  
The focus of the definitions below is on AI Models that learn from data, as these are the primary focus of public, regulatory and commercial 
attention at present. Examples include Models that learn to predict clinical outcomes from labeled health record data, Models that learn to 
interpret medical images, and Models (such as GPT-4) that learn to generate coherent language and respond to requests from unlabeled text 
and sets of instructions and preferences. While different Algorithms and architectures may be used to learn from data, they present common 
policy concerns including data security, Model Bias, interpretability and the potential to make inaccurate recommendations. The definitions 
provided below are intended to provide an approachable guide to interpretation of UW Medicine AI-related policies and guidelines pertaining to 
such systems. 
 
All capitalized terms within this AI Policy Glossary are defined in this document. 
 
Glossary Term  Description   
1 Accuracy Accuracy refers to the degree to which a Model’s outputs are correct when compared to ground truth. In 
healthcare, this is critical as decisions can directly impact patient safety and treatment effectiveness. 
Statistical measures that are commonly used include sensitivity, specificity, positive predictive value, area 
under the receiver operator characteristic (ROC) curve, and area under the precision-recall curve. Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
2 Algorithm & Model An algorithm is a set of rules or instructions that a computer follows. In AI, algorithms are applied with the 
goal of performing tasks that typically require human intelligence, such as recognizing patterns or making 
decisions. These algorithms may consist of rules that are manually defined based on expert knowledge, in 
which case the result of following the algorithm is completion of a task. However, with Machine Learning, a 
model is the result of applying a learning algorithm to a large dataset, enabling this model to make 
predictions or decisions based on unseen data. Essentially, the algorithm is the process while the model is the 
trained system resulting from this process that can apply what it has learned to new situations.  
3 Annotations Annotation refers to the process of labeling or tagging data to provide context and meaning and importantly 
to serve as a “Ground Truth” or “gold standard” for training and evaluation for supervised Machine Learning. 
These labeled data are crucial for training certain AI Models, and as testing data to measure their 
performance. Annotation transforms raw data (e.g. the pixels from a digitized retinal scan) into information 
with an assigned meaning (e.g. diabetic retinopathy, a bounding box around a patient’s face in an image) that 
enables AI Systems to learn to assign this meaning to new, unseen data.  
4 Artificial Intelligence 
System 
AI systems apply AI Algorithms and/or Models to perform specific tasks that typically require human 
intelligence, such as visual perception, speech recognition, decision-making, and language translation. 
Additionally, AI systems can perform tasks beyond individual human capabilities, such as processing large 
datasets at high speeds. 
5 Bias 
 
Bias is a systematic tendency of an AI tool to produce outputs that are less accurate, favorable, or appropriate 
for some patients or users. It arises in artificial intelligence Models in multiple ways. The datasets used to 
train AI Models can reflect the biases that pervade societies and cultures that produced the data they contain.  
For example, when prompted, Generative AI Models can exhibit bias by reinforcing cultural stereotypes 
present in their training data. In addition, the design of AI Systems reflects the values, assumptions, and 
experiences of the decision makers responsible for their development. 
6 Chatbot A computer system designed to simulate and engage in human conversation through text, visual, or voice 
interactions. These can be simple, rule-based systems or advanced, Generative AI-driven Models that respond 
to user queries.  
7 Classification Classification refers to the process of categorizing data into predefined groups or classes based on specific 
features. An AI Model is trained on a labeled dataset, where the correct class for each data point is known, so 
the Model can learn to predict the class for new, unseen data. Classification is used in various applications, 
such as image feature recognition and medical diagnosis. 
8 Clinical Care Means a continuum of services performed for a patient by health professionals, or Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
under their direction, for the purpose of promoting, maintaining or restoring health. 
9 Clinical Decision 
Support 
Clinical Decision Support (CDS) tools provide individuals with knowledge and person-specific information, 
intelligently filtered or presented at appropriate times, to enhance decision-making in the clinical workflow. 
These tools include computerized alerts and reminders to care providers and patients; clinical guidelines; 
condition-specific order sets; focused patient data reports and summaries; documentation templates; 
diagnostic support; and contextually relevant reference information, among other tools. 
10 Clinical Learning 
Environment 
The settings where healthcare Learners receive their clinical education, encompassing locations such as 
hospitals, medical centers, ambulatory sites, and virtual spaces. 
11 Computer Vision A computer system that analyzes images and/or videos to interpret and make decisions based on visual data, 
mimicking humans’ ability to see and comprehend objects or activities.  
12 De-identified Health 
Information 
Data that has been de-identified in accordance with the Health Insurance Portability and Accountability Act of 
1996 (“HIPAA”) (see Section, VI(B) of COMP.103, Uses and Disclosures of Protected Health Information).    
 
13 Deep Learning A class of Machine Learning Algorithms that uses many layers of representations (often tens or even hundreds 
of successive layers, hence the term ‘deep’) in an artificial Neural Network to progressively extract higher-
level features from large amounts of raw input data in order to recognize patterns, make predictions, or 
classify data.   
14 Education An encompassing term that includes the Learning Environment and/or  involves Learners or Learner data. 
15 Equity The principle of ensuring that AI Systems do not perpetuate or exacerbate social inequities and that outcomes 
from AI outputs are equitable for all groups. For example, an AI tool designed to detect skin cancer could be 
less likely to detect skin cancer in individuals with darker skin tones if there is underrepresentation of these 
individuals in the training data. 
16 Explainability The ability to provide a user-friendly explanation of the reasons behind an AI System’s output (e.g., a 
diagnosis or prediction), to provide an understanding of its decision process.  
17 Family Educational 
Rights and Privacy 
Act (FERPA) 
The Family Educational Rights and Privacy Act (FERPA) is a federal law that affords parents the right to have 
access to their children’s education records, the right to seek to have the records amended, and the right to 
have some control over the disclosure of personally identifiable information from the education records. 
When a student turns 18 years old, or enters a postsecondary institution at any age, the rights under FERPA 
transfer from the parents to the student (“eligible student”). FERPA applies to higher-education and 
postgraduate training programs, and universities are responsible for complying to data protection and record Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
retention/request requirements. Records subject to FERPA include: academic records, student identification, 
personal information, disciplinary records, financial records, health records, visa records, exams, and graded 
assessments. 
18 Foundation Model A large Machine Learning Model pre-trained on a vast quantity of data, which can be adapted to a wide range 
of downstream tasks. A well-known example is the large pretrained language Model GPT-4. 
19 Generative AI Generative AI (GenAI) refers to a class of artificial intelligence Models that have the capability to generate 
new content (such as text, images, audio, and video) that is coherent and contextually relevant based on the 
patterns learned from their training data. 
20 Ground Truth Ground truth refers to the benchmark(s) or “gold standard” that AI’s predictions or outputs are compared 
against to measure their performance. It represents information considered to be accurate   often affirmed by 
direct measurement, expert annotation, or empirical observation. While ground truth is often meticulously 
curated, it may not always reflect the complexity and variability of the real world, so should be reviewed 
closely for applicability for any given scenario. 
21 Hallucinations Instances when a Generative AI System generates untrue or inaccurate content that is not supported by real-
world data. This might include false information about people, events, or facts. In some cases, hallucinations 
may include information that seems plausible at first glance but is found to be fictitious or inaccurate on 
further evaluation.  
22 Honest Broker An Honest Broker is an individual, software application, organization or team acting to search UW Medicine 
patient medical records and/or collect patient health information (“PHI”) to respond to a researcher’s 
approved request to access or use Clinical Data to collect and provide de-identified information to the 
research team in accordance with applicable IRB authorization, UW Medicine policies, and core principles 
listed above. The Honest Broker resides within the covered entity and acts as a gatekeeper between the 
covered entity and the researcher and serves as the link between HIPAA Privacy and Security.  
23 
 
Inclusivity Designing and deploying systems that accommodate and represent diverse users, ensuring that AI 
technologies serve a broad range of needs. For example, a Generative AI Chatbot for patient communication 
may incorporate multilingual support, voice interaction for users with visual impairments, or text-to-speech 
options as examples of accessibility options.  
24 Inference Inference in Artificial Intelligence (AI) refers to the process by which a trained AI Model makes predictions on 
new data based on its prior training. It involves using Algorithms to analyze input data and apply learned 
information to generate outputs or decisions. Essentially, inferencing is when a trained Model is asked to 
process data to generate outputs. Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
25 Large Language 
Model 
A type of Neural Network trained on very large amounts of text, often across multiple languages. Current 
models may have hundreds of billions of parameters (hence the use of ‘large’) or more. At their core, these 
models are predicting the next word in a sequence. However, with additional training they have 
demonstrated the ability to respond appropriately to complex questions, generating language resembling that 
written by a person, including the translation of text. 
26 Learner Individuals participating in SoM academic programs, including but not limited to students, residents, fellows, 
postdocs, and other trainees. 
27 Learning 
Environment 
Classroom, office, research space, laboratory, virtual spaces, and Clinical Learning Environments where 
learners engage in didactic, clinical, and/or applied learning activities. Includes engagement with learning 
technologies such as Canvas, Learning Hub, and other platforms. 
28 Limited Data Set A limited data set is a subset of Protected Health Information (PHI) and includes a narrow set of identifiable 
patient information elements as defined in HIPAA. Elements that can be included in a data set include Dates, 
Service, Date of Birth, City, State, Zip code, Age, and any other unique code or identifier that is not listed as a 
direct identifier. There are certain elements that must be excluded to qualify as a limited data set, including 
but limited to Names, Street Addresses, and Email Addresses. 
29 Machine Learning Algorithms that can “learn” from data by identifying patterns and making decisions with minimal human 
intervention. These Algorithms improve performance over time through iterative processes, enabling them to 
solve problems and make predictions.  
30 Natural Language 
Processing 
A subfield of computer science focused on developing systems with the ability to generate and interpret text 
and spoken words.  
31 Neural Network A common type of Machine Learning architecture, inspired by the complex functions of the human brain, 
where many interconnected small units (neurons’), linked by numerous weighted connections, have the 
capability to learn to perform perceptual and linguistic tasks, amongst others. 
32 Protected Health 
Information (PHI) 
Information (verbal, electronic, or on paper) maintained or transmitted by UW Medicine that relates to:  
• The past, present, or future physical or mental health or condition of an individual;  
• The provision of healthcare to an individual; or  
The past, present, or future payment for the provision of healthcare to an individual that either a) identifies 
the individual or b) provides a reasonable basis to believe the information can be used to identify the 
individual. Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
33 Predictive Analytics A branch of advanced analytics that makes predictions about future outcomes using historical data combined 
with statistical modeling, data mining techniques, and Machine Learning. 
 
34 Prompts A prompt is an instruction entered into a system in text, audio, image, or code format that tells the AI System 
what task to perform.  
35 Reinforcement 
Learning 
A category of Machine Learning where a Model iteratively learns by using trial-and-error and a sequence of 
successful outcomes to determine the best next step in solving a given problem.  
36 Research Data Data that has been derived from UW Medicine clinical data and has been collected or created through 
research and is maintained as part of a research record. 
37 Secure UW 
Medicine 
Environment 
Hosted within a UW Medicine data center, cloud data center, or with a contractually authorized partner and 
undergone a review by UW Medicine IT Services to ensure the required controls are in place. If you have 
questions regarding the required controls, reach out to UW Medicine Information Security uwmed-
security@uw.edu or review our security standards online at Information Security Standards – UW Medicine 
Information Security and APS 2.6. 
38 Segmentation Segmentation refers to the process of dividing data into meaningful parts or segments. This technique is often 
used in image processing to identify and separate different objects within an image, making it easier for AI 
Systems to analyze and understand the visual information. 
39 Supervised Learning A category of Machine Learning where labeled datasets are used to train Algorithms to classify data or predict 
outcomes accurately. For example, learning to recognize dog breeds based on labeled dog pictures that serve 
as the assumed source of truth.  
40 Training Data Set A portion of data used to train a Machine Learning Model to learn patterns, relationships, and features to 
make predictions or decisions. It is the primary source of information for the Algorithm to adjust parameters 
and improve performance.   
41 Transparency The degree to which an AI System's operations and decisions are clear, understandable, and accessible for 
review or scrutiny by users and stakeholders. Unfortunately, larger and more capable Models are often less 
transparent.  
42 Transformer A type of Neural Network architecture that underlies many language Models. A key component is a technique 
called “attention,” which helps the Model learn contextual relationships between components of a sequence. 
For example, Generative Pre-trained Transformers (GPTs), developed by OpenAI, use this architecture to 
Model language by learning contextual relationships between words, including ambiguous ones.  Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
43 Validation Data Set A held-out subset of the training data that is often used to tune the Model’s parameters and assess how well 
the Model generalizes to unseen data.  
44 Unsupervised 
Learning 
A category of Machine Learning that uses unlabeled data to discover patterns in similarities, differences, or 
relationships. This method is useful for clustering data or when subject matter experts are unsure of common 
properties of a data set and/or are looking for similarities within a data set that may not be immediately 
apparent.  
45 UW Medicine 
Business Operations 
UW Medicine healthcare, administrative and business operations supporting both the clinical enterprise and 
the UW School of Medicine. For example, this includes AI uses that support administrative processes within 
the central administration of the School of Medicine or within a School of Medicine department.  
46 UW Medicine Data UW Medicine data includes the following types of data stored in any UW Medicine system or application 
regardless of where the data originated:  
• Clinical Data. For purposes of this policy, clinical data is data created or received by UW Medicine in 
Clinical Care decision making, provision, billing, or payment. Clinical data includes healthcare delivery 
records (including PHI), provider data, de-identified healthcare data, data utilized for Quality 
Improvement activities, metadata, reference data, healthcare supply chain data, laboratory data, 
referral data, patient-level financial data, other forms of confidential or sensitive data within 
healthcare records or databases of UW Medicine (including metadata and reference data);  
• Financial Data, such as but not limited to revenue, budgets, financial statements or other financial 
information related to business and operational needs;  
• Personally Identifiable Information (PII) such as staff and faculty data (e.g., names, addresses, job 
roles, salary, bios, and phone numbers);   
• Education Records, are any recorded information that directly relates to (i.e., identifies) a student 
and is maintained by the UW or by a party (e.g., service provider) acting for the UW, including but not 
limited to  directory information, such as name, email address, date of birth, and class, as well as 
many other data types, such as grades, library records, courses taken, disciplinary action, Student 
Identification Number, education loan information, and advising records and any other data 
protected under FERPA. 
• Research Data derived from UW Medicine clinical data; and  
• Any other data used for UW Medicine business, clinical, or operations purposes (e.g., legal, IP, 
confidential/proprietary, trade secret, subject to contractual sharing limitations). Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
 
 
 
 
Authors/Contributors 
Primary Author: Jason Lau 
Contributors: Ana Anderson, Trevor Cohen, Noah Hoffman Michael Leu, Chen Liang, Gang Luo, Angad Singh, Peter Tarczy-Hornoch, Jennifer 
Slyker, Karen Segerson  
References 
1. https://coe.gsa.gov/coe/ai-guide-for-government/what-is-ai-key-terminology/index.html  
a. Artificial Intelligence 
b. Machine Learning 
c. Supervised Learning 
d. Unsupervised Learning 
e. Reinforcement learning 
2. https://itconnect.uw.edu/guides-by-topic/security-authentication/artificial-intelligence-guidelines/  
f. Generative AI 
g. Large Language Models 
h. Hallucinations 
i. Prompts 
3. https://teaching.washington.edu/course-design/ai/ai-ethical-issues/  
j. Bias 
k. Accuracy 
l. Equity  
For the purposes of this policy, UW Medicine data does not include UW Medicine information published for 
public use or has been approved for public use by an appropriate University of Washington authority (see UW 
Administrative Policy Statement 2.4).  Approved Version 
 
  UW Medicine AI Glossary | V5.0 | Revised 8.25.2026 
 
4. Intelligent Systems in Medicine and Health : The Role of AI by Trevor A. Cohen, , Vimla L. Patel, , and Edward H. Shortliffe 2022 
https://ebookcentral.proquest.com/lib/washington/reader.action?docID=7134136  
m. Neural Network 
n. Deep Learning 
o. Transformer 
p. Generative AI 
q. Natural Language Processing 
r. Chatbot 
s. Training Set 
t. Validation Set 
u. Transparency 
v. Explainability 
5. Generative artificial intelligence, patient safety and healthcare quality: a review by Michael D Howell 2024 
https://qualitysafety.bmj.com/content/early/2024/07/24/bmjqs-2023-016690#T1 Stanford - Human-Centered Artificial Intelligence 
https://hai.stanford.edu/sites/default/files/2023-03/AI-Key-Terms-Glossary-Definition.pdf 
w. Foundation Model 
x. Large Language Model 
6. Clinical Decision Support https://www.healthit.gov/topic/safety/clinical-decision-support  
y. Clinical Decision Support 
 
 
 
