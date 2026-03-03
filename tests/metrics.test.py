import requests
import pytest

BASE_URL = 'http://localhost:5000'  # Update accordingly


def test_metrics():
    # Making a sample request to increment count
    requests.post(f'{BASE_URL}/sample-route')
    response = requests.get(f'{BASE_URL}/metrics')
    assert response.status_code == 200
    data = response.json()
    assert 'routes' in data
    assert data['routes']['sample-route'] == 1  # Ensure the count is correct