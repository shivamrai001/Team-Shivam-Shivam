from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    email = Column(String, unique=True)

    password = Column(String)


class Complaint(Base):

    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    description = Column(String)

    image = Column(String)

    latitude = Column(Float)

    longitude = Column(Float)

    category = Column(String)

    severity_score = Column(Integer)

    priority = Column(String)

    genuine_score = Column(Float)

    department = Column(String)

    status = Column(String)

    created_at = Column(String)