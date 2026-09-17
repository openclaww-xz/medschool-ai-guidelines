#!/usr/bin/env python3
import sys, json
sys.path.insert(0, "agents")
from fetch_lib import save

R = "raw/us-med-schools"
jobs = [
    # UR Provost GenAI Use in Education (task 3: Rochester AI pages not yet in repo)
    dict(url="https://www.rochester.edu/provost/gen-ai-education",
         title="Generative AI Use in Education (Provost guidelines)",
         publisher="University of Rochester Office of the Provost",
         pubdate="2025-09-27",
         out=f"{R}/u-rochester--provost-genai-use-in-education.md"),
    # UR University IT AI Tools page (Strong IT equivalent — tech.rochester.edu)
    dict(url="https://tech.rochester.edu/artificial-intelligence-ai-tools",
         title="Artificial Intelligence (AI) Tools (University IT)",
         publisher="University of Rochester Information Technology",
         pubdate="unknown",
         out=f"{R}/u-rochester--university-it-ai-tools.md"),
    # UR AI in Research Committee responsible-use guidelines
    dict(url="https://www.rochester.edu/university-research/ai-research-committee/responsible-use-gen-ai",
         title="Responsible Use of Generative Artificial Intelligence in Research",
         publisher="University of Rochester AI in Research Committee",
         pubdate="unknown",
         out=f"{R}/u-rochester--responsible-use-genai-in-research.md"),
]
for j in jobs:
    try:
        r = save(j["url"], j["title"], j["publisher"], j["pubdate"], j["out"])
    except Exception as e:
        r = {"ok": False, "reason": f"{type(e).__name__}: {e}"}
    print(json.dumps(r))
