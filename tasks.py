# tasks.py
"""Define tasks for the exam question generation pipeline"""

from crewai import Task


def create_generation_task(agent, domain_name, topic, num_questions=5, batch_number=1, start_id=1):
    """Task for generating initial questions"""
    return Task(
        description=f"""Generate {num_questions} multiple-choice exam questions for the 
        AWS Solutions Architect Associate (SAA-C03) exam.

        **Domain:** {domain_name}
        **Topic:** {topic}
        **Batch:** {batch_number}
        **Starting Question Number:** {start_id}

        Requirements for each question:
        1. Must be scenario-based (describe a real-world situation)
        2. Must have exactly 4 answer options (A, B, C, D)
        3. Must have exactly ONE correct answer
        4. Distractors should be plausible but clearly incorrect to someone who knows the material
        5. Questions should test understanding, not memorization
        6. Use current AWS service names and features
        7. Include a mix of "which service" and "which architecture" questions
        8. Scenarios should involve realistic business requirements
        9. Do NOT repeat scenarios or questions from previous batches
        10. Each question should cover a DIFFERENT aspect of the topic

        For EACH question, provide:
        - Question number (starting from {start_id})
        - The scenario/question text (2-4 sentences)
        - Four answer options (A, B, C, D)
        - The correct answer letter
        - A detailed explanation (2-3 sentences explaining WHY it's correct)
        - Brief note on why each wrong answer is wrong

        Format each question clearly with labels and separators.""",
        expected_output=f"""{num_questions} well-formatted AWS SAA-C03 exam questions 
        (numbered {start_id} to {start_id + num_questions - 1}) with answers and 
        explanations, focused on {domain_name} - {topic}.""",
        agent=agent,
    )


def create_review_task(agent, context_tasks):
    """Task for technical review of generated questions"""
    return Task(
        description="""Review the generated AWS exam questions for technical accuracy.

        For each question, verify:
        1. The correct answer is definitively correct based on current AWS documentation
        2. No answer option contains outdated service information
        3. Service names are current and correctly spelled
        4. Service behaviors described match actual AWS behavior
        5. Pricing/cost references are accurate
        6. Region/availability information is correct
        7. There is no ambiguity where multiple answers could be correct
        8. The scenario is realistic and makes technical sense
        9. No duplicate or overly similar questions exist in the batch

        If you find issues:
        - Flag the question number
        - Explain the technical issue
        - Provide the correction
        - If the correct answer is wrong, provide the right answer with justification

        If a question passes review, mark it as "APPROVED".
        
        Output ALL questions (corrected if needed) with their approval status.
        Maintain the original question numbering.""",
        expected_output="""All questions reviewed with APPROVED/NEEDS CORRECTION status, 
        with corrections applied where needed. Each question should be technically accurate.
        Original question numbers preserved.""",
        agent=agent,
        context=context_tasks,
    )


def create_editing_task(agent, context_tasks):
    """Task for quality editing of reviewed questions"""
    return Task(
        description="""Edit and finalize the reviewed AWS exam questions for quality and format.

        For each question, ensure:
        1. Question stem is clear and unambiguous
        2. All options are grammatically parallel
        3. No option is significantly longer/shorter than others
        4. No absolute words (always, never) unless technically accurate
        5. Options are in logical order
        6. The scenario doesn't contain unnecessary information
        7. Proper AWS terminology is used throughout
        8. The explanation is educational and would help a student learn
        9. Question numbering is preserved correctly

        Output the FINAL version of each question in this exact format:

        ---
        QUESTION [number]:
        Domain: [domain name]
        Topic: [topic]
        
        [Scenario and question text]

        A. [option]
        B. [option]
        C. [option]
        D. [option]

        Correct Answer: [letter]

        Explanation: [detailed explanation]

        Why other options are incorrect:
        - [letter]: [reason]
        - [letter]: [reason]  
        - [letter]: [reason]

        AWS Services Covered: [list of services]
        ---""",
        expected_output="""Final formatted set of exam questions ready for use, 
        with consistent formatting, clear wording, and educational explanations.
        All question numbers preserved.""",
        agent=agent,
        context=context_tasks,
    )