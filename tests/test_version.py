import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_version(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert response.json == {'version': '1.0.0'}