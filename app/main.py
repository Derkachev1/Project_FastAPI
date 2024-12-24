import uvicorn
from fastapi import FastAPI
from app.config import settings
from fastapi.staticfiles import StaticFiles
from app.routers import router as api_router 

app = FastAPI()

app.include_router(api_router, prefix=settings.api.prefix)

@app.get("/test")
def test():
    return {"message": "TEST"}

@app.get("/")
def home():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.run.host, port=settings.run.port, reload=True)
