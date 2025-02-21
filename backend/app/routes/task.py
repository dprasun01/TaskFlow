from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database, models
from app.dependencies import get_current_user

router = APIRouter(
  prefix="/tasks",
  tags=["tasks"]
)

@router.post("/", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
  task: schemas.TaskCreate, 
  db: Session = Depends(get_current_user),
  current_user: models.User = Depends(get_current_user)
  ):
  
  # The dependency injection of get_current_user provides the authenticated user's info
  return crud.create_task(db=db, task=task, current_user=current_user)

