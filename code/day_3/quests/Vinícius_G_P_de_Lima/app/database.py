from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABE_URL= "sqllite:///./sql_app.db"

engine=create_engine(url=SQLALCHEMY_DATABE_URL,connect_args={"check_same_thread":False} )
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal
    try:
        yield db
    finally:
        db.close()
        