from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session
from app import crud # models, dependencies, config
from app.database import get_db
# from jose import jwt

router = APIRouter() # Notice that we don't use/need a prefix and tags here

# METHOD FOR LOGGING IN
@router.post("/token", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  
  user = crud.authenticate_user(db, form_data.username, form_data.password)

  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password",
      headers={"WWW-Authenticate" : "Bearer"}
    )
  
  # Create a JWT token
  access_token_expires = timedelta(minutes=30)
  access_token = crud.create_access_token(
    data = {"sub" : user.username}, expires_delta = access_token_expires
  )

  return {"access_token": access_token, "token_type": "bearer"}
