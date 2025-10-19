import math

class Shape:
    def area(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area() to calculate rectangle area."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Override area() to calculate circle area."""
        return math.pi * (self.radius ** 2)