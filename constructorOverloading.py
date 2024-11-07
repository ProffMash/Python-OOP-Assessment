class Rectangle:
    def __init__(self, length, width=None):
        if width is None:
            # If width is not provided, we assume it's a square
            self.length = length
            self.width = length
        else:
            # Otherwise, we use the provided length and width
            self.length = length
            self.width = width

    def calculate_area(self):
        return self.length * self.width

# Test cases:
# 1. Creating a square with side length 5
square = Rectangle(5)
print(f"Square area: {square.calculate_area()}")  # Output: 25

# 2. Creating a rectangle with length 4 and width 6
rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.calculate_area()}")  # Output: 24
