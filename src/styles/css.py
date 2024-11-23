import streamlit as st

from src.states.gui import GUIState


def load_css(state: GUIState):
	chat_state = state.left_col.chat
	gui_title = state.gui_title
	pdf_viewer = state.right_col.pdf_viewer

	st.markdown(f"""
	<style>
		:has(.st-key-{chat_state.key}, .st-key-{pdf_viewer.key}) {{
			height: 100%;
			overflow-y: auto;
			padding-bottom: 2px;
		}}
		.st-key-{chat_state.key}, .st-key-{pdf_viewer.key} {{
			overflow-x: hidden;
		}}
		h1[id={gui_title.key}] {{
			text-align: center;
			margin-top: -1%;
			margin-bottom: 1%;
			padding-top: 0px;
		}}
	</style>
	""", unsafe_allow_html=True)
