#!/usr/bin/env python3
"""Snippet extractor for clause-matrix building (run 15).
Usage: python3 snippets.py <dir> <start> <count>
Prints front-matter + keyword-windowed sentences per file for manual structuring.
"""
import os, re, sys, html

BASE = "/Users/openclaw/git/medschool-ai-guidelines/raw"

FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)

def fm_get(fm, key):
    m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', fm, re.M)
    return m.group(1).strip().strip('"') if m else ""

SENT_SPLIT = re.compile(r'(?<=[.!?;])\s+(?=[A-Z"“\u201c(\-])')

GROUPS = {
  "PHI": r'(?i)\b(PHI|protected health|HIPAA|patient data|patient information|patient privacy|patient confidential|health information|identifiable)\b',
  "BAN": r'(?i)(prohibit\w*|must not|may not|shall not|not be permitted|not permitted|not allowed|not authorize\w*|banned|forbidden|never (use|enter|input|share|upload))',
  "PERM": r'(?i)(permitted|allow\w*|may use|encourag\w*|authoriz\w*|responsible use|acceptable use)',
  "DATE": r'(?i)(effective|adopted|revised|approved|updated|in effect|takes? effect|policy date)',
  "AAMC": r'(?i)AAMC',
  "DISC": r'(?i)(disclos\w*|acknowledg\w*|attribut\w*|citing AI|cite (the )?AI|transparen\w*|declare)',
  "ASSESS": r'(?i)(assess\w*|examin\w*|\bexam\b|quiz\w*|grading|graded|USMLE|NBME|evaluation of student|test secur\w*|summative|formative)',
  "TOOL": r'(?i)(Copilot|ChatGPT|GPT-?[45o]|Claude|Gemini|Secure ?GPT|secure chat|enterprise|HIPAA.?compliant|ChatEpic|Dragon|ambient|Nuance|Merlin|MyChart|Epic|Health ?Bot|playground|LLM)\b',
  "ENF": r'(?i)(enforce\w*|violation\w*|sanction\w*|disciplin\w*|referral|honor (code|pledge)|academic integrity|consequences| misconduct|student conduct)',
  "APPLIES": r'(?i)\b(residents?\b|fellows?\b|GME\b|graduate medical|faculty|clinicians?\b|attending\w*|medical students?\b|students?\b|trainees?\b|program directors?\b)',
}

def clean(t):
    t = html.unescape(t)
    t = re.sub(r'\[?IMAGE[^\]]*\]?', ' ', t)
    t = re.sub(r'\[[^\]]{0,80}\]\([^)]{0,200}\)', lambda m: m.group(0).split(']')[0][1:], t)  # keep link text
    t = re.sub(r'https?://\S+', ' ', t)
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n{2,}', '\n', t)
    return t

def sentences(body):
    body = clean(body)
    body = re.sub(r'\n', ' ', body)
    sents = SENT_SPLIT.split(body)
    out = []
    for s in sents:
        s = s.strip()
        if 25 <= len(s) <= 400:
            out.append(s)
    return out

def main(d, start, count):
    files = sorted(f for f in os.listdir(os.path.join(BASE, d)) if f.endswith('.md'))
    sel = files[start:start+count]
    for fn in sel:
        path = os.path.join(BASE, d, fn)
        raw = open(path, encoding='utf-8', errors='replace').read()
        m = FM.match(raw)
        fm, body = (m.group(1), raw[m.end():]) if m else ("", raw)
        print("=" * 20)
        print(f"FILE: {d}/{fn}")
        print(f"TITLE: {fm_get(fm,'title')} | PUB: {fm_get(fm,'publisher')} | PUBDATE: {fm_get(fm,'published_date')}")
        print(f"CHARS: {len(body)}")
        seen = set()
        for gname, pat in GROUPS.items():
            rx = re.compile(pat)
            hits = []
            for s in sentences(body):
                key = s[:80].lower()
                if key in seen:
                    continue
                if rx.search(s):
                    seen.add(key)
                    hits.append(s[:320])
                if len(hits) >= (5 if gname in ("BAN","PERM","PHI") else 3):
                    break
            if hits:
                print(f"[{gname}]")
                for h in hits:
                    print("  - " + h)
        print()

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
