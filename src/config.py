import openai
import yaml


def setConfig():
    with open("auth/auth.yaml", "r") as f:
        config = yaml.safe_load(f)

    openai.api_key = config['OPENAI']['SECRET']
