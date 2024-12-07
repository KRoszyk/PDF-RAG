import streamlit as st
from attrs import define

from src.core.pdf.pdf_viewer import PdfViewer
from src.core.pdf.content_counter import ContentCounter
from src.states.gui import GUIState


@define
class RightColumn:
    state: GUIState

    def __attrs_post_init__(self):
        state = self.state
        right_col_state = state.right_col
        uploader_state = self.state.left_col.uploader
        next_button_state = right_col_state.next_button
        previous_button_state = right_col_state.previous_button
        _, content_counter_text, prev_content_button, _, next_content_button, _ = st.columns(right_col_state.buttons_panel_layout)

        with content_counter_text:
            ContentCounter(state=state)

        with prev_content_button:
            st.button(previous_button_state.name, disabled=not uploader_state.is_file_uploaded,
                      use_container_width=True)

        with next_content_button:
            st.button(next_button_state.name, disabled=not uploader_state.is_file_uploaded,
                      use_container_width=True)

        PdfViewer(state=state)
