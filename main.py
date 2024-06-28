from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers.router import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def index():
    return RedirectResponse(url="/docs")
