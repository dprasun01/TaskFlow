# This is the backend api file that is going to route GET and POST requests

from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Home page
def read_root():
  return {"message": "Taskflow backend is running"}