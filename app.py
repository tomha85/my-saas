from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def version():
    return jsonify(version="0.1.0")