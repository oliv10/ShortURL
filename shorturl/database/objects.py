import string, random
from dataclasses import dataclass, field
from pydantic import HttpUrl, Field

KEYLEN = 8

@dataclass
class URL:
    url: HttpUrl
    ex: int = Field(120, gt=0)

@dataclass
class URLKey(URL):
    key: str = Field(default_factory=lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=KEYLEN)), min_length=KEYLEN, max_length=KEYLEN)
