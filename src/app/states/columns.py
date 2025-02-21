from pydantic import BaseModel

from src.app.states.basics import ButtonState, FoundPages
from src.app.states.chat import ChatState
from src.app.states.pdf import PDFUploaderState, PdfViewerState
from src.app.states.pdf import ContentCounter


class LeftColumnState(BaseModel):
    buttons_panel_layout: list[float] = [0.5, 1, 0.1, 1,
                                         0.5]  # These values are hardcoded to set widths of the streamlit buttons.
    delete_button: ButtonState = ButtonState(name="Delete PDF")
    clear_button: ButtonState = ButtonState(name="Clear chat")
    uploader: PDFUploaderState = PDFUploaderState()
    chat: ChatState = ChatState()
    rag_trigger: bool = False


class RightColumnState(BaseModel):
    buttons_panel_layout: list[float] = [0.5, 0.5, 1, 0.1, 1,
                                         0.5]  # These values are hardcoded to set widths of the streamlit buttons.
    previous_button: ButtonState = ButtonState(name="previous")
    next_button: ButtonState = ButtonState(name="next")
    pdf_viewer: PdfViewerState = PdfViewerState()
    content_counter: ContentCounter = ContentCounter()
    found_pages: FoundPages = FoundPages()
