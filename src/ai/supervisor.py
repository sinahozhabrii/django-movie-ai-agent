from langgraph_supervisor import create_supervisor
from .llms import get_openai_model
from .agents import get_document_agent,get_movie_discovery_agent
def get_agents_supervisor(checkpointer=None,store=None):
    model = get_openai_model()
    supervisor = create_supervisor(
        model=model,
        agents=[get_document_agent(),get_movie_discovery_agent()],
        prompt=(
            "You are a supervisor managing two agents:\n"
            "- a document agent. Assign CRUD and search doucment tasks to this agent\n"
            "- a movie discovery agent that the only way ALOWED to gather info about any movie . Assign movie discovery tasks to this agent do not gather info about any movie yorself ONLY USE THIS AGENT!\n"
            "Assign work to one agent at a time, do not call agents in parallel.\n"
            "Do not do any work yourself only use agents and thier tools"
        ),
        
    ).compile(checkpointer=checkpointer,store=store)
    return supervisor