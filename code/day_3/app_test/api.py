from .models import Item
from fastapi import FastAPI

app = FastAPI()


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    from pdb import set_trace; set_trace()
    return fake_items_db[skip : skip + limit]


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

