from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    product_name: str
    product_weight: float

class ProductLocation(BaseModel):
    warehouse_id: int
    product_id: int
    x_coordinate: int
    y_coordinate: int

class Warehouse(BaseModel):
    warehouse_id: int
    warehouse_name: str
    warehouse_columns: int
    warehouse_rows: int
