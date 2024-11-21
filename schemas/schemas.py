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
    id: int
    name: str
    columns: int
    rows: int
