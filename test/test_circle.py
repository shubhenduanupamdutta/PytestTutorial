"""Test circle shape."""
import pytest
from source import shapes


class TestCircle:
    """Test circle shape."""

    def setup_method(self, method):
        """Create circle object."""
        print(f"\nSetting up method {method.__name__}...")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        """Delete circle object."""
        print(f"\nTearing down method {method.__name__}...")
        del self.circle

    def test_area(self):
        """Test area calculation."""
        assert self.circle.area() == pytest.approx(314.159, 0.01)

    def test_perimeter(self):
        """Test perimeter calculation."""
        assert self.circle.perimeter() == pytest.approx(62.8318, 0.01)
