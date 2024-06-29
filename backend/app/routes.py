from flask import Blueprint, request, jsonify
from app.watson import get_access_token, analyze_text
import requests

main = Blueprint('main', __name__)
parameters = {
    "decoding_method": "greedy",""
    "max_new_tokens": 300,
    "min_new_tokens": 50,
    "repetition_penalty": 1
}

model_id = "ibm/granite-13b-chat-v2"

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

@main.route('/')
def index():
    return jsonify({'message': 'Welcome to the Smart City Feedback API'})

@main.route('/analyze_feedback', methods=['POST'])
def analyze_feedback():
    data = request.get_json()
    
    access_token = get_access_token()
    analysis = analyze_text("text", access_token)

    return jsonify(analysis)
