from attrs import define, field
from langchain.chains.llm import LLMChain
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from src.config import LlmModelConfig, Template


@define
class Llm:
    template: Template = Template()
    model_config: LlmModelConfig = LlmModelConfig()
    llm_model: OllamaLLM = field(init=False)
    llm_chain: LLMChain = field(init=False)
    prompt: PromptTemplate = field(init=False)

    def __attrs_post_init__(self):
        self.llm_model = OllamaLLM(model=self.model_config.llm_model_name)
        self.prompt = PromptTemplate(input_variables=["question", "context"], template=self.template.template)
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm_model, verbose=True)

    def get_answer(self, question: str, context: str) -> str:
        return self.llm_chain.run(question=question, context=context)
