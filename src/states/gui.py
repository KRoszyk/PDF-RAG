import streamlit as st

from pydantic import BaseModel
from typing import Literal

from src.states.basics import TitleState
from src.states.columns import LeftColumnState, RightColumnState


class GUIState(BaseModel):
    layout_type: Literal["centered", "wide"] = "wide"
    layout_division: list[int] = [1, 1]
    layout_left_panel: list[int] = [0.5, 1, 0.1, 1, 0.5]
    layout_right_panel: list[int] = [0.5, 0.7, 1, 0.1, 1, 0.5]
    left_col: LeftColumnState = LeftColumnState()
    right_col: RightColumnState = RightColumnState()
    gui_title: TitleState = TitleState(text="PDF RAG", key="pdf-rag")

    @staticmethod
    def rerun():
        st.rerun()
