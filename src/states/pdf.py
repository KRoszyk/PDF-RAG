import random
import string
from typing import Literal, Optional

from pydantic import BaseModel


class PDFUploaderState(BaseModel):
	name: str = "uploader"
	key: str = ""
	type: str = "pdf"
	is_file_uploaded: bool = False
	file: Optional[bytes] = None
	label_visibility: Literal["visible", "hidden", "collapsed"] = "collapsed"
	disabled_message: str = "Upload a file to start the conversation about your document!"

	def update_key(self, length: int = 10) -> None:
		self.key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class PdfViewerState(BaseModel):
	key: str = "viewer"
