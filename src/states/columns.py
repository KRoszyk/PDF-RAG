from pydantic import BaseModel

from src.states.basics import ButtonState, TextState
from src.states.chat import ChatState
from src.states.pdf import PDFUploaderState, PdfViewerState


class LeftColumnState(BaseModel):
    uploader: PDFUploaderState = PDFUploaderState()
    chat: ChatState = ChatState()
    delete_button: ButtonState = ButtonState(name="Delete PDF")
    clear_button: ButtonState = ButtonState(name="Clear chat")


class RightColumnState(BaseModel):
    count_content: TextState = TextState(text="0/0")
    previous_button: ButtonState = ButtonState(name="previous")
    next_button: ButtonState = ButtonState(name="next")
    pdf_viewer: PdfViewerState = PdfViewerState()
