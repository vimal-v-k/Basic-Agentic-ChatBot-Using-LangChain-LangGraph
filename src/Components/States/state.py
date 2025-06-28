from typing import Annotated
from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represents the structure of the input of the nodes
    """
    message : Annotated[List,add_messages]