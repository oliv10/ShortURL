from .objects import URLKey
from redis import Redis
from pydantic import HttpUrl

class Database:

    def __init__(self, host: str = "redis", port: int = 6379, table: int = 0, username: str | None = None, password: str | None = None, redis: Redis = None):
        if redis:
            self.db = redis
        else:
            self.db = Redis(host=host, port=port, db=table, username=username, password=password, decode_responses=True)
        self.db.set("None", "/")

    def get_url(self, key: str) -> str | None:
        return self.db.get(key)

    def create_url(self, url: HttpUrl, ex: int) -> URLKey:
        item = URLKey(ex=ex, url=url)
        while self.get_url(item.key) != None:
            return self.create_url(url, ex)
        self.db.set(item.key, str(item.url), ex=ex)
        return item
