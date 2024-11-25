from fastapi import APIRouter


from schemas.schemas import ProductLocation

from services.locations import assign_locations

router = APIRouter()

@router.post("/assign/")
def assign_product_location(product_location: ProductLocation):
    return assign_locations(product_location)
