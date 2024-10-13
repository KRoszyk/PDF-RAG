import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer
import fitz
from .css import load_css


def clear_session():
    st.session_state['pdf_show'] = False
    st.session_state.messages = []


def handle_file_upload(path: str):
    st.session_state['uploaded_file'] = st.file_uploader("Wrzuc plik PDF", type="pdf")
    if st.session_state['uploaded_file'] is not None:
        save_path = os.path.join(path)
        with open(save_path, "wb") as f:
            f.write(st.session_state['uploaded_file'].getbuffer())
        st.success("Plik został załadowany!")
        return True
    else:
        st.warning("Nie wrzucono pliku.")
        clear_session()
        return False


def generate_text():
    messages = st.container(height=5000)
    input_placeholder = st.empty()

    if prompt := input_placeholder.chat_input("Wpisz wiadomość:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": f"{prompt}"})

    with messages:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.chat_message("user").write(message["content"])
            elif message["role"] == "assistant":
                st.chat_message("assistant").write(message["content"])

def mark_text(path_file: str, path_modified_file: str):
    doc = fitz.open(path_file)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        search_text = 'MASTER DATA TRAINEE'
        text_instances = page.search_for(search_text)

        for inst in text_instances:
            highlight = page.add_rect_annot(inst)
            highlight.set_colors(stroke=(1, 0, 0))
            highlight.update()

    doc.save(path_modified_file)
    doc.close()


def show_pdf(file_uploaded: bool, path_file: str, path_modified_file: str):
    if st.button("Pokaż PDF") and file_uploaded:
        st.session_state['pdf_show'] = True
        mark_text(path_file, path_modified_file)

    if st.session_state['pdf_show']:
        pdf_viewer(path_modified_file)
    else:
        st.write(" ")


def create_gui(path_file: str, path_modified_file: str):
    st.set_page_config(layout="wide")

    col1, col2 = st.columns([1, 1])
    load_css()

    if "show_pdf" not in st.session_state:
        st.session_state.show_pdf = False

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = []

    with col1:  # left page (pdf)
        st.markdown('<h1 class="custom-title">Wrzucanie pliku</h1>', unsafe_allow_html=True)
        file_uploaded = handle_file_upload(path_file)
        placeholder = st.container(key="plh1")
        with placeholder:
            show_pdf(file_uploaded, path_file, path_modified_file)

    with col2:  # right page (chat)
        st.markdown('<h1 class="custom-title">Chat</h1>', unsafe_allow_html=True)
        placeholder = st.container(key="plh2")
        with placeholder:
            if file_uploaded:
                generate_text()
            else:
                st.info("Załaduj plik PDF, aby rozpocząć chat.")
