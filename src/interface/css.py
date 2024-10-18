import streamlit as st


def load_css():
    st.markdown("""
    <style>
        :has(.st-key-plh1, .st-key-plh2) {
            height: 100%;
            overflow-y: auto;
            padding-bottom: 0px;
        }
        .st-key-plh1, .st-key-plh2 {
            overflow-x: hidden;
        }
    </style>
    """, unsafe_allow_html=True)