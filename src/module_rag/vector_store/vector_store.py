from attr import define, field
from typing import List
from langchain_community.vectorstores import FAISS

from src.config import VectorDb
from src.module_rag.models.embedding_model import EmbeddingModel


@define(auto_attribs=True)
class VectorStore:
    embedding_model: EmbeddingModel
    vector_db_config: VectorDb = VectorDb()
    vector_db: FAISS = field(init=False)

    def load_vector_db(self) -> None:
        self.vector_db = FAISS.load_local(
            self.vector_db_config.vector_db_path,
            self.embedding_model.model,
            allow_dangerous_deserialization=True
        )

    def create_vector_db(self, sentences: List[str]) -> None:
        text_embedding_pairs = self.embedding_model.get_embedding_pairs(sentences)
        self.vector_db = FAISS.from_embeddings(text_embedding_pairs, self.embedding_model.model)
        self.vector_db.save_local(self.vector_db_config.vector_db_path)

    def get_similar_docs(self, question: str) -> str:
        q_embedding = self.embedding_model.get_embed_documents([question])[0]
        relevant_docs = self.vector_db.similarity_search_by_vector(
            q_embedding,
            k=self.vector_db_config.max_documents
        )
        return " ".join([doc.page_content for doc in relevant_docs])
