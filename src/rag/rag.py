from typing import Optional

from attrs import define
from langchain_community.vectorstores import FAISS

from src.config.basics import DataPaths, MaxDocuments, ModelsNames, Template
from src.models.embedding_model import EMBEDDING_MODEL
from src.models.llm import LLM
from src.pdf_to_text.extraction import TextExtractor
from src.vector_db.vector_db import VectorDbCreator


@define
class RAG:
    data_paths: DataPaths = DataPaths()
    models_names: ModelsNames = ModelsNames()
    template: Template = Template()
    max_docs: MaxDocuments = MaxDocuments()
    vector_db: FAISS | None = None
    text_extractor: TextExtractor = None
    embedding_model: EMBEDDING_MODEL = None
    llm: LLM = None

    def __attrs_post_init__(self):
        self.embedding_model = EMBEDDING_MODEL(embedding_model_name=self.models_names.embedding_model_name)
        self.llm = LLM(llm_model_name=self.models_names.llm_model_name, template=self.template.template)
        self.build_vector_db_from_pdf()

        # This function is necessary because, after a new PDF file is uploaded,
        # we need to extract the sentences from it and create an updated vector database.

    def build_vector_db_from_pdf(self):
        self.text_extractor = TextExtractor(file_path=self.data_paths.pdf_path)

        # We don't need to keep the object because its only job is to create the vector database and save it to a file
        # Maybe it should be a function?
        VectorDbCreator(sentences=self.text_extractor.get_sentences(), embedding_model=self.embedding_model,
                        vector_db_path=self.data_paths.vector_db_path)
        self.vector_db = FAISS.load_local(self.data_paths.vector_db_path, self.embedding_model.model,
                                          allow_dangerous_deserialization=True)

    def get_similar_docs(self, question: str, ) -> str:
        q_embedding = self.embedding_model.get_embed_documents([question])[0]
        relevant_docs = self.vector_db.similarity_search_by_vector(q_embedding, k=self.max_docs.max_documents)
        return " ".join([doc.page_content for doc in relevant_docs])

    def predict(self, question: str) -> str:
        context = self.get_similar_docs(question)
        answer = self.llm.get_llm_chain().run(question=question, context=context)
        return answer
