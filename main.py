

from product import Product
from employee import Employee
from contract_employee import ContractEmployee
from freelancer import Freelancer
from standard_user import StandardUser

products = [
    Product("Laptop", 2500.0, 15, "Laptop gaming"),
    Product("Mouse", 100.0, 150, "Mouse wireless"),
    Product("Tastatura", 300.0, 5, "Clavier mecanic RGB"),
]

employees = [
    Employee("Stancu Adrian", "stancu.adrian@email.com", "Bucuresti", "password123", 3000.0),
    ContractEmployee("Alice Smith", "alice.smith@email.com", "Cluj", "password321", 3500.0, "2025-12-31"),
    Freelancer("George Popescu", "george.popescu@email.com", "Timisoara", "pass123", 2000.0, 5),
]

users = [
    StandardUser("Maria Popescu", "maria@email.com", "Timisoara", "pass123"),
]

user = users[0]
if user.check_email():
    print(f"{user.name} are un email valid.")

if user.check_login("maria@email.com", "pass123"):
    print(f"Utilizatorul {user.name} este autentificat.")
else:
    print("Eroare la autentificare.")

user.add_product(products[0], 2)
user.add_product(products[1], 1)

print(f"Total cheltuit de {user.name}: {user.total_spent()}")

print(user.display_info())


for employee in employees:
    employee.checkin()
    employee.checkout()

for employee in employees:
    print(employee.display_info())


max_hours_employee = max(employees, key=lambda emp: emp._working_hours)
print(f"Angajatul cu cele mai multe ore de lucru este {max_hours_employee.name}.")

max_hours_employee.increase_salary(50)
print(max_hours_employee.display_info())
