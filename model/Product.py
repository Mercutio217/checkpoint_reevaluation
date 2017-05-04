class Product:

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return "{} Description: {} Price: {}".format(self.name, self.description, self.price)

    