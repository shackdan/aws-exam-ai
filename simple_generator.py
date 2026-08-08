# simple_generator.py
"""Simple AWS SAA-C03 Question Generator using Ollama directly - supports up to 100 questions"""

import ollama
import os
import time
from datetime import datetime

OLLAMA_MODEL = "llama3.1:8b"
OUTPUT_DIR = "output"
MAX_QUESTIONS = 100
BATCH_SIZE = 5


def generate_questions(domain, topic, num_questions=5, start_id=1, batch_num=1):
    """Generate questions using a single prompt with role-playing"""
    
    prompt = f"""You are an expert AWS Solutions Architect and exam question writer. 
Generate {num_questions} high-quality multiple-choice questions for the AWS Solutions 
Architect Associate (SAA-C03) exam.

Domain: {domain}
Topic: {topic}
Batch: {batch_num}
Question Numbers: {start_id} to {start_id + num_questions - 1}

Requirements:
- Each question must be scenario-based (2-4 sentence real-world scenario)
- Exactly 4 options (A, B, C, D) with ONE correct answer
- Distractors must be plausible but clearly wrong
- Test understanding, not memorization
- Use current AWS service names
- Each question must cover a DIFFERENT aspect of the topic
- Number questions starting from {start_id}

For each question provide:
1. Question number (starting from {start_id})
2. Question text (scenario + question)
3. Four options (A, B, C, D)
4. Correct answer
5. Explanation of why it's correct
6. Why each wrong answer is wrong

Format clearly with "---" separators between questions.
Begin generating now:"""

    print(f"\n  ⏳ Generating questions {start_id}-{start_id + num_questions - 1}...")
    
    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=prompt,
        options={
            "temperature": 0.7,
            "top_p": 0.9,
            "num_predict": 4096,
        }
    )
    
    return response['response']


def review_questions(questions_text, batch_num=1):
    """Review generated questions for accuracy"""
    
    review_prompt = f"""You are an AWS Principal Solutions Architect reviewing exam questions 
for technical accuracy. Review the following questions (Batch {batch_num}) and:

1. Verify each correct answer is actually correct
2. Check for outdated AWS information
3. Ensure no ambiguity exists
4. Fix any issues found
5. Preserve question numbering exactly

If a question is correct, mark it [APPROVED].
If it needs changes, mark it [CORRECTED] and provide the fix.

Questions to review:
{questions_text}

Provide your reviewed and corrected version of ALL questions with original numbering:"""

    print(f"  ⏳ Reviewing batch {batch_num} for technical accuracy...")
    
    response = ollama.generate(
        model=OLLAMA_MODEL,
        prompt=review_prompt,
        options={
            "temperature": 0.3,
            "num_predict": 4096,
        }
    )
    
    return response['response']


def save_questions(content, domain, topic, num_questions):
    """Save questions to markdown file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_domain = domain.replace(" ", "_").lower()
    filename = f"saa_c03_{safe_domain}_{num_questions}q_{timestamp}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"\n✅ Questions saved to: {filepath}")
    print(f"   File size: {os.path.getsize(filepath) / 1024:.1f} KB")
    return filepath


def run_batch_generation(domain, topic, total_questions, do_review=True):
    """Generate questions in batches"""
    
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
    print(f"  Total Questions: {total_questions}")
    print(f"  Batch Size: {BATCH_SIZE}")
    print(f"  Total Batches: {len(batches)}")
    print(f"  Estimated Time: {len(batches) * 2}-{len(batches) * 4} minutes")
    print(f"{'='*60}")
    
    all_content = []
    all_content.append(f"# AWS SAA-C03 Practice Questions\n\n")
    all_content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
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
            # Generate
            raw_questions = generate_questions(domain, topic, num_q, start_id, batch_num)
            
            # Review (optional)
            if do_review:
                final_questions = review_questions(raw_questions, batch_num)
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
    print("  AWS SAA-C03 Exam Question Generator")
    print(f"  Supports 1-{MAX_QUESTIONS} questions per run")
    print("=" * 60)
    
    # Domain selection
    domains = [
        ("Design Secure Architectures", [
            "Secure access to AWS resources",
            "Secure workloads and applications",
            "Data security controls"
        ]),
        ("Design Resilient Architectures", [
            "Scalable and loosely coupled architectures",
            "Highly available and fault-tolerant architectures"
        ]),
        ("Design High-Performing Architectures", [
            "High-performing storage solutions",
            "Elastic compute solutions",
            "High-performing database solutions",
            "Scalable network architectures"
        ]),
        ("Design Cost-Optimized Architectures", [
            "Cost-optimized storage solutions",
            "Cost-optimized compute solutions",
            "Cost-optimized database solutions"
        ]),
    ]
    
    print("\nDomains:")
    for i, (name, _) in enumerate(domains, 1):
        print(f"  {i}. {name}")
    
    domain_choice = int(input("\nSelect domain (1-4): ")) - 1
    domain_name, topics = domains[domain_choice]
    
    print(f"\nTopics for {domain_name}:")
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. {topic}")
    
    topic_choice = int(input(f"\nSelect topic (1-{len(topics)}): ")) - 1
    topic = topics[topic_choice]
    
    # Number of questions with validation
    while True:
        num_q = int(input(f"\nNumber of questions (1-{MAX_QUESTIONS}, default 5): ") or "5")
        if 1 <= num_q <= MAX_QUESTIONS:
            break
        print(f"  Please enter a number between 1 and {MAX_QUESTIONS}")
    
    # Review option
    do_review = input("\nReview questions for accuracy? (y/n, default y): ").lower() or "y"
    
    # Confirm
    print(f"\n{'─'*40}")
    print(f"  Domain: {domain_name}")
    print(f"  Topic: {topic}")
    print(f"  Questions: {num_q}")
    print(f"  Review: {'Yes' if do_review == 'y' else 'No'}")
    print(f"  Batches: {(num_q + BATCH_SIZE - 1) // BATCH_SIZE}")
    print(f"{'─'*40}")
    
    confirm = input("\nProceed? (y/n, default y): ").lower() or "y"
    if confirm != "y":
        print("Cancelled.")
        return
    
    # Generate
    content = run_batch_generation(domain_name, topic, num_q, do_review == "y")
    
    # Save
    filepath = save_questions(content, domain_name, topic, num_q)
    
    # Display preview
    show_preview = input("\nShow preview of generated questions? (y/n, default y): ").lower() or "y"
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