import os

from sqlalchemy import Column, Integer, ForeignKey
from config import Base

db_schema = os.getenv("DB_SCHEMA")

class ProductWarehouseLocation(Base):
    __tablename__ = "product_warehouse_locations"
    __table_args__ = {'schema': f'{db_schema}'}


    warehouse_id = Column(Integer, ForeignKey(f"{db_schema}.warehouses.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey(f"{db_schema}.products.id"), primary_key=True)
    x_coordinate = Column(Integer, nullable=False)
    y_coordinate = Column(Integer, nullable=False)
