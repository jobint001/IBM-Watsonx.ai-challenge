from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Configuring the MongoDB URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/tester"
mongo = PyMongo(app)
db = mongo.db.users

@app.route('/')
def home():
    return "HomeStuff"

@app.route("/users", methods=["POST"])
def create_user():
    user_data = {
        'name': request.json.get('name'),
        'age': request.json.get('age'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }
    result = db.insert_one(user_data)
    return jsonify({'id': str(result.inserted_id), 'msg': "USER ADDED"})

@app.route("/users", methods=["GET"])
def get_users():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'age': doc['age'],
            'email': doc['email'],
            'password': doc['password']
        })
    return jsonify(users)

@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = db.find_one({'_id' : ObjectId(id)})
    return jsonify(
        {
            '_id': str(user['_id']),
            'name': user['name'],
            'age': user['age'],
            'email': user['email'],
            'password': user['password']
        }
    )

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': "User Deleted Successfully"})

@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json.get('name'),
        'age': request.json.get('age'),
        'email': request.json.get('email'),
        'password': request.json.get('password')
    }})
    return jsonify({'msg': "User Updated Successfully"})

if __name__ == '__main__':
    app.run(debug=True)
