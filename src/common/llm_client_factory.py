import dspy

# OpenAI
from openai import OpenAI
import httpx

##################################################
# Cert Issues

class LlmClientFactory:
    
    def __init__(self, mySettings):   
        self.mySettings = mySettings
        self.defaulDatabricksModel = 'databricks/databricks-meta-llama-3-3-70b-instruct'
        
    def get_dspy_lm_chat_connecting_to_internal_databricks(self) -> dspy.LM:
        client = dspy.LM(
            self.defaulDatabricksModel, 
            model_type='chat', 
            cache=False, 
            api_key = self.mySettings.DATABRICKS_TOKEN, 
            api_base = f'https://{self.mySettings.DATABRICKS_ACCOUNT}.cloud.databricks.com/serving-endpoints'
        )
        
        dspy.configure(lm=client)
        return client
    
    def get_dspy_lm_chat_connecting_to_internal_databricks_model(self, model) -> dspy.LM:
        client = dspy.LM(
            model, 
            model_type='chat', 
            cache=False, 
            api_key = self.mySettings.DATABRICKS_TOKEN, 
            api_base = f'https://{self.mySettings.DATABRICKS_ACCOUNT}.cloud.databricks.com/serving-endpoints'
        )
        
        dspy.configure(lm=client)
        return client
        
    def get_openai_connecting_to_chatgpt(self):
        CA_FILE = self.mySettings.ZA_CERT_PATH 

        http_client = httpx.Client(
            verify=CA_FILE,   # No proxy
            timeout=60.0
        )

        client = OpenAI(
            http_client=http_client, 
            api_key=self.mySettings.OPENAI_API_KEY)
        
        print('THIS WILL SEND DATA OUT OF THE NETWORK, USE WITH CAUTION')
        return client
    


        
