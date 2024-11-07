from abc import ABC, abstractmethod
import math

# Abstracting base class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass Square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Creating instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Calling area() on each
print(f"Area of Circle: {circle.area()}")  # Output: Area of Circle
print(f"Area of Square: {square.area()}")  # Output: Area of Square
