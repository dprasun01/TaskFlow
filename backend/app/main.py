# This is the backend api file that is going to route GET and POST requests

from fastapi import FastAPI
from routes import task, user, auth

app = FastAPI()

# Include the user and task routers
app.include_router(user.router)
app.include_router(task.router)
app.include_router(auth.router)


@app.get("/") # Root URL/endpoint
def read_root():
  return {"message": "Taskflow backend is running"}