from flask import Blueprint, request, jsonify
from app.watson import get_access_token, analyze_text

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({'message': 'Welcome to the Smart City Feedback API'})

@main.route('/analyze_feedback', methods=['POST'])
def analyze_feedback():
    data = request.get_json()
    

    

    access_token = get_access_token()
    print(access_token)
    analysis = analyze_text("text", access_token)

    return jsonify(analysis)
