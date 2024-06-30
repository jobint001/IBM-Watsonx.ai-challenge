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
    
    access_token = get_access_token()
    #access_token= os.getenv('ACCESS_TOKEN')

    analysis = analyze_text("The new public park is fantastic! It's clean and well-maintained, and my kids love the playground. I appreciate the frequent public transport, but the buses are often overcrowded and late.The city app is very helpful for finding information, but it crashes frequently. Waste collection has improved significantly, but there are still areas with irregular schedules. Digital services are good, but internet connectivity in some areas is poor.", access_token)
    print(analysis)
    return jsonify(analysis)
