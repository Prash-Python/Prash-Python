# For loop demonstration.
countries_list = ['USA', 'Canada', 'Germany', 'France', 'Australia']
for country in countries_list:
    print(country)

for i in range(0, len(countries_list)):
    print(f"{i+1}: {countries_list[i]}")

# While loop demonstration.
count = 0
while count < len(countries_list):
    print(f"{count+1}: {countries_list[count]}")
    count += 1
else:
    print("All countries have been printed.")

# Pattern printing using nested loops.
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()  # Move to the next line after each row

for i in range(5, 0, -1):
    for j in range(i):
        print('#', end='')
    print()  # Move to the next line after each row

# Count the number of vowels in a given string.
def countVowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    print(f"Number of vowels in the given string: {count}")
    print(f"Number of consonants in the given string: {len(input_string) - count}")
countVowels(input("Enter a string: "))