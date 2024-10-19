import streamlit as st
import os
import fitz

from streamlit_pdf_viewer import pdf_viewer
from .initialize import initialize_variables


class Gui:
    def __init__(self, path_file: str, path_modified_file: str, message_container_height: int) -> None:

        initialize_variables()

        self.messages = st.session_state.messages
        self.uploaded_file = st.session_state.uploaded_file
        self.path_file = path_file
        self.path_modified_file = path_modified_file
        self.message_container_height = message_container_height
        self.is_pdf_visible = False
        self.is_file_uploaded = False

    def prompt_and_prediction(self) -> None:
        messages_container = st.container(height=self.message_container_height)
        input_placeholder = st.empty()

        if prompt := input_placeholder.chat_input("Enter your message:"):
            self.messages.append({"role": "user", "content": prompt})
            self.messages.append({"role": "assistant", "content": f"{prompt}"})

        with messages_container:
            for message in self.messages:
                if message["role"] == "user":
                    st.chat_message("user").write(message["content"])
                elif message["role"] == "assistant":
                    st.chat_message("assistant").write(message["content"])

    def save_file(self) -> None:
        with open(os.path.join(self.path_file), "wb") as f:
            f.write(self.uploaded_file.getbuffer())
        self.is_file_uploaded = True

    def upload_file(self) -> None:
        self.uploaded_file = st.file_uploader("Upload PDF file", type="pdf")

        if self.uploaded_file is not None and self.is_file_uploaded is False:
            self.save_file()

        elif self.uploaded_file is None:
            self.is_pdf_visible = False
            self.is_file_uploaded = False
            self.messages = []
            st.warning("No file was uploaded")

    def mark_context(self) -> None:
        doc = fitz.open(self.path_file)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            search_text = 'MASTER DATA TRAINEE'
            text_instances = page.search_for(search_text)

            for inst in text_instances:
                highlight = page.add_rect_annot(inst)
                highlight.set_colors(stroke=(1, 0, 0))
                highlight.update()

        doc.save(self.path_modified_file)
        doc.close()

    def show_file(self) -> None:
        if st.button("Show PDF") and self.uploaded_file is not None:
            self.is_pdf_visible = True
            self.mark_context()

        if self.is_pdf_visible:
            pdf_viewer(self.path_modified_file)
