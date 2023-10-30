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
