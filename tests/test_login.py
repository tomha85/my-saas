def test_login_invalid_credentials(client):
    response = client.post('/login', json={'username': 'wrong', 'password': 'credentials'})
    assert response.json == {'ok': False}
    assert response.status_code == 401
