from models import *


def main():
    idiom_generator = Generator()
    idiom_classifier = Classifier()

    idiom_generator.setPrompt()
    response = idiom_generator.getResponse()

    prompt = "Aşağıdaki verilen örneklerden hangileri doğru olarak siniflandirilmistir?\n" + response
    idiom_classifier.setPrompt(prompt)
    response = idiom_classifier.getResponse()

    print(response)


if __name__ == '__main__':
    main()
