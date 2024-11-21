
from fastapi import FastAPI

from dependencies.dependencies import db_connection

from psycopg2 import connect, Error
from psycopg2.extras import RealDictCursor
import sys

from routers import products, locations
from schemas.schemas import ProductLocation
app = FastAPI()

app.include_router(products.router, prefix="/products")
app.include_router(products.router, prefix="/add_product")
app.include_router(locations.router, prefix="/locations")





