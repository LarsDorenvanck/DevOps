import psycopg2

db_connection = psycopg2.connect(
    database = 'packing_optimization_db',
    user = 'postgres',
    password = 'password',
    host = 'localhost',
    port = '5432'
)