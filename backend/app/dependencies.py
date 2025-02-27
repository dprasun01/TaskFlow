from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.config import settings
from app.database import get_db
from app import crud, models

# Extracts the token from the Authentication header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
  
  # Defining a credentials exception
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate" : "Bearer"}
  )

  try:
    # Decoding the JWT token using the SECRET KEY and HS256 algorithm
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    username: str = payload.get("sub")
    if username is None:
      raise credentials_exception
  
  except JWTError:
    raise credentials_exception
  
  user = crud.get_user_by_username(db, username=username)
  if user is None:
    raise credentials_exception
  return user