import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Update accordingly

def test_create_todo():
    response = requests.post(f'{BASE_URL}/todos', json={"task": "Test Todo"})
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data
    assert data['task'] == "Test Todo"


def test_get_todos():
    response = requests.get(f'{BASE_URL}/todos')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)