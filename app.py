from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for todos
todos = []

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = {'id': len(todos) + 1, 'task': data['task']}
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)