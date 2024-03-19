from fastapi import FastAPI
from fastapi.responses import RedirectResponse, Response
from shorturl.database import Database, URL, URLKey
from shorturl.settings import Settings

settings = Settings()
database: Database = Database(host=settings.DBHOST, port=settings.DBPORT, password=settings.DBPASS)
app: FastAPI = FastAPI()

# @app.get("/")
# def get_index():
#     # HTMX Front End App to Do the Things
#     return ["one", 2, "three"]

@app.get("/{key}", response_class=RedirectResponse)
async def redirect_url(key: str) -> RedirectResponse:
    url = database.get_url(key=key)
    if url:
        return RedirectResponse(url)
    else:
        return Response(None, 404)

@app.post("/api/v1/create_key", status_code=201)
async def create_key(url: URL) -> URLKey:
    return database.create_url(url=url.url, ex=url.ex)
