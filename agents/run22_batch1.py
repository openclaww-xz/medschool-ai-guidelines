#!/usr/bin/env python3
import sys, json
sys.path.insert(0, "agents")
from fetch_lib import save

R = "raw/us-med-schools"
jobs = [
    # JABSOM GenAI guidelines for learners (May 2025 PDF)
    dict(url="https://jabsom.hawaii.edu/_docs/jabsom-guidelines-on-generative-ai-for-learners_may-2025.pdf",
         title="JABSOM Guidelines on Generative AI for Learners (v1, May 2025)",
         publisher="John A. Burns School of Medicine, University of Hawai'i",
         pubdate="2025-05",
         out=f"{R}/jabsom--guidelines-on-generative-ai-for-learners.md"),
    # UNR Med Use of AI Policy
    dict(url="https://med.unr.edu/about/policies/artificial-intelligence-policy",
         title="Use of Artificial Intelligence Policy | UNR School of Medicine",
         publisher="University of Nevada, Reno School of Medicine",
         pubdate="2026-01-08",
         out=f"{R}/unr-med--use-of-artificial-intelligence-policy.md"),
    # UAMS Academic Affairs Policy 2.1.6
    dict(url="https://research.uams.edu/irb/wp-content/uploads/sites/9/2026/02/Academic-Affairs-Policy-2.1.6.pdf",
         title="UAMS Artificial Intelligence Generative Tool Use Policy (Academic Affairs Policy 2.1.6)",
         publisher="University of Arkansas for Medical Sciences",
         pubdate="2025-11-07",
         out=f"{R}/uams--ai-generative-tool-use-policy-2.1.6.md"),
    # UK COM GME AI policy
    dict(url="https://medicine.uky.edu/sites/default/files/2026-05/Use+of+Artificial+Intelligence+in+GME+Policy.pdf",
         title="Use of Artificial Intelligence in Graduate Medical Education Policy",
         publisher="University of Kentucky College of Medicine",
         pubdate="2026",
         out=f"{R}/uky-com--use-of-ai-in-gme-policy.md"),
    # UK ADVANCE clinical care guidelines
    dict(url="https://advance.uky.edu/sites/default/files/2024-03/uk-advance-clinical-care-guidelines.pdf",
         title="UK ADVANCE Clinical Care Guidelines for Generative AI",
         publisher="University of Kentucky (UK ADVANCE Committee)",
         pubdate="2024-03",
         out=f"{R}/uky--advance-clinical-care-guidelines-genai.md"),
    # LSUHSC-NO policy
    dict(url="https://www.medschool.lsuhsc.edu/administration/docs/Policy%20on%20Use%20of%20Generative%20AI%20by%20Medical%20Students.pdf",
         title="Policy on Use of Generative AI by Medical Students",
         publisher="LSU Health New Orleans School of Medicine",
         pubdate="2025-10",
         out=f"{R}/lsuhsc-no--policy-on-use-of-generative-ai-by-medical-students.md"),
    # Rush library guide: Resources for Students (quotes UAC0039 verbatim)
    dict(url="https://library.rush.edu/c.php?g=1362441&p=10077641",
         title="Rush Library AI Guide: Resources for Students (excerpts Rush UAC0039 GenAI policy)",
         publisher="Rush University Library",
         pubdate="unknown",
         out=f"{R}/rush--library-guide-ai-resources-for-students-uac0039-excerpts.md"),
    # UNLV IT AI Best Practices (documents absence of UNLV-specific AI policy)
    dict(url="https://it.unlv.edu/ai-technology/best-practices",
         title="AI Best Practices (UNLV IT) - states no campus-wide AI policy exists",
         publisher="UNLV Information Technology",
         pubdate="unknown",
         out=f"{R}/unlv-ksom--it-ai-best-practices-no-campus-policy.md"),
]

results = []
for j in jobs:
    try:
        r = save(j["url"], j["title"], j["publisher"], j["pubdate"], j["out"])
        r.update({"slug": j["out"].split("/")[-1], "err": None})
    except Exception as e:
        r = {"ok": False, "path": j["out"], "reason": f"{type(e).__name__}: {e}", "slug": j["out"].split("/")[-1]}
    results.append(r)
    print(json.dumps(r))
