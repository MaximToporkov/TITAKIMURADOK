#from db_connect import connection
import sqlite3

from DB.db_select import select_cat_for_insert_auto

PATH = r"C:\Users\SAZol\PycharmProjects\Max_corsach\TITAKIMURADOK\DB\db_pc_con.sqlite"
def insert(funk):
    def wrapper(*args):
        funk(*args)
    return wrapper()


def add_user_db(number, name, lastname):
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO users (name, family, phone) VALUES ('{name}', '{lastname}', {number})")
    con.commit()


def add_goods_db(number, brend, location):
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    id_cat = select_cat_for_insert_auto(brend)
    cursor.execute(f"INSERT INTO goods (name, category_id, price) VALUES ('{number}', '{id_cat[0]}', {int(location)})")
    con.commit()


def add_pc_db(cpu, gpu, ram, mother, hdd, col, power):
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO pc (cpu, gpu, ram, motherboard, HDD_SSD, cooling, power) VALUES ('{cpu}', '{gpu}', '{ram}', '{mother}', '{hdd}', '{col}', '{power}')")
    con.commit()


def add_order_db(master, user, pc, price):
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO orders (master_id, user_id, pc_id, price) VALUES ('1', '2', '1', '1')")
    con.commit()