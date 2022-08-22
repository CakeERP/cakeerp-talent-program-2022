from typing import List
from sqlalchemy.orm import Session
from .database import get_db, engine
from .models import Base

from .schemas import SchemaItem, SchemaItemCreate
from .crud import get_item, get_items, create_item

from fastapi import Depends, FastAPI, HTTPException

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/items", response_model=SchemaItem)
def post_item(item: SchemaItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)


@app.get("/items", response_model=List[SchemaItem])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)

    return items


@app.get("/items/{item_id}", response_model=SchemaItem)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id=item_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return db_item
