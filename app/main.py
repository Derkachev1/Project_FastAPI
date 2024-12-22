from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


app = FastAPI()


@app.get("/test")
def test():
    return "TEST"

@app.get("/")
def home():
    return "Hello World"
