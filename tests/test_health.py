import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health(test_client):
    
    response = client.get('/health')
    assert response.json == {'ok': True}
    assert response.status_code == 200
