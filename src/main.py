from models import *
from tqdm import tqdm
from logger import generate_logger


def main():
    idiom_generator = Generator()
    idiom_classifier = Classifier()
    logger = generate_logger()

    for i in tqdm(range(5)):
        logger.info("-" * 35 + f"{i*3}:{i*3+3}" + "-" * 35)
        idiom_generator.setPrompt(st_idx=i * 3, end_idx=i * 3 + 3)
        response = idiom_generator.getResponse()
        logger.info(response)

        idiom_classifier.setPrompt(response)
        response = idiom_classifier.getResponse()
        logger.info(response)


if __name__ == "__main__":
    main()
