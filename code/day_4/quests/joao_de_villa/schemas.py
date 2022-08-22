import datetime
from typing import Optional
from pydantic import BaseModel

class SchemaItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    create_date: datetime.datetime = None

class SchemaItemCreate(SchemaItemBase):
    pass

class SchemaItem(SchemaItemBase):
    id: int

    class Config:
        orm_mode = True

