
from employee import Employee

class Freelancer(Employee):
    def __init__(self, name, email, address, password, salary, num_projects):
        super().__init__(name, email, address, password, salary)
        self.num_projects = num_projects

    def display_info(self):
        return f"Freelancer Name: {self.name}, Email: {self.get_email()}, Address: {self.get_address()},\
            Salary: {self.get_salary()}, Projects: {self.num_projects}"
