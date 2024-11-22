import os

from sqlalchemy import Column, Integer, String
from config import Base

db_schema = os.getenv("DB_SCHEMA")

class Order(Base):
    __tablename__ = "orders"
    __table_args__ = {'schema': f'{db_schema}'}

    id = Column(Integer, primary_key=True, index=True)
