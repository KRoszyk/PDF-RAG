import random
import string
import streamlit as st

from typing import List
from pydantic import BaseModel


class AssistanceMessage(BaseModel):
    role: str = "assistant"
    messages: List[str] = []


class UserMessages(BaseModel):
    role: str = "user"
    messages: List[str] = []


class Chat(BaseModel):
    messages_container: int = 450
    input_text_info: str = "Enter your message:"
    disabled: bool = True


class PDFUploader(BaseModel):
    name: str = "Upload PDF file"
    key: str = ""
    type: str = "pdf"

    def update_key(self, length: int = 10) -> None:
        self.key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class Button(BaseModel):
    name: str = ""


class Title(BaseModel):
    text: str = ""


class Column1(BaseModel):
    title: Title = Title(text="Load file")
    uploader: PDFUploader = PDFUploader()
    user: UserMessages = UserMessages()
    assistant: AssistanceMessage = AssistanceMessage()
    chat: Chat = Chat()


class Column2(BaseModel):
    delete_button: Button = Button(name="Delete PDF")


class GUIState(BaseModel):
    col1: Column1 = Column1()
    col2: Column2 = Column2()

    def save_state(self):
        st.session_state = self.dict()

    def rerun(self):
        self.save_state()
        st.rerun()
