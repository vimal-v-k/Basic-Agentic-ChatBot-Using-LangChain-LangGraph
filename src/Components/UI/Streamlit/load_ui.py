from src.Components.UI.uiconfigfile import Config
import streamlit as st
import os

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_PAGE_TITLE_options(),layout="wide")
        st.header(self.config.get_PAGE_TITLE_options())

        with st.sidebar:
            llm_options = self.config.get_LLM_options()
            usecase_options = self.config.get_USECASE_options()

            self.user_controls["Selected LLM"] = st.selectbox("Selected LLM",llm_options)

            if self.user_controls["Selected LLM"] == "Groq":
                model_options = self.config.get_GROQ_MODELS_options()
                self.user_controls["Selected_Model"] = st.selectbox("Selected_Model",model_options)
        
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key to proceed, Dont have ? Please visit Groq official website.")
            
            self.user_controls["Selected Usecase"] = st.selectbox("Selected Usecase",usecase_options)

        return self.user_controls
    