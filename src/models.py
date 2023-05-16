import pandas as pd
from abc import ABC, abstractmethod
from config import *


class OpenAI(ABC):
    def __init__(self):
        self.dataset = pd.read_excel('dataset/dataset_tr.xlsx')

        self.prompt = ""

    @abstractmethod
    def setPrompt(prompt=None):
        ...

    @abstractmethod
    def getResponse():
        ...


class Generator(OpenAI):
    def __init__(self) -> None:
        super().__init__()

    def setPrompt(self, prompt=None):
        if not prompt:
            self.prompt = "Merhaba, ben Türkçeyi öğrenmeye yeni başladım. Deyimleri öğrenirken çok zorluk çekmekteyim.\
                            Bu yüzden çeşitli deyim ve deyim olmayan örneklere ihtiyacım var.\
                            Örneğin 'adım atmak' deyimi için\
                            Şöyle bir deyim örneğine ihtiyacım var 'Atmadan önce adımını iki kere düşün.' ve şöyle bir deyim olmayan örneğine ihtiyacım var\
                            'Adım atacak yer yoktu'\
                            Bana aşağıdaki kelimeler için deyim olan ve deyim olmayan örnekler verir misin? (Outputta ornekler disinda herhangi bir yazi olmasin)"

            unique_idioms = self.dataset['idiom'].unique()

            for i, data in enumerate(unique_idioms[5:6]):
                self.prompt += f'\n {i+1}. {data}'
        else:
            self.prompt = prompt

        print(self.prompt)

    def getResponse(self):
        setConfig()
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=self.prompt,
                                            temperature=0,
                                            max_tokens=1024,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0)
        return response.get('choices')[0].get('text')


class Classifier(OpenAI):
    def __init__(self):
        super().__init__()

    def setPrompt(self, prompt=None):
        if not prompt:
            self.prompt = "Merhaba senden simdi bir dilbilmci gibi davranmani istiyorum.\
                            Ben Turkceyi yeni ogreniyorum ve bazı kelimelerin birden fazla anlamda olması benim öğrenme sürecimi çok zorlaştırıyor.\
                            Bu konuda ben sana bazi cumleler ve cumle içerisinde geçen kelimeleri verecegim sen de bana bu kelimenin deyim olup olmadigini soyleyeceksin.\
                            Output formatin soyle olmalidir. {Cumle}: {Idiom veya Nonidiom}.\
                            Ornegin, Adım Atmak: 5 adım attıktan sonra sağa dön ve 20 adım daha at: Nonidiom\
                            Bir ornek daha, Adım Atmak: Petrol yasasında geri adım mı atılacak.: Idiom\
                            Asagidaki cumleleri ornekteki gibi siniflandir."

            self.dataset['prompt'] = self.dataset['idiom'] + \
                ": " + self.dataset['submission']

            for i, data in enumerate(self.dataset['prompt'].values):
                self.prompt += f'\n {i+1}. {data}'
        else:
            self.prompt = prompt
        print(self.prompt)

    def getResponse(self):
        setConfig()
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=self.prompt,
                                            temperature=0,
                                            max_tokens=1024,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0)

        return response.get('choices')[0].get('text')
