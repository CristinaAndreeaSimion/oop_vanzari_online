
from person import Person

class Employee(Person):
    def __init__(self, name, email, address, password, salary):
        super().__init__(name, email, address, password)
        self.__salary = salary
        self._working_hours = 0

    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)

    def checkin(self):
        self._working_hours += 1

    def checkout(self):
        self._working_hours += 1

    def get_salary(self):
        return self.__salary

    def display_info(self):
        return f"Employee Name: {self.name}, Email: {self.get_email()}, Address: {self.get_address()},\
            Salary: {self.__salary}, Working Hours: {self._working_hours}"
