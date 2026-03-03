import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_login(client):
    response = client.post('/login', json={'username': 'test', 'password': 'pass'})
    assert response.json == {'ok': True, 'token': 'demo'}
    assert response.status_code == 200


def test_login_missing_data(client):
    response = client.post('/login', json={'username': 'test'})
    assert response.json == {'ok': False}
    assert response.status_code == 400
