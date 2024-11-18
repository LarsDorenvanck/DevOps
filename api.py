
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()


class Product(BaseModel):
    name: str
    product_ID: int
    warehouse_id: int
    cord_x: int
    cord_y: int

class Order(BaseModel):
    order_ID: int
    order_products: list[Product]

products = {
    0: Product(name="banaan", product_ID=0, warehouse_id=2, cord_x=5, cord_y=5),
    1: Product(name="kers", product_ID=1, warehouse_id=1, cord_x=2, cord_y=3),
    2: Product(name="niek", product_ID=2, warehouse_id=2, cord_x=1, cord_y=4),
    3: Product(name="gerby", product_ID=3, warehouse_id=3, cord_x=9, cord_y=9),
    4: Product(name="Sophfia", product_ID=4, warehouse_id=4, cord_x=6, cord_y=9),
    5: Product(name="giswo", product_ID=5, warehouse_id=5, cord_x=7, cord_y=7),
    6: Product(name= "Jan", product_ID=6, warehouse_id=6, cord_x=8, cord_y=2),
}

orders = {
# order_1 = Order(order_ID=0, order_products=[products[2], products[0]])
    0: Order(order_ID=0, order_products=[products[0],products[1],products[2],products[3],products[4],products[5],products[6]]),
}

@app.get("/")
def index() -> dict[str, dict[int, Product]]:
    return {"products": products}


@app.get("/products/{product_id}")
def get_product(product_id: int) -> Product:
    if product_id not in products:
        raise HTTPException(status_code=404, detail=f"Product with id: {product_id} was not found")
    else:
        return products[product_id]

@app.get("/orders/{order_id}")
def get_orders(order_id: int) -> Order:
    if order_id not in orders:
        raise HTTPException(status_code=404, detail=f"Order with id: {order_id} was not found")
    else:
        return orders[order_id]
