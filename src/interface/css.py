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
          .st-emotion-cache-13ln4jf {
            width: 90%;
            padding: 3rem 0rem 3rem;
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