
from fastapi import FastAPI

from dependencies.dependencies import db_connection

from psycopg2 import connect, Error
from psycopg2.extras import RealDictCursor
import sys

from routers import products, boxes
from schemas.schemas import ProductLocation
app = FastAPI()

app.include_router(products.router, prefix="/products")
app.include_router(products.router, prefix="/add_product")



@app.post("/assign_product_location/")
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



def get_product_name(product_id):
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT name FROM packing_optimization_db.products WHERE id = %s", (product_id,))
        data = cursor.fetchall()
        print(data[0][0])
        return data[0][0]
    except Error as e:
        return {"error in request": str(e)}
    finally: cursor.close()


def get_warehouse_constrains(warehouse_id):
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM packing_optimization_db.warehouses WHERE id = %s",
                    (warehouse_id,)
                    )
        data = cursor.fetchall()
        warehouse_name = ({data[0][1]})
        warehouse_x = ({data[0][2]})
        warehouse_y = ({data[0][3]})
        return_tuple = (warehouse_name, warehouse_x, warehouse_y)
        return return_tuple
    except Error as e:
        return {"error in request": str(e)}
    finally: cursor.close()

