from langgraph.prebuilt import create_react_agent
from .llms import get_openai_model
from .tools import document_tools_list,movie_discovery_tools_list,personal_info_tools_list
from langmem.short_term import SummarizationNode, RunningSummary
from .llms import get_openai_model
from langgraph.prebuilt.chat_agent_executor import AgentState
from typing import Any
from langchain_core.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langchain_core.messages.utils import (
    trim_messages, 
    count_tokens_approximately
)
model = get_openai_model()
sum_model = model.bind(max_token=128)


def get_document_agent(checkpointer=None):
    model = get_openai_model()
    agent = create_react_agent(
        model=model,
        tools=document_tools_list,
        prompt='you are helpfull assistante for managing documents within this app',
        checkpointer=checkpointer,
        name='document-assistant',
    )
    
    return agent


def get_movie_discovery_agent(checkpointer=None):
    model = get_openai_model() 
    agent = create_react_agent(
        model=model.bind(max_token=256),
        tools=movie_discovery_tools_list,
        prompt='you are helpfull assistante for discovring info about movies',
        checkpointer=checkpointer,
        name='movie-assistant',
    )
    
    return agent

def get_personal_info_agent(checkpointer=None):
    model = get_openai_model()
    agent = create_react_agent(
        model=model.bind(max_token=256),
        tools=personal_info_tools_list,
        prompt='you are helpfull assistante for managing and saving user personal info within this app',
        checkpointer=checkpointer,
        name='personal-inof-saver-assistant',
    )
    
    return agent