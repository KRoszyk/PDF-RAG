import streamlit as st
from attrs import define

from src.core.chat import Chat
from src.core.pdf.file_uploader import FileUploader
from src.states.gui import GUIState


@define
class LeftColumn:
    state: GUIState

    def __attrs_post_init__(self):
        state = self.state
        chat_state = self.state.left_col.chat
        uploader_state = self.state.left_col.uploader
        rerun_state = self.state.rerun
        delete_button_state = self.state.left_col.delete_button
        clear_button_state = self.state.left_col.clear_button
        # this _ is for empty space
        _, left_button_column, _, right_button_column, _ = st.columns(self.state.layout_left_panel)

        if uploader_state.is_file_uploaded is False:
            # Show file uploader
            FileUploader(state=state)
        else:
            with left_button_column:
                if st.button(delete_button_state.name, use_container_width=True):
                    uploader_state.update_key()
                    uploader_state.is_file_uploaded = False
                    rerun_state()
                # Button to clear chat.
            with right_button_column:
                if st.button(clear_button_state.name, use_container_width=True):
                    chat_state.clear_chat()

        # Initialize a chat inside a container to apply styling to it.
        with st.container(key=chat_state.key):
            Chat(state=state)
