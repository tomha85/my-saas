from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data
users = [{'username': 'demo', 'password': 'demo'}]

def validate_credentials(username, password):
    return any(user['username'] == username and user['password'] == password for user in users)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if validate_credentials(data['username'], data['password']):
        return jsonify(ok=True, token="demo"), 200
    return jsonify({'ok': False}), 401