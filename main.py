import pandas as pd
import openai
import yaml

with open("auth.yaml", "r") as f:
    config = yaml.safe_load(f)

openai.api_key = config['OPENAI']['SECRET']

content = "\
          Merhaba senden simdi bir dilbilmci gibi davranmani istiyorum.\
          Ben Turkceyi yeni ogreniyorum ve bazı kelimelerin birden fazla anlamda olması benim öğrenme sürecimi çok zorlaştırıyor.\
          Bu konuda ben sana bazi cumleler ve cumle içerisinde geçen kelimeleri verecegim sen de bana bu kelimenin deyim olup olmadigini soyleyeceksin.\
          Output formatin soyle olmalidir. {Cumle}: {Idiom veya Nonidiom}.\
          Ornegin, Adım Atmak: 5 adım attıktan sonra sağa dön ve 20 adım daha at: Nonidiom\
          Bir ornek daha, Adım Atmak: Petrol yasasında geri adım mı atılacak.: Idiom\
          Asagidaki cumleleri ornekteki gibi siniflandir.\
          "

df = pd.read_excel("./dataset_tr.xlsx").iloc[50:60, :]
df['prompt'] = df['idiom'] + ": " + df['submission']

for i, data in enumerate(df['prompt'].values):
    content += f'\n {i+1}. {data}'

print(content)
response = openai.Completion.create(model="text-davinci-003",
                                    prompt=content,
                                    temperature=0,
                                    max_tokens=1024,
                                    top_p=1,
                                    frequency_penalty=0,
                                    presence_penalty=0)

choices = response.get('choices')[0]  # type: ignore
text = choices.get('text')
print(text)
