import re

from attrs import define, field
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_ollama.llms import OllamaLLM

from src.rag.config import LLMConfig


@define
class LLM:
    config: LLMConfig = LLMConfig()
    llm_chain: Runnable = field(init=False)

    def __attrs_post_init__(self):
        llm_model = OllamaLLM(model=self.config.llm_model_name)
        prompt = PromptTemplate.from_template(self.config.prompt)
        self.llm_chain = prompt | llm_model | StrOutputParser()

    def invoke(self, question: str, context: str) -> str:
        llm_response = self.llm_chain.invoke({'input': question, 'context': context})
        return self.postprocess_output(llm_response)

    @staticmethod
    def postprocess_output(text: str) -> str:
        # This postprocessing removes <s> tag at the beginning of the LLM response.
        return re.sub(r"<s>\s*", "", text)
