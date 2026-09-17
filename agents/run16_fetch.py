#!/usr/bin/env python3
"""Run 16 batch 1 fetcher — group H schools + health systems."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_lib import save

REPO = "/Users/openclaw/git/medschool-ai-guidelines"
SCH = os.path.join(REPO, "raw/us-med-schools")
HS = os.path.join(REPO, "raw/health-systems")
PDFD = os.path.join(REPO, "pdf")

JOBS = [
    # (outpath, url, title, publisher, pubdate)
    (SCH + "/uc-davis--md-program-acceptable-use-genai-coursework.md",
     "https://health.ucdavis.edu/mdprogram-polices/curricular/Acceptable%20use%20of%20Generative%20Artificial%20Intelligence.html",
     "Acceptable Use of Generative Artificial Intelligence in Academic Coursework Policy",
     "UC Davis School of Medicine MD Program", "unknown"),
    (SCH + "/uc-san-diego--senate-admin-workgroup-genai-education-report.pdf.md",
     "https://evc.ucsd.edu/_files/2024.08.23%20Final%20Report%20-%20Senate%20Admin%20Workgroup%20on%20Impact%20of%20Generative%20Artificial%20Intelligence%20on%20Education%20at%20UC%20San%20Diego.pdf",
     "Final Report - Senate-Admin Workgroup on Impact of Generative Artificial Intelligence on Education at UC San Diego",
     "UC San Diego EVC / Academic Senate", "2024-08-23"),
    (SCH + "/uc-san-diego--libguide-ai-and-academic-integrity.md",
     "https://ucsd.libguides.com/AI/academicintegrity",
     "AI and Academic Integrity - Generative Artificial Intelligence LibGuide",
     "UC San Diego Library", "unknown"),
    (SCH + "/uc-irvine--dtei-generative-ai-for-teaching-learning.md",
     "https://dtei.uci.edu/generative-ai/",
     "Generative AI for Teaching & Learning",
     "UC Irvine Division of Teaching Excellence and Innovation", "unknown"),
    (SCH + "/u-arizona-tucson--policy-on-student-use-of-ai.pdf.md",
     "https://medicine.arizona.edu/sites/default/files/2024-11/Policy-on-Student-Use-of-AI-2024-11-13.pdf",
     "Policy on Student Use of AI",
     "University of Arizona College of Medicine - Tucson", "2024-11-13"),
    (SCH + "/u-arizona--ai-guidelines-and-principles.md",
     "https://responsibleai.arizona.edu/ai-arizona/ai-guidelines-principles",
     "AI Guidelines & Principles",
     "University of Arizona (responsibleai.arizona.edu)", "unknown"),
    (SCH + "/u-arizona-phoenix--ai-use-by-students-policy.md",
     "https://phoenixmed.arizona.edu/policy/ai-use-by-student-policy",
     "Artificial Intelligence (AI) Use by Students Policy",
     "University of Arizona College of Medicine - Phoenix", "unknown"),
    (SCH + "/unm--ai-appropriate-use-and-guidelines.md",
     "https://airesources.unm.edu/ai-guidance/appropriate-use.html",
     "Appropriate Use and Guidelines (UNM AI Resources)",
     "University of New Mexico", "unknown"),
    (SCH + "/unm--faculty-senate-policy-use-of-genai.md",
     "https://fs.unm.edu/nss8/index.php/111/PolicyAI",
     "Policy on the Use of Generative Artificial Intelligence (AI) in Teaching, Research, and Service at UNM",
     "UNM Faculty Senate", "unknown"),
    (SCH + "/u-oklahoma--ai-policies.md",
     "https://www.ou.edu/cfe/artificial-intelligence/AI-policies",
     "OU AI Policies",
     "University of Oklahoma Center for Faculty Excellence", "unknown"),
    (SCH + "/ou-hsc--libguide-artificial-intelligence-and-genai.md",
     "https://libguides.ouhsc.edu/ai",
     "Artificial Intelligence and Generative AI (LibGuide)",
     "University of Oklahoma Health Sciences Center Library", "unknown"),
    (SCH + "/unmc--ai-use-guidelines.md",
     "https://wiki.unmc.edu/index.php/UNMC_AI_Use_Guidelines",
     "UNMC AI Use Guidelines",
     "University of Nebraska Medical Center", "unknown"),
    (SCH + "/ku--responsible-ai.md",
     "https://ai.ku.edu/responsible-ai",
     "Responsible AI - Artificial Intelligence",
     "University of Kansas", "unknown"),
    (SCH + "/kumc--ai-steering-committee.md",
     "https://www.kumc.edu/artificial-intelligence-resource-center/ai-steering-committee.html",
     "AI Steering Committee - KUMC Artificial Intelligence Resource Center",
     "University of Kansas Medical Center", "unknown"),
    (HS + "/uc-davis-health--guidelines-for-using-generative-ai.md",
     "https://health.ucdavis.edu/compliance/regulatory/guidelines-for-using-ai",
     "Guidelines for Using Generative Artificial Intelligence (AI)",
     "UC Davis Health Compliance and Privacy Services", "unknown"),
    (HS + "/uc-davis-health--ai-at-uc-davis-health.md",
     "https://health.ucdavis.edu/welcome/artificial-intelligence",
     "AI at UC Davis Health",
     "UC Davis Health", "unknown"),
    (HS + "/ucsd-health--ai-at-uc-san-diego-health.md",
     "https://health.ucsd.edu/about-us/ai-at-uc-san-diego-health/",
     "AI at UC San Diego Health - How We Use Artificial Intelligence for Smarter, Safer Health Care",
     "UC San Diego Health", "unknown"),
    (HS + "/uci-health--approved-ai-tools.md",
     "https://www.ucihealth.org/about-us/compliance/approved-ai-tools",
     "Approved AI Tools",
     "UCI Health", "unknown"),
    (HS + "/uci-health--safe-and-approved-use-of-ai-tools.md",
     "https://its.health.uci.edu/security/safe-approved-ai-tools",
     "Safe and Approved Use of AI Tools at UCI Health",
     "UCI Health Information Technology Services", "unknown"),
    (HS + "/nebraska-medicine--how-we-use-artificial-intelligence.md",
     "https://www.nebraskamed.com/patients/rights-responsibilities/AI",
     "How we use artificial intelligence",
     "Nebraska Medicine", "unknown"),
    (HS + "/nebraska-medicine--artificial-intelligence-help.md",
     "https://www.nebraskamed.com/help/artificial-intelligence",
     "Artificial Intelligence - Nebraska Medicine Help",
     "Nebraska Medicine", "unknown"),
]

if __name__ == "__main__":
    results = []
    for outpath, url, title, pub, pubdate in JOBS:
        try:
            r = save(url, title, pub, pubdate, outpath, pdfdir=PDFD)
        except Exception as e:
            r = {"ok": False, "path": outpath, "reason": f"{type(e).__name__}: {e}"}
        r["url"] = url
        results.append(r)
        print(json.dumps(r))
    json.dump(results, open(os.path.join(REPO, "agents/run16_fetch1.json"), "w"), indent=1)
    ok = sum(1 for r in results if r.get("ok"))
    print(f"DONE {ok}/{len(results)}")
