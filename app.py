from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = [{'username': 'demo', 'password': 'demo'}]

def validate_credentials(username, password):
    return any(user for user in users if user['username'] == username and user['password'] == password)  

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if validate_credentials(data['username'], data['password']):
        return jsonify(token="your_generated_token_here"), 200
    return jsonify({'ok': False}), 401