my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
my_string = "Python Slicing Example"
print(len(my_list))  # Print the length of the list
print(len(my_string))  # Print the length of the string
print(my_list[0])  # First element of the list
print(my_string[7])  # Eighth character of the string
print(my_list[2:5])  # Sublist from index 2 to 4
print(my_string[0:6])  # Substring from index 0 to 5
print(my_list + [120, 130])  # Concatenation of lists
print(my_string * 2)  # Repeat string twice
print(len(my_list))  # Length of the list
print(len(my_string))  # Length of the string
print(my_string.lower())  # Convert string to lowercase
print(my_string.upper())  # Convert string to uppercase
print(id(my_string))  # Print the memory address of the string before modification
print(my_string.replace("Example", "Demo"))  # Replace 'Example' with 'Demo' in the string
print(id(my_string))  # Print the memory address of the string after modification
print(my_string.find("Slicing"))  # Find the index of substring 'Slicing' in the string
print(my_list[0:10:2])  # Slicing with step
print(my_string.strip())  # Remove leading and trailing whitespace from the string
print(my_string[::1])  # Full string with step 1
print(my_string[::3])  # Slicing with step 3
print(my_list[::-1])  # Reverse the list
print(my_string[::-1])  # Reverse the string
print(my_list[-2:-9:-1])
print(my_string[-2:-9:-1])
my_list.reverse()
print(my_list)  # Print the reversed list
my_string = my_string.capitalize() # Capitalize the string by capitalizing the first character
print(my_string)  # Print the capitalized string
print(my_string.swapcase())  # Swap case of the string
print(my_string.count("e"))  # Count occurrences of 'e' in the string
print(my_string.replace("Demo", "Example"))  # Replace 'Demo' back with 'Example' in the string
del my_list
del my_string  # Delete the list and string variables
