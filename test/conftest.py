"""Pytest configuration file."""
import pytest
from source import shapes


@pytest.fixture
def rectangle():
    """Return rectangle fixture."""
    return shapes.Rectangle(2, 3)


@pytest.fixture
def other_rectangle():
    """Return other rectangle fixture."""
    return shapes.Rectangle(3, 3)
