import datetime
from typing import Optional
from unicodedata import name
from pydantic import BaseModel


class schema_Item_base(BaseModel):
    name:str
    description:Optional[str]=None
    create_date:datetime.datetime=None

class schema_Item_create(schema_Item_base):
    pass 


class schema_Item(schema_Item_base):
    id:int
    class config():
        orm_mode:True