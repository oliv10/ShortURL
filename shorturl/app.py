from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from shorturl.database import Database, URL, URLKey

app: FastAPI = FastAPI()
database: Database = Database()

# @app.get("/")
# def get_index():
#     # HTMX Front End App to Do the Things
#     return ["one", 2, "three"]

@app.get("/{key}", response_class=RedirectResponse)
async def redirect_url(key: str) -> RedirectResponse:
    return RedirectResponse(database.get_url(key=key))

@app.post("/")
async def get_short_url(url: URL) -> URLKey:
    return database.create_url(url=url.url, ex=url.ex)
