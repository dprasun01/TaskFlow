from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

# Initializing the password hashing context using CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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