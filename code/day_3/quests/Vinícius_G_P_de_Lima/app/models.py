from code import interact
from operator import index
from turtle import title
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from.database import Base

class Item(Base):
    id=Column(Integer, primary_key=true, index=true)
    title=Column(string,index=true)
    description=Column(string,index=true)