from attrs import define
import streamlit as st

from src.core.chat import Chat
from src.core.pdf.file_uploader import FileUploader
from src.states.gui import GUIState


@define
class LeftColumn:
	state: GUIState

	def __attrs_post_init__(self):
		chat_state = self.state.left_col.chat

		FileUploader(state=self.state)

		with st.container(key=chat_state.key):
			Chat(state=self.state)
