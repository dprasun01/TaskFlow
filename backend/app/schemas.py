from pydantic import BaseModel
import datetime

# Common base schema for user data
class UserBase(BaseModel):
  username : str
  email : str

# Schema for creating a new user, 
# i.e., it inherits the schems for UserBase (common fields for all users) and asls for a password as well
class UserCreate(UserBase): # -> FOR DESERIALIZATION
  password : str

# Schema for sending user data in responses,
# i.e., when Pydantic converts the SQLAlchemy returned object to FastAPI, only fields specified here will 
# be present in the JSON response the front-end gets
#  |
#  |
# \|/

class UserResponse(UserBase): # -> FOR SERIALIZATION
  # SQLAlchemy creates these fields, as defined in User model during the transaction (writing to database)
  id : int
  created_at : datetime

  class Config:
    # enables Pydantic to SERIALIZE sqlalchemy object(s) returned to dictionaries for JSON response
    orm_mode = True


# Schemas for Tasks:
class TaskBase(BaseModel):
  taskname : str
  task_description : str = "" # -> Default value
  status : bool = False       # -> Default value
  # userid : int
  # username : str

class TaskCreate(TaskBase):
  pass

class TaskResponse(TaskBase):
  id : int
  created_at : datetime

  class Config:
    orm_mode = True