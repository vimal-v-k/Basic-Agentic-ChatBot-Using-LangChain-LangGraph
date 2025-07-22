# from langchain_community.tools.tavily_search import TavilySearchResults
# from langgraph.prebuilt import ToolNode
# import os
# os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# def get_tools():
#     tools = [TavilySearchResults(max_results=3)]
#     return tools

# def create_tool_node(tools):
#     return ToolNode(tools=tools)