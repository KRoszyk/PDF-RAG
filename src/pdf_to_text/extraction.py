from typing import List

from attrs import define
from langchain_unstructured import UnstructuredLoader


@define
class TextExtractor:
    file_path: str
    sentences: List[str] = []

    def __attrs_post_init__(self):
        loader_local = UnstructuredLoader(
            file_path=self.file_path,
            strategy="hi_res",
            partition_via_api=False,
        )
        for doc in loader_local.lazy_load():
            self.sentences.append(doc.page_content)
