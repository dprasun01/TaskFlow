from sqlalchemy import create_engine          # creates a new engine instance; entry point for any SQLAlchemy app
from sqlalchemy.orm import sessionmaker       # read dev-notes for detailed explanation and usage
from app.config import settings               # import the environment variables for our PostgreSQL database


# create an engine using the connection URL defined in .env (loaded via config.py)
engine = create_engine(settings.DATABASE_URL) # Provides low level connection to the database

# sessionmaker creates a factory for generating new session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#<-- binding the session to our engine

def get_db():
  db = SessionLocal()                         # create a new db session for each request to the database
  try:
    yield db                                  # yield the db to the calling route function
  finally:
    db.close()                                # close db/session, regardless of success or failure of the request