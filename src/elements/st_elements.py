# import streamlit as st
# from pydantic import BaseModel
#
# from session_state import GUIState
#
#
# class Column1(BaseModel):
#     state: GUIState
#
#     def show(self, new_state: GUIState):
#         print(self.state.col1)
#         st.markdown(f'<h1 class="custom-title">{self.state.col1.title.text}</h1>', unsafe_allow_html=True)
#         st.file_uploader(
#             label=self.state.col1.uploader.name,
#             type=self.state.col1.uploader.type,
#             key=new_state.col1.uploader.key
#         )
#         st.container(height=self.state.col1.chat.messages_container)
#         input_placeholder = st.empty()
#
#         if prompt := input_placeholder.chat_input(self.state.col1.chat.input_text_info,
#                                                   disabled=self.state.col1.chat.disabled):
#             self.state.col1.user.update_content(prompt)
#             self.state.col1.assistance.update_content(prompt)
#             self.state.col1.chat.add_user_message(self.state.col1.user.content)
#             self.state.col1.chat.add_assistant_message(self.state.col1.assistance.content)
#             self.state.rerun()
#
#
# class Column2(BaseModel):
#     state: GUIState
#
#     def show(self):
#         # Button to delete the uploaded file
#         if st.button(self.state.col2.delete_button.name):
#             self.state.col1.uploader.update_key()
#             self.state.rerun()
