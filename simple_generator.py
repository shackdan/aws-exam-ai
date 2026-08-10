# simple_generator.py
"""Simple AWS exam question generator using Ollama directly - supports up to 100 questions"""

import ollama
import os
import time
import random
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

OLLAMA_MODEL = "qwen2.5-coder:7b"
OUTPUT_DIR = "output"
LOCAL_DOCS_DIR = "local_docs"
RESOURCES_DIR = "resources"
LOCAL_REFERENCE_SUMMARY_DIR = ".local_doc_summaries"
FEEDBACK_DIR = "feedback"
FEEDBACK_SUMMARY_DIR = "feedback_summary"
MAX_QUESTIONS = 100
BATCH_SIZE = 5

CERTIFICATION_CATEGORIES = [
    (
        "Cloud Practitioner",
        [
            (
                "AWS Certified Cloud Practitioner (CLF-C03)",
                "Validates overall understanding of AWS Cloud, including basic services, security, compliance, and pricing models. Ideal for beginners or business professionals seeking a broad overview of AWS."
            ),
        ],
    ),
    (
        "Associate Level",
        [
            (
                "AWS Certified Solutions Architect – Associate (SAA-C03)",
                "Focuses on designing scalable, secure, and reliable applications on AWS. Recommended for those with at least 1 year of hands-on experience."
            ),
            (
                "AWS Certified Developer – Associate (DVA-C02)",
                "Validates ability to develop and maintain applications using AWS services, databases, and developer tools. Suitable for developers with 1+ year of experience."
            ),
            (
                "AWS Certified SysOps Administrator – Associate (SOA-C03)",
                "Focuses on deployment, management, and operational monitoring of AWS workloads. Designed for systems administrators with practical AWS experience."
            ),
        ],
    ),
    (
        "Professional Level",
        [
            (
                "AWS Certified Solutions Architect – Professional (SAP-C02)",
                "Advanced certification for designing complex, multi-tier applications and making architectural decisions. Requires prior Associate-level knowledge."
            ),
            (
                "AWS Certified DevOps Engineer – Professional (DOP-C02)",
                "Validates expertise in provisioning, operating, and managing distributed application systems on AWS. Requires Associate-level certification as a prerequisite."
            ),
        ],
    ),
    (
        "Specialty Certifications",
        [
            (
                "AWS Certified Advanced Networking – Specialty",
                "Focuses on complex networking tasks and hybrid IT network architectures."
            ),
            (
                "AWS Certified Security – Specialty",
                "Validates advanced knowledge of securing AWS workloads."
            ),
            (
                "AWS Certified Machine Learning – Specialty",
                "Demonstrates ability to design, implement, and maintain ML solutions on AWS."
            ),
            (
                "AWS Certified Data Analytics – Specialty",
                "Focuses on designing and managing analytics solutions using AWS services."
            ),
            (
                "AWS Certified Database – Specialty",
                "Validates expertise in database design, deployment, and management on AWS."
            ),
            (
                "AWS Certified SAP on AWS – Specialty",
                "For professionals managing SAP workloads on AWS."
            ),
            (
                "AWS Certified AI Practitioner",
                "Designed for business professionals to validate understanding of AI and ML concepts on AWS."
            ),
        ],
    ),
]

CERTIFICATIONS = {
    name: description
    for _, items in CERTIFICATION_CATEGORIES
    for name, description in items
}

CERTIFICATION_BLUEPRINT_NOTES = {
    "AWS Certified Cloud Practitioner (CLF-C03)": (
        "Use the official CLF-C03 exam guide and blueprint, focusing on cloud concepts, security and compliance, technology, and billing and pricing."
    ),
    "AWS Certified Solutions Architect – Associate (SAA-C03)": (
        "Use the official SAA-C03 exam guide and blueprint, focusing on design secure, resilient, high-performing, and cost-optimized architectures."
    ),
    "AWS Certified Developer – Associate (DVA-C02)": (
        "Use the official DVA-C02 exam guide and blueprint, focusing on developing, deploying, debugging, and monitoring AWS applications."
    ),
    "AWS Certified SysOps Administrator – Associate (SOA-C03)": (
        "Use the official SOA-C03 exam guide and blueprint, focusing on deployment, operations, monitoring, security, and optimization of AWS workloads."
    ),
    "AWS Certified Solutions Architect – Professional (SAP-C02)": (
        "Use the official SAP-C02 exam guide and blueprint, focusing on complex architectures, migration, security, cost optimization, and operational excellence."
    ),
    "AWS Certified DevOps Engineer – Professional (DOP-C02)": (
        "Use the official DOP-C02 exam guide and blueprint, focusing on continuous delivery, security controls, monitoring, incident response, and high-availability."
    ),
    "AWS Certified Advanced Networking – Specialty": (
        "Use the official Advanced Networking Specialty exam guide and blueprint, focusing on complex networking, hybrid IT, and AWS networking services."
    ),
    "AWS Certified Security – Specialty": (
        "Use the official Security Specialty exam guide and blueprint, focusing on AWS security controls, data protection, incident response, and compliance."
    ),
    "AWS Certified Machine Learning – Specialty": (
        "Use the official Machine Learning Specialty exam guide and blueprint, focusing on data engineering, modeling, deployment, and operations for ML solutions."
    ),
    "AWS Certified Data Analytics – Specialty": (
        "Use the official Data Analytics Specialty exam guide and blueprint, focusing on data collection, storage, processing, analysis, and visualization."
    ),
    "AWS Certified Database – Specialty": (
        "Use the official Database Specialty exam guide and blueprint, focusing on database design, deployment, migration, and optimization on AWS."
    ),
    "AWS Certified SAP on AWS – Specialty": (
        "Use the official SAP on AWS Specialty exam guide and blueprint, focusing on SAP deployment, migration, operations, and reliability on AWS."
    ),
    "AWS Certified AI Practitioner": (
        "Use the official AI Practitioner exam guide and blueprint, focusing on business-level AI/ML concepts, AWS AI services, and implementation considerations."
    ),
}

SAA_C03_DOMAINS = [
    ("Design Secure Architectures", [
        "Secure access to AWS resources",
        "Secure workloads and applications",
        "Data security controls",
    ]),
    ("Design Resilient Architectures", [
        "Scalable and loosely coupled architectures",
        "Highly available and fault-tolerant architectures",
    ]),
    ("Design High-Performing Architectures", [
        "High-performing storage solutions",
        "Elastic compute solutions",
        "High-performing database solutions",
        "Scalable network architectures",
    ]),
    ("Design Cost-Optimized Architectures", [
        "Cost-optimized storage solutions",
        "Cost-optimized compute solutions",
        "Cost-optimized database solutions",
    ]),
]


def safe_filename(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in value).strip("_").lower()


def load_local_reference_files(certification: str):
    reference_dirs = [LOCAL_DOCS_DIR, RESOURCES_DIR]
    certification_tokens = certification.lower().replace("–", "").replace("/", " ").split()
    matching_files = []

    for source_dir in reference_dirs:
        if not os.path.isdir(source_dir):
            continue

        for root, _, files in os.walk(source_dir):
            for filename in files:
                lower_name = filename.lower()
                if not lower_name.endswith((".md", ".txt", ".pdf", ".html", ".htm")):
                    continue

                file_path = os.path.join(root, filename)
                if any(keyword in lower_name for keyword in ["blueprint", "exam", "guide", "faq"]):
                    matching_files.append(file_path)
                    continue

                if any(token in lower_name for token in certification_tokens):
                    matching_files.append(file_path)

    if not matching_files:
        for source_dir in reference_dirs:
            if not os.path.isdir(source_dir):
                continue

            for root, _, files in os.walk(source_dir):
                for filename in files:
                    lower_name = filename.lower()
                    if lower_name.endswith((".md", ".txt", ".pdf", ".html", ".htm")):
                        matching_files.append(os.path.join(root, filename))
                        if len(matching_files) >= 3:
                            break
                if len(matching_files) >= 3:
                    break
            if len(matching_files) >= 3:
                break

    return matching_files


def extract_text_from_pdf(path: str, max_chars: int):
    if pdfplumber is None:
        return ""

    try:
        with pdfplumber.open(path) as pdf:
            pages = []
            for page in pdf.pages[:3]:
                text = page.extract_text() or ""
                pages.append(text)
            return "\n".join(pages)[:max_chars]
    except Exception:
        return ""


def extract_text_from_html(path: str, max_chars: int):
    try:
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception:
        return ""

    try:
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        return text[:max_chars]
    except Exception:
        return ""


def read_local_reference_text(file_paths):
    text_parts = []
    max_chars_per_file = 4000
    for path in file_paths[:5]:
        lower_path = path.lower()
        source_text = ""

        if lower_path.endswith(".pdf"):
            source_text = extract_text_from_pdf(path, max_chars_per_file)
        elif lower_path.endswith((".html", ".htm")):
            source_text = extract_text_from_html(path, max_chars_per_file)
        else:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    source_text = f.read(max_chars_per_file)
            except UnicodeDecodeError:
                continue
            except Exception:
                continue

        if not source_text.strip():
            continue

        text_parts.append(f"--- {os.path.basename(path)} ---\n{source_text}")

    return "\n\n".join(text_parts)


def build_local_reference_summary(certification: str, topic: str, raw_reference_text: str):
    if not raw_reference_text.strip():
        return ""

    os.makedirs(LOCAL_REFERENCE_SUMMARY_DIR, exist_ok=True)
    cache_path = os.path.join(
        LOCAL_REFERENCE_SUMMARY_DIR,
        f"{safe_filename(certification)}_{safe_filename(topic)}.txt",
    )

    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()

    prompt = f"""You are an expert AWS exam content summarizer. Summarize the following local reference material for {certification} so it can be used as a compact, exam-relevant context for question generation.
Focus on exam domains, blueprint topics, and key concepts that should guide question creation. Use the available downloaded exam guide, blueprint, and FAQ resources whenever possible. Keep the summary concise and structured.

Local reference material:
{raw_reference_text}
"""

    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=prompt,
        options={
            "temperature": 0.0,
            "top_p": 0.5,
            "num_predict": 2048,
        },
    )
    summary = response["response"].strip()

    with open(cache_path, "w", encoding="utf-8") as f:
        f.write(summary)

    return summary


def save_review_feedback(certification: str, topic: str, review_text: str):
    os.makedirs(FEEDBACK_DIR, exist_ok=True)
    path = os.path.join(
        FEEDBACK_DIR,
        f"{safe_filename(certification)}_{safe_filename(topic)}.txt",
    )
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"--- {timestamp} ---\n{review_text.strip()}\n\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(entry)

    build_feedback_summary(certification, topic)
    return path


def build_feedback_summary(certification: str, topic: str):
    os.makedirs(FEEDBACK_SUMMARY_DIR, exist_ok=True)
    raw_path = os.path.join(
        FEEDBACK_DIR,
        f"{safe_filename(certification)}_{safe_filename(topic)}.txt",
    )
    summary_path = os.path.join(
        FEEDBACK_SUMMARY_DIR,
        f"{safe_filename(certification)}_{safe_filename(topic)}.txt",
    )

    if not os.path.exists(raw_path):
        return ""

    with open(raw_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    prompt = f"""You are an expert at turning reviewer feedback into a compact skill guide for question generation.
Review the following raw review feedback for {certification} ({topic}) and produce a short, actionable summary of the key improvements that should be applied to future generated questions. Keep the guidance under 400 words.

Raw reviewer feedback:
{raw_text}
"""

    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=prompt,
        options={
            "temperature": 0.0,
            "top_p": 0.5,
            "num_predict": 2048,
        },
    )
    summary = response["response"].strip()

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)

    return summary


def load_feedback_guidance(certification: str, topic: str):
    summary_path = os.path.join(
        FEEDBACK_SUMMARY_DIR,
        f"{safe_filename(certification)}_{safe_filename(topic)}.txt",
    )
    general_path = os.path.join(
        FEEDBACK_SUMMARY_DIR,
        f"{safe_filename(certification)}_general.txt",
    )
    raw_path = os.path.join(
        FEEDBACK_DIR,
        f"{safe_filename(certification)}_{safe_filename(topic)}.txt",
    )

    if os.path.exists(summary_path):
        with open(summary_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    if os.path.exists(raw_path):
        return build_feedback_summary(certification, topic)

    if os.path.exists(general_path):
        with open(general_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    return ""


def get_local_reference_summary(certification: str, topic: str):
    # Prefer parsed PDF summaries (from parse_pdfs.py) if available
    def load_parsed_pdf_summaries(certification_name: str):
        pdf_summary_dir = os.path.join(LOCAL_REFERENCE_SUMMARY_DIR, "pdf")
        if not os.path.isdir(pdf_summary_dir):
            return ""

        cert_slug = safe_filename(certification_name)
        collected = []

        for fname in sorted(os.listdir(pdf_summary_dir)):
            lower = fname.lower()
            if cert_slug in lower:
                path = os.path.join(pdf_summary_dir, fname)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        collected.append(f.read())
                except Exception:
                    continue

        # If none matched by slug, include up to 3 recent parsed PDFs as general examples
        if not collected:
            for fname in sorted(os.listdir(pdf_summary_dir))[:3]:
                path = os.path.join(pdf_summary_dir, fname)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        collected.append(f.read())
                except Exception:
                    continue

        return "\n\n".join(collected)

    pdf_text = load_parsed_pdf_summaries(certification)

    file_paths = load_local_reference_files(certification)
    raw_text = read_local_reference_text(file_paths) if file_paths else ""

    combined = "\n\n".join([t for t in (pdf_text, raw_text) if t])
    if not combined:
        return ""

    return build_local_reference_summary(certification, topic, combined)


def extract_questions_from_markdown(text: str):
    parts = [part.strip() for part in text.split("\n---\n") if part.strip()]
    if parts and parts[0].startswith("# AWS"):
        parts = parts[1:]

    questions = []
    for part in parts:
        if len(part) < 50:
            continue
        if "Correct answer" in part or "Explanation" in part or "Question" in part:
            questions.append(part)
    return questions


def get_existing_output_questions(max_questions: int = 20):
    if not os.path.isdir(OUTPUT_DIR):
        return []

    collected = []
    for root, _, files in os.walk(OUTPUT_DIR):
        for filename in sorted(files):
            if not filename.lower().endswith(".md"):
                continue

            path = os.path.join(root, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            questions = extract_questions_from_markdown(content)
            for question in questions:
                if len(collected) >= max_questions:
                    return collected
                collected.append(question)

    return collected


def build_existing_question_reference(existing_questions: list[str]):
    if not existing_questions:
        return ""

    summary_lines = [
        "Existing questions from previous output files are shown below. Avoid producing duplicates or very similar questions.",
    ]
    for i, question in enumerate(existing_questions, start=1):
        short_text = question.replace("\n", " ").strip()
        if len(short_text) > 400:
            short_text = short_text[:400].rstrip() + "..."
        summary_lines.append(f"{i}. {short_text}")
    return "\n".join(summary_lines)


def select_certification():
    """Prompt the user to select an AWS certification exam."""
    print("\nAvailable Certifications:")
    option_index = 1
    options = []

    for category_name, items in CERTIFICATION_CATEGORIES:
        print(f"\n  {category_name}:")
        for cert_name, cert_description in items:
            print(f"    {option_index}. {cert_name}")
            options.append((cert_name, cert_description))
            option_index += 1

    while True:
        selection = input(f"\nSelect certification (1-{len(options)}): ").strip()
        if not selection.isdigit():
            print("  Please enter a number.")
            continue
        choice = int(selection)
        if 1 <= choice <= len(options):
            selected_cert, description = options[choice - 1]
            print(f"\nSelected certification: {selected_cert}")
            print(f"Description: {description}\n")
            return selected_cert
        print(f"  Please choose a number between 1 and {len(options)}")


def select_topic_for_certification(certification):
    """Select or enter a topic for the chosen certification."""
    if certification == "AWS Certified Solutions Architect – Associate (SAA-C03)":
        print("\nDomains:")
        print("  0. General (mix of all domains)")
        for i, (name, topics) in enumerate(SAA_C03_DOMAINS, 1):
            print(f"  {i}. {name}")

        while True:
            domain_choice = input(f"\nSelect domain (0-{len(SAA_C03_DOMAINS)}): ").strip()
            if not domain_choice.isdigit():
                print("  Please enter a number.")
                continue
            domain_index = int(domain_choice) - 1
            if domain_index == -1:
                return "General", "Mixed coverage across all SAA-C03 domains"
            if 0 <= domain_index < len(SAA_C03_DOMAINS):
                domain_name, topics = SAA_C03_DOMAINS[domain_index]
                break
            print(f"  Please choose a number between 0 and {len(SAA_C03_DOMAINS)}")

        print(f"\nTopics for {domain_name}:")
        for i, topic in enumerate(topics, 1):
            print(f"  {i}. {topic}")

        while True:
            topic_choice = input(f"\nSelect topic (1-{len(topics)}): ").strip()
            if not topic_choice.isdigit():
                print("  Please enter a number.")
                continue
            topic_index = int(topic_choice) - 1
            if 0 <= topic_index < len(topics):
                return domain_name, topics[topic_index]
            print(f"  Please choose a number between 1 and {len(topics)}")

    custom_topic = input(
        "\nEnter a focus area or topic for this certification (press Enter for 'General AWS exam topics'): "
    ).strip()
    return "General", custom_topic or "General AWS exam topics"


def generate_questions(aws_certification, topic, num_questions, start_id, allow_multi_select=False, reference_summary="", feedback_guidance=""):
    """Generate questions for a specific AWS certification."""
    if aws_certification not in CERTIFICATIONS:
        raise ValueError(
            f"Invalid certification: {aws_certification}. Please choose from: {', '.join(CERTIFICATIONS.keys())}"
        )

    certification_description = CERTIFICATIONS[aws_certification]
    blueprint_note = CERTIFICATION_BLUEPRINT_NOTES.get(
        aws_certification,
        "Use the official exam guide and blueprint for this certification."
    )

    if allow_multi_select:
        multi_select_note = (
            "Randomly make approximately 25-40% of questions multi-select (with either two or three correct choices). "
            "When a question is multi-select, explicitly phrase the stem to request the number of correct answers, e.g. 'Which two of the following would meet the requirement?' or 'Which three of the following would meet the requirement?'. "
            "Ensure the wording matches the number of correct options and that exactly that many choices are correct. For multi-select questions include clear phrasing such as 'Choose the two correct answers' or 'Choose the three correct answers', and list all correct choices in the answer section with explanations for each."
        )
    else:
        multi_select_note = "Generate standard single-answer multiple-choice questions with one correct answer and three plausible distractors."

    prompt = f"""You are an expert in AWS certifications. Generate {num_questions} multiple-choice questions for the AWS {aws_certification} certification exam.
Ensure the questions align with the exam's official Exam Guide or blueprint. Use the certification-specific guide and blueprint as the baseline for topic coverage, domain weighting, and question style.
Also use the available sample question examples as a guide to mimic the exam's style, length, formatting, and wording exactly.
Each question should include:
1. Domain or topic (aligned with the exam guide)
2. Question text (scenario + question)
3. Four options (A, B, C, D)
4. Correct answer(s)
5. Explanation of why it is correct
6. Why each wrong answer is wrong

Certification Description: {certification_description}
Blueprint Focus: {blueprint_note}
Topic / Focus Area: {topic}
Multi-Select Instructions: {multi_select_note}
"""

    if reference_summary:
        prompt += f"\nLocal Reference Summary:\n{reference_summary}\n"

    existing_questions = get_existing_output_questions(max_questions=20)
    existing_question_reference = build_existing_question_reference(existing_questions)
    if existing_question_reference:
        prompt += f"\n{existing_question_reference}\n"

    if feedback_guidance:
        prompt += f"\nSaved reviewer feedback for future alignment and improvement:\n{feedback_guidance}\n"

    prompt += "\nFormat clearly with \"---\" separators between questions.\nBegin generating now:"""

    print(
        f"\n  ⏳ Generating questions {start_id}-{start_id + num_questions - 1} for {aws_certification} certification..."
    )

    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=prompt,
        options={
            "temperature": 0.7,
            "top_p": 0.9,
            "num_predict": 4096,
        },
    )

    return response["response"]


def review_questions(raw_questions, batch_num, certification, topic, reference_summary=""):
    """Use the model to verify alignment with the certification exam guide and blueprint."""
    print(f"\nReviewing batch {batch_num} with AI validation...\n")

    prompt = f"""You are an expert AWS exam reviewer. Review the generated question batch for the certification below and verify accuracy, format, and alignment with the official exam guide/blueprint.

Certification: {certification}
Topic / Focus Area: {topic}

Review these questions and identify whether each one:
1. Matches the certification's exam guide or blueprint domains.
2. Uses correct AWS terminology and exam-style structure.
3. Includes one correct answer and three plausible wrong options.
4. Provides an accurate explanation for the correct answer.
5. Marks any question or answer that is inconsistent, incorrect, or not aligned.

If the batch is acceptable, respond with a short confirmation message only.
If issues are found, list the batch issues in numbered bullet points.

"""

    if reference_summary:
        prompt += f"Local Reference Summary for review:\n{reference_summary}\n\n"

    prompt += f"Batch content:\n{raw_questions}\n"

    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=prompt,
        options={
            "temperature": 0.0,
            "top_p": 0.5,
            "num_predict": 2048,
        },
    )

    review_result = response["response"].strip()
    print(review_result)

    feedback_path = save_review_feedback(certification, topic, review_result)
    print(f"\nSaved reviewer feedback to: {feedback_path}")

    if review_result.lower().startswith("issues") or "not aligned" in review_result.lower() or "incorrect" in review_result.lower():
        print("\nAI review found potential issues. Please inspect the generated batch manually.")
    else:
        print("\nAI review indicates the batch is aligned with the exam guide and blueprint.")

    return raw_questions

def save_questions(content, certification, domain, topic, num_questions):
    """Save questions to a markdown file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_cert = certification.replace(" ", "_").replace("–", "-").replace("/", "_").lower()
    safe_domain = domain.replace(" ", "_").replace("/", "_").lower()
    safe_topic = topic.replace(" ", "_").replace("/", "_").lower()
    filename = f"{safe_cert}_{safe_domain}_{safe_topic}_{num_questions}q_{timestamp}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# AWS {certification} Practice Questions\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Certification:** {certification}\n")
        f.write(f"**Domain:** {domain}\n")
        f.write(f"**Topic:** {topic}\n")
        f.write(f"**Total Questions:** {num_questions}\n")
        f.write(f"**Model:** {OLLAMA_MODEL}\n\n")
        f.write("---\n\n")
        f.write(content)

    print(f"\n✅ Questions saved to: {filepath}")
    print(f"   File size: {os.path.getsize(filepath) / 1024:.1f} KB")
    return filepath


def run_batch_generation(certification, domain, topic, total_questions, do_review=True, include_multi_select=False, reference_summary="", feedback_guidance=""):
    """Generate questions in batches."""

    batches = []
    remaining = total_questions
    start_id = 1
    batch_num = 1

    while remaining > 0:
        current_size = min(BATCH_SIZE, remaining)
        batches.append((batch_num, current_size, start_id))
        remaining -= current_size
        start_id += current_size
        batch_num += 1

    print(f"\n{'='*60}")
    print(f"  Generation Plan")
    print(f"  Certification: {certification}")
    print(f"  Total Questions: {total_questions}")
    print(f"  Batch Size: {BATCH_SIZE}")
    print(f"  Total Batches: {len(batches)}")
    print(f"  Estimated Time: {len(batches) * 2}-{len(batches) * 4} minutes")
    print(f"{'='*60}")

    all_content = []
    all_content.append(f"# AWS {certification} Practice Questions\n\n")
    all_content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    all_content.append(f"**Certification:** {certification}\n")
    all_content.append(f"**Domain:** {domain}\n")
    all_content.append(f"**Topic:** {topic}\n")
    all_content.append(f"**Total Questions:** {total_questions}\n")
    all_content.append(f"**Model:** {OLLAMA_MODEL}\n\n")
    all_content.append("---\n\n")
    
    successful = 0
    failed = 0
    
    for batch_num, num_q, start_id in batches:
        print(f"\n{'─'*40}")
        print(f"  Batch {batch_num}/{len(batches)} | Questions {start_id}-{start_id + num_q - 1}")
        print(f"{'─'*40}")
        
        try:
            raw_questions = generate_questions(
                certification,
                topic,
                num_q,
                start_id,
                include_multi_select,
                reference_summary,
            )

            if do_review:
                final_questions = review_questions(
                    raw_questions,
                    batch_num,
                    certification,
                    topic,
                    reference_summary,
                )
            else:
                final_questions = raw_questions
            
            all_content.append(f"## Batch {batch_num} (Questions {start_id}-{start_id + num_q - 1})\n\n")
            all_content.append(final_questions)
            all_content.append("\n\n---\n\n")
            
            successful += 1
            print(f"  ✅ Batch {batch_num} complete!")
            
        except Exception as e:
            print(f"  ❌ Batch {batch_num} failed: {e}")
            all_content.append(f"## Batch {batch_num} - FAILED\n\n")
            all_content.append(f"Error: {str(e)}\n\n---\n\n")
            failed += 1
        
        # Pause between batches
        if batch_num < len(batches):
            print(f"  ⏸ Pausing 3 seconds...")
            time.sleep(3)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"  GENERATION COMPLETE")
    print(f"  Successful: {successful}/{len(batches)} batches")
    if failed > 0:
        print(f"  Failed: {failed}/{len(batches)} batches")
    print(f"{'='*60}")
    
    return "".join(all_content)


def main():
    print("=" * 60)
    print("  AWS Exam Question Generator")
    print(f"  Supports 1-{MAX_QUESTIONS} questions per run")
    print("=" * 60)

    certification = select_certification()
    domain_name, topic = select_topic_for_certification(certification)

    while True:
        try:
            num_q = int(input(f"\nNumber of questions (1-{MAX_QUESTIONS}, default 5): ") or "5")
        except ValueError:
            print("  Please enter a valid number.")
            continue

        if 1 <= num_q <= MAX_QUESTIONS:
            break
        print(f"  Please enter a number between 1 and {MAX_QUESTIONS}")

    do_review = True

    print(f"\n{'─'*40}")
    print(f"  Certification: {certification}")
    print(f"  Domain: {domain_name}")
    print(f"  Topic: {topic}")
    print(f"  Questions: {num_q}")
    print(f"  Review: Yes")
    print(f"  Reference docs: Enabled")
    print(f"  Multi-select questions: Enabled")
    print(f"  Batches: {(num_q + BATCH_SIZE - 1) // BATCH_SIZE}")
    print(f"{'─'*40}")

    confirm = input("\nProceed? (y/n, default y): ").strip().lower() or "y"
    if confirm != "y":
        print("Cancelled.")
        return

    reference_summary = get_local_reference_summary(certification, topic)
    if reference_summary:
        print("\nLoaded local reference summary for prompt inclusion.")
    else:
        print("\nNo local reference documents found; continuing without them.")

    feedback_guidance = load_feedback_guidance(certification, topic)
    if feedback_guidance:
        print("\nLoaded saved reviewer feedback for prompt guidance.")
    else:
        print("\nNo saved reviewer feedback found for this certification/topic.")

    include_multi_select = True

    content = run_batch_generation(
        certification,
        domain_name,
        topic,
        num_q,
        do_review == "y",
        include_multi_select,
        reference_summary,
        feedback_guidance,
    )
    filepath = save_questions(content, certification, domain_name, topic, num_q)

    show_preview = input("\nShow preview of generated questions? (y/n, default y): ").strip().lower() or "y"
    if show_preview == "y":
        print("\n" + "=" * 60)
        print("PREVIEW (first 2000 characters):")
        print("=" * 60)
        print(content[:2000])
        if len(content) > 2000:
            print(f"\n... [{len(content) - 2000} more characters in file]")

    print(f"\n✅ Done! Full output saved to: {filepath}")


if __name__ == "__main__":
    main()