---
source: raw/health-systems/ochsner--ai-at-ochsner.md
source_url: https://www.ochsner.org/ai
publisher: Ochsner Health
run: 30
read: full file (189 lines, complete)
---

# Ochsner — AI at Ochsner (patient-facing explainer + FAQ)

## Authority / authorship
- Patient-facing marketing/communications page with governance claims. Named bodies: **Data Governance and AI Steering committees**, "dedicated Artificial Intelligence Steering Committee ... clinicians, nurses, data scientists, legal advisors, and patient safety leaders."
- Vendor deployments named in related-news footer: Latent Health (medication access), AFib AI tech, **DeepScribe** (ambient AI), generative AI in patient messaging. An internal AI agent is personified as "Clara."

## Philosophy (verbatim framing)
- "At Ochsner Health, we believe technology and care should work together to make every patient's experience better and improve healthcare for our communities."
- "AI is not a substitute for the critical relationship between a patient and their care team. It does not diagnose, make medical decisions, or provide the personal touch of a nurse or doctor. It is a tool that enhances efficiency and supports our teams in delivering high-quality, compassionate care."
- "Ochsner Health is leading the way in using technology to improve care..."

## Complete verbatim clause inventory
**Deployment inventory:**
1. "AI-Driven Patient Messaging: AI chatbots enable our care teams to more quickly and effectively guide patients to the right care, answer health questions, and improve access..."
2. "Ambient AI for Clinical Documentation: This technology helps our care teams take notes during patient visits in real time... automatically adding notes to medical records."
3. "Predictive Analytics for Early Intervention: AI securely analyzes patient data to predict risks for conditions like sepsis or heart failure..."
4. "AI-Powered Diagnostic Imaging: Our radiologists use AI tools to help prioritize critical findings and enable faster diagnosis and treatment."
5. "Optimizing Workflow / Automating Administrative Tasks: AI helps with paperwork, authorizations..."
6. "Streamlining Pharmacy Workflows: AI automates routine pharmacy tasks, helping patients get approved for medications by insurance companies..."
7. "AI Health Agents: These AI tools provide real-time health insights, reminders, and guidance..."
8. "AI scanning and mapping: Studying 3D heart maps in real-time during cath procedures ... helps make AFib treatment more accurate."

**Responsibility/governance claims:**
9. "Every new AI tool we adopt is carefully reviewed by our Data Governance and AI Steering committees."
10. "The Ochsner Health AI Steering Committee sets clear rules for how we use AI responsibly. We only work with trusted partners who share our values. We continuously monitor AI tools to make sure they work fairly for all patients."
11. "Yes. At Ochsner, every AI tool is carefully tested before it's used in patient care. We have a dedicated Artificial Intelligence Steering Committee that oversees how AI tools are selected, tested, and implemented. This committee includes a diverse group of experts — clinicians, nurses, data scientists, legal advisors, and patient safety leaders..."
12. "AI tools used at Ochsner must meet strict privacy and cybersecurity standards... only the minimum information necessary is used for each task. For example, AI tools must use two-factor authentication to confirm your identity before providing instructions."

**Ambient listening consent (FAQ):**
13. "Ambient listening is a secure technology that uses AI to create accurate medical notes from conversations during your visit. It listens silently in the background... It recognizes different voices, including yours, your provider's, and anyone else in the room. It captures only health-related information."
14. "Providers will always ask for your verbal consent before using ambient listening. You can choose to turn it on or off at any time. The app only listens during your visit — not before or after. Recordings are securely encrypted, reviewed only by your care team, and stored safely in your medical record..."
15. **AI-agent consent model:** "When you complete Ochsner's consent form, you authorize us to contact you using a variety of methods, including pre-recorded messages, automated systems and AI agents, like Clara. This consent allows us to share important reminders..." with assurances: "These tools are used only for communication and support tasks, not for diagnosing or replacing your care team. You will always know when you're interacting with an AI agent. You can choose not to continue an AI conversation if you'd prefer to speak with a person directly."
16. "You always have the choice to opt out of AI agent interactions. Your access to care, support and services will never be affected by your choice."
17. "You will not be charged for talking to the AI agent."
18. Clara scope: "Clara only has access to the information necessary to assist with her mandated task... Clara is provided only the minimal information needed for the specific task, like confirming patient identification and preferred pharmacy."
19. "after each conversation, your care team will receive a summary of your call"; care team "stays fully informed and in control of your care plan."
20. **AI avatars:** "These avatars will always identify themselves as AI-generated. Importantly, the health information shared by these avatars is not generated by AI. It is carefully written, reviewed and approved by our expert team of scientists, medical writers, and clinicians. AI is only used to bring the avatar to life visually."
21. "No. AI doesn't diagnose or treat patients and does not replace any human clinicians... AI is only used for supportive tasks."
22. Transparency: "Any time you interact with an AI agent, whether by phone, message, or online, it will clearly introduce itself."

## Sophistication markers
- **Clinical deployment governance:** asserted, committee-named (Data Governance + AI Steering), composition disclosed (clinicians, nurses, data scientists, legal, patient safety) — but no pipeline, criteria, registry, or decisions described. Governance-as-reassurance.
- **Monitoring:** one sentence — "We continuously monitor AI tools to make sure they work fairly for all patients" — the only fairness-monitoring claim in this run, but unsubstantiated.
- **Model-failure handling:** none.
- **Ambient-scribe consent rules:** **verbal consent before each use** + on/off at any time + recording-window limitation ("only listens during your visit — not before or after") — stronger than UC Davis's opt-out; lacks UChicago's chart-documentation of consent and third-party-consent specificity.
- **Clinician liability:** none; positioning is entirely "AI supports, humans decide."
- AI-agent consent rides the general treatment consent form (blanket pre-consent) — arguably weaker than purpose-specific consent; opt-out and disclosure rights are clearly stated.
- Sophisticated patient-communication design: AI disclosure duty, no-charge assurance, minimal-data agent scoping, human-content-only avatars.

## Distinctives
- The most complete patient-facing AI communication in the corpus: consent, disclosure, opt-out, cost, data-minimization, and safety FAQ all addressed in plain language.
- Named deployed stack: DeepScribe ambient, sepsis/HF prediction, imaging triage, pharmacy automation, AI phone agent (Clara), avatars.

## Provisional classification
**Progressive-structured (deployed + communicative, governance-asserted).** Broad real deployment with unusually good patient-facing consent/transparency practice; governance is named and multidisciplinary but undetailed — between structured adopter and PR-driven. Because deployments and consent mechanics are verifiable and specific, it sits above pure PR; because governance internals are one-liners, below pioneers.
