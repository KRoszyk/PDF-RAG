from typing import List

from langchain_community.vectorstores import FAISS
from src.models.embedding_model import EmbeddingModel


def create_vector_db(sentences: List[str], embedding_model: EmbeddingModel, vector_db_path: str) -> None:
    text_embedding_pairs = embedding_model.get_embedding_pairs(sentences)
    vector_db = FAISS.from_embeddings(text_embedding_pairs, embedding_model.model)
    vector_db.save_local(vector_db_path)
