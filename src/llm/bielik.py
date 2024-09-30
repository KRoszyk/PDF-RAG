from langchain.chains.llm import LLMChain
from langchain_ollama.llms import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS


class LLM:
    def __init__(self, model_name: str, template: str, embedding_model: HuggingFaceEmbeddings) -> None:
        self.embedding_model = embedding_model
        self.llm_model = OllamaLLM(model=model_name)
        self.prompt = PromptTemplate(input_variables=["question", "context"], template=template)
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm_model, verbose=True)
        self.question = "Co tam?"
        self.vector_db_path = None
        self.vector_db = None

    def load_vector_db(self, vector_db_path: str) -> None:
        self.vector_db = FAISS.load_local(vector_db_path, self.embedding_model, allow_dangerous_deserialization=True)

    def similarity(self) -> str:
        q_embedding = self.embedding_model.embed_documents([self.question])[0]
        relevant_doc = self.vector_db.similarity_search_by_vector(q_embedding, k=1)
        return relevant_doc[0].page_content

    def generate_answer(self) -> str:
        context = self.similarity()
        answer = self.llm_chain.run(question=self.question, context=context)
        return answer
