import pytest, json
from fastapi.testclient import TestClient
from shorturl.app import app

@pytest.fixture
def client():
    return TestClient(app)

# def test_get_index(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == ["one", 2, "three"]

def test_get_short_url(client: TestClient):
    good_body = """
            {
            "url": "https://example.com/",
            "ex": 10
            }
            """
    response = client.post("/api/v1/create_key", data=good_body)
    dict_response = json.loads(response.content)
    assert dict_response["url"] == "https://example.com/"
    assert dict_response["ex"] == 10
    assert response.status_code == 201

    bad_body = """
            {
            "url": "example",
            "ex": "ten"
            }
            """
    response = client.post("/api/v1/create_key", data=bad_body)
    dict_response = json.loads(response.content)
    assert dict_response["detail"][0]["ctx"]["error"] == "relative URL without a base"
    assert dict_response["detail"][1]["msg"] == "Input should be a valid integer, unable to parse string as an integer"
    assert response.status_code == 422

# def test_redirect_url(client):
#     good_body = """
#             {
#             "url": "https://example.com/",
#             "ex": 100
#             }
#             """
#     response = client.post("/", data=good_body)
#     dict_response = json.loads(response.content)
#     key = f"/{dict_response["key"]}"
#     # assert key == f"{key}"
#     response = client.get(key, follow_redirects=True)
#     assert response.content == ""
#     assert response.status_code == 307
