from configparser import ConfigParser

class Config:
    def __init__(self,config_file = "./src/Components/UI/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_LLM_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")

    def get_USECASE_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_GROQ_MODELS_options(self):
        return self.config["DEFAULT"].get("GROQ_MODELS").split(", ")
    
    def get_PAGE_TITLE_options(self):
        return self.config["DEFAULT"].get("PAGE_TITLE") 