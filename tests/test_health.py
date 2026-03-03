def test_health(client):
    response = client.get('/health')
    assert response.json == {'ok': True, 'version': '0.1.0'}
    assert response.status_code == 200
