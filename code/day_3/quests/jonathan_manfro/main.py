from ast import main
from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/status/")

async def root():
    return {"status": "it's alive"}