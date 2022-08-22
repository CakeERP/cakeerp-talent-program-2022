from fastapi import FastAPI, Depends, HTTPException
from typing import List
from schemas import SchemaItem, SchemaItemCreate
from sqlalchemy.orm import Session
from database import get_db, engine
from crud import get_items, get_item, create_item
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/status")
def status():
    return {"message":"ok"}

@app.get("/movies", response_model = List[SchemaItem]) #Definimos que esse endpoint vai devolver no formato que eu defini no schema item
def read_items(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items

@app.post("/movies", response_model=SchemaItem)
def post_item(item: SchemaItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)