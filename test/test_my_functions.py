"""
This file contains the tests for the functions in my_functions.py
"""
import time
import pytest
from source import my_functions


def test_add():
    """Test that the add function works as expected"""
    result = my_functions.add(1, 2)
    assert result == 3


def test_add_strings():
    """Test that the add function works as expected with strings"""
    result = my_functions.add("Hello", "World")
    assert result == "HelloWorld"


def test_divide():
    """Test that the divide function works as expected"""
    result = my_functions.divide(1, 2)
    assert result == 0.5


def test_divide_by_zero():
    """Test that the divide function raises a ValueError when dividing by zero"""
    with pytest.raises(ValueError):
        my_functions.divide(1, 0)


@pytest.mark.slowtest
def test_very_slow():
    """Test that the divide function works as expected, slowed down"""
    time.sleep(5)
    assert my_functions.divide(1, 2) == 0.5


@pytest.mark.skip(reason="This feature is currently broken")
def test_add_skipped():
    """Test that the add function works as expected, but currently skipped"""
    assert my_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="We know we can't divide by zero")
def test_divide_zero_broken():
    """Test that the divide function raises a ValueError when dividing by zero, example of xfail"""
    my_functions.divide(3, 0)
