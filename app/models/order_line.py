import os

from sqlalchemy import Column, Integer, ForeignKey
from config import Base

db_schema = os.getenv("DB_SCHEMA")

class OrderLine(Base):
    __tablename__ = "order_lines"
    __table_args__ = {'schema': f'{db_schema}'}

    order_id = Column(Integer, ForeignKey(f"{db_schema}.orders.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey(f"{db_schema}.products.id"), primary_key=True)
    quantity = Column(Integer, nullable=False)
