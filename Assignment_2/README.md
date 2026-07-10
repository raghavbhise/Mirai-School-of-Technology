# 🎯 AI Decision Studio

AI Decision Studio is a Streamlit-based web application powered by Google's Gemini 2.5 Flash model. Instead of acting as a normal chatbot, it helps users make better decisions by analyzing the same problem from different perspectives.

Whether you're deciding on a career, education, business, or personal matter, the application provides thoughtful responses using specialized AI thinking modes.

---

## ✨ Features

- 🎯 Multiple Decision Modes
  - Logical Analyst
  - Financial Advisor
  - Emotional Coach
  - Future Visionary
  - Devil's Advocate

- 💬 Interactive chat interface using Streamlit Chat.

- ⚡ Real-time streaming responses from Gemini AI.

- 📚 Conversation history maintained throughout the session.

- 📏 Adjustable response length
  - Short
  - Medium
  - Detailed

- 📥 Download the latest AI response as a text file.

- 🗑 Clear conversation with a single click.

- 🎨 Clean and user-friendly interface.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Google Generative AI (Gemini 2.5 Flash)
- python-dotenv

---

## 📂 Project Structure

```
AI-Decision-Studio/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder.

```bash
cd AI-Decision-Studio
```

---

### 2. Create a Virtual Environment (Optional)

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Key

Create a file named `.env` in the project directory.

Example:

```text
API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your Google Gemini API key.

---

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

If it does not open automatically, visit:

```
http://localhost:8501
```

---

## 📖 How to Use

1. Launch the application.
2. Select a thinking mode from the sidebar.
3. Choose the preferred response length.
4. Type your question or decision in the chat box.
5. The AI will generate a response based on the selected perspective.
6. Continue the conversation or clear it anytime.
7. Download the latest response if required.

---

## 🧠 Decision Modes

### 🧠 Logical Analyst

Analyzes the situation logically by listing advantages, disadvantages, and practical conclusions.

---

### 💰 Financial Advisor

Evaluates the financial impact including costs, savings, investment, and long-term value.

---

### ❤️ Emotional Coach

Provides supportive guidance while considering emotions, confidence, and personal well-being.

---

### 🚀 Future Visionary

Predicts future opportunities, trends, and possible outcomes over the coming years.

---

### ⚖️ Devil's Advocate

Challenges assumptions, identifies hidden risks, and presents alternative viewpoints.

---

## 💡 Example Questions

- Should I pursue higher education?
- Should I switch my career to AI?
- Is freelancing better than a full-time job?
- Should I buy a laptop now or wait?
- Which programming language should I learn first?

---

## 🔒 Environment Variable

The application requires the following environment variable.

| Variable | Description |
|----------|-------------|
| API_KEY | Google Gemini API Key |

---

## 📌 Requirements

- Python 3.10 or above
- Internet connection
- Valid Google Gemini API Key

---

## 📄 License

This project is created for educational and learning purposes.
