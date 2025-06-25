import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

st.set_page_config(page_title="🦙 Nikkieesss gpt", layout="centered")
st.title("💬 Nikkieess gpt(how can i help you)")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

prompt = st.chat_input("Type your message...")

# Display previous chat history
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# On new user message
if prompt:
    # Show user's message
    st.session_state.chat_history.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Make POST request to Ollama
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(OLLAMA_URL, json={
                    "model": MODEL,
                    "prompt": prompt,
                    "stream": False
                })
                full_reply = response.json()["response"]
            except Exception as e:
                full_reply = f"❌ Error: {e}"

        st.markdown(full_reply)
        st.session_state.chat_history.append(("assistant", full_reply))
