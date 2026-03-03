from flask import jsonify, request
from app import app

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == "demo" and password == "pass":
        return jsonify(ok=True, token="demo")
    return jsonify(ok=False), 401

@app.route('/health', methods=['GET'])
def health():
    return jsonify(ok=True, version="0.1.0")
