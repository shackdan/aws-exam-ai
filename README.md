```markdown
# AWS SAP-C02 Exam Question Generator

An AI-powered multi-agent system that generates high-quality multiple-choice practice questions for the AWS Solutions Architect Associate (SAP-C02) certification exam.

Built with **Ollama** (local LLM) and **CrewAI** (multi-agent framework), this tool runs entirely on your local machine — no API keys or cloud services required.

---

## Features

- 🤖 **Multi-Agent Pipeline** — Three specialized AI agents (Author, Reviewer, Editor) collaborate to produce high-quality questions
- 📝 **1–100 Questions** per run with automatic batching
- 🎯 **All 4 SAP-C02 Domains** covered with topic-level selection
- 🔄 **Automatic Retry** for failed batches
- 📁 **Markdown Output** — Clean, formatted files ready for study
- 💻 **100% Local** — No internet required after initial model download

---

## Prerequisites

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| OS | Windows 10/11 | Windows 11 |
| RAM | 8 GB | 16 GB+ |
| Disk Space | 10 GB free | 20 GB free |
| Python | 3.11.x or 3.12.x | 3.11.9 |
| Ollama | Latest | Latest |

> ⚠️ **Important:** Python 3.13 and 3.14 are NOT compatible with CrewAI. Use Python 3.11 or 3.12.

---

## Installation

### Step 1: Install Ollama

1. Download from [https://ollama.com/download](https://ollama.com/download)
2. Run the installer and follow the prompts
3. Ollama will start automatically as a background service (check your system tray)

Verify installation:

```bash
ollama --version
```

### Step 2: Download an AI Model

Open **PowerShell** or **Command Prompt** and run:

```bash
ollama pull llama3.1:8b
```

This downloads the model (~4.7 GB). Wait for it to complete.

Verify the model is available:

```bash
ollama list
```

You should see `llama3.1:8b` in the list.

### Step 3: Install Python 3.11

> Skip this if you already have Python 3.11 or 3.12 installed.

1. Download Python 3.11.9 from [https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/)
2. Choose **"Windows installer (64-bit)"**
3. During installation:
   - ✅ Check **"Add Python to PATH"**
   - Click **"Customize installation"**
   - ✅ Check **"Install for all users"**
4. Complete the installation

Verify:

```bash
py -3.11 --version
```

Expected output: `Python 3.11.9`

### Step 4: Clone or Create the Project

```bash
mkdir C:\aws-exam-agent
cd C:\aws-exam-agent
```

Copy all project files into this directory. Your folder structure should look like:

```
C:\aws-exam-agent\
├── README.md
├── main.py
├── agents.py
├── tasks.py
├── config.py
├── simple_generator.py
├── batch_generator.py
├── requirements.txt
├── templates\
│   └── question_template.py
└── output\
    └── (generated files appear here)
```

### Step 5: Create the Virtual Environment

```bash
cd C:\aws-exam-agent
py -3.11 -m venv venv
```

### Step 6: Activate the Virtual Environment

```bash
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command prompt:

```
(venv) C:\aws-exam-agent>
```

> 📌 **You must activate the virtual environment every time you open a new terminal window.**

### Step 7: Upgrade pip

```bash
python -m pip install --upgrade pip setuptools wheel
```

### Step 8: Install Dependencies

**Option A — Using uv (recommended if pip has build errors):**

```bash
pip install uv
uv pip install crewai crewai-tools langchain langchain-community ollama pydantic rich json5
```

**Option B — Using pip directly:**

```bash
pip install crewai crewai-tools langchain langchain-community ollama pydantic rich json5
```

> If you get a `zstandard` build error with Option B, switch to Option A or install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) first.

### Step 9: Verify Installation

Run each of these commands one at a time:

```bash
python -c "import crewai; print(f'crewai {crewai.__version__}')"
python -c "import ollama; print('ollama OK')"
python -c "import rich; print('rich OK')"
python -c "import langchain; print('langchain OK')"
```

All lines should print without errors. If you see any import errors, revisit Step 8.

---

## Running the Application

### Step 1: Make Sure Ollama is Running

Check your Windows system tray for the Ollama icon. If it is not there, open a separate terminal and run:

```bash
ollama serve
```

Leave that terminal open.

### Step 2: Activate the Virtual Environment

Open a new terminal:

```bash
cd C:\aws-exam-agent
venv\Scripts\activate
```

### Step 3: Run the Generator

```bash
python main.py
```

### Step 4: Follow the Interactive Prompts

The application will guide you through the following steps:

1. **Select a domain** — Choose from the 4 SAP-C02 exam domains
2. **Select a topic** — Pick a specific topic or all topics within the domain
3. **Enter number of questions** — Between 1 and 100
4. **Review the generation plan** — See batch breakdown and time estimate
5. **Confirm and generate** — The agents will begin working

Example session:

```
┌─────────────────────────────────────────────────┐
│ AWS SAP-C02 Exam Question Generator             │
│ Powered by Ollama + CrewAI Multi-Agent System   │
│ Model: llama3.1:8b | Max Questions: 100         │
└─────────────────────────────────────────────────┘
✓ Ollama is running

Available SAP-C02 Domains:

  1. Design Secure Architectures (30%)
  2. Design Resilient Architectures (26%)
  3. Design High-Performing Architectures (24%)
  4. Design Cost-Optimized Architectures (20%)
  5. All Domains (mixed)

Select domain: 2

Available Topics:

  1. Design scalable and loosely coupled architectures
  2. Design highly available and fault-tolerant architectures
  3. All topics in this domain

Select topic: 1

How many questions to generate? (1-100): 20
```

The generation plan will display:

```
Generation Configuration:
  Domain: Design Resilient Architectures
  Topic: Design scalable and loosely coupled architectures
  Total Questions: 20
  Batch Size: 5
  Total Batches: 4

┌───────┬───────────┬──────────────┐
│ Batch │ Questions │ Question IDs │
├───────┼───────────┼──────────────┤
│   1   │     5     │    1 - 5     │
│   2   │     5     │    6 - 10    │
│   3   │     5     │   11 - 15    │
│   4   │     5     │   16 - 20    │
└───────┴───────────┴──────────────┘

⏱ Estimated time: 12-24 minutes

Proceed with generation? [y/n]: y
```

### Step 5: Wait for Generation

The system processes each batch through three agents:

1. **Question Author** — Creates scenario-based questions
2. **Technical Reviewer** — Validates AWS accuracy
3. **Quality Editor** — Polishes formatting and clarity

You will see verbose output as each agent works. This is normal. Each batch of 5 questions typically takes 2–5 minutes depending on your hardware.

### Step 6: Find Your Output

When generation completes, the questions are saved to the `output/` folder:

```
output/
├── questions_design_resilient_architectures_20q_20260807_143022.md
└── questions_design_resilient_architectures_20q_20260807_143022_answer_key.md
```

Open the `.md` file in any text editor or Markdown viewer to review your questions.

---

## Alternative: Simple Generator (No CrewAI)

If you want a lighter-weight option that only requires the `ollama` and `rich` packages:

```bash
pip install ollama rich
python simple_generator.py
```

This uses a single model call per batch (no multi-agent review pipeline) but is faster and has fewer dependencies.

---

## Configuration

Edit `config.py` to customize the application behavior:

```python
# Change the model (must be pulled first with 'ollama pull <model>')
OLLAMA_MODEL = "llama3.1:8b"       # Default, good balance
# OLLAMA_MODEL = "llama3.1:70b"    # Better quality, needs 48GB+ RAM
# OLLAMA_MODEL = "mistral:7b"      # Alternative, good for structured output

# Adjust batch size (questions per LLM call)
BATCH_SIZE = 5                      # Default, optimal for quality
# BATCH_SIZE = 10                   # Faster but may reduce quality

# Maximum questions allowed per run
MAX_QUESTIONS = 100
```

To use a different model, pull it first:

```bash
ollama pull mistral:7b
```

Then update the `OLLAMA_MODEL` value in `config.py`.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `Cannot connect to Ollama` | Make sure Ollama is running. Check system tray or run `ollama serve` in a separate terminal. |
| `Model not found` | Run `ollama pull llama3.1:8b` to download the model. |
| `Python version error / Pydantic V1 error` | You are using Python 3.13 or 3.14. Recreate your venv with Python 3.11 or 3.12. |
| `Import errors after install` | Make sure the venv is activated. You should see `(venv)` in your prompt. |
| `Out of memory` | Use a smaller model. Run `ollama pull phi3:mini` and update `config.py`. |
| `Slow generation` | Normal for CPU-only systems. Each batch takes 2–5 minutes. Consider a smaller model or reduce batch count. |
| `zstandard build error during pip install` | Use `uv pip install` instead of `pip install`. |
| `Batch failed during generation` | The app will offer to retry failed batches. If the problem persists, reduce `BATCH_SIZE` in `config.py`. |

### Checking Ollama Status

```bash
# Is Ollama running?
curl http://localhost:11434/api/tags

# What models are available?
ollama list

# Test a model directly
ollama run llama3.1:8b "What is AWS Lambda?"
```

### Resetting the Environment

If things get broken and you need to start fresh:

```bash
cd C:\aws-exam-agent
deactivate
rmdir /s /q venv
py -3.11 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
pip install uv
uv pip install crewai crewai-tools langchain langchain-community ollama pydantic rich json5
```

---

## Project Files Reference

| File | Purpose |
|------|---------|
| `README.md` | This file — setup and usage instructions |
| `main.py` | Main entry point — interactive CLI with multi-agent batching |
| `agents.py` | Defines the 3 AI agents (Author, Reviewer, Editor) |
| `tasks.py` | Defines what each agent does per batch |
| `config.py` | All configuration (model, domains, batch size, limits) |
| `simple_generator.py` | Lightweight alternative without CrewAI |
| `batch_generator.py` | Automated batch generation across all domains |
| `templates/question_template.py` | Pydantic schemas and format templates |
| `output/` | Directory where generated question files are saved |

---

## Tips for Best Results

1. **Start small** — Generate 5 questions first to verify quality before doing larger batches
2. **Verify answers** — Always spot-check a few answers against [AWS documentation](https://docs.aws.amazon.com/)
3. **Use larger models** for better quality if your hardware supports it
4. **Mix domains** — The real exam covers all 4 domains in a single sitting
5. **Review the explanations** — They are educational even if you already know the answer
6. **Run multiple times** — Each run produces different questions, so you can build a large question bank over time

---

## Exam Domain Weights (SAP-C02)

| Domain | Weight |
|--------|--------|
| Design Secure Architectures | 30% |
| Design Resilient Architectures | 26% |
| Design High-Performing Architectures | 24% |
| Design Cost-Optimized Architectures | 20% |

Generate questions proportionally to these weights for the most realistic practice experience. For example, in a set of 50 questions: 15 security, 13 resilience, 12 performance, 10 cost.

---

## License

This project is for personal educational use. Generated questions are AI-created and should be verified against official AWS documentation before use in any formal setting.
```