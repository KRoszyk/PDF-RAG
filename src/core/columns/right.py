from attrs import define
import streamlit as st

from src.states.gui import GUIState


@define
class RightColumn:
	state: GUIState

	def __attrs_post_init__(self):
		# Button to delete the uploaded file.
		if st.button(self.state.right_col.delete_button.name):
			self.state.left_col.uploader.update_key()
			self.state.rerun()
