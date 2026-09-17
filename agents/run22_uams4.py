import subprocess, hashlib, glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
parts = []
for i in range(7):
    src = f"/tmp/uams_p{i}.png"
    dst = f"uams_pg{i}"
    subprocess.run(["cp", src, dst + ".png"], check=True)
    r = subprocess.run(["tesseract", dst + ".png", dst], capture_output=True)
    txt = open(dst + ".txt").read()
    parts.append(txt)
    print(f"page {i}: {len(txt)} chars")
full = "\n\n".join(parts).strip()
print("total:", len(full))

url = "https://research.uams.edu/irb/wp-content/uploads/sites/9/2026/02/Academic-Affairs-Policy-2.1.6.pdf"
fm = f'''---
source_url: "{url}"
title: "UAMS Artificial Intelligence Generative Tool Use Policy (Academic Affairs Policy 2.1.6)"
publisher: "University of Arkansas for Medical Sciences"
published_date: "2025-11-07"
accessed_date: "2026-09-17"
license: "public web PDF (image-only print-to-PDF; text recovered via OCR, minor OCR artifacts possible)"
sha256: ""
---

'''
out = "../raw/us-med-schools/uams--ai-generative-tool-use-policy-2.1.6.md"
with open(out, "w") as f:
    f.write(fm + full + "\n")
print("saved", out, hashlib.sha256(open(out, "rb").read()).hexdigest())
