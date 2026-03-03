import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Update accordingly

def test_health():
    response = requests.get(f'{BASE_URL}/health')
    assert response.status_code == 200
    data = response.json()
    assert data['ok'] is True
    assert data['version'] == "0.1.0"