import streamlit as st
from src.Components.UI.Streamlit.load_ui import LoadStreamlitUI

def load_app():
    """
    This function initiate the UI
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error : Failed to load iser input from the UI")
        return
    
    user_message = st.chat_input("Enter your message : ")

    if user_message:
        pass
        # obj_llm_config = GroqLLM(user_conntrols_inputs = user_input)
        # model = obj_llm_config.get_llm_model()

        # if not model:
        #     st.error("Error : LLM model could not be initialized.")
        #     return

        # usecase = user_input.get("selected_usecase")
        # if not usecase:
        #     st.error("Error : No use case selected")
        #     return