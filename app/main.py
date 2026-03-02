from flask import jsonify
from app import app
from time import time

# Store the start time of the application
start_time = time()

@app.route('/uptime', methods=['GET'])
def uptime():
    uptime_seconds = int(time() - start_time)
    return jsonify(uptime_seconds=uptime_seconds)
