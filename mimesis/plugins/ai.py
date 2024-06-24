"""
use ai for generating your data
"""
try:
    from langchain_huggingface import HuggingFaceEndpoint
    from langchain_core.prompts import PromptTemplate
except ImportError:
    raise ImportError("langchain_huggingface,\
                    langchain_core is required to run this plugin")

from ai_config import default_prompt, default_model_name
class TextAI:
    def __init__(self, model=None):
        if not model:
            self.model = default_model_name
        else:
            self.model = model
        self.llm = HuggingFaceEndpoint(repo_id=self.model, temperature=0.5)
        self.prompt_template = default_prompt

    def chat(self, question, prompt_template=None):
        if prompt_template:
            self.prompt_template = prompt_template
        prompt = PromptTemplate.from_template(self.prompt_template)
        llm_chain = prompt | self.llm
        return llm_chain.invoke({"question": question})


if __name__ == "__main__":
    text_object = TextAI()
    result = text_object.chat("generate a random fruit.")
    print(result)
