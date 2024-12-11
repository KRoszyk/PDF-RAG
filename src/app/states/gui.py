import streamlit as st

from pydantic import BaseModel
from typing import Literal

from src.app.states.basics import TitleState
from src.app.states.columns import LeftColumnState, RightColumnState


class GUIState(BaseModel):
    app_title: str = "PDF RAG"
    layout_type: Literal["centered", "wide"] = "wide"
    layout_division: list[int] = [1, 1]
    left_col: LeftColumnState = LeftColumnState()
    right_col: RightColumnState = RightColumnState()
    gui_title: TitleState = TitleState(text=app_title, key="pdf-rag")

    @staticmethod
    def rerun():
        st.rerun()
