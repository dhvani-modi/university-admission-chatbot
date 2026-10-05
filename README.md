# University Admission AI Chatbot

An AI-powered University Admission Assistant that answers admission-related questions using a university admission policy document as its knowledge base.

## 📌 Project Overview

The University Admission AI Chatbot is designed to help students get quick answers to university admission-related queries.

The chatbot uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the university admission policy and generate answers using an AI language model.

## ✨ Features

- AI-powered admission assistant
- Answers questions from the university admission policy
- Retrieval-Augmented Generation (RAG)
- FastAPI backend
- Interactive web-based chatbot interface
- Conversation history
- Pinecone vector database for document retrieval
- Groq LLM for AI responses
- Responsive frontend design

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Backend
- Python
- FastAPI
- LangChain

### AI & Database
- Groq
- Pinecone
- Google Gemini Embeddings

## 🏗️ Project Structure

```text
AI_Project
│
├── Backend-20260614T111806Z-3-001
│   └── Backend
│       ├── agent.py
│       ├── app.py
│       └── models.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── ADMISSION-POLICY-21102013.pdf
├── requirements.txt
├── .gitignore
└── README.md
🔄 How It Works
User
  ↓
Chatbot Frontend
  ↓
FastAPI Backend
  ↓
LangChain Agent
  ↓
Pinecone Knowledge Base
  ↓
University Admission Policy
  ↓
Groq AI Model
  ↓
Answer
🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/dhvani-modi/university-admission-chatbot.git
2. Open the Project
cd university-admission-chatbot
3. Create Virtual Environment
py -3.13 -m venv chatbot-env
4. Activate Virtual Environment

On Windows PowerShell:

.\chatbot-env\Scripts\Activate.ps1
5. Install Dependencies
pip install -r requirements.txt
6. Configure Environment Variables

Create a .env file and add the required API keys for:

Groq
Pinecone
Google Gemini

Do not upload the .env file to GitHub.

7. Start the Backend
cd Backend-20260614T111806Z-3-001\Backend
uvicorn app:app --reload

The backend will run at:

http://127.0.0.1:8000
8. Run the Frontend

Open:

frontend/index.html

using VS Code Live Server.

💬 Example Questions

The chatbot can answer questions such as:

What are the admission requirements?
What documents are required for admission?
What is the eligibility criteria for BBA?
Is UGAT required for admission?
What is the minimum percentage required?
How many days are given to pay the fees after seat allotment?
🎯 Purpose

The purpose of this project is to demonstrate the practical use of:

Artificial Intelligence
Natural Language Processing
Retrieval-Augmented Generation
Vector databases
REST APIs
Web development

in building a useful university admission assistant.

👩‍💻 Developer

Dhvani Modi

B.Tech Computer Science Engineering Student

GitHub: https://github.com/dhvani-modi

📄 Disclaimer

This project is developed for educational and demonstration purposes. Admission information is based on the provided university admission policy document.


