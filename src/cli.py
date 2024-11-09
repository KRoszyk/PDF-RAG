import streamlit as st

from core.gui import GUI
from src.states.gui import GUIState


def run_app() -> None:
    if 'gui_state' not in st.session_state:
        st.session_state.gui_state = GUIState()

    GUI(state=st.session_state.gui_state)


if __name__ == '__main__':
    run_app()
