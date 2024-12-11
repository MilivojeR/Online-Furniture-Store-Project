from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import Settings

settings = Settings()

engine = create_engine(settings.DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine, expire_on_commit=False, autocommit = False)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close

db = Annotated[Session, Depends(get_db)]