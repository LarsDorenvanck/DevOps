from schemas.schemas import Warehouse
from dependencies.dependencies import db_connection
from psycopg2 import Error

def add_warehouse_to_db(warehouse:Warehouse):
    cursor = db_connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO packing_optimization_db.warehouses(id, name, columns, rows) VALUES (%s,%s,%s,%s)",
            (warehouse.warehouse_id, warehouse.warehouse_name, warehouse.warehouse_columns, warehouse.warehouse_rows)
        )
        db_connection.commit()
        return {"message": f"warehouse with name {warehouse.warehouse_name} added successfully"}
    except Error as e:
        return {"error in request": str(e)}
        db_connection.rollback()
    finally:
        cursor.close()


def delete_warehouse_from_db(warehouse_id: int):
    cursor = db_connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM packing_optimization_db.warehouses WHERE id = (%s)", (warehouse_id,)
        )

        db_connection.commit()
        return {"message": f"warehouse with id {warehouse_id} deleted successfully"}
    except Error as e:
        db_connection.rollback()
        return {"error in request": str(e)}
    finally:
        cursor.close()

def list_warehouses_from_db():
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM packing_optimization_db.warehouses ORDER BY ID ASC")
        data = cursor.fetchall()
        return {"data": data}
    except Error as e:
        return {"error in request": str(e)}
    finally:
        cursor.close()


def get_warehouse_by_id(warehouse_id: int):
    cursor = db_connection.cursor()
    try:
        cursor.execute("SELECT * FROM packing_optimization_db.warehouses WHERE id = %s", (warehouse_id,))
        data = cursor.fetchall()
        return {"data": data}
    except Error as e:
        return {"error in request": str(e)}
    finally:
        cursor.close()

def update_warehouse_in_db(warehouse_id: int, warehouse:Warehouse):
    cursor = db_connection.cursor()
    try:
        cursor.execute("UPDATE packing_optimization_db.warehouses SET name = %s, columns = %s, rows = %s WHERE id= %s",
                       (warehouse.warehouse_name, warehouse.warehouse_columns, warehouse.warehouse_rows, warehouse_id))
        db_connection.commit()
        return {"message": f"warehouse {warehouse_id} updated succesfully"}
    except Error as e:
        db_connection.rollback()
        return {"error in request": str(e)}
    finally:
        cursor.close()
