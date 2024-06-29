import requests
from flask import  request, current_app
from ibm_cloud_sdk_core import IAMTokenManager
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BearerTokenAuthenticator
import os, getpass


def get_access_token():
    api_key = current_app.config['API_KEY']
   
    access_token = IAMTokenManager(
    api_key ,
    url = "https://iam.cloud.ibm.com/identity/token"
).get_token()

    return access_token

def analyze_text(text, access_token):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/your-instance-id/v1/analyze"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "version": "2021-08-01"
    }
    data = {
        "text": text,
        "features": {
            "sentiment": {},
            "categories": {},
            "concepts": {},
            "entities": {},
            "keywords": {},
            "metadata": {},
            "relations": {},
            "semantic_roles": {}
        }
    }
    
    response = requests.post(url, headers=headers, params=params, json=data)
    response.raise_for_status()
    
    return response.json()
