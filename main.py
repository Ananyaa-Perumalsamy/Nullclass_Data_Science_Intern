import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
os.environ["GOOGLE_API_KEY"] = "XXX"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

# Function to analyze sentiment using Gemini
def analyze_sentiment_and_respond(user_input):
    prompt = f"""
    Analyze the sentiment of the following user message and respond accordingly:
    Message: "{user_input}"
    
    #If the sentiment is positive, reply in an encouraging and supportive tone.
    #If the sentiment is negative, reply with empathy and an offer to assist.
    #If the sentiment is neutral, provide a helpful and neutral response.
    #Your response should be friendly, concise, and appropriate for a chatbot conversation.
    
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Sentiment Chatbot", layout="wide")

# Initialize session states
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}  # Stores multiple chat histories
if "current_chat" not in st.session_state:
    st.session_state.current_chat = None  # No chat selected by default
if "new_message" not in st.session_state:
    st.session_state.new_message = False  # Track if a new message was entered

# Sidebar for chat history
st.sidebar.title("📜 Chat History")
chat_names = list(st.session_state.chat_sessions.keys())

# Select chat session
selected_chat = st.sidebar.radio("Select a chat:", ["New Chat"] + chat_names, key="chat_selector")

# If a chat is selected, load it
if selected_chat != "New Chat":
    st.session_state.current_chat = selected_chat
    if selected_chat not in st.session_state.chat_sessions:
        st.session_state.chat_sessions[selected_chat] = []
else:
    st.session_state.current_chat = None

# Display chat header
st.title("🤖 Sentiment-Aware Chatbot")

# Chat history container
chat_history = st.session_state.chat_sessions.get(st.session_state.current_chat, [])

st.subheader(f"🗨 {selected_chat}")
for sender, msg in chat_history:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.write(msg)

# User input
user_input = st.text_input("You:", "", key="user_input")

# Process input only when a new message is entered
if user_input and not st.session_state.new_message:
    st.session_state.new_message = True  # Prevent multiple processing
    response = analyze_sentiment_and_respond(user_input)

    # Save conversation
    chat_history.append(("You", user_input))
    chat_history.append(("Bot", response))

    # Store updated session
    if selected_chat == "New Chat":
        chat_name = f"Chat {len(st.session_state.chat_sessions) + 1}"
        st.session_state.chat_sessions[chat_name] = chat_history
        st.session_state.current_chat = chat_name  # Switch to new chat
    else:
        st.session_state.chat_sessions[selected_chat] = chat_history

    # Refresh UI to update chat
    st.rerun()

# Reset new message flag after processing
st.session_state.new_message = False
