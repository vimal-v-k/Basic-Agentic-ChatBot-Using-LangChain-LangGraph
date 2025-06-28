import streamlit as st
import json
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "BASIC CHATBOT":
            for event in graph.stream({"message" : [("user",user_message)]}):
                # print(event.values())
                for value in event.values():
                    # print(value['message'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value['message'].content)