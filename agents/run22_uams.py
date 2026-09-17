import fitz
doc = fitz.open("pdf/uams--ai-generative-tool-use-policy-2.1.6.pdf")
print("pages:", len(doc))
text = "\n".join(p.get_text() for p in doc)
print("fitz len:", len(text.strip()))
print(text[:600])
with open("/tmp/uams_text.txt", "w") as f:
    f.write(text)
