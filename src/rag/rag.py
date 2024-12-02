from attrs import define
from src.models.embedding_model import EmbeddingModel
from src.models.llm import Llm
from src.pdf_to_text.extraction import TextExtractor
from src.vector_store.vector_store import VectorStore


@define
class Rag:
    text_extractor: TextExtractor = TextExtractor()
    embedding_model: EmbeddingModel = EmbeddingModel()
    llm: Llm = Llm()
    vector_store: VectorStore = None  # We can't create vector stores here because they require an embedding model

    def __attrs_post_init__(self):
        self.vector_store = VectorStore(embedding_model=self.embedding_model)

    def parse_pdf(self) -> None:
        self.text_extractor.extract_text()

    def create_vector_db(self) -> None:
        self.vector_store.create_vector_db(sentences=self.text_extractor.get_sentences())

    def load_vector_db(self) -> None:
        self.vector_store.load_vector_db()

    def predict(self, question: str) -> str:
        context = self.vector_store.get_similar_docs(question)
        answer = self.llm.get_answer(question, context)
        return answer
