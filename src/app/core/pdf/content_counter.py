import streamlit as st
from attrs import define

from src.app.states.gui import GUIState


@define
class ContentCounter:
    state: GUIState

    def __attrs_post_init__(self):
        uploader_state = self.state.left_col.uploader
        content_counter = self.state.right_col.content_counter
        content_counter.text = str(self.state.right_col.scroll_counter.actual_scroll_position) + "/" + str(
            self.state.right_col.scroll_counter.scroll_count)
        if uploader_state.is_file_uploaded is True:
            st.markdown(
                f'<p style="font-size: {content_counter.font_size}px;">{content_counter.text}</p>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<p style="font-size: {content_counter.font_size}px; color: {content_counter.disable_color};">'
                f'{content_counter.text}</p>',
                unsafe_allow_html=True
            )
