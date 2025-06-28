from langgraph.graph import StateGraph,START,END
from src.Components.States.state import State
from src.Components.Nodes.node_builder import BasicChatBotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        self.chatbot = BasicChatBotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.chatbot.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase : str):
        if usecase == "BASIC CHATBOT":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()