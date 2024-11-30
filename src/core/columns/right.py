import streamlit as st
from attrs import define

from src.core.pdf.pdf_viewer import PdfViewer
from src.core.pdf.response_counter import ContentCounter
from src.states.gui import GUIState


@define
class RightColumn:
    state: GUIState

    def __attrs_post_init__(self):
        state = self.state
        uploader_state = self.state.left_col.uploader
        next_button_state = self.state.right_col.next_button
        previous_button_state = self.state.right_col.previous_button
        # this _ is for empty space
        _, left_col, middle_col, _, right_col, _ = st.columns(self.state.layout_right_panel)

        with left_col:
            ContentCounter(state=state)

        with middle_col:
            st.button(previous_button_state.name, disabled=not uploader_state.is_file_uploaded,
                      use_container_width=True)
        with right_col:
            st.button(next_button_state.name, disabled=not uploader_state.is_file_uploaded,
                      use_container_width=True)

        PdfViewer(state=state)
