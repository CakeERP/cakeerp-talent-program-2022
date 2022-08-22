from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/status/") #Equivalente ao que foi visto no desenvolvimento android esse é o ponto final da rota, onde tu
async def root():
    return{"status" : "it's alive"}

