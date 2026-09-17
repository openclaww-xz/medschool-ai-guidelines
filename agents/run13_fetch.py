#!/usr/bin/env python3
"""Run 13 batch fetcher: Group G med schools + health systems."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import fetch_lib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_SCH = os.path.join(REPO, "raw", "us-med-schools")
RAW_HS = os.path.join(REPO, "raw", "health-systems")
PDFDIR = os.path.join(REPO, "pdf")

# (outpath-relative-dir, slug, url, title, publisher, pubdate)
BATCH = [
 ("us-med-schools", "tulane--it-guide-generative-ai-platforms",
  "https://it.tulane.edu/it-guide-generative-ai-platforms",
  "IT Guide for Generative AI Platforms", "Tulane University IT", "unknown"),
 ("us-med-schools", "tulane--provost-faculty-guide-using-generative-ai",
  "https://provost.tulane.edu/faculty-guide-using-generative-ai-tulane",
  "Faculty Guide to Using Generative AI at Tulane", "Tulane University Provost", "unknown"),
 ("us-med-schools", "miami-miller--ai-in-medical-education",
  "https://med.miami.edu/offices/ai-in-medical-education",
  "AI in Medical Education", "University of Miami Miller School of Medicine", "unknown"),
 ("us-med-schools", "miami-miller--ai-in-medical-education-resources",
  "https://med.miami.edu/offices/ai-in-medical-education/resources",
  "AI in Medical Education - Resources", "University of Miami Miller School of Medicine", "unknown"),
 ("us-med-schools", "stony-brook--academic-integrity-generative-ai",
  "https://www.stonybrook.edu/commcms/academic_integrity/generative-ai/index.php",
  "Generative AI - Academic Integrity", "Stony Brook University", "unknown"),
 ("us-med-schools", "rutgers--guidance-on-the-use-of-ai",
  "https://it.rutgers.edu/ai/guidance-on-the-use-of-ai-at-rutgers/",
  "Guidance on the use of AI at Rutgers", "Rutgers University IT", "unknown"),
 ("us-med-schools", "temple--guidelines-for-generative-artificial-intelligence",
  "https://tuportal6.temple.edu/documents/380033/1166174952/Guidelines+for+GenAI.pdf/30bcd155-1311-6434-355c-efc963798189?t=1725490134990",
  "Guidelines for Generative Artificial Intelligence (GenAI)", "Temple University", "2024-09-04"),
 ("us-med-schools", "temple-katz--ai-task-force",
  "https://tuportal6.temple.edu/web/medicine/blog/-/blogs/katz-launches-ai-task-force-to-guide-responsible-and-strategic-use-of-artificial-intelligence-1",
  "Katz Launches AI Task Force to Guide Responsible and Strategic Use of AI", "Lewis Katz School of Medicine, Temple University", "unknown"),
 ("us-med-schools", "wayne-state--guidelines-for-using-generative-ai",
  "https://tech.wayne.edu/policies/aiguidelines",
  "Guidelines for using generative AI", "Wayne State University Computing & Information Technology", "unknown"),
 ("us-med-schools", "vcu-som--acceptable-use-generative-ai-applications-policy",
  "https://assets.som.vcu.edu/pdfs/policies/aipolicy.pdf",
  "Acceptable Use of Generative Artificial/Augmented Intelligence (AI) Applications Policy", "VCU School of Medicine", "unknown"),
 ("us-med-schools", "vcu--library-guide-generative-ai-policies",
  "https://guides.library.vcu.edu/ai",
  "Generative Artificial Intelligence - Before using a Generative AI: Policies", "VCU Libraries", "unknown"),
 ("us-med-schools", "ttuhsc--artificial-intelligence-use",
  "https://www.ttuhsc.edu/compliance/ai",
  "Artificial Intelligence (AI) Use at TTUHSC", "Texas Tech University Health Sciences Center", "unknown"),
 ("us-med-schools", "uth-mcgovern--policy-on-ai-generative-tools",
  "https://med.uth.edu/mcgovern/resources/policy-on-ai-generative-tools/",
  "Policy on AI Generative Tools", "McGovern Medical School at UTHealth Houston", "unknown"),
 ("us-med-schools", "uth-mcgovern--msit-generative-ai-offerings",
  "https://med.uth.edu/msit/generative-ai-offerings/",
  "Generative AI Offerings", "McGovern Medical School IT at UTHealth Houston", "unknown"),
 ("us-med-schools", "ut-austin--acceptable-use-of-generative-ai-tools",
  "https://security.utexas.edu/ai-tools",
  "Acceptable Use of Generative AI Tools", "University of Texas at Austin Information Security Office", "unknown"),
 ("us-med-schools", "tamu--ai-use-guidelines-and-ethics",
  "https://ai.tamu.edu/teach-with-ai/use-guidelines-and-ethics.html",
  "Use Guidelines and Ethics - Artificial Intelligence", "Texas A&M University", "unknown"),
 ("us-med-schools", "dell-med--student-policies-wiki",
  "https://cloud.wikis.utexas.edu/wiki/pages/viewpage.action?pageId=63375680",
  "Student Policies - Dell Medical School", "Dell Medical School, UT Austin", "unknown"),
 ("health-systems", "ochsner--ai-at-ochsner",
  "https://www.ochsner.org/ai",
  "AI at Ochsner", "Ochsner Health", "unknown"),
 ("health-systems", "jackson-health--ai-information",
  "https://jacksonhealth.org/ai-information/",
  "Jackson Health System - AI Information", "Jackson Health System", "unknown"),
 ("health-systems", "houston-methodist--care-with-ai",
  "https://www.houstonmethodist.org/center-for-innovation/our-work/care-with-ai",
  "Future Bet: Predictive and Proactive Care with AI", "Houston Methodist Center for Innovation", "unknown"),
]

if __name__ == "__main__":
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    outdir_map = {"us-med-schools": RAW_SCH, "health-systems": RAW_HS}
    for d, slug, url, title, pub, pubdate in BATCH:
        if only and slug not in only:
            continue
        outp = os.path.join(outdir_map[d], slug + ".md")
        try:
            r = fetch_lib.save(url, title, pub, pubdate, outp, pdfdir=PDFDIR)
        except Exception as e:
            r = {"ok": False, "reason": f"{type(e).__name__}: {e}", "path": outp}
        print(json.dumps(r))
