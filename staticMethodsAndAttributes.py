class Calculator:
    count = 0  # Static attribute to track the number of times add() is called

    @staticmethod
    def add(a, b):
        Calculator.count += 1  # Increment count each time add is called
        return a + b

# Demonstrate the use of static method and attribute
result1 = Calculator.add(5, 10)
print(f"Result of first addition: {result1}")
print(f"Add method called {Calculator.count} time(s)")

result2 = Calculator.add(15, 20)
print(f"Result of second addition: {result2}")
print(f"Add method called {Calculator.count} time(s)")
