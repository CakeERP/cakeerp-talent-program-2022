from fastapi import FastAPI

app = FastAPI()

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