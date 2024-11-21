from fastapi import APIRouter
from psycopg2 import Error
from dependencies.dependencies import db_connection
from schemas.schemas import ProductLocation
from services.get import get_warehouse_constrains, get_product_name

router = APIRouter()

@router.post("/assign_product_location/")
def assign_product_location(product_location: ProductLocation):
    cursor = db_connection.cursor()
    try:
        check_tuple = get_warehouse_constrains(product_location.warehouse_id)
        warehouse_name = check_tuple[0].pop()
        warehouse_x = check_tuple[1].pop()
        warehouse_y = check_tuple[2].pop()
        print(check_tuple[1])
        if warehouse_x < product_location.x_coordinate:
             raise Exception("x_coordinate can not be bigger then warehouse size contrains")
        elif warehouse_y < product_location.y_coordinate:
             raise Exception("y_coordinate can not be smaller than warehouse size contrains")

        cursor.execute("INSERT INTO packing_optimization_db.product_warehouse_locations(warehouse_id, product_id, x_coordinate, y_coordinate) VALUES (%s,%s,%s,%s)",
        (product_location.warehouse_id, product_location.product_id, product_location.x_coordinate, product_location.y_coordinate)
            )
        db_connection.commit()
        product_name= get_product_name(product_location.product_id)
        return {"message": f"product location of {product_name} in {warehouse_name} at x= {product_location.x_coordinate} and y= {product_location.y_coordinate} assigned successfully"}

    except Error as e:
        return {"error in request": str(e)}

    finally: cursor.close()
