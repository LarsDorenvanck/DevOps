from psycopg2 import Error
from dependencies.dependencies import db_connection


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
