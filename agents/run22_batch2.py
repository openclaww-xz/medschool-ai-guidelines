#!/usr/bin/env python3
import sys, json
sys.path.insert(0, "agents")
from fetch_lib import save

R = "raw/us-med-schools"
jobs = [
    # UVM Larner Policy 645.00 (guessing subpage pattern from handbook accordion)
    dict(url="https://www.uvm.edu/larnermed/studenthandbook/645-00-use-artificial-intelligence-medical-education",
         title="Policy 645.00 | Use of Artificial Intelligence in Medical Education",
         publisher="Robert Larner MD College of Medicine, University of Vermont",
         pubdate="unknown",
         out=f"{R}/uvm-larner--policy-645-use-of-ai-in-medical-education.md"),
]
results = []
for j in jobs:
    try:
        r = save(j["url"], j["title"], j["publisher"], j["pubdate"], j["out"])
    except Exception as e:
        r = {"ok": False, "reason": f"{type(e).__name__}: {e}"}
    print(json.dumps(r))
