"""Pytest file for testing Rectangle Class in source.shapes."""


def test_rectangle_area(rectangle):
    """Test rectangle area calculation."""
    assert rectangle.area() == 6


def test_rectangle_perimeter(rectangle):
    """Test rectangle perimeter calculation."""
    assert rectangle.perimeter() == 10


def test_not_equal(rectangle, other_rectangle):
    """Test not equal."""
    assert rectangle != other_rectangle
