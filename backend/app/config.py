from pydantic import BaseSettings
import os
from dotenv import load_dotenv

# Loading the environment variables required for backend from it corresponding .env file (outside backend/)
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(env_path)

class Settings(BaseSettings):
  DATABASE_URL : str
  MONGODB_URI : str
  REDIS_URL : str
  SECRET_KEY : str

  class Config:
    env_file = env_path # Specifying the .env location

settings = Settings() # Creating an instance of Settings
