def add(a, b):
    """Return the sum of a and b."""
    return a + b
def subtract(a, b):
    """Return the difference of a and b."""
    return a - b
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
def divide(a, b):
    """Return the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    """Return a raised to the power of b."""
    if b == 0:
        return 1
    return a ** b
def modulus(a, b):
    """Return the modulus of a and b."""
    return a % b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Addition: {a} + {b} = {add(a, b)}")
print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
try:
    print(f"Division: {a} / {b} = {divide(a, b)}")
except ValueError as e:
    print(e)
print(f"Power: {a} ^ {b} = {power(a, b)}")
print(f"Modulus: {a} % {b} = {modulus(a, b)}")