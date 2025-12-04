a = "Hello, how are you?"
b = "I am fine, thank you!"
print(a[0])  # First character of string a
print(b[5])  # Sixth character of string b
print(a[7:10])  # Substring from index 7 to 9 of string a
print(b[2:8])  # Substring from index 2 to 7 of string b
print(a + " " + b)  # Concatenation of strings a and b
print(a * 2)  # Repeat string a twice
print(len(a))  # Length of string a
print(len(b))  # Length of string b
print(a.lower())  # Convert string a to lowercase
print(b.upper())  # Convert string b to uppercase
print(b.replace("fine", "great"))  # Replace 'fine' with 'great' in string b
print(b.find("thank"))  # Find the index of substring 'thank' in string b
print(a[0:5:1])
print(b[::2])  # Slicing with step
print(a.strip())  # Remove leading and trailing whitespace from string a
print(a[::1])  # Full string with step 1
print(b[::-1])  # Reverse string b
my_string = "GeeksForGeeks"
print(f"Original String: {my_string}")
print("My name is {}".format(my_string))  # Using format() method to insert string into another string
print("Geeks" in my_string)  # Check if substring 'Geeks' is in the string
print("For" not in my_string)  # Check if substring 'For' is not in the string
print(my_string.startswith("Geeks"))  # Check if the string starts with 'Geeks'
print(my_string.endswith("Geeks"))  # Check if the string ends with 'Geeks'
print(my_string.isalpha())  # Check if all characters in the string are alphabetic
print(my_string.isdigit())  # Check if all characters in the string are digits
print(my_string.isalnum())  # Check if all characters in the string are alphanumeric
print(my_string.count("e"))  # Count occurrences of 'e' in the string
print(my_string.find("Geeks"))  # Find the index of substring 'Geeks' in the string
print(my_string.index("For"))  # Find the index of substring 'For' in the string
print(my_string.replace("For", "Example"))  # Replace 'For' with 'Example' in the string
my_string = my_string.capitalize() # Capitalize the string by capitalizing the first character
print(my_string)  # Print the capitalized string
print(my_string.swapcase())  # Swap case of the string
