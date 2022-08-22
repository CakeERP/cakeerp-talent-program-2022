from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

from schema import schema_Item, schema_Item_create
from database import get_db, engine
from crud import create_item, get_item, get_items
from model import Base

from typing import List
from urllib import response


Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/status")
def status():
    return {"message":"ok"}


@app.get("/items/", response_model = list[schema_Item])
def read_items(skip:int=0,limit:int=100, db:Session=Depends(get_db)):
    items=get_items(db,skip=skip,limit=limit)
    return items

@app.post("/items", response_model=schema_Item)
def post_item(item:schema_Item_create, db:Session=Depends(get_db)):
    return create_item(db=db,item=item)
    
@app.get("/items/{item_id}", response_model = schema_Item)
def read_item(item_id:int, db:Session=Depends(get_db)):
    db_item=get_item(db=db,item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item
    