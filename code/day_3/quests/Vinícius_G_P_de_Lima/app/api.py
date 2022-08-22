from fastapi import FastAPI


app=FastAPI()

fake_items_db=[{"item_name":"foo"},{"item_name":"bar"},{"item_name":"baz"}]


@app.get("/")

async def root():
    return {"message":"teste"}

@app.get("/items/")
async def read_items(skip:int=0, limit:int=10):
    return fake_items_db[skip: skip + limit]


@app.post("/items/")
async def create_item(item: Item):
    return item



@app.get("/items/{item_id}")

async def read_item(item_id:int):
    return {"item_id":item_id}
