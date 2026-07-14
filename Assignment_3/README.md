# 🎯 AI Decision Studio – Stateful AI Decision Assistant

AI Decision Studio is a stateful AI chatbot built using Streamlit and Google's Gemini AI. The application helps users analyze decisions from different thinking perspectives while maintaining a continuous conversation history.

Unlike a stateless chatbot that forgets previous messages whenever the Streamlit application reruns, AI Decision Studio uses Streamlit's `st.session_state` as a **Memory Vault** to store and preserve the complete conversation during the active session.

The application is developed as part of the **MirAI School of Technology – Virtual Summer Internship 2026: AI Builder Track**.

---

## 📌 Project Overview

Streamlit reruns the complete Python script whenever a user interacts with an application, such as entering a message or changing a sidebar option.

Without session state, previous messages can be lost during these reruns.

AI Decision Studio solves this problem by storing user and assistant messages inside:

```python
st.session_state.messages
```

Each message is stored as a Python dictionary containing the role and message content.

Example:

```python
{
    "role": "user",
    "content": "Should I learn Machine Learning?"
}
```

The stored messages are rendered again whenever the application reruns. This creates a continuous and stateful chatbot experience.

---

## ✨ Features

* 🎯 AI-powered decision assistance
* 🧠 Multiple AI thinking modes
* 💬 Native Streamlit chat interface
* 🧠 Stateful conversation memory
* 📚 Continuous conversation history
* ⚡ Real-time Gemini response streaming
* 📏 Adjustable AI response length
* 🔄 Chat history preserved during Streamlit reruns
* ⚙️ Sidebar settings without losing previous messages
* 🗑️ Clear conversation functionality
* 📥 Download the latest AI response

---

## 🧠 AI Thinking Modes

The application allows users to analyze a situation from different perspectives.

### 🧠 Logical Analyst

Analyzes the user's situation using logical reasoning, advantages, disadvantages, and practical conclusions.

### 💰 Financial Advisor

Analyzes decisions from a financial perspective by considering costs, savings, financial risks, benefits, and long-term value.

### ❤️ Emotional Coach

Provides supportive and empathetic guidance while considering emotions, confidence, and personal well-being.

### 🚀 Future Visionary

Analyzes the long-term impact of a decision and considers future opportunities, trends, and possible risks.

### ⚖️ Devil's Advocate

Challenges assumptions, identifies hidden risks, questions weak reasoning, and presents alternative viewpoints.

---

## 🧠 Memory Vault – Stateful Chat

The main feature of this assignment is the implementation of a **Memory Vault** using Streamlit Session State.

The Memory Vault stores the complete conversation between the user and the AI.

### 1. Initialize the Memory Vault

When the application starts, it checks whether a `messages` variable already exists in Streamlit Session State.

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

If the variable does not exist, an empty Python list is created.

---

### 2. Render Previous Messages

Every stored message is displayed using Streamlit's native `st.chat_message()` component.

```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

Whenever Streamlit reruns the application, the loop redraws the complete conversation history.

---

### 3. Native Chat Input

The application uses Streamlit's `st.chat_input()` component instead of a traditional text input and SEND button.

```python
if user_message := st.chat_input(
    "Describe your decision or situation..."
):
```

The walrus operator `:=` assigns the entered message to `user_message` and checks whether the user entered a message in a single statement.

---

### 4. Save User Messages

Every new user message is stored in the Memory Vault.

```python
st.session_state.messages.append(
    {
        "role": "user",
        "content": user_message
    }
)
```

---

### 5. Save AI Responses

After Gemini generates a response, the assistant's response is also stored in the same Memory Vault.

```python
st.session_state.messages.append(
    {
        "role": "assistant",
        "content": full_response
    }
)
```

This allows the chatbot to maintain a continuous conversation.

---

## 🔄 Application Workflow

The application follows the workflow below:

```text
Start Application
        ↓
Load Gemini API Key
        ↓
Initialize Session State Memory
        ↓
Display Previous Chat Messages
        ↓
User Enters a New Message
        ↓
Save User Message to Memory
        ↓
Prepare Conversation History
        ↓
Send Prompt to Gemini AI
        ↓
Generate and Stream AI Response
        ↓
Save AI Response to Memory
        ↓
Streamlit Reruns
        ↓
Display Complete Conversation History
```

---

## 💬 Example Continuous Conversation

The Memory Vault allows users to have connected conversations.

### Message 1

```text
I am an AI and Machine Learning student. Which skill should I focus on the most?
```

### Message 2

```text
Why is that skill important for my career?
```

### Message 3

```text
Based on what we discussed, give me a simple 3-month learning plan for that skill.
```

The second and third messages depend on the previous conversation.

The chatbot maintains context because the complete conversation history is stored in `st.session_state.messages` and included when generating the Gemini prompt.

---

## ⚙️ Technologies Used

* Python
* Streamlit
* Google Generative AI
* Gemini 2.5 Flash
* python-dotenv

---

## 📂 Project Structure

```text
AI-Decision-Studio/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## 🚀 Installation and Setup

### Step 1: Clone the Repository

Clone the project repository.

```bash
git clone <repository-url>
```

Navigate to the project directory.

```bash
cd AI-Decision-Studio
```

---

### Step 2: Create a Virtual Environment

Creating a virtual environment is optional but recommended.

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Step 3: Install Dependencies

Install all required Python libraries.

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure the Gemini API Key

Create a `.env` file in the main project directory.

Add your Google Gemini API key:

```text
API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual API key.

The `.env` file should not be uploaded to a public GitHub repository.

---

### Step 5: Run the Streamlit Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in the browser.

The default Streamlit address is:

```text
http://localhost:8501
```

---

## 📦 Requirements

The application requires the following Python libraries:

```text
streamlit
google-generativeai
python-dotenv
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🗑️ Clear Conversation

The **Clear Conversation** button removes all stored messages from the current session.

The Memory Vault is reset using:

```python
st.session_state.messages = []
```

After clearing the conversation, the application reruns and starts a new chat.

---

## 📥 Download AI Response

The latest Gemini AI response can be downloaded as a text file using the sidebar download option.

This allows users to save important decision guidance generated by the AI.

---

## 🎯 Assignment Requirements Covered

* Session State Memory Vault implemented
* `st.session_state.messages` initialized as an empty list
* Previous chat messages rendered using a loop
* `st.chat_message()` used for user and assistant messages
* `st.chat_input()` used instead of a text input and SEND button
* Walrus operator `:=` used with the chat input
* User messages stored in Session State
* Gemini responses stored in Session State
* Continuous multi-message conversations supported
* Chat history remains visible when sidebar settings change

---

## 📄 License

This project is created for educational and internship assignment purposes.

The application demonstrates stateful chatbot development using Streamlit Session State and Google's Gemini AI.
