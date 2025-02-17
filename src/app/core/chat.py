import streamlit as st
from attrs import define

from src.app.states.chat import UserMessage, AssistanceMessage
from src.app.states.gui import GUIState


@define
class Chat:
    state: GUIState

    def __attrs_post_init__(self):
        chat_state = self.state.left_col.chat
        messages_container = st.container(height=chat_state.container_height)

        # Update ChatState with the newest messages.
        if prompt := st.chat_input(
            placeholder=chat_state.input_text_info,
            disabled=chat_state.disabled

        ):
            chat_state.messages.append(UserMessage(content=prompt))
            chat_state.messages.append(AssistanceMessage(content=st.session_state.rag.invoke(prompt)))

        # Display chat messages from history on app rerun.
        with messages_container:
            for message in chat_state.messages:
                with st.chat_message(name=message.name):
                    st.markdown(message.content, unsafe_allow_html=True)
