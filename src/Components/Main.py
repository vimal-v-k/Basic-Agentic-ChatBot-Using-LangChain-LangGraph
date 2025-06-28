import streamlit as st
from src.Components.UI.Streamlit.load_ui import LoadStreamlitUI
from src.Components.LLM.groq_llm import GroqLLM
from src.Components.Graph.graph_builder import GraphBuilder
from src.Components.UI.Streamlit.display_result import DisplayResultStreamlit

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
        try:
            obj_llm_config = GroqLLM(user_controls_input = user_input)
            model = obj_llm_config.get_llm_models()

            if not model:
                st.error("Error : LLM model could not be initialized.")
                return

            usecase = user_input.get("Selected Usecase")
            if not usecase:
                st.error("Error : No use case selected")
                return
            
            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase=usecase,graph=graph,user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error : Graph setup failed {e}")
                return
        except Exception as e:
            st.error(f"Error : Graph setup failed {e}")
            return