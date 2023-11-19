import sqlite3
from sqlite3 import Error
from db_connect import connection

create_user_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    family TEXT NOT NULL,
    phone TEXT NOT NULL
);    
"""

create_master_table = """
CREATE TABLE IF NOT EXISTS master (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    family TEXT NOT NULL,
    phone TEXT NOT NULL
);
"""

create_pc_table = """
CREATE TABLE IF NOT EXISTS pc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    CPU INTEGER,
    GPU INTEGER,
    power INTEGER,
    RAM INTEGER,
    motherboard INTEGER,
    cooling INTEGER,
    HDD_SSD INTEGER,
    FOREIGN KEY (CPU) REFERENCES goods (id)
    FOREIGN KEY (GPU) REFERENCES goods (id)
    FOREIGN KEY (power) REFERENCES goods (id)
    FOREIGN KEY (RAM) REFERENCES goods (id)
    FOREIGN KEY (motherboard) REFERENCES goods (id)
    FOREIGN KEY (cooling) REFERENCES goods (id)
    FOREIGN KEY (HDD_SSD) REFERENCES goods (id)
);
"""

create_goods_table = """
CREATE TABLE IF NOT EXISTS goods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category (id)
);
"""

create_category_table = """
CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
"""

create_order_tables = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    master_id INTEGER,
    user_id INTEGER,
    pc_id INTEGER,
    price INTEGER,
    FOREIGN KEY (master_id) REFERENCES master (id)
    FOREIGN KEY (user_id) REFERENCES users (id)
    FOREIGN KEY (pc_id) REFERENCES pc (id)
);  
"""


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


execute_query(connection, create_user_table)
execute_query(connection, create_master_table)
execute_query(connection, create_category_table)
execute_query(connection, create_goods_table)
execute_query(connection, create_pc_table)
execute_query(connection, create_order_tables)
