from langchain_openai import ChatOpenAI
from config import settings
from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY',default='')
BASE_URL = config('BASE_URL',default='')

def get_openai_model(model='gpt-4.1'):
    if model == None:
        model = 'gpt-4o-mini'
    return ChatOpenAI(
    model=model,
    
    temperature=0,
    
    max_retries=2,
    
    api_key = OPENAI_API_KEY,
    
    base_url=BASE_URL,)