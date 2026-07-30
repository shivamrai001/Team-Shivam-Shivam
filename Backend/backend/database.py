from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import DATABASE_URL

#Create the database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#Create a session factory
Base = declarative_base()

#Database dependancy
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
