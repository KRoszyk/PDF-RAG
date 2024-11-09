from attrs import define
import streamlit as st

from src.core.columns.left import LeftColumn
from src.core.columns.right import RightColumn
from src.states.gui import GUIState
from src.styles.css import load_css


@define
class GUI:
	state: GUIState = GUIState()

	def __attrs_post_init__(self):
		# Set the layout to cover all the page.
		st.set_page_config(layout=self.state.layout_type)
		# Load CSS styling.
		load_css(state=self.state)
		# Add header to the page.
		st.title(self.state.gui_title.text)

		left_column, right_column = st.columns(self.state.layout_division)
		with left_column:
			LeftColumn(state=self.state)
		with right_column:
			RightColumn(state=self.state)
