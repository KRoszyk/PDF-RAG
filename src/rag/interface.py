from attrs import define, field

from src.rag.models.embeddings import EmbeddingModel
from src.rag.models.llm import LLM
from src.rag.pdf_parser.extractor import TextExtractor
from src.rag.vector_store.vector_store import VectorStore


@define
class RAGInterface:
    file: bytes
    embedding_model: EmbeddingModel = EmbeddingModel()
    llm: LLM = LLM()
    vector_store: VectorStore = field(init=False)
    text_extractor: TextExtractor = field(init=False)

    def __attrs_post_init__(self):
        self.text_extractor = TextExtractor(file=self.file)
        self.vector_store = VectorStore(
            embedding_model=self.embedding_model,
            sentences=self.text_extractor.sentences
        )

    def invoke(self, question: str) -> str:
        context = self.vector_store.get_similar_docs(question)
        answer = self.llm.invoke(question, context)
        return answer
