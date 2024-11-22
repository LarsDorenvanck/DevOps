import os

from sqlalchemy import Column, Integer, String
from config import Base

db_schema = os.getenv("DB_SCHEMA")


class Warehouse(Base):
    __tablename__ = "warehouses"
    __table_args__ = {'schema': f'{db_schema}'}


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), nullable=False)
    columns = Column(Integer, nullable=False)
    rows = Column(Integer, nullable=False)
