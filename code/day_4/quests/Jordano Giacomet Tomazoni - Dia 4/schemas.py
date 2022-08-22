from datetime import datetime
from typing import Optional
from pydantic import BaseModel

#Criada uma classe pai e para o SchemaItemCreate eu vou herdar essa classe pai, ele nao vai fazer nada além de ser utilizando quando eu criar um registro

class SchemaItemBase(BaseModel):
    title: str
    year: int
    director: str
    create_date: datetime = None

class SchemaItemCreate(SchemaItemBase):
    pass

#A ideia é que quando o item é criado e usuario nao precisa saber o id

class SchemaItem(SchemaItemBase): #Nesse ponto definimos o id porque esse schema vai servir como uma busca por id
    id: int
    class Config:
        orm_mode = True