from operator import truediv
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlachemy.orm import relationship

from .database import Base


class Item(Base):
    __tavlename__ = "items"

    id =Column(Integer, primary_key=True, index=True)
    tittle=Column(String, index=True)
    description = Column(String, index=True)