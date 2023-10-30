"""This module contains the functions for the calculator."""


def add(number1: float | str, number2: float | str) -> float | str:
    """Add two numbers or strings together."""
    return number1 + number2


def divide(number1: float, number2: float) -> float:
    """Divide two numbers."""
    if number2 == 0:
        raise ValueError("Cannot divide by zero!")
    return number1 / number2
