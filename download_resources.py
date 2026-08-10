"""Download AWS exam guides, blueprints, and FAQs into a local resources folder."""

import argparse
import os
import sys
import time
from pathlib import Path

import requests
from urllib.parse import urljoin, urlparse

RESOURCE_DIR = Path("resources")

EXAM_RESOURCE_LINKS = {
    "AWS Certified Cloud Practitioner (CLF-C03)": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Cloud_Practitioner_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-cloud-practitioner/",
    },
    "AWS Certified Solutions Architect – Associate (SAA-C03)": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Solutions_Architect_Associate_SAA-C03_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-solutions-architect-associate/",
    },
    "AWS Certified Developer – Associate (DVA-C02)": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Developer_Associate_DVA-C02_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-developer-associate/",
    },
    "AWS Certified SysOps Administrator – Associate (SOA-C03)": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_SysOps_Administrator_Associate_SOA-C03_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-sysops-administrator-associate/",
    },
    "AWS Certified Solutions Architect – Professional (SAP-C02)": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Solutions_Architect_Professional_SAP-C02_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-solutions-architect-professional/",
    },
    "AWS Certified DevOps Engineer – Professional (DOP-C02)": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_DevOps_Engineer_Professional_DOP-C02_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-devops-engineer-professional/",
    },
    "AWS Certified Advanced Networking – Specialty": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Advanced_Networking_Specialty_ANS-C00_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-advanced-networking-specialty/",
    },
    "AWS Certified Security – Specialty": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Security_Specialty_SCS-C01_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-security-specialty/",
    },
    "AWS Certified Machine Learning – Specialty": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Machine_Learning_Specialty_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-machine-learning-specialty/",
    },
    "AWS Certified Data Analytics – Specialty": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Data_Analytics_Specialty_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-data-analytics-specialty/",
    },
    "AWS Certified Database – Specialty": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_Database_Specialty_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-database-specialty/",
    },
    "AWS Certified SAP on AWS – Specialty": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_SAP_on_AWS_Specialty_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-sap-on-aws-specialty/",
    },
    "AWS Certified AI Practitioner": {
        "exam_guide": "https://d1.awsstatic.com/training-and-certification/docs/AWS_Certified_AI_Practitioner_Exam_Guide.pdf",
        "faq": "https://aws.amazon.com/certification/certified-ai-practitioner/",
    },
}


def discover_sample_links_from_page(page_url: str) -> list:
    """Fetch an HTML page and return a list of links that likely point to sample questions or practice PDFs."""
    links = []
    try:
        resp = requests.get(page_url, timeout=15)
        resp.raise_for_status()
        html = resp.text
    except Exception:
        return links

    try:
        soup = BeautifulSoup(html, "html.parser")
    except Exception:
        return links

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        text = (a.get_text() or "").lower()
        lower = href.lower()
        if any(k in lower for k in ["sample", "sample-questions", "samplequestions", "practice", "questions"]):
            # make absolute
            abs_url = urljoin(page_url, href)
            links.append(abs_url)
            continue

        if any(k in text for k in ["sample", "sample questions", "practice questions", "example questions"]):
            abs_url = urljoin(page_url, href)
            links.append(abs_url)

    # Deduplicate while preserving order
    seen = set()
    deduped = []
    for u in links:
        if u in seen:
            continue
        seen.add(u)
        deduped.append(u)

    return deduped


def safe_filename(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in value).strip("_").lower()


def normalize_certification_name(name: str) -> str:
    for certification in EXAM_RESOURCE_LINKS:
        if name.strip().lower() == certification.strip().lower():
            return certification
    raise ValueError(f"Unknown certification: {name}")


def download_url(url: str, dest_path: Path, timeout: int = 20) -> bool:
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, stream=True, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"  [ERROR] Failed to download {url}: {exc}")
        return False

    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return True


def download_resources(certification: str | None = None, resource_types: list[str] | None = None, skip_existing: bool = False) -> list[Path]:
    downloaded_files: list[Path] = []
    targets = [certification] if certification else list(EXAM_RESOURCE_LINKS.keys())

    for cert_name in targets:
        if cert_name not in EXAM_RESOURCE_LINKS:
            print(f"Skipping unknown certification: {cert_name}")
            continue

        print(f"Downloading resources for: {cert_name}")
        cert_dir = RESOURCE_DIR / safe_filename(cert_name)
        for resource_type, url in EXAM_RESOURCE_LINKS[cert_name].items():
            if resource_types and resource_type not in resource_types:
                continue

            extension = Path(url).suffix or ".html"
            filename = f"{resource_type}{extension}"
            dest_path = cert_dir / filename

            if skip_existing and dest_path.exists():
                print(f"  Skipping existing file: {dest_path}")
                continue

            print(f"  Downloading {resource_type} from {url}")
            success = download_url(url, dest_path)
            if success:
                downloaded_files.append(dest_path)
                time.sleep(1)
            else:
                print(f"  Failed to save {resource_type} for {cert_name}")

        # Discover and download sample question links from the FAQ page if sample_questions not provided explicitly
        wants_samples = (resource_types is None) or ("sample_questions" in (resource_types or []))
        if wants_samples:
            # Prefer an explicit FAQ or exam page url if available
            faq_url = EXAM_RESOURCE_LINKS[cert_name].get("faq") or EXAM_RESOURCE_LINKS[cert_name].get("exam_guide")
            if faq_url:
                print(f"  Discovering sample question links from {faq_url}")
                found_links = discover_sample_links_from_page(faq_url)
                for link in found_links:
                    extension = Path(urlparse(link).path).suffix or ".html"
                    filename = f"sample_questions{extension}"
                    dest_path = cert_dir / filename

                    if skip_existing and dest_path.exists():
                        print(f"  Skipping existing sample file: {dest_path}")
                        continue

                    print(f"  Downloading sample questions from {link}")
                    success = download_url(link, dest_path)
                    if success:
                        downloaded_files.append(dest_path)
                        time.sleep(1)
                    else:
                        print(f"  Failed to download sample from {link}")

    return downloaded_files


def list_certifications() -> None:
    print("Available certifications:")
    for name in EXAM_RESOURCE_LINKS:
        print(f"- {name}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download AWS exam guides, blueprints, and FAQs into resources/")
    parser.add_argument("--certification", "-c", help="Download resources for a specific certification")
    parser.add_argument(
        "--resource-type",
        "-t",
        action="append",
        choices=["exam_guide", "faq"],
        help="Only download specific resource types. Can be repeated.",
    )
    parser.add_argument("--skip-existing", action="store_true", help="Skip files that already exist")
    parser.add_argument("--list", action="store_true", help="List supported certifications")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.list:
        list_certifications()
        return 0

    certification = None
    if args.certification:
        try:
            certification = normalize_certification_name(args.certification)
        except ValueError as exc:
            print(exc)
            return 1

    downloaded_files = download_resources(
        certification=certification,
        resource_types=args.resource_type,
        skip_existing=args.skip_existing,
    )

    if downloaded_files:
        print("\nDownloaded files:")
        for path in downloaded_files:
            print(f"- {path}")
        return 0

    print("No files were downloaded. Check the certification name and network connectivity.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
