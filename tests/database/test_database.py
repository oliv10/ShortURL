import pytest
from fakeredis import FakeRedis
from shorturl.database import Database, URLKey
import time

@pytest.fixture
def DB():
    return Database(redis=FakeRedis(decode_responses=True))

def test_create_url(DB):
    url = "https://example.com"
    item = DB.create_url(url, 1)
    assert isinstance(item, URLKey)
    assert item.ex == 1
    assert item.url == url

def test_get_url(DB):
    url = "https://example.com"
    item = DB.create_url(url, 1)
    assert DB.get_url(item.key) == url

def test_expired_url(DB):
    url = "https://example.com"
    item = DB.create_url(url, 1)
    time.sleep(1)
    assert DB.get_url(item.key) is None

def test_nonexistent_key(DB):
    assert DB.get_url("nonexistent_key") is None

def test_none_key(DB):
    assert DB.get_url("None") == "/"
