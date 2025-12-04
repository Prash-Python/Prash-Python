# This function checks if a person is eligible to vote based on their age.
def canVote(age):
    if age >= 18:
        return True
    else:
        return False
input_age = int(input("Enter your age: "))
print("Can vote:", canVote(input_age))

# This function categorizes a number as positive, negative, or zero.
def categorizeNumber(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
input_number = float(input("Enter a number: "))
print("The number is:", categorizeNumber(input_number))

# Calcualte the salary based on bonus eligibility
def calculateSalary(base_salary):
    if base_salary >= 50000:
        base_salary = (base_salary * 1.30)
    else:
        base_salary = (base_salary * 1.20)
    return base_salary
input_salary = float(input("Enter your base salary: "))
print("Total Salary:", calculateSalary(input_salary))

# Determine if the given year is a leap year
def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
input_year = int(input("Enter a year: "))
if isLeapYear(input_year):
    print(f"{input_year} is a leap year.")
else:
    print(f"{input_year} is not a leap year.")

# Determine the grade based on the score
def determineGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
input_score = float(input("Enter your score: "))
print("Your grade is:", determineGrade(input_score))

# Check if a number is even or odd
def isEvenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
input_number = int(input("Enter a number: "))
print(f"The number is: {isEvenOrOdd(input_number)}")

# Find the largest of three numbers
def findLargest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
input_a = float(input("Enter the first number: "))
input_b = float(input("Enter the second number: "))
input_c = float(input("Enter the third number: "))
print("The largest number is:", int(findLargest(input_a, input_b, input_c)))