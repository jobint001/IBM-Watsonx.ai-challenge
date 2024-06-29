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

You are a retail expert. You will be given a list of product reviews. Your task is to generate a  summary, only from given product reviews from an ecommerce site to give feedback to another customer. When generating responses, prioritize correctness, i.e., ensure that your response is correct given the context and user query, and that it is grounded in the context.

[Document]
{reviews}
[End]


<|assistant|>
Features customers liked about the product: 1. The machines are beautiful, with a color option of Champagne. 2. The washer does a fantastic job and has many options for washing cycles. 3. The washer and dryer combination is esthetically pleasing. 4. The features of the dryer are great benefits, reliable, and have useful functions like steam. 5. The delivery process was easy, and the machine was easy to install. 6. The capacity of the machine is pretty big. 7. The steam function is a great feature. 8. The washer has the option to choose your wash time and pick how many spin cycles you need. 9. The new model seems even more efficient than the old one. 10. The new model has new features that the customer enjoys. Features customers did not like about the product or had issues with: 1. No specific issues or complaints were mentioned about the product.

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
    print(access_token)

    return access_token

def analyze_text(text, access_token):
    project_id = current_app.config['PROJECT_ID']
    prompt = Prompt(access_token, project_id)
    results = []
    prompt_instruction = summarize_instruction.format(reviews=text)
    results.append(prompt.generate(prompt_instruction, model_id, parameters).replace("\n",""))
   
    
    
    
    return results
