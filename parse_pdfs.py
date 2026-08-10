"""Parse all PDFs under resources/ and save extracted text to .local_doc_summaries/pdf/"""

import os
import re
from pathlib import Path

try:
    import pdfplumber
except Exception as e:
    print("pdfplumber is required. Install with: pip install pdfplumber")
    raise

ROOT = Path("resources")
OUT_DIR = Path(".local_doc_summaries") / "pdf"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MAX_CHARS = 200_000


def safe_filename(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in value).strip("_").lower()


count = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    for fname in filenames:
        if not fname.lower().endswith(".pdf"):
            continue

        full_path = Path(dirpath) / fname
        rel = full_path.relative_to(ROOT)
        parts = rel.parts
        # Build a filename using parent folder (cert) and original name
        if len(parts) >= 2:
            cert_slug = safe_filename(parts[0])
            base = safe_filename("_".join(parts[1:]))
        else:
            cert_slug = safe_filename(parts[0]) if parts else "unknown"
            base = safe_filename(fname)

        out_name = f"{cert_slug}_{base}.txt"
        out_path = OUT_DIR / out_name

        try:
            with pdfplumber.open(full_path) as pdf:
                pages = []
                for p in pdf.pages:
                    text = p.extract_text() or ""
                    pages.append(text)
                text_all = "\n\n".join(pages)
                # Normalize whitespace
                text_all = re.sub(r"\s+", " ", text_all).strip()
                text_all = text_all[:MAX_CHARS]

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"--- Source: {full_path} ---\n")
                f.write(text_all)

            print(f"Wrote: {out_path} ({len(text_all)} chars)")
            count += 1
        except Exception as e:
            print(f"Failed to parse {full_path}: {e}")

print(f"Done. Parsed {count} PDF(s).")
