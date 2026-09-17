import fitz, hashlib
doc = fitz.open("pdf/uams--ai-generative-tool-use-policy-2.1.6.pdf")
parts = []
for i, p in enumerate(doc):
    pix = p.get_pixmap(dpi=200)
    path = f"/tmp/uams_p{i}.png"
    pix.save(path)
    parts.append(path)
print("rendered", len(parts), "pages")

import subprocess
text_parts = []
for path in parts:
    r = subprocess.run(["tesseract", path, "-", "--psm", "4"], capture_output=True)
    text_parts.append(r.stdout.decode("utf-8", errors="replace"))
full = "\n\n".join(text_parts).strip()
print("OCR total len:", len(full))

url = "https://research.uams.edu/irb/wp-content/uploads/sites/9/2026/02/Academic-Affairs-Policy-2.1.6.pdf"
fm = f'''---
source_url: "{url}"
title: "UAMS Artificial Intelligence Generative Tool Use Policy (Academic Affairs Policy 2.1.6)"
publisher: "University of Arkansas for Medical Sciences"
published_date: "2025-11-07"
accessed_date: "2026-09-17"
license: "public web PDF (scanned image; text recovered via OCR)"
sha256: ""
---

'''
out = "raw/us-med-schools/uams--ai-generative-tool-use-policy-2.1.6.md"
with open(out, "w") as f:
    f.write(fm + full + "\n")
print("saved", out, hashlib.sha256(open(out,'rb').read()).hexdigest())
print(full[:500])
