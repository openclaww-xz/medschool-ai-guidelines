import fitz
from PIL import Image
import collections
doc = fitz.open("pdf/uams--ai-generative-tool-use-policy-2.1.6.pdf")
for i, p in enumerate(doc):
    imgs = p.get_images(full=True)
    txt = p.get_text().strip()
    print(f"page {i}: images={len(imgs)} textlen={len(txt)} rect={p.rect}")
print("metadata:", doc.metadata)
im = Image.open("/tmp/uams_p0.png")
print("p0 png:", im.size, im.mode)
c = collections.Counter(im.convert("L").getdata())
print("top gray:", c.most_common(5))
# Try tesseract on the whole image once, default psm, stderr visible
import subprocess
r = subprocess.run(["tesseract", "/tmp/uams_p0.png", "stdout"], capture_output=True)
print("tesseract stdout bytes:", len(r.stdout))
print("tesseract stderr:", r.stderr.decode()[:300])
print(r.stdout.decode(errors="replace")[:400])
