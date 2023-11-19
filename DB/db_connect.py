import sqlite3
from sqlite3 import Error


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("db_pc_con.sqlite")
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection()
