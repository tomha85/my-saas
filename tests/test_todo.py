import pytest
import json
from app.todo import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.data.decode() == 'Todo API is running'

def test_create_todo(client):
    response = client.post('/todos', json={'title': 'Test Todo'})
    assert response.status_code == 200
    json_data = json.loads(response.data)
    assert json_data['title'] == 'Test Todo'
    assert json_data['done'] is False

def test_list_todos(test_client):
    from tests.test_client import client
    from tests.test_client import client
    client.post('/todos', json={'title': 'Todo 1'})
    client.post('/todos', json={'title': 'Todo 2'})
    response = client.get('/todos')
    assert response.status_code == 200
    assert len(json.loads(response.data)) == 2

def test_reset_todos(client):
    from tests.test_client import client
    from tests.test_client import client
    client.post('/todos', json={'title': 'Todo 1'})
    response = client.post('/reset')
    assert response.status_code == 200
    response = client.get('/todos')
    assert response.data == b'[]'