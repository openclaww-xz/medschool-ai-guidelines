#!/usr/bin/env python3
"""Run 07 fetch batch. Usage: python3 run07_fetch.py <batch.json>"""
import sys, json, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import fetch_lib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run(batch):
    results = []
    for item in batch:
        outpath = os.path.join(REPO, item["out"])
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        try:
            r = fetch_lib.save(item["url"], item["title"], item["publisher"],
                               item.get("pubdate", "unknown"), outpath,
                               pdfdir=os.path.join(REPO, "pdf"))
        except Exception as e:
            r = {"ok": False, "path": item["out"], "reason": f"{type(e).__name__}: {e}"}
        results.append({**r, "url": item["url"], "title": item["title"]})
    return results

if __name__ == "__main__":
    batch = json.load(open(sys.argv[1]))
    res = run(batch)
    print(json.dumps(res, indent=1))
