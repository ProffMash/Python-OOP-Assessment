class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Calling the display_info() method to print out the car's details
my_car.display_info()
