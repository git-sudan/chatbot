import streamlit as st
import random
import time

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! Currently we are working on integrating OpenAI models, stay tuned!",
            "Hi, Our Villupuram Engineering team is working on giving best to you. stay tuned!",
            "Work in progress, please wait"
           
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("D-Brain AI (Chatbot for Villupuram)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up? Villupuram"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
