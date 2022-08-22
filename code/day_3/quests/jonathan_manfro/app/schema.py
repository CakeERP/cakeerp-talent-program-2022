from pydantic import BaseModel
from fastapi import FastAPI
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

