import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Adjust accordingly

def test_version():
    response = requests.get(f'{BASE_URL}/version')
    assert response.status_code == 200
    data = response.json()
    assert data['version'] == "0.1.0"