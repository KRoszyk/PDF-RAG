import streamlit as st
import os


def handle_file_upload(path):
    uploaded_file = st.file_uploader("Drop your PDF file here", type="pdf")

    if uploaded_file is not None:
        st.session_state['uploaded_file'] = uploaded_file
        save_path = os.path.join(path)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return 1
    else:
        st.warning("No file is uploaded.")
        return 0


def generate_text():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    messages = st.container()

    if prompt := st.chat_input("Say something"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": f"{prompt}"})

    for message in st.session_state.messages:
        if message["role"] == "user":
            messages.chat_message("user").write(message["content"])
        elif message["role"] == "assistant":
            messages.chat_message("assistant").write(message["content"])


def create_gui(path):
    if handle_file_upload(path) == 1:
        generate_text()
