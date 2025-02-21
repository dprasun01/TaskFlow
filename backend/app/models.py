from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
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
  created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

# Task Model
class Task(Base):
  __tablename__ = "tasks"

  id = Column(Integer, primary_key=True, unique=True, index=True)
  taskname = Column(String, nullable=False, unique=True, index=True)
  task_description = Column(String(250), default="")
  status = Column(Boolean, default=False)
  created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
  
  # user's ID and username as the Foreign Keys
  userid = Column(Integer, ForeignKey("users.id"), nullable=False)
  username = Column(String, ForeignKey("users.username"), nullable=False)