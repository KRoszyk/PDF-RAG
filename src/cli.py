import streamlit as st

from src.app.core.gui import GUI
from src.app.states.gui import GUIState
from src.rag.interface import RAGInterface


def run_app() -> None:
    if 'gui_state' not in st.session_state:
        st.session_state.gui_state = GUIState()

    state = st.session_state.gui_state
    file = state.left_col.uploader.file
    if state.left_col.uploader.is_file_uploaded and state.left_col.rag_bool is False:
        if file is not None:
            st.session_state.rag = RAGInterface(file)
            state.left_col.rag_bool = True

    GUI(state=st.session_state.gui_state)
    print("refresh gui")


if __name__ == '__main__':
    run_app()
