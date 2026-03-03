# Existing app code

from flask import Flask, jsonify
import time

app = Flask(__name__)

# Global variable to store uptime
start_time = time.time()

@app.route('/uptime', methods=['GET'])
def uptime():
    uptime_seconds = int(time.time() - start_time)
    return jsonify(uptime_seconds=uptime_seconds)