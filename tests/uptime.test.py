import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Update accordingly

def test_uptime():
    response = requests.get(f'{BASE_URL}/uptime')
    assert response.status_code == 200
    data = response.json()
    assert 'uptime_seconds' in data
    assert isinstance(data['uptime_seconds'], int)