from db import get_db

def insert_user(first_name, last_name, mail, username, password):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO user(first_name, Last_name, mail, username, password) VALUES (?, ?, ?, ?, ?);"
    cursor.execute(statement, [first_name, last_name, mail, username, password])
    db.commit()
    return True

def insert_product(title, content, uses, date_created):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO products(title, content, uses, date_created) VALUES (?, ?, ?, ?);"
    cursor.execute(statement, [title, content, uses, date_created])
    db.commit()
    return True

def update_product(title, content, uses):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE products SET title = ?, content = ?, uses = ? WHERE product_id = ?;"
    cursor.execute(statement, [title, content, uses])
    db.commit()
    return True


def delete_product():
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM products WHERE product_id = ?;"
    cursor.execute(statement)
    db.commit()
    return True


def get_by_id():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT product_id, title, content, uses FROM products WHERE product_id = ?;"
    cursor.execute(statement, [])
    return cursor.fetchone()

def get_products():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT product_id, title, content, uses FROM products;"
    cursor.execute(query)
    return cursor.fetchall()

def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM user;"
    cursor.execute(query)
    return cursor.fetchall()
