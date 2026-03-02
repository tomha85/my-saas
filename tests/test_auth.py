import pytest
import json
from app.auth import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get('/health')
    assert response.get_json() == {'ok': True}


def test_login_success(client):
    response = client.post('/login', json={'username': 'demo', 'password': 'demo'})
    assert response.status_code == 200
    assert response.get_json() == {'ok': True, 'token': 'demo'}


def test_login_failure(client):
    response = client.post('/login', json={'username': 'wrong', 'password': 'wrong'})
    assert response.status_code == 401
    assert response.get_json() == {'ok': False}


def test_signup_success(client):
    response = client.post('/signup', json={'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200
    assert response.get_json() == {'ok': True}


def test_signup_failure(client):
    response = client.post('/signup', json={'email': '', 'password': 'password'})
    assert response.status_code == 400
    assert response.get_json() == {'ok': False}