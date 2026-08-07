# main.py
"""Main entry point for the AWS SAA-C03 Exam Question Generator"""

import os
import sys
import time
from datetime import datetime
from crewai import Crew, Process
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskID
from rich.table import Table

from config import SAA_C03_DOMAINS, OUTPUT_DIR, OLLAMA_MODEL, MAX_QUESTIONS, MIN_QUESTIONS, BATCH_SIZE
from agents import create_question_author, create_technical_reviewer, create_quality_editor
from tasks import create_generation_task, create_review_task, create_editing_task

console = Console()


def display_banner():
    """Display the application banner"""
    console.print(Panel.fit(
        "[bold blue]AWS SAA-C03 Exam Question Generator[/bold blue]\n"
        "[dim]Powered by Ollama + CrewAI Multi-Agent System[/dim]\n"
        f"[dim]Model: {OLLAMA_MODEL} | Max Questions: {MAX_QUESTIONS}[/dim]",
        border_style="blue"
    ))


def select_domain():
    """Let user select which domain to generate questions for"""
    console.print("\n[bold]Available SAA-C03 Domains:[/bold]\n")
    
    domains = list(SAA_C03_DOMAINS.items())
    for i, (key, domain) in enumerate(domains, 1):
        console.print(f"  {i}. {domain['name']} ({domain['weight']})")
    
    console.print(f"  {len(domains) + 1}. All Domains (mixed)")
    
    choice = IntPrompt.ask(
        "\nSelect domain",
        choices=[str(i) for i in range(1, len(domains) + 2)],
        default="1"
    )
    
    if choice == len(domains) + 1:
        return "all", "All Domains", "Mixed topics"
    
    domain_key = domains[choice - 1][0]
    domain_data = domains[choice - 1][1]
    return domain_key, domain_data['name'], domain_data['topics']


def select_topic(topics):
    """Let user select a specific topic within a domain"""
    if topics == "Mixed topics":
        return "Mixed topics across all domains"
    
    console.print("\n[bold]Available Topics:[/bold]\n")
    for i, topic in enumerate(topics, 1):
        console.print(f"  {i}. {topic}")
    console.print(f"  {len(topics) + 1}. All topics in this domain")
    
    choice = IntPrompt.ask(
        "\nSelect topic",
        choices=[str(i) for i in range(1, len(topics) + 2)],
        default="1"
    )
    
    if choice == len(topics) + 1:
        return "All topics in this domain"
    
    return topics[choice - 1]


def get_num_questions():
    """Get the number of questions to generate with validation"""
    while True:
        num = IntPrompt.ask(
            f"\nHow many questions to generate? ({MIN_QUESTIONS}-{MAX_QUESTIONS})",
            default=5
        )
        if MIN_QUESTIONS <= num <= MAX_QUESTIONS:
            return num
        else:
            console.print(f"[red]Please enter a number between {MIN_QUESTIONS} and {MAX_QUESTIONS}[/red]")


def calculate_batches(total_questions, batch_size=BATCH_SIZE):
    """Calculate how to split questions into batches"""
    batches = []
    remaining = total_questions
    batch_num = 1
    start_id = 1
    
    while remaining > 0:
        current_batch_size = min(batch_size, remaining)
        batches.append({
            "batch_number": batch_num,
            "num_questions": current_batch_size,
            "start_id": start_id,
        })
        remaining -= current_batch_size
        start_id += current_batch_size
        batch_num += 1
    
    return batches


def display_generation_plan(domain_name, topic, num_questions, batches):
    """Display the generation plan to the user"""
    table = Table(title="Generation Plan")
    table.add_column("Batch", style="cyan", justify="center")
    table.add_column("Questions", style="green", justify="center")
    table.add_column("Question IDs", style="yellow", justify="center")
    
    for batch in batches:
        table.add_row(
            str(batch["batch_number"]),
            str(batch["num_questions"]),
            f"{batch['start_id']} - {batch['start_id'] + batch['num_questions'] - 1}"
        )
    
    console.print(f"\n[bold]Generation Configuration:[/bold]")
    console.print(f"  Domain: {domain_name}")
    console.print(f"  Topic: {topic}")
    console.print(f"  Total Questions: {num_questions}")
    console.print(f"  Batch Size: {BATCH_SIZE}")
    console.print(f"  Total Batches: {len(batches)}")
    console.print()
    console.print(table)
    
    if num_questions > 20:
        estimated_time = len(batches) * 3  # ~3 minutes per batch estimate
        console.print(f"\n[yellow]⏱ Estimated time: {estimated_time}-{estimated_time * 2} minutes[/yellow]")


def run_single_batch(domain_name, topic, batch_info):
    """Run the multi-agent pipeline for a single batch"""
    
    batch_num = batch_info["batch_number"]
    num_questions = batch_info["num_questions"]
    start_id = batch_info["start_id"]
    
    # Create agents
    author = create_question_author()
    reviewer = create_technical_reviewer()
    editor = create_quality_editor()
    
    # Create tasks
    generation_task = create_generation_task(
        author, domain_name, topic, num_questions, batch_num, start_id
    )
    review_task = create_review_task(reviewer, [generation_task])
    editing_task = create_editing_task(editor, [generation_task, review_task])
    
    # Create and run the crew
    crew = Crew(
        agents=[author, reviewer, editor],
        tasks=[generation_task, review_task, editing_task],
        process=Process.sequential,
        verbose=True,
    )
    
    # Execute
    result = crew.kickoff()
    
    return result


def run_question_generation(domain_name, topic, num_questions):
    """Run the full question generation pipeline with batching"""
    
    batches = calculate_batches(num_questions)
    all_results = []
    failed_batches = []
    
    console.print(f"\n[bold green]Starting question generation...[/bold green]")
    console.print(f"  Model: {OLLAMA_MODEL}")
    console.print(f"  Domain: {domain_name}")
    console.print(f"  Topic: {topic}")
    console.print(f"  Total Questions: {num_questions}")
    console.print(f"  Batches: {len(batches)}")
    console.print(f"\n[dim]This may take a while for large sets...[/dim]\n")
    
    for i, batch_info in enumerate(batches):
        batch_num = batch_info["batch_number"]
        batch_questions = batch_info["num_questions"]
        start_id = batch_info["start_id"]
        
        console.print(f"\n{'='*60}")
        console.print(
            f"[bold cyan]  Batch {batch_num}/{len(batches)} | "
            f"Questions {start_id}-{start_id + batch_questions - 1} | "
            f"Generating {batch_questions} questions[/bold cyan]"
        )
        console.print(f"{'='*60}\n")
        
        try:
            result = run_single_batch(domain_name, topic, batch_info)
            all_results.append({
                "batch_number": batch_num,
                "start_id": start_id,
                "num_questions": batch_questions,
                "result": str(result),
                "status": "success"
            })
            console.print(f"\n[green]✓ Batch {batch_num} complete![/green]")
            
        except Exception as e:
            console.print(f"\n[red]✗ Batch {batch_num} failed: {e}[/red]")
            failed_batches.append(batch_num)
            all_results.append({
                "batch_number": batch_num,
                "start_id": start_id,
                "num_questions": batch_questions,
                "result": f"FAILED: {str(e)}",
                "status": "failed"
            })
        
        # Brief pause between batches to avoid overwhelming the model
        if i < len(batches) - 1:
            console.print(f"[dim]  Pausing 5 seconds before next batch...[/dim]")
            time.sleep(5)
    
    # Summary
    successful = len([r for r in all_results if r["status"] == "success"])
    console.print(f"\n{'='*60}")
    console.print(f"[bold]Generation Complete![/bold]")
    console.print(f"  Successful batches: {successful}/{len(batches)}")
    if failed_batches:
        console.print(f"  [red]Failed batches: {failed_batches}[/red]")
    console.print(f"{'='*60}")
    
    return all_results


def save_output(all_results, domain_name, topic, num_questions):
    """Save all generated questions to a single file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_domain = domain_name.replace(" ", "_").lower()
    filename = f"questions_{safe_domain}_{num_questions}q_{timestamp}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    successful_results = [r for r in all_results if r["status"] == "success"]
    failed_results = [r for r in all_results if r["status"] == "failed"]
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# AWS SAA-C03 Practice Questions\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Domain:** {domain_name}\n")
        f.write(f"**Topic:** {topic}\n")
        f.write(f"**Model:** {OLLAMA_MODEL}\n")
        f.write(f"**Total Questions Requested:** {num_questions}\n")
        f.write(f"**Batches Successful:** {len(successful_results)}/{len(all_results)}\n")
        
        if failed_results:
            f.write(f"**Failed Batches:** {[r['batch_number'] for r in failed_results]}\n")
        
        f.write("\n---\n\n")
        
        for result in successful_results:
            f.write(f"## Batch {result['batch_number']} ")
            f.write(f"(Questions {result['start_id']}-{result['start_id'] + result['num_questions'] - 1})\n\n")
            f.write(result["result"])
            f.write("\n\n---\n\n")
    
    console.print(f"\n[bold green]✓ Questions saved to:[/bold green] {filepath}")
    console.print(f"  File size: {os.path.getsize(filepath) / 1024:.1f} KB")
    
    # Also save a separate answer key
    answer_key_path = filepath.replace(".md", "_answer_key.md")
    with open(answer_key_path, "w", encoding="utf-8") as f:
        f.write(f"# Answer Key - AWS SAA-C03 Practice Questions\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Domain:** {domain_name}\n")
        f.write(f"**Topic:** {topic}\n\n")
        f.write("---\n\n")
        f.write("*Review the main question file for full explanations.*\n\n")
        for result in successful_results:
            f.write(f"### Batch {result['batch_number']}\n\n")
            f.write(result["result"])
            f.write("\n\n")
    
    console.print(f"[bold green]✓ Answer key saved to:[/bold green] {answer_key_path}")
    
    return filepath


def retry_failed_batches(all_results, domain_name, topic):
    """Offer to retry any failed batches"""
    failed = [r for r in all_results if r["status"] == "failed"]
    
    if not failed:
        return all_results
    
    retry = Prompt.ask(
        f"\n[yellow]{len(failed)} batch(es) failed. Retry them?[/yellow]",
        choices=["y", "n"],
        default="y"
    )
    
    if retry == "n":
        return all_results
    
    console.print("\n[bold]Retrying failed batches...[/bold]")
    
    for i, result in enumerate(all_results):
        if result["status"] == "failed":
            batch_info = {
                "batch_number": result["batch_number"],
                "num_questions": result["num_questions"],
                "start_id": result["start_id"],
            }
            
            console.print(f"\n  Retrying batch {result['batch_number']}...")
            
            try:
                retry_result = run_single_batch(domain_name, topic, batch_info)
                all_results[i] = {
                    "batch_number": result["batch_number"],
                    "start_id": result["start_id"],
                    "num_questions": result["num_questions"],
                    "result": str(retry_result),
                    "status": "success"
                }
                console.print(f"  [green]✓ Batch {result['batch_number']} succeeded on retry![/green]")
            except Exception as e:
                console.print(f"  [red]✗ Batch {result['batch_number']} failed again: {e}[/red]")
            
            time.sleep(5)
    
    return all_results


def main():
    """Main application loop"""
    display_banner()
    
    # Check if Ollama is running
    try:
        import ollama
        ollama.list()
        console.print("[green]✓ Ollama is running[/green]")
    except Exception as e:
        console.print(f"[red]✗ Cannot connect to Ollama: {e}[/red]")
        console.print("[yellow]Make sure Ollama is running (check system tray)[/yellow]")
        sys.exit(1)
    
    while True:
        # Select domain
        domain_key, domain_name, topics = select_domain()
        
        # Select topic
        topic = select_topic(topics)
        
        # Number of questions (now supports up to 100)
        num_questions = get_num_questions()
        
        # Calculate and display plan
        batches = calculate_batches(num_questions)
        display_generation_plan(domain_name, topic, num_questions, batches)
        
        # Confirm
        confirm = Prompt.ask("\nProceed with generation?", choices=["y", "n"], default="y")
        
        if confirm == "y":
            # Run generation
            all_results = run_question_generation(domain_name, topic, num_questions)
            
            # Retry failed batches
            all_results = retry_failed_batches(all_results, domain_name, topic)
            
            # Save output
            save_output(all_results, domain_name, topic, num_questions)
        
        # Continue?
        again = Prompt.ask("\nGenerate more questions?", choices=["y", "n"], default="n")
        if again == "n":
            console.print("\n[bold blue]Thank you! Good luck on your SAA-C03 exam![/bold blue]")
            break


if __name__ == "__main__":
    main()