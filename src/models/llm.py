from attrs import define
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM


@define
class LLM:
    template: str
    llm_model_name: str
    llm_model: OllamaLLM = None
    llm_chain: LLMChain = None
    prompt: PromptTemplate = None

    def __attrs_post_init__(self):
        self.llm_model = OllamaLLM(model=self.llm_model_name)
        self.prompt = PromptTemplate(input_variables=["question", "context"], template=self.template)
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm_model, verbose=True)

    def get_llm_chain(self):
        return self.llm_chain
