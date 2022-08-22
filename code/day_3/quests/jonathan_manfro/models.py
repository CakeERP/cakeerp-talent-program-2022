import email
from operator import truediv
from unicodedata import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlachemy.orm import relationship

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id =Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    description = Column(String, index=True)
    email = Column(String, index=True)