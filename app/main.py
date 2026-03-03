from flask import jsonify, request
from app import app

@app.route('/health', methods=['GET'])
def health():
    return jsonify(ok=True)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get('username') == 'demo' and data.get('password') == 'pass':
        return jsonify(ok=True, token='demo')
    return jsonify(ok=False), 401
