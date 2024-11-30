import streamlit as st
from attrs import define

from src.states.gui import GUIState


@define
class ContentCounter:
    state: GUIState

    def __attrs_post_init__(self):
        uploader_state = self.state.left_col.uploader
        count_content = self.state.right_col.count_content

        if uploader_state.is_file_uploaded is True:
            st.markdown(f'<p style="font-size: 24px;">{count_content.text}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="font-size: 24px; color: gray;">{count_content.text}</p>', unsafe_allow_html=True)
