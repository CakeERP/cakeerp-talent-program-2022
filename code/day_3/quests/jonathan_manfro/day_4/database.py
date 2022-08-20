from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

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
