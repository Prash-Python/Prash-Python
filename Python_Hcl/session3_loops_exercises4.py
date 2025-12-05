# Question 5: Calculate the factorial of a number.
def calculateFactorial(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial *= i
    print(f"Factorial of {number} is {factorial}")
calculateFactorial(int(input("Enter a number to calculate its factorial: ")))

# Question 1: Find all divisors of a number.
def divisorsOfNumber(number):
    print(f"Divisors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
divisorsOfNumber(int(input("Enter a number to find its divisors: ")))

# Question 3: Print numbers from 1 to 100 with specific conditions.
def printConditionalOutput():
    for i in range(1, 101, 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
printConditionalOutput()


# Question 4: Find numbers between 1000 and 2000 divisible by 7 but not by 5.
def findNumbers():
    for i in range(1000, 2001, 1):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
findNumbers()

# Question 2: Determine if a number is prime.
def determinePrimeNumbers(number):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                print(f"{number} is not a prime number.")
                return
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
determinePrimeNumbers(int(input("Enter a number to check if it is prime: ")))

# Question 6: Count the number of vowels in a given string.
def countVowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    print(f"Number of vowels in the given string: {count}")
    print(f"Number of consonants in the given string: {len(input_string) - count}")

# Question 7: Find all palindrome numbers between 1 and 1000.
def isPalindrome():
    count = 0
    for num in range(1, 1001, 1):
        if str(num) == str(num)[::-1]:
            print(f"{num} is a palindrome.")
            count += 1
    print(f"Total palindrome numbers between 1 and 1000: {count}")
isPalindrome()

# Question 8: Check if a number is an Armstrong number.
def isArmstrongNumber(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_powers == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
isArmstrongNumber(int(input("Enter a number to check if it is an Armstrong number: ")))

# Question 9: Generate Diamond Pattern.
def printDiamondPattern(n):
    # Upper part of diamond
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # Lower part of diamond
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
printDiamondPattern(5)

