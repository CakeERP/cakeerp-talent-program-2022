from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLITE_DATABASE_URL = "sqlite:///./sqlite_app.db"

engine = create_engine(
    SQLITE_DATABASE_URL, connect_args = {"check_same_thread": False}
)

SessaoLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Banco = declarative_base