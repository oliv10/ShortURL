from .objects import URLKey
from redis import Redis
from pydantic import HttpUrl

class database:

    def __init__(self, db:Redis = Redis(host='redis', port=6379, decode_responses=True)):
        self.db = db
        self.db.set("None", "/")

    def get_url(self, key: str) -> str:
        return self.db.get(key)

    def create_url(self, url: HttpUrl, ex: int) -> URLKey:
        item = URLKey(ex=ex, url=url)
        while self.get_url(item.key) != None:
            return self.create_url(url, ex)
        self.db.set(item.key, str(item.url), ex=ex)
        return item
