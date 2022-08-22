from sqlalchemy.orm import Session

from models import Item
from schemas import SchemaItemCreate

#Ideia desse primeiro elemento é pegar de um banco session, todos os items de 0 a 100

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

#Ideia nessa função é pegar um item especifico baseado no id, de modo que usamos um filtro para isso, onde o filtro do model tem que ser igual ao passado por parametro

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first

#Criar itens em formato de dicionario

def create_item(db: Session, item: SchemaItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item