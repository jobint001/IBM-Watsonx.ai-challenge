import requests
from flask import  request, current_app
from ibm_cloud_sdk_core import IAMTokenManager
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BearerTokenAuthenticator
import os, getpass

parameters = {
    "decoding_method": "greedy",""
    "max_new_tokens": 300,
    "min_new_tokens": 50,
    "repetition_penalty": 1
}

model_id = "ibm/granite-13b-chat-v2"

summarize_instruction = """

You are Granite Chat, an AI language model developed by IBM. You are a cautious assistant. Your task is to create a brief, accurate summary of citizen feedback on public infrastructure projects and services to assist city planners in making informed decisions. Ensure the summary captures the key themes and sentiments expressed in the feedback and organize the output into sections for features citizens liked, features citizens did not like, and the best infrastructure project to be considered next based on the feedback. Format the summary exactly as shown in the examples.

[Document]
{feedback}
[End]


<|assistant|>
"""

class Prompt:
    def __init__(self, access_token, project_id):
        self.access_token = access_token
        self.project_id = project_id

    def generate(self, input, model_id, parameters):
        wml_url = "https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text?version=2023-05-28"
        Headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = { 
            "model_id": model_id,
            "input": input,
            "parameters": parameters,
            "project_id": self.project_id
        }
        response = requests.post(wml_url, json=data, headers=Headers)
        if response.status_code == 200:
            return response.json()["results"][0]["generated_text"]
        else:
            return response.text

def get_access_token():
    api_key = current_app.config['API_KEY']
   
    access_token = IAMTokenManager(
    api_key ,
    url = "https://iam.cloud.ibm.com/identity/token"
).get_token()
    
    return access_token

def  analyze_text(text, access_token):
    project_id = current_app.config['PROJECT_ID']
    prompt = Prompt(access_token, project_id)
    results = []
    prompt_instruction = summarize_instruction.format(feedback=text)
    results.append(prompt.generate(prompt_instruction, model_id, parameters).replace("\n",""))
   
    return results
