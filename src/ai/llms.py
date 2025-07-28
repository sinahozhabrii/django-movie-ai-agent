from langchain_openai import ChatOpenAI
from config import settings
def get_openai_model(model='gpt-4o-mini-tts'):
    if model == None:
        model = 'gpt-4o-mini'
    return ChatOpenAI(
    model=model,
    temperature=0,
    max_retries=2,
    api_key = settings.OPENAI_API_KEY )