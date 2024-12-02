from typing import List
from langchain_community.vectorstores import FAISS
from pydantic import BaseModel

from src.config.basics import MaxDocuments, VectorDbPath
from src.models.embedding_model import EmbeddingModel


class VectorStore(BaseModel):
    embedding_model: EmbeddingModel
    vector_db_config: VectorDbPath = VectorDbPath()
    max_docs: MaxDocuments = MaxDocuments()
    vector_db: FAISS = None

    class Config:
        arbitrary_types_allowed = True

    def load_vector_db(self) -> None:
        self.vector_db = FAISS.load_local(
            self.vector_db_config.vector_db_path,
            self.embedding_model.model,
            allow_dangerous_deserialization=True)

    def create_vector_db(self, sentences: List[str]) -> None:
        text_embedding_pairs = self.embedding_model.get_embedding_pairs(sentences)
        vector_db = FAISS.from_embeddings(text_embedding_pairs, self.embedding_model.model)
        vector_db.save_local(self.vector_db_config.vector_db_path)

    def get_similar_docs(self, question: str) -> str:
        q_embedding = self.embedding_model.get_embed_documents([question])[0]
        relevant_docs = self.vector_db.similarity_search_by_vector(q_embedding, k=self.max_docs.max_documents)
        return " ".join([doc.page_content for doc in relevant_docs])
