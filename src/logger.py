import logging
from datetime import datetime


def generate_logger():
    # Get the current date and time, formatted as a string
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")

    # Create a filename with this timestamp
    filename = f"outcomes/logs/log_{dt_string}.log"

    # Create a logger
    logger = logging.getLogger(__name__)

    # Set the level of this logger to INFO
    logger.setLevel(logging.INFO)

    # Create a file handler for outputting log messages to a file
    handler = logging.FileHandler(filename)

    # Set the level of this handler to INFO
    handler.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter(
        '%(message)s\n')

    # Add the formatter to the handler
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger
