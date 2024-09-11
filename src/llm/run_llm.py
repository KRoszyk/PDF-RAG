from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from src.llm.find_context import similarity

TEMPLATE = """Użyj poniższych informacji, aby odpowiedzieć na pytanie na końcu.
   Jeśli nie znasz odpowiedzi, po prostu powiedz, że nie wiesz, nie próbuj wymyślać odpowiedzi.
   Użyj maksymalnie trzech zdań i postaraj się, aby odpowiedź była jak najkrótsza.
   Zawsze na końcu odpowiedzi dodaj "dzięki za pytanie!"
   {context}
   Pytanie: {question}
   Pomocna odpowiedź:"""


def generate_answer(question: str, llm_chain: LLMChain) -> str:
    context = similarity(question)
    answer = llm_chain.run(question=question, context=context)
    return answer


def run_question(question: str):
    llm_model = OllamaLLM(model="mwiewior/bielik")
    prompt = PromptTemplate(input_variables=["question", "context"], template=TEMPLATE)
    llm_chain = LLMChain(prompt=prompt, llm=llm_model, verbose=True)

    return generate_answer(question, llm_chain)
