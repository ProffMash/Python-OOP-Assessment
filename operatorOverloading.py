class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Creating two Vector objects
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Adding the two vectors using the overloaded + operator
result = v1 + v2

# Displaying the result
print(result)  # Output: Vector(4, 6)
