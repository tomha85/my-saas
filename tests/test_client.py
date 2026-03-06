import pytest

@pytest.fixture
def client():
    from app import app
    test_client = app.test_client()
    yield test_client
