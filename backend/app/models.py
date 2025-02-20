from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

# Creating a base class for our models
Base = declarative_base()   # -> a class created by the declarative_base function provided by SQLAlchemy

# We'll build all of our models based on this Base

# User Model
class User(Base):
  __tablename__ = "users"       # name of the table

  id = Column(Integer, unique=True, primary_key=True, index=True)               # self-explanatory
  username = Column(String, unique=True, index=True, nullable=False)
  email = Column(String, unique=True, index=True, nullable=False)
  hashed_password = Column(String, nullable=False)
  created_at = Column(DateTime, default=datetime.timezone.utc)