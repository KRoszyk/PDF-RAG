from attrs import define, Factory
from langchain_unstructured import UnstructuredLoader

from src.rag.config import PdfPath


@define
class TextExtractor:
    pdf_config: PdfPath = PdfPath()
    sentences: list[str] = Factory(list)

    def __attrs_post_init__(self):
        loader_local = UnstructuredLoader(
            file_path=self.pdf_config.pdf_path,
            strategy="hi_res",
            partition_via_api=False,
        )
        for doc in loader_local.lazy_load():
            self.sentences.append(doc.page_content)
