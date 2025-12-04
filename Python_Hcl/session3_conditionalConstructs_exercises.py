# Exercise 1: Given the number of years, calculate the equivalent duration in months, weeks, days, hours, minutes, and seconds.
# def calculateDuration(number_of_years):
#     print("Calculating duration in months, weeks, days, hours, minutes, and seconds...")
#     estimated_leap_years = number_of_years // 4
#     estimated_non_leap_years = number_of_years - estimated_leap_years
#     total_days = (estimated_non_leap_years * 365) + (estimated_leap_years * 366)
#     number_of_months = number_of_years * 12
#     number_of_weeks = number_of_years * 52
#     number_of_days = total_days
#     number_of_hours = number_of_days * 24
#     number_of_minutes = number_of_hours * 60
#     number_of_seconds = number_of_minutes * 60
#     print(f"Months: {number_of_months}, Weeks: {number_of_weeks}, Days: {number_of_days}, Hours: {number_of_hours}, Minutes: {number_of_minutes}, Seconds: {number_of_seconds}")
# calculateDuration(float(input("Enter number of years: ")))

# Exercise 2: Obtain temperature of 7 days from the user and calculate the average temperature of the week.
# for daily_temp in range(1, 8):
#     temp = float(input(f"Enter temperature for day {daily_temp}: "))
#     if daily_temp == 1:
#         total_temp = temp
#     else:
#         total_temp += temp
# average_temp = total_temp / 7
# print(f"The average temperature of the week is: {average_temp}")

# Exercise 3: Get a number from the user and determine if it is even or odd.
# number = int(input("Enter a number: "))
# def isEvenOrOdd(number):
#     if number % 2 == 0:
#         print(f"The number {number} is even.")
#     else:
#         print(f"The number {number} is odd.")
# isEvenOrOdd(number)

# Exercise 4: Get a number from the user and determine if it is positive, negative, or zero.
# number = float(input("Enter a number: "))
# def checkNumberSign(number):
#     if number > 0:
#         print(f"The number {number} is positive.")
#     elif number < 0:
#         print(f"The number {number} is negative.")
#     else:
#         print("The number is zero.")
# checkNumberSign(number)

# Exercise 5: Get three numbers from the user and determine the largest among them.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# def findLargest(num1, num2, num3):
#     if (num1 >= num2) and (num1 >= num3):
#         print(f"The largest number is {num1}")
#     elif (num2 >= num1) and (num2 >= num3):
#         print(f"The largest number is {num2}")
#     else:
#         print(f"The largest number is {num3}")
# findLargest(num1, num2, num3)

# Exercise 6: Print if a given number is a multiple of 3, 5, or both.
number = int(input("Enter a number: "))
def checkMultiple(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print(f"The number {number} is a multiple of both 3 and 5.")
    elif number % 3 == 0:
        print(f"The number {number} is a multiple of 3.")
    elif number % 5 == 0:
        print(f"The number {number} is a multiple of 5.")
    else:
        print(f"The number {number} is not a multiple of 3 or 5.") 
checkMultiple(number)

# Exercise 7: Get a character from the user and determine if it is a vowel or consonant.
char = input("Enter a character: ").lower()
def checkVowelOrConsonant(char):
    if char in 'aeiou':
        print(f"The character '{char}' is a vowel.")
    elif char.isalpha():
        print(f"The character '{char}' is a consonant.")
    else:
        print("Please enter a valid alphabet character.")
checkVowelOrConsonant(char)

# Exercise 8: Print if a given number is prime or not.
number = int(input("Enter a number: "))
def checkPrime(number):
    if number <= 1:
        print(f"The number {number} is not prime.")
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"The number {number} is not prime.")
            return
    print(f"The number {number} is prime.")
checkPrime(number)