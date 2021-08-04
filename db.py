import sqlite3
from sqlite3 import Error

DATABASE_NAME = "products.db"

def get_db():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():

    create_user_table = """CREATE TABLE IF NOT EXISTS user(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
				last_name TEXT NOT NULL,
				mail TEXT NOT NULL,
				username TEXT NOT NULL,
				password TEXT NOT NULL
            ); """

    create_products_table =  """CREATE TABLE IF NOT EXISTS products(
         product_id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT NOT NULL,
         content TEXT NOT NULL,
         uses TEXT NOT NULL,
         date_created TEXT NOT NULL
         )
         """

    # create a database connection
    conn = get_db()

    # create tables
    if conn is not None:
        # create user table
        create_table(conn, create_user_table)

        # create products table
        create_table(conn, create_products_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
