@app.route('/me', methods=['POST'])
def me():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        return jsonify(message="Authorized access"), 200
    return jsonify(error="Unauthorized"), 401
