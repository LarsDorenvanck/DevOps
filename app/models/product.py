import os

from sqlalchemy import Column, Integer, String, DECIMAL
from config import Base

db_schema = os.getenv("DB_SCHEMA")

class Product(Base):
    __tablename__ = "products"
    __table_args__ = {'schema': f'{db_schema}'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False)
    weight = Column(DECIMAL, nullable=True)
