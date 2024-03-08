import string, random
from dataclasses import dataclass, field
from pydantic import HttpUrl, Field

@dataclass
class URL:
    url: HttpUrl
    ex: int = Field(120, gt=0)

@dataclass
class URLKey(URL):
    key: str = field(default_factory=lambda: ''.join(random.choices(string.ascii_letters, k=8)))
