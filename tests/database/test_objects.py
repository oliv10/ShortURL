from shorturl.database import URL, URLKey
from pydantic import HttpUrl

def test_url():
    url = URL(HttpUrl("https://example.com/"), 30)
    assert str(url.url) == "https://example.com/"
    assert url.ex == 30

def test_urlkey():
    urlKey = URLKey(HttpUrl("https://example.com/"), 30)
    assert str(urlKey.url) == "https://example.com/"
    assert urlKey.ex == 30
    assert urlKey.key