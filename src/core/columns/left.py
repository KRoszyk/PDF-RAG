from attrs import define
import streamlit as st

from src.core.chat import Chat
from src.core.pdf.file_uploader import FileUploader
from src.states.gui import GUIState


@define
class LeftColumn:
    state: GUIState

    def __attrs_post_init__(self):
        chat_state = self.state.left_col.chat
        uploader_state = self.state.left_col.uploader
        rerun_state = self.state.rerun
        delete_button_state = self.state.left_col.delete_button
        clear_button_state = self.state.left_col.clear_button

        if uploader_state.is_file_uploaded is False:
            # Show file uploader
            FileUploader(state=self.state)
        else:
            # Button to delete the uploaded file.
            if st.button(delete_button_state.name):
                uploader_state.update_key()
                uploader_state.is_file_uploaded = False
                rerun_state()
            # Button to clear chat.
            if st.button(clear_button_state.name):
                chat_state.clear_chat()
                rerun_state()

        # Initialize a chat inside a container to apply styling to it.
        with st.container(key=chat_state.key):
            Chat(state=self.state)
