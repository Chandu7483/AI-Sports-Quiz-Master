# AI Sports Quiz Generator

## Overview
AI Sports Quiz Generator is a Retrieval-Augmented Generation (RAG) application that generates sports quizzes using:
- Google Gemini
- ChromaDB
- Sentence Transformers
- DuckDuckGo Search
- Gradio

## Features
- AI-generated sports quizzes
- Local knowledge retrieval using ChromaDB
- Live web search
- Interactive Gradio interface

## Project Structure

```
sports-quiz-agent/
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Environment Variable

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```