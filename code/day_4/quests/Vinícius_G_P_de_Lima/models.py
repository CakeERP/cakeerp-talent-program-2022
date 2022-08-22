import datetime
from operator import index
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    description = Column(String(245), index=True)
    create_date = Column(DateTime, default=datetime.datetime.utcnow())

