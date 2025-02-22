import streamlit as st

from src.app.core.gui import GUI
from src.app.states.chat import AssistanceMessage
from src.app.states.gui import GUIState
from src.rag.interface import RAGInterface


def run_app() -> None:
    if 'gui_state' not in st.session_state:
        st.session_state.gui_state = GUIState()

    state = st.session_state.gui_state
    file = state.left_col.uploader.file

    # create rag if file is uploaded
    if state.left_col.uploader.is_file_uploaded and state.left_col.rag_created is False:
        st.session_state.rag = RAGInterface(file)
        state.left_col.rag_created = True

    # get answer from RAG
    if state.left_col.chat.trigger_new_prompt:
        state.left_col.chat.messages.append(AssistanceMessage(content=st.session_state.rag.invoke(state.left_col.chat.prompt)))
        state.left_col.chat.trigger_new_prompt = False
        # get similar docs for marking text in a PDF file
        state.right_col.pdf_viewer.phrases_to_highlight = st.session_state.rag.vector_store.similar_docs

    GUI(state=st.session_state.gui_state)


if __name__ == '__main__':
    run_app()
