from flask import Blueprint, request, jsonify
from app.watson import get_access_token, analyze_text
import requests, os

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return jsonify({'message': 'Welcome to the Smart City Feedback API'})

@main.route('/analyze_feedback', methods=['POST'])
def analyze_feedback():
    data = request.get_json()
    
    #access_token = get_access_token()
    access_token= os.getenv('ACCESS_TOKEN')

    analysis = analyze_text("this product is dope and i am using it for like a month and its not working anymore", access_token)

    return jsonify(analysis)
