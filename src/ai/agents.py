from langgraph.prebuilt import create_react_agent
from .llms import get_openai_model
from .tools import document_tools_list,movie_discovery_tools_list
def get_document_agent(checkpointer=None):
    model = get_openai_model()
    agent = create_react_agent(
        model=model,
        tools=document_tools_list,
        prompt='you are helpfull assistante for managing documents within this app',
        checkpointer=checkpointer
        
    )
    
    return agent


def get_movie_discovery_agent(checkpointer=None):
    model = get_openai_model()
    agent = create_react_agent(
        model=model,
        tools=movie_discovery_tools_list,
        prompt='you are helpfull assistante for discovring info about movies',
        checkpointer=checkpointer,
        
    )
    
    return agent