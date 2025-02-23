import streamlit as st
from attrs import define

from src.app.core.chat import Chat
from src.app.core.pdf.file_uploader import FileUploader
from src.app.states.gui import GUIState


@define
class LeftColumn:
    state: GUIState

    def __attrs_post_init__(self):
        state = self.state
        left_col_state = state.left_col
        chat_state = left_col_state.chat
        uploader_state = left_col_state.uploader
        delete_button_state = left_col_state.delete_button
        clear_button_state = left_col_state.clear_button
        _, delete_pdf_button, _, clear_chat_button, _ = st.columns(left_col_state.buttons_panel_layout)

        if uploader_state.is_file_uploaded is False:
            FileUploader(state=state)

        else:
            with delete_pdf_button:
                if st.button(delete_button_state.name, use_container_width=True):
                    uploader_state.update_key()
                    uploader_state.is_file_uploaded = False
                    state.left_col.rag_created = False
                    state.right_col.scroll_counter.scroll_count = 0
                    state.right_col.scroll_counter.actual_scroll_position = 0
                    state.right_col.pdf_viewer.annotations = []
                    state.right_col.pdf_viewer.phrases_to_highlight = []
                    state.rerun()

            with clear_chat_button:
                if st.button(clear_button_state.name, use_container_width=True):
                    chat_state.clear_chat()

        # Initialize a chat inside a container to apply styling to it.
        with st.container(key=chat_state.key):
            Chat(state=state)
