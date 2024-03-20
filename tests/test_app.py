from typing import Any
import pytest
from fastapi.testclient import TestClient
from shorturl.app import app
from shorturl.database import Database
from unittest.mock import patch
from fakeredis import FakeRedis

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

@pytest.fixture
def DB():
    return Database(redis=FakeRedis(decode_responses=True))

@pytest.fixture(params=[
    {
        "url": "https://example.com/",
        "ex": 10
    },
    {
        "url": "example",
        "ex": "ten"
    }
])
def input(request: pytest.FixtureRequest):
    return request.param

def test_create_short_url(client: TestClient, input: Any, DB: Database):
    with patch("shorturl.app.database", DB):
        response = client.post("/api/v1/create_key", json=input)
    
    if isinstance(input["ex"], int):
        assert response.status_code == 201
        data = response.json()
        assert data["url"] == input["url"]
        assert data["ex"] == input["ex"]
        assert "key" in data
    else:
        assert response.status_code == 422
        data = response.json()
        assert len(data["detail"]) == 2
        assert data["detail"][0]["msg"] == "Input should be a valid URL, relative URL without a base"
        assert data["detail"][1]["msg"] == "Input should be a valid integer, unable to parse string as an integer"
