class Employee:
    def calculate_salary(self):
        print("Calculating generic employee salary...")

class Manager(Employee):
    def calculate_salary(self):
        # Overriding to provide specific salary calculation for a manager
        print("Calculating manager's salary with additional benefits and bonuses...")

# method overriding
generic_employee = Employee()
generic_employee.calculate_salary()  # Calling the method from Employee

manager = Manager()
manager.calculate_salary()  # Calling the overridden method from Manager
