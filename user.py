from person import Person

class User(Person):
    def __init__(self, name, email, address, password):
        super().__init__(name, email, address, password)
        self.phone = None
        self.shopping_history = {}

    def add_product(self, product, quantity):
        if product in self.shopping_history:
            self.shopping_history[product] += quantity
        else:
            self.shopping_history[product] = quantity

    def total_spent(self):
        return sum(product.get_price() * quantity for product, quantity in self.shopping_history.items())

    def display_info(self):
        return f"User Name: {self.name}, Email: {self.get_email()}, Phone: {self.phone}, Total Spent: {self.total_spent()}"
