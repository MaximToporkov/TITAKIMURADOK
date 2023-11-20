import sqlite3


PATH = r"C:\Users\SAZol\PycharmProjects\Max_corsach\TITAKIMURADOK\DB\db_pc_con.sqlite"

def select_cat():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM category")
    return cursor.fetchall()


def select_cat_for_insert_auto(cat):
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT id FROM category WHERE name='{cat}';")
    id = cursor.fetchone()
    cursor.close()
    con.close()
    return id


def select_user():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM users;")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_goods():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM users;")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_master():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM users;")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_cpu():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT goods.name, category.id FROM goods, category WHERE category.id = '1';")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_gpu():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT goods.name, category.id FROM goods, category WHERE category.id = '2';")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_power():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT goods.name, category.id FROM goods, category WHERE category.id = '3';")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_ram():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT goods.name, category.id FROM goods, category WHERE category.id = '4';")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_motherboard():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT goods.name, category.id FROM goods, category WHERE category.id = '5';")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_cooling():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT goods.name, category.id FROM goods, category WHERE category.id = '6';")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id


def select_hdd():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT goods.name, category.id FROM goods, category WHERE category.id = '7';")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id

def select_price():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT price FROM goods;")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id

def select_pc():
    con = sqlite3.connect(PATH)
    cursor = con.cursor()
    cursor.execute(f"SELECT id FROM pc ;")
    id = cursor.fetchall()
    cursor.close()
    con.close()
    return id

# def select_order():
#     con = sqlite3.connect(PATH)
#     cursor = con.cursor()
#     cursor.execute(f"SELECT users.phone, master.name "
#                    f"FROM master, users, pc"
#                    f"WHERE master_id = master.id AND user_id = users.id")
#     id = cursor.fetchall()
#     cursor.close()
#     con.close()
#     return id
