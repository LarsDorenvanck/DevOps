from fastapi import APIRouter

from schemas.schemas import Product
from services.products import add_products_to_db, search_products_by_id, list_products_from_db, update_products_in_db, \
    delete_products_from_db

router = APIRouter()


@router.post("/")
def add_order(product: Product):
    return add_products_to_db(product)

@router.get("/")
def get_products():
    return list_products_from_db()

@router.put("/{product_id}")
def update_product(product_id: str, product: Product):
    return update_products_in_db(product_id,product)

@router.get("/{product_id}")
def get_data_from_db(product_id: int):
    return search_products_by_id(product_id)

@router.delete("/{product_id}")
def delete_product(product_id: int):
    return delete_products_from_db(product_id)
