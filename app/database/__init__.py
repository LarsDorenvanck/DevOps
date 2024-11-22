from config import db_config
from app.database.database_functions import create_database_if_not_exist, create_schema_if_not_exist

def create_database():
    create_database_if_not_exist(db_config["name"], db_config["url"])

def create_schema():
    create_schema_if_not_exist(db_config["name"], db_config["url"], db_config["schema"])




