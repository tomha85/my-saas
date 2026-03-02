import pytest
import json
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert json.loads(response.data) == {'ok': True}