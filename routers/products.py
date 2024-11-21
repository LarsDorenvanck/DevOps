from fastapi import APIRouter
from psycopg2 import Error
from dependencies.dependencies import db_connection
from schemas.schemas import Product

router = APIRouter()


@router.post("/add_product/")
def add_order(product:Product):
    cursor = db_connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO packing_optimization_db.products(id, name, weight) VALUES (%s,%s,%s)",
            (product.product_id, product.product_name, product.product_weight)
            )
        db_connection.commit()
        return{"message": f"product with name {product.product_name} added successfully"}
    except Error as e:
        return {"error in request": str(e)}
        db_connection.rollback()
    finally: cursor.close()



@router.get("/{product_id}")
def get_data_from_db(product_id: int):
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM packing_optimization_db.products WHERE id = %s", (product_id,))
        data = cursor.fetchall()
        print(f"{data[0][0]}\n{data[0][1]}\n{data[0][2]}")
        return {"data": data}
    except Error as e:
        return {"error in request": str(e)}
    finally:
        cursor.close()
