def test_me_authorized(client):
    response = client.post('/me', headers={'Authorization': 'Bearer valid_token'})
    assert response.status_code == 200
    assert response.json == {'message': 'Authorized access'}


def test_me_unauthorized(client):
    response = client.post('/me')
    assert response.status_code == 401
    assert response.json == {'error': 'Unauthorized'}
