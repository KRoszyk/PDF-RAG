from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List


def create_vector_db(sentences: List[str], embedding_model: HuggingFaceEmbeddings, vector_db_path: str) -> None:
    text_embeddings = embedding_model.embed_documents(sentences)
    text_embedding_pairs = list(zip(sentences, text_embeddings))
    vector_db = FAISS.from_embeddings(text_embedding_pairs, embedding_model)
    vector_db.save_local(vector_db_path)
