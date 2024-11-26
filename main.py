from fastapi import FastAPI
from app.database import create_database, create_schema

# Initialize FastAPI app
app = FastAPI()

# Optional to create database and
# create_database()
# create_schema()

print("iets")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}