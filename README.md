# 🎓 College Assistant AI

An intelligent AI-powered chatbot built using **Flask**, **Python**, and the **Qwen2.5-1.5B-Instruct** language model. The chatbot provides assistance with programming, computer science subjects, interview preparation, resumes, and general academic queries through a modern web interface.

---

## 📖 Overview

College Assistant AI is a local AI chatbot designed to help students with their daily academic needs. Unlike cloud-based chatbots that require API keys, this application runs a locally downloaded Large Language Model (LLM), allowing users to interact with the chatbot without relying on external AI APIs after the model is downloaded.

---

## ✨ Features

- 🤖 AI-powered conversational chatbot
- 💻 Programming assistance (Python, Java, C, C++)
- 🗄️ Database Management System (DBMS)
- ⚙️ Operating Systems
- 🧠 Artificial Intelligence
- 📊 Machine Learning & Deep Learning
- 📄 Resume Building Tips
- 🎯 Interview Preparation
- 💬 Multi-turn conversation memory (current session)
- 🌐 Modern Flask-based web interface
- 📱 Responsive design
- 🌙 Dark-themed UI

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- Transformers
- PyTorch

### Frontend
- HTML5
- CSS3
- JavaScript

### AI Model
- Qwen2.5-1.5B-Instruct

---

## 📂 Project Structure

```
CollegeAssistantAI/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CollegeAssistantAI.git
cd CollegeAssistantAI
```

### Create a virtual environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

```
User
   │
   ▼
Web Interface (HTML/CSS/JS)
   │
   ▼
Flask Backend
   │
   ▼
Qwen2.5-1.5B-Instruct
   │
   ▼
Generated Response
```

---

## 💬 Example

**User**

```
Explain Normalization in DBMS.
```

**Assistant**

```
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity...
```

---

## 📸 Screenshots

### Home Screen

> Add a screenshot here.

```
screenshots/home.png
```

### Chat Interface

> Add a screenshot here.

```
screenshots/chat.png
```

---

## 🚀 Future Improvements

- ✅ Chat history
- ✅ Multiple chat sessions
- ✅ Markdown rendering
- ✅ Syntax highlighting
- ✅ Streaming AI responses
- ✅ PDF upload
- ✅ RAG (Retrieval-Augmented Generation)
- ✅ Voice input
- ✅ Voice output
- ✅ User authentication
- ✅ Conversation export

---

## 📋 Requirements

- Python 3.10+
- Flask
- PyTorch
- Transformers
- Accelerate
- Internet connection (only for the first model download)

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**ERAMALINGAM S**

GitHub: https://github.com/ERAMALINGAM-2007

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

---

## 🙏 Acknowledgements

- Hugging Face Transformers
- PyTorch
- Flask
- Qwen Team
