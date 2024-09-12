import streamlit as st
import os

def add_custom_css():
    st.markdown(
        f"""
              <style>
              /* Ustawienie tła dla całej strony */
              .stApp {{
                  background-image: url("https://img.freepik.com/darmowe-wektory/szablon-ramki-niebieski-krzywa_53876-99024.jpg?t=st=1725212108~exp=1725215708~hmac=8ab3e63ad7cecc8747185f54599e74066417b6f5eebe5daaaaebe02b9fd92dd5&w=1060");
                  background-size: cover;
                  background-repeat: no-repeat;
                  background-attachment: fixed;
              }}

        /* Zmiana stylu tytułu */
        .stTitle {{
            color: white;
            font-size: 3em;
            text-shadow: 2px 2px 4px #000000;
        }}

        /* Zmiana stylu pola tekstowego */
        .stTextInput {{
            font-size: 1.2em;
            color: #333;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def handle_file_upload(path):
    uploaded_file = st.file_uploader("Drop your PDF file here", type="pdf")
    if uploaded_file is not None:
        st.session_state['file_loaded'] = True
        st.session_state['uploaded_file'] = uploaded_file
        save_path = os.path.join(path, "plik.pdf")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    else:
        st.warning("Uploaded file is empty!")


def generate_text():
    user_query = st.session_state.get('user_input', '')
    if user_query.strip():
        generated_content = f"Response to: {user_query}"
        st.session_state['generated_text'] += f"User: {user_query}\nBot: {generated_content}\n\n"
        st.session_state['user_input'] = ''


def create_gui(path):
    add_custom_css()

    st.title("CHATBOX")

    handle_file_upload(path)

    st.text_area("Generated text will appear here", value=st.session_state.get('generated_text', ''), height=450,
                 key='generated_text_display')

    st.text_area("Enter your text here", height=100,
                 key='user_input')

    st.button("Send a query", on_click=generate_text)


