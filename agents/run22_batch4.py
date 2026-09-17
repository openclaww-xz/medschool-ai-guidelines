#!/usr/bin/env python3
import sys, json
sys.path.insert(0, "agents")
from fetch_lib import save

R = "raw/us-med-schools"
H = "raw/health-systems"
jobs = [
    # USD Sanford SSOM Pillar 1 Student Handbook w/ AI in Medical Education Policy (PowerDMS public)
    dict(url="https://public.powerdms.com/USD/documents/2178849",
         title="Pillar 1 Student Handbook Class of 2029 2025-2026 (includes Artificial Intelligence (AI) in Medical Education Policy)",
         publisher="USD Sanford School of Medicine",
         pubdate="2025",
         out=f"{R}/usd-ssom--pillar1-student-handbook-ai-policy.md"),
    # VCU Health CIO interview: documents AI workgroup + responsible AI principles/framework
    dict(url="https://www.vcuhealth.org/news/how-vcu-health-it-has-become-a-national-leader-in-the-health-care-information-technology-space",
         title="How VCU Health IT has become a national leader in health care IT (documents AI workgroup and responsible-AI principles)",
         publisher="VCU Health",
         pubdate="2025-09-26",
         out=f"{H}/vcu-health--it-national-leader-ai-workgroup-responsible-ai.md"),
    # UMMC VC Notes: AI-use policy under development + AI Governance Committee
    dict(url="https://umc.edu/news/VCNotes/2024/December/13.html",
         title="AI in Academic Medicine (VC Notes: UMMC AI-use policy under development, AI Governance Committee)",
         publisher="University of Mississippi Medical Center",
         pubdate="2024-12-13",
         out=f"{R}/ummc--vc-notes-ai-in-academic-medicine-policy-in-development.md"),
]
for j in jobs:
    try:
        r = save(j["url"], j["title"], j["publisher"], j["pubdate"], j["out"])
    except Exception as e:
        r = {"ok": False, "reason": f"{type(e).__name__}: {e}"}
    print(json.dumps(r))
