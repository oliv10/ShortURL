import string, random
from dataclasses import dataclass, field
from pydantic import HttpUrl, Field
from shorturl.settings import Settings

settings = Settings()

@dataclass
class URL:
    url: HttpUrl
    ex: int = Field(120, gt=0)

@dataclass
class URLKey(URL):
    key: str = field(default_factory=lambda: ''.join(random.choices(string.ascii_letters+string.digits, k=settings.KEYLEN)), metadata={"min_length": settings.KEYLEN, "max_length": settings.KEYLEN})
