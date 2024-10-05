import streamlit as st


def load_css():
    st.markdown("""
    <style>
        .st-emotion-cache-13ln4jf {
            width: 100%;
            padding: 2rem 1rem 0rem;
            max-width: 80rem;
        }
        .st-emotion-cache-ocqkz7 {
            display: flex;
            flex-wrap: wrap;
            -webkit-box-flex: 1;
            flex-grow: 1;
            -webkit-box-align: stretch;
            align-items: stretch;
            gap: 2rem;
        }

    </style>
    """, unsafe_allow_html=True)