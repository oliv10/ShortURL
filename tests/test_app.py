import pytest
from fastapi.testclient import TestClient
from shorturl.app import app

@pytest.fixture
def client():
    return TestClient(app)

# def test_get_index(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == ["one", 2, "three"]
