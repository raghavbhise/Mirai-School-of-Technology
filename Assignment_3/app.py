import os
import dotenv
import streamlit as st
import google.generativeai as genai


# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

dotenv.load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("API_KEY not found in the .env file.")
    st.stop()


# --------------------------------------------------
# Configure Gemini API
# --------------------------------------------------

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# --------------------------------------------------
# Task 1: Initialize the Memory Vault
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Configure Streamlit Page
# --------------------------------------------------

st.set_page_config(
    page_title="AI Decision Studio",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Decision Studio")

st.caption(
    "Explore your decisions from different AI thinking perspectives."
)


# --------------------------------------------------
# Define AI Thinking Modes
# --------------------------------------------------

MODES = {
    "🧠 Logical Analyst": (
        "You are a logical decision analyst. "
        "Analyze the user's situation using facts, reasoning, "
        "advantages, disadvantages, and practical conclusions."
    ),

    "💰 Financial Advisor": (
        "You are a financial decision advisor. "
        "Analyze the situation from a financial perspective. "
        "Consider costs, savings, risks, benefits, and long-term value."
    ),

    "❤️ Emotional Coach": (
        "You are a supportive emotional coach. "
        "Understand the user's emotions and provide encouraging, "
        "empathetic, and confidence-building guidance."
    ),

    "🚀 Future Visionary": (
        "You are a future-focused visionary. "
        "Analyze how the user's decision may affect them in the next "
        "five years. Discuss future opportunities, trends, and risks."
    ),

    "⚖️ Devil's Advocate": (
        "You are a devil's advocate. "
        "Challenge the user's assumptions, identify hidden risks, "
        "question weak reasoning, and present alternative viewpoints."
    )
}


# --------------------------------------------------
# Sidebar Settings
# --------------------------------------------------

st.sidebar.header("⚙️ Decision Settings")

selected_mode = st.sidebar.selectbox(
    "Choose Thinking Mode",
    options=list(MODES.keys())
)

response_length = st.sidebar.radio(
    "Response Length",
    options=["Short", "Medium", "Detailed"],
    index=1
)

st.sidebar.info(
    "Changing the thinking mode will not remove your conversation history."
)


# --------------------------------------------------
# Clear Chat Option
# --------------------------------------------------

if st.sidebar.button("🗑️ Clear Conversation"):
    st.session_state.messages = []
    st.rerun()


# --------------------------------------------------
# Task 2: Render the Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# Task 3: Upgrade the Input UI
# --------------------------------------------------

if user_message := st.chat_input(
    "Describe your decision or situation..."
):


    # --------------------------------------------------
    # Task 4: Save User Message to Memory
    # --------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )


    # Display Current User Message
    with st.chat_message("user"):
        st.markdown(user_message)


    # --------------------------------------------------
    # Prepare Conversation History for Gemini
    # --------------------------------------------------

    conversation_history = ""

    for message in st.session_state.messages:

        role = message["role"].capitalize()
        content = message["content"]

        conversation_history += (
            f"{role}: {content}\n"
        )


    # --------------------------------------------------
    # Create Gemini Prompt
    # --------------------------------------------------

    full_prompt = f"""
You are part of an AI Decision Studio.

Your current thinking mode is:

{selected_mode}

Thinking instructions:

{MODES[selected_mode]}

The user selected the following response length:

{response_length}

Conversation history:

{conversation_history}

Respond to the user's latest message.

Maintain awareness of the previous conversation.

Do not repeat previous answers unnecessarily.

Follow the selected thinking mode while answering.
"""


    # --------------------------------------------------
    # Generate Gemini Response
    # --------------------------------------------------

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        full_response = ""

        try:

            response = model.generate_content(
                full_prompt,
                stream=True
            )

            for chunk in response:

                try:
                    chunk_text = chunk.text
                except ValueError:
                    chunk_text = ""

                if chunk_text:

                    full_response += chunk_text

                    response_placeholder.markdown(
                        full_response + "▌"
                    )

            if full_response:

                response_placeholder.markdown(full_response)

                # ------------------------------------------
                # Save AI Response to Memory
                # ------------------------------------------

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": full_response
                    }
                )

            else:

                error_message = (
                    "I could not generate a text response. "
                    "Please try asking your question again."
                )

                response_placeholder.warning(error_message)

        except Exception as error:

            st.error(
                f"Gemini API Error: {error}"
            )


# --------------------------------------------------
# Download Latest AI Response
# --------------------------------------------------

if st.session_state.messages:

    latest_response = ""

    for message in reversed(
        st.session_state.messages
    ):

        if message["role"] == "assistant":

            latest_response = message["content"]

            break


    if latest_response:

        st.sidebar.download_button(
            label="📥 Download Latest Response",
            data=latest_response,
            file_name="ai_decision.txt",
            mime="text/plain"
        )