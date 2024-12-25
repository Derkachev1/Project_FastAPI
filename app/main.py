import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

from config import settings

from __init__ import router as api_router


app = FastAPI()
app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


@app.get("/test")
def test():
    return "TEST"

@app.get("/")
def home():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
