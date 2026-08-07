# AWS SAA-C03 Exam Question Generator

An AI-powered multi-agent system that generates high-quality multiple-choice practice questions for the AWS Solutions Architect Associate (SAA-C03) certification exam.

Built with **Ollama** (local LLM) and **CrewAI** (multi-agent framework), this tool runs entirely on your local machine — no API keys or cloud services required.

---

## Features

- 🤖 **Multi-Agent Pipeline** — Three specialized AI agents (Author, Reviewer, Editor) collaborate to produce high-quality questions
- 📝 **1–100 Questions** per run with automatic batching
- 🎯 **All 4 SAA-C03 Domains** covered with topic-level selection
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