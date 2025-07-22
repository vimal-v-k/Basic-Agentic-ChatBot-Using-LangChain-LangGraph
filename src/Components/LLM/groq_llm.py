import os
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')


class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input
    
    def get_llm_models(self):
        try:
            selected_groq_model = self.user_controls_input["Selected_Model"]

            llm = ChatGroq(api_key=api_key,model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error occured with exception : {e}")
        return llm