import streamlit as st

from pydantic import BaseModel
from typing import Optional
from states.session_state import GUIState
from elements.st_elements import Column1, Column2


class GUI(BaseModel):
    state: GUIState = GUIState()
    column1: Optional[Column1] = None
    column2: Optional[Column2] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.column1 = Column1(state=self.state)
        self.column2 = Column2(state=self.state)

    def show(self):
        col1, col2 = st.columns([1, 1])
        with col1:
            self.column1.show()
        with col2:
            self.column2.show()


if __name__ == '__main__':
    st.set_page_config(layout="wide")

    if st.session_state is not None:
        gui = GUI(state=st.session_state)
    else:
        gui = GUI()
        st.session_state = gui.state.dict()

    gui.show()
    gui.state.save_state()
