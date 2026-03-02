import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_uptime(client):
    response = client.get('/uptime')
    assert "uptime_seconds" in response.json
    assert response.status_code == 200
