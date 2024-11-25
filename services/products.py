from dependencies.dependencies import db_connection
from schemas.schemas import Product
from psycopg2 import Error

from services.get import get_product_name


def add_products_to_db(product:Product):
    cursor = db_connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO packing_optimization_db.products(id, name, weight) VALUES (%s,%s,%s)",
            (product.product_id, product.product_name, product.product_weight)
        )
        db_connection.commit()
        return {"message": f"product with name {product.product_name} added successfully"}
    except Error as e:
        return {"error in request": str(e)}
        db_connection.rollback()
    finally:
        cursor.close()


def search_products_by_id(product_id: int):
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM packing_optimization_db.products WHERE id = %s", (product_id,))
        data = cursor.fetchall()
        return {"data": data}
    except Error as e:
        return {"error in request": str(e)}
    finally:
        cursor.close()

def list_products_from_db():
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM packing_optimization_db.products ORDER BY ID ASC")
        data = cursor.fetchall()
        return {"data": data}
    except Error as e:
        return {"error in request": str(e)}
    finally:
        cursor.close()

def update_products_in_db(product_id:int, product:Product):
    cursor = db_connection.cursor()

    try:
        cursor.execute("UPDATE packing_optimization_db.products SET name = %s, weight = %s WHERE id= %s",
                       (product.product_name, product.product_weight,product_id)
                       )
        db_connection.commit()
        return {f"product {product.product_name} updated succesfully"}
    except Error as e:
        db_connection.rollback()
        return {"error in request": str(e)}
    finally:
        cursor.close()

def delete_products_from_db(product_id:int):
    cursor = db_connection.cursor()
    try:
        cursor.execute(
            "DELETE FROM packing_optimization_db.products WHERE id = (%s)", (product_id,)
        )

        db_connection.commit()
        return {"message": f"product with id {product_id} deleted successfully"}
    except Error as e:
        db_connection.rollback()
        return {"error in request": str(e)}
    finally:
        cursor.close()