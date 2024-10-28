import streamlit as st
from pydantic import BaseModel
from states.session_state import GUIState


class Column1(BaseModel):
    state: GUIState

    def show(self):
        st.markdown(f'<h1 class="custom-title">{self.state.col1.title.text}</h1>', unsafe_allow_html=True)
        file = st.file_uploader(
            label=self.state.col1.uploader.name,
            type=self.state.col1.uploader.type,
            key=self.state.col1.uploader.key
        )
        # show chat if file is uploaded
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


class Column2(BaseModel):
    state: GUIState

    def show(self):
        # Button to delete the uploaded file
        if st.button(self.state.col2.delete_button.name):
            self.state.col1.uploader.update_key()
            self.state.rerun()
