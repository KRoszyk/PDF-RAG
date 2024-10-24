import streamlit as st
from .css import load_css
from .pdf_loader import Pdf_loader
from .pdf_loader import Chat
from .pdf_loader import PDF_viewer


class Gui:
    def __init__(self, path_file: str, path_modified_file: str, message_container_height: int,
                 layout_division: int) -> None:
        self.path_file = path_file
        # self.path_modified_file = path_modified_file
        self.message_container_height = message_container_height
        self.layout_division = layout_division
        self.initialization()

    def initialization(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "show_pdf" not in st.session_state:
            st.session_state.show_pdf = False

        if "disabled_chat" not in st.session_state:
            st.session_state.disabled_chat = True

    def show_gui(self) -> None:
        load_css()
        col1, col2 = st.columns(self.layout_division)

        with col1:
            st.markdown('<h1 class="custom-title">Load file</h1>', unsafe_allow_html=True)
            chat = Chat(st.session_state.messages, self.message_container_height)
            chat.chat_handling()
            if st.session_state['show_pdf'] == False:
                pdf_loader = Pdf_loader(self.path_file)
            chat.show_chat()
        with col2:
            placeholder = st.container(key="plh2")
            with placeholder:
                pdf_viewer = PDF_viewer(self.path_file)
                st.markdown('<h1 class="custom-title"></h1>', unsafe_allow_html=True)
