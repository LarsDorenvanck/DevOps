from fastapi import APIRouter
from schemas.schemas import Warehouse
from services.warehouses import add_warehouse_to_db, delete_warehouse_from_db, list_warehouses_from_db, \
    get_warehouse_by_id, update_warehouse_in_db

router = APIRouter()

@router.post("/")
def add_warehouses(warehouse:Warehouse):
    return add_warehouse_to_db(warehouse)

@router.get("/")
def list_warehouses():
    return list_warehouses_from_db()

@router.get("/{warehouse_id}")
def get_warehouse(warehouse_id: int):
    return get_warehouse_by_id(warehouse_id)

@router.put("/{warehouse_id}")
def update_warehouse(warehouse_id: int, warehouse:Warehouse):
    return update_warehouse_in_db(warehouse_id, warehouse)

@router.delete("/{warehouse_id}")
def delete_warehouses(warehouse_id: int):
    return delete_warehouse_from_db(warehouse_id)

