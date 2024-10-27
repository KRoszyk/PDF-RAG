from pydantic import BaseModel
import streamlit as st

from session_state import GUIState
from st_elements import Column1, Column2

from pydantic import BaseModel
import streamlit as st

from session_state import GUIState
from st_elements import Column1, Column2


class GUI(BaseModel):
    state: GUIState = GUIState()
    column1: Column1 = Column1(state=state)
    column2: Column2 = Column2(state=state)

    def show(self):
        col1, col2 = st.columns([1, 1])
        with col1:
            # TODO: Check why this state isn't passed into column1 object (hacked with passing new_state).
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
