from flask import jsonify
from app import app

@app.route('/health', methods=['GET'])
def health():
    return jsonify(ok=True, version="0.1.0")
