from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import SQLAlchemyError
from config import engine, Base, db_config
from app.models import (
    Warehouse,
    Product,
    ProductWarehouseLocation,
    Order,
    OrderLine,
    Box,
)

def create_database_if_not_exist(db_name, db_url):
    """
    Ensures the database exists. Creates it if not already present.
    """
    try:
        if not database_exists(f"{db_url}{db_name}"):
            print(f"Database {db_name} does not exist. Creating...")
            create_database(f"{db_url}{db_name}")
            print(f"Database {db_name} created successfully.")
        else:
            print(f"Database {db_name} already exists.")
    except SQLAlchemyError as e:
        print(f"Failed to create or check the database: {str(e)}")

def create_schema_if_not_exist(db_name, db_url, db_schema):
    """
    Checks if a specific schema exists and creates it if not.
    """
    # Create server engines
    server_engine = create_engine(db_url)
    server_engine_with_database = create_engine(db_url + db_name)
    try:
        with server_engine_with_database.connect() as conn:
            if not server_engine.dialect.has_schema(conn, db_schema):
                statement = text(f"CREATE SCHEMA IF NOT EXISTS {db_schema}")
                conn.execute(statement)
                conn.commit()
                print(f"Schema '{db_schema}' created successfully!")
            else:
                print(f"Schema '{db_schema}' already exists!")

    except Exception as e:
        print(f"Failed to create schema: {e}")


def create_tables_if_not_exist():
    """
    Ensures all tables in the database exist.
    """
    try:
        print("Checking and creating tables if they do not exist...")
        Base.metadata.create_all(bind=engine, checkfirst=True)
        print("Tables checked or created successfully.")
    except SQLAlchemyError as e:
        print(f"Failed to create tables: {str(e)}")

