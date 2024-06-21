from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate


class TextAI:
    def __init__(self, model=None):
        if not model:
            self.model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
        else:
            self.model = model
        self.llm = HuggingFaceEndpoint(repo_id=self.model, temperature=0.5)
        self.prompt_template = """
        Answer the following question after <<<>>> with only one word.
        Do not include any other information.
        You will only respond with one word, Do not provide explanations or notes.

        ####
        Here are some examples:

        Question: generate a random number.
        Answer: 10
        Question: generate a random fruit name.
        Answer: apple
        Question: generate a random name.
        Answer: brad
        ###

        <<<
        Question: {question}
        >>>
        """

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
