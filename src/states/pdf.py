import random
import string
from typing import Literal

from pydantic import BaseModel


class PDFUploaderState(BaseModel):
	name: str = "uploader"
	key: str = ""
	type: str = "pdf"
	label_visibility: Literal["visible", "hidden", "collapsed"] = "collapsed"
	disabled_message: str = "Upload a file to start the conversation about your document!"

	def update_key(self, length: int = 10) -> None:
		self.key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
