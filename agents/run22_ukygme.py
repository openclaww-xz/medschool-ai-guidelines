#!/usr/bin/env python3
import sys, json, shutil, hashlib, os
sys.path.insert(0, "agents")
import subprocess

# copy the fetched PDF into pdf/
src = "/tmp/uky_gme2.pdf"
dst = "pdf/uky-com--use-of-ai-in-gme-policy.pdf"
shutil.copy(src, dst)
body = subprocess.run(["pdftotext", "-layout", dst, "-"], capture_output=True, text=True).stdout.strip()
print("pdf text len:", len(body))
print(body[:400])

url = "https://medicine.uky.edu/sites/default/files/2026-05/Use%20of%20Artificial%20Intelligence%20in%20GME%20Policy.pdf"
fm = f'''---
source_url: "{url}"
title: "Use of Artificial Intelligence in Graduate Medical Education (GME) Policy"
publisher: "University of Kentucky College of Medicine"
published_date: "2026"
accessed_date: "2026-09-17"
license: "public web PDF"
sha256: ""
---

'''
out = "raw/us-med-schools/uky-com--use-of-ai-in-gme-policy.md"
with open(out, "w") as f:
    f.write(fm + body + "\n")
print("saved", out, hashlib.sha256(open(out, "rb").read()).hexdigest())
