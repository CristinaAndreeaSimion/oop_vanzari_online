
from employee import Employee

class ContractEmployee(Employee):
    def __init__(self, name, email, address, password, salary, contract_expiry):
        super().__init__(name, email, address, password, salary)
        self.contract_expiry = contract_expiry

    def display_info(self):
        return f"Contract Employee Name: {self.name}, Email: {self.get_email()}, Address: {self.get_address()}, Salary: {self.get_salary()}, Contract Expiry: {self.contract_expiry}"
