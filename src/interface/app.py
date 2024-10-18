import streamlit as st

from typing import List
from .css import load_css
from .gui import Gui


def create_gui(path_file: str,
               path_modified_file: str,
               message_container_height: int,
               layout_division: List[int]) -> None:

    if "application" not in st.session_state:
        st.session_state.application = Gui(path_file, path_modified_file, message_container_height)

    load_css()
    col1, col2 = st.columns(layout_division)

    with col1:
        st.markdown('<h1 class="custom-title">Load file</h1>', unsafe_allow_html=True)
        st.session_state.application.upload_file()
        placeholder = st.container(key="plh1")
        with placeholder:
            if st.session_state.application.is_file_uploaded is True:
                st.session_state.application.prompt_and_prediction()

    with col2:
        placeholder = st.container(key="plh2")
        with placeholder:
            st.session_state.application.show_file()
            st.markdown('<h1 class="custom-title"></h1>', unsafe_allow_html=True)
