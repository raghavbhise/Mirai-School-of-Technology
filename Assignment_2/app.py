import os
import dotenv
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / ".env")

# -----------------------------
# Load Environment Variables
# -----------------------------
dotenv.load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("API_KEY not found in .env file")
    st.stop()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Decision Studio",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Decision Studio")
st.caption("View your problem from different perspectives.")

# -----------------------------
# Decision Modes
# -----------------------------

MODES = {
    "🧠 Logical Analyst":
    """
    Think only using logic.
    Give pros, cons and a rational conclusion.
    """,

    "💰 Financial Advisor":
    """
    Analyze from financial point of view.
    Mention costs, savings and long-term impact.
    """,

    "❤️ Emotional Coach":
    """
    Respond with empathy.
    Help reduce stress and build confidence.
    """,

    "🚀 Future Visionary":
    """
    Think 5 years ahead.
    Predict future opportunities and risks.
    """,

    "⚖️ Devil's Advocate":
    """
    Challenge every assumption.
    Point out hidden problems and risks.
    """
}

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Settings")

selected_mode = st.sidebar.selectbox(
    "Choose Thinking Mode",
    list(MODES.keys())
)

response_size = st.sidebar.radio(
    "Response Length",
    ["Short", "Medium", "Detailed"],
    index=1
)

if st.sidebar.button("🗑 Clear Conversation"):
    st.session_state.chat = []
    st.rerun()

# -----------------------------
# Chat Memory
# -----------------------------

if "chat" not in st.session_state:
    st.session_state.chat = []

for message in st.session_state.chat:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------

question = st.chat_input("Describe your situation...")

if question:

    st.session_state.chat.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    history = ""

    for msg in st.session_state.chat:
        history += f"{msg['role'].capitalize()}: {msg['content']}\n"

    prompt = f"""
You are an AI Decision Assistant.

Thinking Style:
{MODES[selected_mode]}

Response Length:
{response_size}

Conversation:
{history}

Now answer the user's latest question.
"""

    with st.chat_message("assistant"):

        placeholder = st.empty()
        answer = ""

        try:

            response = model.generate_content(
                prompt,
                stream=True
            )

            for chunk in response:

                if chunk.text:
                    answer += chunk.text
                    placeholder.markdown(answer + "▌")

            placeholder.markdown(answer)

            st.session_state.chat.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            st.error(e)

# -----------------------------
# Download
# -----------------------------

if st.session_state.get("chat"):

    last_answer = ""

    for msg in reversed(st.session_state.chat):
        if msg["role"] == "assistant":
            last_answer = msg["content"]
            break

    st.download_button(
        "📥 Download Last Answer",
        last_answer,
        file_name="decision.txt"
    )