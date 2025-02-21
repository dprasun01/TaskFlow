from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

  """
  user: schemas.UserCreate: 
  FastAPI automatically validates and parses the incoming JSON body using the UserCreate Pydantic model

  db: Session = Depends(database.get_db): 
  This uses dependency injection to provide a new database session to the endpoint.
  """
  
  # First, check if the username is already taken
  db_user_exists = crud.get_user_by_username(db, user.username)
  
  if db_user_exists:
    raise HTTPException(status_code=400, detail="Username is already taken.")
  
  # Create the new user
  return crud.create_user(db=db, user=user)