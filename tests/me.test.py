import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Update accordingly

def test_get_me():
    response = requests.get(f'{BASE_URL}/me', headers={"Authorization": "Bearer demo"})
    assert response.status_code == 200
    data = response.json()
    assert data['username'] == "demo"


def test_get_me_unauthorized():
    response = requests.get(f'{BASE_URL}/me')
    assert response.status_code == 401
    data = response.json()
    assert 'error' in data
    assert data['error'] == "Unauthorized"