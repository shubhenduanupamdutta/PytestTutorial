"""Generic shapes and their properties."""

import math


class Shape:
    """Generic shape."""

    def area(self):
        """Calculate area of shape."""

    def perimeter(self):
        """Calculate perimeter of shape."""


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, length: float, width: float):
        self.length: float = length
        self.width: float = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.length == other.length and self.width == other.width

    def area(self) -> float:
        """Calculate area of rectangle."""
        return self.length * self.width

    def perimeter(self) -> float:
        """Calculate perimeter of rectangle."""
        return 2 * (self.length + self.width)


class Square(Rectangle):
    """Square shape."""

    def __init__(self, length: float):
        super().__init__(length, length)
