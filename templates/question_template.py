# templates/question_template.py
"""Templates and schemas for exam questions"""

from pydantic import BaseModel, Field
from typing import List, Optional


class ExamQuestion(BaseModel):
    """Schema for a single AWS exam question"""
    question_id: int = Field(description="Unique question identifier")
    domain: str = Field(description="SAP-C02 domain this question belongs to")
    topic: str = Field(description="Specific topic within the domain")
    difficulty: str = Field(description="Difficulty level", default="Associate")
    question_text: str = Field(description="The question stem")
    option_a: str = Field(description="Answer option A")
    option_b: str = Field(description="Answer option B")
    option_c: str = Field(description="Answer option C")
    option_d: str = Field(description="Answer option D")
    correct_answer: str = Field(description="The correct answer letter (A, B, C, or D)")
    explanation: str = Field(description="Detailed explanation of why the answer is correct")
    why_others_wrong: str = Field(description="Brief explanation of why other options are incorrect")
    aws_services: List[str] = Field(description="AWS services referenced in this question")


class QuestionSet(BaseModel):
    """A set of exam questions"""
    questions: List[ExamQuestion]
    domain_focus: str
    total_questions: int


QUESTION_FORMAT_TEMPLATE = """
## Question {question_id}

**Domain:** {domain}
**Topic:** {topic}

{question_text}

A. {option_a}
B. {option_b}
C. {option_c}
D. {option_d}

**Correct Answer:** {correct_answer}

**Explanation:** {explanation}

**Why other options are incorrect:** {why_others_wrong}

**AWS Services:** {aws_services}

---
"""