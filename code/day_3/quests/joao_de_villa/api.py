from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    age: int
    male: bool


@app.get("/{item_id}")
async def root(item_id: int):
    return{
        "id": item_id
    }

@app.get("/")
async def root():
    return{
        "message": "Hello World",
        "contagem": 24,
        "lista": [3,4,5,6,"teste", False],
    }

@app.post("/items")
async def create_item(item: Item):
    return{
        item
    }

@app.get("/status")
async def root():
    return{
        "status": "it's alive",
    }