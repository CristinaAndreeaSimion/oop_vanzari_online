
from user import User

class StandardUser(User):
    def __init__(self, name, email, address, password):
        super().__init__(name, email, address, password)

    def calculate_discount(self):
        if self.total_spent() > 10000:
            return 0.10  # 10% discount
        return 0.05  # 5% discount

    def display_info(self):
        discount = self.calculate_discount()
        return f"Standard User Name: {self.name}, Email: {self.get_email()}, Total Spent: {self.total_spent()}, Discount: {discount * 100}%"
