import sqlite3
import os

from model.Product import Product


class DBController:
    """Class for database connection"""

    def __init__(self):
        self.dir = os.path.dirname(__file__)
        self.filename = os.path.join(self.dir, "products.db")

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

    def add_to_db(self, product):
        """ Saves todo item in database """
        database = self.get_connection()
        cursor = database.cursor()
        cursor.execute("INSERT INTO products (name, description, price)"
                       "VALUES (?, ?, ?);",
                       (product.name, product.description, product.price))
        database.commit()
        database.close()

    def remove_from_db(self, product_id):
        database = self.get_connection()
        cursor = database.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id, ))
        database.commit()
        database.close()
