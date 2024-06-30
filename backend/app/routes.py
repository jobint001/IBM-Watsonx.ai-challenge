from flask import Blueprint, request, jsonify, current_app
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from app.watson import get_access_token, analyze_text

main = Blueprint('main', __name__)

@main.before_app_request
def setup_db():
    current_app.config["MONGO_URI"] = "mongodb://localhost:27017/tester"
    main.mongo = PyMongo(current_app)
    main.db = main.mongo.db.users

@main.route('/')
def home():
    return "HomeStuff"

@main.route("/users", methods=["POST"])
def create_user():
    user_data = {
        'name': request.json.get('name'),
        'age': request.json.get('age'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    result = main.db.insert_one(user_data)
    return jsonify({'id': str(result.inserted_id), 'msg': "USER ADDED"})

@main.route("/users", methods=["GET"])
def get_users():
    users = []
    for doc in main.db.find():
        users.append({
            '_id': str(doc['_id']),
            'name': doc['name'],
            'age': doc['age'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)

@main.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = main.db.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify({
            '_id': str(user['_id']),
            'name': user['name'],
            'age': user['age'],
            'email': user['email'],
            'password': user['password']
        })
    else:
        return jsonify({'error': 'User not found'}), 404

@main.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = main.db.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return jsonify({'msg': "User Deleted Successfully"})
    else:
        return jsonify({'error': 'User not found'}), 404

@main.route("/users/<id>", methods=["PUT"])
def update_user(id):
    result = main.db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json.get('name'),
        'age': request.json.get('age'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }})
    if result.matched_count:
        return jsonify({'msg': "User Updated Successfully"})
    else:
        return jsonify({'error': 'User not found'}), 404

@main.route('/analyze_feedback', methods=['POST'])
def analyze_feedback():
    data = request.get_json()
    access_token = get_access_token()
    print(access_token)
    analysis = analyze_text("text", access_token)
    return jsonify(analysis)
