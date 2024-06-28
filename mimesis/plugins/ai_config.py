default_prompt = """
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
default_model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"