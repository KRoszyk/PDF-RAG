from langchain.chains.llm import LLMChain
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from src.llm.embedding_model import EMBEDDING_MODEL


class LLM:
    def __init__(self, llm__model_name: str, template: str) -> None:
        self.llm_model = OllamaLLM(model=llm__model_name)
        self.prompt = PromptTemplate(input_variables=["question", "context"], template=template)
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm_model, verbose=True)
        self.vector_db = None

    def load_vector_db(self, vector_db_path: str, embedding_model: EMBEDDING_MODEL) -> None:
        self.vector_db = FAISS.load_local(vector_db_path, embedding_model.model, allow_dangerous_deserialization=True)

    def get_similar_docs(self, question: str, embedding_model: EMBEDDING_MODEL, max_docs: int) -> str:
        q_embedding = embedding_model.get_embed_documents([question])[0]
        relevant_docs = self.vector_db.similarity_search_by_vector(q_embedding, k=max_docs)
        return " ".join([doc.page_content for doc in relevant_docs])

    def predict(self, question: str, embedding_model: EMBEDDING_MODEL) -> str:
        context = self.get_similar_docs(question, embedding_model, 3)
        answer = self.llm_chain.run(question=question, context=context)
        return answer
