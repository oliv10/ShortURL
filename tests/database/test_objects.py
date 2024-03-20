import pytest
from shorturl.database import URL, URLKey
from shorturl.settings import Settings
from pydantic import HttpUrl

settings = Settings()

def valid_url():
    return HttpUrl("https://example.com/")

@pytest.fixture
def url():
    return URL(valid_url(), 30)

@pytest.fixture
def url_key():
    return URLKey(valid_url(), 30)

def test_url(url):
    assert str(url.url) == "https://example.com/"
    assert url.ex == 30

def test_urlkey(url_key):
    assert str(url_key.url) == "https://example.com/"
    assert url_key.ex == 30
    assert url_key.key

def test_urlkey_key_length(url_key):
    assert len(url_key.key) == settings.KEYLEN

def test_urlkey_key_uniqueness():
    keys = set()
    for _ in range(100):
        url_key = URLKey(valid_url(), 30)
        keys.add(url_key.key)
    assert len(keys) == 100
