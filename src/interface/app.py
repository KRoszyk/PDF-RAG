import streamlit as st

from typing import List
from .css import load_css
from .gui import Gui


def create_gui(path_file: str,
               path_modified_file: str,
               message_container_height: int,
               layout_division: List[int]) -> None:

    if "application" not in st.session_state:
        st.session_state.application = Gui(path_file, path_modified_file, message_container_height, layout_division)

    st.session_state.application.show_gui()
