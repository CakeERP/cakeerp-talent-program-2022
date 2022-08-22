from sqlalchemy.orm import Session
from models import Item
from schema import schema_Item_create



def get_items( db : Session, skip : int=0, limit : int=100):
    return db.query(Item).offset(skip).limit(limit).all()



def get_item( db : Session,item_id:int):
    return db.query(Item).filter(item_id==item_id).first()


def create_item( db:Session, item:schema_Item_create):
     db_item(**item.dict())
     db.add(db.item)
     db.commit()
     db.refresh(db.item)
     return db_item

