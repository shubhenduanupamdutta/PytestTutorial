"""Parameterized tests for the Square class."""
import pytest
from source import shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (10, 100), (0.5, 0.25), (9, 81)])
def test_multiple_square_area(side_length, expected_area):
    """Test area calculation for squares."""
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (10, 40), (0.5, 2), (9, 36)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    """Test perimeter calculation for squares."""
    assert shapes.Square(side_length).perimeter() == expected_perimeter
