import os
from dorenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine (
        url = SQLALCHEMY_DATABASE_URL,
        connect_args={}
)
SessionLocal = sessionmaker (autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLoval()
    try:
        yield db
    finally:
        db.close()
