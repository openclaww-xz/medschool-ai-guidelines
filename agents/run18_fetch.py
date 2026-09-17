#!/usr/bin/env python3
"""Run 18 batch fetcher: DO + HBCU med school AI policies."""
import sys, json, traceback
sys.path.insert(0, "/Users/openclaw/git/medschool-ai-guidelines")
sys.path.insert(0, "/Users/openclaw/git/medschool-ai-guidelines/agents")
import os
os.chdir("/Users/openclaw/git/medschool-ai-guidelines")
from fetch_lib import save

BATCH = json.load(open(sys.argv[1]))
results = []
for item in BATCH:
    try:
        r = save(item["url"], item["title"], item["publisher"], item.get("date","unknown"), item["out"], "pdf")
        results.append({**item, **r})
        print(("OK " if r.get("ok") else "FAIL "), item["out"], r.get("len", r.get("reason","")))
    except Exception as e:
        results.append({**item, "ok": False, "reason": f"{type(e).__name__}: {e}"})
        print("ERR ", item["url"], e)
    sys.stdout.flush()
json.dump(results, open(sys.argv[2], "w"), indent=1)
