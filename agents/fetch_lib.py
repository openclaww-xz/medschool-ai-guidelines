#!/usr/bin/env python3
"""Fetch a URL, extract main text, wrap with YAML front-matter, save under raw/."""
import subprocess, sys, hashlib, re, os, json
from bs4 import BeautifulSoup
import requests

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

def fetch(url, timeout=40):
    r = requests.get(url, timeout=timeout, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    r.raise_for_status()
    return r.content, r.headers.get("Content-Type", "")

def html_to_text(data):
    soup = BeautifulSoup(data, "lxml")
    for t in soup(["script", "style", "noscript", "header", "footer", "nav", "form", "aside"]):
        t.decompose()
    main = soup.find("main") or soup.find("article") or soup.find("div", class_=re.compile(r"content|main", re.I)) or soup.body or soup
    text = main.get_text("\n")
    lines = [l.strip() for l in text.splitlines()]
    out, blank = [], 0
    for l in lines:
        if l:
            out.append(l); blank = 0
        else:
            blank += 1
            if blank == 1:
                out.append("")
    return "\n".join(out).strip()

def pdf_to_text(path):
    r = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True)
    return r.stdout.strip()

def save(url, title, publisher, pubdate, outpath, pdfdir=None, license_="public web page"):
    accessed = "2026-09-17"
    data, ctype = fetch(url)
    is_pdf = "pdf" in ctype.lower() or data[:5] == b"%PDF-"
    body = ""
    pdfpath = None
    if is_pdf:
        os.makedirs(pdfdir or "pdf", exist_ok=True)
        base = os.path.basename(outpath).replace(".md", "")
        pdfpath = os.path.join(pdfdir or "pdf", base + ".pdf")
        with open(pdfpath, "wb") as f:
            f.write(data)
        body = pdf_to_text(pdfpath)
    else:
        body = html_to_text(data)
    if len(body) < 200:
        return {"ok": False, "path": outpath, "reason": f"extracted text too short ({len(body)} chars)", "len": len(body)}
    fm = f'''---
source_url: "{url}"
title: "{title}"
publisher: "{publisher}"
published_date: "{pubdate}"
accessed_date: "{accessed}"
license: "{license_}"
sha256: ""
---

'''
    with open(outpath, "w") as f:
        f.write(fm + body + "\n")
    h = hashlib.sha256(open(outpath, "rb").read()).hexdigest()
    return {"ok": True, "path": outpath, "len": len(body), "sha256": h, "pdf": pdfpath}
