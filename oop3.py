#Creating an Employee class with attributes name and salary.
#Creating a Payroll class that takes a list of Employee objects and calculates the total payroll.

# Define the Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Defining the Payroll class
class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, salary):
        # Adding Employee objects to the list
        self.employees.append(Employee(name, salary))

    def calculate_total_payroll(self):
        # Calculating the total payroll
        return sum(employee.salary for employee in self.employees if employee.salary > 0)

# Usage
payroll_system = Payroll()

# Adding employees
payroll_system.add_employee("Joseph", 1000)
payroll_system.add_employee("Habiba", 2000)
payroll_system.add_employee("Bob", 40000)

# Calculating total payroll
total_payroll = payroll_system.calculate_total_payroll()
print(f"Total Payroll: {total_payroll}")

# Displaying employee details
for employee in payroll_system.employees:
    print(f"{employee.name}: {employee.salary}")
