# 🏆 AI Sports Quiz Master

An AI-powered Sports Quiz application that generates dynamic quizzes using **Retrieval-Augmented Generation (RAG)**. The application combines a local knowledge base, vector search, live web search, and Google's Gemini AI to create interactive sports quizzes.

---

## 🚀 Features

- 🎯 Dynamic AI-generated sports quizzes
- 🏏 Multiple sports support
- 📊 Three difficulty levels (Easy, Medium, Hard)
- 🔢 Multiple question count options
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔍 ChromaDB vector database for semantic search
- 🌐 Live web search using DuckDuckGo
- 🤖 Google Gemini for quiz generation
- 💡 Explanations and interesting facts for every question
- 🖥️ Interactive Gradio interface

---

## 🛠️ Tech Stack

- Python
- Gradio
- Google Gemini API
- ChromaDB
- Sentence Transformers
- DuckDuckGo Search
- Transformers
- Dotenv

---

## 📂 Project Structure

```
AI-Sports-Quiz-Master/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── assets/
├── data/
│   ├── sports_data.txt
│   └── sample_quiz.json
│
├── docs/
│
├── src/
│   ├── embeddings.py
│   ├── prompt_template.py
│   ├── quiz_generator.py
│   ├── rag_pipeline.py
│   ├── vector_store.py
│   └── web_search.py
│
└── tests/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Chandu7483/AI-Sports-Quiz-Master.git
```

Move into the project directory:

```bash
cd AI-Sports-Quiz-Master
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open the Gradio URL displayed in the terminal.

---

## 🧠 How It Works

```
User
   │
   ▼
Select Sport & Difficulty
   │
   ▼
Retrieve Context
   │
   ├── ChromaDB
   └── DuckDuckGo
   │
   ▼
Gemini AI
   │
   ▼
Generate Quiz (JSON)
   │
   ▼
Interactive Gradio Quiz
```

---

## 🎮 Supported Sports

- 🏏 Cricket
- ⚽ Football
- 🏀 Basketball
- 🎾 Tennis
- 🏸 Badminton
- 🤼 Kabaddi
- 🏑 Hockey
- 🏐 Volleyball

---

## 📌 Future Enhancements

- User authentication
- Quiz history
- Leaderboard
- Timer for each question
- Voice-enabled quizzes
- More sports
- Database-backed score tracking

---

## 👨‍💻 Author

**Chandu M**

Python Developer | AI Enthusiast | Data Science Graduate

GitHub: https://github.com/Chandu7483

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.