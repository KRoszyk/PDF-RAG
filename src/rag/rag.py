from typing import Optional

from attrs import define
from langchain_community.vectorstores import FAISS

from src.config.basics import DataPaths, ModelsNames, Template
from src.models.embedding_model import EmbeddingModel
from src.models.llm import LLM
from src.pdf_to_text.extraction import TextExtractor
from src.vector_db.initialize import create_vector_db


@define
class RAG:
    data_paths: DataPaths = DataPaths()
    models_names: ModelsNames = ModelsNames()
    template: Template = Template()
    vector_db: Optional[FAISS] = None
    text_extractor: TextExtractor = None
    embedding_model: EmbeddingModel = None
    llm: LLM = None

    def __attrs_post_init__(self):
        self.embedding_model = EmbeddingModel(embedding_model_name=self.models_names.embedding_model_name)
        self.llm = LLM(llm_model_name=self.models_names.llm_model_name, template=self.template.template)
        self.build_vector_db_from_pdf()

        # This function is necessary because, after a new PDF file is uploaded,
        # we need to extract the sentences from it and create an updated vector database.
    def build_vector_db_from_pdf(self):
        self.text_extractor = TextExtractor(file_path=self.data_paths.pdf_path)
        create_vector_db(sentences=self.text_extractor.sentences, embedding_model=self.embedding_model,
                         vector_db_path=self.data_paths.vector_db_path)
        self.vector_db = FAISS.load_local(self.data_paths.vector_db_path, self.embedding_model.model,
                                          allow_dangerous_deserialization=True)

    def get_similar_docs(self, question: str, max_docs: int) -> str:
        q_embedding = self.embedding_model.get_embed_documents([question])[0]
        relevant_docs = self.vector_db.similarity_search_by_vector(q_embedding, k=max_docs)
        return " ".join([doc.page_content for doc in relevant_docs])

    def predict(self, question: str) -> str:
        context = self.get_similar_docs(question, 5)
        answer = self.llm.llm_chain.run(question=question, context=context)
        return answer
