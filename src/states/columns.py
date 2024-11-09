from pydantic import BaseModel

from src.states.basics import ButtonState
from src.states.chat import ChatState
from src.states.pdf import PDFUploaderState


class LeftColumnState(BaseModel):
	uploader: PDFUploaderState = PDFUploaderState()
	chat: ChatState = ChatState()


class RightColumnState(BaseModel):
	delete_button: ButtonState = ButtonState(name="Delete PDF")
