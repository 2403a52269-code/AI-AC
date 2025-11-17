"""
This module provides basic calculator functions: addition, subtraction,
multiplication, and division. It demonstrates structured documentation
using NumPy Style docstrings.
"""
def add(a: float, b: float) -> float:
    """
    Add two numbers.
    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.
    Returns
    -------
    float
        The sum of a and b.
    """
    return a + b
def subtract(a: float, b: float) -> float:
    """
    Subtract one number from another.
    Parameters
    ----------
    a : float
        The number from which to subtract.
    b : float
        The number to subtract.
    Returns
    -------
    float
        The result of a - b.
    """
    return a - b
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    Parameters
    ----------
    a : float
        The first number.
    b : float
        The second number.
    Returns
    -------
    float
        The product of a and b.
    """
    return a * b
def divide(a: float, b: float) -> float:
    """
    Divide one number by another.
    Parameters
    ----------
    a : float
        The dividend.
    b : float
        The divisor (must not be zero).
    Returns
    -------
    float
        The result of a / b.
    Raises
    ------
    ZeroDivisionError
        If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
def main():
    """
    Run an interactive calculator that takes user input.
    This function prompts the user to enter two numbers and choose an
    arithmetic operation (add, subtract, multiply, divide). It then
    performs the calculation using the corresponding function and prints
    the result.
    Notes
    -----
    - Input values are converted to floats.
    - Division by zero is handled gracefully with an error message.
    """
    print("Basic Calculator")
    print("Available operations: add, subtract, multiply, divide")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation: ").strip().lower()
    if operation == "add":
        print("Result:", add(a, b))
    elif operation == "subtract":
        print("Result:", subtract(a, b))
    elif operation == "multiply":
        print("Result:", multiply(a, b))
    elif operation == "divide":
        try:
            print("Result:", divide(a, b))
        except ZeroDivisionError as e:
            print("Error:", e)
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, divide.")
if __name__ == "__main__":
    main()
