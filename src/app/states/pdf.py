import random
import string

from pydantic import BaseModel
from typing import Literal


class PDFUploaderState(BaseModel):
    name: str = "uploader"
    key: str = ""
    type: str = "pdf"
    is_file_uploaded: bool = False
    file: bytes | None = None
    label_visibility: Literal["visible", "hidden", "collapsed"] = "collapsed"
    disabled_message: str = "Upload a file to start the conversation about your document!"

    def update_key(self, length: int = 10) -> None:
        self.key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class PdfViewerState(BaseModel):
    key: str = "viewer"
    json_path: str = "data/json/spans_metadata.json"
    phrases_to_highlight: list[str] = []

    def update_key(self, length: int = 10) -> None:
        self.key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class ContentCounter(BaseModel):
    text: str = '0/0'
    font_size: int = 24
    disable_color: str = 'gray'
