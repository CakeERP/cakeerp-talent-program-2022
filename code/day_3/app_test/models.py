from sqlalchemy import Column, Integer, String
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(45), index=True)
    description = Column(String(245), index=True)
