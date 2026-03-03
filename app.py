from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Simulate token creation upon successful login
    return jsonify(token="your_generated_token_here"), 200

@app.route('/version', methods=['GET'])
def version():
    return jsonify(version="1.0.0")