def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def validate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number.")
    return True