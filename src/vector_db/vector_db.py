from attrs import define
from typing import List

from langchain_community.vectorstores import FAISS
from src.models.embedding_model import EMBEDDING_MODEL


@define
class VectorDbCreator:
    sentences: List[str]
    vector_db_path: str
    embedding_model: EMBEDDING_MODEL

    def __attrs_post_init__(self):
        text_embedding_pairs = self.embedding_model.get_embedding_pairs(self.sentences)
        vector_db = FAISS.from_embeddings(text_embedding_pairs, self.embedding_model.model)
        vector_db.save_local(self.vector_db_path)
