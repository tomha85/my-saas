from flask import jsonify
from app import app

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status='ok')
