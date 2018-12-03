import sqlite3
from contextlib import closing

from business import Product

def get_products():
    conn = sqlite3.connect("products.sqlite")
    conn.row_factory = sqlite3.Row
    products = []
    try:
        with closing(conn.cursor()) as c:
            query = '''SELECT * FROM Products'''
            for row in c.execute(query):
                product = Product(row[0], row[1], float(row[2]), int(row[3]), int(row[4]))
                products.append(product)

    except sqlite3.OperationalError as e:
        products = None
        print("Error reading database -", e)
    return products

