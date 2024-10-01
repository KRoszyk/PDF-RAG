from typing import List, Tuple
from langchain_huggingface import HuggingFaceEmbeddings


class EMBEDDING_MODEL:
    def __init__(self, embedding_model_name: str) -> None:
        self.model = HuggingFaceEmbeddings(model_name=embedding_model_name)

    def get_embed_documents(self, documents: List[str]) -> List[list[float]]:
        return self.model.embed_documents(documents)

    def get_embedding_pairs(self, documents: List[str]) -> List[Tuple[str, list]]:
        text_embeddings = self.get_embed_documents(documents)
        return list(zip(documents, text_embeddings))
