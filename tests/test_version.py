def test_version(client):
    response = client.get('/version')
    assert response.json == {'version': '0.0.1'}
    assert response.status_code == 200
