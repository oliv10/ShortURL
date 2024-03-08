import pytest
from fakeredis import FakeRedis
from shorturl.database import Database
import time

@pytest.fixture
def DB():
    return Database(FakeRedis(decode_responses=True))

def test_create_url(DB):
    item = DB.create_url("https://example.com", 1)
    assert item.ex == 1
    assert item.url == "https://example.com"

def test_get_url(DB):
    item = DB.create_url("https://example.com", 1)
    assert DB.get_url(item.key) == "https://example.com"
    time.sleep(2)
    assert DB.get_url("failed") == None
    assert DB.get_url("None") == "/"
    assert DB.get_url(item.key) == None
