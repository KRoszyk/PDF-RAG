from typing import Literal

from pydantic import BaseModel
import streamlit as st

from src.states.basics import TitleState
from src.states.columns import LeftColumnState, RightColumnState


class GUIState(BaseModel):
	layout_type: Literal["centered", "wide"] = "wide"
	layout_division: list[int] = [1, 1]
	left_col: LeftColumnState = LeftColumnState()
	right_col: RightColumnState = RightColumnState()
	gui_title: TitleState = TitleState(text="PDF RAG", key="pdf-rag")

	@staticmethod
	def rerun():
		st.rerun()
