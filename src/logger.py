import logging
from datetime import datetime


def generate_logger():
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    filename = f"outcomes/logs/log_{dt_string}.log"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(filename)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(message)s\n")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
