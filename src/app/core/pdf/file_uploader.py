import streamlit as st
from attrs import define

from src.app.states.gui import GUIState


@define
class FileUploader:
    state: GUIState

    def __attrs_post_init__(self):
        uploader_state = self.state.left_col.uploader
        chat_state = self.state.left_col.chat

        uploaded_file = st.file_uploader(
            label=uploader_state.name,
            type=uploader_state.type,
            key=uploader_state.key,
            label_visibility=uploader_state.label_visibility,
        )
        if uploaded_file is None:
            st.warning(uploader_state.disabled_message)
            chat_state.disabled = True
            chat_state.clear_chat()
        else:
            uploader_state.file = uploaded_file.read()
            uploader_state.is_file_uploaded = True
            chat_state.disabled = False
            self.state.rerun()
