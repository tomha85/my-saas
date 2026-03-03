from tests.test_client import client

def test_login_invalid_credentials(test_client):
    
    response = client.post('/login', json={'username': 'wrong', 'password': 'credentials'})
    assert response.json == {'ok': False}
    assert response.status_code == 401
