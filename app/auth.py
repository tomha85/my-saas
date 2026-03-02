from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'ok': True})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Mock authentication check
    if username == 'demo' and password == 'demo':
        return jsonify({'ok': True, 'token': 'demo'})
    return jsonify({'ok': False}), 401

if __name__ == '__main__':
    app.run(debug=True)