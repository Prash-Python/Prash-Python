# Exercise 2: Electricity Bill Calculation
# Write a function to calculate the electricity bill based on the following criteria:
def generateElectricityBill(units_consumed):
    print("Calculating electricity bill...")
    if units_consumed <= 100:
        bill_amount = units_consumed * 5
    elif units_consumed <= 200:
        bill_amount = (100 * 5) + ((units_consumed - 100) * 7)
    else:
        bill_amount = (100 * 5) + (100 * 7) + ((units_consumed - 200) * 10)
    bill_amount += fixed_charge
    print(f"Total electricity bill for {units_consumed} units is: {bill_amount} currency units")
fixed_charge = 100.0
generateElectricityBill(float(input("Enter units consumed: ")))

# Use match case to determine if the given character is a vowel or consonant.
def checkVowelOrConsonant(character):
    print("Checking if the character is a vowel or consonant...")
    match character.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print(f"{character} is a Vowel")
        case _:
            print(f"{character} is a Consonant")
checkVowelOrConsonant(input("Enter a character: "))

# Use match case to create a simple calculator that performs addition, subtraction, multiplication, or division based on user input.
def simpleCalculator(num1, num2, operation):
    print("Performing calculation...")
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        case '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        case '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please choose from +, -, *, /.")

simpleCalculator(float(input("Enter first number: ")), float(input("Enter second number: ")), input("Enter operation (+, -, *, /): "))