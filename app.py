import streamlit as st

st.set_page_config(page_title="Chatbot Agent", page_icon="🤖")

# Title
st.title("🤖 Chatbot Agent")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Save user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Simple rule-based response
    response = "I didn’t understand that."
    if "hello" in prompt.lower():
        response = "Hello! How can I help you today?"
    elif "how are you" in prompt.lower():
        response = "I’m just a bot, but I’m doing great! 🚀"

    # Save bot reply
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)

