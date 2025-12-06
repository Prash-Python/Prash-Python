# Password checker.
def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check for lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check for digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check for special character
    special_characters = "!@#$%^&*()-+"
    if not any(char in special_characters for char in password):
        return False
    
    return True
password = input("Enter a password to check its validity: ")
if is_valid_password(password):
    print("The password is valid.")
else:
    print("The password is invalid.")

# Find mumber of vowels, consonants, white spaces, numbers, and special characters in a given string.
def countStringComponents(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    whitespace_count = 0
    digit_count = 0
    special_char_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char.isspace():
            whitespace_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_char_count += 1

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"White spaces: {whitespace_count}")
    print(f"Digits: {digit_count}")
    print(f"Special characters: {special_char_count}")

input_string = input("Enter a string to analyze: ")
countStringComponents(input_string)

# Calculate the sum of digits in a given string.
def sum_of_digits(input_string):
    digits = ""
    for char in input_string:
        if char.isdigit():
            digits += char
    if digits == "":
        total = 0
    else:
        total = int(digits)
    final_sum = total + num
    print(f"The sum of digits {total} and {num} is: {final_sum}")
text = input("Enter a string containing digits to sum: ")
num = int(input("Enter a number to add to the sum of digits: "))
sum_of_digits(text)