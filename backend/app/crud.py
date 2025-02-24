from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

# Initializing the password hashing context using CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# USER CRUD OPERATIONS

def create_user(db: Session, user: schemas.UserCreate):
  
  # Hash the password first, this is obtained from the user Pydantic schema/model object
  hashed_password = pwd_context.hash(user.password)

  # [IMPORTANT] Create the user ORM object based on models.User
  db_user = models.User(
    username = user.username,
    email = user.email,
    hashed_password = hashed_password
  )

  # Add the new user object to the database session
  db.add(db_user) # -> adds the user as well as an id and created_at to the database session

  # Commit the transaction
  db.commit() # Finalizes and saves the transaction permanently on the actual database

  # Refresh to obtain the user's auto-generated fields
  db.refresh(db_user)

  return db_user # -> to FastAPI, which then uses Pydantic UserResponse schema to decouple the response for the API


def get_user_by_username(db: Session, username: str):

  # Queries the database db on User Table and filters by the first occurence of the given username
  # returns the first found record or None if not found
  return db.query(models.User).filter_by(username=username).first()


# TASK CRUD OPERATIONS

def create_task(db: Session, task: schemas.TaskCreate, current_user):

  db_task = models.Task(
    taskname = task.taskname,
    task_description = task.task_description,
    status = task.status,
    userid = current_user.id,
    username = current_user.username
  )

  db.add(db_task)
  db.commit()
  db.refresh(db_task)
  return db_task

def get_tasks(db: Session, current_user):
  # Get all the tasks by the current user in a list
  tasks = db.query(models.Task).filter_by(username=current_user.username, userid = current_user.id).all()
  return tasks

def get_task(db: Session, taskid: int, current_user):
  # Get one particular task by the current user
  return db.query(models.Task).filter_by(userid=current_user.id, id=taskid).first()


# AUTHENTICATE USERS

def authenticate_user(db: Session, username: str, password: str):
  # Get the first user with that username (bound to be unique)
  user = db.query(models.User).filter_by(username=username).first()
  if not user:
    return None
  
  # Verify the hashed password of the user
  if not pwd_context.verify(password, user.hashed_password):
    return None
  
  return user

# CREATE ACCESS TOKENS

def create_acess_token():
  pass