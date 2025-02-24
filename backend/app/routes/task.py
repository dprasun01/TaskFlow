from fastapi import HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database, models, dependencies

router = APIRouter(
  prefix="/tasks",
  tags=["tasks"]
)

@router.post("/", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
  task: schemas.TaskCreate, 
  db: Session = Depends(database.get_db),
  current_user: models.User = Depends(dependencies.get_current_user)
  ):
  
  # The dependency injection of get_current_user provides the authenticated user's info
  return crud.create_task(db=db, task=task, current_user=current_user)


# response_model is configured as a list of TaskResponse schema [IMPORTANT]
@router.get("/", response_model=List[schemas.TaskResponse], status_code=status.HTTP_200_OK)
def read_tasks(
  db: Session = Depends(database.get_db),
  current_user: models.User = Depends(dependencies.get_current_user)
):
  tasks = crud.get_tasks(db=db, current_user=current_user)
  return tasks


@router.get("/{taskid}", response_model=schemas.TaskResponse, status_code=status.HTTP_200_OK)
def read_task(
  taskid: int,
  db: Session = Depends(database.get_db),
  current_user: models.User = Depends(dependencies.get_current_user)
):
  task = crud.get_task(db=db, taskid=taskid, current_user=current_user)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  return task