from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/") #Equivalente ao que foi visto no desenvolvimento android esse é o ponto final da rota, onde tu
async def root():
    return{"message" : "Hello World"}

fake_items_db = [{"item_name":"foo"}, {"item_name": "Bar"}, {"item_name":"Baz"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 3):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}") #Equivalente ao que foi visto no desenvolvimento android esse é o ponto final da rota, onde tudo vai acontecer
async def read_item(item_id : int): #Eu posso definir um tipo de dado que deve ser passado na requisicao
    return{"item_id" : item_id}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

#Devo criar um modelo que ira receber os meus dados de cliente por exemplo

#Agora para usar esse modelo eu preciso de uma funcao
@app.post("/items/")
async def create_item(item:Item):
    return item


#A ideia é que meu end point seja em items/item_id
#Portanto eu posso passar esse endpoint como parametro da funcao
#E ele ser lido

