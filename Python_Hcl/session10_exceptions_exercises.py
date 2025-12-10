# Exercise 1: Define an exception if the input age is less than the voting age.
def defineException(age):
    if age < 18:
        raise ValueError(f"Entered Age {age} cannot be less than voting age")
    else:
        print(f"Eligible to vote for provided age: {age}")
defineException(int(input("Enter the age: ")))

# 1. Ask the user to input an integer. If they enter a string or invalid number, handle the exception and ask again.
def integer_check(number):
    while number.isdigit() :
        print(number)
        break
    else:
        number = input("Enter the number again: ")
        # Call recursively.
        integer_check(number)
integer_check(input("Enter a valid integer value: "))

# 2. Write a function that takes a list of numbers and returns the reciprocal of each number. Handle division by zero.
def integer_check_again(given_number_list):
    my_list = []
    try:
        for item in given_number_list:
            # if item != 0:
            my_list.append(1/item)
    except ZeroDivisionError as e:
        print(f"Do not provide 0 in your values list. Got division by zero exception...{e}")
    else:
        print(f"Reciprocals items list {my_list}")
    finally:
        print("Program is executed...")
given_list = [1,2,3,4,5,6,0]
integer_check_again(given_list)

"""Create a program that simulates a bank account.
Raise a custom exception InsufficientFundsError if withdrawal > balance.
Handle it gracefully by printing an error message.
"""
class InsufficientFundsError(Exception):
    pass

def bank_account_simulation(balance_amount, withdrawal_amount):
    if balance_amount < withdrawal_amount:
        raise InsufficientFundsError("Your balance is lower than the withdrawal amount...")
bank_account_simulation(int(input("Enter balance amount: ")), int(input("Enter withdrawal amount: ")))



