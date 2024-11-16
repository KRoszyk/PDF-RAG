from attrs import define
import streamlit as st

from src.states.gui import GUIState
from src.core.pdf.pdf_viewer import PdfViewer


@define
class RightColumn:
    state: GUIState

    def __attrs_post_init__(self):
        uploader_state = self.state.left_col.uploader
        next_button_state = self.state.right_col.next_button
        previous_button_state = self.state.right_col.previous_button
        count_button_state = self.state.right_col.count_button

        st.button(count_button_state.name, disabled=not uploader_state.is_file_uploaded)
        st.button(previous_button_state.name, disabled=not uploader_state.is_file_uploaded)
        st.button(next_button_state.name, disabled=not uploader_state.is_file_uploaded)

        PdfViewer(state=self.state)
