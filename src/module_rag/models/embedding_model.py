from attrs import define, field
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List, Tuple
from src.config import EmbeddingModelConfig


@define(auto_attribs=True)
class EmbeddingModel:
    model_config: EmbeddingModelConfig = EmbeddingModelConfig()
    model: HuggingFaceEmbeddings = field(init=False)

    def __attrs_post_init__(self):
        self.model = HuggingFaceEmbeddings(model_name=self.model_config.embedding_model_name)

    def get_embed_documents(self, documents: List[str]) -> List[List[float]]:
        return self.model.embed_documents(documents)

    def get_embedding_pairs(self, documents: List[str]) -> List[Tuple[str, List[float]]]:
        text_embeddings = self.get_embed_documents(documents)
        return list(zip(documents, text_embeddings))
