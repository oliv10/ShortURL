from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from shorturl.database import URL, Database, objects

app = FastAPI()
DB = Database()

# @app.get("/")
# def get_index():
#     # HTMX Front End App to Do the Things
#     return ["one", 2, "three"]

@app.get("/{key}", response_class=RedirectResponse)
def redirect_url(key: str) -> RedirectResponse:
    return DB.get_url(key=key)

@app.post("/")
def get_short_url(url: URL) -> objects.URLKey:
    return DB.create_url(url=url.url, ex=url.ex)
