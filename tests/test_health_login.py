import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get('/health')
    assert response.json == {'ok': True}
    assert response.status_code == 200


def test_login_success(client):
    from tests.test_client import client
    from tests.test_client import client
    response = client.post('/login', json={'username': 'demo', 'password': 'pass'})
    assert response.json == {'ok': True, 'token': 'demo'}
    assert response.status_code == 200


def test_login_failure(client):
    from tests.test_client import client
    from tests.test_client import client
    response = client.post('/login', json={'username': 'wrong', 'password': 'credentials'})
    assert response.json == {'ok': False}
    assert response.status_code == 401
