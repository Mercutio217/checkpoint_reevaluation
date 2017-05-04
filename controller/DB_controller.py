import sqlite3
import os

from model.Product import Product


class DBController:

    """Class for database connection"""


    def __init__(self):
        self.dir = os.path.dirname(__file__)
        self.filename = os.path.join(dir, "todo.db")

    def get_connection(self):
        base = sqlite3.connect(self.filename)
        return base

    def get_all(self):
        database = self.get_connection()
        list_of_products = []
        db_list = database.execute("SELECT * FROM products")
        for info in db_list:
            product = Product(info[1], info[2], info[3])
            product.id = info[0]
            list_of_products.append(product)
        database.close()

        return list_of_products




