from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data for users
users = [{'username': 'demo', 'password': 'demo'}]

@app.route('/me', methods=['GET'])
def get_me():
    auth_header = request.headers.get('Authorization')
    if auth_header != 'Bearer demo':
        return jsonify({'error': 'Unauthorized'}), 401
    return jsonify({'username': 'demo'})