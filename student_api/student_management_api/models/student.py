from sqlalchemy import Column, Integer, String
from database.db import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)

# Create table
Base.metadata.create_all(bind=engine)