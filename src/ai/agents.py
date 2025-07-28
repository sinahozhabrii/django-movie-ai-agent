from langgraph.prebuilt import create_react_agent
from .llms import get_openai_model
from .tools import tools_list
def get_document_agent():
    model = get_openai_model()
    agent = create_react_agent(
        model=model,
        tools=tools_list,
        prompt='you are helpfull assistante for managing documents within this app'
    )
    
    return agent