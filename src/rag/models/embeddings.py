from attrs import define, field
from langchain_huggingface import HuggingFaceEmbeddings

from src.rag.config import EmbeddingModelConfig


@define(auto_attribs=True)
class EmbeddingModel:
    config: EmbeddingModelConfig = EmbeddingModelConfig()
    model: HuggingFaceEmbeddings = field(init=False)

    def __attrs_post_init__(self):
        self.model = HuggingFaceEmbeddings(model_name=self.config.embeddings_model_name)

    def get_embed_documents(self, documents: list[str]) -> list[list[float]]:
        return self.model.embed_documents(documents)

    def get_embedding_pairs(self, documents: list[str]) -> list[tuple[str, list[float]]]:
        text_embeddings = self.get_embed_documents(documents)
        return list(zip(documents, text_embeddings))
