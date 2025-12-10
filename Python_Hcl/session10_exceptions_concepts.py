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

    try:
        print(10 + "20")
    except TypeError as e:
        print(f"This is type error {e}")

catchTheException()

def handleTheException(number, text):
    if number < 0:
        print("Error, cannot provide negative values for square root...")
    else:
        val = math.sqrt(number)
        print(f"Square root value is: {val}")

    if text.isdigit() :
        a = int(text)
        print(a)
    else:
        print(f"Given text value is not valid...")

    x = int(input("Enter the Numerator: "))
    y = int(input("Enter the denominator: "))
    if y == 0:
        print(f"Cannot perform division by {y}")
    else:
        print(x/y)
handleTheException(9, "18")
# handleTheException(-1, "Python")

def exceptionWithElseBlock():
    # Exception might come here.
    try:
        val = 10/3
    # If exception came, it will come to except block and never goes to else block.
    except ZeroDivisionError as e:
        print(e)
    # If exception did not came, it will come to else block and never goes to except block.
    else:
        print(f"Result is {val}")
    # This block will essentially execute always.
    finally:
        print("Code Execution Done")
exceptionWithElseBlock()

# raise exceptions
def raiseNamedException():
    val = 3500
    if val > 3000:
        # ValueError below is pre defined and hence named exception.
        raise ValueError("Enter value <= 3000...")
    else:
        print(val)
raiseNamedException()
