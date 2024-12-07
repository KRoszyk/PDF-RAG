from attrs import define, field
from src.module_rag.models.embedding_model import EmbeddingModel
from src.module_rag.models.llm import Llm
from src.module_rag.pdf_to_text.extraction import TextExtractor
from src.module_rag.vector_store.vector_store import VectorStore


@define
class Rag:
    text_extractor: TextExtractor = TextExtractor()
    embedding_model: EmbeddingModel = EmbeddingModel()
    llm: Llm = Llm()
    vector_store: VectorStore = field(init=False)

    def __attrs_post_init__(self):
        self.vector_store = VectorStore(embedding_model=self.embedding_model)
        self.text_extractor.extract_text()
        self.vector_store.create_vector_db(sentences=self.text_extractor.get_sentences())
        self.vector_store.load_vector_db()

    def predict(self, question: str) -> str:
        context = self.vector_store.get_similar_docs(question)
        answer = self.llm.get_answer(question, context)
        return answer
