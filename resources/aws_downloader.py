#!/usr/bin/env python3
"""
URL Finder - Scrapes AWS certification pages to find correct PDF URLs
for the 3 failing certifications
"""

import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# AWS certification pages to scrape
CERT_PAGES = {
    "AIF-C01": {
        "name": "AWS Certified AI Practitioner",
        "pages": [
            "https://aws.amazon.com/certification/certified-ai-practitioner/",
            "https://aws.amazon.com/certification/exams/?nc2=sb_ce_exm",
        ]
    },
    "PAS-C01": {
        "name": "AWS Certified SAP on AWS Specialty",
        "pages": [
            "https://aws.amazon.com/certification/certified-sap-on-aws-specialty/",
        ]
    },
    "SCS-C02": {
        "name": "AWS Certified Security Specialty",
        "pages": [
            "https://aws.amazon.com/certification/certified-security-specialty/",
        ]
    },
}

def scrape_pdf_links(url: str) -> list[str]:
    """Scrape a page and return all PDF links found"""
    try:
        print(f"  🌐 Scraping: {url}")
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        pdf_links = []

        # Find all <a> tags with href ending in .pdf
        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            if href.lower().endswith(".pdf"):
                # Make absolute if relative
                if href.startswith("//"):
                    href = "https:" + href
                elif href.startswith("/"):
                    href = "https://aws.amazon.com" + href
                pdf_links.append(href)

        # Also search raw HTML for any d1.awsstatic.com PDF URLs
        raw_links = re.findall(
            r'https://d1\.awsstatic\.com[^\s"\'<>]+\.pdf',
            response.text
        )
        pdf_links.extend(raw_links)

        # Deduplicate
        return list(dict.fromkeys(pdf_links))

    except requests.exceptions.RequestException as e:
        print(f"  ❌ Failed to scrape {url}: {e}")
        return []

def verify_url(url: str) -> tuple[bool, int]:
    """Check if a URL returns a valid PDF"""
    try:
        response = requests.head(url, headers=HEADERS, timeout=10, allow_redirects=True)
        is_ok = response.status_code == 200
        return is_ok, response.status_code
    except requests.exceptions.RequestException:
        return False, 0

def main():
    print("=" * 65)
    print("  AWS PDF URL Finder - Scraping certification pages")
    print("=" * 65)

    for code, info in CERT_PAGES.items():
        print(f"\n{'─'*65}")
        print(f"🔍 [{code}] {info['name']}")
        print(f"{'─'*65}")

        found_pdfs = []

        for page_url in info["pages"]:
            links = scrape_pdf_links(page_url)
            if links:
                print(f"  📄 Found {len(links)} PDF link(s):")
                for link in links:
                    ok, status = verify_url(link)
                    status_icon = "✅" if ok else f"❌ ({status})"
                    print(f"     {status_icon} {link}")
                    if ok:
                        found_pdfs.append(link)
            else:
                print(f"  ⚠️  No PDF links found on this page")

        if found_pdfs:
            print(f"\n  🎯 WORKING URL(s) for {code}:")
            for url in found_pdfs:
                print(f'     "{url}"')
        else:
            print(f"\n  ❌ No working PDFs found for {code}")
            print(f"  👉 Manually visit: {info['pages'][0]}")

    print("\n" + "=" * 65)
    print("  Done! Copy working URLs into aws_downloader.py")
    print("=" * 65)

if __name__ == "__main__":
    main()
