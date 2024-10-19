import streamlit as st


def initialize_variables() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None



