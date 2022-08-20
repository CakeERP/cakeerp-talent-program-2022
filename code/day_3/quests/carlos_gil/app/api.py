from fastapi import FastAPI


app = FastAPI()

@app.get('/status')
async def root():
    return {"status": "it's alive"}
