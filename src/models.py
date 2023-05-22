import pandas as pd
from abc import ABC, abstractmethod
from config import *


class OpenAI(ABC):
    def __init__(self):
        self.dataset = pd.read_excel("dataset/dataset_tr.xlsx")

        self.prompt = ""

    def getResponse(self, model="gpt-3.5-turbo"):
        setConfig()
        if model == "gpt-3.5-turbo":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Sen bir Türkçe dilbilimcisin."},
                    {"role": "user", "content": self.prompt},
                ],
                max_tokens=3250,
                temperature=0,
            )
            return response.get("choices")[0].get("message").get("content")  # type: ignore
        elif model == "text-davinci-003":
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=self.prompt,
                temperature=0,
                max_tokens=3000,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0.5,
            )
            return response.get("choices")[0].get("text")  # type: ignore

    @abstractmethod
    def setPrompt():
        ...


class Generator(OpenAI):
    def __init__(self) -> None:
        super().__init__()

    def setPrompt(self, prompt=None, st_idx=0, end_idx=3, vis_prompt=False):
        if not prompt:
            with open("src/requirements_prompts/generetor_requirements.txt") as f:
                self.prompt = f.read()

            unique_idioms = self.dataset["idiom"].unique()

            for i, data in enumerate(unique_idioms[st_idx:end_idx]):
                self.prompt += f"\n {i+1}. {data}"
            self.prompt += "\n"
        else:
            self.prompt = prompt

        if vis_prompt:
            print(self.prompt + "\n")


class Classifier(OpenAI):
    def __init__(self):
        super().__init__()

    def setPrompt(self, prompt, vis_prompt=False):
        with open("src/requirements_prompts/classifier_requirements.txt") as f:
            requirements = f.read()
        self.prompt = prompt + "\n" + requirements
        if vis_prompt:
            print(self.prompt + "\n")
