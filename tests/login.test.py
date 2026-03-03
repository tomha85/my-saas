import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Update accordingly

def test_login_valid():
    response = requests.post(f'{BASE_URL}/login', json={"username": "demo", "password": "demo"})
    assert response.status_code == 200
    data = response.json()
    assert 'token' in data


def test_login_invalid():
    response = requests.post(f'{BASE_URL}/login', json={"username": "invalid", "password": "credentials"})
    assert response.status_code == 401
    data = response.json()
    assert data['ok'] is False