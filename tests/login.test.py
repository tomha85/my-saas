import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Update accordingly

def test_login():
    response = requests.post(f'{BASE_URL}/login', json={"username": "test", "password": "test"})
    assert response.status_code == 200
    data = response.json()
    assert 'token' in data
    assert isinstance(data['token'], str)

def test_version():
    response = requests.get(f'{BASE_URL}/version')
    assert response.status_code == 200
    data = response.json()
    assert 'version' in data
    assert data['version'] == "1.0.0"