import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection components from environment variables
db_config = {
    "name" : os.getenv("DB_NAME"),
    "user" : os.getenv("DB_USER"),
    "password" : os.getenv("DB_PASSWORD"),
    "host" : os.getenv("DB_HOST"),
    "port" : os.getenv("DB_PORT"),
    "database" : os.getenv("DB_DATABASE"),
    "schema" : os.getenv("DB_SCHEMA"),
    "url" : f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/",
    "url_with_database" : f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
}

# Create the SQLAlchemy engine
engine = create_engine(db_config["url_with_database"])

# SessionLocal for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for model definitions
Base = declarative_base()


