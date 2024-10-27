from pydantic import BaseModel
import streamlit as st
from state.session_state import GUIState


# from st_elements import Column1, Column2


class GUI(BaseModel):
    state: GUIState = GUIState()

    # column1: Column1 = Column1(state=state)
    # column2: Column2 = Column2(state=state)

    def show(self):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f'<h1 class="custom-title">{self.state.col1.title.text}</h1>', unsafe_allow_html=True)
            file = st.file_uploader(
                label=self.state.col1.uploader.name,
                type=self.state.col1.uploader.type,
                key=self.state.col1.uploader.key
            )

            if file is not None:
                self.state.col1.chat.disabled = False
            else:
                self.state.col1.chat.disabled = True

            messages_container = st.container(height=self.state.col1.chat.messages_container)
            input_placeholder = st.empty()

            if prompt := input_placeholder.chat_input(self.state.col1.chat.input_text_info,
                                                      disabled=self.state.col1.chat.disabled):
                self.state.col1.user.messages.append(prompt)
                self.state.col1.assistant.messages.append(prompt)

            with messages_container:
                for user_message, assistant_message in zip(self.state.col1.user.messages,
                                                           self.state.col1.assistant.messages):
                    st.chat_message(self.state.col1.user.role).write(user_message)
                    st.chat_message(self.state.col1.assistant.role).write(assistant_message)

        with col2:
            if st.button(self.state.col2.delete_button.name):
                self.state.col1.uploader.update_key()
                self.state.rerun()


if __name__ == '__main__':
    st.set_page_config(layout="wide")

    if st.session_state is not None:
        gui = GUI(state=st.session_state)
    else:
        gui = GUI()
        st.session_state = gui.state.dict()

    gui.show()
    gui.state.save_state()
