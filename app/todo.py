from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
id_counter = 1

@app.route('/')
def hello():
    return 'Todo API is running'

@app.route('/todos', methods=['POST'])
def create_todo():
    global id_counter
    data = request.json
    todo = {'id': id_counter, 'title': data['title'], 'done': False}
    todos.append(todo)
    id_counter += 1
    return jsonify(todo)

@app.route('/todos', methods=['GET'])
def list_todos():
    return jsonify(todos)

@app.route('/reset', methods=['POST'])
def reset_todos():
    global todos, id_counter
    todos = []
    id_counter = 1
    return jsonify({'message': 'Todos cleared'})

if __name__ == '__main__':
    app.run(debug=True)