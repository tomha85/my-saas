from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def get_version():
    return jsonify(version='1.0.0')

if __name__ == '__main__':
    app.run()