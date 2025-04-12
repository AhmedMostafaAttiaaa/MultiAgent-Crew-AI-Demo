import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    return os.getenv("OPENAI_API_KEY")

def get_anthropic_api_key():
    load_env()
    return os.getenv("ANTHROPIC_API_KEY")

def get_mistral_api_key():
    load_env()
    return os.getenv("MISTRAL_API_KEY")
