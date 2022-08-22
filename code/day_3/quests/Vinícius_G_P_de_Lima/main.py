from fastapi import FastAPI


app=FastAPI()

@app.get("/items/")

async def root():
    return {"status":"it's alive"}






