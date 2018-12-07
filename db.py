import sqlite3
from contextlib import closing

from business import Product

def get_products():
    conn = sqlite3.connect("products.sqlite")
    conn.row_factory = sqlite3.Row
    products = []
    try:
        with closing(conn.cursor()) as c:
            query = '''SELECT * FROM Products;'''
            for row in c.execute(query):
                product = Product(row[0], row[1], float(row[2]), int(row[3]), int(row[4]))
                products.append(product)

    except sqlite3.OperationalError as e:
        products = None
        print("Error reading database -", e)
    return products

def updateItems(products):
    conn = sqlite3.connect("products.sqlite")
    conn.row_factory = sqlite3.Row
    for product in products:
        try:
            with closing(conn.cursor()) as c:
                c.execute('UPDATE Products SET quantity=? WHERE productID=?', (product.quantityAvailable, product.productID))
                conn.commit()
        except sqlite3.OperationalError as e:
            print("Error reading database -", e)

def insertItems(itemList):
    conn = sqlite3.connect("products.sqlite")
    conn.row_factory = sqlite3.Row
    try:
        with closing(conn.cursor()) as c:
            c.executemany('INSERT OR REPLACE INTO Products(productID, name, price, discountPercent, quantity) VALUES(?,?,?,?,?)', itemList)
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Error reading database -", e)
