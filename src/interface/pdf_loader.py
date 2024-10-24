import os

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


class Pdf_loader():
    def __init__(self, path_file):
        self.uploaded_file = st.file_uploader("Upload PDF file", type="pdf", key="uploader")
        self.path_file = path_file
        self.save_file()

    def save_file(self):
        if self.uploaded_file is not None:
            with open(os.path.join(self.path_file), "wb") as f:
                f.write(self.uploaded_file.getbuffer())
                self.uploaded_file = None
            st.session_state['show_pdf'] = True



class Chat():
    def __init__(self, messages, message_container_height):
        self.messages = messages
        self.message_container_height = message_container_height

    def show_chat(self):
        messages_container = st.container(height=self.message_container_height)
        input_placeholder = st.empty()

        if prompt := input_placeholder.chat_input("Enter your message:", disabled=st.session_state['disabled_chat']):
            self.messages.append({"role": "user", "content": prompt})
            self.messages.append({"role": "assistant", "content": f"{prompt}"})

        with messages_container:
            for message in self.messages:
                if message["role"] == "user":
                    st.chat_message("user").write(message["content"])
                elif message["role"] == "assistant":
                    st.chat_message("assistant").write(message["content"])

    def chat_handling(self):
        if st.session_state['show_pdf']:
            if st.button("delete_pdf"):
                st.session_state.clear()
                st.rerun()
                # st.session_state['show_pdf'] = False


class PDF_viewer():
    def __init__(self, path_file):
        self.path_file = path_file
        self.show_pdf()

    def show_pdf(self):
        if st.session_state['show_pdf']:
            pdf_viewer(self.path_file)
            st.session_state['disabled_chat'] = False
        else:
            st.session_state['disabled_chat'] = True
