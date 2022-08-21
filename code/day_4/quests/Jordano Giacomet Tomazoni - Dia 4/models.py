import datetime
from email.policy import default
from operator import index
from turtle import title

from sqlalchemy import Column, Integer, String, DateTime

from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), index = True)
    year = Column(Integer, index = True)
    director = Column(String(45), index = True)
    create_date = Column(DateTime, default=datetime.datetime.utcnow())
