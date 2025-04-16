
class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price  # Privat
        self.quantity = quantity
        self._description = description  # Protejat

    def check_quantity(self):
        return self.quantity > 10

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price
