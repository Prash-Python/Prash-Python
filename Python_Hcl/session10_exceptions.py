import math
def catchTheException():
    try:
        a = math.sqrt(9)
        print(a)
        b = math.sqrt(-4)
        print(b)
    except ValueError as ve:
        print(f"Caught an exception: {ve}")

    try:
        val = int("Python")
        print(val)
    except ValueError as e:
        print(f"Again caught an exception: {e}")

    try:
        a = 10/0
        print(a)
    except ZeroDivisionError as z:
        print(f"Division by zero operation: {z}")
catchTheException()