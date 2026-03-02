from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/health', methods=['GET'])\ndef health():\n    return {'status': 'ok'}\n
