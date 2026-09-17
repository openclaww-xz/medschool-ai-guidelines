from PIL import Image, ImageDraw
im = Image.new("RGB", (400, 100), "white")
d = ImageDraw.Draw(im)
d.text((10, 40), "Hello policy test 123", fill="black")
im.save("agents/run22_ocr_test.png")
import subprocess, os
os.chdir("agents")
r = subprocess.run(["tesseract", "run22_ocr_test.png", "stdout"], capture_output=True)
print("ret:", r.returncode)
print("stderr:", r.stderr.decode(errors="replace")[:200])
print("out:", r.stdout.decode(errors="replace"))
