from controller.DB_controller import DBController


class Product_Controller:

    def __init__(self):
        my_database = DBController()
        self.database = my_database.get_connection()
        self.product_list = my_database.get_all()

    def get_product_list(self):
        return self.product_list