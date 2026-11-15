# DecisionTrace AI

### AI-Powered Meeting Decision & Commitment Intelligence
[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6)
![LLM](https://img.shields.io/badge/AI-LLM-blueviolet)
![RAG](https://img.shields.io/badge/Architecture-RAG-success)
![Embeddings](https://img.shields.io/badge/Embeddings-SentenceTransformers-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)
![API](https://img.shields.io/badge/LLM_API-OpenRouter-purple)

DecisionTrace AI is a Retrieval-Augmented Generation
(RAG) application that helps teams retrieve decisions,
responsibilities, and deadlines from meeting notes.

## Business Problem

Important decisions are often scattered across multiple
meeting documents. Teams may struggle to identify the
latest approved decision or the person responsible.

DecisionTrace AI retrieves relevant meeting evidence
and uses an LLM to generate an answer with source
references.

## Technologies

- Python
- Sentence Transformers (all-MiniLM-L6-v2)
- NumPy
- OpenRouter LLM API
- Streamlit
- Python unittest

## Features

1. Meeting document ingestion
2. Text chunking
3. 384-dimensional embeddings
4. Semantic search using cosine similarity
5. Retrieval-Augmented Generation
6. Grounded answers with source references
7. Interactive Streamlit dashboard
8. Automated unit tests

## Architecture

Meeting Notes (.txt)
       |
       v
Document Ingestion
       |
       v
Text Chunking
       |
       v
Sentence Transformer Embeddings
       |
       v
Semantic Search
       |
       v
Relevant Meeting Evidence
       |
       v
OpenRouter LLM
       |
       v
Generated Answer + Sources
       |
       v
Streamlit Dashboard

## Installation

Clone the repository and enter the project folder.

Create a virtual environment:

    python -m venv .venv

Activate on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

Copy .env.example to .env and configure:

    OPENROUTER_API_KEY=your_private_api_key
    OPENROUTER_MODEL=openrouter/free

Run the dashboard:

    python -m streamlit run app.py

## Testing

Run automated tests:

    python -m unittest discover -s tests -p "test_*.py" -v

Run the RAG demonstration:

    python test_rag.py

## Example Questions

- Why was the website launch postponed?
- Who approved the postponement?
- What is the latest approved launch date?
- Who is responsible for payment integration?

## Dataset

Three fictional meeting documents representing
NovaTech Solutions.

The data is synthetic and created for
demonstration purposes.

## Limitations

- Small sample dataset
- TXT files only
- Approximate similarity ranking
- LLM responses can contain errors
- Free model availability may vary
- Not intended for production use

## Security

API keys are stored locally in .env.
Private environment files are excluded from Git.

## Project Status

Local RAG pipeline and Streamlit application implemented.
Automated evaluation and GitHub publication are part
of the final verification process.
