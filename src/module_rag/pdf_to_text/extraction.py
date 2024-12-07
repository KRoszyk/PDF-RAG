from typing import List
from langchain_unstructured import UnstructuredLoader
from pydantic import BaseModel
from src.config import PdfPath


class TextExtractor(BaseModel):
    sentences: List[str] = []
    pdf_config: PdfPath = PdfPath()

    def extract_text(self) -> None:
        loader_local = UnstructuredLoader(
            file_path=self.pdf_config.pdf_path,
            strategy="hi_res",
            partition_via_api=False,
        )
        for doc in loader_local.lazy_load():
            self.sentences.append(doc.page_content)

    def get_sentences(self) -> List[str]:
        return self.sentences
