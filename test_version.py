import pytest
import json
from api.version import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_version(client):
    response = client.get('/version')
    assert response.status_code == 200
    assert json.loads(response.data) == {"version": "0.1.0"}