from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for request counts
request_counts = {}

@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    # Increment request count for the route
    if path not in request_counts:
        request_counts[path] = 0
    request_counts[path] += 1
    return jsonify(success=True)

@app.route('/metrics', methods=['GET'])
def metrics():
    return jsonify(routes=request_counts)