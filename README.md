---
title: AI Sports Quiz Master
emoji: 🏆
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.38.2
app_file: app.py
pinned: false
---

# 🏆 AI Sports Quiz Master

An intelligent Sports Quiz Generation Agent built using **Google Gemini**, **RAG (Retrieval-Augmented Generation)**, **ChromaDB**, **Sentence Transformers**, and **Gradio**.

The application generates fresh, sport-specific quizzes with detailed explanations by combining a local knowledge base and live web search.

---

## 🚀 Features

- 🏏 Supports multiple sports (Cricket, Football, Basketball, Tennis, Kabaddi, Badminton, etc.)
- 🎯 Difficulty Levels (Easy, Medium, Hard)
- 🤖 AI-generated questions using Google Gemini
- 📚 Retrieval-Augmented Generation (RAG)
- 🗂️ ChromaDB Vector Database
- 🌐 Live web search for recent sports information
- 🧠 Semantic search using Sentence Transformers
- 💡 Detailed explanations for every answer
- 🎨 Interactive Gradio interface

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- Stramlit
- ChromaDB
- Sentence Transformers
- DuckDuckGo Search
- RAG Architecture

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
├── docs/
├── src/
└── tests/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Chandu7483/AI-Sports-Quiz-Master.git
cd AI-Sports-Quiz-Master
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the Application

```bash
python app.py
```

---

## 📌 Supported Sports

- Cricket
- Football
- Basketball
- Tennis
- Kabaddi
- Badminton
- General Sports

---

## 📷 Demo

Launch the Gradio application locally or via Hugging Face Spaces.

---

## 🎯 Future Enhancements

- More Sports Coverage
- Leaderboard
- User Authentication
- Timed Quiz Mode
- Score Analytics
- Sports APIs Integration

---

## 👨‍💻 Author

**Chandu M**

- GitHub: https://github.com/Chandu7483

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.