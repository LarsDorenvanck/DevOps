from fastapi import FastAPI
from routers import products, locations, warehouses

app = FastAPI()

app.include_router(products.router, prefix="/products")
app.include_router(locations.router, prefix="/locations")
app.include_router(warehouses.router, prefix="/warehouses")





