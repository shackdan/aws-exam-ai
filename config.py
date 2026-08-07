# config.py
"""Configuration for the AWS Exam Question Generator"""

# Ollama Configuration
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.1:8b"  # Change to "llama3.1:70b" if you have resources

# SAA-C03 Exam Domains and Weightings
SAA_C03_DOMAINS = {
    "domain_1": {
        "name": "Design Secure Architectures",
        "weight": "30%",
        "topics": [
            "Secure access to AWS resources",
            "Secure workloads and applications",
            "Determine appropriate data security controls",
        ]
    },
    "domain_2": {
        "name": "Design Resilient Architectures",
        "weight": "26%",
        "topics": [
            "Design scalable and loosely coupled architectures",
            "Design highly available and fault-tolerant architectures",
        ]
    },
    "domain_3": {
        "name": "Design High-Performing Architectures",
        "weight": "24%",
        "topics": [
            "Determine high-performing and scalable storage solutions",
            "Design high-performing and elastic compute solutions",
            "Determine high-performing database solutions",
            "Determine high-performing and scalable network architectures",
            "Determine high-performing data ingestion and transformation solutions",
        ]
    },
    "domain_4": {
        "name": "Design Cost-Optimized Architectures",
        "weight": "20%",
        "topics": [
            "Design cost-optimized storage solutions",
            "Design cost-optimized compute solutions",
            "Design cost-optimized database solutions",
            "Design cost-optimized network architectures",
        ]
    }
}

# Question Generation Settings
MAX_QUESTIONS = 100
MIN_QUESTIONS = 1
BATCH_SIZE = 5  # Questions per LLM call (optimal for quality)
DIFFICULTY_LEVELS = ["Associate"]
OUTPUT_DIR = "output"