from controller.DB_controller import DBController


class Product_Controller:

    def __init__(self):
        self.database = DBController()
        self.connection = self.database.get_connection()
        self.product_list = self.database.get_all()

    def get_product_list(self):
        return self.product_list

    def add_product(self, product):
        self.database.add_to_db(product)

    def remove_product(self, product_id):
        self.database.remove_from_db(product_id)

