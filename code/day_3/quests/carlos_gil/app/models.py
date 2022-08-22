from sqlalchemy import Column, Integer, String

from .database import Base

class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, index=True)
    name: Column(String, index=True)
    email: Column(String, index=True)
    description: Column(String, index=True)